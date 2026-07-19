# -*- coding: utf-8 -*-
"""
apply_photos.py — Lấp ảnh còn thiếu.
Đọc _incoming/photo_out_*.json ([{slug, photo_file}]), gán photo (Special:FilePath)
cho các địa điểm đang thiếu ảnh (photo == null) khớp slug. Không ghi đè ảnh đã có.
Chạy: python3 tools/apply_photos.py
"""
import json, os, glob, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INCOMING = os.path.join(ROOT, "_incoming")
REGIONS = os.path.join(ROOT, "data", "regions")


def photo_url(pf):
    if not pf:
        return None
    fn = pf.strip()
    if fn.lower().startswith("http"):
        fn = urllib.parse.unquote(fn.rstrip("/").split("/")[-1])
    if fn.startswith("File:"):
        fn = fn[5:]
    return "https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(fn)


def main():
    mapping = {}
    for f in glob.glob(os.path.join(INCOMING, "photo_out_*.json")):
        try:
            data = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            print("  ! lỗi đọc", os.path.basename(f), e); continue
        if isinstance(data, dict):
            data = data.get("results") or data.get("photos") or []
        for r in data:
            slug = r.get("slug"); pf = r.get("photo_file")
            if slug and pf:
                mapping[slug] = pf
    print("Tên ảnh thu được:", len(mapping))

    filled = 0
    for rp in glob.glob(os.path.join(REGIONS, "*.json")):
        arr = json.load(open(rp, encoding="utf-8"))
        changed = False
        for p in arr:
            if not p.get("photo") and p["slug"] in mapping:
                p["photo"] = photo_url(mapping[p["slug"]])
                p["photo_credit"] = "Wikimedia Commons"
                filled += 1; changed = True
        if changed:
            json.dump(arr, open(rp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Đã lấp ảnh:", filled, "điểm")


if __name__ == "__main__":
    main()
