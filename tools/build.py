# -*- coding: utf-8 -*-
"""
build.py — Bộ biên dịch dữ liệu (data compiler)

Quét mọi file trong data/regions/*.json (mỗi file = 1 vùng, là mảng địa điểm)
rồi sinh ra: data/index.json, data/bundle.js và các export.

Chạy nhanh (chỉ index.json + bundle.js cho web):  BUILD_FAST=1 python3 tools/build.py
Chạy đầy đủ (kèm csv/geojson/xlsx):                python3 tools/build.py
"""
import json, os, csv, glob, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS_DIR = os.path.join(ROOT, "data", "regions")
DATA_DIR = os.path.join(ROOT, "data")
EXPORTS_DIR = os.path.join(ROOT, "exports")
DOCS_DIR = os.path.join(ROOT, "tai-lieu-noi-bo")

FAST = bool(os.environ.get("BUILD_FAST"))

# Nhãn quốc gia (VI) — đồng bộ với kho dữ liệu chính, đủ 17 nước.
COUNTRY_NAMES = {
    "russia": "Nga", "vietnam": "Việt Nam", "china": "Trung Quốc",
    "korea": "Hàn Quốc", "japan": "Nhật Bản", "thailand": "Thái Lan",
    "laos": "Lào", "cambodia": "Campuchia", "indonesia": "Indonesia",
    "kazakhstan": "Kazakhstan", "uzbekistan": "Uzbekistan", "myanmar": "Myanmar",
    "malaysia": "Malaysia", "singapore": "Singapore", "philippines": "Philippines",
    "brunei": "Brunei", "timor-leste": "Đông Timor",
}

# Quét thư mục tài liệu nội bộ MỘT LẦN (nhanh hơn os.path.exists từng điểm).
def scan_docs():
    html_set, docx_set = set(), set()
    if os.path.isdir(DOCS_DIR):
        for reg in os.listdir(DOCS_DIR):
            p = os.path.join(DOCS_DIR, reg)
            if not os.path.isdir(p):
                continue
            try:
                for fn in os.listdir(p):
                    if fn.endswith(".html"):
                        html_set.add(reg + "/" + fn[:-5])
                    elif fn.endswith(".docx"):
                        docx_set.add(reg + "/" + fn[:-5])
            except Exception:
                pass
    return html_set, docx_set

DOC_HTML, DOC_DOCX = scan_docs()


def attach_doc_flags(reg_slug, p):
    slug = p.get("slug")
    p.pop("has_doc", None); p.pop("doc_url", None); p.pop("doc_docx", None)
    if not slug:
        p["has_doc"] = False
        return
    key = reg_slug + "/" + slug
    if key in DOC_HTML:
        p["has_doc"] = True
        p["doc_url"] = "tai-lieu-noi-bo/" + key + ".html"
        if key in DOC_DOCX:
            p["doc_docx"] = "tai-lieu-noi-bo/" + key + ".docx"
    else:
        p["has_doc"] = False

REQUIRED = ["id", "name_vi", "region", "coordinates"]


def load_regions():
    regions = []
    files = sorted(glob.glob(os.path.join(REGIONS_DIR, "*.json")))
    files = [f for f in files if not os.path.basename(f).startswith("_")]  # bỏ file backup/tạm
    for path in files:
        slug = os.path.splitext(os.path.basename(path))[0]
        try:
            with open(path, encoding="utf-8") as f:
                items = json.load(f)
        except Exception as e:
            print(f"  ! Bỏ qua {slug}: lỗi đọc JSON ({e})")
            continue
        if not isinstance(items, list):
            print(f"  ! Bỏ qua {slug}: nội dung không phải mảng")
            continue
        good = []
        for it in items:
            miss = [k for k in REQUIRED if k not in it or it.get(k) in (None, "")]
            if miss:
                continue
            good.append(it)
        regions.append({"slug": slug, "items": good})
    return regions


def bbox_center(items):
    lats = [p["coordinates"]["lat"] for p in items if p.get("coordinates")]
    lons = [p["coordinates"]["lon"] for p in items if p.get("coordinates")]
    if not lats:
        return None, None
    bbox = [min(lons), min(lats), max(lons), max(lats)]
    center = [sum(lats) / len(lats), sum(lons) / len(lons)]
    return bbox, center


