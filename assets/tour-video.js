/* =====================================================================
   tour-video.js — 🎬 Video thuyết trình chuyến đi · Cẩm nang Du lịch
   Tác giả nội dung: Phạm Đăng Hiển · fb.com/lopmaybay

   Dựng video từ Bảng lịch trình: mở đầu → từng ngày (lịch trình trong ngày)
   → bay giữa các điểm, lộ trình tự vẽ dần → thẻ thông tin từng điểm (ảnh, giờ,
   giới thiệu, điểm nhấn, giờ mở cửa, vé, ghi chú) → tổng kết.

   - Xuất file MP4 KHÔNG âm thanh: WebCodecs (H.264, dự phòng VP9/AV1) + mp4-muxer
     (assets/vendor/mp4-muxer.min.js, MIT). Dự phòng cuối: MediaRecorder.
   - Trình chiếu toàn màn hình thời gian thực, có giọng đọc (RT.TTS / speechSynthesis).
   Chạy hoàn toàn trên trình duyệt. Ô bản đồ (Esri/OSM) và ảnh Wikimedia được tải
   với CORS nên vẽ được lên canvas; ô/ảnh nào không tải được thì tự bỏ qua.

   Gọi: TourVideo.open(data)  — data do gis.html gom (xem videoData() trong gis.html).
   ===================================================================== */
