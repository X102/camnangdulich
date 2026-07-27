# -*- coding: utf-8 -*-
"""Cập nhật số liệu (địa điểm, vùng) trên trang chủ trung-tam.html từ data/index.json.
Chạy sau mỗi lần build.py để trang chủ luôn hiển thị đúng tổng số địa điểm."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
idx = json.load(open(os.path.join(ROOT, "data", "index.json"), encoding="utf-8"))
total = str(idx.get("total_places", 0))
nreg = str(len(idx.get("regions", [])))
hub = os.path.join(ROOT, "trung-tam.html")
if not os.path.exists(hub):
    print("Không thấy trung-tam.html"); raise SystemExit(0)
html = open(hub, encoding="utf-8").read()
html = re.sub(r'(<b>)\s*\d+\s*(</b><span>địa điểm)', r'\g<1>' + total + r'\g<2>', html)
html = re.sub(r'(<b>)\s*\d+\s*(</b><span>vùng)', r'\g<1>' + nreg + r'\g<2>', html)
open(hub, "w", encoding="utf-8").write(html)
print("Trang chủ:", total, "địa điểm,", nreg, "vùng")
