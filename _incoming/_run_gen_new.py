# -*- coding: utf-8 -*-
"""Sinh HTML+DOCX cho 6 tài liệu mới (dùng lại hàm của gen_place_doc), rồi cập nhật mục lục."""
import sys, os, json, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import gen_place_doc as g

slugs = ["gulag-history-museum", "shukhov-tower", "peter-the-great-statue",
         "lakhta-center", "general-staff-building", "rossi-street"]
for sl in slugs:
    fp = os.path.join(ROOT, "_incoming", "doc_" + sl + ".json")
    d = json.load(open(fp, encoding="utf-8"))
    reg = g.region_of(d)
    outdir = os.path.join(g.OUTROOT, reg)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, sl + ".html"), "w", encoding="utf-8") as f:
        f.write(g.build_html(d))
    tag = "HTML+DOCX"
    try:
        g.build_docx(d, os.path.join(outdir, sl + ".docx"))
    except Exception as e:
        tag = "HTML only (docx err: %s)" % e
    print("+ %s/%s: %s" % (reg, sl, tag))

print("--- cap nhat muc luc ---")
subprocess.run(["python3", os.path.join(ROOT, "tools", "build_docs_index.py")], check=False)