(function (global) {
  "use strict";
  var VERSION = "1.0";
  var BASE = (function () {
    try { var s = document.currentScript && document.currentScript.src; if (s) return s.replace(/[^\/?#]*([?#].*)?$/, ""); } catch (e) { }
    return "assets/";
  })();

  /* ---------------- 0. tiện ích ---------------- */
  var PI = Math.PI;
  function clamp(x, a, b) { return x < a ? a : (x > b ? b : x); }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function seg(t, a, b) { return b <= a ? (t >= b ? 1 : 0) : clamp((t - a) / (b - a), 0, 1); }
  function ease(t) { t = clamp(t, 0, 1); return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
  function easeOut(t) { t = clamp(t, 0, 1); return 1 - Math.pow(1 - t, 3); }
  function easeOutBack(t) { t = clamp(t, 0, 1); var c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2); }
  function bounce(t) {
    t = clamp(t, 0, 1); var n = 7.5625, d = 2.75;
    if (t < 1 / d) return n * t * t;
    if (t < 2 / d) return n * (t -= 1.5 / d) * t + 0.75;
    if (t < 2.5 / d) return n * (t -= 2.25 / d) * t + 0.9375;
    return n * (t -= 2.625 / d) * t + 0.984375;
  }
  function escH(s) { return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
  function fmtClock(sec) { sec = Math.max(0, Math.round(sec)); var m = Math.floor(sec / 60), s = sec % 60; return m + ":" + (s < 10 ? "0" : "") + s; }
  function sleep(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }
  function cut(s, n) { s = String(s || "").replace(/\s+/g, " ").trim(); return s.length > n ? s.slice(0, n - 1).replace(/[\s,.;:–-]+$/, "") + "…" : s; }

  var FONT = '"Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", Arial, "Segoe UI Emoji", "Apple Color Emoji", "Noto Color Emoji", sans-serif';
  function F(weight, px, italic) { return (italic ? "italic " : "") + weight + " " + Math.max(1, Math.round(px)) + "px " + FONT; }
  var C = { navy: "#152c4e", navy2: "#0f2138", gold: "#c8a24b", gold2: "#f2c14e", cream: "#fbf8f1", ink: "#1e2733", muted: "#5c6773",
            red: "#e8514b", line: "#e7e3d6", route: "#ffc94d" };

  /* ---------------- 1. chữ theo ngôn ngữ ---------------- */
  var TXT = {
    vi: { journey: "HÀNH TRÌNH", day: "NGÀY", days: "ngày", nights: "đêm", stops: "điểm", stop: "Điểm", km: "km", pax: "khách",
          start: "Bắt đầu", from: "Xuất phát", hours: "Giờ mở cửa", ticket: "Vé", stay: "tham quan", min: "phút", note: "Ghi chú",
          summary: "TỔNG KẾT HÀNH TRÌNH", thanks: "Cảm ơn quý khách!", per: "/người", agenda: "Lịch trình trong ngày",
          more: "điểm nữa", photo: "Ảnh", guide: "Hướng dẫn viên", cost: "Chi phí dự kiến",
          wd: ["Chủ nhật", "Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy"] },
    en: { journey: "THE JOURNEY", day: "DAY", days: "days", nights: "nights", stops: "stops", stop: "Stop", km: "km", pax: "guests",
          start: "Start", from: "Starting from", hours: "Opening hours", ticket: "Tickets", stay: "visit", min: "min", note: "Note",
          summary: "TRIP SUMMARY", thanks: "Thank you!", per: "/person", agenda: "Today's plan",
          more: "more stops", photo: "Photo", guide: "Guide", cost: "Estimated cost",
          wd: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] },
    ru: { journey: "ПУТЕШЕСТВИЕ", day: "ДЕНЬ", days: "дн.", nights: "ноч.", stops: "точек", stop: "Точка", km: "км", pax: "гостей",
          start: "Начало", from: "Отправление", hours: "Часы работы", ticket: "Билеты", stay: "осмотр", min: "мин", note: "Заметка",
          summary: "ИТОГИ ПУТЕШЕСТВИЯ", thanks: "Спасибо!", per: "/чел.", agenda: "План на день",
          more: "ещё", photo: "Фото", guide: "Гид", cost: "Ориентировочная стоимость",
          wd: ["воскресенье", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота"] }
  };
  var MONTH_EN = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  var CAT_ICON = { museum: "🏛️", palace: "👑", church: "⛪", fortress: "🏰", monument: "🗿", park_garden: "🌳",
                   square_street: "🏙️", theatre: "🎭", bridge: "🌉", other: "📍" };
  function parseISO(d) { var m = String(d || "").match(/^(\d{4})-(\d{2})-(\d{2})/); return m ? new Date(+m[1], +m[2] - 1, +m[3]) : null; }
  function fmtDay(iso, L) {
    var d = parseISO(iso); if (!d) return "";
    var dd = ("0" + d.getDate()).slice(-2), mm = ("0" + (d.getMonth() + 1)).slice(-2), T = TXT[L] || TXT.vi;
    if (L === "en") return T.wd[d.getDay()] + ", " + d.getDate() + " " + MONTH_EN[d.getMonth()] + " " + d.getFullYear();
    if (L === "ru") return T.wd[d.getDay()] + ", " + dd + "." + mm + "." + d.getFullYear();
    return T.wd[d.getDay()] + ", " + dd + "/" + mm + "/" + d.getFullYear();
  }
  function fmtShortDate(iso, L) { var d = parseISO(iso); if (!d) return ""; var dd = ("0" + d.getDate()).slice(-2), mm = ("0" + (d.getMonth() + 1)).slice(-2);
    return L === "en" ? d.getDate() + " " + MONTH_EN[d.getMonth()] + " " + d.getFullYear() : (L === "ru" ? dd + "." + mm + "." + d.getFullYear() : dd + "/" + mm + "/" + d.getFullYear()); }
  function sayTime(hm, L) { var m = String(hm || "").match(/(\d{1,2}):(\d{2})/); if (!m) return hm || ""; var h = +m[1], mi = +m[2];
    if (L === "vi") return h + " giờ" + (mi ? " " + mi : ""); return h + ":" + m[2]; }
  function sayDate(iso, L) { var d = parseISO(iso); if (!d) return ""; var T = TXT[L] || TXT.vi;
    if (L === "vi") return T.wd[d.getDay()].toLowerCase() + " ngày " + d.getDate() + " tháng " + (d.getMonth() + 1);
    if (L === "en") return T.wd[d.getDay()] + ", " + MONTH_EN[d.getMonth()] + " " + d.getDate();
    return T.wd[d.getDay()] + ", " + d.getDate() + "." + ("0" + (d.getMonth() + 1)).slice(-2); }
  function pt(p, base, L) { return (p && (p[base + "_" + L] || p[base + "_vi"] || p[base + "_en"] || p[base + "_ru"])) || ""; }
  function parr(p, base, L) { var a = p && (p[base + "_" + L] || p[base + "_vi"] || p[base + "_en"]); return Array.isArray(a) ? a : []; }
  function prac(p, key, L) { var r = (p && p.practical) || {}; return r[key + "_" + L] || r[key + "_vi"] || r[key + "_en"] || ""; }
  function modeName(m, L) { return (m && (m[L] || m.vi)) || ""; }

  /* ---------------- 2. MD5 + link ảnh Wikimedia ----------------
     Ảnh trong CSDL dạng commons.wikimedia.org/wiki/Special:FilePath/<tên>. Đổi sang link trực tiếp
     upload.wikimedia.org (có CORS) theo quy tắc băm MD5 của MediaWiki, ưu tiên bản thu nhỏ 1280px. */
  function md5(str) {
    var b = new TextEncoder().encode(str), n = b.length, i;
    var words = new Array(((((n + 8) >> 6) + 1) << 4)).fill(0);
    for (i = 0; i < n; i++) words[i >> 2] |= b[i] << ((i % 4) * 8);
    words[n >> 2] |= 0x80 << ((n % 4) * 8);
    words[words.length - 2] = n * 8;
    var S = [7, 12, 17, 22, 5, 9, 14, 20, 4, 11, 16, 23, 6, 10, 15, 21], K = [];
    for (i = 0; i < 64; i++) K[i] = Math.floor(Math.abs(Math.sin(i + 1)) * 4294967296) | 0;
    var a0 = 1732584193, b0 = -271733879, c0 = -1732584194, d0 = 271733878;
    for (var o = 0; o < words.length; o += 16) {
      var A = a0, B = b0, Cc = c0, D = d0;
      for (var j = 0; j < 64; j++) {
        var f, g, r = j >> 4;
        if (r === 0) { f = (B & Cc) | (~B & D); g = j; }
        else if (r === 1) { f = (D & B) | (~D & Cc); g = (5 * j + 1) % 16; }
        else if (r === 2) { f = B ^ Cc ^ D; g = (3 * j + 5) % 16; }
        else { f = Cc ^ (B | ~D); g = (7 * j) % 16; }
        var tmp = D; D = Cc; Cc = B;
        var x = (A + f + K[j] + words[o + g]) | 0, s = S[r * 4 + (j % 4)];
        B = (B + ((x << s) | (x >>> (32 - s)))) | 0; A = tmp;
      }
      a0 = (a0 + A) | 0; b0 = (b0 + B) | 0; c0 = (c0 + Cc) | 0; d0 = (d0 + D) | 0;
    }
    function hx(v) { var out = ""; for (var k = 0; k < 4; k++) out += ("0" + ((v >>> (k * 8)) & 255).toString(16)).slice(-2); return out; }
    return hx(a0) + hx(b0) + hx(c0) + hx(d0);
  }
  function wfEnc(s) { return encodeURIComponent(s).replace(/%(3B|40|24|21|2A|28|29|2C|2F|7E|3A)/gi, function (m0) { return decodeURIComponent(m0); }); }
  function photoCandidates(url) {
    if (!url) return [];
    var m = String(url).match(/commons\.wikimedia\.org\/wiki\/Special:FilePath\/([^?#]+)/i);
    if (!m) return [url];
    var name; try { name = decodeURIComponent(m[1]); } catch (e) { name = m[1]; }
    name = name.replace(/ /g, "_"); name = name.charAt(0).toUpperCase() + name.slice(1);
    var h = md5(name), enc = wfEnc(name), up = "https://upload.wikimedia.org/wikipedia/commons/", dir = h.charAt(0) + "/" + h.slice(0, 2) + "/";
    var ext = (name.split(".").pop() || "").toLowerCase(), out = [];
    if (/^(jpe?g|png|gif|webp)$/.test(ext)) { out.push(up + "thumb/" + dir + enc + "/1280px-" + enc, up + "thumb/" + dir + enc + "/960px-" + enc, up + dir + enc); }
    else if (ext === "svg") out.push(up + "thumb/" + dir + enc + "/1280px-" + enc + ".png");
    else if (ext === "tif" || ext === "tiff") out.push(up + "thumb/" + dir + enc + "/lossy-page1-1280px-" + enc + ".jpg");
    return out;
  }

  /* ---------------- 3. tải ảnh / ô bản đồ (CORS, hàng đợi, hết giờ) ---------------- */
  var IMG = {}, _q = [], _active = 0, MAXC = 10, _onAsset = null;
  function pump() {
    while (_active < MAXC && _q.length) {
      var job = _q.shift(); _active++;
      (function (job) {
        var im = new Image(), done = false;
        im.crossOrigin = "anonymous"; im.decoding = "async";
        var to = setTimeout(function () { fin(false); }, job.timeout);
        function fin(ok) {
          if (done) return; done = true; clearTimeout(to); _active--;
          job.e.state = ok ? "ok" : "err"; job.e.img = ok ? im : null; job.res(job.e);
          if (_onAsset) { try { _onAsset(); } catch (er) { } }
          pump();
        }
        im.onload = function () { fin(im.naturalWidth > 0); };
        im.onerror = function () { fin(false); };
        im.src = job.url;
      })(job);
    }
  }
  function loadImg(url, timeout) {
    var e = IMG[url]; if (e) return e.p;
    e = IMG[url] = { state: "loading", img: null };
    e.p = new Promise(function (res) { _q.push({ url: url, e: e, res: res, timeout: timeout || 15000 }); });
    pump();
    return e.p;
  }
  function imgReady(url) { var e = IMG[url]; return e && e.state === "ok" ? e.img : null; }
  function imgSettled(url) { var e = IMG[url]; return !!e && e.state !== "loading"; }
  var PHOTO = {};   // id điểm -> {state, img}
  function loadPhoto(st) {
    var key = st.photo; if (!key) return Promise.resolve(null);
    if (PHOTO[key]) return PHOTO[key].p;
    var rec = PHOTO[key] = { state: "loading", img: null };
    var cands = photoCandidates(key);
    rec.p = (async function () {
      for (var i = 0; i < cands.length; i++) { var e = await loadImg(cands[i], 20000); if (e.state === "ok") { rec.state = "ok"; rec.img = e.img; return e.img; } }
      rec.state = "err"; return null;
    })();
    return rec.p;
  }
  function photoOf(st) { var r = st.photo && PHOTO[st.photo]; return r && r.state === "ok" ? r.img : null; }

  /* ---------------- 4. bản đồ Web Mercator ---------------- */
  var BASEMAPS = {
    sat: { max: 17, layers: ["https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                             "https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}"],
           attr: "Ảnh nền: Esri, Maxar, Earthstar Geographics", dim: 0.16 },
    osm: { max: 18, layers: ["https://tile.openstreetmap.org/{z}/{x}/{y}.png"], attr: "© OpenStreetMap contributors", dim: 0.06 },
    plain: { max: 18, layers: [], attr: "", dim: 0 }
  };
  function mx(lon) { return (lon + 180) / 360 * 256; }
  function my(lat) { var s = Math.sin(clamp(lat, -85.05, 85.05) * PI / 180); return (0.5 - Math.log((1 + s) / (1 - s)) / (4 * PI)) * 256; }
  function unLon(x) { return x / 256 * 360 - 180; }
  function unLat(y) { var n = PI - 2 * PI * y / 256; return 180 / PI * Math.atan(0.5 * (Math.exp(n) - Math.exp(-n))); }
  function tileUrl(tpl, z, x, y) { return tpl.replace("{z}", z).replace("{x}", x).replace("{y}", y); }
  // các ô cần cho một khung: camera {x,y,z,fx,fy}; bias < 0 = dùng ô mức thấp hơn (lúc đang bay cho nhẹ)
  function tilesFor(cam, W, H, bm, bias) {
    var out = []; if (!bm.layers.length) return out;
    var tz = clamp(Math.round(cam.z + (bias || 0)), 1, bm.max), sc = Math.pow(2, cam.z - tz), T = 256 * sc, n = 1 << tz;
    var px = cam.x * Math.pow(2, cam.z), py = cam.y * Math.pow(2, cam.z), left = px - cam.fx * W, top = py - cam.fy * H;
    var x0 = Math.floor(left / T), x1 = Math.floor((left + W) / T), y0 = Math.max(0, Math.floor(top / T)), y1 = Math.min(n - 1, Math.floor((top + H) / T));
    for (var ty = y0; ty <= y1; ty++) for (var tx = x0; tx <= x1; tx++) {
      out.push({ z: tz, x: ((tx % n) + n) % n, y: ty, sx: tx * T - left, sy: ty * T - top, T: T });
    }
    return out;
  }
  function drawTiles(ctx, cam, W, H, bm, bias) {
    var tl = tilesFor(cam, W, H, bm, bias);
    for (var L = 0; L < bm.layers.length; L++) {
      var tpl = bm.layers[L];
      for (var i = 0; i < tl.length; i++) {
        var t = tl[i], u = tileUrl(tpl, t.z, t.x, t.y), im = imgReady(u);
        if (im) { ctx.drawImage(im, t.sx, t.sy, t.T + 0.6, t.T + 0.6); continue; }
        if (!IMG[u]) loadImg(u, 15000);                       // xem trước: tải dần ô còn thiếu
        if (L > 0) continue;   // lớp nhãn: thiếu thì thôi
        for (var k = 1; k <= 4 && t.z - k >= 1; k++) {        // tạm dùng ô cha (mờ hơn) cho tới khi ô thật về
          var pz = t.z - k, pxx = t.x >> k, pyy = t.y >> k, pim = imgReady(tileUrl(tpl, pz, pxx, pyy));
          if (!pim) continue;
          var sub = 256 / (1 << k), ox = (t.x - (pxx << k)) * sub, oy = (t.y - (pyy << k)) * sub;
          ctx.drawImage(pim, ox, oy, sub, sub, t.sx, t.sy, t.T + 0.6, t.T + 0.6); break;
        }
      }
    }
  }
  function requestTiles(cam, W, H, bm, bias) {
    var tl = tilesFor(cam, W, H, bm, bias), ps = [];
    bm.layers.forEach(function (tpl) { tl.forEach(function (t) { ps.push(loadImg(tileUrl(tpl, t.z, t.x, t.y), 15000)); }); });
    return ps;
  }
  function drawPlain(ctx, cam, W, H, S) {
    var g = ctx.createLinearGradient(0, 0, W * 0.4, H); g.addColorStop(0, "#21466e"); g.addColorStop(1, "#0c1b30");
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    var k = Math.pow(2, cam.z), left = cam.x * k - cam.fx * W, top = cam.y * k - cam.fy * H;
    var lonA = unLon(left / k), lonB = unLon((left + W) / k), latA = unLat(top / k), latB = unLat((top + H) / k);
    var span = Math.abs(lonB - lonA), steps = [0.01, 0.02, 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10], st = steps[steps.length - 1];
    for (var i = 0; i < steps.length; i++) if (span / steps[i] <= 14) { st = steps[i]; break; }
    ctx.strokeStyle = "rgba(255,255,255,0.07)"; ctx.lineWidth = Math.max(1, S);
    ctx.beginPath();
    for (var lo = Math.ceil(lonA / st) * st; lo <= lonB; lo += st) { var xx = mx(lo) * k - left; ctx.moveTo(xx, 0); ctx.lineTo(xx, H); }
    for (var la = Math.ceil(latB / st) * st; la <= latA; la += st) { var yy = my(la) * k - top; ctx.moveTo(0, yy); ctx.lineTo(W, yy); }
    ctx.stroke();
  }
  function toScreen(cam, W, H, x, y) { var k = Math.pow(2, cam.z); return { x: (x - cam.x) * k + cam.fx * W, y: (y - cam.y) * k + cam.fy * H }; }

  /* bay mượt giữa hai góc nhìn (van Wijk & Nuij, như flyTo của Leaflet/d3) */
  var RHO = Math.SQRT2;
  function cosh(x) { x = Math.exp(x); return (x + 1 / x) / 2; }
  function sinh(x) { x = Math.exp(x); return (x - 1 / x) / 2; }
  function tanh(x) { x = Math.exp(2 * x); return (x - 1) / (x + 1); }
  function zoomPath(c0, c1, W) {
    var ux0 = c0.x, uy0 = c0.y, w0 = W / Math.pow(2, c0.z), ux1 = c1.x, uy1 = c1.y, w1 = W / Math.pow(2, c1.z);
    var dx = ux1 - ux0, dy = uy1 - uy0, d2 = dx * dx + dy * dy, Sv, fn;
    if (d2 < 1e-18) { Sv = Math.log(w1 / w0) / RHO; fn = function (t) { return [ux0 + t * dx, uy0 + t * dy, w0 * Math.exp(RHO * t * Sv)]; }; }
    else {
      var d1 = Math.sqrt(d2), b0 = (w1 * w1 - w0 * w0 + 4 * d2) / (2 * w0 * 2 * d1), b1 = (w1 * w1 - w0 * w0 - 4 * d2) / (2 * w1 * 2 * d1);
      var r0 = Math.log(Math.sqrt(b0 * b0 + 1) - b0), r1 = Math.log(Math.sqrt(b1 * b1 + 1) - b1);
      Sv = (r1 - r0) / RHO;
      fn = function (t) { var s = t * Sv, ch = cosh(r0), u = w0 / (2 * d1) * (ch * tanh(RHO * s + r0) - sinh(r0)); return [ux0 + u * dx, uy0 + u * dy, w0 * ch / cosh(RHO * s + r0)]; };
    }
    return { S: Math.abs(Sv), at: function (t) { var r = fn(t); return { x: r[0], y: r[1], z: Math.log(W / r[2]) / Math.LN2 }; } };
  }
  function fitCam(pts, rect, W, H, maxZ, pad) {
    var x0 = Infinity, x1 = -Infinity, y0 = Infinity, y1 = -Infinity;
    pts.forEach(function (p) { x0 = Math.min(x0, p.x); x1 = Math.max(x1, p.x); y0 = Math.min(y0, p.y); y1 = Math.max(y1, p.y); });
    var bw = Math.max(x1 - x0, 1e-9), bh = Math.max(y1 - y0, 1e-9);
    var z = Math.log(Math.min(rect.w * (1 - 2 * pad) / bw, rect.h * (1 - 2 * pad) / bh)) / Math.LN2;
    return { x: (x0 + x1) / 2, y: (y0 + y1) / 2, z: clamp(z, 3, maxZ), fx: (rect.x + rect.w / 2) / W, fy: (rect.y + rect.h / 2) / H };
  }

  /* ---------------- 5. bố cục theo khung hình ---------------- */
  function layout(W, H) {
    var ar = W / H, S = Math.min(W, H) / 1080;
    if (ar >= 1.2) return {
      kind: "land", S: S, W: W, H: H,
      mapCard: { x: 0, y: 0, w: W * 0.56, h: H * 0.92 },
      card: { x: W * 0.578, y: H * 0.06, w: W * 0.39, h: H * 0.815 },
      mapSide: { x: W * 0.40, y: H * 0.04, w: W * 0.58, h: H * 0.86 },
      panel: { x: W * 0.05, y: H * 0.10, w: W * 0.36, h: H * 0.76 },
      bar: { x: W * 0.05, y: H * 0.915, w: W * 0.47 },
      chipY: H * 0.085, footY: H * 0.972 };
    var mh = ar < 0.8 ? 0.47 : 0.45;
    return {
      kind: ar < 0.8 ? "port" : "square", S: S, W: W, H: H,
      mapCard: { x: 0, y: H * 0.05, w: W, h: H * mh },
      card: { x: W * 0.045, y: H * (mh + 0.06), w: W * 0.91, h: H * (0.955 - mh - 0.06) },
      mapSide: { x: 0, y: H * 0.05, w: W, h: H * mh },
      panel: { x: W * 0.045, y: H * (mh + 0.06), w: W * 0.91, h: H * (0.955 - mh - 0.06) },
      bar: { x: W * 0.045, y: H * 0.03, w: W * 0.91 },
      chipY: H * 0.09, footY: H * 0.985 };
  }

  /* ---------------- 6. chuẩn bị dữ liệu + kịch bản ---------------- */
  var DEF = { aspect: "16:9", res: 720, basemap: "sat", pace: "mid", lang: "vi",
              photo: true, desc: true, hl: true, prac: true, note: true, times: true, cost: false, sign: true,
              title: "", credit: "Phạm Đăng Hiển · fb.com/lopmaybay", voice: true };
  function dims(O) { var s = O.res === 1080 ? 1080 : 720;
    if (O.aspect === "9:16") return { W: s, H: Math.round(s * 16 / 9 / 2) * 2 };
    if (O.aspect === "1:1") return { W: s, H: s };
    return { W: Math.round(s * 16 / 9 / 2) * 2, H: s }; }
  function prepare(data, O) {
    var L = O.lang, stops = [];
    (data.stops || []).forEach(function (s) {
      var p = s.place || {}, c = p.coordinates || {}, lat = +c.lat, lon = +c.lon;
      if (!isFinite(lat) || !isFinite(lon) || (lat === 0 && lon === 0)) return;
      stops.push({ day: +s.day || 1, arr: s.arr || "", dep: s.dep || "", stay: +s.stay || 0, travel: +s.travel || 0,
        mode: s.mode || null, note: s.note || "", cv: +s.cv || 0, cvu: s.cvu,
        lat: lat, lon: lon, x: mx(lon), y: my(lat), custom: !!p.custom,
        name: pt(p, "name", L) || "?", ru: (L !== "ru" ? p.name_ru : p.name_en) || "", cat: (p.categories || [])[0] || "other",
        short: pt(p, "presentation_short", L), hl: parr(p, "highlights", L).slice(0, 3),
        hours: prac(p, "hours", L), ticket: prac(p, "ticket", L), photo: p.photo || "", credit: p.photo_credit || "" });
    });
    stops.forEach(function (s, k) { s.i = k; s.num = k + 1; });
    var dmap = {}; (data.days || []).forEach(function (d) { dmap[d.day] = d; });
    var days = [];
    stops.forEach(function (s) {
      var last = days[days.length - 1];
      if (!last || last.day !== s.day) { var di = dmap[s.day] || {}; last = { day: s.day, date: di.date || "", start: di.start || "", pax: di.pax || "", stops: [] }; days.push(last); }
      last.stops.push(s);
    });
    var title = (O.title || "").trim() || (data.hasTitle && data.title) || ((L === "en" ? "Trip " : L === "ru" ? "Путешествие " : "Hành trình ") + (data.nDays || days.length) + " " + (TXT[L] || TXT.vi).days);
    return { stops: stops, days: days, title: title, date: data.date || (days[0] && days[0].date) || "", lastDate: (days[days.length - 1] || {}).date || "",
             pax: data.pax || "", nDays: data.nDays || days.length, nights: data.nights, km: +data.km || 0, startName: data.startName || "",
             per: data.perPerson || "", group: data.group || "" };
  }
  function buildScenes(D, O, W, H) {
    var LY = layout(W, H), L = O.lang, T = TXT[L] || TXT.vi, bm = BASEMAPS[O.basemap] || BASEMAPS.sat;
    var pace = O.pace === "fast" ? 0.72 : (O.pace === "slow" ? 1.35 : 1);
    var maxZ = Math.min(bm.max, 16.2), scenes = [], tt = 0, N = D.stops.length;
    function push(sc) { sc.t0 = tt; tt += sc.dur; scenes.push(sc); return sc; }
    function stopCam(s) { var c = fitCam([s], LY.mapCard, W, H, Math.min(maxZ, s.cat === "park_garden" ? 14.6 : 15.6), 0.2); return c; }
    function endCam(sc) { return { x: sc.camB.x, y: sc.camB.y, z: sc.camB.z + (sc.drift || 0), fx: sc.camB.fx, fy: sc.camB.fy }; }
    var allCam = fitCam(D.stops, LY.mapSide, W, H, Math.min(maxZ, 15), 0.12);
    // MỞ ĐẦU
    var intro = push({ type: "intro", dur: 6.8 * pace, camA: allCam, camB: allCam, drift: 0.18, flyDur: 0, r0: -1, r1: -1, done: 0,
      narr: D.title + ". " + (L === "vi" ? "Hành trình " + D.nDays + " ngày, " + N + " điểm tham quan" + (D.date ? ", khởi hành " + sayDate(D.date, L) : "") + "."
        : L === "en" ? D.nDays + "-day trip with " + N + " stops" + (D.date ? ", starting " + sayDate(D.date, L) : "") + "."
        : "Путешествие на " + D.nDays + " дн., " + N + " точек" + (D.date ? ", начало: " + sayDate(D.date, L) : "") + ".") });
    intro.previewEnd = 0.7 + Math.min(4.2, 0.5 + N * 0.32) * pace;
    var prevEnd = endCam(intro), done = 0;
    D.days.forEach(function (d) {
      var dc = fitCam(d.stops, LY.mapSide, W, H, Math.min(maxZ, 15), 0.14);
      var nItems = Math.min(d.stops.length, 8);
      var dsc = ({ type: "day", day: d, camA: prevEnd, camB: dc, drift: 0.12, done: done, r0: done - 1, r1: done - 1,
        narr: (L === "vi" ? "Ngày " + d.day + (d.date ? ", " + sayDate(d.date, L) : "") + ". Bắt đầu lúc " + sayTime(d.start || "08:00", L) + ", gồm " + d.stops.length + " điểm."
          : L === "en" ? "Day " + d.day + (d.date ? ", " + sayDate(d.date, L) : "") + ". We start at " + sayTime(d.start || "08:00", L) + " with " + d.stops.length + " stops."
          : "День " + d.day + (d.date ? ", " + sayDate(d.date, L) : "") + ". Начало в " + sayTime(d.start || "08:00", L) + ", точек: " + d.stops.length + ".") });
      // chặng bay sang vùng của ngày mới (có thể rất xa, vd Moskva → Kolomna) dài theo quãng bay
      dsc.flight = zoomPath(dsc.camA, dsc.camB, W); dsc.flyDur = clamp(0.9 + 0.45 * dsc.flight.S, 1.2, 3.8) * pace;
      dsc.dur = dsc.flyDur + clamp(2.6 + 0.42 * nItems, 3, 6.2) * pace;
      push(dsc);
      prevEnd = endCam(dsc);
      d.stops.forEach(function (s) {
        var sc = stopCam(s);
        var tr = { type: "travel", stop: s, camA: prevEnd, camB: sc, drift: 0, done: s.i, r0: s.i - 1, r1: s.i,
          narr: (s.i > 0 && s.travel > 0 && s.mode) ? (L === "vi" ? "Di chuyển bằng " + modeName(s.mode, L).toLowerCase() + ", khoảng " + s.travel + " phút."
            : L === "en" ? "By " + modeName(s.mode, L).toLowerCase() + ", about " + s.travel + " minutes." : modeName(s.mode, L) + ", около " + s.travel + " мин.") : "" };
        tr.flight = zoomPath(tr.camA, tr.camB, W);
        tr.dur = clamp(1.15 + 0.5 * tr.flight.S, 1.7, 4.6) * pace; tr.flyDur = tr.dur;
        push(tr);
        prevEnd = endCam(tr);
        // thẻ điểm
        var chars = s.name.length + (O.desc ? Math.min(s.short.length, 300) : 0) + (O.hl ? s.hl.slice(0, 2).join(" ").length * 0.7 : 0)
                  + (O.prac ? Math.min((s.hours + s.ticket).length, 160) * 0.6 : 0) + (O.note ? Math.min(s.note.length, 180) : 0);
        var st = push({ type: "stop", stop: s, camA: prevEnd, camB: prevEnd, drift: 0.3, flyDur: 0, done: s.i, r0: s.i, r1: s.i,
          dur: clamp(3.6 + chars * 0.016, 6, 12) * pace,
          narr: (L === "vi" ? T.stop + " " + s.num + ": " + s.name + ". " + (s.arr ? "Đến lúc " + sayTime(s.arr, L) + (s.stay ? ", tham quan khoảng " + s.stay + " phút. " : ". ") : "")
                 : L === "en" ? "Stop " + s.num + ": " + s.name + ". " + (s.arr ? "Arrival " + sayTime(s.arr, L) + (s.stay ? ", about " + s.stay + " minutes here. " : ". ") : "")
                 : "Точка " + s.num + ": " + s.name + ". " + (s.arr ? "Прибытие в " + sayTime(s.arr, L) + (s.stay ? ", осмотр около " + s.stay + " мин. " : ". ") : ""))
               + (O.desc && s.short ? s.short + " " : "") + (O.note && s.note ? (L === "vi" ? "Lưu ý: " : L === "en" ? "Note: " : "Заметка: ") + s.note : "") });
        prevEnd = endCam(st);
        done = s.i + 1;
      });
    });
    // KẾT
    var outCam = fitCam(D.stops, LY.mapSide, W, H, Math.min(maxZ, 15), 0.12);
    var out = { type: "outro", dur: 7.2 * pace, camA: prevEnd, camB: outCam, drift: 0.1, done: N, r0: N - 1, r1: N - 1,
      narr: (L === "vi" ? "Hành trình kết thúc: " + N + " điểm trong " + D.nDays + " ngày" + (D.km >= 1 ? ", khoảng " + Math.round(D.km) + " ki-lô-mét" : "") + ". Cảm ơn quý khách đã theo dõi!"
        : L === "en" ? "That's the trip: " + N + " stops in " + D.nDays + " days. Thank you for watching!" : "Итого: " + N + " точек за " + D.nDays + " дн. Спасибо за внимание!") };
    out.flight = zoomPath(out.camA, out.camB, W); out.flyDur = Math.min(2.2, out.dur * 0.35);
    out.t0 = tt; tt += out.dur; scenes.push(out);
    return { scenes: scenes, total: tt, LY: LY, bm: bm, W: W, H: H, N: N, D: D, O: O, T: T };
  }
  function sceneAt(V, t) {
    var sc = V.scenes, lo = 0, hi = sc.length - 1;
    if (t <= 0) return 0; if (t >= V.total) return hi;
    while (lo < hi) { var mid = (lo + hi + 1) >> 1; if (sc[mid].t0 <= t) lo = mid; else hi = mid - 1; }
    return lo;
  }
  function camAt(sc, tau) {
    if (sc.flight && tau < sc.flyDur) {
      var u = ease(tau / sc.flyDur), p = sc.flight.at(u);
      return { x: p.x, y: p.y, z: p.z, fx: lerp(sc.camA.fx, sc.camB.fx, u), fy: lerp(sc.camA.fy, sc.camB.fy, u), moving: (tau / sc.flyDur > 0.1 && tau / sc.flyDur < 0.9) };
    }
    var h = seg(tau, sc.flyDur || 0, sc.dur);
    return { x: sc.camB.x, y: sc.camB.y, z: sc.camB.z + (sc.drift || 0) * h, fx: sc.camB.fx, fy: sc.camB.fy, moving: false };
  }
  function frameState(V, t) {
    var i = sceneAt(V, t), sc = V.scenes[i], tau = t - sc.t0, cam = camAt(sc, tau);
    var r = sc.r1 != null ? sc.r1 : (sc.done || 0) - 1;
    if (sc.type === "travel") r = sc.r0 < 0 ? -1 : lerp(sc.r0, sc.r1, sc.flyDur ? ease(tau / sc.flyDur) : 1);
    if (sc.type === "intro") r = -1;
    return { i: i, sc: sc, tau: tau, cam: cam, r: r };
  }

  /* ---------------- 7. vẽ khung hình ---------------- */
  function wrap(ctx, text, maxW, maxLines) {
    text = String(text || "").replace(/\s+/g, " ").trim(); if (!text) return [];
    var words = text.split(" "), lines = [], cur = "", truncated = false;
    for (var i = 0; i < words.length; i++) {
      var w = words[i], test = cur ? cur + " " + w : w;
      if (ctx.measureText(test).width <= maxW) { cur = test; continue; }
      if (cur) lines.push(cur);
      cur = w;
      while (ctx.measureText(cur).width > maxW && cur.length > 1) {   // từ quá dài -> cắt
        var k = cur.length - 1; while (k > 1 && ctx.measureText(cur.slice(0, k)).width > maxW) k--;
        lines.push(cur.slice(0, k)); cur = cur.slice(k);
      }
      if (maxLines && lines.length >= maxLines) { truncated = true; break; }
    }
    if (!truncated && cur) lines.push(cur);
    if (maxLines && lines.length > maxLines) { lines.length = maxLines; truncated = true; }
    if (truncated && lines.length) {
      var last = lines[lines.length - 1];
      while (last.length > 1 && ctx.measureText(last + "…").width > maxW) last = last.slice(0, -1);
      lines[lines.length - 1] = last.replace(/[\s,.;:–-]+$/, "") + "…";
    }
    return lines;
  }
  function rr(ctx, x, y, w, h, r) { r = Math.max(0, Math.min(r, w / 2, h / 2)); ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath(); }
  function rrTop(ctx, x, y, w, h, r) { ctx.beginPath(); ctx.moveTo(x, y + h); ctx.lineTo(x, y + r); ctx.arcTo(x, y, x + r, y, r); ctx.lineTo(x + w - r, y); ctx.arcTo(x + w, y, x + w, y + r, r); ctx.lineTo(x + w, y + h); ctx.closePath(); }
  function spacing(ctx, px) { if ("letterSpacing" in ctx) ctx.letterSpacing = Math.round(px) + "px"; }
  function txt(ctx, s, x, y, font, color, align, alpha) {
    if (alpha != null && alpha <= 0) return;
    ctx.save(); if (alpha != null) ctx.globalAlpha *= alpha;
    ctx.font = font; ctx.fillStyle = color; ctx.textAlign = align || "left"; ctx.textBaseline = "alphabetic"; ctx.fillText(s, x, y); ctx.restore();
  }
  function appear(tau, start, len) { var a = seg(tau, start, start + (len || 0.55)); return { a: a, dy: (1 - easeOut(a)) }; }

  function drawRoute(ctx, V, fs, pts, S) {
    var N = pts.length; if (N < 2) return;
    var sc = fs.sc, pr = N - 1;
    if (sc.type === "intro") pr = (N - 1) * ease(seg(fs.tau, 0.7, sc.previewEnd));
    // đường xem trước (mờ, nét đứt) cho toàn lộ trình
    ctx.save(); ctx.lineCap = "round"; ctx.lineJoin = "round";
    ctx.setLineDash([10 * S, 11 * S]); ctx.strokeStyle = "rgba(255,255,255,0.62)"; ctx.lineWidth = 3 * S;
    pathTo(ctx, pts, pr); ctx.stroke(); ctx.setLineDash([]);
    // đường đã đi (vàng, sáng)
    var r = fs.r;
    if (r > 0) {
      ctx.strokeStyle = "rgba(15,33,56,0.55)"; ctx.lineWidth = 9 * S; pathTo(ctx, pts, r); ctx.stroke();
      ctx.strokeStyle = "rgba(255,201,77,0.28)"; ctx.lineWidth = 16 * S; pathTo(ctx, pts, r); ctx.stroke();
      ctx.strokeStyle = C.route; ctx.lineWidth = 5 * S; pathTo(ctx, pts, r); ctx.stroke();
    }
    ctx.restore();
    // người đi đường (biểu tượng phương tiện) ở đầu nét khi đang di chuyển
    if (sc.type === "travel" && sc.r0 >= 0 && fs.tau < sc.flyDur) {
      var k = Math.floor(clamp(r, 0, N - 1)), f = clamp(r - k, 0, 1), a = pts[k], b = pts[Math.min(N - 1, k + 1)];
      var hx = lerp(a.x, b.x, f), hy = lerp(a.y, b.y, f);
      ctx.save(); ctx.beginPath(); ctx.arc(hx, hy, 21 * S, 0, 2 * PI); ctx.fillStyle = "#fff"; ctx.shadowColor = "rgba(0,0,0,0.35)"; ctx.shadowBlur = 10 * S; ctx.fill(); ctx.restore();
      txt(ctx, (sc.stop.mode && sc.stop.mode.e) || "🚗", hx, hy + 8.5 * S, F(400, 23 * S), "#000", "center");
    }
  }
  function pathTo(ctx, pts, r) {
    ctx.beginPath(); if (r < 0 || !pts.length) return;
    ctx.moveTo(pts[0].x, pts[0].y);
    var k = Math.floor(r);
    for (var i = 1; i <= k && i < pts.length; i++) ctx.lineTo(pts[i].x, pts[i].y);
    var f = r - k; if (f > 0 && k + 1 < pts.length) ctx.lineTo(lerp(pts[k].x, pts[k + 1].x, f), lerp(pts[k].y, pts[k + 1].y, f));
  }
  function drawMarkers(ctx, V, fs, pts, S) {
    var sc = fs.sc, N = pts.length, cur = sc.type === "stop" ? sc.stop.i : -1, target = sc.type === "travel" ? sc.stop.i : -1;
    var placed = [];
    for (var i = 0; i < N; i++) {
      var vis = 1;
      if (sc.type === "intro") vis = seg(fs.tau, 0.7 + (sc.previewEnd - 0.7) * (N > 1 ? i / (N - 1) : 0) - 0.05, 0.7 + (sc.previewEnd - 0.7) * (N > 1 ? i / (N - 1) : 0) + 0.35);
      if (vis <= 0) continue;
      var state = (sc.type === "outro" || i < sc.done) ? "visited" : (i === cur ? "current" : "future");
      var R = (state === "current" ? 20 : state === "visited" ? 14.5 : (i === target ? 15 : 12)) * S;
      var x = pts[i].x, y = pts[i].y;
      for (var j = 0; j < placed.length; j++) { var q = placed[j]; if (Math.abs(q.x - x) < q.R + R * 0.9 && Math.abs(q.y - y) < q.R + R * 0.9) x = q.x + q.R + R * 0.95; }
      placed.push({ x: x, y: y, R: R });
      var yy = y;
      if (state === "current") yy = y - (1 - bounce(seg(fs.tau, 0, 0.75))) * 60 * S;
      ctx.save(); ctx.globalAlpha *= vis;
      var sca = sc.type === "intro" ? easeOutBack(vis) : 1;
      if (state === "current" || i === target) {
        for (var k2 = 0; k2 < 2; k2++) { var ph = ((V.amb * 0.75 + k2 * 0.5) % 1); ctx.beginPath(); ctx.arc(x, y, R + ph * 42 * S, 0, 2 * PI);
          ctx.strokeStyle = "rgba(232,81,75," + (0.6 * (1 - ph)).toFixed(3) + ")"; ctx.lineWidth = 3 * S; ctx.stroke(); }
      }
      ctx.beginPath(); ctx.arc(x, yy, R * sca, 0, 2 * PI);
      ctx.shadowColor = "rgba(0,0,0,0.35)"; ctx.shadowBlur = 8 * S;
      ctx.fillStyle = state === "current" ? C.red : (state === "visited" ? C.gold2 : "rgba(255,255,255,0.92)"); ctx.fill();
      ctx.shadowBlur = 0; ctx.lineWidth = 3 * S; ctx.strokeStyle = state === "future" ? (i === target ? C.red : "rgba(21,44,78,0.7)") : "#fff"; ctx.stroke();
      ctx.font = F(800, R * 1.0 * sca); ctx.fillStyle = state === "current" ? "#fff" : C.navy; ctx.textAlign = "center"; ctx.textBaseline = "middle";
      ctx.fillText(String(i + 1), x, yy + R * 0.07); ctx.restore();
    }
  }
  function scrim(ctx, LY, W, H) {
    if (LY.kind === "land") {
      var g = ctx.createLinearGradient(0, 0, W * 0.62, 0); g.addColorStop(0, "rgba(9,18,33,0.88)"); g.addColorStop(0.62, "rgba(9,18,33,0.55)"); g.addColorStop(1, "rgba(9,18,33,0)");
      ctx.fillStyle = g; ctx.fillRect(0, 0, W * 0.62, H);
    }
  }
  function dayOffset(sc) { return Math.max(0, (sc.flyDur || 0) - 0.9); }
  // độ đậm của lớp tối bên trái (khung ngang) — vẽ DƯỚI lộ trình & ghim để ghim không bị tối
  function panelAlpha(fs) {
    var sc = fs.sc, tau = fs.tau;
    if (sc.type === "intro") return 1 - seg(tau, sc.dur - 0.6, sc.dur);
    if (sc.type === "day") return (1 - seg(tau, sc.dur - 0.5, sc.dur)) * easeOut(seg(tau - dayOffset(sc), 0, 0.4));
    if (sc.type === "outro") return easeOut(seg(tau, 0.6, 1.3)) * (1 - seg(tau, sc.dur - 0.25, sc.dur));
    return 0;
  }
  function panelBox(ctx, R, S, alpha) {
    ctx.save(); ctx.globalAlpha *= alpha; rr(ctx, R.x, R.y, R.w, R.h, 26 * S);
    ctx.fillStyle = "rgba(15,33,56,0.90)"; ctx.shadowColor = "rgba(0,0,0,0.35)"; ctx.shadowBlur = 24 * S; ctx.fill(); ctx.restore();
  }
  // vẽ một "chồng" dòng chữ, mỗi dòng xuất hiện lần lượt
  function stack(ctx, items, x, y, w, tau, a0, S) {
    var yy = y;
    items.forEach(function (it, idx) {
      if (it.gap) { yy += it.gap; return; }
      ctx.font = it.font; var lines = it.lines || wrap(ctx, it.text, w, it.max || 3);
      var ap = appear(tau, (it.at != null ? it.at : 0.25 + idx * 0.14), 0.55);
      lines.forEach(function (ln) { yy += it.lh; txt(ctx, ln, x, yy + ap.dy * 18 * S, it.font, it.color, "left", ap.a * a0); });
      yy += it.after || 0;
    });
    return yy;
  }
  function measureStack(ctx, items, w) {
    var h = 0; items.forEach(function (it) { if (it.gap) { h += it.gap; return; } ctx.font = it.font; it.lines = wrap(ctx, it.text, w, it.max || 3); h += it.lines.length * it.lh + (it.after || 0); }); return h;
  }

  function drawIntro(ctx, V, fs) {
    var LY = V.LY, S = LY.S, W = V.W, H = V.H, D = V.D, T = V.T, sc = fs.sc, tau = fs.tau;
    var a0 = 1 - seg(tau, sc.dur - 0.6, sc.dur), land = LY.kind === "land";
    if (!land) panelBox(ctx, LY.panel, S, a0 * easeOut(seg(tau, 0, 0.5)));
    var P = LY.panel, pad = land ? 0 : 36 * S, x = P.x + pad, w = P.w - pad * 2, big = land ? 66 : 70;
    var meta = [];
    if (D.date) meta.push("📅 " + fmtShortDate(D.date, V.O.lang) + (D.lastDate && D.lastDate !== D.date ? " → " + fmtShortDate(D.lastDate, V.O.lang) : ""));
    if (D.pax) meta.push("👥 " + D.pax);
    meta.push("🗓️ " + D.nDays + " " + T.days + (D.nights ? " " + D.nights + " " + T.nights : "") + " · 📍 " + V.N + " " + T.stops + (D.km >= 1 ? " · 🚗 ~" + Math.round(D.km) + " " + T.km : ""));
    if (D.startName) meta.push("🚩 " + T.from + ": " + D.startName);
    var items = [{ text: "🧭 " + T.journey, font: F(800, 25 * S), color: C.gold2, lh: 34 * S, after: 12 * S, max: 1, at: 0.2 },
                 { text: D.title, font: F(800, big * S), color: "#fff", lh: big * 1.16 * S, after: 22 * S, max: 3, at: 0.38 }];
    meta.forEach(function (m, k) { items.push({ text: m, font: F(600, 27 * S), color: "#e6edf6", lh: 40 * S, max: 2, at: 0.75 + k * 0.16 }); });
    if (V.O.sign && V.O.credit) items.push({ gap: 26 * S }, { text: (V.O.lang === "vi" ? "🎙️ " + T.guide + ": " : "🎙️ ") + V.O.credit, font: F(700, 23 * S), color: C.gold2, lh: 32 * S, max: 2, at: 1.5 });
    var h = measureStack(ctx, items, w);
    var y0 = P.y + Math.max(land ? 0 : 30 * S, (P.h - h) / 2);
    ctx.save(); spacing(ctx, 0); stack(ctx, items, x, y0, w, tau, a0, S); ctx.restore();
  }
  function drawDay(ctx, V, fs) {
    var LY = V.LY, S = LY.S, W = V.W, H = V.H, T = V.T, sc = fs.sc, d = sc.day, L = V.O.lang;
    var tau = fs.tau - dayOffset(sc);                       // chữ hiện khi chặng bay gần tới nơi
    var a0 = 1 - seg(fs.tau, sc.dur - 0.5, sc.dur), land = LY.kind === "land";
    if (!land) panelBox(ctx, LY.panel, S, a0 * easeOut(seg(tau, 0, 0.4)));
    var P = LY.panel, pad = land ? 0 : 36 * S, x = P.x + pad, w = P.w - pad * 2;
    var head = [{ text: T.day + " " + d.day, font: F(900, 84 * S), color: C.gold2, lh: 86 * S, after: 6 * S, max: 1, at: 0.1 }];
    if (d.date) head.push({ text: fmtDay(d.date, L), font: F(700, 30 * S), color: "#fff", lh: 40 * S, max: 1, at: 0.25 });
    head.push({ text: "▶ " + T.start + " " + (d.start || "08:00") + (d.pax ? " · 👥 " + d.pax + " " + T.pax : ""), font: F(600, 26 * S), color: "#dbe4f0", lh: 36 * S, max: 1, at: 0.35, after: 18 * S });
    var hh = measureStack(ctx, head, w), maxItems = land ? 8 : 7, list = d.stops.slice(0, maxItems), rowH = 44 * S;
    var total = hh + 10 * S + list.length * rowH + (d.stops.length > maxItems ? rowH : 0);
    var y = P.y + Math.max(land ? 0 : 30 * S, (P.h - total) / 2);
    y = stack(ctx, head, x, y, w, tau, a0, S);
    ctx.save(); ctx.globalAlpha *= a0 * seg(tau, 0.45, 0.8); ctx.fillStyle = C.gold; ctx.fillRect(x, y + 2 * S, Math.min(w, 120 * S), 3 * S); ctx.restore();
    y += 16 * S;
    var showTime = V.O.times;
    list.forEach(function (s, k) {
      var ap = appear(tau, 0.55 + k * 0.17, 0.5), ox = (1 - easeOut(ap.a)) * 40 * S, yy = y + rowH * (k + 0.72);
      ctx.save(); ctx.globalAlpha *= ap.a * a0;
      var cx = x + ox + (showTime ? 92 * S : 0) + 17 * S;
      if (showTime) txt(ctx, s.arr || "", x + ox, yy, F(800, 25 * S), C.gold2, "left");
      ctx.beginPath(); ctx.arc(cx, yy - 9 * S, 16 * S, 0, 2 * PI); ctx.fillStyle = C.gold2; ctx.fill();
      ctx.font = F(800, 17 * S); ctx.fillStyle = C.navy; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText(String(s.num), cx, yy - 8 * S);
      ctx.font = F(700, 26 * S); var nm = wrap(ctx, s.name, w - (cx - x) - 30 * S, 1)[0] || "";
      txt(ctx, nm, cx + 28 * S, yy, F(700, 26 * S), "#fff", "left");
      ctx.restore();
    });
    if (d.stops.length > maxItems) txt(ctx, "+ " + (d.stops.length - maxItems) + " " + T.more, x, y + rowH * (list.length + 0.72), F(600, 24 * S), "#c9d4e3", "left", a0 * seg(tau, 0.6 + list.length * 0.17, 1.2 + list.length * 0.17));
  }
  function drawTravelChip(ctx, V, fs) {
    var sc = fs.sc, s = sc.stop, S = V.LY.S, tau = fs.tau, L = V.O.lang, T = V.T;
    var a = easeOut(seg(tau, 0.05, 0.4)) * (1 - seg(tau, sc.dur - 0.35, sc.dur)); if (a <= 0) return;
    var label;
    if (s.i === 0) label = "🚩 " + (V.D.startName ? T.from + ": " + V.D.startName + " → " : "") + s.name;
    else label = ((s.mode && s.mode.e) || "🚗") + " " + modeName(s.mode, L) + (s.travel ? " · " + s.travel + " " + T.min : "") + "  →  " + s.num + ". " + s.name;
    ctx.save(); ctx.font = F(700, 27 * S); label = wrap(ctx, label, V.W * 0.84, 1)[0] || label;
    var tw = ctx.measureText(label).width, pw = tw + 48 * S, ph = 56 * S, x = (V.W - pw) / 2, y = V.LY.chipY + (1 - a) * -20 * S;
    ctx.globalAlpha *= a; rr(ctx, x, y, pw, ph, ph / 2); ctx.fillStyle = "rgba(15,33,56,0.9)"; ctx.shadowColor = "rgba(0,0,0,0.3)"; ctx.shadowBlur = 14 * S; ctx.fill();
    ctx.shadowBlur = 0; ctx.fillStyle = "#fff"; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText(label, V.W / 2, y + ph / 2 + 1 * S);
    ctx.restore();
  }
  function chipRow(ctx, chips, x, y, maxW, S) {
    ctx.font = F(700, 21 * S); var cx = x, cy = y, h = 38 * S, rows = 1;
    chips.forEach(function (c) {
      var w = ctx.measureText(c.t).width + 24 * S;
      if (cx + w > x + maxW && cx > x) { cx = x; cy += h + 8 * S; rows++; }
      rr(ctx, cx, cy, w, h, h / 2); ctx.fillStyle = c.bg; ctx.fill();
      ctx.fillStyle = c.fg; ctx.textAlign = "left"; ctx.textBaseline = "middle"; ctx.fillText(c.t, cx + 12 * S, cy + h / 2 + 1 * S);
      cx += w + 8 * S;
    });
    return rows * h + (rows - 1) * 8 * S;
  }
  function cardModel(ctx, V, s) {
    // dựng nội dung thẻ một lần (theo kích thước), lưu lại để mỗi khung chỉ việc vẽ
    var key = "m_" + V.W + "x" + V.H + "_" + (photoOf(s) ? 1 : 0);
    if (s[key]) return s[key];
    var LY = V.LY, S = LY.S, R = LY.card, O = V.O, T = V.T, L = O.lang, land = LY.kind === "land";
    var pad = 30 * S, w = R.w - pad * 2, img = O.photo ? photoOf(s) : null;
    var photoH = img ? Math.round(R.h * (land ? 0.36 : (LY.kind === "square" ? 0.27 : 0.34))) : Math.round(96 * S);
    var avail = R.h - photoH - pad - 22 * S, items = [];
    items.push({ k: "name", text: s.name, font: F(800, (land ? 38 : 42) * S), color: C.navy, lh: (land ? 45 : 50) * S, max: 2 });
    if (s.ru) items.push({ k: "ru", text: s.ru, font: F(500, 22 * S, true), color: C.muted, lh: 30 * S, max: 1, after: 10 * S });
    var chips = [];
    if (O.times && s.arr) chips.push({ t: "🕘 " + s.arr + (s.dep && s.dep !== s.arr ? "–" + s.dep : ""), bg: C.navy, fg: "#fff" });
    if (O.times && s.stay) chips.push({ t: "⏱ " + s.stay + " " + T.min, bg: "#efeadd", fg: C.navy });
    if (O.cost && s.cv) chips.push({ t: "🎟 " + s.cv.toLocaleString("vi-VN") + (s.cvu === "p" ? T.per : ""), bg: "#efeadd", fg: C.navy });
    var fixedH = 0; items.forEach(function (it) { ctx.font = it.font; it.lines = wrap(ctx, it.text, w, it.max); fixedH += it.lines.length * it.lh + (it.after || 0); });
    ctx.font = F(700, 21 * S);
    var chipH = chips.length ? 38 * S + 14 * S : 0;   // ước lượng 1 hàng
    var left = avail - fixedH - chipH, opt = [];
    function addText(k, text, font, color, lh, maxL, minL, after, extra) {
      if (!text) return; ctx.font = font; var full = wrap(ctx, text, w - (extra || 0), maxL);
      var can = Math.floor((left - (after || 0)) / lh); if (can < (minL || 1)) return;
      var lines = full.length > can ? wrap(ctx, text, w - (extra || 0), can) : full;
      left -= lines.length * lh + (after || 0); opt.push({ k: k, lines: lines, font: font, color: color, lh: lh, after: after || 0, extra: extra || 0 });
    }
    // ghi chú riêng của hướng dẫn viên được ưu tiên giữ chỗ trước phần giới thiệu chung
    var noteFont = F(600, 22.5 * S, true), noteLines = [], noteH = 0;
    if (O.note && s.note) { ctx.font = noteFont; noteLines = wrap(ctx, "📝 " + s.note, w - 20 * S, 2); noteH = noteLines.length * 31 * S + 18 * S;
      if (noteH <= left) left -= noteH; else noteLines = []; }
    if (O.desc) addText("desc", s.short, F(400, 25.5 * S), "#2c3440", 36 * S, land ? 5 : 6, 2, 12 * S);
    if (noteLines.length) opt.push({ k: "note", lines: noteLines, font: noteFont, color: "#5a4a1e", lh: 31 * S, after: 18 * S, extra: 20 * S });
    if (O.hl) s.hl.slice(0, 2).forEach(function (h) { addText("hl", "★ " + h, F(500, 23 * S), "#384150", 32 * S, 2, 1, 6 * S); });
    if (O.prac && s.hours) addText("prac", "🕒 " + T.hours + ": " + s.hours, F(500, 22 * S), "#384150", 31 * S, 1, 1, 4 * S);
    if (O.prac && s.ticket) addText("prac", "🎟 " + T.ticket + ": " + s.ticket, F(500, 22 * S), "#384150", 31 * S, 1, 1, 4 * S);
    var m = { img: img, photoH: photoH, items: items, chips: chips, opt: opt, pad: pad, w: w };
    s[key] = m; return m;
  }
  function drawStopCard(ctx, V, fs) {
    var LY = V.LY, S = LY.S, R = LY.card, sc = fs.sc, s = sc.stop, tau = fs.tau, land = LY.kind === "land";
    var a = easeOut(seg(tau, 0.15, 0.7)), out = seg(tau, sc.dur - 0.5, sc.dur), alpha = a * (1 - out);
    if (alpha <= 0) return;
    var m = cardModel(ctx, V, s), off = (1 - a) * 70 * S + out * 40 * S;
    var x = R.x + (land ? off : 0), y = R.y + (land ? 0 : off), w = R.w, h = R.h;
    ctx.save(); ctx.globalAlpha *= alpha;
    rr(ctx, x, y, w, h, 28 * S); ctx.fillStyle = "rgba(251,248,241,0.97)"; ctx.shadowColor = "rgba(0,0,0,0.38)"; ctx.shadowBlur = 30 * S; ctx.shadowOffsetY = 8 * S; ctx.fill();
    ctx.shadowColor = "transparent"; ctx.shadowBlur = 0; ctx.shadowOffsetY = 0;
    // ảnh (Ken Burns) hoặc dải màu có biểu tượng loại điểm
    ctx.save(); rrTop(ctx, x, y, w, m.photoH, 28 * S); ctx.clip();
    if (m.img) {
      var im = m.img, u = clamp(tau / sc.dur, 0, 1), sca = Math.max(w / im.naturalWidth, m.photoH / im.naturalHeight) * (1.05 + 0.09 * u);
      var dw = im.naturalWidth * sca, dh = im.naturalHeight * sca;
      ctx.drawImage(im, x + (w - dw) * (0.5 + 0.18 * (u - 0.5)), y + (m.photoH - dh) * (0.45 + 0.1 * (u - 0.5)), dw, dh);
      var g = ctx.createLinearGradient(0, y + m.photoH * 0.55, 0, y + m.photoH); g.addColorStop(0, "rgba(0,0,0,0)"); g.addColorStop(1, "rgba(0,0,0,0.42)");
      ctx.fillStyle = g; ctx.fillRect(x, y, w, m.photoH);
      txt(ctx, V.T.photo + ": " + (s.credit || "Wikimedia Commons"), x + w - 14 * S, y + m.photoH - 12 * S, F(500, 15 * S), "rgba(255,255,255,0.85)", "right");
    } else {
      var g2 = ctx.createLinearGradient(x, y, x + w, y + m.photoH); g2.addColorStop(0, C.navy); g2.addColorStop(1, "#2b5c8f");
      ctx.fillStyle = g2; ctx.fillRect(x, y, w, m.photoH);
      txt(ctx, CAT_ICON[s.cat] || "📍", x + w - 60 * S, y + m.photoH * 0.68, F(400, 46 * S), "#fff", "center", 0.9);
    }
    ctx.restore();
    // số thứ tự
    var bx = x + m.pad + 26 * S, by = y + m.photoH;
    ctx.beginPath(); ctx.arc(bx, by, 30 * S, 0, 2 * PI); ctx.fillStyle = C.red; ctx.fill(); ctx.lineWidth = 5 * S; ctx.strokeStyle = "#fff"; ctx.stroke();
    ctx.font = F(800, 28 * S); ctx.fillStyle = "#fff"; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText(String(s.num), bx, by + 1 * S);
    // nội dung
    var cx = x + m.pad, cy = y + m.photoH + 22 * S, k = 0;
    m.items.forEach(function (it) {
      var ap = appear(tau, 0.35 + (k++) * 0.13, 0.5);
      it.lines.forEach(function (ln) { cy += it.lh; txt(ctx, ln, cx, cy + ap.dy * 14 * S, it.font, it.color, "left", ap.a); });
      cy += it.after || 0;
    });
    if (m.chips.length) { var apc = appear(tau, 0.35 + (k++) * 0.13, 0.5); ctx.save(); ctx.globalAlpha *= apc.a; cy += chipRow(ctx, m.chips, cx, cy + 4 * S + apc.dy * 10 * S, m.w, S) + 14 * S; ctx.restore(); }
    m.opt.forEach(function (it) {
      var ap = appear(tau, 0.35 + (k++) * 0.13, 0.5);
      if (it.k === "note") { ctx.save(); ctx.globalAlpha *= ap.a; ctx.fillStyle = "#fff3d6"; rr(ctx, cx - 4 * S, cy + 4 * S, m.w + 8 * S, it.lines.length * it.lh + 14 * S, 10 * S); ctx.fill();
        ctx.fillStyle = C.gold; ctx.fillRect(cx - 4 * S, cy + 4 * S, 5 * S, it.lines.length * it.lh + 14 * S); ctx.restore(); cy += 4 * S; }
      it.lines.forEach(function (ln) { cy += it.lh; txt(ctx, ln, cx + (it.k === "note" ? 14 * S : 0), cy + ap.dy * 12 * S, it.font, it.color, "left", ap.a); });
      cy += it.after;
    });
    ctx.restore();
  }
  function drawOutro(ctx, V, fs) {
    var LY = V.LY, S = LY.S, W = V.W, H = V.H, D = V.D, T = V.T, sc = fs.sc, tau = fs.tau, land = LY.kind === "land", O = V.O;
    var a0 = easeOut(seg(tau, 0.6, 1.3)) * (1 - seg(tau, sc.dur - 0.25, sc.dur));
    if (!land) panelBox(ctx, LY.panel, S, a0);
    var P = LY.panel, pad = land ? 0 : 36 * S, x = P.x + pad, w = P.w - pad * 2;
    var head = [{ text: "🏁 " + T.summary, font: F(800, 25 * S), color: C.gold2, lh: 34 * S, after: 10 * S, max: 1, at: 0.8 },
                { text: D.title, font: F(800, 50 * S), color: "#fff", lh: 58 * S, after: 26 * S, max: 2, at: 0.95 }];
    var stats = [[String(D.nDays), T.days], [String(V.N), T.stops]]; if (D.km >= 1) stats.push(["~" + Math.round(D.km), T.km]);
    var tail = [];
    if (O.cost && D.per) tail.push({ text: "💰 " + T.cost + ": " + D.per + T.per, font: F(700, 26 * S), color: "#fff", lh: 38 * S, max: 2, at: 1.8, after: 6 * S });
    tail.push({ text: T.thanks, font: F(800, 40 * S), color: C.gold2, lh: 52 * S, max: 2, at: 2.0, after: 8 * S });
    if (O.sign && O.credit) tail.push({ text: "🎙️ " + O.credit, font: F(700, 24 * S), color: "#e6edf6", lh: 34 * S, max: 2, at: 2.2 });
    var hh = measureStack(ctx, head, w) + 120 * S + measureStack(ctx, tail, w) + 26 * S;
    var y = P.y + Math.max(land ? 0 : 30 * S, (P.h - hh) / 2);
    y = stack(ctx, head, x, y, w, tau, a0, S);
    var cw = Math.min(w / stats.length, 190 * S);
    stats.forEach(function (st, k) {
      var ap = appear(tau, 1.25 + k * 0.15, 0.5), bx = x + k * cw;
      txt(ctx, st[0], bx, y + 70 * S + ap.dy * 16 * S, F(900, 68 * S), "#fff", "left", ap.a * a0);
      txt(ctx, st[1], bx + 2 * S, y + 104 * S + ap.dy * 16 * S, F(700, 23 * S), C.gold2, "left", ap.a * a0);
    });
    y += 120 * S + 26 * S;
    stack(ctx, tail, x, y, w, tau, a0, S);
  }
  function drawBar(ctx, V, fs) {
    var LY = V.LY, S = LY.S, B = LY.bar, N = V.N, sc = fs.sc, T = V.T, D = V.D; if (N < 2) return;
    var a = sc.type === "intro" ? seg(fs.tau, sc.dur - 1, sc.dur) : (sc.type === "outro" ? 1 - seg(fs.tau, 0.3, 1) : 1); if (a <= 0) return;
    var gap = 10 * S, nd = D.days.length, cell = (B.w - gap * (nd - 1)) / N, cur = sc.type === "stop" ? sc.stop.i : -1, dd = 0, x = B.x;
    ctx.save(); ctx.globalAlpha *= a;
    var dayNow = sc.day ? sc.day.day : (sc.stop ? sc.stop.day : 0), label = "";
    if (dayNow) label = T.day + " " + dayNow + (sc.stop ? " · " + T.stop.toUpperCase() + " " + sc.stop.num + "/" + N : "");
    if (label) txt(ctx, label, B.x, B.y - 10 * S, F(800, 19 * S), "#fff", "left");
    D.days.forEach(function (d) {
      d.stops.forEach(function (s) {
        var on = s.i < sc.done || s.i === cur;
        rr(ctx, x + 1.5 * S, B.y, cell - 3 * S, 7 * S, 3.5 * S);
        ctx.fillStyle = s.i === cur ? C.red : (on ? C.gold2 : "rgba(255,255,255,0.35)"); ctx.fill();
        x += cell;
      });
      dd++; x += gap;
    });
    ctx.restore();
  }
  function renderFrame(ctx, V, t, amb) {
    var W = V.W, H = V.H, S = V.LY.S, fs = frameState(V, t); V.amb = amb != null ? amb : t;
    ctx.save(); ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.globalAlpha = 1;
    ctx.fillStyle = "#0c1b30"; ctx.fillRect(0, 0, W, H);
    if (V.bm.layers.length) {
      drawPlain(ctx, fs.cam, W, H, S);
      drawTiles(ctx, fs.cam, W, H, V.bm, fs.cam.moving ? -1 : 0);
      if (V.bm.dim) { ctx.fillStyle = "rgba(8,16,30," + V.bm.dim + ")"; ctx.fillRect(0, 0, W, H); }
    } else drawPlain(ctx, fs.cam, W, H, S);
    var vg = ctx.createRadialGradient(W / 2, H / 2, Math.min(W, H) * 0.35, W / 2, H / 2, Math.max(W, H) * 0.75);
    vg.addColorStop(0, "rgba(0,0,0,0)"); vg.addColorStop(1, "rgba(0,0,0,0.42)"); ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);
    if (V.LY.kind === "land") { var pa = panelAlpha(fs); if (pa > 0) { ctx.save(); ctx.globalAlpha = pa; scrim(ctx, V.LY, W, H); ctx.restore(); } }
    var pts = V.D.stops.map(function (s) { return toScreen(fs.cam, W, H, s.x, s.y); });
    drawRoute(ctx, V, fs, pts, S);
    drawMarkers(ctx, V, fs, pts, S);
    var ty = fs.sc.type;
    if (ty === "intro") drawIntro(ctx, V, fs);
    else if (ty === "day") drawDay(ctx, V, fs);
    else if (ty === "travel") drawTravelChip(ctx, V, fs);
    else if (ty === "stop") drawStopCard(ctx, V, fs);
    else if (ty === "outro") drawOutro(ctx, V, fs);
    drawBar(ctx, V, fs);
    if (V.bm.attr) txt(ctx, V.bm.attr, 14 * S, V.LY.footY, F(500, 14 * S), "rgba(255,255,255,0.72)", "left");
    if (V.O.sign && V.O.credit) txt(ctx, V.O.credit, W - 16 * S, V.LY.footY, F(700, 17 * S), "rgba(255,255,255,0.82)", "right");
    var fade = Math.max(1 - seg(t, 0, 0.6), seg(t, V.total - 0.8, V.total));
    if (fade > 0) { ctx.fillStyle = "rgba(0,0,0," + fade.toFixed(3) + ")"; ctx.fillRect(0, 0, W, H); }
    ctx.restore();
    return fs;
  }

  /* ---------------- 8. tải trước tài nguyên ---------------- */
  function collectTiles(V, step) {
    var seen = {}, list = [];
    for (var t = 0; t <= V.total; t += step) {
      var fs = frameState(V, Math.min(t, V.total - 0.001));
      tilesFor(fs.cam, V.W, V.H, V.bm, fs.cam.moving ? -1 : 0).forEach(function (tl) {
        V.bm.layers.forEach(function (tpl) { var u = tileUrl(tpl, tl.z, tl.x, tl.y); if (!seen[u]) { seen[u] = 1; list.push(u); } });
      });
    }
    return list;
  }
  async function preloadAll(V, onProg, isCancelled, opts) {
    opts = opts || {};
    var photos = V.D.stops.filter(function (s) { return s.photo && V.O.photo; });
    var np = 0; onProg && onProg("photo", 0, photos.length);
    await Promise.all(photos.map(function (s) { return loadPhoto(s).then(function () { np++; onProg && onProg("photo", np, photos.length); }); }));
    if (isCancelled && isCancelled()) return;
    if (!V.bm.layers.length) return { tiles: 0, failed: 0 };
    var urls = collectTiles(V, opts.step || (1 / 6)), nd = 0, nf = 0;
    if (opts.maxTiles && urls.length > opts.maxTiles) urls = urls.slice(0, opts.maxTiles);
    onProg && onProg("tile", 0, urls.length);
    var startT = Date.now();
    await new Promise(function (res) {
      if (!urls.length) return res();
      var left = urls.length;
      urls.forEach(function (u) { loadImg(u, 15000).then(function (e) { nd++; if (e.state !== "ok") nf++; if (nd % 8 === 0 || nd === urls.length) onProg && onProg("tile", nd, urls.length); if (--left === 0) res(); }); });
      if (opts.timeoutMs) setTimeout(res, opts.timeoutMs);
      var iv = setInterval(function () { if ((isCancelled && isCancelled()) || left === 0) { clearInterval(iv); res(); } }, 300);
    });
    return { tiles: urls.length, failed: nf, ms: Date.now() - startT };
  }
  async function ensureFrame(V, t) {
    var fs = frameState(V, t), ps = requestTiles(fs.cam, V.W, V.H, V.bm, fs.cam.moving ? -1 : 0);
    if (ps.length) await Promise.all(ps);
    if (fs.sc.stop && V.O.photo) await loadPhoto(fs.sc.stop);
  }

  /* ---------------- 9. xuất video ---------------- */
  function loadScript(src) {
    return new Promise(function (res, rej) { var s = document.createElement("script"); s.src = src; s.onload = res; s.onerror = function () { rej(new Error("Không tải được " + src)); }; document.head.appendChild(s); });
  }
  async function pickEncoder(W, H, fps, bitrate) {
    if (!global.VideoEncoder) return null;
    var cands = [["avc1.640028", "avc"], ["avc1.4d0028", "avc"], ["avc1.42e028", "avc"], ["avc1.42001f", "avc"], ["vp09.00.40.08", "vp9"], ["av01.0.08M.08", "av1"]];
    for (var i = 0; i < cands.length; i++) {
      var cfg = { codec: cands[i][0], width: W, height: H, bitrate: bitrate, framerate: fps, latencyMode: "quality" };
      if (cands[i][1] === "avc") cfg.avc = { format: "avc" };
      try { var r = await VideoEncoder.isConfigSupported(cfg); if (r && r.supported) return { cfg: r.config || cfg, mux: cands[i][1] }; } catch (e) { }
    }
    return null;
  }
  async function exportVideo(V, ui) {
    var W = V.W, H = V.H, fps = 30, nFrames = Math.ceil(V.total * fps), cancelled = false;
    ui.onCancel(function () { cancelled = true; });
    var canvas = document.createElement("canvas"); canvas.width = W; canvas.height = H;
    var ctx = canvas.getContext("2d", { alpha: false });
    var bitrate = Math.round(W * H * fps * (V.O.res === 1080 ? 0.085 : 0.095));
    ui.phase("Chuẩn bị bộ mã hoá video…", 0);
    var enc = await pickEncoder(W, H, fps, bitrate);
    var info = await preloadAll(V, function (kind, d, n) {
      ui.phase(kind === "photo" ? "Tải ảnh các điểm: " + d + "/" + n : "Tải ô bản đồ: " + d + "/" + n, n ? d / n : 0);
    }, function () { return cancelled; }) || {};
    if (cancelled) throw new Error("cancel");
    if (enc) {
      if (!global.Mp4Muxer) await loadScript(BASE + "vendor/mp4-muxer.min.js");
      var target = new Mp4Muxer.ArrayBufferTarget();
      var muxer = new Mp4Muxer.Muxer({ target: target, video: { codec: enc.mux, width: W, height: H, frameRate: fps }, fastStart: "in-memory", firstTimestampBehavior: "offset" });
      var encErr = null;
      var encoder = new VideoEncoder({ output: function (chunk, meta) { muxer.addVideoChunk(chunk, meta); }, error: function (e) { encErr = e; } });
      encoder.configure(enc.cfg);
      var t0 = Date.now();
      for (var f = 0; f < nFrames; f++) {
        if (cancelled) { try { encoder.close(); } catch (e) { } throw new Error("cancel"); }
        if (encErr) throw encErr;
        var t = f / fps;
        await ensureFrame(V, t);
        renderFrame(ctx, V, t, t);
        var vf = new VideoFrame(canvas, { timestamp: Math.round(f * 1e6 / fps), duration: Math.round(1e6 / fps) });
        encoder.encode(vf, { keyFrame: f % (fps * 2) === 0 }); vf.close();
        while (encoder.encodeQueueSize > 4) await sleep(4);
        if (f % 10 === 0) {
          var el = (Date.now() - t0) / 1000, eta = f > 30 ? el / f * (nFrames - f) : 0;
          ui.phase("Đang dựng video: " + Math.round(f / nFrames * 100) + "%" + (eta ? " · còn ~" + fmtClock(eta) : ""), f / nFrames);
          await sleep(0);
        }
      }
      await encoder.flush(); encoder.close();
      if (encErr) throw encErr;
      muxer.finalize();
      return { blob: new Blob([target.buffer], { type: "video/mp4" }), ext: "mp4", codec: enc.cfg.codec, info: info };
    }
    // dự phòng: MediaRecorder (ghi theo thời gian thực)
    if (!global.MediaRecorder || !canvas.captureStream) throw new Error("Trình duyệt này không hỗ trợ xuất video. Hãy dùng Chrome hoặc Edge bản mới.");
    var types = ["video/mp4;codecs=avc1", "video/mp4", "video/webm;codecs=vp9", "video/webm;codecs=vp8", "video/webm"], mt = "";
    for (var k = 0; k < types.length; k++) if (MediaRecorder.isTypeSupported(types[k])) { mt = types[k]; break; }
    var stream = canvas.captureStream(fps), rec = new MediaRecorder(stream, mt ? { mimeType: mt, videoBitsPerSecond: bitrate } : { videoBitsPerSecond: bitrate }), chunks = [];
    rec.ondataavailable = function (e) { if (e.data && e.data.size) chunks.push(e.data); };
    var stopped = new Promise(function (r) { rec.onstop = r; });
    rec.start(1000);
    var start = performance.now();
    await new Promise(function (res) {
      function tick() {
        if (cancelled) { rec.stop(); return res(); }
        var t = (performance.now() - start) / 1000;
        if (t >= V.total) { renderFrame(ctx, V, V.total - 0.001, t); rec.stop(); return res(); }
        renderFrame(ctx, V, t, t); ui.phase("Đang ghi video (thời gian thực): " + Math.round(t / V.total * 100) + "%", t / V.total);
        requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    });
    await stopped; if (cancelled) throw new Error("cancel");
    var type = (rec.mimeType || mt || "video/webm").split(";")[0];
    return { blob: new Blob(chunks, { type: type }), ext: /mp4/.test(type) ? "mp4" : "webm", codec: rec.mimeType || mt, info: info };
  }

  /* ---------------- 10. giọng đọc cho chế độ trình chiếu ---------------- */
  var Voice = {
    on: true,
    speak: function (text, L, done) {
      var RT = global.RT;
      if (!text || !this.on) { done && done(); return; }
      if (RT && RT.TTS && RT.TTS.supported) {
        var called = false;
        RT.TTS.speak(text, { lang: L, onState: function (st) { if (st === "end" && !called) { called = true; done && done(); } } });
        return;
      }
      var sy = global.speechSynthesis; if (!sy) { done && done(); return; }
      sy.cancel();
      var loc = L === "en" ? "en-US" : (L === "ru" ? "ru-RU" : "vi-VN"), vs = sy.getVoices() || [];
      var v = vs.filter(function (x) { return x.lang && x.lang.replace("_", "-").toLowerCase().indexOf(loc.slice(0, 2)) === 0; })[0];
      var parts = String(text).match(/[^.!?…]+[.!?…]*\s*/g) || [text], i = 0;
      (function next() { if (i >= parts.length) { done && done(); return; } var u = new SpeechSynthesisUtterance(parts[i++]); u.lang = loc; if (v) u.voice = v; u.onend = next; u.onerror = next; sy.speak(u); })();
    },
    stop: function () { var RT = global.RT; try { if (RT && RT.TTS) RT.TTS.stop(); } catch (e) { } try { global.speechSynthesis && global.speechSynthesis.cancel(); } catch (e) { } }
  };

  /* ---------------- 11. giao diện ---------------- */
  var CSS = ".tv-ov{position:fixed;inset:0;z-index:5000;background:rgba(6,12,22,.86);display:flex;align-items:stretch;justify-content:center;font-family:" + FONT.replace(/"/g, "'") + ";color:#1e2733}" +
    ".tv-box{background:#f7f4ec;width:min(1180px,100%);max-height:100%;overflow:auto;display:flex;flex-direction:column;border-radius:0}" +
    "@media(min-width:900px){.tv-ov{padding:18px}.tv-box{border-radius:16px}}" +
    ".tv-top{display:flex;align-items:center;gap:10px;background:linear-gradient(135deg,#152c4e,#0f2138);color:#fff;padding:12px 16px;position:sticky;top:0;z-index:2}" +
    ".tv-top h2{margin:0;font-size:17px;flex:1}.tv-x{border:1px solid rgba(255,255,255,.35);background:rgba(255,255,255,.1);color:#fff;border-radius:9px;padding:7px 12px;font-weight:800;cursor:pointer;font-size:14px}" +
    ".tv-main{display:grid;grid-template-columns:1fr;gap:14px;padding:14px}@media(min-width:900px){.tv-main{grid-template-columns:minmax(0,1.55fr) minmax(300px,1fr)}}" +
    ".tv-prev{background:#0c1b30;border-radius:12px;overflow:hidden;display:flex;align-items:center;justify-content:center}" +
    ".tv-prev canvas{display:block;max-width:100%;max-height:62vh;width:auto;height:auto}" +
    ".tv-ctl{display:flex;align-items:center;gap:8px;margin-top:8px;flex-wrap:wrap}.tv-ctl input[type=range]{flex:1;min-width:140px}" +
    ".tv-b{border:1px solid #d9d2bd;background:#fff;color:#152c4e;border-radius:10px;padding:8px 12px;font-weight:800;cursor:pointer;font-size:13.5px;min-height:40px}" +
    ".tv-b.gold{background:#c8a24b;border-color:#c8a24b;color:#1a1305}.tv-b.navy{background:#152c4e;border-color:#152c4e;color:#fff}.tv-b:disabled{opacity:.5;cursor:default}" +
    ".tv-lbl{font-size:12.5px;color:#5c6773}.tv-set{display:flex;flex-direction:column;gap:11px}" +
    ".tv-f{display:flex;flex-direction:column;gap:5px}.tv-f>b{font-size:12.5px;color:#152c4e}" +
    ".tv-f input[type=text]{border:1px solid #d9d2bd;border-radius:9px;padding:9px 10px;font-size:14px;font-family:inherit}" +
    ".tv-seg{display:flex;flex-wrap:wrap;gap:6px}.tv-seg button{border:1px solid #d9d2bd;background:#fff;border-radius:999px;padding:6px 11px;font-size:12.5px;font-weight:700;color:#152c4e;cursor:pointer;min-height:34px}" +
    ".tv-seg button.on{background:#152c4e;border-color:#152c4e;color:#fff}.tv-chk{display:flex;flex-wrap:wrap;gap:6px 12px;font-size:13px}.tv-chk label{display:flex;gap:5px;align-items:center;cursor:pointer}" +
    ".tv-go{display:flex;flex-direction:column;gap:8px;margin-top:4px}.tv-go .tv-b{min-height:46px;font-size:14.5px}" +
    ".tv-prog{background:#fff;border:1px solid #e7e3d6;border-radius:12px;padding:12px;display:none}.tv-bar{height:10px;background:#efeadd;border-radius:6px;overflow:hidden;margin:8px 0}.tv-bar i{display:block;height:100%;width:0;background:#c8a24b;transition:width .2s}" +
    ".tv-res{display:none;background:#fff;border:1px solid #e7e3d6;border-radius:12px;padding:12px}.tv-res video{width:100%;max-height:50vh;background:#000;border-radius:8px}" +
    ".tv-note{font-size:12px;color:#5c6773;line-height:1.5}" +
    ".tv-show{position:fixed;inset:0;z-index:6000;background:#000;display:flex;align-items:center;justify-content:center}" +
    ".tv-show canvas{max-width:100vw;max-height:100vh;width:auto;height:auto}" +
    ".tv-sctl{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);display:flex;gap:8px;align-items:center;background:rgba(15,33,56,.88);padding:8px 10px;border-radius:14px;transition:opacity .3s;color:#fff;font-size:13px}" +
    ".tv-sctl button{border:1px solid rgba(255,255,255,.3);background:rgba(255,255,255,.08);color:#fff;border-radius:10px;min-width:44px;min-height:40px;font-size:16px;cursor:pointer}" +
    ".tv-sctl.hide{opacity:0}.tv-sctl .tv-sl{max-width:38vw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;padding:0 6px}";

  function loadOpts() { var o = {}; try { o = JSON.parse(localStorage.getItem("tv_opts") || "{}") || {}; } catch (e) { } var r = {}; for (var k in DEF) r[k] = (o[k] != null ? o[k] : DEF[k]); return r; }
  function saveOpts(O) { try { var c = {}; for (var k in O) if (k !== "title") c[k] = O[k]; localStorage.setItem("tv_opts", JSON.stringify(c)); } catch (e) { } }

  function open(data) {
    if (!data || !data.stops || !data.stops.length) { alert("Lịch trình đang trống — hãy thêm điểm vào tour trước."); return; }
    if (!document.getElementById("tv-css")) { var st = document.createElement("style"); st.id = "tv-css"; st.textContent = CSS; document.head.appendChild(st); }
    var O = loadOpts(); O.title = "";
    var ov = document.createElement("div"); ov.className = "tv-ov";
    ov.innerHTML = '<div class="tv-box"><div class="tv-top"><h2>🎬 Video thuyết trình chuyến đi</h2><button class="tv-x" data-a="close">✕ Đóng</button></div>' +
      '<div class="tv-main"><div><div class="tv-prev"><canvas></canvas></div>' +
      '<div class="tv-ctl"><button class="tv-b" data-a="prev" title="Cảnh trước">⏮</button><button class="tv-b navy" data-a="play">▶ Xem thử</button><button class="tv-b" data-a="next" title="Cảnh sau">⏭</button>' +
      '<input type="range" min="0" max="1000" value="0" data-a="seek"/><span class="tv-lbl" data-v="time">0:00</span></div>' +
      '<div class="tv-lbl" data-v="scene" style="margin-top:4px"></div>' +
      '<div class="tv-prog" data-v="prog"><b data-v="phase">…</b><div class="tv-bar"><i></i></div><button class="tv-b" data-a="cancel">Huỷ</button></div>' +
      '<div class="tv-res" data-v="res"></div></div>' +
      '<div class="tv-set">' +
      '<div class="tv-f"><b>Tiêu đề video</b><input type="text" data-o="title" placeholder="' + escH(data.hasTitle ? data.title : "VD: Moskva – Vành đai Vàng 5 ngày") + '"/></div>' +
      seg3("aspect", "Khung hình", [["16:9", "▭ 16:9 ngang"], ["9:16", "▯ 9:16 dọc (TikTok, Reels, Zalo)"], ["1:1", "◻ 1:1 vuông"]]) +
      seg3("res", "Độ nét", [[720, "720p (nhẹ, dễ gửi)"], [1080, "1080p (nét)"]]) +
      seg3("basemap", "Nền bản đồ", [["sat", "🛰️ Vệ tinh"], ["osm", "🗺️ Bản đồ phố"], ["plain", "◼ Đơn giản (không tải ảnh nền)"]]) +
      seg3("pace", "Nhịp độ", [["fast", "Nhanh"], ["mid", "Vừa"], ["slow", "Chậm"]]) +
      seg3("lang", "Ngôn ngữ chữ & giọng", [["vi", "🇻🇳 Việt"], ["en", "🇬🇧 English"], ["ru", "🇷🇺 Русский"]]) +
      '<div class="tv-f"><b>Hiện trên video</b><div class="tv-chk">' +
      chk("photo", "Ảnh") + chk("desc", "Giới thiệu ngắn") + chk("hl", "Điểm nhấn") + chk("prac", "Giờ mở cửa & vé") + chk("note", "Ghi chú của anh") + chk("times", "Giờ đến–đi") + chk("cost", "Chi phí") + chk("sign", "Chữ ký") + '</div></div>' +
      '<div class="tv-f"><b>Chữ ký (góc video & cuối video)</b><input type="text" data-o="credit"/></div>' +
      '<div class="tv-lbl" data-v="est"></div>' +
      '<div class="tv-go"><button class="tv-b gold" data-a="show">▶ Trình chiếu toàn màn hình (có giọng đọc)</button><button class="tv-b navy" data-a="export">⬇️ Xuất video MP4</button></div>' +
      '<div class="tv-note">Video MP4 không có âm thanh (hình + chữ). Chế độ trình chiếu đọc thuyết minh bằng giọng máy; muốn có file kèm giọng đọc, anh có thể quay màn hình lúc trình chiếu (Windows: Win+Alt+R).<br>Ảnh: Wikimedia Commons. Nền bản đồ: Esri / © OpenStreetMap.</div>' +
      '</div></div></div>';
    document.body.appendChild(ov);
    function seg3(k, label, opts) { return '<div class="tv-f"><b>' + label + '</b><div class="tv-seg" data-k="' + k + '">' + opts.map(function (o) { return '<button data-val="' + o[0] + '">' + o[1] + "</button>"; }).join("") + "</div></div>"; }
    function chk(k, label) { return '<label><input type="checkbox" data-c="' + k + '"/> ' + label + "</label>"; }
    var $ = function (sel) { return ov.querySelector(sel); };
    var canvas = $("canvas"), ctx = canvas.getContext("2d", { alpha: false }), V = null, t = 3.2, poster = true, playing = false, raf = 0, last = 0, dirty = true;
    $('[data-o="credit"]').value = O.credit || "";
    function syncUI() {
      ov.querySelectorAll(".tv-seg").forEach(function (sg) { var k = sg.dataset.k; sg.querySelectorAll("button").forEach(function (b) { b.classList.toggle("on", String(O[k]) === b.dataset.val); }); });
      ov.querySelectorAll("[data-c]").forEach(function (c) { c.checked = !!O[c.dataset.c]; });
    }
    function rebuild() {
      var d = dims(O), D = prepare(data, O);
      canvas.width = d.W; canvas.height = d.H;
      V = buildScenes(D, O, d.W, d.H); t = Math.min(t, V.total);
      var mb = Math.round(V.total * Math.round(d.W * d.H * 30 * (O.res === 1080 ? 0.085 : 0.095)) / 8 / 1048576 * 0.75);
      $('[data-v="est"]').textContent = "⏱ Thời lượng ~" + fmtClock(V.total) + " · " + D.stops.length + " điểm · " + D.days.length + " ngày · dự kiến ~" + mb + " MB (" + d.W + "×" + d.H + ")";
      D.stops.forEach(function (s) { if (O.photo && s.photo) loadPhoto(s); });
      dirty = true; saveOpts(O);
    }
    _onAsset = function () { dirty = true; };
    function draw() { if (!V) return; renderFrame(ctx, V, t, playing ? (performance.now() / 1000) : t); dirty = false;
      $('[data-a="seek"]').value = Math.round(t / V.total * 1000); $('[data-v="time"]').textContent = fmtClock(t) + " / " + fmtClock(V.total);
      var sc = V.scenes[sceneAt(V, t)]; $('[data-v="scene"]').textContent = sceneLabel(sc, V); }
    function loop(ts) {
      raf = requestAnimationFrame(loop);
      if (playing) { var dt = last ? (ts - last) / 1000 : 0; last = ts; t += dt; if (t >= V.total) { t = V.total; playing = false; $('[data-a="play"]').textContent = "▶ Xem thử"; } dirty = true; }
      if (dirty) draw();
    }
    raf = requestAnimationFrame(loop);
    function close() { cancelAnimationFrame(raf); playing = false; _onAsset = null; document.removeEventListener("keydown", esc); ov.remove(); }
    function esc(e) { if (e.key === "Escape" && !document.querySelector(".tv-show")) close(); }
    document.addEventListener("keydown", esc);
    ov.addEventListener("click", function (e) {
      var b = e.target.closest("[data-a],[data-val]"); if (!b) return;
      if (b.dataset.val != null && b.parentNode.dataset.k) { var k = b.parentNode.dataset.k, v = b.dataset.val; O[k] = (k === "res") ? +v : v; syncUI(); rebuild(); return; }
      var a = b.dataset.a;
      if (a === "close") close();
      else if (a === "play") { playing = !playing; last = 0; if (playing && (poster || t >= V.total - 0.05)) t = 0; poster = false; b.textContent = playing ? "⏸ Dừng" : "▶ Xem thử"; }
      else if (a === "prev" || a === "next") { poster = false; var i = sceneAt(V, t + 0.001) + (a === "next" ? 1 : -1); i = clamp(i, 0, V.scenes.length - 1); t = V.scenes[i].t0 + 0.001; dirty = true; }
      else if (a === "show") { playing = false; $('[data-a="play"]').textContent = "▶ Xem thử"; present(data, O); }
      else if (a === "export") doExport();
    });
    ov.addEventListener("input", function (e) {
      var el = e.target;
      if (el.dataset.a === "seek") { poster = false; t = (+el.value / 1000) * V.total; dirty = true; return; }
      if (el.dataset.o) { O[el.dataset.o] = el.value; clearTimeout(el._t); el._t = setTimeout(rebuild, 350); }
    });
    ov.addEventListener("change", function (e) { var el = e.target; if (el.dataset.c) { O[el.dataset.c] = el.checked; rebuild(); } });
    var cancelFn = null;
    async function doExport() {
      playing = false; $('[data-a="play"]').textContent = "▶ Xem thử";
      var prog = $('[data-v="prog"]'), res = $('[data-v="res"]'), btn = $('[data-a="export"]'), bar = prog.querySelector("i");
      prog.style.display = "block"; res.style.display = "none"; btn.disabled = true;
      var d = dims(O), Vx = buildScenes(prepare(data, O), O, d.W, d.H);
      var ui = { phase: function (msg, f) { $('[data-v="phase"]').textContent = msg; bar.style.width = Math.round(clamp(f, 0, 1) * 100) + "%"; }, onCancel: function (fn) { cancelFn = fn; } };
      try {
        var r = await exportVideo(Vx, ui);
        var url = URL.createObjectURL(r.blob), name = slug(prepare(data, O).title) + "-" + O.aspect.replace(":", "x") + "." + r.ext, mb = (r.blob.size / 1048576).toFixed(1);
        var warn = (r.info && r.info.tiles && r.info.failed > r.info.tiles * 0.3) ? '<div class="tv-note" style="color:#b23b34">⚠️ ' + r.info.failed + "/" + r.info.tiles + " ô bản đồ không tải được (mạng chậm hoặc bị chặn) — những chỗ đó dùng nền đơn giản. Có thể thử lại, hoặc chọn nền “Đơn giản”.</div>" : "";
        res.innerHTML = "<b>✅ Xong: " + escH(name) + " · " + mb + " MB · " + fmtClock(Vx.total) + "</b>" + warn + '<video controls playsinline src="' + url + '"></video>' +
          '<div class="tv-ctl"><a class="tv-b gold" href="' + url + '" download="' + escH(name) + '">⬇️ Tải về máy</a>' +
          (navigator.canShare && navigator.canShare({ files: [new File([r.blob], name, { type: r.blob.type })] }) ? '<button class="tv-b" data-a="share">📤 Chia sẻ (Zalo, Messenger…)</button>' : "") + "</div>" +
          '<div class="tv-note">Mã hoá: ' + escH(r.codec || "") + (r.ext !== "mp4" ? " — trình duyệt này chỉ xuất được WebM; dùng Chrome/Edge để có MP4." : "") + "</div>";
        res.style.display = "block";
        var sh = res.querySelector('[data-a="share"]');
        if (sh) sh.onclick = function (ev) { ev.stopPropagation(); navigator.share({ files: [new File([r.blob], name, { type: r.blob.type })], title: name }).catch(function () { }); };
        prog.style.display = "none";
      } catch (err) {
        prog.style.display = "none";
        if (err && err.message === "cancel") { res.innerHTML = '<div class="tv-note">Đã huỷ.</div>'; }
        else { res.innerHTML = '<div class="tv-note" style="color:#b23b34">❌ Lỗi khi xuất video: ' + escH(err && (err.message || err)) + "</div>"; try { console.error(err); } catch (e) { } }
        res.style.display = "block";
      } finally { btn.disabled = false; cancelFn = null; }
    }
    $('[data-a="cancel"]').onclick = function (e) { e.stopPropagation(); if (cancelFn) cancelFn(); };
    syncUI(); rebuild();
    return { close: close };
  }
  function slug(s) { return String(s || "video").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/đ/g, "d").replace(/Đ/g, "D").replace(/[^a-zA-Z0-9]+/g, "-").replace(/^-+|-+$/g, "").toLowerCase().slice(0, 60) || "video-chuyen-di"; }
  function sceneLabel(sc, V) {
    var T = V.T;
    if (sc.type === "intro") return "🎬 Mở đầu";
    if (sc.type === "day") return "📅 " + T.day + " " + sc.day.day;
    if (sc.type === "travel") return "➜ " + sc.stop.num + ". " + sc.stop.name;
    if (sc.type === "stop") return "📍 " + sc.stop.num + ". " + sc.stop.name;
    return "🏁 Tổng kết";
  }

  /* ---------------- 12. trình chiếu toàn màn hình (thời gian thực + giọng đọc) ---------------- */
  function present(data, O0) {
    var O = {}; for (var k in O0) O[k] = O0[k];
    var box = document.createElement("div"); box.className = "tv-show";
    box.innerHTML = '<canvas></canvas><div class="tv-sctl"><button data-p="prev" title="Cảnh trước (←)">⏮</button><button data-p="play" title="Tạm dừng (Space)">⏸</button><button data-p="next" title="Cảnh sau (→)">⏭</button>' +
      '<button data-p="voice" title="Bật/tắt giọng đọc">🔊</button><span class="tv-sl"></span><button data-p="close" title="Thoát (Esc)">✕</button></div>';
    document.body.appendChild(box);
    var canvas = box.querySelector("canvas"), ctx = canvas.getContext("2d", { alpha: false }), ctl = box.querySelector(".tv-sctl"), sl = box.querySelector(".tv-sl");
    // khung trình chiếu theo cỡ màn hình, giữ đúng tỉ lệ đã chọn
    var ratio = O.aspect === "9:16" ? 9 / 16 : (O.aspect === "1:1" ? 1 : 16 / 9);
    var sw = window.innerWidth * (window.devicePixelRatio || 1), sh = window.innerHeight * (window.devicePixelRatio || 1);
    var W = Math.min(1920, sw, sh * ratio), H = W / ratio; if (H > Math.min(1920, sh)) { H = Math.min(1920, sh); W = H * ratio; }
    W = Math.round(W / 2) * 2; H = Math.round(H / 2) * 2; canvas.width = W; canvas.height = H;
    var V = buildScenes(prepare(data, O), O, W, H), idx = 0, tau = 0, playing = true, last = 0, raf = 0, narrDone = true, amb = 0;
    Voice.on = O.voice !== false;
    try { (box.requestFullscreen || box.webkitRequestFullscreen || function () { }).call(box); } catch (e) { }
    preloadAll(V, null, null, { step: 0.5, maxTiles: 600 });
    function startScene(i) {
      idx = clamp(i, 0, V.scenes.length - 1); tau = 0.0001; narrDone = false; Voice.stop();
      var sc = V.scenes[idx]; sl.textContent = sceneLabel(sc, V);
      if (sc.stop && O.photo) loadPhoto(sc.stop);
      var my = idx; setTimeout(function () { if (my !== idx) return; Voice.speak(sc.narr, O.lang, function () { if (my === idx) narrDone = true; }); }, 250);
      // an toàn: máy không có giọng / giọng bị treo thì vẫn chạy tiếp
      setTimeout(function () { if (my === idx) narrDone = true; }, 2750 + (sc.narr ? sc.narr.length * 95 : 0));
    }
    function frame(ts) {
      raf = requestAnimationFrame(frame);
      var dt = last ? Math.min(0.1, (ts - last) / 1000) : 0; last = ts; amb += dt;
      var sc = V.scenes[idx];
      if (playing) {
        var hold = sc.dur - (sc.type === "outro" ? 0.3 : 0.55);
        if (tau + dt >= hold && !narrDone && Voice.on && sc.narr) tau = Math.max(tau, Math.min(hold, tau + dt));  // chờ đọc xong
        else tau += dt;
        if (tau >= sc.dur) { if (idx < V.scenes.length - 1) startScene(idx + 1); else { tau = sc.dur; playing = false; ctl.querySelector('[data-p="play"]').textContent = "▶"; } }
      }
      renderFrame(ctx, V, V.scenes[idx].t0 + Math.min(tau, V.scenes[idx].dur - 0.0001), amb);
    }
    var hideT = 0;
    function poke() { ctl.classList.remove("hide"); clearTimeout(hideT); hideT = setTimeout(function () { ctl.classList.add("hide"); }, 2600); }
    function close() { cancelAnimationFrame(raf); Voice.stop(); document.removeEventListener("keydown", key); try { if (document.fullscreenElement) document.exitFullscreen(); } catch (e) { } box.remove(); }
    function key(e) {
      if (e.key === "Escape") close();
      else if (e.key === " ") { e.preventDefault(); toggle(); }
      else if (e.key === "ArrowRight") startScene(idx + 1);
      else if (e.key === "ArrowLeft") startScene(idx - 1);
      poke();
    }
    function toggle() { playing = !playing; ctl.querySelector('[data-p="play"]').textContent = playing ? "⏸" : "▶";
      if (!playing) Voice.stop(); else if (!narrDone) Voice.speak(V.scenes[idx].narr, O.lang, function () { narrDone = true; }); }
    document.addEventListener("keydown", key);
    box.addEventListener("mousemove", poke); box.addEventListener("touchstart", poke, { passive: true });
    ctl.addEventListener("click", function (e) {
      var b = e.target.closest("[data-p]"); if (!b) return; var a = b.dataset.p;
      if (a === "close") close(); else if (a === "play") toggle();
      else if (a === "next") startScene(idx + 1); else if (a === "prev") startScene(idx - 1);
      else if (a === "voice") { Voice.on = !Voice.on; b.textContent = Voice.on ? "🔊" : "🔇"; if (!Voice.on) { Voice.stop(); narrDone = true; } }
      poke();
    });
    var RT = global.RT, warnVi = O.lang === "vi" && Voice.on && RT && RT.TTS && RT.TTS.hasVietnameseVoice && !RT.TTS.hasVietnameseVoice();
    startScene(0); raf = requestAnimationFrame(frame); poke();
    if (warnVi) sl.textContent = "⚠️ Máy chưa có giọng tiếng Việt — giọng đọc có thể không chuẩn";
  }

  global.TourVideo = { open: open, present: present, version: VERSION,
    _t: { md5: md5, photoCandidates: photoCandidates, prepare: prepare, buildScenes: buildScenes, renderFrame: renderFrame, exportVideo: exportVideo, frameState: frameState, collectTiles: collectTiles, dims: dims, DEF: DEF } };
})(window);