def build():
    print("Đang biên dịch dữ liệu..." + (" [FAST]" if FAST else ""))
    regions = [r for r in load_regions() if r["items"]]
    all_places = []
    region_meta = []
    cat_counts = {}

    for r in regions:
        items = r["items"]
        for p in items:
            attach_doc_flags(r["slug"], p)
            all_places.append(p)
            for c in p.get("categories", []):
                cat_counts[c] = cat_counts.get(c, 0) + 1
        bbox, center = bbox_center(items)
        name_vi = items[0].get("region_name_vi", r["slug"]) if items else r["slug"]
        fed = items[0].get("federal_district") if items else None
        country = (items[0].get("country") if items else None) or "russia"
        region_meta.append({
            "slug": r["slug"], "name_vi": name_vi, "federal_district": fed,
            "country": country, "count": len(items), "bbox": bbox, "center": center,
        })

    gbbox, gcenter = bbox_center(all_places)
    try:
        generated = datetime.datetime.now().isoformat(timespec="seconds")
    except Exception:
        generated = "BUILD_TIME"

    country_counts = {}
    for p in all_places:
        c = p.get("country") or "russia"
        country_counts[c] = country_counts.get(c, 0) + 1
    # chỉ liệt kê nhãn cho các nước thực sự có mặt
    country_names = {k: v for k, v in COUNTRY_NAMES.items() if k in country_counts}
    for k in country_counts:
        country_names.setdefault(k, k)

    index = {
        "generated": generated, "total_places": len(all_places),
        "regions": region_meta, "categories": cat_counts,
        "countries": country_counts, "country_names": country_names,
        "bbox": gbbox, "center": gcenter,
    }

    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(EXPORTS_DIR, exist_ok=True)

    with open(os.path.join(DATA_DIR, "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    bundle = {"meta": index, "places": all_places}
    with open(os.path.join(DATA_DIR, "bundle.js"), "w", encoding="utf-8") as f:
        f.write("/* Tự động sinh bởi build.py — KHÔNG sửa tay. */\n")
        f.write("window.RUSSIA_DB = ")
        json.dump(bundle, f, ensure_ascii=False)
        f.write(";\n")

    if FAST:
        print(f"Xong [FAST]. Tổng {len(all_places)} địa điểm, {len(region_meta)} vùng.")
        print("Đã sinh: data/index.json, data/bundle.js")
        return index

    with open(os.path.join(EXPORTS_DIR, "places.json"), "w", encoding="utf-8") as f:
        json.dump(all_places, f, ensure_ascii=False, indent=2)

    csv_cols = ["id","name_vi","name_ru","name_en","region_name_vi","categories","lat","lon",
        "rating_value","rating_count","rating_source","duration","ticket","hours","best_time",
        "yandex_map","google_map","official_site","status","short_presentation"]
    with open(os.path.join(EXPORTS_DIR, "places.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f); w.writerow(csv_cols)
        for p in all_places:
            pr = p.get("practical", {}) or {}; rt = p.get("rating", {}) or {}
            w.writerow([p.get("id"),p.get("name_vi"),p.get("name_ru"),p.get("name_en"),
                p.get("region_name_vi"),"|".join(p.get("categories", [])),
                p["coordinates"]["lat"],p["coordinates"]["lon"],
                rt.get("value"),rt.get("count"),rt.get("source"),
                pr.get("duration_vi"),pr.get("ticket_vi"),pr.get("hours_vi"),pr.get("best_time_vi"),
                (p.get("maps", {}) or {}).get("yandex"),(p.get("maps", {}) or {}).get("google"),
                p.get("official_site"),p.get("status"),p.get("presentation_short_vi")])

    features = []
    for p in all_places:
        features.append({"type":"Feature",
            "geometry":{"type":"Point","coordinates":[p["coordinates"]["lon"],p["coordinates"]["lat"]]},
            "properties":{"id":p.get("id"),"name_vi":p.get("name_vi"),"name_ru":p.get("name_ru"),
                "name_en":p.get("name_en"),"region":p.get("region_name_vi"),
                "categories":p.get("categories", []),"rating":(p.get("rating", {}) or {}).get("value"),
                "reviews":(p.get("rating", {}) or {}).get("count"),"short":p.get("presentation_short_vi"),
                "yandex":(p.get("maps", {}) or {}).get("yandex"),"google":(p.get("maps", {}) or {}).get("google"),
                "photo":p.get("photo"),"status":p.get("status")}})
    with open(os.path.join(EXPORTS_DIR, "places.geojson"), "w", encoding="utf-8") as f:
        json.dump({"type":"FeatureCollection","features":features}, f, ensure_ascii=False, indent=2)

    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill, Alignment
        from openpyxl.utils import get_column_letter
        wb = Workbook(); ws = wb.active; ws.title = "Places"
        headers = ["ID","Tên (VI)","Tên (RU)","Tên (EN)","Vùng","Loại","Vĩ độ","Kinh độ","Sao",
            "Số đánh giá","Nguồn ĐG","Thời lượng","Giá vé","Giờ mở cửa","Thời điểm đẹp",
            "Yandex Map","Google Map","Web chính thức","Trạng thái","Thuyết trình ngắn"]
        ws.append(headers)
        for c in range(1, len(headers)+1):
            cell = ws.cell(row=1, column=c); cell.fill = PatternFill("solid", fgColor="1F4E79")
            cell.font = Font(color="FFFFFF", bold=True); cell.alignment = Alignment(vertical="center", wrap_text=True)
        for p in all_places:
            pr = p.get("practical", {}) or {}; rt = p.get("rating", {}) or {}
            ws.append([p.get("id"),p.get("name_vi"),p.get("name_ru"),p.get("name_en"),
                p.get("region_name_vi"),", ".join(p.get("categories", [])),
                p["coordinates"]["lat"],p["coordinates"]["lon"],rt.get("value"),rt.get("count"),rt.get("source"),
                pr.get("duration_vi"),pr.get("ticket_vi"),pr.get("hours_vi"),pr.get("best_time_vi"),
                (p.get("maps", {}) or {}).get("yandex"),(p.get("maps", {}) or {}).get("google"),
                p.get("official_site"),p.get("status"),p.get("presentation_short_vi")])
        widths=[22,30,24,24,18,16,10,10,6,12,12,14,22,26,22,30,30,26,12,50]
        for i,wdt in enumerate(widths, start=1):
            ws.column_dimensions[get_column_letter(i)].width = wdt
        ws.freeze_panes = "A2"; wb.save(os.path.join(EXPORTS_DIR, "places.xlsx"))
    except Exception as e:
        print(f"  ! Không tạo được XLSX: {e}")

    print(f"Xong. Tổng {len(all_places)} địa điểm, {len(region_meta)} vùng.")
    return index


if __name__ == "__main__":
    build()
