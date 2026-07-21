/* App gộp cho bản một-file: chia sẻ bộ lọc giữa Danh sách và Bản đồ. */
(function () {
  var places = RT.getPlaces();
  var meta = RT.getMeta();
  var activeCats = {};
  var LIST_PAGE = 48, listShown = LIST_PAGE;
  var tour = [];
  var map = null, cluster = null, routeLayer = null, markers = {}, mapReady = false, labelsOn = false;

  /* ---------- Bộ lọc dùng chung ---------- */
  function passFilter(p) {
    var q = (document.getElementById("q").value || "").trim().toLowerCase();
    var region = document.getElementById("region").value;
    var minStar = parseFloat(document.getElementById("minStar").value) || 0;
    var catKeys = Object.keys(activeCats);
    if (region && p.region !== region) return false;
    if (minStar && ((p.rating || {}).value || 0) < minStar) return false;
    if (catKeys.length && !(p.categories || []).some(function (c) { return activeCats[c]; })) return false;
    if (q) {
      var hay = [p.name_vi, p.name_ru, p.name_en, p.presentation_short_vi, p.presentation_long_vi].join(" ").toLowerCase();
      if (hay.indexOf(q) < 0) return false;
    }
    return true;
  }
  function filtered() { return places.filter(passFilter); }

  /* ---------- Danh sách ---------- */
  function photoStyle(p) {
    if (p.photo) return 'style="background-image:url(\'' + p.photo + "'),linear-gradient(135deg,#2b4a72,#16293f)\"";
    return "";
  }
  function cardHTML(p) {
    var info = RT.catInfo(RT.primaryCat(p));
    var rt = p.rating || {}, pr = p.practical || {};
    var isFree = (p.tags || []).indexOf("free") >= 0 || /miễn phí/i.test(pr.ticket_vi || "");
    var hl = (p.highlights_vi || []).map(function (h) { return "<li>" + RT.escapeHtml(h) + "</li>"; }).join("");
    return '<article class="card" data-id="' + p.id + '">' +
      '<div class="card-photo" ' + photoStyle(p) + '><div class="ph-fallback">' + info.emoji + '</div>' +
      '<div class="cat-tag"><span class="chip" style="background:' + info.color + '">' + info.emoji + " " + info.vi + '</span></div></div>' +
      '<div class="card-body">' +
        '<div style="display:flex;justify-content:space-between;gap:8px;align-items:flex-start;">' +
        '<div><h3>' + RT.escapeHtml(p.name_vi) + '</h3><div class="subname">' + RT.escapeHtml(p.name_ru || "") + '</div></div>' +
        (isFree ? '<span class="badge-free">Miễn phí</span>' : '') + '</div>' +
        '<div class="rating-row">' + RT.starHTML(rt.value) + (rt.value != null ? '<b>' + rt.value + '</b>' : '') +
        (rt.count != null ? '<span class="muted">· ' + RT.fmtCount(rt.count) + ' đánh giá' + (rt.source ? " · " + rt.source : "") + '</span>' : '') + '</div>' +
        '<div class="short">' + RT.escapeHtml(p.presentation_short_vi || "") + '</div>' +
        '<div class="card-actions">' +
          '<button class="btn sm gold tts-btn" data-kind="short">🔊 Nghe</button>' +
          '<button class="btn sm tts-btn" data-kind="long">🎧 Nghe chi tiết</button>' +
          '<button class="btn sm toggle-detail">📖 Chi tiết</button>' +
          (p.maps && p.maps.yandex ? '<a class="btn sm" href="' + p.maps.yandex + '" target="_blank" rel="noopener">📍 Yandex</a>' : '') +
          (p.maps && p.maps.google ? '<a class="btn sm" href="' + p.maps.google + '" target="_blank" rel="noopener">🗺️ Google</a>' : '') +
        '</div>' +
        '<div class="detail"><h4>Thuyết trình chi tiết</h4><p>' + RT.escapeHtml(p.presentation_long_vi || "") + '</p>' +
          (hl ? '<h4>Điểm nhấn</h4><ul>' + hl + '</ul>' : '') +
          '<h4>Thông tin tham quan</h4><div class="practical">' +
          (pr.hours_vi ? '<div><b>🕒 Giờ:</b> ' + RT.escapeHtml(pr.hours_vi) + '</div>' : '') +
          (pr.ticket_vi ? '<div><b>🎟️ Vé:</b> ' + RT.escapeHtml(pr.ticket_vi) + '</div>' : '') +
          (pr.duration_vi ? '<div><b>⏱️ Thời lượng:</b> ' + RT.escapeHtml(pr.duration_vi) + '</div>' : '') +
          (pr.best_time_vi ? '<div><b>🌤️ Thời điểm đẹp:</b> ' + RT.escapeHtml(pr.best_time_vi) + '</div>' : '') +
          (pr.tips_vi ? '<div><b>💡 Mẹo:</b> ' + RT.escapeHtml(pr.tips_vi) + '</div>' : '') + '</div>' +
          (p.review_summary_vi ? '<h4>Tóm tắt bình luận</h4><p>' + RT.escapeHtml(p.review_summary_vi) + '</p>' : '') +
        '</div>' +
      '</div></article>';
  }
  function renderList(more) {
    var list = filtered();
    list.sort(function (a, b) {
      var s = document.getElementById("sort").value;
      if (s === "name") return (a.name_vi || "").localeCompare(b.name_vi || "", "vi");
      if (s === "reviews") return ((b.rating || {}).count || 0) - ((a.rating || {}).count || 0);
      return ((b.rating || {}).value || 0) - ((a.rating || {}).value || 0);
    });
    if (more !== true) listShown = LIST_PAGE;
    var slice = list.slice(0, listShown);
    document.getElementById("countLine").textContent = "Hiển thị " + slice.length + " / " + list.length + " địa điểm";
    var grid = document.getElementById("grid");
    grid.innerHTML = slice.map(cardHTML).join("");
    var mw = document.getElementById("moreWrap");
    if (mw) {
      var rem = list.length - slice.length;
      mw.innerHTML = rem > 0 ? '<button class="btn primary" id="moreBtn">⬇️ Xem thêm ' + Math.min(LIST_PAGE, rem) + ' địa điểm (còn ' + rem + ')</button>' : "";
      if (rem > 0) document.getElementById("moreBtn").onclick = function () { listShown += LIST_PAGE; renderList(true); };
    }
    grid.querySelectorAll(".card").forEach(function (card) {
      var p = places.filter(function (x) { return x.id === card.dataset.id; })[0];
      card.querySelector(".toggle-detail").onclick = function () { card.querySelector(".detail").classList.toggle("open"); };
      card.querySelectorAll(".tts-btn").forEach(function (btn) {
        btn.onclick = function () {
          var kind = btn.dataset.kind, txt = kind === "long" ? p.presentation_long_vi : p.presentation_short_vi;
          if (RT.TTS.activeId === p.id + ":" + kind) { RT.TTS.stop(); return; }
          RT.TTS.speak(txt, { id: p.id + ":" + kind, onState: function (st) {
            document.querySelectorAll(".tts-btn").forEach(function (b) { b.classList.remove("speaking"); });
            if (st === "start") btn.classList.add("speaking");
          } });
        };
      });
    });
  }

  /* ---------- Bản đồ ---------- */
  function makeIcon(p) {
    var info = RT.catInfo(RT.primaryCat(p));
    return L.divIcon({ className: "rt-pin", html: '<div class="pin" style="background:' + info.color + '"><span>' + info.emoji + "</span></div>", iconSize: [30, 30], iconAnchor: [15, 30], popupAnchor: [0, -30] });
  }
  function popupHTML(p) {
    var rt = p.rating || {}, inTour = tour.indexOf(p.id) >= 0;
    return '<div class="pop">' + (p.photo ? '<img class="pop-photo" src="' + p.photo + '" onerror="this.style.display=\'none\'"/>' : '') +
      '<h4>' + RT.escapeHtml(p.name_vi) + '</h4><div class="sub">' + RT.escapeHtml(p.name_ru || "") + '</div>' +
      '<div>' + RT.starHTML(rt.value) + (rt.value != null ? ' <b>' + rt.value + '</b>' : '') + (rt.count != null ? ' <span class="muted">(' + RT.fmtCount(rt.count) + ')</span>' : '') + '</div>' +
      '<div style="font-size:12.5px;margin-top:6px;">' + RT.escapeHtml(p.presentation_short_vi || "") + '</div>' +
      '<div class="pop-actions"><button class="btn sm gold" onclick="RTAPP.speak(\'' + p.id + '\')">🔊 Nghe</button>' +
      '<button class="btn sm ' + (inTour ? "primary" : "") + '" onclick="RTAPP.toggleTour(\'' + p.id + '\')">' + (inTour ? "✓ Trong tour" : "➕ Tour") + '</button>' +
      (p.maps && p.maps.yandex ? '<a class="btn sm" href="' + p.maps.yandex + '" target="_blank" rel="noopener">📍</a>' : '') +
      (p.maps && p.maps.google ? '<a class="btn sm" href="' + p.maps.google + '" target="_blank" rel="noopener">🗺️</a>' : '') +
      '</div></div>';
  }
  function initMap() {
    if (mapReady) return;
    mapReady = true;
    map = L.map("map").setView(meta.center || [59.93, 30.33], 10);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", { maxZoom: 19, attribution: "&copy; OpenStreetMap" }).addTo(map);
    cluster = (typeof L.markerClusterGroup === "function") ? L.markerClusterGroup({ maxClusterRadius: 45 }) : L.layerGroup();
    map.addLayer(cluster);
    renderMarkers();
    try { var b = L.latLngBounds(places.map(function (p) { return [p.coordinates.lat, p.coordinates.lon]; })); if (b.isValid()) map.fitBounds(b.pad(0.15)); } catch (e) {}
  }
  function renderMarkers() {
    if (!mapReady) return;
    cluster.clearLayers(); markers = {};
    filtered().forEach(function (p) {
      var m = L.marker([p.coordinates.lat, p.coordinates.lon], { icon: makeIcon(p) });
      m.bindPopup(popupHTML(p), { minWidth: 230 });
      if (labelsOn) m.bindTooltip(p.name_vi, { permanent: true, direction: "right", offset: [10, -10], className: "rt-label" });
      markers[p.id] = m; cluster.addLayer(m);
    });
  }
  function visitHours(p) { var t = (p.practical || {}).duration_vi || "", m = t.match(/(\d+(?:[.,]\d+)?)/); if (!m) return 1.5; var n = parseFloat(m[1].replace(",", ".")); return (/phút/.test(t) && !/giờ/.test(t)) ? n / 60 : n; }
  function tourPlaces() { return tour.map(function (id) { return places.filter(function (p) { return p.id === id; })[0]; }).filter(Boolean); }
  function renderTour() {
    document.getElementById("tourCount").textContent = tour.length;
    var tp = tourPlaces(), wrap = document.getElementById("tourList");
    if (!tp.length) { wrap.innerHTML = '<div class="tour-empty">Bấm “➕ Tour” trên bản đồ để thêm điểm.</div>'; document.getElementById("tourStat").innerHTML = ""; drawRoute(); return; }
    var perDay = Math.max(1, parseInt(document.getElementById("perDay").value) || 4), html = "";
    tp.forEach(function (p, i) {
      var day = Math.floor(i / perDay) + 1;
      var seg = i > 0 ? RT.haversineKm({ lat: tp[i - 1].coordinates.lat, lon: tp[i - 1].coordinates.lon }, { lat: p.coordinates.lat, lon: p.coordinates.lon }).toFixed(1) + " km" : "";
      html += '<div class="tour-item"><div class="idx' + (i % perDay === 0 ? " day" : "") + '">' + (i + 1) + '</div><div style="flex:1;"><div><b>' + RT.escapeHtml(p.name_vi) + '</b></div><div class="muted" style="font-size:11.5px;">Ngày ' + day + (seg ? ' · ' + seg : '') + ' · ' + ((p.practical || {}).duration_vi || "") + '</div></div><button class="btn sm" onclick="RTAPP.toggleTour(\'' + p.id + '\')">✕</button></div>';
    });
    wrap.innerHTML = html;
    var km = RT.routeDistanceKm(tp), vh = tp.reduce(function (s, p) { return s + visitHours(p); }, 0), days = Math.ceil(tp.length / perDay);
    document.getElementById("tourStat").innerHTML = '<div class="tour-stat">🧮 <b>' + tp.length + '</b> điểm · <b>' + days + '</b> ngày · <b>' + km.toFixed(1) + ' km</b> (đường chim bay)<br>⏱️ Tham quan ~<b>' + vh.toFixed(1) + ' giờ</b></div>';
    drawRoute();
  }
  function drawRoute() {
    if (!mapReady) return;
    if (routeLayer) { map.removeLayer(routeLayer); routeLayer = null; }
    var tp = tourPlaces(); if (tp.length < 2) return;
    var perDay = Math.max(1, parseInt(document.getElementById("perDay").value) || 4);
    var colors = ["#1f3a5f", "#c8a24b", "#2E86DE", "#27AE60", "#E74C3C", "#7C5CFC"], layers = [];
    for (var i = 1; i < tp.length; i++) {
      if (Math.floor(i / perDay) !== Math.floor((i - 1) / perDay)) continue;
      layers.push(L.polyline([[tp[i - 1].coordinates.lat, tp[i - 1].coordinates.lon], [tp[i].coordinates.lat, tp[i].coordinates.lon]], { color: colors[Math.floor(i / perDay) % colors.length], weight: 3, opacity: .8, dashArray: "6,6" }));
    }
    routeLayer = L.layerGroup(layers).addTo(map);
  }

  window.RTAPP = {
    speak: function (id) { var p = places.filter(function (x) { return x.id === id; })[0]; if (!p) return; if (RT.TTS.activeId === id) { RT.TTS.stop(); return; } RT.TTS.speak(p.presentation_long_vi || p.presentation_short_vi, { id: id }); },
    toggleTour: function (id) { var i = tour.indexOf(id); if (i >= 0) tour.splice(i, 1); else tour.push(id); renderTour(); if (markers[id]) markers[id].setPopupContent(popupHTML(places.filter(function (x) { return x.id === id; })[0])); }
  };

  /* ---------- Điều khiển + tab ---------- */
  function fillControls() {
    var rsel = document.getElementById("region");
    (meta.regions || []).forEach(function (r) { var o = document.createElement("option"); o.value = r.slug; o.textContent = r.name_vi + " (" + r.count + ")"; rsel.appendChild(o); });
    if ((meta.regions || []).length < 2) rsel.style.display = "none";
    var wrap = document.getElementById("filterCats");
    Object.keys(meta.categories || {}).forEach(function (slug) {
      var info = RT.catInfo(slug), el = document.createElement("span");
      el.className = "fc"; el.textContent = info.emoji + " " + info.vi;
      el.onclick = function () { if (activeCats[slug]) { delete activeCats[slug]; el.classList.remove("on"); el.style.background = ""; } else { activeCats[slug] = true; el.classList.add("on"); el.style.background = info.color; } renderAll(); };
      wrap.appendChild(el);
    });
  }
  function renderAll() { renderList(); renderMarkers(); }
  function showTab(t) {
    document.getElementById("listView").style.display = t === "list" ? "block" : "none";
    document.getElementById("mapView").style.display = t === "map" ? "flex" : "none";
    document.querySelectorAll(".tabbtn").forEach(function (b) { b.classList.toggle("active", b.dataset.tab === t); });
    if (t === "map") { initMap(); setTimeout(function () { if (map) map.invalidateSize(); renderMarkers(); }, 60); }
  }

  document.addEventListener("DOMContentLoaded", function () {
    fillControls();
    ["q", "sort", "region"].forEach(function (id) { var el = document.getElementById(id); if (el) el.oninput = el.onchange = renderAll; });
    document.getElementById("minStar").oninput = function () { document.getElementById("starVal").textContent = this.value; renderAll(); };
    var _sl = document.getElementById("showLabels"); if (_sl) _sl.onchange = function () { labelsOn = this.checked; renderMarkers(); };
    document.getElementById("perDay").oninput = renderTour;
    document.getElementById("rate").oninput = function () { RT.TTS.setRate(parseFloat(this.value)); };
    document.getElementById("stopAll").onclick = function () { RT.TTS.stop(); document.querySelectorAll(".tts-btn").forEach(function (b) { b.classList.remove("speaking"); }); };
    document.getElementById("optimize").onclick = function () { var tp = tourPlaces(); if (tp.length < 2) return; tour = RT.nearestRoute(tp, 0).map(function (p) { return p.id; }); renderTour(); };
    document.getElementById("clearTour").onclick = function () { tour = []; renderTour(); };
    document.querySelectorAll(".tabbtn").forEach(function (b) { b.onclick = function () { showTab(b.dataset.tab); }; });
    if (document.getElementById("voiceWarn") && RT.TTS.supported && !RT.TTS.hasVietnameseVoice()) setTimeout(function () { document.getElementById("voiceWarn").style.display = "block"; }, 600);
    renderList();
    renderTour();
  });
})();
