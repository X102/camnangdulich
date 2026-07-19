# -*- coding: utf-8 -*-
"""normalize_categories.py — Chuẩn hoá 'categories' của mọi bản ghi về đúng bảng cho phép.
Chạy: python3 tools/normalize_categories.py"""
import json, os, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")

ALLOWED = {"museum", "palace", "church", "fortress", "monument",
           "park_garden", "bridge", "square_street", "theatre", "other"}
MAP = {
    "landmark": "monument", "viewpoint": "monument", "historic_site": "monument",
    "historical": "monument", "history": "monument", "archaeological_site": "monument",
    "archaeological": "monument", "memorial": "monument", "statue": "monument", "obelisk": "monument",
    "religious_site": "church", "religious-site": "church", "religious": "church",
    "cathedral": "church", "monastery": "church", "convent": "church", "mosque": "church", "temple": "church",
    "natural_site": "park_garden", "nature": "park_garden", "natural": "park_garden",
    "park": "park_garden", "garden": "park_garden", "reserve": "park_garden",
    "national_park": "park_garden", "waterfall": "park_garden", "mountain": "park_garden", "lake": "park_garden",
    "cave": "other", "beach": "park_garden",
    "square": "square_street", "street": "square_street", "town": "square_street",
    "city": "square_street", "waterfront": "square_street", "embankment": "square_street", "village": "square_street",
    "estate": "palace", "manor": "palace", "castle": "fortress", "kremlin": "fortress",
    "gallery": "museum",
}


def norm(cats):
    out = []
    for c in (cats or []):
        c2 = c if c in ALLOWED else MAP.get(str(c).strip().lower(), "other")
        if c2 not in out:
            out.append(c2)
    return out or ["other"]


def main():
    changed_files = 0
    changed_recs = 0
    for rp in glob.glob(os.path.join(REGIONS, "*.json")):
        arr = json.load(open(rp, encoding="utf-8"))
        ch = False
        for r in arr:
            nc = norm(r.get("categories"))
            if nc != r.get("categories"):
                r["categories"] = nc
                changed_recs += 1
                ch = True
        if ch:
            json.dump(arr, open(rp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            changed_files += 1
    print(f"Chuẩn hoá: {changed_recs} bản ghi ở {changed_files} file")


if __name__ == "__main__":
    main()
