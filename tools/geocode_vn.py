# -*- coding: utf-8 -*-
"""geocode_vn.py — TỰ ĐỘNG LẤY TOẠ ĐỘ CHUẨN cho các điểm Việt Nam bằng tìm kiếm tiếng Việt.

Ý tưởng (đúng như yêu cầu):
  - Tìm kiếm mỗi địa điểm bằng TÊN TIẾNG VIỆT + tỉnh + "Việt Nam" trên dịch vụ geocoding
    OpenStreetMap/Nominatim (miễn phí, không cần API key, dữ liệu WGS84 như Google).
  - CHỈ tự động cập nhật khi có ĐÚNG 1 kết quả khớp trong đúng tỉnh và tên khớp (so khớp cho chuẩn).
  - Trường hợp nhiều kết quả / không khớp tỉnh / không khớp tên  ->  ghi ra file review để soi tay.
  - Luôn ghi log cũ→mới + khoảng lệch để anh kiểm chứng.

CÁCH CHẠY (trên máy có mạng — KHÔNG chạy trong sandbox):
  python3 tools/geocode_vn.py            # DRY-RUN: chỉ dò + ghi _sync/geocode_review.csv, KHÔNG sửa gì
  python3 tools/geocode_vn.py --apply    # Áp dụng các điểm 'update' tin cậy rồi build lại
  python3 tools/geocode_vn.py --limit 30 # thử 30 điểm đầu cho nhanh

Lưu ý lịch sự với Nominatim: tự động nghỉ ~1.1s/lần (đúng chính sách 1 request/giây).
Có cache _sync/geocode_cache.json để chạy lại không phải dò lại từ đầu.
"""
import json, os, glob, csv, time, re, sys, math, unicodedata
import urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
REG = os.path.join(ROOT, "data", "regions")
SYNC = os.path.join(ROOT, "_sync"); os.makedirs(SYNC, exist_ok=True)
CACHE = os.path.join(SYNC, "geocode_cache.json")
REVIEW = os.path.join(SYNC, "geocode_review.csv")
NOMINATIM = "https://nominatim.openstreetmap.org/search"
UA = "camnangdulich-geocoder/1.0 (lopmaybay@gmail.com)"
SLEEP = 1.1
MOVE_THRESHOLD_M = 150     # chỉ đề xuất đổi khi lệch > 150m so với toạ độ hiện tại
APPLY = "--apply" in sys.argv
LIMIT = None
for i, a in enumerate(sys.argv):
    if a == "--limit" and i + 1 < len(sys.argv): LIMIT = int(sys.argv[i + 1])

STOP = set("va và của the ở tại khu di tích đền chùa nhà thờ núi hồ thác đảo bãi vịnh thành phố tỉnh vietnam việt nam".split())

def strip_d(s):
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("đ", "d").replace("Đ", "D").lower().strip()

def norm_prov(s):
    s = strip_d(s)
    for pre in ["thanh pho ", "tinh ", "tp. ", "tp ", "dac khu "]:
        if s.startswith(pre): s = s[len(pre):]
    return s.strip()

def haversine_m(a, b, c, d):
    R = 6371000; p = math.radians
    x = math.sin(p(c - a) / 2) ** 2 + math.cos(p(a)) * math.cos(p(c)) * math.sin(p(d - b) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(x))

def geocode(q):
    params = {"q": q, "format": "jsonv2", "countrycodes": "vn", "limit": 5,
              "addressdetails": 1, "accept-language": "vi"}
    url = NOMINATIM + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r)

# Sáp nhập tỉnh 2025: tên tỉnh MỚI -> các tên tỉnh CŨ đã gộp vào (OSM có thể còn dùng tên cũ)
MERGER = {
    "hai phong": ["hai duong"], "hung yen": ["thai binh"], "ninh binh": ["nam dinh", "ha nam"],
    "phu tho": ["vinh phuc", "hoa binh"], "bac ninh": ["bac giang"], "tuyen quang": ["ha giang"],
    "lao cai": ["yen bai"], "thai nguyen": ["bac kan"], "quang tri": ["quang binh"],
    "da nang": ["quang nam"], "quang ngai": ["kon tum"], "gia lai": ["binh dinh"],
    "dak lak": ["phu yen"], "khanh hoa": ["ninh thuan"], "lam dong": ["dak nong", "binh thuan"],
    "dong nai": ["binh phuoc"], "ho chi minh": ["ba ria", "vung tau", "binh duong"],
    "tay ninh": ["long an"], "dong thap": ["tien giang"], "vinh long": ["ben tre", "tra vinh"],
    "an giang": ["kien giang"], "can tho": ["soc trang", "hau giang"], "ca mau": ["bac lieu"],
    "hue": ["thua thien"],
}

def province_ok(result, region_name_vi):
    target = norm_prov(region_name_vi)
    if not target: return False
    hay = strip_d(result.get("display_name", ""))
    addr = result.get("address", {}) or {}
    hay += " " + " ".join(strip_d(str(v)) for v in addr.values())
    names = [target] + MERGER.get(target, [])
    return any(nm in hay for nm in names)

def name_ok(result, name_vi):
    words = [w for w in strip_d(name_vi).split() if len(w) >= 3 and w not in STOP]
    if not words: return True
    hay = strip_d(result.get("display_name", ""))
    hits = sum(1 for w in words if w in hay)
    return hits >= 1

