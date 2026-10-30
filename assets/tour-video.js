/* =====================================================================
   tour-video.js — 🎬 Video thuyết trình chuyến đi · Cẩm nang Du lịch
   Tác giả nội dung: Phạm Đăng Hiển · fb.com/lopmaybay

   Dựng video từ Bảng lịch trình: mở đầu → từng ngày (lịch trình trong ngày)
   → bay giữa các điểm, lộ trình tự vẽ dần → thẻ thông tin từng điểm (ảnh, giờ,
   giới thiệu ĐẦY ĐỦ chia trang, điểm nhấn, giờ mở cửa, vé, ghi chú) → tổng kết + mã QR.

   v2:
   - Thuyết minh có tiếng ngay trong file MP4: giọng AI chạy trên máy (Piper — VAIS-1000 tiếng Việt,
     denis tiếng Nga, LJSpeech tiếng Anh), tên tiếng Nga viết La-tinh được đổi về chữ Kirin và đọc
     bằng giọng Nga; giờ phút/đơn vị/số La Mã được đọc đúng kiểu tiếng Việt (1h30p → 1 giờ 30 phút).
   - Nhạc nền: 4 bản dựng sẵn (tự tổng hợp, không vướng bản quyền) hoặc nhạc của anh; tự giảm nhỏ khi đọc.
   - Phụ đề (+ file .srt), chữ trên thẻ sáng theo lời đọc, đồng hồ hành trình, mã QR cuối video,
     ảnh bìa, mục lục chương cho YouTube.
   - Xuất MP4: WebCodecs (H.264 + AAC, dự phòng Opus) + mp4-muxer (assets/vendor/mp4-muxer.min.js, MIT).
     Dự phòng cuối: MediaRecorder. Trình chiếu toàn màn hình: giọng AI hoặc giọng có sẵn của máy (Việt + Nga).
   Chạy hoàn toàn trên trình duyệt. Ô bản đồ (Esri/OSM) và ảnh Wikimedia được tải với CORS.

   v2.1: TourVideo.lib (bộ công cụ dùng chung cho nghe-thuat/art-video.js), exportVideo nhận V.preload/V.ensure/V.render,
         thêm 2 bản nhạc: 🎋 Ngũ cung (đàn tranh, sáo — điệu ngũ cung Việt) và 🕯️ Suy ngẫm (piano, nền tĩnh).

   Gọi: TourVideo.open(data)  — data do gis.html gom (xem videoData() trong gis.html).
   ===================================================================== */
