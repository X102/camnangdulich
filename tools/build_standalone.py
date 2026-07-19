# -*- coding: utf-8 -*-
"""
build_standalone.py — Gộp toàn bộ app thành MỘT file HTML tự chứa
(dist/russia-tourism-standalone.html): mở là chạy, không cần server,
nhúng sẵn thư viện bản đồ + dữ liệu. Chỉ ảnh nền bản đồ & ảnh địa điểm cần Internet.

Chạy:  python3 tools/build_standalone.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return f.read()


def main():
    app_css = read("assets", "app.css")
    leaflet_css = read("assets", "vendor", "leaflet.css")
    mc_css = read("assets", "vendor", "MarkerCluster.css")
    mcd_css = read("assets", "vendor", "MarkerCluster.Default.css")
    leaflet_js = read("assets", "vendor", "leaflet.js")
    mc_js = read("assets", "vendor", "leaflet.markercluster.js")
    common_js = read("assets", "common.js")
    bundle_js = read("data", "bundle.js")
    app_js = read("tools", "standalone_app.js")

    extra_css = """
    html,body{height:100%}
    .tabs{max-width:1280px;margin:0 auto;padding:10px 20px 0;display:flex;gap:8px}
    .tabbtn{cursor:pointer;border:1px solid var(--line);background:#fff;padding:9px 18px;border-radius:12px 12px 0 0;font-weight:700;font-size:14px;color:var(--muted)}
    .tabbtn.active{background:var(--navy);color:#fff;border-color:var(--navy)}
    .toolbar{max-width:1280px;margin:0 auto 8px;border-radius:0 12px 12px 12px}
    #listView{max-width:1280px;margin:0 auto;padding:0 20px 20px}
    #mapView{display:none;height:70vh;margin:0 20px 20px;border:1px solid var(--line);border-radius:12px;overflow:hidden}
    .map-side{width:330px;min-width:330px;background:#fff;border-right:1px solid var(--line);overflow-y:auto;padding:14px 16px}
    .map-wrap{flex:1;position:relative}#map{position:absolute;inset:0}
    .rt-pin .pin{width:30px;height:30px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);border:2px solid #fff;box-shadow:0 2px 6px rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center}
    .rt-pin .pin span{transform:rotate(45deg);font-size:14px}
    .leaflet-tooltip.rt-label{background:rgba(255,255,255,.92);border:1px solid var(--line);border-radius:6px;box-shadow:0 1px 4px rgba(0,0,0,.2);color:var(--navy);font-weight:600;font-size:11.5px;padding:2px 7px;white-space:nowrap}
    .leaflet-tooltip.rt-label:before{display:none}
    .leaflet-popup-content{margin:12px 14px;font-family:inherit}
    .pop h4{margin:0 0 4px;font-size:15px}.pop .sub{color:var(--muted);font-size:11.5px;margin-bottom:6px}
    .pop .pop-actions{display:flex;gap:5px;flex-wrap:wrap;margin-top:8px}
    .pop-photo{width:100%;height:92px;object-fit:cover;border-radius:8px;margin-bottom:6px;background:#22405f}
    .tour-item{display:flex;gap:8px;align-items:flex-start;padding:7px 0;border-bottom:1px dashed var(--line);font-size:13px}
    .tour-item .idx{background:var(--navy);color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex:0 0 auto}
    .tour-item .idx.day{background:var(--gold);color:#241c05}
    .tour-empty{color:var(--muted);font-size:13px}.tour-stat{background:#f0f4fa;border-radius:10px;padding:8px 10px;font-size:12.5px;margin:8px 0}
    .fc{cursor:pointer;user-select:none;padding:4px 9px;border-radius:999px;border:1.5px solid var(--line);font-size:12px;font-weight:600;color:var(--muted)}
    .fc.on{color:#fff;border-color:transparent}
    @media(max-width:820px){#mapView{flex-direction:column;height:auto}.map-side{width:100%;min-width:0}.map-wrap{height:60vh}}
    """

    html = """<!DOCTYPE html><html lang="vi"><head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Cẩm nang Du lịch Nga · Saint Petersburg (bản mẫu)</title>
<style>
""" + leaflet_css + "\n" + mc_css + "\n" + mcd_css + "\n" + app_css + "\n" + extra_css + """
</style></head><body>
<header class="site-header"><nav class="nav">
  <span class="brand"><span>🇷🇺 Cẩm nang Du lịch Nga</span><span class="dot">●</span></span>
  <div class="nav-links"><span class="muted" style="color:#cdd7e6;font-size:13px">Bản mẫu Saint Petersburg · một file duy nhất</span></div>
</nav></header>

<div class="tabs">
  <div class="tabbtn active" data-tab="list">📖 Danh sách</div>
  <div class="tabbtn" data-tab="map">🗺️ Bản đồ &amp; lập tour</div>
</div>

<div class="toolbar">
  <input type="search" id="q" placeholder="🔎 Tìm theo tên, mô tả…" style="min-width:200px;flex:1;border:1px solid var(--line);border-radius:10px;padding:8px 12px;font-family:inherit"/>
  <select id="sort" style="border:1px solid var(--line);border-radius:10px;padding:8px 12px;font-family:inherit">
    <option value="stars">Đánh giá cao nhất</option><option value="reviews">Nhiều đánh giá</option><option value="name">Tên A→Z</option></select>
  <select id="region" style="border:1px solid var(--line);border-radius:10px;padding:8px 12px;font-family:inherit"><option value="">Tất cả vùng</option></select>
  <span class="muted" style="font-size:12px">Sao ≥ <b id="starVal">0</b></span><input type="range" id="minStar" min="0" max="5" step="0.5" value="0" style="width:90px"/>
  <span class="muted" style="font-size:12px;margin-left:auto">Tốc độ đọc</span><input type="range" id="rate" min="0.6" max="1.4" step="0.1" value="1" style="width:90px"/>
  <button class="btn sm" id="stopAll">⏹ Dừng</button>
</div>
<div class="filter-cats" id="filterCats" style="max-width:1280px;margin:0 auto 10px;padding:0 20px;display:flex;gap:6px;flex-wrap:wrap"></div>

<div id="listView">
  <div class="notice voice-warn" id="voiceWarn" style="display:none;margin-bottom:12px">🔊 Máy chưa có giọng tiếng Việt riêng — vẫn đọc được, cài giọng vi-VN để hay hơn.</div>
  <div id="countLine" class="muted" style="margin:4px 0 14px"></div>
  <div class="grid" id="grid"></div>
</div>

<div id="mapView">
  <div class="map-side">
    <label style="display:flex;align-items:center;gap:7px;font-size:12.5px;margin-bottom:12px;cursor:pointer;font-weight:600;color:var(--navy)"><input type="checkbox" id="showLabels" style="width:15px;height:15px;cursor:pointer"/> 🏷️ Hiện tên địa điểm trên bản đồ</label>
    <h3 style="margin:0 0 10px">🧭 Kế hoạch tour <span class="muted" style="font-weight:400;font-size:12px">(<span id="tourCount">0</span>)</span></h3>
    <div id="tourList"><div class="tour-empty">Bấm “➕ Tour” trên bản đồ để thêm điểm.</div></div>
    <div id="tourStat"></div>
    <label class="muted" style="font-size:12px;display:flex;align-items:center;gap:4px;margin:8px 0">Điểm/ngày <input type="number" id="perDay" min="1" max="10" value="4" style="width:52px;border:1px solid var(--line);border-radius:8px;padding:3px 6px"/></label>
    <div style="display:flex;gap:6px;flex-wrap:wrap"><button class="btn sm primary" id="optimize">🧮 Tối ưu</button><button class="btn sm" id="clearTour">🗑️ Xoá</button></div>
  </div>
  <div class="map-wrap"><div id="map"></div></div>
</div>

<footer class="site-footer"><div class="fwrap">
  <div>Cẩm nang Du lịch Nga · bản mẫu Saint Petersburg (18 địa điểm) · dữ liệu mở rộng dần.</div>
  <div class="contact">Liên hệ: <b>Phạm Đăng Hiển</b> · <a href="mailto:lopmaybay@gmail.com">lopmaybay@gmail.com</a> · <a href="https://fb.com/lopmaybay" target="_blank" rel="noopener">fb.com/lopmaybay</a></div>
</div></footer>

<script>""" + leaflet_js + """</script>
<script>""" + mc_js + """</script>
<script>""" + common_js + """</script>
<script>""" + bundle_js + """</script>
<script>""" + app_js + """</script>
</body></html>"""

    os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
    out = os.path.join(ROOT, "dist", "russia-tourism-standalone.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("Đã tạo", out, "(", round(len(html) / 1024), "KB )")


if __name__ == "__main__":
    main()
