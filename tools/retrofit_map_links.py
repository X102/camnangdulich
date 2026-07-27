# -*- coding: utf-8 -*-
"""retrofit_map_links.py — Chuyển TẤT CẢ link bản đồ sang dạng TRỎ-ĐỊA-ĐIỂM.

Trước đây maps.yandex chỉ thả ghim toạ độ (pt=lon,lat) nên khi toạ độ lệch vài
trăm mét là ghim rơi lệch, lại KHÔNG mở thẻ địa điểm để đọc bình luận/thông tin.
Nay MỌI link đều TRỎ THẲNG tới thẻ địa điểm:
  - Google: tìm theo TÊN + vùng + quốc gia -> mở đúng trang địa điểm (review, ảnh).
  - Yandex (Nga): tìm theo TÊN NGA (name_ru) + canh giữa theo toạ độ (ll), z=16.
  - Yandex (Việt Nam): dùng TÊN Latinh/địa phương (tên Nga hầu như không khớp POI
            Việt Nam) + canh giữa toạ độ THẬT, z=17 -> mở thẻ địa điểm, không lệch xa.
Toạ độ trong 'coordinates' GIỮ NGUYÊN (dùng cho bản đồ nội bộ/GIS).

Chạy:  python3 tools/retrofit_map_links.py
"""
import json, os, glob, re, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")

# Tên vùng tiếng Nga cho phần định vị của link Yandex (các vùng ưu tiên).
RU_LOC = {
    "moscow": "Москва",
    "saint-petersburg": "Санкт-Петербург",
    "moscow-oblast": "Московская область",
    "leningrad-oblast": "Ленинградская область",
}


def pretty_en(region_slug):
    base = region_slug[3:] if region_slug.startswith("vn-") else region_slug
    return base.replace("-", " ").title()


def is_vn(rec, region_slug):
    return (rec.get("country") == "vietnam") or region_slug.startswith("vn-")


def clean_name(name):
    """Bỏ phần phiên âm trong ngoặc / bổ nghĩa để truy vấn bản đồ khớp POI hơn."""
    name = re.sub(r"\s*\(.*?\)\s*", " ", name or "")
    name = name.split(" (")[0]
    return re.sub(r"\s+", " ", name).strip()


def build_maps(rec, region_slug):
    lat = rec["coordinates"]["lat"]
    lon = rec["coordinates"]["lon"]
    name_ru = (rec.get("name_ru") or "").strip()
    name_en = (rec.get("name_en") or "").strip()
    name_vi = (rec.get("name_vi") or "").strip()
    reg_en = pretty_en(region_slug)
    vn = is_vn(rec, region_slug)
    country_en = "Vietnam" if vn else "Russia"

    if vn:
        # VIỆT NAM: link TRỎ THẲNG tới thẻ địa điểm (đọc được bình luận/thông tin).
        # Dùng tên Latinh/địa phương (tên Nga hầu như không khớp POI Việt Nam),
        # canh giữa theo toạ độ THẬT + zoom cao nên không mở lệch xa.
        gname = clean_name(name_en or name_vi or name_ru)
        gparts = [gname] + ([reg_en] if reg_en.lower() not in gname.lower() else []) + [country_en]
        google = "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(", ".join(gparts))
        yname = clean_name(name_en or name_vi or name_ru)
        yparts = [yname] + ([reg_en] if reg_en.lower() not in yname.lower() else []) + [country_en]
        yandex = f"https://yandex.com/maps/?text={urllib.parse.quote(', '.join(yparts))}&ll={lon},{lat}&z=17"
        return {"yandex": yandex, "google": google}

    # --- NGA: GIỮ NGUYÊN quy ước cũ (tên Nga khớp POI Yandex rất tốt) ---
    y_name = name_ru or name_en or name_vi
    ru_loc = RU_LOC.get(region_slug)
    y_text = f"{y_name}, {ru_loc}" if ru_loc else y_name
    yq = urllib.parse.quote(y_text)
    yandex = f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16"

    g_name = name_en or name_vi or name_ru
    parts = [g_name]
    if reg_en.lower() not in g_name.lower():
        parts.append(reg_en)
    parts.append(country_en)
    gq = urllib.parse.quote(", ".join(parts))
    google = f"https://www.google.com/maps/search/?api=1&query={gq}"

    return {"yandex": yandex, "google": google}


def main():
    files = sorted(f for f in glob.glob(os.path.join(REGIONS, "*.json")))
    changed_recs = 0
    changed_files = 0
    for path in files:
        region_slug = os.path.splitext(os.path.basename(path))[0]
        arr = json.load(open(path, encoding="utf-8"))
        if not isinstance(arr, list):
            continue
        ch = False
        for rec in arr:
            if not rec.get("coordinates"):
                continue
            newmaps = build_maps(rec, region_slug)
            if rec.get("maps") != newmaps:
                rec["maps"] = newmaps
                changed_recs += 1
                ch = True
        if ch:
            json.dump(arr, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            changed_files += 1
    print(f"Đã đổi link bản đồ: {changed_recs} bản ghi ở {changed_files} file.")


if __name__ == "__main__":
    main()