def decide(place, results):
    """Chỉ tự sửa khi kết quả ĐÁNG TIN: đúng tên VÀ (đúng tỉnh HOẶC nằm trong ~40km điểm cũ).
    Điểm cũ đa số đã đúng tỉnh, nên bán kính 40km chặn việc ghép nhầm sang nơi CÙNG TÊN ở tỉnh khác
    (vd 'Bảo tàng Mỹ thuật TP.HCM' bị ghép sang bảo tàng ở Hà Nội). Có bảng alias sáp nhập tỉnh 2025."""
    cur = place["coordinates"]; clat, clon = cur["lat"], cur["lon"]
    if not results:
        return ("no_result", None, None, "")
    def cand(r): return float(r["lat"]), float(r["lon"]), r.get("display_name", "")
    def trusted(r):
        if not name_ok(r, place.get("name_vi", "")): return False
        nlat, nlon, _ = cand(r)
        near = haversine_m(clat, clon, nlat, nlon) <= 40000
        return province_ok(r, place.get("region_name_vi", "")) or near
    good = [r for r in results if trusted(r)]
    if len(good) == 1:
        nlat, nlon, disp = cand(good[0]); dist = haversine_m(clat, clon, nlat, nlon)
        return ("update" if dist > MOVE_THRESHOLD_M else "ok_close", (nlat, nlon), dist, disp)
    if len(good) >= 2:
        nlat, nlon, disp = cand(good[0])
        return ("review_multi", (nlat, nlon), haversine_m(clat, clon, nlat, nlon), disp)
    # có kết quả nhưng không cái nào vừa khớp tên vừa (đúng tỉnh/gần) -> soi tay, KHÔNG tự sửa
    nlat, nlon, disp = cand(results[0])
    return ("review_far", (nlat, nlon), haversine_m(clat, clon, nlat, nlon), disp)

def main():
    files = {f: json.load(open(f, encoding="utf-8")) for f in glob.glob(os.path.join(REG, "vn-*.json"))}
    places = []
    for f, arr in files.items():
        for p in arr: places.append((f, p))
    if LIMIT: places = places[:LIMIT]
    cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
    rows = []; updates = {}; n_upd = 0; n_rev = 0
    print(f"Dò {len(places)} điểm Việt Nam qua Nominatim (tiếng Việt)…")
    for i, (f, p) in enumerate(places, 1):
        q = f'{p.get("name_vi","")}, {p.get("region_name_vi","")}, Việt Nam'
        key = p["slug"]
        if key in cache:
            results = cache[key]
        else:
            try:
                results = geocode(q); cache[key] = results
                time.sleep(SLEEP)
            except Exception as e:
                results = []; print(f"  ! lỗi dò {key}: {e}")
            if i % 25 == 0:
                json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
                print(f"  … {i}/{len(places)}")
        action, coord, dist, disp = decide(p, results)
        cur = p["coordinates"]
        rows.append([p["slug"], p.get("name_vi", ""), p.get("region_name_vi", ""),
                     cur["lat"], cur["lon"],
                     coord[0] if coord else "", coord[1] if coord else "",
                     round(dist) if dist is not None else "", len(results), action, disp[:80]])
        if action == "update":
            updates.setdefault(f, []).append((p["slug"], coord)); n_upd += 1
        elif action.startswith("review"):
            n_rev += 1
    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
    with open(REVIEW, "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.writer(fp)
        w.writerow(["slug", "name_vi", "tinh", "lat_cu", "lon_cu", "lat_moi", "lon_moi",
                    "lech_m", "so_ket_qua", "hanh_dong", "ket_qua_google/osm"])
        w.writerows(rows)
    print(f"\nTóm tắt: cần cập nhật (update)={n_upd} | cần soi tay (review)={n_rev} | tổng={len(rows)}")
    print(f"Đã ghi bảng soi: {REVIEW}")
    if APPLY and updates:
        undo = []
        for f, lst in updates.items():
            arr = files[f]; by = {x["slug"]: x for x in arr}
            for slug, (nlat, nlon) in lst:
                if slug in by:
                    oc = by[slug].get("coordinates", {}) or {}
                    undo.append([slug, oc.get("lat"), oc.get("lon"), round(nlat, 6), round(nlon, 6)])
                    by[slug]["coordinates"] = {"lat": round(nlat, 6), "lon": round(nlon, 6)}
                    m = by[slug].get("maps") or {}
                    if isinstance(m.get("yandex"), str) and "&ll=" in m["yandex"]:
                        m["yandex"] = m["yandex"].split("&ll=")[0] + f"&ll={round(nlon,6)},{round(nlat,6)}&z=17"
            json.dump(arr, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        with open(os.path.join(SYNC, "geocode_undo.csv"), "w", encoding="utf-8-sig", newline="") as uf:
            w = csv.writer(uf); w.writerow(["slug", "lat_cu", "lon_cu", "lat_moi", "lon_moi"]); w.writerows(undo)
        print(f"ĐÃ ÁP DỤNG {n_upd} điểm. (log hoàn tác: _sync/geocode_undo.csv) Đang build lại…")
        os.system(f'cd "{ROOT}" && "{sys.executable}" tools/build.py')
    elif updates:
        print("(DRY-RUN) Chưa sửa gì. Xem file review rồi chạy lại với --apply để áp dụng.")

if __name__ == "__main__":
    main()