(function (global) {
  "use strict";
  var VERSION = "2.1";
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
          more: "điểm nữa", photo: "Ảnh", guide: "Hướng dẫn viên", cost: "Chi phí dự kiến", qr: "Quét mã để liên hệ", warn: "Lưu ý",
          wd: ["Chủ nhật", "Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy"] },
    en: { journey: "THE JOURNEY", day: "DAY", days: "days", nights: "nights", stops: "stops", stop: "Stop", km: "km", pax: "guests",
          start: "Start", from: "Starting from", hours: "Opening hours", ticket: "Tickets", stay: "visit", min: "min", note: "Note",
          summary: "TRIP SUMMARY", thanks: "Thank you!", per: "/person", agenda: "Today's plan",
          more: "more stops", photo: "Photo", guide: "Guide", cost: "Estimated cost", qr: "Scan to contact", warn: "Note",
          wd: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] },
    ru: { journey: "ПУТЕШЕСТВИЕ", day: "ДЕНЬ", days: "дн.", nights: "ноч.", stops: "точек", stop: "Точка", km: "км", pax: "гостей",
          start: "Начало", from: "Отправление", hours: "Часы работы", ticket: "Билеты", stay: "осмотр", min: "мин", note: "Заметка",
          summary: "ИТОГИ ПУТЕШЕСТВИЯ", thanks: "Спасибо!", per: "/чел.", agenda: "План на день",
          more: "ещё", photo: "Фото", guide: "Гид", cost: "Ориентировочная стоимость", qr: "Сканируйте для связи", warn: "Обратите внимание",
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

  /* ================= 6. ĐỌC THÀNH TIẾNG: chuẩn hoá chữ + tách đoạn tiếng Nga =================
     Bài viết tiếng Việt về nước Nga có rất nhiều tên Nga viết bằng chữ La-tinh (Kolomna, Sergiyev Posad,
     Spaso-Preobrazhensky…) — giọng tiếng Việt đọc sai. Ở đây:
       • chuẩn hoá ký hiệu cho giọng Việt: 1h30p → "1 giờ 30 phút", 08:45 → "8 giờ 45", 10:00–18:00 → "… đến …",
         ~300 RUB/người → "khoảng 300 rúp một người", 2.867 m → "2867 mét", thế kỷ XIX → "thế kỷ 19", Nikolai II → "… đệ nhị"…
       • nhận ra từ tiếng Nga (La-tinh hoá) → đổi ngược về chữ Kirin (Коломна, Сергиев Посад…) để GIỌNG NGA đọc:
         từ điển tay + kho từ Kirin lấy từ chính CSDL (name_ru, nguồn) + quy tắc chuyển tự ngược.
       • kết quả: danh sách đoạn [{l:'vi'|'ru'|'en', t:'…'}] — mỗi đoạn đọc bằng giọng đúng ngôn ngữ. */
  var SAY = (function () {
    var VIC = "àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ";
    var reVIC = new RegExp("[" + VIC + "]");
    var reSYL = /^(?:ngh|ng|nh|ch|gh|gi|kh|ph|th|tr|qu|[bcdghklmnprstvx])?(?:a|ai|ao|au|ay|am|an|ang|anh|e|em|en|eo|i|ia|iu|im|in|inh|o|oa|oai|oay|oan|oang|oanh|oam|oe|oen|oeo|oi|om|on|ong|oong|u|ua|ui|um|un|ung|uy|uya|uyn|uynh|uyu|y)$/;
    var CYR = /[Ѐ-ӿ]/;
    function RX(src, fl) { try { return new RegExp(src, fl == null ? "gu" : fl); } catch (e) { return null; } }
    var EMO = RX("[\\u{1F000}-\\u{1FAFF}\\u{2600}-\\u{27BF}\\u{2B00}-\\u{2BFF}\\u{2300}-\\u{23FF}\\u{25A0}-\\u{25FF}\\u{FE0F}\\u{200D}\\u{20E3}\\u{E0020}-\\u{E007F}]") || /[️‍]/g;
    function isVi(w) {
      var lw = String(w).toLowerCase(); if (reVIC.test(lw)) return true;
      var ps = lw.split(/[-'’]/); for (var i = 0; i < ps.length; i++) if (ps[i] && !reSYL.test(ps[i])) return false;
      return true;
    }
    function isAcr(w) { return w.length >= 2 && w.length <= 7 && /^[A-Z][A-Za-z]*$/.test(w) && (w.match(/[A-Z]/g) || []).length >= 2 && !/[a-z]{3}/.test(w); }
    function up1(s) { return s ? s.charAt(0).toUpperCase() + s.slice(1) : s; }
    function roman(s) {
      s = String(s || "").toUpperCase(); if (!/^[IVXLC]+$/.test(s)) return 0;
      var m = { I: 1, V: 5, X: 10, L: 50, C: 100 }, n = 0, prev = 0;
      for (var i = s.length - 1; i >= 0; i--) { var v = m[s.charAt(i)]; if (v < prev) n -= v; else { n += v; prev = v; } }
      return n;
    }
    var WD = ["", "", "hai", "ba", "tư", "năm", "sáu", "bảy"];
    var ORD = ["", "nhất", "nhị", "tam", "tứ", "ngũ", "lục", "thất", "bát", "cửu", "thập"];
    var ORD_EN = ["", "the First", "the Second", "the Third", "the Fourth", "the Fifth", "the Sixth", "the Seventh", "the Eighth", "the Ninth", "the Tenth"];

    /* ---- từ điển tay ----
       TR: cách viết La-tinh của tên/từ Nga → chữ Kirin (dùng cả khi đọc tiếng Việt lẫn tiếng Anh)
       EX: tên tiếng Anh của địa danh Nga (Moscow, Kremlin…) → Kirin (chỉ khi đọc tiếng Việt)
       VI: từ tiếng Anh / thuật ngữ hay gặp → phiên âm cho giọng Việt
       Khoá bắt đầu bằng ^ = chỉ khớp khi viết hoa chữ đầu. */
    var TR = {}, EX = {}, VI = {};
    function load(dst, str) { str.split("|").forEach(function (kv) { var i = kv.indexOf(":"); if (i < 1) return; var k = kv.slice(0, i), cap = k.charAt(0) === "^"; if (cap) k = k.slice(1); dst[k] = { v: kv.slice(i + 1), cap: cap }; }); }
    load(TR, "pyotr:Пётр|nikolai:Николай|nikolay:Николай|aleksandr:Александр|alexandr:Александр|mikhail:Михаил|ekaterina:Екатерина|yekaterina:Екатерина|" +
      "elizaveta:Елизавета|georgy:Георгий|georgiy:Георгий|pavel:Павел|andrei:Андрей|andrey:Андрей|sergiy:Сергий|sergei:Сергей|sergey:Сергей|serafim:Серафим|" +
      "vasily:Василий|vasiliy:Василий|vasili:Василий|dmitry:Дмитрий|dmitri:Дмитрий|dmitriy:Дмитрий|yuri:Юрий|yury:Юрий|yuriy:Юрий|grigory:Григорий|grigori:Григорий|" +
      "anatoly:Анатолий|valery:Валерий|arkady:Аркадий|afanasy:Афанасий|gennady:Геннадий|innokenty:Иннокентий|yevgeny:Евгений|evgeny:Евгений|evgeni:Евгений|" +
      "aleksei:Алексей|alexei:Алексей|aleksey:Алексей|alexey:Алексей|ilya:Илья|igor:Игорь|olga:Ольга|sofia:Софья|sofya:Софья|tatiana:Татьяна|tatyana:Татьяна|" +
      "natalia:Наталья|natalya:Наталья|daria:Дарья|darya:Дарья|anna:Анна|maria:Мария|marina:Марина|yaroslavl:Ярославль|tchaikovsky:Чайковский|tolstoy:Толстой|" +
      "dostoevsky:Достоевский|dostoyevsky:Достоевский|chekhov:Чехов|gogol:Гоголь|rachmaninoff:Рахманинов|rachmaninov:Рахманинов|vrubel:Врубель|" +
      "yeltsin:Ельцин|gorbachev:Горбачёв|rurik:Рюрик|yenisei:Енисей|yenisey:Енисей|^ob:Обь|^don:Дон|^perm:Пермь|kazan:Казань|tver:Тверь|ryazan:Рязань|" +
      "suzdal:Суздаль|tyumen:Тюмень|izmailovo:Измайлово|izmaylovo:Измайлово|bolshoi:Большой|mariinsky:Мариинский|novodevichy:Новодевичий|tretyakov:Третьяков|" +
      "tretyakovka:Третьяковка|lubyanka:Лубянка|polyana:Поляна|ges:ГЭС|^gum:ГУМ|tsum:ЦУМ|vdnkh:ВДНХ|mkad:МКАД|mgu:МГУ|gulag:ГУЛАГ|nkvd:НКВД|kgb:КГБ|ussr:СССР|" +
      "izba:изба|samovar:самовар|matryoshka:матрёшка|matreshka:матрёшка|balalaika:балалайка|kokoshnik:кокошник|datsan:дацан|stanitsa:станица|aul:аул|" +
      "pustyn:пустынь|terem:терем|ostrog:острог|kurgan:курган|nerpa:нерпа|pryanik:пряник|pastila:пастила|banya:баня|kvass:квас|kvas:квас|borscht:борщ|" +
      "borsch:борщ|blini:блины|bliny:блины|pelmeni:пельмени|ataman:атаман|boyar:боярин|streltsy:стрельцы|voevoda:воевода|dacha:дача|shatyor:шатёр|" +
      "iconostas:иконостас|zvonnitsa:звонница|sobor:собор|muzey:музей|tserkov:церковь|khram:храм|monastyr:монастырь|ploshchad:площадь|ulitsa:улица|" +
      "prospekt:проспект|naberezhnaya:набережная|ozero:озеро|reka:река|zapovednik:заповедник|usadba:усадьба|kreml:кремль|sloboda:слобода|posad:посад|" +
      "oblast:область|krai:край|kray:край|okrug:округ|skete:скит|skit:скит|jordan:Иордан|sankt-peterburg:Санкт-Петербург|peterburg:Петербург|moskva-reka:Москва-река");
    load(EX, "moscow:Москва|kremlin:Кремль|kremlins:кремли|hermitage:Эрмитаж|siberia:Сибирь|petersburg:Петербург|peterhof:Петергоф|crimea:Крым|" +
      "caucasus:Кавказ|urals:Урал|chechnya:Чечня|yakutia:Якутия|isaac:Исаакий|basil:Василий|^peter:Пётр|nicholas:Николай|alexander:Александр|" +
      "catherine:Екатерина|elizabeth:Елизавета|^michael:Михаил|^george:Георгий|^paul:Павел|^andrew:Андрей|sergius:Сергий|seraphim:Серафим|^city:Сити|" +
      "venice:Венеция|^paris:Париж|^rome:Рим|jerusalem:Иерусалим|chagall:Шагал|faberge:Фаберже|fabergé:Фаберже|quarenghi:Кваренги|montferrand:Монферран|" +
      "trinity:Троица|^volga:Волга|apollo:Аполлон|neptune:Нептун|samson:Самсон|^napoleon:Наполеон");
    load(VI, "unesco:U-nét-xcô|tour:tua|tours:tua|trekking:trếch-kinh|trek:trếch|check-in:chéc-in|checkin:chéc-in|homestay:hôm-xtây|resort:ri-dọt|" +
      "spa:xpa|kayak:kai-ắc|kayaking:kai-ắc|rafting:ráp-tinh|zipline:díp-lai|combo:com-bô|show:sô|bar:ba|pub:pắp|cafe:cà phê|café:cà phê|menu:mê-nu|" +
      "buffet:búp-phê|online:on-lai|wifi:oai-phai|wi-fi:oai-phai|selfie:xen-phi|camping:cam-pinh|picnic:píc-níc|safari:xa-pha-ri|festival:phét-xti-van|" +
      "park:pác|video:vi-đi-ô|studio:xtu-đi-ô|game:ghêm|jazz:giắc|rock:rốc|ok:ô-kê|top:tốp|view:viu|workshop:uốc-sốp|masterclass:lớp học|food:phút|" +
      "hall:hôn|mini:mi-ni|hi-tech:hai-tếch|laser:la-de|logo:lô-gô|euro:ơ-rô|metro:mê-trô|taxi:tắc-xi|bus:buýt|catamaran:ca-ta-ma-ran|souvenir:quà lưu niệm|" +
      "audio:âu-đi-ô|audioguide:thuyết minh tự động|audio-guide:thuyết minh tự động|gothic:Gô-tích|neo-gothic:tân Gô-tích|pseudo-gothic:giả Gô-tích|" +
      "baroque:ba-rốc|barok:ba-rốc|rococo:rô-cô-cô|byzantine:Bi-dăng-tin|renaissance:Phục Hưng|classicism:cổ điển|neoclassical:tân cổ điển|" +
      "constructivism:kiến tạo|modern:mô-đéc|^art:át|nouveau:nu-vô|ampir:am-pia|empire:am-pia|avant-garde:tiên phong|opera:ô-pê-ra|operetta:ô-pê-rét|" +
      "opereta:ô-pê-rét|ballet:ba-lê|musical:nhạc kịch|organ:oóc-gan|piano:pi-a-nô|guitar:ghi-ta|tenor:tê-no|baritone:ba-ri-tôn|icon:i-côn|icons:i-côn|" +
      "fresco:bích hoạ|frescoes:bích hoạ|minaret:mi-na-rét|mausoleum:lăng|obelisk:ô-bê-lít|rotunda:rô-tun-đa|colonnade:hàng cột|bastion:pháo đài|" +
      "panorama:pa-nô-ra-ma|diorama:đi-ô-ra-ma|planetarium:cung thiên văn|oceanarium:thuỷ cung|aquarium:thuỷ cung|dendrarium:vườn cây|arboretum:vườn cây|" +
      "necropolis:khu mộ cổ|stupa:bảo tháp|granite:gra-nít|granit:gra-nít|marble:cẩm thạch|karst:các-xtơ|basalt:ba-dan|bazan:ba-dan|taiga:tai-ga|" +
      "tundra:tun-đra|geyser:mạch nước phun|fjord:vịnh hẹp|canyon:hẻm núi|plateau:cao nguyên|caldera:miệng núi lửa|glacier:sông băng|tulip:tu-líp|" +
      "bison:bò rừng|mammoth:voi ma-mút|olympic:Ô-lim-pích|olympics:Ô-lim-pích|cossack:Cô-dắc|cossacks:Cô-dắc|saint:Xanh|nobel:Nô-ben|" +
      "lhq:Liên Hợp Quốc|beatles:Bít-tồn|grand:gran|prix:pri|arena:a-rê-na|gallery:ga-le-ri|art-gallery:phòng tranh|world:uơn|cup:cúp|fifa:Phi-pha|spa-resort:khu nghỉ dưỡng");
    var EN_STOP = {}; ("park opera center centre museum hotel metro tour art gallery theatre theater palace church cathedral monastery river lake square street " +
      "avenue bridge garden gardens tower gate house hall station island mount mountain hill bay sea national central state russian soviet victory memorial " +
      "monument old new great grand saint st little big red white black blue golden green upper lower north south east west the of and ring road " +
      "believers lake pillars falls valley canyon cave caves forest beach resort village town city castle fortress museum-reserve reserve nature wildlife " +
      "republic region district gallery collection exhibition centre center culture cultural heritage world war peace love history historical science " +
      "space music theatre ballet opera art arts modern contemporary fine folk house-museum estate manor tea coffee cafe restaurant bar club hotel " +
      "airport port harbour harbor market mall shop store bay cape peninsula glacier volcano hot springs spring waterfall trail path wood musk bison").split(" ").forEach(function (w) { EN_STOP[w] = 1; });
    function dget(D, w) { var e = D[w.toLowerCase().replace(/’/g, "'")]; return e && (!e.cap || /^[A-ZÀ-Ỹ]/.test(w)) ? e : null; }
    function caseLike(src, cy) { return /^[A-Z]/.test(src) ? up1(cy) : cy; }

    /* ---- chuyển tự ngược La-tinh → Kirin ---- */
    var C1 = { a: "а", b: "б", v: "в", g: "г", d: "д", z: "з", k: "к", l: "л", m: "м", n: "н", o: "о", p: "п", r: "р", s: "с", t: "т", u: "у", f: "ф", h: "х", c: "к", x: "кс", w: "в", q: "к" };
    var DI = [["shch", "щ"], ["sch", "щ"], ["dzh", "дж"], ["tch", "ч"], ["zh", "ж"], ["kh", "х"], ["ch", "ч"], ["sh", "ш"], ["ts", "ц"], ["tz", "ц"], ["ph", "ф"], ["th", "т"], ["ck", "к"]];
    var CONS = /[бвгджзйклмнпрстфхцчшщ]/, VOWC = /[аеёиоуыэюя]/;
    function rtWord(w) {
      var s = String(w).toLowerCase().replace(/’/g, "'"), o = "", i = 0, n = s.length, seenV = false;
      while (i < n) {
        var ch = s.charAt(i), rest = s.slice(i), hit = null, k;
        for (k = 0; k < DI.length; k++) if (rest.indexOf(DI[k][0]) === 0) { hit = DI[k]; break; }
        if (hit) { o += hit[1]; i += hit[0].length; continue; }
        if (ch === "'") { if (o && CONS.test(o.slice(-1))) o += "ь"; i++; continue; }
        if ((ch === "y" || ch === "j") && i + 1 < n && /[aeiou]/.test(s.charAt(i + 1))) {
          var pc = o.slice(-1);
          if (pc && CONS.test(pc) && seenV && pc !== "й") o += "ь";       // Ilya → Илья, Podmoskovye → Подмосковье
          o += { a: "я", u: "ю", e: "е", o: "ё", i: "и" }[s.charAt(i + 1)]; i += 2; seenV = true; continue;
        }
        if (ch === "y" || ch === "j") {
          var p2 = o.slice(-1);
          if (!p2 || VOWC.test(p2)) { o += "й"; i++; continue; }        // Maykop, Bolshoy
          if (i === n - 1) { o += (/[кгхжчшщ]$/.test(o) || /[жхш]н$/.test(o)) ? "ий" : "ый"; i++; continue; }   // Uspensky, Nizhny, Krasny
          o += "ы"; i++; seenV = true; continue;                         // Vyborg, Tsaritsyno
        }
        if (ch === "i") {
          var p3 = o.slice(-1);
          if (i === n - 2 && s.charAt(n - 1) === "a" && p3 && CONS.test(p3)) { o += "ия"; i += 2; continue; }   // Khakassia → Хакассия
          if (p3 && /[аоеуэ]/.test(p3) && (i === n - 1 || !/[aeiouy]/.test(s.charAt(i + 1)))) { o += "й"; i++; continue; }   // Baikal, Nikolai
          if (p3 === "и" && i === n - 1) { o += "й"; i++; continue; }
          o += "и"; i++; seenV = true; continue;
        }
        if (ch === "e") { o += i === 0 ? "э" : "е"; i++; seenV = true; continue; }
        var c = C1[ch]; if (c) { o += c; if (ch === "a" || ch === "o" || ch === "u") seenV = true; i++; continue; }
        o += ch; i++;
      }
      return o;
    }
    var INI = { E: "Е", Yu: "Ю", Ya: "Я", Ye: "Е", Yo: "Ё", Zh: "Ж", Kh: "Х", Ts: "Ц", Ch: "Ч", Sh: "Ш" };
    function iniCyr(x) { return INI[x] || up1(rtWord(x)); }
    function rtAcr(w) {
      var o = "", i = 0, M = { A: "А", B: "Б", V: "В", G: "Г", D: "Д", E: "Э", Z: "З", I: "И", K: "К", L: "Л", M: "М", N: "Н", O: "О", P: "П", R: "Р", S: "С", T: "Т", U: "У", F: "Ф", H: "Х", C: "Ц", X: "Х", Y: "Ы", W: "В", J: "Й", Q: "К" };
      while (i < w.length) {
        var two = w.substr(i, 2), t2 = two.charAt(0).toUpperCase() + two.charAt(1).toLowerCase();
        if (INI[t2] && t2 !== "E" && two.length === 2) { o += INI[t2]; i += 2; continue; }
        o += M[w.charAt(i).toUpperCase()] || w.charAt(i); i++;
      }
      return o;
    }
    var RUISH = /(?:zh|kh|shch|tsk|tsy|ts$|sk(?:y|iy|ii|aya|oye|oe|ie)?$|ov[ao]?$|ev[ao]?$|yov|yev|ovo$|evo$|ino$|aya$|oye$|yy$|iy$|nik$|ets$|grad$|gorod$|^[bcdfgklmnprstvz]y[aeou])/;

    /* ---- kho từ Kirin lấy từ CSDL: khớp "gần đúng" (bỏ qua ь/ъ, й/и, ы/и, ё/е, э/е, phụ âm đôi, тс/ц) ---- */
    var VOC = null;
    function canon(c) { return String(c).toLowerCase().replace(/ё/g, "е").replace(/э/g, "е").replace(/[ъь]/g, "").replace(/[йы]/g, "и").replace(/тс/g, "ц").replace(/(.)\1+/g, "$1"); }
    function vocab() {
      if (VOC) return VOC; VOC = {};
      var DB = global.RUSSIA_DB, P = (DB && DB.places) || [], re = /[А-Яа-яЁё]+(?:-[А-Яа-яЁё]+)*/g;
      function add(s) { if (!s) return; var m = String(s).match(re); if (!m) return; for (var j = 0; j < m.length; j++) { var w = m[j]; if (w.length < 2) continue; var k = canon(w), e = VOC[k] || (VOC[k] = {}); e[w] = (e[w] || 0) + 1; } }
      for (var i = 0; i < P.length; i++) {
        var p = P[i]; if (!p || (p.country && p.country !== "russia")) continue;
        add(p.name_ru); var src = p.sources; if (src && src.length) for (var j = 0; j < src.length; j++) add(src[j] && src[j].title);
      }
      return VOC;
    }
    function vlookup(cy, cap) {
      var e = vocab()[canon(cy)]; if (!e) return null;
      var best = null, bn = -1;
      for (var w in e) { var isCap = w.charAt(0) !== w.charAt(0).toLowerCase(), sc = e[w] + (isCap === !!cap ? 1e6 : 0); if (sc > bn) { bn = sc; best = w; } }
      return best;
    }

    /* ---- phân loại một từ ---- */
    function classify(w, ctx, lang) {
      if (CYR.test(w)) return { l: "ru", t: w };
      var d = dget(TR, w);
      if (d) return { l: "ru", t: caseLike(w, d.v) };
      var low = w.toLowerCase();
      if (lang === "en") {
        if (!ctx.ru || !/^[A-Z]/.test(w) || EN_STOP[low] || reVIC.test(low)) return null;
        if (isAcr(w)) return /kh|ts|zh/i.test(w) ? { l: "ru", t: rtAcr(w) } : null;
        var cy0 = w.split("-").map(rtWord).join("-"), h0 = vlookup(cy0, true);
        if (h0 && low.length >= 4) return { l: "ru", t: h0 };
        if (RUISH.test(low)) return { l: "ru", t: up1(cy0) };
        return null;
      }
      var x = dget(EX, w); if (x) return { l: "ru", t: caseLike(w, x.v) };
      var v = dget(VI, w); if (v) return { l: "vi", t: v.v };
      if (isVi(w) && !isAcr(w)) return null;
      if (!ctx.ru || w.length < 2) return null;
      if (isAcr(w)) return w.length >= 3 ? { l: "ru", t: rtAcr(w) } : null;
      if (EN_STOP[low]) return null;
      var cap = /^[A-Z]/.test(w), cy = w.split("-").map(function (pt) {
        var d1 = dget(TR, pt) || dget(EX, pt); if (d1) return d1.v.toLowerCase();
        return rtWord(pt);
      }).join("-"), hit = vlookup(cy, cap);
      if (cap && cy.indexOf("-") > 0) cy = cy.split("-").map(function (x, i2) { var src0 = w.split("-")[i2] || ""; return /^[A-Z]/.test(src0) ? up1(x) : x; }).join("-");
      if (!hit && !cap && !RUISH.test(low)) return null;       // từ thường lạ (thường là tiếng Anh/thuật ngữ) → để giọng Việt
      var out = hit || cy;
      return { l: "ru", t: cap ? up1(out) : out };
    }

    /* ---- chuẩn hoá giọng Việt ---- */
    var NV = null;
    function nvRules() {
      if (NV) return NV;
      var b0 = "(?<![\\p{L}\\p{M}\\p{N}])", b1 = "(?![\\p{L}\\p{M}\\p{N}])";
      function hm(h, m) { h = +h; m = +m; return h + " giờ" + (m ? " " + m + (m < 10 ? " phút" : "") : ""); }
      NV = [
        [RX("[“”„«»\"]"), " "],
        [RX("(^|[\\s(\\[{,;:])['‘’`]+"), "$1"],
        [RX("['‘’`]+(?=[\\s)\\]},.;:!?]|$)"), ""],
        [RX("…|\\.{3,}"), ". "],
        [RX("\\s*(?:→|⇒|->|=>|⟶|➜|➔)\\s*"), ", "],
        [RX("[•·▪●◦]"), ", "],
        // dải số trước (10:00–18:00 · 1903–1912 · 300 – 500 RUB · 2-3 giờ)
        [RX("(\\d[\\p{L}%°₽$€']{0,4})\\s*[–—−]\\s*(?=[\\d~≈])"), "$1 đến "],
        [RX("(\\d[hpm%']{0,2})\\s*-\\s*(?=\\d)"), "$1 đến "],
        [RX("((?:[Tt]hứ\\s?|T)[2-7])\\s*[–—-]\\s*(?=(?:[Tt]hứ\\s?|T)[2-7]|CN(?![\\p{L}]))"), "$1 đến "],
        [RX("\\s[–—-]\\s"), ", "],
        [RX("\\s*&\\s*"), " và "],
        [RX("(^|\\s)[−–-](?=\\d)"), "$1âm "],
        [RX("(^|[\\s(~≈])\\+(?=\\d)"), "$1"], [RX("([\\p{L}])[–—]([\\p{L}])"), "$1 $2"],
        [RX("[~≈]\\s*"), "khoảng "],
        // giờ phút
        [RX("(\\d{1,2})[hH](\\d{2})\\s*(?:phút|ph|p|')" + b1), function (m0, h, m) { return hm(h, m) + (+m >= 10 ? " phút" : ""); }],
        [RX("(\\d{1,2})[hH](\\d{2})" + b1), function (m0, h, m) { return hm(h, m); }],
        [RX(b0 + "(\\d{1,2}):(\\d{2})(?![\\d:])"), function (m0, h, m) { return hm(h, m); }],
        [RX("(\\d{1,2})\\s?[hH]" + b1), "$1 giờ"],
        [RX("(\\d+)\\s?(?:ph|p)" + b1), "$1 phút"],
        [RX("(\\d+)'(?![\\p{L}'])"), "$1 phút"],
        // số: dấu chấm hàng nghìn, dấu phẩy thập phân
        [RX("(\\d)[.\\u00a0\\u202f](?=\\d{3}(?!\\d))"), "$1"],
        [RX("(\\d),(\\d{3})(?!\\d)"), "$1$2"],
        [RX("(\\d),(\\d{1,2})(?!\\d)"), "$1 phẩy $2"],
        // tiền
        [RX("(\\d)\\s?(?:₽|руб\\.?|RUB|Rub|rub|rúp)" + b1), "$1 rúp"],
        [RX(b0 + "RUB" + b1), "rúp"], [RX("₽"), " rúp"],
        [RX("(\\d)\\s?(?:VNĐ|VND|vnđ|vnd|đồng|đ|₫)" + b1), "$1 đồng"], [RX("(\\d)\\s?₫"), "$1 đồng"],
        [RX("\\$\\s?(\\d[\\d.,]*)"), "$1 đô la"],
        [RX("(\\d)\\s?(?:USD|usd)" + b1), "$1 đô la"],
        [RX("(\\d)\\s?(?:€|EUR)" + b1), "$1 ơ rô"],
        [RX("(\\d)\\s?(?:NDT|CNY|¥)" + b1), "$1 nhân dân tệ"], [RX(b0 + "NDT" + b1), "nhân dân tệ"],
        [RX("(\\d)\\s?k" + b1), "$1 nghìn"], [RX("(\\d)\\s?tr" + b1), "$1 triệu"],
        // đơn vị đo
        [RX("(\\d)\\s?km/h" + b1), "$1 ki lô mét một giờ"],
        [RX("(\\d)\\s?km(?:²|2)" + b1), "$1 ki lô mét vuông"], [RX("(\\d)\\s?km" + b1), "$1 ki lô mét"],
        [RX("(\\d)\\s?m²"), "$1 mét vuông"], [RX("(\\d)\\s?m³"), "$1 mét khối"],
        [RX("(\\d)\\s?cm" + b1), "$1 xăng ti mét"], [RX("(\\d)\\s?mm" + b1), "$1 mi li mét"], [RX("(\\d)\\s?m" + b1), "$1 mét"],
        [RX("(\\d)\\s?ha" + b1), "$1 héc ta"], [RX("(\\d)\\s?kg" + b1), "$1 ki lô gam"],
        [RX("\\s?°\\s?C" + b1), " độ xê"], [RX("°"), " độ"], [RX("(\\d)\\s?%"), "$1 phần trăm"],
        [RX("\\s?/\\s?(?=(?:người lớn|người|khách|lượt|vé|xe|phòng|đêm|ngày|giờ|tuần|tháng|năm|nhóm|đoàn|chiếc|suất|bàn|cặp|gia đình|trẻ em|trẻ|lần|chai|ly|cốc|kg)" + b1 + ")"), " một "],
        // ngày tháng
        [RX("(?:ngày\\s+)?" + b0 + "(\\d{1,2})/(\\d{1,2})/(\\d{4})" + b1), function (m0, d, mo, y) { return "ngày " + (+d) + " tháng " + (+mo) + " năm " + y; }],
        [RX("ngày\\s+(\\d{1,2})/(\\d{1,2})" + b1), function (m0, d, mo) { return "ngày " + (+d) + " tháng " + (+mo); }],
        [RX(b0 + "24/7" + b1), "suốt ngày đêm"],
        // thứ trong tuần, Công nguyên
        [RX(b0 + "T\\.?\\s?([2-7])" + b1), function (m0, d) { return "thứ " + WD[+d]; }],
        [RX(b0 + "([Tt])hứ\\s?([2-7])(?!\\d)"), function (m0, t, d) { return (t === "T" ? "Thứ " : "thứ ") + WD[+d]; }],
        [RX(b0 + "([Tt])hứ\\s?1(?!\\d)"), "$1hứ nhất"],
        [RX("([Tt]hứ (?:hai|ba|tư|năm|sáu|bảy))\\s*[–—-]\\s*(?=[Tt]hứ|CN" + b1 + ")"), "$1 đến "],
        [RX("([Tt]hứ (?:hai|ba|tư|năm|sáu|bảy)\\s*(?:đến|và|,)?\\s*)CN" + b1), "$1chủ nhật"], [RX("(đến|và|nghỉ|đóng cửa|trừ|cả|mở cửa|ngày)\\s+CN" + b1), "$1 chủ nhật"],
        [RX("(\\d)\\s?(?:TCN|tr\\.\\s?CN)" + b1), "$1 trước Công nguyên"], [RX(b0 + "TCN" + b1), "trước Công nguyên"], [RX(b0 + "SCN" + b1), "sau Công nguyên"],
        [RX("(sau|trước)\\s+CN" + b1), "$1 Công nguyên"], [RX("(\\d)\\s+CN" + b1), "$1 Công nguyên"],
        // thế kỷ, thế chiến (số La Mã)
        [RX("(thế kỷ|thế kỉ|Thế kỷ|Thế kỉ|TK\\.?)\\s*([IVXLC]+)(?:\\s*(?:[–—-]|đến)\\s*([IVXLC]+))?" + b1), function (m0, w, a, b) {
          var A = roman(a), B = b ? roman(b) : 0; if (!A) return m0; return (/^T[hế]/.test(w) ? "Thế kỷ " : "thế kỷ ") + A + (B ? " đến " + B : ""); }],
        [RX("([Tt]hế kỷ \\d+\\s*(?:và|hoặc|,)\\s*)([IVXLC]{2,})" + b1), function (m0, p, a) { return p + (roman(a) || a); }],
        [RX("([Tt]hế chiến|[Cc]hiến tranh thế giới|[Đđ]ại chiến thế giới)(\\s+thứ)?\\s+(I{1,2})" + b1), function (m0, w, t, n) { return w + " thứ " + (n === "I" ? "nhất" : "hai"); }],
        // viết tắt
        [RX("TP\\.?\\s?HCM" + b1), "Thành phố Hồ Chí Minh"], [RX(b0 + "(?:TP|Tp)\\.?(?=\\s)"), "thành phố"],
        [RX(b0 + "Q\\.\\s?(\\d)"), "quận $1"], [RX(b0 + "v\\.v\\.?"), "vân vân"], [RX(b0 + "VD:"), "ví dụ:"],
        [RX(b0 + "KTS" + b1), "kiến trúc sư"], [RX(b0 + "HDV" + b1), "hướng dẫn viên"], [RX(b0 + "UBND" + b1), "uỷ ban nhân dân"],
        [RX(b0 + "CLB" + b1), "câu lạc bộ"], [RX(b0 + "SĐT" + b1), "số điện thoại"], [RX(b0 + "WC" + b1), "nhà vệ sinh"],
        [RX(b0 + "(?:Saint|St\\.?|ST\\.?|Sankt|San)[\\s-]+Peter(?:s)?burg" + b1), "Sankt-Peterburg"],
        // ngoặc, gạch chéo, dọn dấu
        [RX("\\s*[(\\[]\\s*"), ", "], [RX("\\s*[)\\]]"), ", "],
        [RX("(\\d)\\s?/\\s?(\\d)"), "$1 trên $2"], [RX("\\s*/\\s*"), ", "],
        [RX("\\s*,(?:\\s*,)+"), ","], [RX("([.!?;:])\\s*,"), "$1"], [RX("\\s*,\\s*([.!?;:])"), "$1"], [RX("\\s+([,.!?;:])"), "$1"],
        [RX("\\s{2,}"), " "]
      ].filter(function (r) { return r[0]; });
      return NV;
    }
    function base(s) { return String(s == null ? "" : s).normalize("NFC").replace(EMO, " "); }
    function normVi(s) { s = base(s); var R = nvRules(); for (var i = 0; i < R.length; i++) s = s.replace(R[i][0], R[i][1]); return s.replace(/^[\s,;]+/, "").replace(/[\s,]+$/, "").trim(); }
    function pl(n, a, b, c) { n = Math.abs(n) % 100; var n1 = n % 10; if (n > 10 && n < 20) return c; if (n1 > 1 && n1 < 5) return b; if (n1 === 1) return a; return c; }
    function normRu(s) {
      s = base(s).replace(/[“”„«»"]/g, " ").replace(/…/g, ". ").replace(/\s*(?:→|⇒|->|➜)\s*/g, ", ").replace(/[•·]/g, ", ");
      s = s.replace(/(\d)\s*[–—−-]\s*(?=\d)/g, "$1 — ").replace(/[~≈]\s*/g, "около ");
      s = s.replace(/(\d)[.   ](?=\d{3}(?!\d))/g, "$1");
      s = s.replace(/(\d{1,2}):(\d{2})(?![\d:])/g, function (m0, h, m) { return +m ? (+h) + " " + m : (+h) + " " + pl(+h, "час", "часа", "часов"); });
      s = s.replace(/(\d+)\s?(?:₽|руб\.?|RUB)/g, function (m0, n) { return n + " " + pl(+n, "рубль", "рубля", "рублей"); });
      s = s.replace(/(\d+)\s?км(?![а-я])/g, function (m0, n) { return n + " " + pl(+n, "километр", "километра", "километров"); });
      s = s.replace(/(\d+)\s?мин\.?(?![а-я])/g, function (m0, n) { return n + " " + pl(+n, "минута", "минуты", "минут"); });
      return s.replace(/\s*[(\[]\s*/g, ", ").replace(/\s*[)\]]/g, ", ").replace(/\s+([,.!?;:])/g, "$1").replace(/,\s*([.!?])/g, "$1").replace(/\s{2,}/g, " ").trim();
    }
    function normEn(s) {
      s = base(s).replace(/[“”„«»"]/g, " ").replace(/…/g, ". ").replace(/\s*(?:→|⇒|->|➜)\s*/g, ", ").replace(/[•·]/g, ", ");
      s = s.replace(/(\d)\s*[–—−]\s*(?=\d)/g, "$1 to ").replace(/\s[–—-]\s/g, ", ").replace(/[~≈]\s*/g, "about ");
      s = s.replace(/(\d{1,2}):(\d{2})(?![\d:])/g, function (m0, h, m) { return +m ? (+h) + " " + m : (+h) + " o'clock"; });
      s = s.replace(/(\d)\s?(?:₽|RUB)/g, "$1 rubles").replace(/₽/g, " rubles").replace(/(\d)\s?km\b/g, "$1 kilometers").replace(/(\d)\s?m\b/g, "$1 meters").replace(/°\s?C\b/g, " degrees Celsius");
      return s.replace(/\s*[(\[]\s*/g, ", ").replace(/\s*[)\]]/g, ", ").replace(/\s+([,.!?;:])/g, "$1").replace(/,\s*([.!?])/g, "$1").replace(/\s{2,}/g, " ").trim();
    }

    /* ---- bỏ phần "phiên âm" trong ngoặc: (đọc: Lô-ba-tsép-xki), (La-gô Na-ki) — giọng Nga đã đọc chuẩn tên gốc ---- */
    function stripHints(s) {
      s = String(s || "").replace(/\s*\((?:đọc|phiên âm|phát âm)\s*:[^)]*\)/gi, "");
      return s.replace(/\s*\(([^()]{2,80})\)/g, function (m0, inner) {
        if (/\d/.test(inner) || !/\S-\S/.test(inner)) return m0;
        var ws = inner.split(/[\s,]+/).filter(Boolean); if (!ws.length) return m0;
        for (var i = 0; i < ws.length; i++) if (!isVi(ws[i].replace(/[.!?;:]+$/, ""))) return m0;
        return "";
      });
    }
    function stripParens(s) { return String(s || "").replace(/\s*\([^)]*\)/g, "").replace(/\s{2,}/g, " ").trim(); }

    /* ---- tách đoạn theo ngôn ngữ ---- */
    var TOKRE = RX("([\\p{L}\\p{M}]+(?:['’\\-][\\p{L}\\p{M}]+)*)|(\\d+)|(\\s+)|([^\\p{L}\\p{M}\\d\\s]+)");
    var ROMAN = /^(?:I{1,3}|IV|VI{0,3}|IX|X{1,3}|XI{1,3}|XIV|XV|XVI{1,3})$/;
    var INIRE = /^(?:[A-Z]|Yu|Ya|Ye|Yo|Zh|Kh|Ts|Ch|Sh)$/;
    function segs(text, ctx) {
      ctx = ctx || {}; var lang = ctx.lang || "vi";
      if (lang === "ru") {
        var r0 = normRu(text).replace(RX("[\\p{L}\\p{M}]+(?:['’\\-][\\p{L}\\p{M}]+)*") || /[A-Za-z]+/g, function (w) {
          if (CYR.test(w) || reVIC.test(w.toLowerCase()) || (isVi(w) && !isAcr(w))) return w; var d = dget(TR, w) || dget(EX, w); if (d) return caseLike(w, d.v);
          if (isAcr(w)) return rtAcr(w); var cy = w.split("-").map(rtWord).join("-"); return caseLike(w, vlookup(cy, /^[A-Z]/.test(w)) || cy);
        });
        return r0 ? [{ l: "ru", t: r0 }] : [];
      }
      var s = lang === "en" ? normEn(stripHints(text)) : normVi(stripHints(text));
      if (!s) return [];
      if (!TOKRE) return [{ l: lang, t: s }];
      var tk = [], m; TOKRE.lastIndex = 0;
      while ((m = TOKRE.exec(s))) tk.push({ w: m[1], sp: m[3], p: m[4], s: m[0] });
      var i, j, k, t;
      for (i = 0; i < tk.length; i++) if (tk[i].w) tk[i].c = classify(tk[i].w, ctx, lang);
      // số La Mã sau tên riêng: Nikolai II → Николай + "đệ nhị"
      for (i = 0; i < tk.length; i++) {
        t = tk[i]; if (!t.w || !ROMAN.test(t.w)) continue;
        j = i - 1; if (tk[j] && tk[j].sp) j--;
        var pv = tk[j]; if (!pv || !pv.w || !/^[A-ZÀ-ỸĐ]/.test(pv.w) || ROMAN.test(pv.w)) continue;
        if (!(pv.c && pv.c.l === "ru") && isVi(pv.w)) continue;
        var n = roman(t.w); if (!n || n > 10) continue;
        t.c = { l: lang, t: lang === "en" ? ORD_EN[n] : "đệ " + ORD[n] }; t.roman = 1;
        if (tk[i + 1] && tk[i + 1].p && tk[i + 1].p.charAt(0) === ".") t.endDot = 1;
      }
      // chữ cái viết tắt trước họ Nga: A. P. Chekhov → А. П. Чехов
      if (ctx.ru) for (i = 0; i < tk.length; i++) {
        t = tk[i]; if (!t.w || t.roman || !INIRE.test(t.w) || !(tk[i + 1] && tk[i + 1].p && tk[i + 1].p.charAt(0) === ".")) continue;
        j = i; var ini = [];
        while (tk[j] && tk[j].w && !tk[j].roman && INIRE.test(tk[j].w) && tk[j + 1] && tk[j + 1].p && tk[j + 1].p.charAt(0) === "." && tk[j + 1].p.length <= 2) { ini.push(tk[j].w); j += 2; if (tk[j] && tk[j].sp) j++; }
        var sur = tk[j];
        if (ini.length && sur && sur.w && sur.c && sur.c.l === "ru") {
          sur.c = { l: "ru", t: ini.map(function (x) { return iniCyr(x) + "."; }).join(" ") + " " + sur.c.t }; sur.pre = ini.map(function (x) { return x + "."; }).join(" ") + " ";
          for (k = i; k < j; k++) tk[k].skip = 1;
          i = j;
        }
      }
      // gộp thành đoạn
      var out = [], cur = null;
      function push(l, str, orig) { if (!str) return; if (cur && cur.l === l) { cur.t += str; cur.o += orig == null ? str : orig; } else { cur = { l: l, t: str, o: orig == null ? str : orig }; out.push(cur); } }
      for (i = 0; i < tk.length; i++) {
        t = tk[i]; if (t.skip) continue;
        if (t.c) { push(t.c.l, t.c.t, t.c.l === "ru" ? (t.pre || "") + t.s : null); continue; }
        if (cur && cur.l === "ru") {
          if (t.sp) { var nx = tk[i + 1]; if (nx && !nx.skip && nx.c && nx.c.l === "ru") { push("ru", " "); continue; } }
          if (t.p && /^[,.;:!?]+$/.test(t.p)) { push("ru", t.p); continue; }
          if (t.p === "-" && tk[i + 1] && tk[i + 1].c && tk[i + 1].c.l === "ru") { push("ru", "-"); continue; }
        }
        push(lang, t.s);
      }
      var res = [];
      out.forEach(function (x) {
        var tt = x.t.replace(/\s+/g, " ").trim(), oo = x.o.replace(/\s+/g, " ").trim(); if (!tt) return;
        if (!/[\p{L}\p{N}]/u.test(tt)) { if (res.length) { res[res.length - 1].t += tt; res[res.length - 1].o += tt; } return; }
        var lst = res[res.length - 1];
        if (lst && lst.l === x.l) { lst.t += " " + tt; lst.o += " " + oo; } else res.push(x.l === "ru" ? { l: x.l, t: tt, o: oo } : { l: x.l, t: tt });
      });
      return res;
    }

    /* ---- tách câu (giữ nguyên văn để làm phụ đề) ---- */
    var ABBR = /(?:^|[\s(])(?:[A-ZĐ]|St|Sv|TP|Tp|Q|v\.v|TS|ThS|PGS|GS|tr|ul|pr|g|ok|im|т|г|ул|им|св)$/;
    function sentences(text) {
      var s = String(text || "").replace(/\s+/g, " ").trim(), out = [], st = 0, i;
      if (!s) return out;
      var re = /[.!?…]+["'”’»)]*(?=\s+[^\s])/g, m;
      while ((m = re.exec(s))) {
        var end = m.index + m[0].length, before = s.slice(st, m.index);
        if (/[.]/.test(m[0]) && m[0].length === 1 && ABBR.test(before)) continue;     // viết tắt / chữ cái đầu tên
        var nxt = s.slice(end).replace(/^\s+/, "").charAt(0);
        if (nxt && /[a-zà-ỹđ]/.test(nxt)) continue;                                   // sau dấu chấm mà chữ thường → chưa hết câu
        out.push({ t: s.slice(st, end).trim(), a: st, b: end });
        st = end; while (s.charAt(st) === " ") st++;
      }
      if (st < s.length) out.push({ t: s.slice(st).trim(), a: st, b: s.length });
      return out;
    }
    function nkey(s) { return String(s || "").normalize("NFC").toLowerCase().replace(/[^\p{L}\p{N}]+/gu, ""); }
    function words(s) { return String(s || "").normalize("NFC").toLowerCase().split(/[^\p{L}\p{N}]+/u).filter(function (w) { return w.length > 1; }); }
    // bỏ trong ghi chú những câu đã có trong phần giới thiệu / điểm nhấn (nút 📖 chép nguyên văn giới thiệu vào ghi chú)
    function dedupe(note, desc, hl) {
      if (!note) return "";
      var dk = nkey(desc), hk = (hl || []).map(nkey), ds = sentences(desc).map(function (x) { return words(x.t); }), keep = [];
      sentences(note).forEach(function (x) {
        var k = nkey(x.t); if (k.length < 2) return;
        if (dk && (dk.indexOf(k) >= 0 || (k.length > 40 && k.indexOf(dk) >= 0 && dk.length > k.length * 0.8))) return;
        for (var i = 0; i < hk.length; i++) if (hk[i] && (hk[i].indexOf(k) >= 0 || k.indexOf(hk[i]) >= 0 && hk[i].length > 15)) return;
        var ws = words(x.t);
        if (ws.length >= 5) for (var j = 0; j < ds.length; j++) {
          var set = {}, inter = 0; ds[j].forEach(function (w) { set[w] = 1; });
          ws.forEach(function (w) { if (set[w]) inter++; });
          if (inter / Math.max(ws.length, ds[j].length) >= 0.8) return;
        }
        keep.push(x.t);
      });
      return keep.join(" ");
    }
    return { pl: pl, segs: segs, normVi: normVi, normRu: normRu, normEn: normEn, sentences: sentences, dedupe: dedupe, stripHints: stripHints,
             stripParens: stripParens, rtWord: rtWord, isVi: isVi, vocab: vocab, classify: classify, roman: roman, nkey: nkey };
  })();

  /* ---------------- 7. tuỳ chọn, chuẩn bị dữ liệu, lời thuyết minh, kịch bản ---------------- */
  var DEF = { aspect: "16:9", res: 720, basemap: "sat", pace: "mid", lang: "vi",
              photo: true, desc: true, hl: true, prac: true, note: true, times: true, cost: false, sign: true,
              title: "", credit: "Phạm Đăng Hiển · fb.com/lopmaybay",
              voice: "ai", rate: 1, detail: "full", ruName: true,
              music: "calm", musicVol: 0.55, caps: true, clock: true, qr: true, qrUrl: "https://fb.com/lopmaybay",
              sysVi: "", sysRu: "", sysEn: "" };
  function dims(O) { var s = O.res === 1080 ? 1080 : 720;
    if (O.aspect === "9:16") return { W: s, H: Math.round(s * 16 / 9 / 2) * 2 };
    if (O.aspect === "1:1") return { W: s, H: s };
    return { W: Math.round(s * 16 / 9 / 2) * 2, H: s }; }
  // nội dung đúng ngôn ngữ (không mượn tiếng Việt khi làm video tiếng Anh/Nga — tránh giọng Nga đọc chữ Việt)
  function ptn(p, base, L) { if (!p) return ""; if (L === "vi") return p[base + "_vi"] || p[base + "_en"] || ""; return p[base + "_" + L] || ""; }
  function parrn(p, base, L) { var a = p && (L === "vi" ? (p[base + "_vi"] || p[base + "_en"]) : p[base + "_" + L]); return Array.isArray(a) ? a : []; }
  function pracn(p, key, L) { var r = (p && p.practical) || {}; return (L === "vi" ? (r[key + "_vi"] || r[key + "_en"]) : r[key + "_" + L]) || ""; }
  function clean1(s) { return String(s || "").replace(/\s+/g, " ").trim(); }
  // tên trên thẻ: bỏ phần ngoặc chỉ là phiên âm La-tinh của tên Nga "(Sobor Vasiliya Blazhennogo)" — tên Nga đã có dòng riêng;
  // giữ ngoặc chỉ nơi chốn "(Zvenigorod)" hoặc phiên âm tiếng Việt "(La-gô Na-ki)"
  function cardTitle(name, L) {
    if (L !== "vi") return name;
    var out = String(name).replace(/\s*\(([^()]*)\)/g, function (m0, inner) {
      var ws = inner.replace(/[«»"“”']/g, " ").split(/[\s,]+/).filter(Boolean);
      if (ws.length < 2 || /[0-9]/.test(inner)) return m0;
      for (var i = 0; i < ws.length; i++) if (SAY.isVi(ws[i]) && /[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]/i.test(ws[i])) return m0;
      return "";
    }).trim();
    return out || name;
  }
  // "ngắn gọn": lấy trọn câu đầu (≤ ~230 ký tự), KHÔNG cắt giữa câu, không dấu "…"
  function firstSentences(text, maxC) {
    var ss = SAY.sentences(text); if (!ss.length) return "";
    var out = ss[0].t; for (var i = 1; i < ss.length && (out + " " + ss[i].t).length <= maxC; i++) out += " " + ss[i].t;
    return out;
  }
  function prepare(data, O) {
    var L = O.lang, stops = [], nRu = 0;
    (data.stops || []).forEach(function (s) {
      var p = s.place || {}, c = p.coordinates || {}, lat = +c.lat, lon = +c.lon;
      if (!isFinite(lat) || !isFinite(lon) || (lat === 0 && lon === 0)) return;
      var desc = clean1(ptn(p, "presentation_short", L)) || (L !== "vi" ? "" : clean1(p.presentation_long_vi));
      if (O.detail === "short" && desc) desc = firstSentences(desc, 230);
      var hl = parrn(p, "highlights", L).slice(0, 3).map(clean1).filter(Boolean);
      var isRu = p.country ? p.country === "russia" : null; if (isRu) nRu++;
      stops.push({ day: +s.day || 1, arr: s.arr || "", dep: s.dep || "", stay: +s.stay || 0, travel: +s.travel || 0,
        mode: s.mode || null, noteRaw: s.note || "", cv: +s.cv || 0, cvu: s.cvu, place: p, isRu: isRu,
        lat: lat, lon: lon, x: mx(lon), y: my(lat), custom: !!p.custom,
        name: cardTitle(pt(p, "name", L) || "?", L), ru: (L !== "ru" ? p.name_ru : p.name_en) || "", cat: (p.categories || [])[0] || "other",
        short: desc, hl: hl, hours: clean1(pracn(p, "hours", L)), ticket: clean1(pracn(p, "ticket", L)),
        photo: p.photo || "", credit: p.photo_credit || "" });
    });
    // ghi chú của anh: bỏ những câu trùng phần giới thiệu/điểm nhấn (nút 📖 chép nguyên văn giới thiệu vào ghi chú)
    stops.forEach(function (s, k) {
      s.i = k; s.num = k + 1;
      s.note = SAY.dedupe(clean1(s.noteRaw), s.short, s.hl);
      if (s.isRu == null) s.isRu = nRu > 0;
    });
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
             per: data.perPerson || "", group: data.group || "", ru: nRu * 2 >= stops.length && nRu > 0 };
  }

  /* lời thuyết minh: theo từng cảnh, mỗi câu = { c: chữ phụ đề, segs: [{l,t}] đoạn đọc theo ngôn ngữ, ref: vị trí trên thẻ } */
  function guideName(O) { return clean1(String(O.credit || "").split(/[·|•]/)[0]); }
  function narrate(D, O) {
    var L = O.lang, T = TXT[L] || TXT.vi, NR = {}, tctx = { lang: L, ru: D.ru };
    function sent(c, say, ctx, extra) { if (say == null) say = c; var o = { c: c, segs: typeof say === "string" ? SAY.segs(say, ctx || tctx) : say }; if (extra) for (var k in extra) o[k] = extra[k]; return o; }
    function speakT(hm) { return sayTime(hm, L); }
    // giới thiệu
    var intro = [sent(D.title + ".", D.title + ".")];
    var nd = D.nDays, ns = D.stops.length;
    if (L === "vi") intro.push(sent("Hành trình " + nd + " ngày" + (D.nights ? " " + D.nights + " đêm" : "") + ", " + ns + " điểm tham quan" + (D.date ? ", khởi hành " + fmtDay(D.date, L) : "") + ".",
      "Hành trình " + nd + " ngày" + (D.nights ? " " + D.nights + " đêm" : "") + ", " + ns + " điểm tham quan" + (D.date ? ", khởi hành " + sayDate(D.date, L) : "") + "."));
    else if (L === "en") intro.push(sent(nd + "-day trip, " + ns + " stops" + (D.date ? ", starting " + fmtDay(D.date, L) : "") + ".", nd + " day trip with " + ns + " stops" + (D.date ? ", starting " + sayDate(D.date, L) : "") + "."));
    else intro.push(sent("Путешествие на " + nd + " дн., точек: " + ns + (D.date ? ", начало " + fmtDay(D.date, L) : "") + ".", "Путешествие: дней — " + nd + ", точек — " + ns + (D.date ? ". Начало: " + sayDate(D.date, L) : "") + "."));
    if (D.startName) intro.push(sent((L === "vi" ? "Xuất phát từ " : L === "en" ? "Starting from " : "Отправление: ") + D.startName + "."));
    if (O.sign && guideName(O)) intro.push(sent((L === "vi" ? "Hướng dẫn viên: " : L === "en" ? "Your guide: " : "Ваш гид: ") + guideName(O) + ".", (L === "vi" ? "Cùng hướng dẫn viên " : L === "en" ? "With your guide, " : "С вами гид ") + guideName(O) + "."));
    NR.intro = intro;
    D.days.forEach(function (d) {
      var a = [];
      if (L === "vi") {
        a.push(sent("Ngày " + d.day + (d.date ? ", " + fmtDay(d.date, L) : "") + ".", "Ngày " + d.day + (d.date ? ", " + sayDate(d.date, L) : "") + "."));
        a.push(sent("Bắt đầu lúc " + (d.start || "08:00") + ", gồm " + d.stops.length + " điểm.", "Bắt đầu lúc " + speakT(d.start || "08:00") + ", gồm " + d.stops.length + " điểm."));
      } else if (L === "en") {
        a.push(sent("Day " + d.day + (d.date ? ", " + fmtDay(d.date, L) : "") + ".", "Day " + d.day + (d.date ? ", " + sayDate(d.date, L) : "") + "."));
        a.push(sent("We start at " + (d.start || "08:00") + " with " + d.stops.length + " stops.", "We start at " + speakT(d.start || "08:00") + " with " + d.stops.length + " stops."));
      } else {
        a.push(sent("День " + d.day + (d.date ? ", " + fmtDay(d.date, L) : "") + ".", "День " + d.day + (d.date ? ", " + sayDate(d.date, L) : "") + "."));
        a.push(sent("Начало в " + (d.start || "08:00") + ", точек: " + d.stops.length + ".", "Начало в " + (d.start || "08:00") + ". Точек: " + d.stops.length + "."));
      }
      NR["day:" + d.day] = a;
    });
    D.stops.forEach(function (s) {
      var ctx = { lang: L, ru: !!s.isRu }, p = s.place, a = [];
      if (s.i > 0 && s.travel > 0 && s.mode) {
        var mn = modeName(s.mode, L), mk = s.mode.k, du = durTxt(s.travel, L);
        NR["trv:" + s.i] = [L === "vi" ? sent(mk === "walk" ? "Đi bộ khoảng " + du + "." : mk === "other" ? "Di chuyển khoảng " + du + "." : "Di chuyển bằng " + mn.toLowerCase() + ", khoảng " + du + ".")
          : L === "en" ? sent(mk === "walk" ? "A " + du + " walk." : "By " + mn.toLowerCase() + ", about " + du + ".") : sent(mn + ", около " + du + ".")];
      }
      // tên điểm: phần tiếng Việt + tên Nga đọc bằng giọng Nga
      var nmSay = L === "ru" ? (p.name_ru || s.name) : SAY.stripParens(s.name);
      var nmSegs = SAY.segs(nmSay, ctx), hasRu = nmSegs.some(function (x) { return x.l === "ru"; });
      var lead = L === "vi" ? "Điểm " + s.num + ": " : L === "en" ? "Stop " + s.num + ": " : "Точка " + s.num + ": ";
      var segs = [{ l: L, t: lead }].concat(nmSegs);
      var cap = lead + (L === "ru" ? s.name : SAY.stripParens(s.name));
      if (L !== "ru" && O.ruName && s.isRu && !hasRu && p.name_ru && !CYRX.test(s.name)) {
        var rn = clean1(String(p.name_ru).replace(/[«»"“”]/g, "").replace(/\s*\([^)]*\)/g, ""));
        if (rn) { segs.push({ l: "ru", t: rn, o: "" }); cap += " — " + rn; }
      }
      a.push(sent(cap + ".", mergeSegs(segs.concat([{ l: L, t: "." }])), null, { k: "name" }));
      if (O.times && s.arr) {
        var sd = s.stay ? durTxt(s.stay, L) : "";
        if (L === "vi") a.push(sent("Đến lúc " + s.arr + (s.stay ? ", tham quan khoảng " + sd + "." : "."), "Đến lúc " + speakT(s.arr) + (s.stay ? ", tham quan khoảng " + sd + "." : "."), ctx, { k: "time" }));
        else if (L === "en") a.push(sent("Arrival " + s.arr + (s.stay ? ", about " + sd + " here." : "."), "Arrival at " + speakT(s.arr) + (s.stay ? ", about " + sd + " here." : "."), ctx, { k: "time" }));
        else a.push(sent("Прибытие в " + s.arr + (s.stay ? ", осмотр около " + sd + "." : "."), "Прибытие в " + s.arr + (s.stay ? ". Осмотр около " + sd + "." : "."), ctx, { k: "time" }));
      }
      if (O.desc && s.short) SAY.sentences(s.short).forEach(function (x) { a.push(sent(x.t, x.t, ctx, { k: "desc", ref: { f: "desc", a: x.a, b: x.b } })); });
      if (O.note && s.note) SAY.sentences(s.note).forEach(function (x, j) {
        var pre = j === 0 ? (L === "vi" ? "Lưu ý: " : L === "en" ? "Note: " : "Обратите внимание: ") : "";
        a.push(sent(pre + x.t, pre + x.t, ctx, { k: "note", ref: { f: "note", a: x.a, b: x.b } }));
      });
      NR["stop:" + s.i] = a;
    });
    var out = [];
    if (L === "vi") {
      out.push(sent("Hành trình kết thúc: " + ns + " điểm trong " + nd + " ngày" + (D.km >= 1 ? ", khoảng " + Math.round(D.km) + " km" : "") + "."));
      if (O.cost && D.per) out.push(sent("Chi phí dự kiến: " + D.per + " một người."));
      out.push(sent("Cảm ơn quý khách đã theo dõi!"));
      if (O.qr && O.qrUrl) out.push(sent("Quét mã QR trên màn hình để liên hệ hướng dẫn viên."));
    } else if (L === "en") {
      out.push(sent("That's the trip: " + ns + " stops in " + nd + " days" + (D.km >= 1 ? ", about " + Math.round(D.km) + " km" : "") + "."));
      if (O.cost && D.per) out.push(sent("Estimated cost: " + D.per + " per person."));
      out.push(sent("Thank you for watching!"));
      if (O.qr && O.qrUrl) out.push(sent("Scan the QR code to contact your guide."));
    } else {
      out.push(sent("Итого: точек — " + ns + ", дней — " + nd + "."));
      out.push(sent("Спасибо за внимание!"));
      if (O.qr && O.qrUrl) out.push(sent("Отсканируйте QR-код, чтобы связаться с гидом."));
    }
    NR.outro = out;
    return NR;
  }
  var CYRX = /[Ѐ-ӿ]/;
  // 90 → "1 giờ 30 phút" · "1 hour 30 minutes" · "1 ч 30 мин"
  function durTxt(min, L) {
    min = Math.round(+min || 0); var h = Math.floor(min / 60), m = min % 60;
    if (L === "en") return h ? h + " hour" + (h > 1 ? "s" : "") + (m ? " " + m + " minutes" : "") : m + " minutes";
    if (L === "ru") return h ? h + " " + SAY.pl(h, "час", "часа", "часов") + (m ? " " + m + " " + SAY.pl(m, "минута", "минуты", "минут") : "") : m + " " + SAY.pl(m, "минута", "минуты", "минут");
    return h ? h + " giờ" + (m ? " " + m + " phút" : "") : m + " phút";
  }
  function mergeSegs(a) {
    var out = [];
    a.forEach(function (x) {
      if (!x || !x.t) return;
      var last = out[out.length - 1];
      if (last && last.l === x.l) { last.t = (last.t + " " + x.t).replace(/\s+([.,!?;:])/g, "$1"); if (last.o != null || x.o != null) last.o = ((last.o != null ? last.o : last.t) + " " + (x.o != null ? x.o : x.t)).replace(/\s+([.,!?;:])/g, "$1"); }
      else if (last && !/[\p{L}\p{N}]/u.test(x.t)) { last.t += x.t; if (last.o != null) last.o += x.t; }
      else out.push(x.o != null ? { l: x.l, t: x.t, o: x.o } : { l: x.l, t: x.t });
    });
    return out.map(function (x) { var r = { l: x.l, t: x.t.replace(/\s+/g, " ").replace(/:\s*\./, ".").trim() }; if (x.o != null) r.o = x.o.replace(/\s+/g, " ").trim(); return r; }).filter(function (x) { return x.t; });
  }
  // chia khung thời gian cho các câu theo độ dài (khi chưa có giọng AI để biết chính xác)
  function estimateSents(narr, a, b) {
    if (!narr || !narr.length) return [];
    var w = narr.map(function (x) { return Math.max(8, (x.c || "").length); }), tot = w.reduce(function (s, v) { return s + v; }, 0), t = a, span = Math.max(0.5, b - a);
    return w.map(function (v) { var d = span * v / tot, r = { t0: t, t1: t + d }; t += d; return r; });
  }
  function readSec(chars) { return chars / 15.5; }    // tốc độ đọc/ nói tiếng Việt ước lượng

  function buildScenes(D, O, W, H, NR, AP) {
    var LY = layout(W, H), L = O.lang, T = TXT[L] || TXT.vi, bm = BASEMAPS[O.basemap] || BASEMAPS.sat;
    var pace = O.pace === "fast" ? 0.72 : (O.pace === "slow" ? 1.35 : 1);
    var maxZ = Math.min(bm.max, 16.2), scenes = [], tt = 0, N = D.stops.length;
    NR = NR || {};
    function push(sc) { sc.t0 = tt; tt += sc.dur; sc.idx = scenes.length; scenes.push(sc); return sc; }
    function stopCam(s) { return fitCam([s], LY.mapCard, W, H, Math.min(maxZ, s.cat === "park_garden" ? 14.6 : 15.6), 0.2); }
    function endCam(sc) { return { x: sc.camB.x, y: sc.camB.y, z: sc.camB.z + (sc.drift || 0), fx: sc.camB.fx, fy: sc.camB.fy }; }
    // khớp thời lượng cảnh với lời đọc: lead = lúc bắt đầu đọc, tail = thời gian chờ sau khi đọc xong
    function voiced(sc, lead, tail) {
      sc.narr = NR[sc.key] || []; sc.lead = lead;
      var ap = AP && AP.scenes && AP.scenes[sc.key];
      if (ap && ap.dur > 0) {
        sc.dur = Math.max(sc.dur, lead + ap.dur + tail); sc.ap = ap;
        sc.sentT = ap.sents.map(function (x) { return { t0: lead + x.t0, t1: lead + x.t1 }; });
      } else sc.sentT = estimateSents(sc.narr, lead, Math.max(lead + 0.5, sc.dur - tail));
      return sc;
    }
    var allCam = fitCam(D.stops, LY.mapSide, W, H, Math.min(maxZ, 15), 0.12);
    var intro = { key: "intro", type: "intro", dur: 6.8 * pace, camA: allCam, camB: allCam, drift: 0.18, flyDur: 0, r0: -1, r1: -1, done: 0 };
    intro.previewEnd = 0.7 + Math.min(4.2, 0.5 + N * 0.32) * pace;
    push(voiced(intro, 0.9, 1.1));
    var prevEnd = endCam(intro), done = 0;
    D.days.forEach(function (d) {
      var dc = fitCam(d.stops, LY.mapSide, W, H, Math.min(maxZ, 15), 0.14), nItems = Math.min(d.stops.length, 8);
      var dsc = { key: "day:" + d.day, type: "day", day: d, camA: prevEnd, camB: dc, drift: 0.12, done: done, r0: done - 1, r1: done - 1 };
      dsc.flight = zoomPath(dsc.camA, dsc.camB, W); dsc.flyDur = clamp(0.9 + 0.45 * dsc.flight.S, 1.2, 3.8) * pace;
      dsc.dur = dsc.flyDur + clamp(2.6 + 0.42 * nItems, 3, 6.2) * pace;
      push(voiced(dsc, Math.max(0.35, dsc.flyDur - 0.5), 0.9));
      prevEnd = endCam(dsc);
      d.stops.forEach(function (s) {
        var tr = { key: "trv:" + s.i, type: "travel", stop: s, camA: prevEnd, camB: stopCam(s), drift: 0, done: s.i, r0: s.i - 1, r1: s.i };
        tr.flight = zoomPath(tr.camA, tr.camB, W);
        tr.dur = clamp(1.15 + 0.5 * tr.flight.S, 1.7, 4.6) * pace; tr.flyDur = tr.dur;
        push(voiced(tr, 0.2, 0.35));
        prevEnd = endCam(tr);
        var shown = (O.desc ? s.short.length : 0) + (O.note ? s.note.length : 0) + s.name.length + 30;
        var extraT = Math.min(10, ((O.hl ? s.hl.join(" ").length : 0) + (O.prac ? (s.hours + s.ticket).length : 0)) / 28);
        var st = { key: "stop:" + s.i, type: "stop", stop: s, camA: prevEnd, camB: prevEnd, drift: 0.3, flyDur: 0, done: s.i, r0: s.i, r1: s.i,
          dur: clamp(1.8 + shown / 20 + extraT, 6, 32) * pace };
        push(voiced(st, 0.6, 1.0 + extraT * pace));
        prevEnd = endCam(st);
        done = s.i + 1;
      });
    });
    var out = { key: "outro", type: "outro", dur: 7.2 * pace + (O.qr && O.qrUrl ? 1.5 : 0), camA: prevEnd, camB: fitCam(D.stops, LY.mapSide, W, H, Math.min(maxZ, 15), 0.12), drift: 0.1, done: N, r0: N - 1, r1: N - 1 };
    out.flight = zoomPath(out.camA, out.camB, W); out.flyDur = Math.min(2.2, out.dur * 0.35);
    push(voiced(out, 1.2, 2.4));
    var keys = {}; scenes.forEach(function (sc, i) { keys[sc.key] = i; });
    return { scenes: scenes, keys: keys, total: tt, LY: LY, bm: bm, W: W, H: H, N: N, D: D, O: O, T: T, NR: NR, AP: AP || null };
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
  // câu đang đọc ở thời điểm tau của cảnh (trình chiếu bằng giọng máy: lấy đúng câu máy đang đọc)
  function sentAt(V, sc, tau) {
    if (V.live && V.live.key === sc.key) return V.live.idx;
    var st = sc.sentT; if (!st || !st.length) return -1;
    for (var i = st.length - 1; i >= 0; i--) if (tau >= st[i].t0 - 0.05) return tau <= st[i].t1 + 0.35 ? i : -1;
    return -1;
  }
  function sentStarted(V, sc, tau) {
    if (V.live && V.live.key === sc.key) return V.live.idx;
    var st = sc.sentT; if (!st || !st.length) return -1;
    for (var i = st.length - 1; i >= 0; i--) if (tau >= st[i].t0 - 0.05) return i;
    return -1;
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
  // xuống dòng KHÔNG cắt bớt; mỗi dòng nhớ vị trí ký tự (a,b) trong đoạn gốc để tô sáng câu đang đọc
  function wrapAll(ctx, text, maxW) {
    text = String(text || ""); var out = [], cur = "", ca = 0, ce = 0, re = /\S+/g, m;
    while ((m = re.exec(text))) {
      var w = m[0], wa = m.index, test = cur ? cur + " " + w : w;
      if (ctx.measureText(test).width <= maxW) { if (!cur) ca = wa; cur = test; ce = wa + w.length; continue; }
      if (cur) out.push({ s: text.slice(ca, ce), a: ca, b: ce });
      var p = 0;
      while (w.length - p > 1 && ctx.measureText(w.slice(p)).width > maxW) {
        var k = w.length; while (k > p + 1 && ctx.measureText(w.slice(p, k)).width > maxW) k--;
        out.push({ s: w.slice(p, k), a: wa + p, b: wa + k }); p = k;
      }
      cur = w.slice(p); ca = wa + p; ce = wa + w.length;
    }
    if (cur) out.push({ s: text.slice(ca, ce), a: ca, b: ce });
    return out;
  }
  // một dòng vừa khung: thu nhỏ chữ trước (tới minScale), chỉ khi vẫn không vừa mới thêm "…"
  function fitLine(ctx, text, maxW, weight, px, minScale) {
    var f = px; ctx.font = F(weight, f);
    while (ctx.measureText(text).width > maxW && f > px * (minScale || 0.75)) { f *= 0.94; ctx.font = F(weight, f); }
    return { font: F(weight, f), text: ctx.measureText(text).width <= maxW ? text : (wrap(ctx, text, maxW, 1)[0] || text) };
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
      var fl = fitLine(ctx, s.name, w - (cx - x) - 30 * S, 700, 26 * S, 0.72);
      txt(ctx, fl.text, cx + 28 * S, yy, fl.font, "#fff", "left");
      ctx.restore();
    });
    if (d.stops.length > maxItems) txt(ctx, "+ " + (d.stops.length - maxItems) + " " + T.more, x, y + rowH * (list.length + 0.72), F(600, 24 * S), "#c9d4e3", "left", a0 * seg(tau, 0.6 + list.length * 0.17, 1.2 + list.length * 0.17));
  }
  function drawTravelChip(ctx, V, fs) {
    var sc = fs.sc, s = sc.stop, S = V.LY.S, tau = fs.tau, L = V.O.lang, T = V.T;
    var a = easeOut(seg(tau, 0.05, 0.4)) * (1 - seg(tau, sc.dur - 0.35, sc.dur)); if (a <= 0) return;
    var label;
    if (s.i === 0) label = "🚩 " + (V.D.startName ? T.from + ": " + V.D.startName + " → " : "") + s.name;
    else label = ((s.mode && s.mode.e) || "🚗") + " " + modeName(s.mode, L) + (s.travel ? " · " + durTxt(s.travel, L) : "") + "  →  " + s.num + ". " + s.name;
    ctx.save(); ctx.font = F(700, 27 * S); label = wrap(ctx, label, V.W * 0.84, 1)[0] || label;
    var tw = ctx.measureText(label).width, pw = tw + 48 * S, ph = 56 * S, x = (V.W - pw) / 2, y = V.LY.chipY + (1 - a) * -20 * S;
    ctx.globalAlpha *= a; rr(ctx, x, y, pw, ph, ph / 2); ctx.fillStyle = "rgba(15,33,56,0.9)"; ctx.shadowColor = "rgba(0,0,0,0.3)"; ctx.shadowBlur = 14 * S; ctx.fill();
    ctx.shadowBlur = 0; ctx.fillStyle = "#fff"; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText(label, V.W / 2, y + ph / 2 + 1 * S);
    ctx.restore();
  }
  function chipRow(ctx, chips, x, y, maxW, S, measureOnly) {
    ctx.font = F(700, 21 * S); var cx = x, cy = y, h = 38 * S, rows = 1;
    chips.forEach(function (c) {
      var w = ctx.measureText(c.t).width + 24 * S;
      if (cx + w > x + maxW && cx > x) { cx = x; cy += h + 8 * S; rows++; }
      if (!measureOnly) {
        rr(ctx, cx, cy, w, h, h / 2); ctx.fillStyle = c.bg; ctx.fill();
        ctx.fillStyle = c.fg; ctx.textAlign = "left"; ctx.textBaseline = "middle"; ctx.fillText(c.t, cx + 12 * S, cy + h / 2 + 1 * S);
      }
      cx += w + 8 * S;
    });
    return rows * h + (rows - 1) * 8 * S;
  }
  /* Thẻ điểm: giới thiệu ĐẦY ĐỦ (không cắt "…"). Nội dung dài thì chia trang, lật trang theo lời đọc. */

  function pageState(V, sc, m, tau) {
    var P = m.pages.length; if (P <= 1) return { i: 0, a: 1, prev: -1 };
    if (sc._pgm !== m) {
      sc._pgm = m;
      sc._pg = (sc.narr || []).map(function (x) {
        if (!x.ref) return -1;
        for (var p = 0; p < P; p++) for (var q = 0; q < m.pages[p].length; q++) { var it = m.pages[p][q]; if (it.k === x.ref.f && x.ref.a >= it.a - 1 && x.ref.a < it.b + 1) return p; }
        return -1;
      });
      var lastN = 0; sc._pg.forEach(function (p) { if (p > lastN) lastN = p; });
      sc.extraPages = P - 1 - lastN;
    }
    var of = sc._pg, starts = [], i, n;
    if (V.live && V.live.key === sc.key) {                 // trình chiếu giọng máy: theo câu đang đọc thật
      var cur = 0, idx = V.live.idx; for (n = 0; n <= idx && n < of.length; n++) if (of[n] > cur) cur = of[n];
      if (V.live.doneTau != null && sc.extraPages > 0) cur = Math.min(P - 1, Math.max(cur, P - 1 - sc.extraPages + Math.floor((tau - V.live.doneTau) / 3.4) + 1));
      var since = V.live.pgT && V.live.pg === cur ? tau - V.live.pgT : 0; if (V.live.pg !== cur) { V.live.prevPg = V.live.pg; V.live.pg = cur; V.live.pgT = tau; since = 0; }
      return { i: cur, a: clamp(since / 0.35, 0, 1), prev: V.live.prevPg == null ? -1 : V.live.prevPg };
    }
    var st = sc.sentT || [], lastEnd = 0, lastNP = 0;
    for (i = 0; i < P; i++) starts.push(i === 0 ? 0 : null);
    for (n = 0; n < of.length; n++) if (of[n] >= 0 && st[n]) {
      if (of[n] > 0) { var t0 = st[n].t0 - 0.2; if (starts[of[n]] == null || t0 < starts[of[n]]) starts[of[n]] = t0; }
      if (of[n] >= lastNP) { lastNP = of[n]; lastEnd = Math.max(lastEnd, st[n].t1); }
    }
    var from = null;
    for (i = 1; i < P; i++) if (starts[i] == null) { from = i; break; }
    if (from != null) {
      var a0 = Math.max(lastEnd + 0.4, (starts[from - 1] || 0) + 2.2), b0 = sc.dur - 0.8, k = P - from;
      if (b0 - a0 < k * 1.6) a0 = Math.max((starts[from - 1] || 0) + 1.2, b0 - k * 1.6);
      for (i = from; i < P; i++) starts[i] = a0 + (b0 - a0) * (i - from) / k;
    }
    var cur2 = 0; for (i = 0; i < P; i++) if (tau >= starts[i]) cur2 = i;
    return { i: cur2, a: clamp((tau - starts[cur2]) / 0.35, 0, 1), prev: cur2 - 1 };
  }

  function cardModel(ctx, V, s) {
    var key = "m2_" + V.W + "x" + V.H + "_" + (photoOf(s) ? 1 : 0);
    if (s[key]) return s[key];
    var LY = V.LY, S = LY.S, R = LY.card, O = V.O, T = V.T, land = LY.kind === "land", sq = LY.kind === "square";
    var pad = 30 * S, w = R.w - pad * 2, img = O.photo ? photoOf(s) : null;
    var chips = [];
    if (O.times && s.arr) chips.push({ t: "🕘 " + s.arr + (s.dep && s.dep !== s.arr ? "–" + s.dep : ""), bg: C.navy, fg: "#fff" });
    if (O.times && s.stay) chips.push({ t: "⏱ " + s.stay + " " + T.min, bg: "#efeadd", fg: C.navy });
    if (O.cost && s.cv) chips.push({ t: "🎟 " + s.cv.toLocaleString("vi-VN") + (s.cvu === "p" ? T.per : ""), bg: "#efeadd", fg: C.navy });
    function build(photoFrac, f) {
      var photoH = img ? Math.round(R.h * photoFrac) : Math.round(92 * S), head = [], hy = 0, np = (land ? 38 : 42) * S * f, nl;
      for (var tries = 0; tries < 6; tries++) { ctx.font = F(800, np); nl = wrapAll(ctx, s.name, w); if (nl.length <= 2 || np < 27 * S) break; np *= 0.9; }
      head.push({ lines: nl, font: F(800, np), color: C.navy, lh: np * 1.18 }); hy += nl.length * np * 1.18;
      if (s.ru) {
        var rf = F(500, 22 * S * f, true); ctx.font = rf; var rl = wrapAll(ctx, s.ru, w).slice(0, 2);
        head.push({ lines: rl, font: rf, color: C.muted, lh: 30 * S * f, after: 10 * S }); hy += rl.length * 30 * S * f + 10 * S;
      }
      var chipH = chips.length ? chipRow(ctx, chips, 0, 0, w, S, true) + 18 * S : 0;
      var top = photoH + 22 * S + hy + chipH + 6 * S, viewH = R.h - top - pad - 16 * S, items = [];
      function add(k, text, font, color, lh, after, indent, prefix) {
        if (!text) return; ctx.font = font;
        var ls = wrapAll(ctx, text, w - (indent || 0)), blk = items.length;
        ls.forEach(function (ln, j) { items.push({ k: k, s: ln.s, a: ln.a, b: ln.b, font: font, color: color, lh: lh, indent: indent || 0, first: j === 0, after: j === ls.length - 1 ? (after || 0) : 0, prefix: j === 0 ? prefix : null, blk: blk, n: ls.length }); });
      }
      if (O.desc) add("desc", s.short, F(400, 25.5 * S * f), "#2c3440", 36 * S * f, 14 * S);
      if (O.note && s.note) add("note", s.note, F(600, 22.5 * S * f, true), "#5a4a1e", 31 * S * f, 22 * S, 44 * S, "📝");
      if (O.hl) s.hl.forEach(function (h, j) { add("hl" + j, h, F(500, 23 * S * f), "#384150", 32 * S * f, 8 * S, 30 * S, "★"); });
      if (O.prac && s.hours) add("hours", T.hours + ": " + s.hours, F(500, 22 * S * f), "#384150", 31 * S * f, 6 * S, 32 * S, "🕒");
      if (O.prac && s.ticket) add("ticket", T.ticket + ": " + s.ticket, F(500, 22 * S * f), "#384150", 31 * S * f, 6 * S, 32 * S, "🎟");
      var pages = [], cur = [], y = 0;
      for (var i = 0; i < items.length; i++) {
        var it = items[i], extra = it.k === "note" && it.first ? 12 * S : 0;
        // khối ngắn (≤ 4 dòng) không bị cắt đôi sang trang sau; khối dài thì tránh để lại đúng 1 dòng ở cuối trang
        if (it.first && cur.length && ((it.n <= 4 && y + extra + it.lh * it.n > viewH) || (it.n > 4 && y + extra + it.lh * 2 > viewH))) { pages.push(cur); cur = []; y = 0; }
        else if (y + extra + it.lh > viewH && cur.length) { pages.push(cur); cur = []; y = 0; }
        y += extra; it.y = y; cur.push(it); y += it.lh + it.after;
      }
      if (cur.length) pages.push(cur);
      return { photoH: photoH, head: head, chips: chips, top: top, viewH: viewH, pages: pages, img: img, pad: pad, w: w };
    }
    var fr = img ? (land ? 0.36 : (sq ? 0.27 : 0.34)) : 0, m = build(fr, 1);
    if (m.pages.length > 1) { var m2 = build(img ? fr * 0.7 : 0, 0.93); if (m2.pages.length < m.pages.length) m = m2; }
    s[key] = m; return m;
  }
  // trang nào đang hiện ở thời điểm tau: trang có câu đang đọc; trang không có lời đọc (điểm nhấn, giờ, vé) chia đều phần thời gian còn lại
  function drawStopCard(ctx, V, fs) {
    var LY = V.LY, S = LY.S, R = LY.card, sc = fs.sc, s = sc.stop, tau = fs.tau, land = LY.kind === "land";
    var a = easeOut(seg(tau, 0.15, 0.7)), out = seg(tau, sc.dur - 0.5, sc.dur), alpha = a * (1 - out);
    if (alpha <= 0) return;
    var m = cardModel(ctx, V, s), off = (1 - a) * 70 * S + out * 40 * S;
    var x = R.x + (land ? off : 0), y = R.y + (land ? 0 : off), w = R.w, h = R.h;
    ctx.save(); ctx.globalAlpha *= alpha;
    rr(ctx, x, y, w, h, 28 * S); ctx.fillStyle = "rgba(251,248,241,0.97)"; ctx.shadowColor = "rgba(0,0,0,0.38)"; ctx.shadowBlur = 30 * S; ctx.shadowOffsetY = 8 * S; ctx.fill();
    ctx.shadowColor = "transparent"; ctx.shadowBlur = 0; ctx.shadowOffsetY = 0;
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
    var bx = x + m.pad + 26 * S, by = y + m.photoH;
    ctx.beginPath(); ctx.arc(bx, by, 30 * S, 0, 2 * PI); ctx.fillStyle = C.red; ctx.fill(); ctx.lineWidth = 5 * S; ctx.strokeStyle = "#fff"; ctx.stroke();
    ctx.font = F(800, 28 * S); ctx.fillStyle = "#fff"; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText(String(s.num), bx, by + 1 * S);
    var cx = x + m.pad, cy = y + m.photoH + 22 * S, k = 0;
    m.head.forEach(function (it) {
      var ap = appear(tau, 0.35 + (k++) * 0.13, 0.5);
      it.lines.forEach(function (ln) { cy += it.lh; txt(ctx, ln.s, cx, cy - it.lh * 0.16 + ap.dy * 14 * S, it.font, it.color, "left", ap.a); });
      cy += it.after || 0;
    });
    if (m.chips.length) { var apc = appear(tau, 0.35 + (k++) * 0.13, 0.5); ctx.save(); ctx.globalAlpha *= apc.a; chipRow(ctx, m.chips, cx, cy + 6 * S + apc.dy * 10 * S, m.w, S); ctx.restore(); }
    // phần chữ (theo trang) + tô sáng câu đang đọc
    var ps = pageState(V, sc, m, tau), base0 = y + m.top, apT = appear(tau, 0.35 + k * 0.13, 0.5);
    var voiced = !!(sc.ap || (V.live && V.live.key === sc.key)), hn = voiced ? sentAt(V, sc, tau) : -1, hr = hn >= 0 && sc.narr[hn] ? sc.narr[hn].ref : null;
    function drawPage(pi, al, dy) {
      var pg = m.pages[pi]; if (!pg || al <= 0.001) return;
      ctx.save(); ctx.globalAlpha *= al;
      var nb = null;
      pg.forEach(function (it) { if (it.k !== "note") return; if (!nb) nb = { y0: it.y, y1: it.y + it.lh }; else nb.y1 = it.y + it.lh; });
      if (nb) { var ny = base0 + nb.y0 - 8 * S + dy; ctx.fillStyle = "#fff3d6"; rr(ctx, cx - 6 * S, ny, m.w + 12 * S, nb.y1 - nb.y0 + 16 * S, 10 * S); ctx.fill(); ctx.fillStyle = C.gold; ctx.fillRect(cx - 6 * S, ny, 5 * S, nb.y1 - nb.y0 + 16 * S); }
      pg.forEach(function (it) {
        var bl = base0 + it.y + it.lh * 0.78 + dy, tx = cx + it.indent;
        if (it.prefix) txt(ctx, it.prefix, cx + (it.k === "note" ? 10 * S : 0), bl, it.font, it.k === "note" ? "#5a4a1e" : C.gold, "left");
        var inBlk = hr && it.k === hr.f, hit = inBlk && it.b > hr.a && it.a < hr.b;
        if (!inBlk) { txt(ctx, it.s, tx, bl, it.font, it.color, "left"); return; }
        txt(ctx, it.s, tx, bl, it.font, it.color, "left", 0.55);
        if (!hit) return;
        ctx.font = it.font;
        var i0 = clamp(hr.a - it.a, 0, it.s.length), i1 = clamp(hr.b - it.a, 0, it.s.length), pre = it.s.slice(0, i0), mid = it.s.slice(i0, i1).replace(/\s+$/, "");
        var x0 = tx + ctx.measureText(pre).width, mw = ctx.measureText(mid).width;
        ctx.save(); ctx.fillStyle = "rgba(242,193,78,0.30)"; rr(ctx, x0 - 3 * S, bl - it.lh * 0.7, mw + 6 * S, it.lh * 0.86, 5 * S); ctx.fill(); ctx.restore();
        txt(ctx, mid, x0, bl, it.font, it.k === "note" ? "#3d3010" : "#111a26", "left");
      });
      ctx.restore();
    }
    ctx.save(); ctx.globalAlpha *= apT.a;
    if (ps.prev >= 0 && ps.a < 1) drawPage(ps.prev, 1 - ps.a, -ps.a * 10 * S);
    drawPage(ps.i, ps.a, (1 - ps.a) * 14 * S + apT.dy * 12 * S);
    ctx.restore();
    if (m.pages.length > 1) {                              // chấm số trang
      var dn = m.pages.length, dr = 4.5 * S, gap = 14 * S, dx0 = x + w - m.pad - (dn - 1) * gap, dyy = y + h - 18 * S;
      for (var d = 0; d < dn; d++) { ctx.beginPath(); ctx.arc(dx0 + d * gap, dyy, d === ps.i ? dr * 1.25 : dr, 0, 2 * PI); ctx.fillStyle = d === ps.i ? C.gold : "rgba(21,44,78,0.22)"; ctx.fill(); }
    }
    ctx.restore();
  }
  function drawOutro(ctx, V, fs) {
    var LY = V.LY, S = LY.S, W = V.W, H = V.H, D = V.D, T = V.T, sc = fs.sc, tau = fs.tau, land = LY.kind === "land", O = V.O;
    var a0 = easeOut(seg(tau, 0.6, 1.3)) * (1 - seg(tau, sc.dur - 0.25, sc.dur));
    if (!land) panelBox(ctx, LY.panel, S, a0);
    var P = LY.panel, pad = land ? 0 : 36 * S, x = P.x + pad, w = P.w - pad * 2, room = P.h - (land ? 0 : 50 * S);
    var qr = O.qr && O.qrUrl ? qrCanvas(O.qrUrl) : null, qs = qr ? Math.min(w * 0.36, 210 * S) : 0, gap = 22 * S;
    var head = [{ text: "🏁 " + T.summary, font: F(800, 25 * S), color: C.gold2, lh: 34 * S, after: 10 * S, max: 1, at: 0.8 },
                { text: D.title, font: F(800, 50 * S), color: "#fff", lh: 58 * S, after: 26 * S, max: 2, at: 0.95 }];
    var stats = [[String(D.nDays), T.days], [String(V.N), T.stops]]; if (D.km >= 1) stats.push(["~" + Math.round(D.km), T.km]);
    function mkTail() {
      var t = [];
      if (O.cost && D.per) t.push({ text: "💰 " + T.cost + ": " + D.per + T.per, font: F(700, 26 * S), color: "#fff", lh: 38 * S, max: 3, at: 1.8, after: 6 * S });
      t.push({ text: T.thanks, font: F(800, 40 * S), color: C.gold2, lh: 52 * S, max: 3, at: 2.0, after: 8 * S });
      if (O.sign && O.credit) t.push({ text: "🎙️ " + O.credit, font: F(700, 24 * S), color: "#e6edf6", lh: 34 * S, max: 3, at: 2.2 });
      return t;
    }
    var head0 = measureStack(ctx, head, w), qh = qs ? qs + 54 * S : 0;
    // A: mã QR cạnh lời cảm ơn (khung ngang, nhiều chỗ theo chiều cao) · B: mã QR cột phải cạnh số liệu (khung dọc/vuông)
    var tailA = mkTail(), hA = head0 + 146 * S + Math.max(measureStack(ctx, tailA, w - (qs ? qs + gap : 0)), qh);
    var mode = "A", tail = tailA, hh = hA, tw = w - (qs ? qs + gap : 0), sw = w;
    if (qs && hA > room) {
      var tailB = mkTail(), twB = w - qs - gap, hB = head0 + Math.max(146 * S + measureStack(ctx, tailB, twB), qh);
      if (hB > room) { qs = Math.max(96 * S, qs - (hB - room)); qh = qs + 54 * S; twB = w - qs - gap; hB = head0 + Math.max(146 * S + measureStack(ctx, tailB, twB), qh); }
      mode = "B"; tail = tailB; hh = hB; tw = twB; sw = twB;
    }
    var y = P.y + Math.max(land ? 0 : 30 * S, (P.h - hh) / 2);
    y = stack(ctx, head, x, y, w, tau, a0, S);
    var yStats = y, cw = Math.min(sw / stats.length, 190 * S);
    stats.forEach(function (st, k) {
      var ap = appear(tau, 1.25 + k * 0.15, 0.5), bx = x + k * cw;
      txt(ctx, st[0], bx, y + 70 * S + ap.dy * 16 * S, F(900, 68 * S), "#fff", "left", ap.a * a0);
      txt(ctx, st[1], bx + 2 * S, y + 104 * S + ap.dy * 16 * S, F(700, 23 * S), C.gold2, "left", ap.a * a0);
    });
    y += 146 * S;
    stack(ctx, tail, x, y, tw, tau, a0, S);
    if (qr) {
      var ap2 = appear(tau, 2.4, 0.6), qx = x + w - qs, qy = (mode === "B" ? yStats + 8 * S : y + 6 * S) + ap2.dy * 16 * S;
      ctx.save(); ctx.globalAlpha *= a0 * ap2.a;
      rr(ctx, qx, qy, qs, qs, 14 * S); ctx.fillStyle = "#fff"; ctx.shadowColor = "rgba(0,0,0,0.3)"; ctx.shadowBlur = 14 * S; ctx.fill(); ctx.shadowBlur = 0;
      var n = qr.width, inner = qs - 26 * S, mod = Math.floor(inner / n), sz = mod >= 2 ? mod * n : inner;
      ctx.imageSmoothingEnabled = false; ctx.drawImage(qr, Math.round(qx + (qs - sz) / 2), Math.round(qy + (qs - sz) / 2), sz, sz); ctx.imageSmoothingEnabled = true;
      txt(ctx, T.qr, qx + qs / 2, qy + qs + 26 * S, F(700, 17 * S), C.gold2, "center");
      var su = shortUrl(O.qrUrl); ctx.font = F(500, 14.5 * S); su = wrap(ctx, su, qs + 30 * S, 1)[0] || su;
      txt(ctx, su, qx + qs / 2, qy + qs + 46 * S, F(500, 14.5 * S), "#e6edf6", "center");
      ctx.restore();
    }
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
    var mins = V.O.clock ? clockAt(V, fs) : null;
    if (mins != null) { var tc = tintAt(mins); if (tc) { ctx.fillStyle = tc; ctx.fillRect(0, 0, W, H); } }
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
    if (mins != null) drawClock(ctx, V, fs, mins);
    drawCaption(ctx, V, fs);
    if (V.bm.attr) txt(ctx, V.bm.attr, 14 * S, V.LY.footY, F(500, 14 * S), "rgba(255,255,255,0.72)", "left");
    if (V.O.sign && V.O.credit) txt(ctx, V.O.credit, W - 16 * S, V.LY.footY, F(700, 17 * S), "rgba(255,255,255,0.82)", "right");
    var fade = Math.max(1 - seg(t, 0, 0.6), seg(t, V.total - 0.8, V.total));
    if (fade > 0) { ctx.fillStyle = "rgba(0,0,0," + fade.toFixed(3) + ")"; ctx.fillRect(0, 0, W, H); }
    ctx.restore();
    return fs;
  }  /* ---- đồng hồ hành trình + ánh sáng theo giờ trong ngày ---- */
  function hmMin(hm) { var m = String(hm || "").match(/(\d{1,2}):(\d{2})/); return m ? (+m[1]) * 60 + (+m[2]) : null; }
  function clockAt(V, fs) {
    var sc = fs.sc, tau = fs.tau, s, a, b;
    if (sc.type === "day") return hmMin(sc.day.start || "08:00");
    if (sc.type === "travel") {
      s = sc.stop; b = hmMin(s.arr); if (b == null) return null;
      var prev = V.D.stops[s.i - 1];
      a = (prev && prev.day === s.day) ? hmMin(prev.dep || prev.arr) : null;
      if (a == null) { var dd = V.D.days.filter(function (d) { return d.day === s.day; })[0]; a = hmMin((dd && dd.start) || ""); }
      if (a == null || a > b) a = b - (s.travel || 0);
      return lerp(a, b, ease(clamp(tau / (sc.flyDur || sc.dur), 0, 1)));
    }
    if (sc.type === "stop") {
      s = sc.stop; a = hmMin(s.arr); if (a == null) return null;
      b = hmMin(s.dep); if (b == null || b < a) b = a + (s.stay || 0);
      return lerp(a, b, clamp(tau / sc.dur, 0, 1));
    }
    return null;
  }
  var TINT = [[0, [12, 22, 70, 0.34]], [290, [12, 22, 70, 0.30]], [380, [255, 150, 110, 0.12]], [470, [255, 200, 150, 0]], [940, [255, 190, 90, 0]],
              [1040, [255, 160, 60, 0.13]], [1130, [140, 70, 130, 0.17]], [1220, [14, 24, 72, 0.30]], [1440, [12, 22, 70, 0.34]]];
  function tintAt(mins) {
    var m = ((mins % 1440) + 1440) % 1440;
    for (var i = 1; i < TINT.length; i++) if (m <= TINT[i][0]) {
      var A = TINT[i - 1], B = TINT[i], u = (m - A[0]) / (B[0] - A[0]), c = A[1].map(function (v, k) { return lerp(v, B[1][k], u); });
      return c[3] < 0.01 ? null : "rgba(" + Math.round(c[0]) + "," + Math.round(c[1]) + "," + Math.round(c[2]) + "," + c[3].toFixed(3) + ")";
    }
    return null;
  }
  function drawClock(ctx, V, fs, mins) {
    var LY = V.LY, S = LY.S, sc = fs.sc, W = V.W, H = V.H, land = LY.kind === "land", tau = fs.tau;
    var a = sc.type === "day" ? easeOut(seg(tau - dayOffset(sc), 0, 0.5)) * (1 - seg(tau, sc.dur - 0.4, sc.dur))
          : sc.type === "stop" ? easeOut(seg(tau, 0.2, 0.7)) * (1 - seg(tau, sc.dur - 0.5, sc.dur)) : 1;
    if (a <= 0) return;
    var r = (land ? 40 : 44) * S, cx, cy;
    if (land) { if (sc.type === "stop") { cx = LY.card.x - r - 24 * S; cy = LY.card.y + r + 6 * S; } else { cx = W - r - 26 * S; cy = r + 30 * S; } }
    else { cx = W - r - 22 * S; cy = sc.type === "stop" ? LY.mapCard.y + r + 18 * S : H * 0.135 + r; }
    ctx.save(); ctx.globalAlpha *= a;
    ctx.beginPath(); ctx.arc(cx, cy, r, 0, 2 * PI); ctx.fillStyle = "rgba(251,248,241,0.96)"; ctx.shadowColor = "rgba(0,0,0,0.35)"; ctx.shadowBlur = 12 * S; ctx.fill();
    ctx.shadowBlur = 0; ctx.lineWidth = 3 * S; ctx.strokeStyle = C.navy; ctx.stroke();
    for (var i = 0; i < 12; i++) {
      var an = i / 12 * 2 * PI, r1 = r * (i % 3 === 0 ? 0.7 : 0.8), r2 = r * 0.88;
      ctx.beginPath(); ctx.moveTo(cx + Math.sin(an) * r1, cy - Math.cos(an) * r1); ctx.lineTo(cx + Math.sin(an) * r2, cy - Math.cos(an) * r2);
      ctx.lineWidth = (i % 3 === 0 ? 2.6 : 1.3) * S; ctx.strokeStyle = C.navy; ctx.stroke();
    }
    function hand(frac, len, wd, col) { var an = frac * 2 * PI; ctx.beginPath(); ctx.moveTo(cx - Math.sin(an) * len * 0.16, cy + Math.cos(an) * len * 0.16); ctx.lineTo(cx + Math.sin(an) * len, cy - Math.cos(an) * len); ctx.lineCap = "round"; ctx.lineWidth = wd; ctx.strokeStyle = col; ctx.stroke(); }
    hand(((mins / 60) % 12) / 12, r * 0.5, 4.4 * S, C.navy); hand((mins % 60) / 60, r * 0.74, 2.6 * S, C.navy);
    ctx.beginPath(); ctx.arc(cx, cy, 3.8 * S, 0, 2 * PI); ctx.fillStyle = C.red; ctx.fill();
    var hh = Math.floor(mins / 60) % 24, mm = Math.floor(mins % 60), lab = (hh < 10 ? "0" : "") + hh + ":" + (mm < 10 ? "0" : "") + mm;
    var ic = (mins % 1440) >= 360 && (mins % 1440) < 1110 ? "☀️" : ((mins % 1440) >= 1110 && (mins % 1440) < 1260 ? "🌇" : "🌙");
    ctx.font = F(800, 18 * S); var tw = ctx.measureText(lab).width + 34 * S, ph = 28 * S, py = cy + r + 8 * S;
    rr(ctx, cx - tw / 2, py, tw, ph, ph / 2); ctx.fillStyle = "rgba(15,33,56,0.9)"; ctx.fill();
    txt(ctx, ic, cx - tw / 2 + 15 * S, py + ph * 0.72, F(400, 14 * S), "#fff", "center");
    txt(ctx, lab, cx + 9 * S, py + ph * 0.73, F(800, 18 * S), "#fff", "center");
    ctx.restore();
  }
  /* ---- phụ đề (câu đang đọc) — không hiện ở cảnh thẻ điểm vì chữ đã có trên thẻ ---- */
  function drawCaption(ctx, V, fs) {
    var O = V.O, sc = fs.sc; if (!O.caps || sc.type === "stop" || V.cover) return;
    var live = V.live && V.live.key === sc.key; if (!(sc.ap || live)) return;
    var n = sentAt(V, sc, fs.tau); if (n < 0 || !sc.narr[n]) return;
    var LY = V.LY, S = LY.S, W = V.W, H = V.H, land = LY.kind === "land", st = (sc.sentT && sc.sentT[n]) || { t0: fs.tau, t1: fs.tau + 3 };
    var a = live ? 1 : Math.min(seg(fs.tau, st.t0 - 0.05, st.t0 + 0.15), 1 - seg(fs.tau, st.t1 + 0.15, st.t1 + 0.35)); if (a <= 0) return;
    var fz = (land ? 29 : 33) * S, onMap = land && sc.type !== "travel", maxW = onMap ? W * 0.5 : Math.min(W * (land ? 0.7 : 0.88), 1150 * S);
    ctx.save(); ctx.font = F(600, fz);
    var lines = wrapAll(ctx, sc.narr[n].c, maxW).map(function (l) { return l.s; }), chunks = [];
    for (var i = 0; i < lines.length; i += 2) chunks.push(lines.slice(i, i + 2));
    var ci = 0;
    if (chunks.length > 1 && !live) {
      var tot = 0, acc = 0, u = clamp((fs.tau - st.t0) / Math.max(0.3, st.t1 - st.t0), 0, 0.999);
      chunks.forEach(function (c) { tot += c.join(" ").length; });
      for (i = 0; i < chunks.length; i++) { acc += chunks[i].join(" ").length; if (u < acc / tot) { ci = i; break; } }
    }
    var ls = chunks[ci] || [], lh = fz * 1.3, bw = 0; ls.forEach(function (l) { bw = Math.max(bw, ctx.measureText(l).width); });
    bw += 40 * S; var bh = ls.length * lh + 18 * S;
    var cx = onMap ? W * 0.715 : W / 2, by = land ? H * 0.885 : (sc.type === "travel" ? H * 0.95 : LY.mapSide.y + LY.mapSide.h - 14 * S);
    ctx.globalAlpha *= a; rr(ctx, cx - bw / 2, by - bh, bw, bh, 12 * S); ctx.fillStyle = "rgba(8,16,30,0.78)"; ctx.fill();
    ls.forEach(function (l, k) { txt(ctx, l, cx, by - bh + 9 * S + lh * (k + 0.78), F(600, fz), "#fff", "center"); });
    ctx.restore();
  }
  /* ---- mã QR (thư viện qrcode-generator, MIT — nạp khi cần) ---- */
  var QR = { url: null, cv: null, st: 0 };
  function ensureQR() {
    if (global.qrcode) return Promise.resolve(true);
    if (!QR.p) QR.p = loadScript(BASE + "vendor/qrcode.min.js").then(function () { QR.st = 2; if (_onAsset) { try { _onAsset(); } catch (e) { } } return true; }, function () { QR.st = 3; return false; });
    return QR.p;
  }
  function qrCanvas(url) {
    if (QR.url === url && QR.cv) return QR.cv;
    if (!global.qrcode) { ensureQR(); return null; }
    try {
      var lib = global.qrcode; if (lib.stringToBytesFuncs && lib.stringToBytesFuncs["UTF-8"]) lib.stringToBytes = lib.stringToBytesFuncs["UTF-8"];
      var q = lib(0, "M"); q.addData(url); q.make();
      var n = q.getModuleCount(), cv = document.createElement("canvas"); cv.width = cv.height = n;
      var c2 = cv.getContext("2d"); c2.fillStyle = "#fff"; c2.fillRect(0, 0, n, n); c2.fillStyle = C.navy2;
      for (var r = 0; r < n; r++) for (var c = 0; c < n; c++) if (q.isDark(r, c)) c2.fillRect(c, r, 1, 1);
      QR.url = url; QR.cv = cv; return cv;
    } catch (e) { return null; }
  }
  function shortUrl(u) { return String(u || "").replace(/^https?:\/\/(www\.)?/i, "").replace(/\/$/, ""); }
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

  /* ================= 9. GIỌNG ĐỌC AI (Piper) — chạy ngay trong trình duyệt =================
     onnxruntime-web (MIT, cdnjs) + piper-phonemize/espeak-ng (wasm, jsDelivr) + mô hình giọng Piper (Hugging Face):
       🇻🇳 vi_VN-vais1000-medium (dữ liệu VAIS-1000, CC BY 4.0) · 🇷🇺 ru_RU-denis-medium (CC0) · 🇬🇧 en_US-ljspeech-medium (LJSpeech, public domain)
     Lần đầu tải ~60 MB mỗi giọng + ~30 MB bộ chạy, lưu trong Cache Storage của trình duyệt cho lần sau.
     Câu đã đọc cũng được lưu lại (Cache Storage) nên xuất lại video chỉ đọc những câu mới sửa. */
  var AIV = (function () {
    var ORT_JS = "https://cdnjs.cloudflare.com/ajax/libs/onnxruntime-web/1.18.0/ort.wasm.min.js";
    var ORT_BASE = "https://cdnjs.cloudflare.com/ajax/libs/onnxruntime-web/1.18.0/";
    var PH_BASE = "https://cdn.jsdelivr.net/npm/@diffusionstudio/piper-wasm@1.0.0/build/";
    var HF = ["https://huggingface.co/diffusionstudio/piper-voices/resolve/main/", "https://huggingface.co/rhasspy/piper-voices/resolve/main/"];
    var VOICES = {
      vi: { path: "vi/vi_VN/vais1000/medium/vi_VN-vais1000-medium.onnx", mb: 61, name: "VAIS-1000", lic: "CC BY 4.0", g: "nữ" },
      ru: { path: "ru/ru_RU/denis/medium/ru_RU-denis-medium.onnx", mb: 61, name: "Denis", lic: "CC0", g: "nam" },
      en: { path: "en/en_US/ljspeech/medium/en_US-ljspeech-medium.onnx", mb: 64, name: "LJSpeech", lic: "public domain", g: "nữ" }
    };
    var CACHE = "tv-piper-v1", SAYC = "tv-say-v1";
    var MODEL = {}, CFG = {}, SESS = {}, pend = {}, ortP = null, phP = null, PH = null, memo = new Map(), W = {}, wseq = 0, noWorker = false;
    function supported() { return !!(global.WebAssembly && global.fetch && typeof BigInt64Array !== "undefined"); }
    async function cacheOpen(n) { try { return global.caches ? await caches.open(n) : null; } catch (e) { return null; } }
    async function fetchCached(url, onProg) {
      var c = await cacheOpen(CACHE);
      if (c) { try { var hit = await c.match(url); if (hit) { var b0 = await hit.arrayBuffer(); if (onProg) onProg(b0.byteLength, b0.byteLength, true); return b0; } } catch (e) { } }
      var res = await fetch(url, { mode: "cors" }); if (!res.ok) throw new Error("HTTP " + res.status + " — " + url);
      var total = +res.headers.get("content-length") || 0, buf;
      if (res.body && res.body.getReader) {
        var rd = res.body.getReader(), parts = [], got = 0;
        for (;;) { var r = await rd.read(); if (r.done) break; parts.push(r.value); got += r.value.length; if (onProg) onProg(got, total); }
        buf = new Uint8Array(got); var o = 0; parts.forEach(function (p) { buf.set(p, o); o += p.length; }); buf = buf.buffer;
      } else buf = await res.arrayBuffer();
      if (c) { try { await c.put(url, new Response(buf.slice(0), { headers: { "content-type": "application/octet-stream" } })); } catch (e) { } }
      return buf;
    }
    async function fetchVoice(file, onProg) {
      var err = null;
      for (var i = 0; i < HF.length; i++) { try { return await fetchCached(HF[i] + file, onProg); } catch (e) { err = e; } }
      throw err;
    }
    async function isCached(lang) { var c = await cacheOpen(CACHE); if (!c) return false; try { for (var i = 0; i < HF.length; i++) if (await c.match(HF[i] + VOICES[lang].path)) return true; } catch (e) { } return false; }
    function ensureOrt() { return ortP || (ortP = (async function () { if (!global.ort) await loadScript(ORT_JS); ort.env.wasm.wasmPaths = ORT_BASE; ort.env.wasm.numThreads = 1; })()); }
    function ensurePhon(onProg) {
      return phP || (phP = (async function () {
        if (!global.createPiperPhonemize) await loadScript(PH_BASE + "piper_phonemize.js");
        var wb = await fetchCached(PH_BASE + "piper_phonemize.wasm");
        var mod = await WebAssembly.compile(wb), data = await fetchCached(PH_BASE + "piper_phonemize.data", onProg);
        PH = { mod: mod, data: data }; return PH;
      })().catch(function (e) { phP = null; throw e; }));
    }
    async function phonemize(text, voice) {
      var P = await ensurePhon(), outs = [];
      var m = await global.createPiperPhonemize({ print: function (d) { outs.push(d); }, printErr: function () { }, locateFile: function (u) { return PH_BASE + u; },
        instantiateWasm: function (imports, cb) { WebAssembly.instantiate(P.mod, imports).then(function (inst) { cb(inst); }); return {}; },
        getPreloadedPackage: function () { return P.data; } });
      m.callMain(["-l", voice, "--input", JSON.stringify([{ text: text }]), "--espeak_data", "/espeak-ng-data"]);
      for (var i = 0; i < outs.length; i++) { try { var j = JSON.parse(outs[i]); if (j && j.phoneme_ids) return j.phoneme_ids; } catch (e) { } }
      return [];
    }
    // tải giọng (mô hình + cấu hình); onProg(phần đã tải, tổng, từ bộ nhớ đệm?)
    function load(lang, onProg) {
      if (MODEL[lang]) return Promise.resolve();
      if (pend[lang]) return pend[lang];
      var v = VOICES[lang]; if (!v) return Promise.reject(new Error("Chưa có giọng AI cho " + lang));
      pend[lang] = (async function () {
        CFG[lang] = JSON.parse(new TextDecoder().decode(await fetchVoice(v.path + ".json")));
        MODEL[lang] = await fetchVoice(v.path, onProg);
      })().catch(function (e) { pend[lang] = null; throw e; });
      return pend[lang];
    }
    // ---- chạy mô hình: nhiều Web Worker song song (nhanh hơn), lỗi thì chạy ngay trên trang ----
    var WSRC = "self.onmessage=async function(e){var d=e.data;try{" +
      "if(d.t==='init'){importScripts(d.ort);ort.env.wasm.wasmPaths=d.base;ort.env.wasm.numThreads=1;self.S={};postMessage({t:'ok',id:d.id});}" +
      "else if(d.t==='load'){self.S[d.lang]={s:await ort.InferenceSession.create(new Uint8Array(d.model),{executionProviders:['wasm']}),cfg:d.cfg};postMessage({t:'ok',id:d.id});}" +
      "else if(d.t==='run'){var L=self.S[d.lang],c=L.cfg,inf=c.inference||{},ids=d.ids;" +
      "var f={input:new ort.Tensor('int64',BigInt64Array.from(ids,function(x){return BigInt(x)}),[1,ids.length])," +
      "input_lengths:new ort.Tensor('int64',BigInt64Array.from([BigInt(ids.length)]),[1])," +
      "scales:new ort.Tensor('float32',Float32Array.from([inf.noise_scale==null?0.667:inf.noise_scale,(inf.length_scale==null?1:inf.length_scale)/(d.rate||1),inf.noise_w==null?0.8:inf.noise_w]),[3])};" +
      "if((c.num_speakers||1)>1)f.sid=new ort.Tensor('int64',BigInt64Array.from([BigInt(0)]),[1]);" +
      "var r=await L.s.run(f);var pcm=new Float32Array(r.output.data);postMessage({t:'ok',id:d.id,pcm:pcm},[pcm.buffer]);}" +
      "}catch(err){postMessage({t:'err',id:d.id,msg:String(err&&err.message||err)})}};";
    function mkWorker() {
      var url = URL.createObjectURL(new Blob([WSRC], { type: "text/javascript" })), w = new Worker(url), o = { w: w, cb: {} };
      setTimeout(function () { URL.revokeObjectURL(url); }, 60000);
      w.onmessage = function (e) { var d = e.data, f = o.cb[d.id]; if (f) { delete o.cb[d.id]; f(d); } };
      w.onerror = function (e) { var cbs = o.cb; o.cb = {}; o.dead = true; for (var k in cbs) cbs[k]({ t: "err", msg: (e && e.message) || "worker error" }); };
      return o;
    }
    function wcall(o, msg, tr) { return new Promise(function (res, rej) { var id = ++wseq; msg.id = id; o.cb[id] = function (d) { if (d.t === "err") rej(new Error(d.msg)); else res(d); }; o.w.postMessage(msg, tr || []); }); }
    function nWorkers(lang) { var hc = navigator.hardwareConcurrency || 4, mem = navigator.deviceMemory || 4; return lang === "vi" || lang === "en" ? clamp(Math.min(Math.floor(hc / 2), mem >= 8 ? 3 : 2), 1, 3) : 1; }
    async function workersFor(lang) {
      if (noWorker || !global.Worker) return null;
      if (W[lang]) return W[lang];
      var list = [], n = nWorkers(lang);
      try {
        for (var i = 0; i < n; i++) { var o = mkWorker(); await wcall(o, { t: "init", ort: ORT_JS, base: ORT_BASE }); await wcall(o, { t: "load", lang: lang, model: MODEL[lang], cfg: CFG[lang] }); list.push(o); }
      } catch (e) { list.forEach(function (o) { try { o.w.terminate(); } catch (er) { } }); if (!list.length) { noWorker = true; return null; } }
      W[lang] = list; return list;
    }
    async function sessMain(lang) {
      if (SESS[lang]) return SESS[lang];
      await ensureOrt(); SESS[lang] = await ort.InferenceSession.create(new Uint8Array(MODEL[lang]), { executionProviders: ["wasm"] }); return SESS[lang];
    }
    async function runMain(lang, ids, rate) {
      var s = await sessMain(lang), c = CFG[lang], inf = c.inference || {};
      var f = { input: new ort.Tensor("int64", BigInt64Array.from(ids, function (x) { return BigInt(x); }), [1, ids.length]),
        input_lengths: new ort.Tensor("int64", BigInt64Array.from([BigInt(ids.length)]), [1]),
        scales: new ort.Tensor("float32", Float32Array.from([inf.noise_scale == null ? 0.667 : inf.noise_scale, (inf.length_scale == null ? 1 : inf.length_scale) / (rate || 1), inf.noise_w == null ? 0.8 : inf.noise_w]), [3]) };
      if ((c.num_speakers || 1) > 1) f.sid = new ort.Tensor("int64", BigInt64Array.from([BigInt(0)]), [1]);
      var r = await s.run(f); return new Float32Array(r.output.data);
    }
    // cắt khoảng lặng đầu/cuối, chuẩn hoá độ to cho giọng Việt và giọng Nga nghe đều nhau
    function tidy(pcm, sr) {
      var n = pcm.length, th = 0.008, i0 = 0, i1 = n - 1, pad = Math.round(sr * 0.035);
      while (i0 < n && Math.abs(pcm[i0]) < th) i0++;
      while (i1 > i0 && Math.abs(pcm[i1]) < th) i1--;
      if (i1 <= i0) return new Float32Array(0);
      var out = pcm.slice(Math.max(0, i0 - pad), Math.min(n, i1 + pad + 1)), sum = 0, pk = 0, k;
      for (k = 0; k < out.length; k++) { var v = out[k]; sum += v * v; if (v > pk) pk = v; else if (-v > pk) pk = -v; }
      var rms = Math.sqrt(sum / Math.max(1, out.length)), g = rms > 1e-4 ? 0.1 / rms : 1; g = Math.min(g, 0.97 / Math.max(pk, 1e-4), 5);
      var fz = Math.min(out.length >> 1, Math.round(sr * 0.006));
      for (k = 0; k < out.length; k++) out[k] *= g;
      for (k = 0; k < fz; k++) { out[k] *= k / fz; out[out.length - 1 - k] *= k / fz; }
      return out;
    }
    function skey(lang, rate, text) { return "https://tv-say.local/" + lang + "/" + rate + "/" + md5(VOICES[lang].path + "|" + text); }
    async function getSaved(lang, rate, text) {
      var c = await cacheOpen(SAYC); if (!c) return null;
      try { var r = await c.match(skey(lang, rate, text)); if (!r) return null; var sr = +r.headers.get("x-sr") || 22050, b = await r.arrayBuffer(), i16 = new Int16Array(b), f = new Float32Array(i16.length);
        for (var i = 0; i < i16.length; i++) f[i] = i16[i] / 32767; return { pcm: f, sr: sr }; } catch (e) { return null; }
    }
    async function putSaved(lang, rate, text, clip) {
      var c = await cacheOpen(SAYC); if (!c) return;
      try { var i16 = new Int16Array(clip.pcm.length); for (var i = 0; i < i16.length; i++) i16[i] = Math.max(-32767, Math.min(32767, Math.round(clip.pcm[i] * 32767)));
        await c.put(skey(lang, rate, text), new Response(i16.buffer, { headers: { "content-type": "application/octet-stream", "x-sr": String(clip.sr) } })); } catch (e) { }
    }
    function sayText(seg) { var t = seg.t; if (seg.l === "ru" && !/[.!?,;:]$/.test(t)) t += ","; return t; }
    /* Đọc toàn bộ lời thuyết minh → AP = { scenes: { key: { dur, sents:[{t0,t1}], clips:[{t, pcm, sr}] } } } */
    async function synthNarration(NR, O, ui, isCancelled) {
      var rate = +O.rate || 1, need = {}, jobs = [], seen = {}, k, key;
      for (key in NR) NR[key].forEach(function (s) { s.segs.forEach(function (g) { if (!VOICES[g.l]) return; need[g.l] = 1; var t = sayText(g), id = g.l + "|" + t; if (!seen[id]) { seen[id] = 1; jobs.push({ l: g.l, t: t }); } }); });
      var langs = Object.keys(need);
      // 1) tải bộ chạy + giọng
      var steps = [{ k: "phon", label: "bộ phân tích phát âm", mb: 19 }].concat(langs.map(function (l) { return { k: l, label: "giọng " + (l === "vi" ? "Việt" : l === "ru" ? "Nga" : "Anh"), mb: VOICES[l].mb }; }));
      var totMB = steps.reduce(function (s, x) { return s + x.mb; }, 0), doneMB = 0;
      for (var si = 0; si < steps.length; si++) {
        var st = steps[si];
        var prog = function (got, tot, cached) { var f = tot ? got / tot : 0; ui.phase((cached ? "Đã có sẵn " : "Đang tải ") + st.label + (tot && !cached ? ": " + (got / 1048576).toFixed(0) + "/" + (tot / 1048576).toFixed(0) + " MB" : "") + " (lần đầu cần ~" + totMB + " MB, lần sau dùng lại)", (doneMB + st.mb * f) / totMB * 0.3); };
        if (st.k === "phon") { await ensureOrt(); await ensurePhon(prog); } else await load(st.k, prog);
        doneMB += st.mb; if (isCancelled && isCancelled()) throw new Error("cancel");
      }
      // 2) đọc từng đoạn (dùng lại câu đã đọc lần trước)
      var todo = [], t0 = Date.now(), nDone = 0;
      for (k = 0; k < jobs.length; k++) {
        var j = jobs[k], mk = j.l + "|" + rate + "|" + j.t;
        if (memo.has(mk)) { j.clip = memo.get(mk); continue; }
        var sv = await getSaved(j.l, rate, j.t); if (sv) { j.clip = sv; memo.set(mk, sv); continue; }
        todo.push(j);
      }
      function tick() { nDone++; var el = (Date.now() - t0) / 1000, eta = nDone > 2 ? el / nDone * (todo.length - nDone) : 0; ui.phase("Đang tạo giọng đọc AI: " + nDone + "/" + todo.length + " đoạn" + (eta > 3 ? " · còn ~" + fmtClock(eta) : ""), 0.3 + 0.7 * nDone / Math.max(1, todo.length)); }
      if (todo.length) ui.phase("Đang tạo giọng đọc AI: 0/" + todo.length + " đoạn…", 0.3);
      var byL = {}; todo.forEach(function (j) { (byL[j.l] = byL[j.l] || []).push(j); });
      async function finish(j, pcm) { var sr = CFG[j.l].audio.sample_rate || 22050, clip = { pcm: tidy(pcm, sr), sr: sr }; j.clip = clip; memo.set(j.l + "|" + rate + "|" + j.t, clip); putSaved(j.l, rate, j.t, clip); tick(); }
      await Promise.all(Object.keys(byL).map(async function (l) {
        var q = byL[l], voice = CFG[l].espeak && CFG[l].espeak.voice || l, ws = await workersFor(l);
        for (var i = 0; i < q.length; i++) q[i].ids = null;
        async function lane(o) {
          while (q.length) {
            if (isCancelled && isCancelled()) throw new Error("cancel");
            var j = q.shift(); j.ids = await phonemize(j.t, voice);
            if (!j.ids.length) { await finish(j, new Float32Array(0)); continue; }
            var pcm = o ? (await wcall(o, { t: "run", lang: l, ids: j.ids, rate: rate })).pcm : await runMain(l, j.ids, rate);
            await finish(j, pcm);
            if (!o) await sleep(0);
          }
        }
        if (ws && ws.length) await Promise.all(ws.map(lane)); else await lane(null);
      }));
      // 3) xếp thời gian từng cảnh
      var clipOf = {}; jobs.forEach(function (j) { clipOf[j.l + "|" + j.t] = j.clip; });
      var AP = { rate: rate, scenes: {} }, gr = 1 / Math.max(0.7, rate);
      for (key in NR) {
        var t = 0, sents = [], clips = [];
        NR[key].forEach(function (s, si2) {
          var st0 = t, prevEnd = "";
          s.segs.forEach(function (g, gi) {
            var c = clipOf[g.l + "|" + sayText(g)]; if (!c || !c.pcm.length) return;
            if (gi > 0) t += (/[.!?]$/.test(prevEnd) ? 0.28 : /[,;:]$/.test(prevEnd) ? 0.14 : 0.05) * gr;
            clips.push({ t: t, pcm: c.pcm, sr: c.sr, l: g.l }); t += c.pcm.length / c.sr; prevEnd = g.t.trim();
          });
          sents.push({ t0: st0, t1: t }); t += 0.36 * gr;
        });
        AP.scenes[key] = { dur: Math.max(0, t - 0.36 * gr), sents: sents, clips: clips };
      }
      return AP;
    }
    function dispose() { for (var l in W) (W[l] || []).forEach(function (o) { try { o.w.terminate(); } catch (e) { } }); W = {}; }
    async function storageInfo() { var o = {}; for (var l in VOICES) o[l] = await isCached(l); return o; }
    async function clearAll() { try { await caches.delete(CACHE); await caches.delete(SAYC); } catch (e) { } MODEL = {}; CFG = {}; SESS = {}; pend = {}; memo.clear(); dispose(); }
    return { VOICES: VOICES, supported: supported, load: load, synthNarration: synthNarration, phonemize: phonemize, dispose: dispose, storageInfo: storageInfo, clearAll: clearAll,
             credit: function (langs) { return (langs || ["vi", "ru"]).map(function (l) { var v = VOICES[l]; return v ? v.name + " (" + v.lic + ")" : ""; }).filter(Boolean).join(", "); } };
  })();

  /* ================= 10. NHẠC NỀN + TRỘN TIẾNG + MÃ HOÁ ÂM THANH =================
     Nhạc dựng sẵn do chính trình duyệt tổng hợp (không dùng bản ghi của ai → không vướng bản quyền):
       calm (Nhẹ nhàng) · upbeat (Rộn ràng) · journey (Hành trình) · folk (giai điệu dân ca Nga «Коробейники», thế kỷ 19 — phạm vi công cộng)
       · ngu (Ngũ cung — giai điệu tự soạn, đàn tranh + sáo) · zen (Suy ngẫm — piano mềm, nền tĩnh)
     Hoặc nhạc của anh (MP3/M4A/WAV…). Nhạc tự nhỏ lại khi có lời đọc, mở/kết mượt. */
  var MUSIC = (function () {
    var PRE = {
      calm: { name: "🌿 Nhẹ nhàng", bpm: 72 }, upbeat: { name: "☀️ Rộn ràng", bpm: 112 },
      journey: { name: "🏔️ Hành trình", bpm: 66 }, folk: { name: "🪕 Dân ca Nga", bpm: 104 },
      ngu: { name: "🎋 Ngũ cung", bpm: 64 }, zen: { name: "🕯️ Suy ngẫm", bpm: 58 }
    };
    var BARS = { calm: 8, journey: 8, ngu: 8, zen: 8 };
    var NAMES = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 };
    function midi(n) { var m = /^([A-G])(#|b)?(-?\d)$/.exec(n); return 12 * (+m[3] + 1) + NAMES[m[1]] + (m[2] === "#" ? 1 : m[2] === "b" ? -1 : 0); }
    function hz(m) { return 440 * Math.pow(2, (m - 69) / 12); }
    function chord(root, kind) { var r = midi(root); return kind === "m" ? [r, r + 3, r + 7] : kind === "7" ? [r, r + 4, r + 7, r + 10] : [r, r + 4, r + 7]; }
    var KS = {};
    function ksBuf(ctx, m, dur, bright, decay) {
      dur = 1.8; var sr = ctx.sampleRate, key = m + "|" + bright + "|" + (decay || 0) + "|" + sr; if (KS[key]) return KS[key];
      var n = Math.round(sr * dur), b = ctx.createBuffer(1, n, sr), y = b.getChannelData(0), N = Math.max(2, Math.round(sr / hz(m))), seed = (m * 9301 + 49297) % 233280, i, prev = 0;
      for (i = 0; i < N; i++) { seed = (seed * 9301 + 49297) % 233280; var r = seed / 233280 * 2 - 1; prev = prev + (r - prev) * bright; y[i] = prev; }
      var d = decay || 0.996;
      for (i = N; i < n; i++) y[i] = d * 0.5 * (y[i - N] + y[i - N + 1]);
      var pk = 0; for (i = 0; i < Math.min(n, N * 4); i++) pk = Math.max(pk, Math.abs(y[i])); if (pk > 0) for (i = 0; i < n; i++) y[i] /= pk;
      KS[key] = b; return b;
    }
    var NOISE = null;
    function noise(ctx) { if (NOISE && NOISE.sampleRate === ctx.sampleRate) return NOISE; var n = ctx.sampleRate, b = ctx.createBuffer(1, n, n), y = b.getChannelData(0), s = 12345; for (var i = 0; i < n; i++) { s = (s * 1103515245 + 12345) & 0x7fffffff; y[i] = s / 0x3fffffff - 1; } NOISE = b; return b; }
    function pan(ctx, v) { if (ctx.createStereoPanner) { var p = ctx.createStereoPanner(); p.pan.value = v; return p; } return ctx.createGain(); }
    // ---- nhạc cụ ----
    function pluck(ctx, out, m, t, len, vol, opt) {
      opt = opt || {};
      var s = ctx.createBufferSource(); s.buffer = ksBuf(ctx, m, 1.8, opt.bright || 0.5, opt.decay);
      var g = ctx.createGain(); g.gain.setValueAtTime(vol, t); g.gain.setValueAtTime(vol, t + len); g.gain.exponentialRampToValueAtTime(0.0008, t + len + (opt.rel || 0.5));
      var f = ctx.createBiquadFilter(); f.type = "lowpass"; f.frequency.value = opt.lp || 5200;
      s.connect(f); f.connect(g); g.connect(out); s.start(t); s.stop(t + len + (opt.rel || 0.5) + 0.05);
    }
    function tone(ctx, out, m, t, len, vol, opt) {
      opt = opt || {};
      var g = ctx.createGain(), f = ctx.createBiquadFilter(); f.type = "lowpass"; f.frequency.value = opt.lp || 2400; f.Q.value = opt.q || 0.5;
      var a = opt.a || 0.02, r = opt.r || 0.15, types = opt.types || ["sawtooth"], det = opt.det || [0];
      g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(vol, t + a); g.gain.setValueAtTime(vol, t + Math.max(a, len)); g.gain.linearRampToValueAtTime(0, t + Math.max(a, len) + r);
      types.forEach(function (ty, i) {
        var o = ctx.createOscillator(); o.type = ty; o.frequency.value = hz(m); o.detune.value = det[i % det.length];
        if (opt.vib) { var l = ctx.createOscillator(), lg = ctx.createGain(); l.frequency.value = opt.vib; lg.gain.value = opt.vibD || 5; l.connect(lg); lg.connect(o.detune); l.start(t); l.stop(t + len + r + 0.05); }
        o.connect(f); o.start(t); o.stop(t + Math.max(a, len) + r + 0.05);
      });
      f.connect(g); g.connect(out);
    }
    function bell(ctx, out, m, t, vol) {
      [[1, 1], [2.76, 0.35], [5.4, 0.12]].forEach(function (p) {
        var o = ctx.createOscillator(), g = ctx.createGain(); o.type = "sine"; o.frequency.value = hz(m) * p[0];
        g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(vol * p[1], t + 0.008); g.gain.exponentialRampToValueAtTime(0.0005, t + 2.4 / p[0] + 0.3);
        o.connect(g); g.connect(out); o.start(t); o.stop(t + 2.8);
      });
    }
    function kick(ctx, out, t, vol) {
      var o = ctx.createOscillator(), g = ctx.createGain(); o.type = "sine"; o.frequency.setValueAtTime(130, t); o.frequency.exponentialRampToValueAtTime(42, t + 0.16);
      g.gain.setValueAtTime(vol, t); g.gain.exponentialRampToValueAtTime(0.001, t + 0.32); o.connect(g); g.connect(out); o.start(t); o.stop(t + 0.35);
    }
    function hat(ctx, out, t, vol, len, hp) {
      var s = ctx.createBufferSource(), f = ctx.createBiquadFilter(), g = ctx.createGain(); s.buffer = noise(ctx); f.type = "highpass"; f.frequency.value = hp || 7000;
      g.gain.setValueAtTime(vol, t); g.gain.exponentialRampToValueAtTime(0.001, t + (len || 0.05)); s.connect(f); f.connect(g); g.connect(out); s.start(t, Math.random() * 0.5); s.stop(t + (len || 0.05) + 0.02);
    }
    function drum(ctx, out, t, vol) {     // trống trầm kiểu điện ảnh
      var o = ctx.createOscillator(), g = ctx.createGain(); o.type = "sine"; o.frequency.setValueAtTime(90, t); o.frequency.exponentialRampToValueAtTime(48, t + 0.5);
      g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(vol, t + 0.01); g.gain.exponentialRampToValueAtTime(0.001, t + 1.2); o.connect(g); g.connect(out); o.start(t); o.stop(t + 1.25);
      hat(ctx, out, t, vol * 0.25, 0.25, 900);
    }
    function verbBus(ctx, dest, wet) {    // vang nhẹ (2 đường trễ có lọc)
      var inp = ctx.createGain(), dry = ctx.createGain(); dry.gain.value = 1; inp.connect(dry); dry.connect(dest);
      [[0.137, 0.32, -0.6], [0.229, 0.28, 0.6]].forEach(function (d) {
        var dl = ctx.createDelay(1), fb = ctx.createGain(), lp = ctx.createBiquadFilter(), wg = ctx.createGain(), p = pan(ctx, d[2]);
        dl.delayTime.value = d[0]; fb.gain.value = d[1]; lp.type = "lowpass"; lp.frequency.value = 2600; wg.gain.value = wet;
        inp.connect(dl); dl.connect(lp); lp.connect(fb); fb.connect(dl); lp.connect(wg); wg.connect(p); p.connect(dest);
      });
      return inp;
    }
    // ---- các bản nhạc: trả về độ dài một vòng (giây) ----
    var PROG_CALM = [["C4", ""], ["G3", ""], ["A3", "m"], ["F3", ""], ["C4", ""], ["E3", "m"], ["F3", ""], ["G3", ""]];
    function sCalm(ctx, out, t0) {
      var spb = 60 / 72, bar = spb * 4, bus = verbBus(ctx, out, 0.35), pad = pan(ctx, 0); pad.connect(bus);
      var mel = [76, 79, 81, 79, 76, 74, 72, 74, 76, 74, 72, 69, 72, 74, 76, 79];
      PROG_CALM.forEach(function (c, b) {
        var t = t0 + b * bar, ch = chord(c[0], c[1]);
        ch.forEach(function (m) { tone(ctx, pad, m, t, bar - 0.2, 0.035, { types: ["triangle", "sawtooth"], det: [-6, 7], lp: 900, a: 0.9, r: 1.2 }); });
        tone(ctx, bus, ch[0] - 12, t, bar - 0.3, 0.07, { types: ["sine"], a: 0.05, r: 0.8, lp: 600 });
        var arp = [ch[0], ch[1], ch[2], ch[0] + 12, ch[2], ch[1], ch[0] + 12, ch[2]];
        arp.forEach(function (m, k) { pluck(ctx, bus, m + 12, t + k * spb / 2, spb * 0.45, 0.06, { bright: 0.35, lp: 3000, rel: 0.9, decay: 0.997 }); });
        if (b % 2 === 0) bell(ctx, bus, mel[(b * 2) % mel.length], t + spb * 1.5, 0.05);
        if (b % 2 === 1) bell(ctx, bus, mel[(b * 2 + 5) % mel.length], t + spb * 2.5, 0.04);
      });
      return PROG_CALM.length * bar;
    }
    var PROG_UP = [["A3", "m"], ["F3", ""], ["C4", ""], ["G3", ""]];
    function sUpbeat(ctx, out, t0) {
      var spb = 60 / 112, bar = spb * 4, bus = verbBus(ctx, out, 0.18), L = pan(ctx, -0.35), R = pan(ctx, 0.35); L.connect(bus); R.connect(bus);
      for (var b = 0; b < 16; b++) {
        var c = PROG_UP[b % 4], ch = chord(c[0], c[1]), t = t0 + b * bar, pat = [0, 1, 2, 1, 3, 2, 1, 2];
        for (var k = 0; k < 8; k++) {
          var nt = [ch[0], ch[1], ch[2], ch[0] + 12][pat[k]] + 12;
          pluck(ctx, k % 2 ? R : L, nt, t + k * spb / 2, spb * 0.4, 0.07, { bright: 0.6, lp: 4200, rel: 0.35 });
          hat(ctx, out, t + k * spb / 2, k % 2 ? 0.022 : 0.012, 0.04);
        }
        for (var q = 0; q < 4; q++) {
          if (b >= 2 && q % 2 === 0) kick(ctx, out, t + q * spb, 0.32);
          if (b >= 2 && q % 2 === 1) hat(ctx, out, t + q * spb, 0.06, 0.12, 1800);
          tone(ctx, out, ch[0] - 12 + (q === 3 ? 7 : 0), t + q * spb, spb * 0.55, 0.11, { types: ["triangle"], lp: 700, a: 0.01, r: 0.08 });
        }
        if (b >= 8 && b % 2 === 0) [ch[2] + 12, ch[1] + 12, ch[0] + 24].forEach(function (m, k2) { pluck(ctx, bus, m, t + spb * (2 + k2 * 0.5), spb * 0.6, 0.05, { bright: 0.45, lp: 5000, rel: 0.8 }); });
      }
      return 16 * bar;
    }
    var PROG_J = [["D3", "m"], ["A#2", ""], ["F3", ""], ["C3", ""], ["D3", "m"], ["A#2", ""], ["G2", "m"], ["A2", ""]];
    function sJourney(ctx, out, t0) {
      var spb = 60 / 66, bar = spb * 4, bus = verbBus(ctx, out, 0.42), str = pan(ctx, 0); str.connect(bus);
      var motif = [74, 77, 76, 72, 74, 69, 72, 74];
      PROG_J.forEach(function (c, b) {
        var t = t0 + b * bar, ch = chord(c[0], c[1]);
        ch.concat([ch[0] + 12, ch[1] + 12]).forEach(function (m, k) { tone(ctx, str, m + 12, t, bar - 0.1, k < 3 ? 0.03 : 0.018, { types: ["sawtooth", "sawtooth"], det: [-9, 9], lp: 1300, a: 1.4, r: 1.6, vib: 5, vibD: 4 }); });
        tone(ctx, bus, ch[0] - 12, t, bar - 0.2, 0.09, { types: ["sine", "triangle"], a: 0.6, r: 1, lp: 400 });
        drum(ctx, out, t, 0.33); if (b % 2) drum(ctx, out, t + spb * 2, 0.22);
        if (b >= 2) tone(ctx, bus, motif[b % motif.length], t + spb, spb * 2.6, 0.045, { types: ["triangle", "sine"], det: [-3, 3], lp: 1800, a: 0.25, r: 0.9, vib: 5.5, vibD: 8 });
      });
      return PROG_J.length * bar;
    }
    // «Коробейники» — giai điệu dân ca Nga (phạm vi công cộng), đàn balalaika (gảy rung) + đàn bayan đệm
    var KOR = "E5:2 B4:1 C5:1 D5:2 C5:1 B4:1|A4:2 A4:1 C5:1 E5:2 D5:1 C5:1|B4:3 C5:1 D5:2 E5:2|C5:2 A4:2 A4:4|R:1 D5:2 F5:1 A5:2 G5:1 F5:1|E5:3 C5:1 E5:2 D5:1 C5:1|B4:2 B4:1 C5:1 D5:2 E5:2|C5:2 A4:2 A4:2 R:2";
    var KCH = [["E3", ""], ["A2", "m"], ["E3", ""], ["A2", "m"], ["D3", "m"], ["C3", ""], ["E3", ""], ["A2", "m"]];
    function sFolk(ctx, out, t0) {
      var spb = 60 / 104, e8 = spb / 2, bar = spb * 4, bus = verbBus(ctx, out, 0.22), bal = pan(ctx, 0.25), bay = pan(ctx, -0.25); bal.connect(bus); bay.connect(bus);
      var bars = KOR.split("|").map(function (b) { return b.trim().split(/\s+/).map(function (x) { var p = x.split(":"); return { n: p[0], d: +p[1] }; }); });
      for (var rep = 0; rep < 2; rep++) bars.forEach(function (notes, bi) {
        var tb = t0 + (rep * 8 + bi) * bar, pos = 0, c = KCH[bi], ch = chord(c[0], c[1]);
        notes.forEach(function (nt) {
          var t = tb + pos * e8, len = nt.d * e8; pos += nt.d; if (nt.n === "R") return;
          var m = midi(nt.n);
          if (rep === 0) {                                 // vòng 1: balalaika chính, rung khi nốt dài
            if (nt.d >= 2) { var nTr = Math.max(2, Math.round(len * 11)); for (var k = 0; k < nTr; k++) pluck(ctx, bal, m, t + k * len / nTr, len / nTr, 0.085 * (1 - k / nTr * 0.25), { bright: 0.75, lp: 5200, rel: 0.12 }); }
            else pluck(ctx, bal, m, t, len, 0.1, { bright: 0.75, lp: 5200, rel: 0.25 });
          } else {                                         // vòng 2: bayan hát giai điệu, balalaika bè dưới
            tone(ctx, bay, m, t, len * 0.92, 0.05, { types: ["sawtooth", "square"], det: [-7, 7], lp: 2300, a: 0.03, r: 0.07, vib: 5.5, vibD: 6 });
            pluck(ctx, bal, m - (nt.d >= 2 ? 12 : 0), t, len, 0.055, { bright: 0.7, lp: 4200, rel: 0.2 });
          }
        });
        for (var q = 0; q < 4; q++) {                      // "oom-pah": bass phách 1-3, hợp âm phách 2-4
          var tq = tb + q * spb;
          if (q % 2 === 0) tone(ctx, bay, ch[0] - 12 + (q === 2 ? 7 : 0), tq, spb * 0.42, 0.09, { types: ["sawtooth", "square"], det: [-5, 5], lp: 650, a: 0.01, r: 0.07 });
          else ch.forEach(function (m) { tone(ctx, bay, m + 12, tq, spb * 0.22, 0.03, { types: ["sawtooth", "square"], det: [-6, 6], lp: 1900, a: 0.01, r: 0.05 }); });
        }
      });
      return 16 * bar;
    }
    // 🎋 Ngũ cung — giai điệu tự soạn theo thang âm ngũ cung (Đô Rê Fa Son La): đàn tranh gảy có "nhấn" (luyến cao độ),
    // sáo trúc hát giai điệu, tiếng mõ gỗ điểm nhịp, nền trầm ngân dài. Không dựa trên bài hát có bản quyền nào.
    function pluckBend(ctx, out, m, t, len, vol, bend, opt) {
      opt = opt || {};
      var s = ctx.createBufferSource(); s.buffer = ksBuf(ctx, m, 1.8, opt.bright || 0.55, opt.decay || 0.9975);
      var g = ctx.createGain(); g.gain.setValueAtTime(vol, t); g.gain.setValueAtTime(vol, t + len); g.gain.exponentialRampToValueAtTime(0.0008, t + len + (opt.rel || 0.8));
      var f = ctx.createBiquadFilter(); f.type = "lowpass"; f.frequency.value = opt.lp || 4200;
      if (bend) { var r = s.playbackRate; r.setValueAtTime(1, t); r.setValueAtTime(1, t + 0.16); r.linearRampToValueAtTime(Math.pow(2, bend / 12), t + 0.3); r.linearRampToValueAtTime(1, t + 0.62); }
      s.connect(f); f.connect(g); g.connect(out); s.start(t); s.stop(t + len + (opt.rel || 0.8) + 0.05);
    }
    function woodblock(ctx, out, t, vol, hz0) {
      var o = ctx.createOscillator(), g = ctx.createGain(), f = ctx.createBiquadFilter(); o.type = "sine"; o.frequency.setValueAtTime(hz0 || 880, t); o.frequency.exponentialRampToValueAtTime((hz0 || 880) * 0.82, t + 0.06);
      f.type = "bandpass"; f.frequency.value = hz0 || 880; f.Q.value = 6;
      g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(vol, t + 0.002); g.gain.exponentialRampToValueAtTime(0.0005, t + 0.12);
      o.connect(f); f.connect(g); g.connect(out); o.start(t); o.stop(t + 0.14);
    }
    var NGU_MEL = "A4:2 G4:1 A4:1 C5:4|D5:2 C5:1 A4:1 G4:4|F4:2 G4:1 A4:1 G4:2 F4:2|D4:6 R:2|C5:2 D5:1 F5:1 D5:4|C5:2 A4:1 G4:1 A4:4|G4:2 F4:1 D4:1 F4:2 G4:2|C4:6 R:2";
    var NGU_BASS = ["C3", "G2", "F2", "D3", "A2", "F2", "G2", "C3"];
    function sNgu(ctx, out, t0) {
      var spb = 60 / 64, e8 = spb / 2, bar = spb * 4, bus = verbBus(ctx, out, 0.42), zl = pan(ctx, -0.3), fl = pan(ctx, 0.22); zl.connect(bus); fl.connect(bus);
      var bars = NGU_MEL.split("|").map(function (b) { return b.trim().split(/\s+/).map(function (x) { var p = x.split(":"); return { n: p[0], d: +p[1] }; }); });
      var PENT = [0, 2, 5, 7, 9];
      bars.forEach(function (notes, bi) {
        var tb = t0 + bi * bar, root = midi(NGU_BASS[bi]);
        tone(ctx, bus, root - 12, tb, bar - 0.2, 0.06, { types: ["sine"], a: 0.8, r: 1.4, lp: 420 });
        tone(ctx, bus, root - 5, tb, bar - 0.2, 0.025, { types: ["triangle"], a: 1.2, r: 1.6, lp: 600 });
        // đàn tranh: chuỗi gảy rải lên xuống trên thang ngũ cung, có nhấn ở nốt đầu phách
        var base = root + 12, arp = [0, 7, 12, 14, 17, 14, 12, 7];
        arp.forEach(function (iv, k) {
          var m = base + iv; var pc = ((m - 60) % 12 + 12) % 12; if (PENT.indexOf(pc) < 0) m += 2;
          pluckBend(ctx, zl, m, tb + k * e8, e8 * 0.9, k % 4 === 0 ? 0.075 : 0.05, (k === 0 && bi % 2 === 1) ? 2 : 0, { bright: 0.6, rel: 1.1 });
        });
        // sáo: giai điệu (vòng 2 của bản lặp mới thổi để mở đầu nhẹ nhàng)
        var pos = 0;
        notes.forEach(function (nt) {
          var t = tb + pos * e8, len = nt.d * e8; pos += nt.d; if (nt.n === "R") return;
          var m = midi(nt.n) + 12;
          tone(ctx, fl, m, t, len * 0.94, 0.045, { types: ["sine", "triangle"], det: [0, 4], lp: 3200, a: 0.09, r: 0.28, vib: 5.2, vibD: nt.d >= 4 ? 14 : 6 });
          hat(ctx, fl, t, 0.006, 0.09, 2200);
        });
        woodblock(ctx, out, tb, 0.07, 940); woodblock(ctx, out, tb + spb * 2, 0.045, 760);
        if (bi % 4 === 3) bell(ctx, bus, 84, tb + spb * 3, 0.035);
      });
      return bars.length * bar;
    }
    // 🕯️ Suy ngẫm — tiếng "piano" mềm thưa nốt trên nền dây êm, vang dài; hợp video chậm, chiêm nghiệm
    var PROG_Z = [["D3", "m"], ["A#2", ""], ["F3", ""], ["C3", ""], ["D3", "m"], ["G2", "m"], ["A#2", ""], ["A2", ""]];
    function sZen(ctx, out, t0) {
      var spb = 60 / 58, bar = spb * 4, bus = verbBus(ctx, out, 0.55), pno = pan(ctx, 0.12), pad = pan(ctx, -0.1); pno.connect(bus); pad.connect(bus);
      var top = [74, 72, 69, 67, 69, 70, 72, 69];
      PROG_Z.forEach(function (c, b) {
        var t = t0 + b * bar, ch = chord(c[0], c[1]);
        ch.forEach(function (m) { tone(ctx, pad, m + 12, t, bar - 0.1, 0.022, { types: ["sawtooth", "triangle"], det: [-7, 7], lp: 780, a: 1.6, r: 1.8 }); });
        tone(ctx, bus, ch[0] - 12, t, bar - 0.2, 0.05, { types: ["sine"], a: 0.4, r: 1.2, lp: 380 });
        [ch[0] + 12, ch[1] + 12, ch[2] + 12].forEach(function (m, k) {
          pluck(ctx, pno, m, t + k * spb * 0.5, spb * 1.6, 0.05, { bright: 0.28, lp: 2400, rel: 2.2, decay: 0.9985 });
          tone(ctx, pno, m, t + k * spb * 0.5, 0.05, 0.018, { types: ["sine"], a: 0.004, r: 1.4, lp: 3000 });
        });
        pluck(ctx, pno, top[b], t + spb * 2.5, spb * 1.4, 0.06, { bright: 0.3, lp: 2600, rel: 2.4, decay: 0.9985 });
        if (b % 2 === 1) pluck(ctx, pno, top[(b + 3) % top.length] + 12, t + spb * 3.25, spb, 0.035, { bright: 0.3, lp: 3000, rel: 2.6, decay: 0.9985 });
      });
      return PROG_Z.length * bar;
    }
    var FN = { calm: sCalm, upbeat: sUpbeat, journey: sJourney, folk: sFolk, ngu: sNgu, zen: sZen };
    var LOOPS = {};
    async function loop(preset, sr) {
      var k = preset + "@" + sr; if (LOOPS[k]) return LOOPS[k];
      var spb = 60 / PRE[preset].bpm, est = (BARS[preset] || 16) * 4 * spb, tail = 3.5;
      var ctx = new OfflineAudioContext(2, Math.ceil((est + tail) * sr), sr), g = ctx.createGain(); g.gain.value = 0.9; g.connect(ctx.destination);
      var len = FN[preset](ctx, g, 0), buf = await ctx.startRendering();
      KS = {};
      LOOPS[k] = { buf: buf, len: len }; return LOOPS[k];
    }
    // lát kín thời lượng: chồng vòng nhạc (vòng sau đè phần ngân của vòng trước) hoặc nối nhạc của anh có đoạn chuyển mượt
    function tile(src, loopLen, total, sr, xfade) {
      var n = Math.ceil(total * sr), out = [new Float32Array(n), new Float32Array(n)], L = Math.round(loopLen * sr), m = src.length, xf = Math.round((xfade || 0) * sr);
      for (var c = 0; c < 2; c++) {
        var s = src.getChannelData(Math.min(c, src.numberOfChannels - 1)), o = out[c];
        for (var start = 0, k = 0; start < n; start += L - xf, k++) {
          for (var i = 0; i < m && start + i < n; i++) {
            var w = 1; if (xf) { if (k > 0 && i < xf) w = i / xf; if (i > L - xf && i < L) w = Math.min(w, (L - i) / xf); else if (i >= L) w = 0; }
            o[start + i] += s[i] * w;
          }
          if (L - xf <= 0) break;
        }
      }
      return out;
    }
    function norm(ch, target) {      // chuẩn hoá độ to (RMS) để mọi bản nhạc/nhạc của anh nghe ngang nhau
      var sum = 0, n = 0, pk = 0, i, c; for (c = 0; c < ch.length; c++) for (i = 0; i < ch[c].length; i += 3) { var v = ch[c][i]; sum += v * v; n++; if (v > pk) pk = v; else if (-v > pk) pk = -v; }
      var rms = Math.sqrt(sum / Math.max(1, n)), g = rms > 1e-5 ? Math.min(target / rms, 0.98 / Math.max(pk, 1e-5)) : 1;
      for (c = 0; c < ch.length; c++) { var a = ch[c]; for (i = 0; i < a.length; i++) a[i] *= g; }
      return ch;
    }
    async function track(O, total, sr, userBuf) {
      if (O.music === "file" && userBuf) {
        var mb = userBuf; if (mb.sampleRate !== sr) mb = await resample(mb, sr);
        if (mb.duration >= total) { var n2 = Math.ceil(total * sr); return norm([mb.getChannelData(0).slice(0, n2), (mb.numberOfChannels > 1 ? mb.getChannelData(1) : mb.getChannelData(0)).slice(0, n2)], 0.12); }
        return norm(tile(mb, mb.duration, total, sr, Math.min(2, mb.duration / 4)), 0.12);
      }
      if (!FN[O.music]) return null;
      var lp = await loop(O.music, sr);
      return norm(tile(lp.buf, lp.len, total, sr, 0), 0.12);
    }
    async function resample(buf, sr) {
      var ctx = new OfflineAudioContext(Math.min(2, buf.numberOfChannels), Math.ceil(buf.duration * sr), sr), s = ctx.createBufferSource(); s.buffer = buf; s.connect(ctx.destination); s.start(0);
      return await ctx.startRendering();
    }
    async function decodeFile(file) {
      var ab = await file.arrayBuffer(), ctx = new OfflineAudioContext(2, 48000, 48000);
      return await new Promise(function (res, rej) { var p = ctx.decodeAudioData(ab, res, rej); if (p && p.then) p.then(res, rej); });
    }
    return { PRE: PRE, track: track, decodeFile: decodeFile, loop: loop };
  })();

  // khoảng thời gian có lời đọc (để giảm nhỏ nhạc), gộp các khoảng gần nhau cho khỏi "nhấp nhô"
  function voiceSpans(V) {
    var sp = [];
    V.scenes.forEach(function (sc) { if (!sc.ap) return; sc.sentT.forEach(function (x) { sp.push([sc.t0 + x.t0, sc.t0 + x.t1]); }); });
    sp.sort(function (a, b) { return a[0] - b[0]; });
    var out = []; sp.forEach(function (s) { var l = out[out.length - 1]; if (l && s[0] - l[1] < 1.4) l[1] = Math.max(l[1], s[1]); else out.push([s[0], s[1]]); });
    return out;
  }
  /* trộn lời đọc + nhạc thành một dải âm thanh stereo 48 kHz dài đúng bằng video */
  async function mixAudio(V, O, userMusic, ui) {
    var sr = 48000, total = V.total, len = Math.ceil((total + 0.05) * sr), hasV = V.scenes.some(function (sc) { return sc.ap; });
    var mus = O.music && O.music !== "off" ? await MUSIC.track(O, total + 0.1, sr, userMusic) : null;
    if (!hasV && !mus) return null;
    if (ui) ui.phase("Đang trộn lời đọc với nhạc nền…", 0.99);
    var ctx = new OfflineAudioContext(2, len, sr), comp = ctx.createDynamicsCompressor();
    comp.threshold.value = -9; comp.knee.value = 8; comp.ratio.value = 3.5; comp.attack.value = 0.004; comp.release.value = 0.22; comp.connect(ctx.destination);
    var vg = ctx.createGain(); vg.gain.value = 1; vg.connect(comp);
    V.scenes.forEach(function (sc) {
      if (!sc.ap) return; var base = sc.t0 + sc.lead;
      sc.ap.clips.forEach(function (c) {
        if (!c.pcm.length) return;
        var b = ctx.createBuffer(1, c.pcm.length, c.sr); b.getChannelData(0).set(c.pcm);
        var s = ctx.createBufferSource(); s.buffer = b; s.connect(vg); s.start(base + c.t);
      });
    });
    if (mus) {
      var mb = ctx.createBuffer(2, len, sr); mb.getChannelData(0).set(mus[0].subarray(0, len)); mb.getChannelData(1).set(mus[1].subarray(0, len));
      var ms = ctx.createBufferSource(), mg = ctx.createGain(), lvl = clamp(+O.musicVol || 0, 0, 1) * (hasV ? 0.62 : 0.9), duck = hasV ? 0.24 : 1;
      ms.buffer = mb; ms.connect(mg); mg.connect(comp);
      var g = mg.gain, endLvl = lvl, fadeAt = Math.max(0.2, total - 3.5);
      g.setValueAtTime(0, 0); g.linearRampToValueAtTime(lvl, Math.min(1.6, total / 3));
      voiceSpans(V).forEach(function (s) {
        var a = Math.max(1.7, s[0] - 0.3), b = s[1] + 0.25; if (a >= fadeAt - 0.4) { if (a < total) { g.setValueAtTime(lvl, Math.max(1.7, Math.min(a, fadeAt - 0.4))); g.linearRampToValueAtTime(lvl * duck, Math.min(a, fadeAt - 0.4) + 0.3); endLvl = lvl * duck; } return; }
        g.setValueAtTime(lvl, a); g.linearRampToValueAtTime(lvl * duck, a + 0.3);
        if (b + 0.6 >= fadeAt) { endLvl = lvl * duck; return; }
        g.setValueAtTime(lvl * duck, b); g.linearRampToValueAtTime(lvl, b + 0.6);
      });
      g.setValueAtTime(endLvl, fadeAt); g.linearRampToValueAtTime(0, total);
      ms.start(0);
    }
    return await ctx.startRendering();
  }
  async function pickAudioCodec() {
    if (!global.AudioEncoder) return null;
    var c = [["mp4a.40.2", "aac"], ["opus", "opus"]];
    for (var i = 0; i < c.length; i++) {
      var cfg = { codec: c[i][0], sampleRate: 48000, numberOfChannels: 2, bitrate: 160000 };
      try { var r = await AudioEncoder.isConfigSupported(cfg); if (r && r.supported) return { cfg: cfg, mux: c[i][1] }; } catch (e) { }
    }
    return null;
  }
  async function encodeAudio(buf, ac, muxer, onProg) {
    var err = null, enc = new AudioEncoder({ output: function (ch, meta) { muxer.addAudioChunk(ch, meta); }, error: function (e) { err = e; } });
    enc.configure(ac.cfg);
    var L = buf.getChannelData(0), R = buf.numberOfChannels > 1 ? buf.getChannelData(1) : L, n = L.length, step = 4800, sr = buf.sampleRate;
    for (var i = 0; i < n; i += step) {
      if (err) throw err;
      var k = Math.min(step, n - i), d = new Float32Array(k * 2); d.set(L.subarray(i, i + k), 0); d.set(R.subarray(i, i + k), k);
      var ad = new AudioData({ format: "f32-planar", sampleRate: sr, numberOfFrames: k, numberOfChannels: 2, timestamp: Math.round(i / sr * 1e6), data: d });
      enc.encode(ad); ad.close();
      if (enc.encodeQueueSize > 24) await sleep(2);
      if (onProg && (i / step) % 50 === 0) onProg(i / n);
    }
    await enc.flush(); enc.close(); if (err) throw err;
  }
  /* phát dải âm thanh đã trộn đồng bộ với hình (xem thử / trình chiếu) */
  function AudioPlayer() {
    var ac = null, src = null, gain = null, buf = null, startAt = 0, off = 0, on = false;
    function ctx() { if (!ac) { var C2 = global.AudioContext || global.webkitAudioContext; ac = new C2(); gain = ac.createGain(); gain.connect(ac.destination); } return ac; }
    return {
      set: function (b) { this.stop(); buf = b; },
      has: function () { return !!buf; },
      play: function (t) { if (!buf) return; this.stop(); var c = ctx(); if (c.state === "suspended") c.resume(); src = c.createBufferSource(); src.buffer = buf; src.connect(gain); off = Math.max(0, t); startAt = c.currentTime - off; src.start(0, Math.min(off, buf.duration)); on = true; },
      stop: function () { if (src) { try { src.stop(); } catch (e) { } src.disconnect(); src = null; } if (on && ac) off = ac.currentTime - startAt; on = false; },
      time: function () { return on && ac ? ac.currentTime - startAt : off; },
      playing: function () { return on; },
      mute: function (m) { ctx(); gain.gain.value = m ? 0 : 1; },
      close: function () { this.stop(); if (ac) { try { ac.close(); } catch (e) { } ac = null; } }
    };
  }

  /* ---------------- 11. xuất video (hình + tiếng) ---------------- */
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
  async function exportVideo(V, ui, audio) {
    var W = V.W, H = V.H, fps = 30, nFrames = Math.ceil(V.total * fps), cancelled = false;
    ui.onCancel(function () { cancelled = true; });
    var canvas = document.createElement("canvas"); canvas.width = W; canvas.height = H;
    var ctx = canvas.getContext("2d", { alpha: false });
    var bitrate = Math.round(W * H * fps * (V.O.res === 1080 ? 0.085 : 0.095));
    ui.phase("Chuẩn bị bộ mã hoá…", 0);
    var enc = await pickEncoder(W, H, fps, bitrate), ac = audio ? await pickAudioCodec() : null;
    if (V.O.qr && V.O.qrUrl) { await ensureQR(); qrCanvas(V.O.qrUrl); }
    // V.preload / V.ensure / V.render: cho phép mô-đun khác (vd. video giải mã tác phẩm) dùng chung bộ xuất video này
    var info = await (V.preload ? V.preload(function (d, n, label) { ui.phase((label || "Tải ảnh: ") + d + "/" + n, n ? d / n : 0); }, function () { return cancelled; })
      : preloadAll(V, function (kind, d, n) {
        ui.phase(kind === "photo" ? "Tải ảnh các điểm: " + d + "/" + n : "Tải ô bản đồ: " + d + "/" + n, n ? d / n : 0);
      }, function () { return cancelled; })) || {};
    var draw = V.render || renderFrame;
    if (cancelled) throw new Error("cancel");
    if (enc) {
      if (!global.Mp4Muxer) await loadScript(BASE + "vendor/mp4-muxer.min.js");
      var target = new Mp4Muxer.ArrayBufferTarget();
      var mo = { target: target, video: { codec: enc.mux, width: W, height: H, frameRate: fps }, fastStart: "in-memory", firstTimestampBehavior: "offset" };
      if (audio && ac) mo.audio = { codec: ac.mux, numberOfChannels: 2, sampleRate: audio.sampleRate };
      var muxer = new Mp4Muxer.Muxer(mo);
      if (audio && ac) { ui.phase("Đang mã hoá âm thanh (" + (ac.mux === "aac" ? "AAC" : "Opus") + ")…", 0); await encodeAudio(audio, ac, muxer); }
      var encErr = null;
      var encoder = new VideoEncoder({ output: function (chunk, meta) { muxer.addVideoChunk(chunk, meta); }, error: function (e) { encErr = e; } });
      encoder.configure(enc.cfg);
      var t0 = Date.now();
      for (var f = 0; f < nFrames; f++) {
        if (cancelled) { try { encoder.close(); } catch (e) { } throw new Error("cancel"); }
        if (encErr) throw encErr;
        var t = f / fps;
        if (V.ensure) await V.ensure(t); else await ensureFrame(V, t);
        draw(ctx, V, t, t);
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
      return { blob: new Blob([target.buffer], { type: "video/mp4" }), ext: "mp4", codec: enc.cfg.codec + (audio && ac ? " + " + ac.cfg.codec : ""), info: info, audio: !!(audio && ac), noAudioCodec: !!(audio && !ac) };
    }
    // dự phòng: MediaRecorder (ghi theo thời gian thực, kèm tiếng nếu có)
    if (!global.MediaRecorder || !canvas.captureStream) throw new Error("Trình duyệt này không hỗ trợ xuất video. Hãy dùng Chrome hoặc Edge bản mới.");
    var types = audio ? ["video/mp4;codecs=avc1,mp4a.40.2", "video/mp4", "video/webm;codecs=vp9,opus", "video/webm;codecs=vp8,opus", "video/webm"] : ["video/mp4;codecs=avc1", "video/mp4", "video/webm;codecs=vp9", "video/webm;codecs=vp8", "video/webm"], mt = "";
    for (var k = 0; k < types.length; k++) if (MediaRecorder.isTypeSupported(types[k])) { mt = types[k]; break; }
    var stream = canvas.captureStream(fps), actx = null, asrc = null;
    if (audio) {
      var AC = global.AudioContext || global.webkitAudioContext; actx = new AC({ sampleRate: audio.sampleRate });
      var dest = actx.createMediaStreamDestination(); asrc = actx.createBufferSource(); asrc.buffer = audio; asrc.connect(dest);
      dest.stream.getAudioTracks().forEach(function (tr) { stream.addTrack(tr); });
    }
    var rec = new MediaRecorder(stream, mt ? { mimeType: mt, videoBitsPerSecond: bitrate } : { videoBitsPerSecond: bitrate }), chunks = [];
    rec.ondataavailable = function (e) { if (e.data && e.data.size) chunks.push(e.data); };
    var stopped = new Promise(function (r) { rec.onstop = r; });
    rec.start(1000);
    if (asrc) { if (actx.state === "suspended") await actx.resume(); asrc.start(); }
    var start = performance.now();
    await new Promise(function (res) {
      function tick() {
        if (cancelled) { rec.stop(); return res(); }
        var t = (performance.now() - start) / 1000;
        if (t >= V.total) { draw(ctx, V, V.total - 0.001, t); rec.stop(); return res(); }
        draw(ctx, V, t, t); ui.phase("Đang ghi video (thời gian thực): " + Math.round(t / V.total * 100) + "%", t / V.total);
        requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    });
    await stopped; if (actx) { try { actx.close(); } catch (e) { } }
    if (cancelled) throw new Error("cancel");
    var type = (rec.mimeType || mt || "video/webm").split(";")[0];
    return { blob: new Blob(chunks, { type: type }), ext: /mp4/.test(type) ? "mp4" : "webm", codec: rec.mimeType || mt, info: info, audio: !!audio };
  }
  /* phụ đề .srt (YouTube/Facebook đọc được), mục lục chương cho YouTube, ảnh bìa */
  function srtTime(t) { t = Math.max(0, t); var ms = Math.round(t * 1000), h = Math.floor(ms / 3600000), m = Math.floor(ms / 60000) % 60, s = Math.floor(ms / 1000) % 60, r = ms % 1000;
    return (h < 10 ? "0" : "") + h + ":" + (m < 10 ? "0" : "") + m + ":" + (s < 10 ? "0" : "") + s + "," + ("00" + r).slice(-3); }
  function makeSRT(V) {
    var out = [], n = 0, cv = document.createElement("canvas").getContext("2d"); cv.font = "16px sans-serif";
    V.scenes.forEach(function (sc) {
      (sc.narr || []).forEach(function (x, i) {
        var st = sc.sentT && sc.sentT[i]; if (!st || !x.c) return;
        var lines = wrap(cv, x.c, 380, 0), body = [];
        for (var k = 0; k < lines.length; k += 2) body.push(lines.slice(k, k + 2).join("\n"));
        var a = sc.t0 + st.t0, b = sc.t0 + st.t1 + 0.25, step = (b - a) / body.length;
        body.forEach(function (bt, j) { n++; out.push(n + "\n" + srtTime(a + j * step) + " --> " + srtTime(a + (j + 1) * step) + "\n" + bt); });
      });
    });
    return out.join("\n\n") + "\n";
  }
  function makeChapters(V) {
    var L = V.O.lang, out = [], last = -99, pendDay = null;
    V.scenes.forEach(function (sc) {
      var label = null, t = sc.t0;
      if (sc.type === "intro") { label = L === "vi" ? "Mở đầu" : L === "en" ? "Intro" : "Начало"; t = 0; }
      else if (sc.type === "day") { pendDay = (L === "vi" ? "Ngày " : L === "en" ? "Day " : "День ") + sc.day.day; return; }
      else if (sc.type === "travel") label = (pendDay ? pendDay + " · " : "") + sc.stop.num + ". " + sc.stop.name;
      else if (sc.type === "outro") label = L === "vi" ? "Tổng kết" : L === "en" ? "Summary" : "Итоги";
      if (!label) return;
      if (out.length && t - last < 10) return;
      pendDay = null; out.push(fmtClock(t) + " " + label); last = t;
    });
    return out.join("\n");
  }
  async function coverBlob(V) {
    var c = document.createElement("canvas"); c.width = V.W; c.height = V.H; var x = c.getContext("2d", { alpha: false }), sc = V.scenes[0];
    var t = Math.min(sc.dur - 0.7, (sc.previewEnd || 3) + 1.4);
    await ensureFrame(V, t); V.cover = true; try { renderFrame(x, V, t, t); } finally { V.cover = false; }
    return await new Promise(function (r) { c.toBlob(r, "image/jpeg", 0.9); });
  }

  /* ---------------- 12. giọng có sẵn của máy (trình chiếu) — mỗi ngôn ngữ một giọng: Việt + Nga (+ Anh) ---------------- */
  var SysVoice = {
    list: function () { var sy = global.speechSynthesis; try { return sy ? (sy.getVoices() || []) : []; } catch (e) { return []; } },
    ofLang: function (lang) { var re = new RegExp("^" + lang, "i"); return this.list().filter(function (v) { return re.test(String(v.lang || "").replace("_", "-")); }); },
    score: function (v) { var n = v.name || ""; return (/natural|neural|online/i.test(n) ? 40 : 0) + (/google/i.test(n) ? 20 : 0) + (/microsoft/i.test(n) ? 10 : 0) + (v.localService ? 0 : 3); },
    // đoán giọng nam/nữ theo tên (Microsoft/Google/Apple) để giọng Nga cùng giới với giọng Việt
    sex: function (v) {
      var n = String(v && v.name || "").toLowerCase();
      if (/\bmale\b/.test(n)) return "m";
      if (/\bfemale\b/.test(n)) return "f";
      if (/\b(an|namminh|pavel|dmitry|dmitri|maxim|yuri|yury|david|mark|guy|ryan|christopher|eric|andrew|brian|roger|steffan|george|james|thomas|daniel|fred|ralph|aaron|arthur|gordon|oliver|tom|evan|nathan|reed|eddy|rocko)\b/.test(n)) return "m";
      if (/\b(hoaimy|linh|irina|svetlana|dariya|ekaterina|milena|katya|anna|zira|aria|jenny|michelle|sonia|libby|hazel|susan|samantha|victoria|karen|moira|tessa|fiona|catherine|emma|ava|allison|natasha|elena|joanna|kendra|kimberly|salli|ivy|nicole|amy|emily|olivia|sara|natalie|clara)\b/.test(n) || /^google\b/.test(n)) return "f";
      return "";
    },
    pick: function (lang, pref, like) {
      var c = this.ofLang(lang); if (!c.length) return null;
      if (pref) { var p = c.filter(function (v) { return v.name === pref; })[0]; if (p) return p; }
      var self = this, g = like ? self.sex(like) : "";
      function sc(v) { return self.score(v) + (g && self.sex(v) === g ? 25 : 0); }
      return c.slice().sort(function (a, b) { return sc(b) - sc(a); })[0];
    },
    key: function (l) { return "sys" + l.charAt(0).toUpperCase() + l.slice(1); },
    main: function (O) { return this.pick(O.lang, O[this.key(O.lang)]); },
    // đọc lần lượt các đoạn; đoạn tiếng Nga dùng giọng Nga (máy không có giọng Nga thì đọc cách viết La-tinh bằng giọng Việt như cũ)
    speak: function (segs, O, cb) {
      var sy = global.speechSynthesis, self = this, i = 0, alive = true;
      if (!sy || !segs || !segs.length) { cb && cb(); return { stop: function () { } }; }
      var parts = [], vm = self.main(O);
      segs.forEach(function (g) {
        var v = g.l === O.lang ? vm : self.pick(g.l, O[self.key(g.l)], vm), t = g.t, l = g.l;
        if (!v && l === "ru") { if (!g.o) return; t = g.o; l = O.lang; v = vm; }
        (t.length > 220 ? (t.match(/[^,;:]+[,;:]?\s*/g) || [t]) : [t]).forEach(function (x) { if (x.trim()) parts.push({ t: x.trim(), v: v, l: l }); });
      });
      (function next() {
        if (!alive) return;
        if (i >= parts.length) { cb && cb(); return; }
        var p = parts[i++], u = new SpeechSynthesisUtterance(p.t);
        u.lang = p.v ? p.v.lang : (p.l === "en" ? "en-US" : p.l === "ru" ? "ru-RU" : "vi-VN"); if (p.v) u.voice = p.v; u.rate = clamp(+O.rate || 1, 0.6, 1.6);
        var done = false; function fin() { if (done) return; done = true; clearTimeout(to); next(); }
        var to = setTimeout(fin, 2500 + p.t.length * 140);
        u.onend = fin; u.onerror = fin; sy.speak(u);
      })();
      return { stop: function () { alive = false; try { sy.cancel(); } catch (e) { } } };
    },
    stop: function () { try { global.speechSynthesis && global.speechSynthesis.cancel(); } catch (e) { } try { var RT = global.RT; if (RT && RT.TTS) RT.TTS.stop(); } catch (e) { } }
  };

  /* ---------------- 13. giao diện ---------------- */
  var CSS = ".tv-ov{position:fixed;inset:0;z-index:5000;background:rgba(6,12,22,.86);display:flex;align-items:stretch;justify-content:center;font-family:" + FONT.replace(/"/g, "'") + ";color:#1e2733}" +
    ".tv-box{background:#f7f4ec;width:min(1220px,100%);max-height:100%;overflow:auto;display:flex;flex-direction:column;border-radius:0}" +
    "@media(min-width:900px){.tv-ov{padding:18px}.tv-box{border-radius:16px}}" +
    ".tv-top{display:flex;align-items:center;gap:10px;background:linear-gradient(135deg,#152c4e,#0f2138);color:#fff;padding:12px 16px;position:sticky;top:0;z-index:2}" +
    ".tv-top h2{margin:0;font-size:17px;flex:1}.tv-x{border:1px solid rgba(255,255,255,.35);background:rgba(255,255,255,.1);color:#fff;border-radius:9px;padding:7px 12px;font-weight:800;cursor:pointer;font-size:14px}" +
    ".tv-main{display:grid;grid-template-columns:1fr;gap:14px;padding:14px}@media(min-width:900px){.tv-main{grid-template-columns:minmax(0,1.5fr) minmax(320px,1fr)}}" +
    ".tv-prev{background:#0c1b30;border-radius:12px;overflow:hidden;display:flex;align-items:center;justify-content:center}" +
    ".tv-prev canvas{display:block;max-width:100%;max-height:60vh;width:auto;height:auto}" +
    ".tv-ctl{display:flex;align-items:center;gap:8px;margin-top:8px;flex-wrap:wrap}.tv-ctl input[type=range]{flex:1;min-width:140px}" +
    ".tv-b{border:1px solid #d9d2bd;background:#fff;color:#152c4e;border-radius:10px;padding:8px 12px;font-weight:800;cursor:pointer;font-size:13.5px;min-height:40px;font-family:inherit;text-decoration:none;display:inline-flex;align-items:center;gap:4px}" +
    ".tv-b.gold{background:#c8a24b;border-color:#c8a24b;color:#1a1305}.tv-b.navy{background:#152c4e;border-color:#152c4e;color:#fff}.tv-b:disabled{opacity:.5;cursor:default}" +
    ".tv-lbl{font-size:12.5px;color:#5c6773}.tv-set{display:flex;flex-direction:column;gap:11px}" +
    ".tv-f{display:flex;flex-direction:column;gap:6px}.tv-f>b{font-size:12.5px;color:#152c4e}" +
    ".tv-sub{background:#fff;border:1px solid #e7e3d6;border-radius:12px;padding:10px}" +
    ".tv-f input[type=text]{border:1px solid #d9d2bd;border-radius:9px;padding:9px 10px;font-size:14px;font-family:inherit}" +
    ".tv-f select{border:1px solid #d9d2bd;border-radius:9px;padding:7px 8px;font-size:13px;font-family:inherit;background:#fff;max-width:100%;min-height:36px}" +
    ".tv-seg{display:flex;flex-wrap:wrap;gap:6px}.tv-seg button{border:1px solid #d9d2bd;background:#fff;border-radius:999px;padding:6px 11px;font-size:12.5px;font-weight:700;color:#152c4e;cursor:pointer;min-height:34px;font-family:inherit}" +
    ".tv-seg button.on{background:#152c4e;border-color:#152c4e;color:#fff}.tv-chk{display:flex;flex-wrap:wrap;gap:6px 12px;font-size:13px}.tv-chk label{display:flex;gap:5px;align-items:center;cursor:pointer}" +
    ".tv-row{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:13px}.tv-row input[type=range]{flex:1;min-width:120px}.tv-row label{display:flex;flex-direction:column;gap:3px;flex:1 1 180px;font-size:12px;color:#5c6773}" +
    ".tv-go{display:flex;flex-direction:column;gap:8px;margin-top:4px}.tv-go .tv-b{min-height:46px;font-size:14.5px;justify-content:center}" +
    ".tv-prog{background:#fff;border:1px solid #e7e3d6;border-radius:12px;padding:12px;display:none;margin-top:8px}.tv-bar{height:10px;background:#efeadd;border-radius:6px;overflow:hidden;margin:8px 0}.tv-bar i{display:block;height:100%;width:0;background:#c8a24b;transition:width .2s}" +
    ".tv-res{display:none;background:#fff;border:1px solid #e7e3d6;border-radius:12px;padding:12px;margin-top:8px}.tv-res video{width:100%;max-height:50vh;background:#000;border-radius:8px;margin-top:6px}" +
    ".tv-res textarea{width:100%;min-height:120px;font-size:12.5px;border:1px solid #d9d2bd;border-radius:8px;padding:8px;box-sizing:border-box;margin-top:6px}" +
    ".tv-note{font-size:12px;color:#5c6773;line-height:1.5}.tv-hide{display:none!important}" +
    ".tv-show{position:fixed;inset:0;z-index:6000;background:#000;display:flex;align-items:center;justify-content:center}" +
    ".tv-show canvas{max-width:100vw;max-height:100vh;width:auto;height:auto}" +
    ".tv-sctl{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);display:flex;gap:8px;align-items:center;background:rgba(15,33,56,.88);padding:8px 10px;border-radius:14px;transition:opacity .3s;color:#fff;font-size:13px;z-index:2}" +
    ".tv-sctl button{border:1px solid rgba(255,255,255,.3);background:rgba(255,255,255,.08);color:#fff;border-radius:10px;min-width:44px;min-height:40px;font-size:16px;cursor:pointer}" +
    ".tv-sctl.hide{opacity:0}.tv-sctl .tv-sl{max-width:38vw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;padding:0 6px}";

  function loadOpts() {
    var o = {}; try { o = JSON.parse(localStorage.getItem("tv_opts") || "{}") || {}; } catch (e) { }
    if (typeof o.voice === "boolean") o.voice = o.voice ? "ai" : "off";       // bản 1: voice = true/false
    if (o.music === "file") o.music = DEF.music;                               // nhạc của anh không lưu được qua phiên
    var r = {}; for (var k in DEF) r[k] = (o[k] != null ? o[k] : DEF[k]); return r;
  }
  function saveOpts(O) { try { var c = {}; for (var k in O) if (k !== "title") c[k] = O[k]; localStorage.setItem("tv_opts", JSON.stringify(c)); } catch (e) { } }
  function slug(s) { return String(s || "video").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/đ/g, "d").replace(/Đ/g, "D").replace(/[^a-zA-Z0-9]+/g, "-").replace(/^-+|-+$/g, "").toLowerCase().slice(0, 60) || "video-chuyen-di"; }
  function sceneLabel(sc, V) {
    var T = V.T;
    if (sc.type === "intro") return "🎬 Mở đầu";
    if (sc.type === "day") return "📅 " + T.day + " " + sc.day.day;
    if (sc.type === "travel") return "➜ " + sc.stop.num + ". " + sc.stop.name;
    if (sc.type === "stop") return "📍 " + sc.stop.num + ". " + sc.stop.name;
    return "🏁 Tổng kết";
  }
  function narrLangs(NR) { var o = {}; for (var k in NR) NR[k].forEach(function (s) { s.segs.forEach(function (g) { o[g.l] = 1; }); }); return Object.keys(o); }
  function dl(blob, name) { var a = document.createElement("a"), u = URL.createObjectURL(blob); a.href = u; a.download = name; document.body.appendChild(a); a.click(); setTimeout(function () { a.remove(); URL.revokeObjectURL(u); }, 4000); }

  function open(data) {
    if (!data || !data.stops || !data.stops.length) { alert("Lịch trình đang trống — hãy thêm điểm vào tour trước."); return; }
    if (!document.getElementById("tv-css")) { var st = document.createElement("style"); st.id = "tv-css"; st.textContent = CSS; document.head.appendChild(st); }
    var O = loadOpts(); O.title = "";
    var userMusic = null, userMusicName = "", AUD = { nk: null, AP: null, mk: null, mix: null }, player = AudioPlayer(), busy = false;
    var ov = document.createElement("div"); ov.className = "tv-ov";
    function seg3(k, label, opts, cls) { return '<div class="tv-f' + (cls ? " " + cls : "") + '"><b>' + label + '</b><div class="tv-seg" data-k="' + k + '">' + opts.map(function (o) { return '<button data-val="' + o[0] + '"' + (o[2] ? ' title="' + escH(o[2]) + '"' : "") + ">" + o[1] + "</button>"; }).join("") + "</div></div>"; }
    function chk(k, label) { return '<label><input type="checkbox" data-c="' + k + '"/> ' + label + "</label>"; }
    ov.innerHTML = '<div class="tv-box"><div class="tv-top"><h2>🎬 Video thuyết trình chuyến đi</h2><button class="tv-x" data-a="close">✕ Đóng</button></div>' +
      '<div class="tv-main"><div><div class="tv-prev"><canvas></canvas></div>' +
      '<div class="tv-ctl"><button class="tv-b" data-a="prev" title="Cảnh trước">⏮</button><button class="tv-b navy" data-a="play">▶ Xem thử</button><button class="tv-b" data-a="next" title="Cảnh sau">⏭</button>' +
      '<input type="range" min="0" max="1000" value="0" data-a="seek"/><span class="tv-lbl" data-v="time">0:00</span></div>' +
      '<div class="tv-ctl"><button class="tv-b" data-a="build" title="Tạo lời đọc AI + nhạc nền để xem thử có tiếng">🔊 Dựng tiếng</button><span class="tv-lbl" data-v="aud"></span></div>' +
      '<div class="tv-lbl" data-v="scene" style="margin-top:4px"></div>' +
      '<div class="tv-prog" data-v="prog"><b data-v="phase">…</b><div class="tv-bar"><i></i></div><button class="tv-b" data-a="cancel">Huỷ</button></div>' +
      '<div class="tv-res" data-v="res"></div></div>' +
      '<div class="tv-set">' +
      '<div class="tv-f"><b>Tiêu đề video</b><input type="text" data-o="title" placeholder="' + escH(data.hasTitle ? data.title : "VD: Moskva – Vành đai Vàng 5 ngày") + '"/></div>' +
      seg3("aspect", "Khung hình", [["16:9", "▭ 16:9 ngang"], ["9:16", "▯ 9:16 dọc (TikTok, Reels, Zalo)"], ["1:1", "◻ 1:1 vuông"]]) +
      seg3("res", "Độ nét", [[720, "720p (nhẹ, dễ gửi)"], [1080, "1080p (nét)"]]) +
      seg3("basemap", "Nền bản đồ", [["sat", "🛰️ Vệ tinh"], ["osm", "🗺️ Bản đồ phố"], ["plain", "◼ Đơn giản"]]) +
      seg3("pace", "Nhịp hình", [["fast", "Nhanh"], ["mid", "Vừa"], ["slow", "Chậm"]]) +
      seg3("lang", "Ngôn ngữ chữ & giọng", [["vi", "🇻🇳 Việt"], ["en", "🇬🇧 English"], ["ru", "🇷🇺 Русский"]]) +
      '<div class="tv-f tv-sub"><b>🎙️ Thuyết minh</b>' +
      '<div class="tv-seg" data-k="voice"><button data-val="ai">🤖 Giọng AI — có tiếng trong file video</button><button data-val="sys">💻 Giọng của máy (chỉ trình chiếu)</button><button data-val="off">🔇 Không đọc</button></div>' +
      '<div class="tv-f" data-show="ai sys"><div class="tv-seg" data-k="rate"><button data-val="0.9">🐢 Đọc chậm</button><button data-val="1">Vừa</button><button data-val="1.15">🐇 Nhanh</button></div>' +
      '<div class="tv-seg" data-k="detail"><button data-val="full">Đọc đủ phần giới thiệu</button><button data-val="short" title="Chỉ câu đầu, cắt trọn câu — không có dấu …">Ngắn gọn</button></div>' +
      '<div class="tv-chk">' + chk("ruName", "Đọc kèm tên gốc tiếng Nga (Красная площадь…)") + "</div></div>" +
      '<div class="tv-note" data-show="ai" data-v="aiinfo"></div>' +
      '<div class="tv-row" data-show="sys"><label>Giọng Việt<select data-o="sysVi"></select></label><label>Giọng Nga<select data-o="sysRu"></select></label><label data-v="enpick">Giọng Anh<select data-o="sysEn"></select></label></div>' +
      '<div class="tv-note" data-show="sys" data-v="sysinfo"></div>' +
      '<div class="tv-row" data-show="ai sys"><button class="tv-b" data-a="hear">🔊 Nghe thử giọng</button><span class="tv-lbl" data-v="hearst"></span></div></div>' +
      '<div class="tv-f tv-sub"><b>🎵 Nhạc nền</b>' +
      '<div class="tv-seg" data-k="music"><button data-val="off">Tắt</button>' + Object.keys(MUSIC.PRE).map(function (k) { return '<button data-val="' + k + '">' + MUSIC.PRE[k].name + "</button>"; }).join("") + '<button data-val="file">📂 Nhạc của anh…</button></div>' +
      '<input type="file" accept="audio/*,.mp3,.m4a,.aac,.wav,.ogg,.opus,.flac" data-v="mfile" class="tv-hide"/>' +
      '<div class="tv-row" data-show-music="1"><span>Âm lượng</span><input type="range" min="0" max="100" step="5" data-o="musicVol"/><button class="tv-b" data-a="hearm">▶ Nghe thử</button></div>' +
      '<div class="tv-note" data-v="minfo"></div></div>' +
      '<div class="tv-f"><b>Hiện trên video</b><div class="tv-chk">' +
      chk("photo", "Ảnh") + chk("desc", "Giới thiệu") + chk("hl", "Điểm nhấn") + chk("prac", "Giờ mở cửa & vé") + chk("note", "Ghi chú của anh") + chk("times", "Giờ đến–đi") +
      chk("cost", "Chi phí") + chk("sign", "Chữ ký") + chk("caps", "Phụ đề lời đọc") + chk("clock", "Đồng hồ & ánh sáng theo giờ") + chk("qr", "Mã QR cuối video") + "</div></div>" +
      '<div class="tv-f"><b>Chữ ký (góc video & cuối video)</b><input type="text" data-o="credit"/></div>' +
      '<div class="tv-f" data-show-qr="1"><b>Mã QR dẫn tới (Facebook, Zalo, web…)</b><input type="text" data-o="qrUrl" placeholder="https://fb.com/lopmaybay"/></div>' +
      '<div class="tv-lbl" data-v="est"></div>' +
      '<div class="tv-go"><button class="tv-b gold" data-a="show">▶ Trình chiếu toàn màn hình</button><button class="tv-b navy" data-a="export">⬇️ Xuất video MP4</button></div>' +
      '<div class="tv-note">Giọng AI chạy ngay trên máy (không gửi chữ đi đâu): Piper — VAIS-1000 (CC BY 4.0), Denis (CC0), LJSpeech (public domain). ' +
      'Nhạc dựng sẵn do trình duyệt tự tổng hợp (giai điệu «Коробейники» là dân ca Nga, phạm vi công cộng). Ảnh: Wikimedia Commons. Nền bản đồ: Esri / © OpenStreetMap.</div>' +
      "</div></div></div>";
    document.body.appendChild(ov);
    var $ = function (sel) { return ov.querySelector(sel); };
    var canvas = $("canvas"), ctx = canvas.getContext("2d", { alpha: false }), V = null, t = 3.2, poster = true, playing = false, raf = 0, last = 0, dirty = true;
    $('[data-o="credit"]').value = O.credit || ""; $('[data-o="qrUrl"]').value = O.qrUrl || ""; $('[data-o="musicVol"]').value = Math.round((+O.musicVol || 0) * 100);
    function narrKey() { return JSON.stringify([O.lang, O.voice, O.rate, O.detail, O.ruName, O.desc, O.note, O.times, O.sign, guideName(O), O.qr && O.qrUrl ? 1 : 0, O.cost, O.title]); }
    function mixKey(Vx) { return narrKey() + "|" + O.music + "|" + O.musicVol + "|" + userMusicName + "|" + Vx.total.toFixed(3) + "|" + O.aspect + "|" + O.pace; }
    function fillVoices() {
      var vm = SysVoice.main(O);
      [["sysVi", "vi"], ["sysRu", "ru"], ["sysEn", "en"]].forEach(function (p) {
        var sel = $('[data-o="' + p[0] + '"]'), vs = SysVoice.ofLang(p[1]), best = SysVoice.pick(p[1], O[p[0]], p[1] === O.lang ? null : vm);
        sel.innerHTML = vs.length ? vs.map(function (v) { return '<option value="' + escH(v.name) + '"' + (best && best.name === v.name ? " selected" : "") + ">" + escH(v.name) + "</option>"; }).join("") : '<option value="">(máy chưa có giọng này)</option>';
      });
      var hasVi = SysVoice.ofLang("vi").length, hasRu = SysVoice.ofLang("ru").length;
      $('[data-v="sysinfo"]').textContent = (hasVi ? "" : "⚠️ Máy chưa có giọng tiếng Việt (Windows: Cài đặt → Thời gian & ngôn ngữ → Giọng nói → thêm Tiếng Việt; hoặc dùng Edge). ") +
        (hasRu ? "Tên tiếng Nga sẽ được đọc bằng giọng Nga." : "⚠️ Máy chưa có giọng tiếng Nga — tên Nga sẽ đọc bằng giọng Việt. Nên dùng 🤖 Giọng AI hoặc trình duyệt Edge/Chrome.");
      $('[data-v="enpick"]').classList.toggle("tv-hide", O.lang !== "en");
    }
    try { if (global.speechSynthesis) global.speechSynthesis.onvoiceschanged = function () { fillVoices(); }; } catch (e) { }
    function syncUI() {
      ov.querySelectorAll(".tv-seg").forEach(function (sg) { var k = sg.dataset.k; sg.querySelectorAll("button").forEach(function (b) { b.classList.toggle("on", String(O[k]) === b.dataset.val); }); });
      ov.querySelectorAll("[data-c]").forEach(function (c) { c.checked = !!O[c.dataset.c]; });
      ov.querySelectorAll("[data-show]").forEach(function (el) { el.classList.toggle("tv-hide", el.dataset.show.split(" ").indexOf(O.voice) < 0); });
      ov.querySelectorAll("[data-show-music]").forEach(function (el) { el.classList.toggle("tv-hide", O.music === "off"); });
      ov.querySelectorAll("[data-show-qr]").forEach(function (el) { el.classList.toggle("tv-hide", !O.qr); });
      $('[data-a="export"]').textContent = "⬇️ Xuất video MP4 " + (O.voice === "ai" ? (O.music !== "off" ? "(lời đọc + nhạc)" : "(có lời đọc)") : O.music !== "off" ? "(chỉ có nhạc)" : "(không tiếng)");
      $('[data-v="minfo"]').textContent = O.music === "file" ? (userMusicName ? "🎵 " + userMusicName : "Chọn một tệp nhạc trên máy (MP3, M4A, WAV…)") : (O.music === "off" ? "" : "Nhạc tự nhỏ lại khi có lời đọc, mở đầu và kết thúc mượt.");
      fillVoices(); aiInfo();
    }
    async function aiInfo() {
      var el = $('[data-v="aiinfo"]'); if (!el || O.voice !== "ai") return;
      if (!AIV.supported()) { el.innerHTML = "⚠️ Trình duyệt này chưa chạy được giọng AI — hãy dùng Chrome hoặc Edge bản mới."; return; }
      var langs = O.lang === "vi" ? ["vi", "ru"] : O.lang === "en" ? ["en", "ru"] : ["ru"], info = {};
      try { info = await AIV.storageInfo(); } catch (e) { }
      var miss = langs.filter(function (l) { return !info[l]; }), mb = miss.reduce(function (s, l) { return s + AIV.VOICES[l].mb; }, 0) + (miss.length ? 30 : 0);
      el.innerHTML = "Giọng AI đọc thẳng vào file video: " + langs.map(function (l) { var v = AIV.VOICES[l]; return (l === "vi" ? "🇻🇳 " : l === "ru" ? "🇷🇺 " : "🇬🇧 ") + v.name + " (" + v.g + ")"; }).join(" + ") +
        ". Tên Nga viết La-tinh được đổi về chữ Nga để giọng Nga đọc đúng. " + (miss.length ? "Lần đầu cần tải ~" + mb + " MB (lưu lại trên máy, lần sau dùng ngay)." : "✅ Giọng đã có sẵn trên máy.");
    }
    function audLabel() {
      var need = O.voice === "ai" || O.music !== "off", ok = player.has(), el = $('[data-v="aud"]');
      $('[data-a="build"]').classList.toggle("tv-hide", !need || ok);
      var ai = O.voice === "ai", mu = O.music !== "off", sysNote = O.voice === "sys" ? " · 💻 giọng máy chỉ đọc khi trình chiếu (muốn video tải về có lời đọc → chọn 🤖 Giọng AI)" : "";
      el.textContent = !need ? (O.voice === "sys" ? "💻 Giọng máy chỉ đọc khi trình chiếu — muốn video tải về có lời đọc, chọn 🤖 Giọng AI" : "🔇 Video không tiếng") :
        ok ? (ai ? "🔊 Xem thử có tiếng (lời đọc" + (mu ? " + nhạc" : "") + ")" : "🎵 Xem thử có nhạc nền" + sysNote) :
        "Xem thử đang không tiếng — bấm 🔊 Dựng tiếng để nghe " + (ai ? "lời đọc" + (mu ? " + nhạc" : "") : "nhạc nền") + sysNote;
    }
    function rebuild() {
      var d = dims(O), D = prepare(data, O), NR = narrate(D, O), ap = (O.voice === "ai" && AUD.nk === narrKey()) ? AUD.AP : null;
      canvas.width = d.W; canvas.height = d.H;
      var wasPlaying = playing && player.playing(); player.stop();
      V = buildScenes(D, O, d.W, d.H, NR, ap); t = Math.min(t, V.total);
      player.set(AUD.mix && AUD.mk === mixKey(V) ? AUD.mix : null);
      if (wasPlaying && player.has()) player.play(t);
      var mb = Math.round(V.total * Math.round(d.W * d.H * 30 * (O.res === 1080 ? 0.085 : 0.095)) / 8 / 1048576 * 0.75 + (O.voice === "ai" || O.music !== "off" ? V.total * 0.02 : 0));
      $('[data-v="est"]').textContent = "⏱ Thời lượng ~" + fmtClock(V.total) + (O.voice === "ai" && !ap ? " (tính lại theo lời đọc khi dựng tiếng)" : "") + " · " + D.stops.length + " điểm · " + D.days.length + " ngày · ~" + mb + " MB (" + d.W + "×" + d.H + ")";
      D.stops.forEach(function (s) { if (O.photo && s.photo) loadPhoto(s); });
      if (O.qr && O.qrUrl) qrCanvas(O.qrUrl);
      dirty = true; saveOpts(O); audLabel();
    }
    _onAsset = function () { dirty = true; };
    function draw() {
      if (!V) return; renderFrame(ctx, V, t, playing ? (performance.now() / 1000) : t); dirty = false;
      $('[data-a="seek"]').value = Math.round(t / V.total * 1000); $('[data-v="time"]').textContent = fmtClock(t) + " / " + fmtClock(V.total);
      $('[data-v="scene"]').textContent = sceneLabel(V.scenes[sceneAt(V, t)], V);
    }
    function setPlay(on) { playing = on; last = 0; $('[data-a="play"]').textContent = on ? "⏸ Dừng" : "▶ Xem thử"; if (on && player.has()) player.play(t); else player.stop(); }
    function loop(ts) {
      raf = requestAnimationFrame(loop);
      if (playing) {
        if (player.has() && player.playing()) t = player.time(); else { var dt = last ? (ts - last) / 1000 : 0; last = ts; t += dt; }
        if (t >= V.total) { t = V.total; setPlay(false); }
        dirty = true;
      }
      if (dirty) draw();
    }
    raf = requestAnimationFrame(loop);
    function close() { cancelAnimationFrame(raf); playing = false; player.close(); hearStop(); SysVoice.stop(); AIV.dispose(); _onAsset = null; document.removeEventListener("keydown", esc); ov.remove(); }
    function esc(e) { if (e.key === "Escape" && !document.querySelector(".tv-show")) close(); }
    document.addEventListener("keydown", esc);
    // ---- tiến trình chung (dựng tiếng / xuất video) ----
    var cancelFn = null, prog = $('[data-v="prog"]'), bar = prog.querySelector("i");
    function mkUI() { return { phase: function (msg, f) { $('[data-v="phase"]').textContent = msg; bar.style.width = Math.round(clamp(f || 0, 0, 1) * 100) + "%"; }, onCancel: function (fn) { cancelFn = fn; } }; }
    // dựng lời đọc AI + nhạc cho đúng các tuỳ chọn hiện tại
    async function buildAudio(ui, isCancelled) {
      var D = prepare(data, O), NR = narrate(D, O), nk = narrKey();
      if (O.voice === "ai") { if (AUD.nk !== nk || !AUD.AP) { AUD.AP = null; AUD.AP = await AIV.synthNarration(NR, O, ui, isCancelled); AUD.nk = nk; } }
      var d = dims(O), Vx = buildScenes(D, O, d.W, d.H, NR, O.voice === "ai" ? AUD.AP : null), mk = mixKey(Vx);
      if (AUD.mk !== mk) { AUD.mix = await mixAudio(Vx, O, userMusic, ui); AUD.mk = mk; }
      return { V: Vx, mix: AUD.mix, NR: NR };
    }
    async function withProgress(fn) {
      if (busy) return null; busy = true; var cancelled = false;
      prog.style.display = "block"; var ui = mkUI(); ui.onCancel(function () { cancelled = true; });
      ov.querySelectorAll('[data-a="export"],[data-a="show"],[data-a="build"]').forEach(function (b) { b.disabled = true; });
      try { return await fn(ui, function () { return cancelled; }); }
      finally { busy = false; prog.style.display = "none"; cancelFn = null; ov.querySelectorAll('[data-a="export"],[data-a="show"],[data-a="build"]').forEach(function (b) { b.disabled = false; }); }
    }
    function showErr(err) {
      var res = $('[data-v="res"]');
      if (err && err.message === "cancel") res.innerHTML = '<div class="tv-note">Đã huỷ.</div>';
      else { res.innerHTML = '<div class="tv-note" style="color:#b23b34">❌ Lỗi: ' + escH(err && (err.message || err)) + "</div>"; try { console.error(err); } catch (e) { } }
      res.style.display = "block";
    }
    async function doBuild(andPlay) {
      try {
        var r = await withProgress(buildAudio); if (!r) return false;
        rebuild(); if (andPlay) { poster = false; if (t >= V.total - 0.1) t = 0; setPlay(true); }
        return true;
      } catch (err) { showErr(err); return false; }
    }
    async function doExport() {
      setPlay(false);
      var res = $('[data-v="res"]'); res.style.display = "none";
      try {
        var out = await withProgress(async function (ui, isC) {
          var b = (O.voice === "ai" || O.music !== "off") ? await buildAudio(ui, isC) : (function () { var D = prepare(data, O), NR = narrate(D, O), d = dims(O); return { V: buildScenes(D, O, d.W, d.H, NR, null), mix: null, NR: NR }; })();
          var x = await exportVideo(b.V, { phase: ui.phase, onCancel: function (fn) { cancelFn = fn; } }, b.mix);
          return { r: x, V: b.V, NR: b.NR };
        });
        if (!out) return;
        rebuild();
        var r = out.r, Vx = out.V, url = URL.createObjectURL(r.blob), base = slug(prepare(data, O).title) + "-" + O.aspect.replace(":", "x"), name = base + "." + r.ext, mb = (r.blob.size / 1048576).toFixed(1);
        var warn = (r.info && r.info.tiles && r.info.failed > r.info.tiles * 0.3) ? '<div class="tv-note" style="color:#b23b34">⚠️ ' + r.info.failed + "/" + r.info.tiles + " ô bản đồ không tải được (mạng chậm hoặc bị chặn) — những chỗ đó dùng nền đơn giản. Có thể thử lại, hoặc chọn nền “Đơn giản”.</div>" : "";
        if (r.noAudioCodec) warn += '<div class="tv-note" style="color:#b23b34">⚠️ Trình duyệt này không mã hoá được âm thanh nên video không có tiếng — hãy dùng Chrome hoặc Edge bản mới.</div>';
        var hasNarr = O.voice === "ai" && r.audio && Vx.scenes.some(function (sc) { return sc.ap; });
        var langs = narrLangs(out.NR).filter(function (l) { return AIV.VOICES[l]; });
        res.innerHTML = "<b>✅ Xong: " + escH(name) + " · " + mb + " MB · " + fmtClock(Vx.total) + (r.audio ? (hasNarr ? " · 🔊 có lời đọc" + (O.music !== "off" ? " + nhạc" : "") : " · 🎵 có nhạc nền") : " · 🔇 không tiếng") + "</b>" + warn + '<video controls playsinline src="' + url + '"></video>' +
          '<div class="tv-ctl"><a class="tv-b gold" href="' + url + '" download="' + escH(name) + '">⬇️ Tải video về máy</a>' +
          (hasNarr ? '<button class="tv-b" data-r="srt" title="Tệp phụ đề cho YouTube/Facebook">💬 Phụ đề .srt</button>' : "") +
          '<button class="tv-b" data-r="chap" title="Dán vào phần mô tả YouTube để có chương">📑 Mục lục YouTube</button><button class="tv-b" data-r="cover">🖼️ Ảnh bìa JPG</button>' +
          (navigator.canShare && navigator.canShare({ files: [new File([r.blob], name, { type: r.blob.type })] }) ? '<button class="tv-b" data-r="share">📤 Chia sẻ (Zalo, Messenger…)</button>' : "") + "</div>" +
          '<div data-r="box"></div><div class="tv-note">Mã hoá: ' + escH(r.codec || "") + (r.ext !== "mp4" ? " — trình duyệt này chỉ xuất được WebM; dùng Chrome/Edge để có MP4." : "") +
          (O.voice === "ai" && r.audio ? " · Giọng đọc AI: Piper — " + escH(AIV.credit(langs)) : "") + "</div>";
        res.style.display = "block";
        res.querySelectorAll("[data-r]").forEach(function (b) {
          b.onclick = async function (ev) {
            ev.stopPropagation(); var k = b.dataset.r, box = res.querySelector('[data-r="box"]');
            if (k === "srt") dl(new Blob([makeSRT(Vx)], { type: "text/plain;charset=utf-8" }), base + ".srt");
            else if (k === "chap") { var ch = makeChapters(Vx); try { await navigator.clipboard.writeText(ch); b.textContent = "✅ Đã chép mục lục"; } catch (e) { } box.innerHTML = '<textarea readonly>' + escH(ch) + "</textarea>"; }
            else if (k === "cover") { b.disabled = true; try { dl(await coverBlob(Vx), base + "-bia.jpg"); } finally { b.disabled = false; } }
            else if (k === "share") navigator.share({ files: [new File([r.blob], name, { type: r.blob.type })], title: name }).catch(function () { });
          };
        });
      } catch (err) { showErr(err); }
    }
    // ---- nghe thử giọng / nhạc ----
    var hearP = null;
    function hearStop() { if (hearP) { try { hearP.stop(); } catch (e) { } hearP = null; } SysVoice.stop(); }
    async function hear() {
      hearStop(); var st = $('[data-v="hearst"]');
      var D = prepare(data, O), NR = narrate(D, O), s0 = D.stops[0], key = s0 ? "stop:" + s0.i : "intro";
      var sample = {}; sample[key] = (NR[key] || []).filter(function (x) { return x.k === "name" || x.k === "desc"; }).slice(0, 2);
      if (!sample[key].length) sample[key] = (NR.intro || []).slice(0, 1);
      if (O.voice === "sys") { st.textContent = "🔊 Đang đọc…"; var h = SysVoice.speak([].concat.apply([], sample[key].map(function (x) { return x.segs; })), O, function () { st.textContent = ""; }); hearP = h; return; }
      try {
        var ap = await withProgress(function (ui, isC) { return AIV.synthNarration(sample, O, ui, isC); }); if (!ap) return;
        var a = ap.scenes[key], C2 = global.AudioContext || global.webkitAudioContext, ac = new C2(), sr = ac.sampleRate;
        var b = ac.createBuffer(1, Math.ceil((a.dur + 0.3) * sr), sr), out = b.getChannelData(0);
        a.clips.forEach(function (c) { var r = c.sr / sr, o = Math.round(c.t * sr), n = Math.floor(c.pcm.length / r); for (var i = 0; i < n && o + i < out.length; i++) { var x = i * r, k = Math.floor(x), f = x - k; out[o + i] += c.pcm[k] * (1 - f) + (c.pcm[k + 1] || 0) * f; } });
        var src = ac.createBufferSource(); src.buffer = b; src.connect(ac.destination); src.start();
        st.textContent = "🔊 " + sample[key].map(function (x) { return x.c; }).join(" ");
        hearP = { stop: function () { try { src.stop(); ac.close(); } catch (e) { } st.textContent = ""; } };
        src.onended = function () { if (hearP) hearP.stop(); hearP = null; };
      } catch (err) { showErr(err); }
    }
    async function hearMusic() {
      hearStop(); if (O.music === "off") return;
      var btn = $('[data-a="hearm"]'); btn.disabled = true;
      try {
        var sr = 48000, ch = await MUSIC.track(O, 14, sr, userMusic); if (!ch) return;
        var C2 = global.AudioContext || global.webkitAudioContext, ac = new C2({ sampleRate: sr }), n = ch[0].length, b = ac.createBuffer(2, n, sr), vol = clamp(+O.musicVol || 0, 0, 1) * 0.9;
        for (var c = 0; c < 2; c++) { var o = b.getChannelData(c), s = ch[c]; for (var i = 0; i < n; i++) o[i] = s[i] * vol * Math.min(1, i / sr / 0.8, (n - i) / sr / 1.5); }
        var src = ac.createBufferSource(); src.buffer = b; src.connect(ac.destination); src.start();
        hearP = { stop: function () { try { src.stop(); ac.close(); } catch (e) { } } }; src.onended = function () { if (hearP) hearP.stop(); hearP = null; };
      } catch (err) { showErr(err); } finally { btn.disabled = false; }
    }
    // ---- sự kiện ----
    var mfile = $('[data-v="mfile"]');
    mfile.onchange = async function () {
      var f = mfile.files && mfile.files[0]; if (!f) return;
      $('[data-v="minfo"]').textContent = "Đang đọc tệp nhạc…";
      try { userMusic = await MUSIC.decodeFile(f); userMusicName = f.name + " · " + fmtClock(userMusic.duration); O.music = "file"; }
      catch (e) { userMusic = null; userMusicName = ""; if (O.music === "file") O.music = DEF.music; alert("Không đọc được tệp nhạc này — hãy thử MP3/M4A/WAV khác."); }
      mfile.value = ""; syncUI(); rebuild();
    };
    ov.addEventListener("click", function (e) {
      var b = e.target.closest("[data-a],[data-val]"); if (!b || b.disabled) return;
      if (b.dataset.val != null && b.parentNode.dataset.k) {
        var k = b.parentNode.dataset.k, v = b.dataset.val;
        if (k === "music" && v === "file") { if (!userMusic) { mfile.click(); return; } }
        O[k] = (k === "res" || k === "rate") ? +v : v; hearStop(); syncUI(); rebuild(); return;
      }
      var a = b.dataset.a;
      if (a === "close") close();
      else if (a === "play") { if (playing) setPlay(false); else { if (poster || t >= V.total - 0.05) t = 0; poster = false; setPlay(true); } }
      else if (a === "prev" || a === "next") { poster = false; var i = sceneAt(V, t + 0.001) + (a === "next" ? 1 : -1); i = clamp(i, 0, V.scenes.length - 1); t = V.scenes[i].t0 + 0.001; if (playing) setPlay(true); dirty = true; }
      else if (a === "build") { setPlay(false); doBuild(true); }
      else if (a === "show") startShow();
      else if (a === "export") doExport();
      else if (a === "hear") hear();
      else if (a === "hearm") hearMusic();
    });
    async function startShow() {
      setPlay(false); hearStop();
      if (O.voice === "ai" || (O.voice === "off" && O.music !== "off")) {
        try { var r = await withProgress(buildAudio); if (!r) return; rebuild(); present(data, O, { NR: r.NR, AP: O.voice === "ai" ? AUD.AP : null, mix: r.mix, music: userMusic }); }
        catch (err) { showErr(err); }
      } else present(data, O, { music: userMusic });
    }
    ov.addEventListener("input", function (e) {
      var el = e.target;
      if (el.dataset.a === "seek") { poster = false; t = (+el.value / 1000) * V.total; if (playing) setPlay(true); dirty = true; return; }
      if (el.dataset.o === "musicVol") { O.musicVol = (+el.value) / 100; clearTimeout(el._t); el._t = setTimeout(rebuild, 300); return; }
      if (el.dataset.o && el.tagName !== "SELECT") { O[el.dataset.o] = el.value; clearTimeout(el._t); el._t = setTimeout(rebuild, 350); }
    });
    ov.addEventListener("change", function (e) {
      var el = e.target;
      if (el.dataset.c) { O[el.dataset.c] = el.checked; syncUI(); rebuild(); }
      else if (el.tagName === "SELECT" && el.dataset.o) { O[el.dataset.o] = el.value; saveOpts(O); if (el.dataset.o === SysVoice.key(O.lang)) fillVoices(); }
    });
    $('[data-a="cancel"]').onclick = function (e) { e.stopPropagation(); if (cancelFn) cancelFn(); };
    syncUI(); rebuild();
    return { close: close };
  }

  /* ---------------- 14. trình chiếu toàn màn hình ----------------
     • giọng AI / chỉ có nhạc: phát dải âm thanh đã trộn, hình chạy theo đồng hồ của âm thanh (khớp như video xuất ra)
     • giọng máy: đọc từng cảnh bằng giọng Việt + giọng Nga của máy, cảnh chờ đọc xong mới chuyển; nhạc tự nhỏ lại khi đọc */
  function present(data, O0, pre) {
    pre = pre || {};
    var O = {}; for (var k in O0) O[k] = O0[k];
    if (!document.getElementById("tv-css")) { var st0 = document.createElement("style"); st0.id = "tv-css"; st0.textContent = CSS; document.head.appendChild(st0); }
    var box = document.createElement("div"); box.className = "tv-show";
    box.innerHTML = '<canvas></canvas><div class="tv-sctl"><button data-p="prev" title="Cảnh trước (←)">⏮</button><button data-p="play" title="Tạm dừng (Space)">⏸</button><button data-p="next" title="Cảnh sau (→)">⏭</button>' +
      '<button data-p="voice" title="Bật/tắt tiếng">🔊</button><span class="tv-sl"></span><button data-p="close" title="Thoát (Esc)">✕</button></div>';
    document.body.appendChild(box);
    var canvas = box.querySelector("canvas"), ctx = canvas.getContext("2d", { alpha: false }), ctl = box.querySelector(".tv-sctl"), sl = box.querySelector(".tv-sl");
    var ratio = O.aspect === "9:16" ? 9 / 16 : (O.aspect === "1:1" ? 1 : 16 / 9);
    var sw = window.innerWidth * (window.devicePixelRatio || 1), sh = window.innerHeight * (window.devicePixelRatio || 1);
    var W = Math.min(1920, sw, sh * ratio), H = W / ratio; if (H > Math.min(1920, sh)) { H = Math.min(1920, sh); W = H * ratio; }
    W = Math.round(W / 2) * 2; H = Math.round(H / 2) * 2; canvas.width = W; canvas.height = H;
    var D = prepare(data, O), NR = pre.NR || narrate(D, O), V = buildScenes(D, O, W, H, NR, pre.AP || null);
    var timed = !!pre.mix || O.voice === "ai" || O.voice === "off", sound = true, raf = 0, last = 0, amb = 0, playing = true, closed = false;
    try { (box.requestFullscreen || box.webkitRequestFullscreen || function () { }).call(box); } catch (e) { }
    preloadAll(V, null, null, { step: 0.5, maxTiles: 600 });
    if (O.qr && O.qrUrl) ensureQR();
    var hideT = 0;
    function poke() { ctl.classList.remove("hide"); clearTimeout(hideT); hideT = setTimeout(function () { ctl.classList.add("hide"); }, 2600); }
    function setPlayBtn() { ctl.querySelector('[data-p="play"]').textContent = playing ? "⏸" : "▶"; }
    var player = AudioPlayer(), t = 0;
    if (timed) {
      // ---- chế độ có dải âm thanh dựng sẵn (hoặc không tiếng): hình theo đồng hồ âm thanh ----
      (async function () {
        var mix = pre.mix;
        if (mix && Math.abs(mix.duration - V.total) > 0.12) { sl.textContent = "Đang khớp tiếng…"; try { mix = await mixAudio(V, O, pre.music, null); } catch (e) { mix = null; } }
        if (closed) return;
        player.set(mix || null); if (player.has()) player.play(0);
        raf = requestAnimationFrame(frameT); poke();
      })();
    } else { V.live = { key: null, idx: -1 }; startScene(0); raf = requestAnimationFrame(frameL); poke(); }
    function frameT(ts) {
      raf = requestAnimationFrame(frameT);
      var dt = last ? Math.min(0.1, (ts - last) / 1000) : 0; last = ts; amb += dt;
      if (playing) { if (player.has() && player.playing()) t = player.time(); else t += dt; if (t >= V.total) { t = V.total - 0.001; playing = false; player.stop(); setPlayBtn(); } }
      renderFrame(ctx, V, Math.min(t, V.total - 0.001), amb);
      var sc = V.scenes[sceneAt(V, t)]; if (sl.dataset.k !== sc.key) { sl.dataset.k = sc.key; sl.textContent = sceneLabel(sc, V); }
    }
    function seekScene(d) { var i = clamp(sceneAt(V, t + 0.001) + d, 0, V.scenes.length - 1); t = V.scenes[i].t0 + 0.001; if (playing && player.has()) player.play(t); }
    // ---- chế độ giọng máy: từng cảnh, chờ đọc xong ----
    var idx = 0, tau = 0, narrDone = true, speaking = null, music = null, mg = null, mctx = null;
    function startScene(i) {
      idx = clamp(i, 0, V.scenes.length - 1); tau = 0.0001; narrDone = false; if (speaking) speaking.stop(); speaking = null; SysVoice.stop();
      var sc = V.scenes[idx]; sl.textContent = sceneLabel(sc, V); V.live = { key: sc.key, idx: -1 };
      if (sc.stop && O.photo) loadPhoto(sc.stop);
      var my = idx, list = sc.narr || [];
      if (!sound || O.voice !== "sys" || !list.length) { narrDone = true; return; }
      setTimeout(function () {
        if (my !== idx) return;
        var n = 0;
        (function nextSent() {
          if (my !== idx) return;
          if (n >= list.length) { narrDone = true; V.live.doneTau = tau; duck(false); return; }
          V.live.idx = n; duck(true);
          speaking = SysVoice.speak(list[n].segs, O, function () { n++; nextSent(); });
        })();
      }, Math.max(150, (sc.lead || 0.3) * 1000 * 0.6));
    }
    function frameL(ts) {
      raf = requestAnimationFrame(frameL);
      var dt = last ? Math.min(0.1, (ts - last) / 1000) : 0; last = ts; amb += dt;
      var sc = V.scenes[idx];
      if (playing) {
        var extra = sc.type === "stop" && sc.extraPages ? sc.extraPages * 3.4 : 0, hold = sc.dur - (sc.type === "outro" ? 0.3 : 0.55);
        if (!narrDone && tau + dt >= hold) tau = Math.max(tau, Math.min(hold, tau + dt));
        else if (narrDone && V.live.doneTau != null && extra && tau < V.live.doneTau + extra && tau + dt >= hold) tau = Math.min(hold, tau + dt);
        else tau += dt;
        if (tau >= sc.dur) { if (idx < V.scenes.length - 1) startScene(idx + 1); else { tau = sc.dur; playing = false; setPlayBtn(); } }
      }
      renderFrame(ctx, V, V.scenes[idx].t0 + Math.min(tau, V.scenes[idx].dur - 0.0001), amb);
    }
    // nhạc nền khi trình chiếu bằng giọng máy (lặp, nhỏ lại khi đọc)
    if (!timed && O.music !== "off") (async function () {
      try {
        var sr = 48000, ch = await MUSIC.track(O, Math.min(600, V.total * 1.7 + 30), sr, pre.music); if (!ch || closed) return;
        var C2 = global.AudioContext || global.webkitAudioContext; mctx = new C2({ sampleRate: sr });
        var b = mctx.createBuffer(2, ch[0].length, sr); b.getChannelData(0).set(ch[0]); b.getChannelData(1).set(ch[1]);
        music = mctx.createBufferSource(); music.buffer = b; music.loop = true; mg = mctx.createGain(); mg.gain.value = 0;
        music.connect(mg); mg.connect(mctx.destination); music.start(); duck(!narrDone);
      } catch (e) { }
    })();
    function mlevel() { return clamp(+O.musicVol || 0, 0, 1) * (O.voice === "sys" ? 0.6 : 0.9); }
    function duck(on) { if (!mg || !mctx) return; var g = mg.gain, now = mctx.currentTime; g.cancelScheduledValues(now); g.setValueAtTime(g.value, now); g.linearRampToValueAtTime(sound ? mlevel() * (on ? 0.25 : 1) : 0, now + (on ? 0.25 : 0.8)); }
    function close() {
      closed = true; cancelAnimationFrame(raf); player.close(); if (speaking) speaking.stop(); SysVoice.stop();
      if (mctx) { try { music.stop(); mctx.close(); } catch (e) { } }
      document.removeEventListener("keydown", key); try { if (document.fullscreenElement) document.exitFullscreen(); } catch (e) { } box.remove();
    }
    function toggle() {
      playing = !playing; setPlayBtn();
      if (timed) { if (playing) { if (t >= V.total - 0.05) t = 0; if (player.has()) player.play(t); } else player.stop(); return; }
      if (!playing) { if (speaking) speaking.stop(); SysVoice.stop(); if (mctx) mctx.suspend(); }
      else { if (mctx) mctx.resume(); if (!narrDone) startScene(idx); }
    }
    function key(e) {
      if (e.key === "Escape") close();
      else if (e.key === " ") { e.preventDefault(); toggle(); }
      else if (e.key === "ArrowRight") timed ? seekScene(1) : startScene(idx + 1);
      else if (e.key === "ArrowLeft") timed ? seekScene(-1) : startScene(idx - 1);
      poke();
    }
    document.addEventListener("keydown", key);
    box.addEventListener("mousemove", poke); box.addEventListener("touchstart", poke, { passive: true });
    ctl.addEventListener("click", function (e) {
      var b = e.target.closest("[data-p]"); if (!b) return; var a = b.dataset.p;
      if (a === "close") close(); else if (a === "play") toggle();
      else if (a === "next") timed ? seekScene(1) : startScene(idx + 1); else if (a === "prev") timed ? seekScene(-1) : startScene(idx - 1);
      else if (a === "voice") {
        sound = !sound; b.textContent = sound ? "🔊" : "🔇";
        if (timed) player.mute(!sound);
        else { if (!sound) { if (speaking) speaking.stop(); SysVoice.stop(); narrDone = true; } duck(!narrDone); }
      }
      poke();
    });
    if (!timed && O.voice === "sys" && !SysVoice.ofLang(O.lang).length) sl.textContent = "⚠️ Máy chưa có giọng " + (O.lang === "vi" ? "tiếng Việt" : O.lang === "ru" ? "tiếng Nga" : "tiếng Anh") + " — nên chọn 🤖 Giọng AI";
    return { close: close };
  }

  global.TourVideo = { open: open, present: present, version: VERSION,
    _t: { md5: md5, photoCandidates: photoCandidates, prepare: prepare, narrate: narrate, buildScenes: buildScenes, renderFrame: renderFrame, exportVideo: exportVideo,
          frameState: frameState, collectTiles: collectTiles, dims: dims, DEF: DEF, SAY: SAY, AIV: AIV, MUSIC: MUSIC, mixAudio: mixAudio, makeSRT: makeSRT,
          makeChapters: makeChapters, coverBlob: coverBlob, SysVoice: SysVoice, qrCanvas: qrCanvas, ensureQR: ensureQR, cardModel: cardModel, pageState: pageState },
    // bộ công cụ dùng chung (nghe-thuat/art-video.js)
    lib: { VERSION: VERSION, BASE: BASE, clamp: clamp, lerp: lerp, seg: seg, ease: ease, easeOut: easeOut, easeOutBack: easeOutBack, escH: escH, fmtClock: fmtClock, sleep: sleep,
           F: F, FONT: FONT, C: C, wrap: wrap, wrapAll: wrapAll, fitLine: fitLine, rr: rr, spacing: spacing, md5: md5, dims: dims, SAY: SAY, AIV: AIV, MUSIC: MUSIC,
           mixAudio: mixAudio, exportVideo: exportVideo, makeSRT: makeSRT, ensureQR: ensureQR, qrCanvas: qrCanvas, shortUrl: shortUrl, AudioPlayer: AudioPlayer,
           CSS: CSS, dl: dl, slug: slug, mergeSegs: mergeSegs, loadScript: loadScript, estimateSents: estimateSents, SysVoice: SysVoice, wfEnc: wfEnc, pickAudioCodec: pickAudioCodec } };
})(window);
