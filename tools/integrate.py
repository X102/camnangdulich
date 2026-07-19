# -*- coding: utf-8 -*-
"""
integrate.py — Gộp các bản ghi "content record" (do agent tạo, đặt trong _incoming/*.json)
thành bản ghi đầy đủ và trộn vào data/regions/<region>.json (khử trùng theo slug).

Mỗi content record cần có: region, slug, name_vi, name_ru, name_en, categories,
lat, lon, address_vi, rating{value,count,source,as_of}, review_summary_vi,
presentation_short_vi, presentation_long_vi, highlights_vi[3],
practical{hours_vi,ticket_vi,duration_vi,best_time_vi,tips_vi}, photo_file, official_site, tags.

Chạy: python3 tools/integrate.py
"""
import json, os, glob, urllib.parse, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INCOMING = os.path.join(ROOT, "_incoming")
REGIONS_DIR = os.path.join(ROOT, "data", "regions")
QUEUE = os.path.join(ROOT, "_source", "regions_queue.json")
try:
    TODAY = datetime.date.today().isoformat()
except Exception:
    TODAY = "2026-07-16"

# slug vùng -> (name_vi, federal_district)
RMETA = {}
if os.path.exists(QUEUE):
    q = json.load(open(QUEUE, encoding="utf-8"))
    for r in q["regions"]:
        RMETA[r["slug"]] = (r["name_vi"], r["federal_district"])


def maps(lat, lon):
    return {"yandex": f"https://yandex.com/maps/?pt={lon},{lat}&z=17&l=map",
            "google": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"}


def photo_url(pf):
    if not pf:
        return None
    fn = pf.strip()
    if fn.lower().startswith("http"):
        fn = urllib.parse.unquote(fn.rstrip("/").split("/")[-1])
    if fn.startswith("File:"):
        fn = fn[5:]
    return "https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(fn)


def wrap(rec):
    region = rec["region"]
    name_vi_reg, fed = RMETA.get(region, (region, ""))
    lat, lon = float(rec["lat"]), float(rec["lon"])
    return {
        "id": f"{region}-{rec['slug']}", "slug": rec["slug"], "region": region,
        "region_name_vi": name_vi_reg, "federal_district": fed,
        "name_vi": rec["name_vi"], "name_ru": rec.get("name_ru", ""), "name_en": rec.get("name_en", ""),
        "categories": rec.get("categories", ["other"]),
        "coordinates": {"lat": lat, "lon": lon}, "address_vi": rec.get("address_vi", ""),
        "rating": rec.get("rating", {"value": None, "count": None, "source": None, "as_of": None}),
        "review_summary_vi": rec.get("review_summary_vi", ""),
        "presentation_short_vi": rec.get("presentation_short_vi", ""),
        "presentation_long_vi": rec.get("presentation_long_vi", ""),
        "highlights_vi": rec.get("highlights_vi", []),
        "practical": rec.get("practical", {}),
        "photo": photo_url(rec.get("photo_file")),
        "photo_credit": ("Wikimedia Commons" if rec.get("photo_file") else None),
        "maps": maps(lat, lon), "official_site": rec.get("official_site"),
        "sources": [{"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Special:Search?search=" + urllib.parse.quote(rec.get("name_en", rec["slug"]))}],
        "tags": rec.get("tags", []), "status": "enriched", "last_updated": TODAY,
    }


def main():
    files = sorted(glob.glob(os.path.join(INCOMING, "*.json")))
    files = [f for f in files if not os.path.basename(f).startswith("photo_")]
    incoming_by_region = {}
    problems = []
    for path in files:
        try:
            data = json.load(open(path, encoding="utf-8"))
        except Exception as e:
            problems.append(f"{os.path.basename(path)}: JSON lỗi ({e})")
            continue
        if isinstance(data, dict):
            data = data.get("places") or data.get("records") or [data]
        for rec in data:
            try:
                for k in ("region", "slug", "name_vi", "lat", "lon"):
                    if k not in rec or rec[k] in (None, ""):
                        raise KeyError(k)
                incoming_by_region.setdefault(rec["region"], []).append(wrap(rec))
            except Exception as e:
                problems.append(f"{os.path.basename(path)}: bỏ 1 bản ghi ({e}) slug={rec.get('slug')}")

    summary = {}
    for region, newrecs in incoming_by_region.items():
        rp = os.path.join(REGIONS_DIR, region + ".json")
        existing = json.load(open(rp, encoding="utf-8")) if os.path.exists(rp) else []
        seen = {p["slug"] for p in existing}
        added = 0
        for r in newrecs:
            if r["slug"] in seen:
                continue
            existing.append(r); seen.add(r["slug"]); added += 1
        json.dump(existing, open(rp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        summary[region] = {"added": added, "total": len(existing)}

    print("KẾT QUẢ GỘP:")
    for reg, s in summary.items():
        print(f"  {reg}: +{s['added']} -> tổng {s['total']}")
    if problems:
        print("VẤN ĐỀ:")
        for p in problems:
            print("  -", p)
    else:
        print("Không có lỗi bản ghi.")


if __name__ == "__main__":
    main()
