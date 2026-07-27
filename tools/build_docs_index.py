# -*- coding: utf-8 -*-
"""build_docs_index.py — Sinh trang tai-lieu-noi-bo/index.html liên kết TẤT CẢ tài liệu địa điểm.
Mở 1 link duy nhất để tra cứu mọi tài liệu. Chạy: python3 tools/build_docs_index.py"""
import json, os, glob, html as _html, unicodedata, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
DOCS = os.path.join(ROOT, "tai-lieu-noi-bo")
try:
    TODAY = datetime.date.today().isoformat()
except Exception:
    TODAY = "2026-07-24"
FONT = '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans","Helvetica Neue",Arial,sans-serif'


def nfc(s):
    return unicodedata.normalize("NFC", s) if isinstance(s, str) else s


# slug -> (name_vi, region_name_vi)
META = {}
REGORDER = []
for f in sorted(glob.glob(os.path.join(REGIONS, "*.json"))):
    for r in json.load(open(f, encoding="utf-8")):
        META[r["slug"]] = (nfc(r.get("name_vi", r["slug"])), nfc(r.get("region_name_vi", os.path.basename(f)[:-5])))


def main():
    groups = {}
    total = 0
    for hp in sorted(glob.glob(os.path.join(DOCS, "*", "*.html"))):
        base = os.path.basename(hp)
        if base == "index.html":
            continue
        region_dir = os.path.basename(os.path.dirname(hp))
        slug = base[:-5]
        name_vi, region_vi = META.get(slug, (slug, region_dir))
        has_docx = os.path.exists(os.path.join(os.path.dirname(hp), slug + ".docx"))
        groups.setdefault(region_vi, []).append((name_vi, region_dir, slug, has_docx))
        total += 1
    # render
    esc = _html.escape
    cards = ""
    for region_vi in sorted(groups.keys()):
        items = sorted(groups[region_vi], key=lambda x: x[0].lower())
        rows = ""
        for name_vi, region_dir, slug, has_docx in items:
            hurl = f"{region_dir}/{slug}.html"
            durl = f"{region_dir}/{slug}.docx"
            dlink = f'<a class="dx" href="{esc(durl)}" title="Tải bản Word (.docx)">Word ⬇</a>' if has_docx else ""
            rows += (f'<div class="item" data-n="{esc(name_vi.lower())}">'
                     f'<a class="nm" href="{esc(hurl)}">{esc(name_vi)}</a>{dlink}</div>')
        cards += (f'<section class="grp" data-r="{esc(region_vi.lower())}"><h2>{esc(region_vi)} '
                  f'<span class="c">({len(items)})</span></h2><div class="list">{rows}</div></section>')
    html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Tài liệu thuyết minh nội bộ — Mục lục</title>
<style>
*{{box-sizing:border-box}}body{{font-family:{FONT};margin:0;background:#f6f7fb;color:#1e2733}}
.hd{{background:linear-gradient(135deg,#152c4e,#0f2138);color:#fff;padding:26px 20px}}
.hd .k{{letter-spacing:.18em;text-transform:uppercase;font-size:11px;color:#c8a24b;font-weight:800}}
.hd h1{{margin:6px 0 4px;font-size:24px}}.hd p{{margin:0;color:#cfd9e8;font-size:14px}}
.wrap{{max-width:1000px;margin:0 auto;padding:18px}}
.top{{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:12px}}
.top a{{color:#152c4e;font-weight:700;text-decoration:none;font-size:13.5px}}
#q{{flex:1;min-width:200px;border:1px solid #e4e7ee;border-radius:10px;padding:10px 14px;font-size:15px;font-family:inherit}}
.grp h2{{font-size:17px;color:#152c4e;border-bottom:2px solid #c8a24b;padding-bottom:5px;margin:20px 0 10px}}
.grp .c{{color:#5c6773;font-weight:400;font-size:13px}}
.list{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px;align-items:stretch}}
.item{{background:#fff;border:1px solid #e4e7ee;border-radius:12px;padding:12px 14px;box-shadow:0 3px 10px rgba(20,30,50,.05);display:flex;justify-content:space-between;align-items:center;gap:10px;transition:border-color .15s,box-shadow .15s,transform .15s;min-height:58px}}
.item:hover{{border-color:#152c4e;box-shadow:0 8px 20px rgba(20,30,50,.12);transform:translateY(-1px)}}
.item .nm{{flex:1;min-width:0;font-weight:600;font-size:14px;line-height:1.35;color:#22303f;text-decoration:none;overflow-wrap:anywhere}}
.item .nm:hover{{color:#152c4e}}
.dx{{flex-shrink:0;color:#a9863a;font-size:11.5px;font-weight:800;text-decoration:none;white-space:nowrap;border:1px solid #e8dcc0;background:#faf5e9;border-radius:999px;padding:4px 10px}}
.dx:hover{{background:#f0e5cf;border-color:#c8a24b}}
.empty{{color:#5c6773;padding:30px 0;text-align:center;display:none}}
.foot{{color:#5c6773;font-size:12px;text-align:center;padding:20px}}
</style></head><body>
<div class="hd"><div class="k">Cẩm nang Du lịch · Nội bộ</div>
<h1>📚 Tài liệu thuyết minh chi tiết — Mục lục</h1>
<p>{total} tài liệu · mở 1 link để tra cứu mọi địa điểm · cập nhật {TODAY}</p></div>
<div class="wrap">
<div class="top"><a href="../trung-tam.html">🏠 Trang chủ</a><a href="../gis.html">🗺️ Bản đồ GIS</a><a href="../list.html">📖 Danh sách</a>
<input id="q" type="search" placeholder="🔎 Tìm nhanh tên địa điểm…"/></div>
{cards}
<div class="empty" id="empty">Không tìm thấy tài liệu phù hợp.</div>
<div class="foot">Tài liệu nội bộ — không public. Trang này tự cập nhật mỗi khi có tài liệu mới.</div>
</div>
<script>
var q=document.getElementById('q');
q.oninput=function(){{
  var t=(this.value||'').trim().toLowerCase(),any=false;
  document.querySelectorAll('.grp').forEach(function(g){{
    var vis=0;
    g.querySelectorAll('.item').forEach(function(it){{
      var ok=!t||(it.getAttribute('data-n')||'').indexOf(t)>=0;
      it.style.display=ok?'':'none'; if(ok)vis++;
    }});
    g.style.display=vis?'':'none'; if(vis)any=true;
  }});
  document.getElementById('empty').style.display=any?'none':'block';
}};
</script>
</body></html>"""
    with open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Đã sinh tai-lieu-noi-bo/index.html ({total} tài liệu)")


if __name__ == "__main__":
    os.makedirs(DOCS, exist_ok=True)
    main()
