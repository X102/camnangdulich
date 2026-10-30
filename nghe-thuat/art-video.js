/* =====================================================================
   art-video.js — 🎨 Video "Giờ thì tôi mới hiểu…" · Giải mã tác phẩm
   Cẩm nang Du lịch (bản nội bộ) · Phạm Đăng Hiển · fb.com/lopmaybay

   Dựng video kiểu trend "Giờ thì tôi mới hiểu vì sao người ta có thể dành hàng giờ ngắm nhìn một bức tranh":
     câu mở đầu → giới thiệu → máy quay lướt vào TỪNG CHI TIẾT (khung sáng, đánh số), đặt câu hỏi → lời giải
     → kéo ra toàn cảnh, hiện lại các điểm vừa xem → lời kết → nguồn ảnh, mã QR.
   - Lời đọc: giọng AI chạy trên máy (Piper, dùng chung với assets/tour-video.js), phụ đề sáng theo lời đọc (karaoke).
   - Nhạc nền: các bản tự tổng hợp (🎋 Ngũ cung, 🕯️ Suy ngẫm…) hoặc nhạc của anh; tự nhỏ lại khi có lời.
   - Xuất MP4 (H.264 + AAC/Opus), phụ đề .srt, mục lục chương, ảnh bìa, chữ đăng bài kèm hashtag.
   - ✏️ Chỉnh chi tiết: kéo khung trên ảnh, sửa câu hỏi/lời giải, thêm/bớt chi tiết, nạp ảnh của anh,
     lưu ngay trên máy (localStorage + IndexedDB), xuất/nhập kịch bản JSON.
   Phụ thuộc: ../assets/tour-video.js (v2.1+, TourVideo.lib).
   Gọi: ArtVideo.open(work)  ·  ArtVideo.edit(work)  ·  ArtVideo.newWork()
   ===================================================================== */
(function (global) {
  "use strict";
  var TVv = global.TourVideo;
  if (!TVv || !TVv.lib) { if (global.console) console.error("art-video.js cần assets/tour-video.js (v2.1+)"); return; }
  var L = TVv.lib, VERSION = "1.0";
  var clamp = L.clamp, lerp = L.lerp, seg = L.seg, ease = L.ease, easeOut = L.easeOut, F = L.F, C = L.C, wrap = L.wrap, rr = L.rr, escH = L.escH,
      fmtClock = L.fmtClock, SAY = L.SAY, AIV = L.AIV, MUSIC = L.MUSIC, sleep = L.sleep;
  var SERIF = '"Times New Roman", "Noto Serif", "Liberation Serif", Georgia, serif';
  function FS(weight, px, italic) { return (italic ? "italic " : "") + weight + " " + Math.max(1, Math.round(px)) + "px " + SERIF; }
  var GOLD = "#f2c14e", GOLD2 = "#c8a24b", NAVY = "#0f2138";
  var DB = function () { return global.ART_DB || { types: [], eras: [], works: [] }; };
  function typeOf(id) { var t = (DB().types || []).filter(function (x) { return x.id === id; })[0]; return t || { id: id, vi: id, icon: "🎨", noun: "một tác phẩm" }; }
  function clone(o) { return JSON.parse(JSON.stringify(o)); }

  /* ---------------- 1. ảnh: Wikimedia Commons (có CORS) · ảnh của anh (IndexedDB) ---------------- */
  function commonsParts(file) {
    var name = String(file || "").replace(/ /g, "_"); name = name.charAt(0).toUpperCase() + name.slice(1);
    var h = L.md5(name), enc = L.wfEnc(name);
    return { up: "https://upload.wikimedia.org/wikipedia/commons/", dir: h.charAt(0) + "/" + h.slice(0, 2) + "/", enc: enc, ext: (name.split(".").pop() || "").toLowerCase() };
  }
  function commonsCands(im) {
    var p = commonsParts(im.file), base = p.up + "thumb/" + p.dir + p.enc + "/", out = [];
    if (p.ext === "svg") return [base + "3840px-" + p.enc + ".png", base + "1920px-" + p.enc + ".png", base + "1280px-" + p.enc + ".png"];
    if ((im.w || 0) > 3840) out.push(base + "3840px-" + p.enc);
    else out.push(p.up + p.dir + p.enc);
    if ((im.w || 0) > 1920) out.push(base + "1920px-" + p.enc);
    if ((im.w || 0) > 1280) out.push(base + "1280px-" + p.enc);
    out.push(p.up + p.dir + p.enc);
    return out.filter(function (u, i) { return out.indexOf(u) === i; });
  }
  // ảnh nhỏ cho danh mục (chuẩn kích thước của Wikimedia: 330/500/960…)
  function commonsThumb(im, w) {
    if (!im || !im.file) return "";
    var p = commonsParts(im.file); w = w || 500;
    if (p.ext === "svg") return p.up + "thumb/" + p.dir + p.enc + "/" + w + "px-" + p.enc + ".png";
    if ((im.w || 0) <= w) return p.up + p.dir + p.enc;
    return p.up + "thumb/" + p.dir + p.enc + "/" + w + "px-" + p.enc;
  }
  function commonsPage(file) { return "https://commons.wikimedia.org/wiki/File:" + encodeURIComponent(String(file).replace(/ /g, "_")); }
  var IMGC = {};
  function loadOne(url, timeout) {
    if (IMGC[url]) return IMGC[url];
    IMGC[url] = new Promise(function (res) {
      var im = new Image(), done = false; im.crossOrigin = "anonymous"; im.decoding = "async";
      var to = setTimeout(function () { fin(null); }, timeout || 30000);
      function fin(v) { if (done) return; done = true; clearTimeout(to); if (!v) delete IMGC[url]; res(v); }
      im.onload = function () { fin(im.naturalWidth > 0 ? im : null); }; im.onerror = function () { fin(null); };
      im.src = url;
    });
    return IMGC[url];
  }
  async function loadCands(cands) { for (var i = 0; i < cands.length; i++) { var im = await loadOne(cands[i]); if (im) return im; } return null; }

  // IndexedDB: ảnh của anh (blob) theo khoá "<id>#<số ảnh>"
  var IDB = (function () {
    var dbp = null;
    function open() {
      if (dbp) return dbp;
      dbp = new Promise(function (res) {
        try { var rq = indexedDB.open("av-images", 1); rq.onupgradeneeded = function () { rq.result.createObjectStore("img"); }; rq.onsuccess = function () { res(rq.result); }; rq.onerror = function () { res(null); }; }
        catch (e) { res(null); }
      });
      return dbp;
    }
    async function tx(mode, fn) { var db = await open(); if (!db) return null; return await new Promise(function (res) { try { var t = db.transaction("img", mode), st = t.objectStore("img"), r = fn(st); t.oncomplete = function () { res(mode === "readonly" ? ((r && r.result) || null) : true); }; t.onerror = function () { res(null); }; } catch (e) { res(null); } }); }
    return {
      get: function (k) { return tx("readonly", function (s) { return s.get(k); }); },
      put: function (k, blob) { return tx("readwrite", function (s) { return s.put(blob, k); }); },
      del: function (k) { return tx("readwrite", function (s) { return s.delete(k); }); },
      keys: function () { return tx("readonly", function (s) { return s.getAllKeys(); }); }
    };
  })();
  var BLOBURL = {};
  async function userImageURL(id, k) {
    var key = id + "#" + k; if (BLOBURL[key]) return BLOBURL[key];
    var b = await IDB.get(key); if (!b || !(b instanceof Blob)) return null;
    BLOBURL[key] = URL.createObjectURL(b); return BLOBURL[key];
  }
  async function setUserImage(id, k, blob) {
    var key = id + "#" + k; if (BLOBURL[key]) { try { URL.revokeObjectURL(BLOBURL[key]); } catch (e) { } delete BLOBURL[key]; }
    if (blob) await IDB.put(key, blob); else await IDB.del(key);
  }

  /* lưu bản chỉnh (localStorage) + tác phẩm của anh */
  function lsGet(k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } }
  function lsSet(k, v) { try { if (v == null) localStorage.removeItem(k); else localStorage.setItem(k, JSON.stringify(v)); return true; } catch (e) { return false; } }
  var EDIT_FIELDS = ["title", "artist", "date", "medium", "where", "hook", "intro", "end", "trendLine", "steps", "img", "type", "y", "era", "place", "size", "status", "alt", "tags"];
  function getOverride(id) { return lsGet("av_edit_" + id, null); }
  function setOverride(id, o) { return lsSet("av_edit_" + id, o); }
  function listCustom() { return lsGet("av_my", []); }
  function saveCustom(w) { var a = listCustom().filter(function (x) { return x.id !== w.id; }); w.custom = true; a.unshift(w); return lsSet("av_my", a); }
  function deleteCustom(id) { lsSet("av_my", listCustom().filter(function (x) { return x.id !== id; })); setOverride(id, null); for (var k = 0; k < 8; k++) setUserImage(id, k, null); }
  // tác phẩm sau khi áp bản chỉnh của anh
  function resolve(w) {
    var o = clone(w), ov = getOverride(w.id);
    if (ov) EDIT_FIELDS.forEach(function (f) { if (ov[f] !== undefined) o[f] = ov[f]; });
    o.edited = !!ov; o.img = o.img || []; o.steps = o.steps || [];
    return o;
  }
  async function hasUserImage(id, k) { return !!(await IDB.get(id + "#" + k)); }

  /* ---------------- 2. lời đọc ---------------- */
  var DEF = { aspect: "9:16", res: 720, len: "full", pace: "mid", voice: "ai", rate: 1, music: "auto", musicVol: 0.5, trend: true, caps: true,
              qcard: true, nums: true, spot: true, credit: "Phạm Đăng Hiển · fb.com/lopmaybay", qr: true, qrUrl: "https://fb.com/lopmaybay", srcs: true, lang: "vi" };
  function loadOpts() { var o = {}, s = lsGet("av_opts", {}); for (var k in DEF) o[k] = (s && s[k] !== undefined) ? s[k] : DEF[k]; o.lang = "vi"; return o; }
  function saveOpts(O) { var c = {}; for (var k in O) if (k !== "trendText") c[k] = O[k]; lsSet("av_opts", c); }
  function musicFor(w, O) { if (O.music && O.music !== "auto") return O.music; return w.type === "painting" || w.type === "music" ? "zen" : "ngu"; }
  function trendLine(w, O) {
    if (O.trendText && String(O.trendText).trim()) return String(O.trendText).trim();
    if (w.trendLine) return w.trendLine;
    var noun = w.trend || typeOf(w.type).noun || "một tác phẩm";
    if (/^(nghe|đứng|ngồi|lắng)/.test(noun)) return "Giờ thì tôi mới hiểu vì sao người ta có thể dành hàng giờ " + noun + "…";
    return "Giờ thì tôi mới hiểu vì sao người ta có thể dành hàng giờ ngắm nhìn " + noun + "…";
  }
  function sentencesOf(text) { return SAY.sentences(String(text || "")).map(function (x) { return x.t; }).filter(Boolean); }
  function shortAnswer(st) { if (st.s) return st.s; var ss = sentencesOf(st.a), out = ss[0] || ""; if (out.length < 70 && ss[1]) out += " " + ss[1]; return out; }
  function pickSteps(w, O) {
    var all = (w.steps || []).map(function (s, i) { var c = clone(s); c.n = i; return c; });
    if (O.len !== "short") return all;
    var k = all.filter(function (s) { return s.k; });
    if (k.length < 3) k = all.slice(0, Math.min(4, all.length));   // chưa đánh dấu: lấy 4 chi tiết đầu
    return k.slice(0, 6);
  }
  // cách đọc cho giọng Việt: tên riêng nước ngoài viết theo âm Việt (chỉ dùng khi ĐỌC, phụ đề giữ nguyên chữ gốc)
  var PRON = [[/\bParis\b/g, "Pa-ri"], [/\bPraha\b/g, "Pra-ha"], [/\bPaul Zetter\b/g, "Pôn Dét-tơ"], [/\bCaroline Fry\b/g, "Ca-rô-lin Phrai"], [/\bMona Lisa\b/g, "Mô-na Li-da"],
              [/\bFukuoka\b/g, "Phu-cu-ô-ca"], [/\bfranc\b/g, "phrăng"], [/\bminuet\b/g, "mi-nu-ét"], [/\bUNESCO\b/g, "U-nét-xcô"], [/\bCông nguyên\b/g, "Công nguyên"]];
  function speakable(c) { var t = String(c || ""); PRON.forEach(function (p) { t = t.replace(p[0], p[1]); }); return t; }
  function narrate(w, O, steps) {
    var NR = {}, ctx = { lang: "vi", ru: false };
    // chỉ dùng giọng Việt cho video giải mã (không tải thêm giọng Nga/Anh): đoạn bị nhận nhầm là tiếng nước ngoài thì đọc bằng chữ gốc
    function sent(c) { var segs = SAY.segs(speakable(c), ctx).map(function (g) { return g.l === "vi" ? g : { l: "vi", t: (g.o != null && g.o !== "") ? g.o : g.t }; }); return { c: c, segs: L.mergeSegs(segs) }; }
    function many(text) { return sentencesOf(text).map(sent); }
    if (O.trend) NR.trend = [sent(trendLine(w, O).replace(/…$/, "."))];
    NR.hook = many(w.hook || "");
    var info = w.intro || (w.title + (w.artist ? ", " + w.artist : "") + (w.date ? ", " + w.date : "") + ".");
    if (O.len !== "short") NR.info = many(info);          // bản ngắn: thẻ tên tác phẩm hiện im lặng, không đọc
    steps.forEach(function (st, i) {
      NR["q:" + i] = many(st.q || "");
      NR["a:" + i] = many(O.len === "short" ? shortAnswer(st) : (st.a || ""));
    });
    NR.end = many(w.end || ("Giờ thì bạn đã hiểu vì sao người ta có thể ngắm " + w.title + " hàng giờ."));
    var out = [];
    if (O.qr && O.qrUrl) out.push(sent("Theo dõi để xem những tác phẩm tiếp theo nhé."));
    NR.outro = out;
    Object.keys(NR).forEach(function (k) { if (!NR[k].length) delete NR[k]; });
    return NR;
  }

  /* ---------------- 3. ảnh của video: tải + khung cắt + nền mờ ---------------- */
  async function loadWorkImages(w, onProg) {
    var res = [], n = w.img.length;
    for (var k = 0; k < n; k++) {
      var d = w.img[k], el = null, src = "";
      var uu = await userImageURL(w.id, k);
      if (uu) { el = await loadOne(uu); src = "user"; }
      if (!el && d.file) { el = await loadCands(commonsCands(d)); src = "commons"; }
      if (onProg) onProg(k + 1, n);
      res.push(prepImage(el, d, src));
    }
    return res;
  }
  function prepImage(el, d, src) {
    if (!el) return { ok: false, d: d };
    var W = el.naturalWidth || el.width, H = el.naturalHeight || el.height, c = d.crop || [0, 0, 1, 1];
    var r = { ok: true, el: el, W: W, H: H, x0: c[0] * W, y0: c[1] * H, cw: c[2] * W, ch: c[3] * H, d: d, src: src };
    // nền mờ: thu nhỏ còn ~48 px rồi phóng to là thành nhoè mịn
    var bw = 48, bh = Math.max(8, Math.round(bw * r.ch / r.cw)), bc = document.createElement("canvas"); bc.width = bw; bc.height = bh;
    var bx = bc.getContext("2d"); bx.imageSmoothingQuality = "high"; bx.drawImage(el, r.x0, r.y0, r.cw, r.ch, 0, 0, bw, bh);
    r.blur = bc;
    return r;
  }

  /* ---------------- 4. máy quay ---------------- */
  // view = { k: số ảnh, cx, cy, w } (đơn vị: điểm ảnh gốc); chiều cao = w / FA
  function fullView(I, k, FA) { var m = I[k]; if (!m || !m.ok) return { k: k, cx: 0, cy: 0, w: 1, none: true }; return { k: k, cx: m.x0 + m.cw / 2, cy: m.y0 + m.ch / 2, w: Math.max(m.cw, m.ch * FA) }; }
  // Khung an toàn: vùng màn hình KHÔNG bị thẻ câu hỏi (trên) và phụ đề (dưới) che — chi tiết được đặt vào giữa vùng này
  var MC = null;
  function measureCtx() { if (!MC) MC = document.createElement("canvas").getContext("2d"); return MC; }
  function qCardBottom(Ly, text, small) {
    var u = Ly.u, px = (small ? 25 : 31) * u, mc = measureCtx(); mc.font = F(800, px);
    return Ly.qY + 54 * u + wrap(mc, text || "", Ly.qW - 44 * u, 4).length * px * 1.28;
  }
  function safeRects(W, H, O, st) {
    var Ly = LY(W, H), u = Ly.u, gap = 24 * u, top = 0.05 * H;
    if (O.qcard) top = Math.max(qCardBottom(Ly, st.q, false), qCardBottom(Ly, st.q, true) + (st.tag ? 49 * u : 0)) + gap;
    else if (st.tag) top = Ly.qY + 49 * u + gap;
    var bot = O.caps ? Ly.capY - (3 * 27 * u * 1.32 + 0.7 * 27 * u) / 2 - 12 * u : H - 34 * u;
    var mx = (Ly.port || Ly.sq ? 0.035 : 0.03) * W, A = { x0: mx, y0: top, x1: W - mx, y1: bot };
    if (A.y1 - A.y0 < H * 0.28) A.y0 = A.y1 - H * 0.28;                 // câu hỏi quá dài: chấp nhận che bớt
    var out = [A];
    if (!Ly.port && !Ly.sq && O.qcard) out.push({ x0: Ly.qX + Ly.qW + 0.025 * W, y0: 0.06 * H, x1: W - mx, y1: bot, side: true });  // ngang: chi tiết đứng bên phải thẻ câu hỏi
    return out;
  }
  // tâm view theo 1 trục: đưa tâm chi tiết về tâm vùng an toàn, nhưng mép ảnh không được lùi vào trong vùng an toàn
  function axisCenter(want, a0, a1, k, S, s0, s1) {
    var lo = a0 + (S / 2 - s0) / k, hi = a1 - (s1 - S / 2) / k;
    if (lo > hi) return (a0 + a1) / 2 - ((s0 + s1) / 2 - S / 2) / k;   // ảnh nhỏ hơn vùng an toàn: đặt giữa vùng
    return clamp(want, lo, hi);
  }
  function boxView(I, k, b, FA, W, H, rects) {
    var m = I[k]; if (!m || !m.ok) return fullView(I, k, FA);
    var bx = m.x0 + b[0] * m.cw, by = m.y0 + b[1] * m.ch, bw = b[2] * m.cw, bh = b[3] * m.ch;
    var area = b[2] * b[3], pad = area > 0.5 ? 1.04 : area > 0.15 ? 1.14 : 1.26;
    var kFull = Math.min(W / m.cw, H / m.ch), best = null;
    (rects && rects.length ? rects : [{ x0: 0, y0: 0, x1: W, y1: H }]).forEach(function (R, ri) {
      var sw = R.x1 - R.x0, sh = R.y1 - R.y0, kFit = Math.min(sw / (bw * pad), sh / (bh * pad));
      var kk = Math.min(Math.max(kFit, kFull * 0.5), Math.max(3.0, kFull));   // ≤ 3 lần điểm ảnh gốc; không nhỏ hơn nửa «cả bức»
      var score = Math.min(kFit, 3.0) * (R.side ? 0.8 : 1);                  // chọn vùng chứa trọn chi tiết to nhất; ưu tiên vùng dưới thẻ câu hỏi
      if (!best || score > best.score) best = { R: R, k: kk, score: score };
    });
    var R = best.R, kk = best.k, ax = (R.x0 + R.x1) / 2, ay = (R.y0 + R.y1) / 2;
    var cx = axisCenter(bx + bw / 2 - (ax - W / 2) / kk, m.x0, m.x0 + m.cw, kk, W, R.x0, R.x1);
    var cy = axisCenter(by + bh / 2 - (ay - H / 2) / kk, m.y0, m.y0 + m.ch, kk, H, R.y0, R.y1);
    return { k: k, cx: cx, cy: cy, w: W / kk, box: [bx, by, bw, bh] };
  }
  function camLerp(a, b, u) {
    if (a.k !== b.k || a.none || b.none) return u < 0.5 ? a : b;
    var la = Math.log(a.w), lb = Math.log(b.w), d = Math.hypot(b.cx - a.cx, b.cy - a.cy), wm = Math.max(a.w, b.w);
    var bump = clamp(d / wm - 0.35, 0, 1.4) * 0.5;
    return { k: a.k, cx: lerp(a.cx, b.cx, u), cy: lerp(a.cy, b.cy, u), w: Math.exp(lerp(la, lb, u) + bump * Math.sin(Math.PI * u)) };
  }
  function drift(v, amt) { return { k: v.k, cx: v.cx, cy: v.cy, w: v.w * (1 - amt), box: v.box, none: v.none }; }

  /* ---------------- 5. dựng cảnh ---------------- */
  function readSec(chars) { return chars / 14.5 + 0.35; }
  function build(w, O, W, H, NR, AP, I) {
    var FA = W / H, pace = O.pace === "fast" ? 0.8 : O.pace === "slow" ? 1.3 : 1, steps = pickSteps(w, O), scenes = [], tt = 0;
    var k0 = 0; for (var q = 0; q < I.length; q++) if (I[q] && I[q].ok) { k0 = q; break; }
    function push(sc) { sc.t0 = tt; tt += sc.dur; sc.idx = scenes.length; scenes.push(sc); return sc; }
    function voiced(sc, lead, tail, minDur) {
      sc.narr = NR[sc.key] || []; sc.lead = lead;
      var ap = AP && AP.scenes && AP.scenes[sc.key];
      if (ap && ap.dur > 0) {
        sc.dur = Math.max(minDur || 0, sc.fly || 0, lead + ap.dur + tail); sc.ap = ap;
        sc.sentT = ap.sents.map(function (x) { return { t0: lead + x.t0, t1: lead + x.t1 }; });
      } else {
        var t = lead; sc.sentT = sc.narr.map(function (s) { var d = readSec((s.c || "").length) * pace, r = { t0: t, t1: t + d }; t = r.t1 + 0.3; return r; });
        sc.dur = Math.max(minDur || 0, sc.fly || 0, t - 0.3 + tail);
      }
      return sc;
    }
    var vFull = fullView(I, k0, FA), last = vFull;
    if (O.trend && NR.trend) push(voiced({ key: "trend", type: "trend", A: vFull, B: drift(vFull, 0.02) }, 0.55, 0.9, 4.2 * pace));
    push(voiced({ key: "hook", type: "hook", A: drift(vFull, 0.02), B: drift(vFull, 0.06) }, 0.3, 0.7, 3.8));
    push(voiced({ key: "info", type: "info", A: drift(vFull, 0.06), B: drift(vFull, 0.09) }, 0.45, 1.1, (O.len === "short" ? 3.2 : 4.6) * pace));
    last = drift(vFull, 0.09);
    steps.forEach(function (st, i) {
      var k = st.i || 0, isCard = !!st.card || !I[k] || !I[k].ok, target = isCard ? last : boxView(I, k, st.b || [0, 0, 1, 1], FA, W, H, safeRects(W, H, O, st));
      var dist = isCard ? 0 : (last.k !== target.k ? 1.5 : Math.hypot(target.cx - last.cx, target.cy - last.cy) / Math.max(target.w, last.w) + Math.abs(Math.log(target.w / last.w)));
      var fly = isCard ? 0.6 : clamp(1.0 + 0.55 * dist, 1.1, 2.4) * pace;
      var qs = push(voiced({ key: "q:" + i, type: "q", st: st, num: i + 1, of: steps.length, card: isCard, A: last, B: target, fly: fly, xfade: !isCard && last.k !== target.k }, Math.min(0.5, fly * 0.4), 0.75, fly + 0.4));
      var as = push(voiced({ key: "a:" + i, type: "a", st: st, num: i + 1, of: steps.length, card: isCard, A: target, B: isCard ? target : drift(target, 0.05) }, 0.12, 0.5, 2.2));
      as.qs = qs; if (!isCard) last = as.B;
    });
    var endV = vFull;
    var sh = O.len === "short";
    push(voiced({ key: "end", type: "end", A: last, B: drift(endV, 0.03), fly: 1.7 * pace, xfade: last.k !== endV.k, steps: steps }, sh ? 1.1 : 1.3, sh ? 1.0 : 1.4, sh ? 4.5 : 5.5));
    push(voiced({ key: "outro", type: "outro", A: drift(endV, 0.03), B: drift(endV, 0.05) }, 0.6, 0.6, (O.qr && O.qrUrl ? (sh ? 5.2 : 6.2) : 4.2)));
    var V = { scenes: scenes, total: tt, W: W, H: H, FA: FA, O: O, w: w, I: I, NR: NR, AP: AP || null, steps: steps, k0: k0 };
    V.render = renderArt; V.preload = function () { return Promise.resolve({}); }; V.ensure = function () { return Promise.resolve(); };
    return V;
  }
  function sceneAt(V, t) { var sc = V.scenes, lo = 0, hi = sc.length - 1; if (t <= 0) return 0; if (t >= V.total) return hi; while (lo < hi) { var m = (lo + hi + 1) >> 1; if (sc[m].t0 <= t) lo = m; else hi = m - 1; } return lo; }
  function camOf(sc, tau) {
    var fly = sc.fly || 0;
    if (fly && tau < fly) { var u = ease(tau / fly); return { v: camLerp(sc.A, sc.B, u), fade: sc.xfade ? u : -1, A: sc.A, B: sc.B }; }
    var h = seg(tau, fly, sc.dur), a = sc.fly ? sc.B : sc.A;
    if (!sc.fly) return { v: camLerp(sc.A, sc.B, ease(h) * 0.999 + 0.0005), fade: -1 };
    return { v: { k: a.k, cx: a.cx, cy: a.cy, w: a.w }, fade: -1 };
  }
  function sentIdx(sc, tau) { var st = sc.sentT; if (!st) return -1; for (var i = st.length - 1; i >= 0; i--) if (tau >= st[i].t0 - 0.05) return i; return -1; }

  /* ---------------- 6. vẽ khung hình ---------------- */
  function LY(W, H) {
    var port = H > W * 1.2, sq = !port && H > W * 0.9, u = Math.min(W, H) / 720;
    return { port: port, sq: sq, u: u, pad: Math.round((port ? 0.06 : 0.045) * W), capY: port ? H * 0.80 : H * 0.84, capW: W * (port ? 0.88 : 0.74),
             qY: port ? H * 0.085 : sq ? H * 0.05 : H * 0.07, qW: port ? W * 0.88 : sq ? W * 0.92 : W * 0.56, qX: port ? W * 0.06 : W * 0.04 };
  }
  function drawImageView(ctx, V, v, alpha) {
    var m = V.I[v.k]; if (!m || !m.ok || v.none) return null;
    var W = V.W, H = V.H, k = W / v.w, dx = W / 2 - v.cx * k, dy = H / 2 - v.cy * k;
    ctx.save(); ctx.globalAlpha = alpha == null ? 1 : alpha;
    // nền mờ phủ kín khung (thấy khi ảnh không lấp đầy khung)
    var cw = m.cw * k, ch = m.ch * k, ix = dx + m.x0 * k, iy = dy + m.y0 * k;
    if (ix > 0.5 || iy > 0.5 || ix + cw < W - 0.5 || iy + ch < H - 0.5) {
      var s = Math.max(W / m.blur.width, H / m.blur.height) * 1.08;
      ctx.imageSmoothingEnabled = true; ctx.imageSmoothingQuality = "high";
      ctx.drawImage(m.blur, (W - m.blur.width * s) / 2, (H - m.blur.height * s) / 2, m.blur.width * s, m.blur.height * s);
      ctx.fillStyle = "rgba(6,10,18,0.55)"; ctx.fillRect(0, 0, W, H);
      // bóng đổ quanh tác phẩm
      ctx.shadowColor = "rgba(0,0,0,0.55)"; ctx.shadowBlur = 30 * (W / 720); ctx.fillStyle = "#000";
      ctx.fillRect(dx + m.x0 * k, dy + m.y0 * k, cw, ch); ctx.shadowBlur = 0;
    }
    ctx.imageSmoothingEnabled = true; ctx.imageSmoothingQuality = "high";
    ctx.beginPath(); ctx.rect(dx + m.x0 * k, dy + m.y0 * k, cw, ch); ctx.clip();
    ctx.drawImage(m.el, dx, dy, m.W * k, m.H * k);
    ctx.restore();
    return { k: k, dx: dx, dy: dy };
  }
  function toScreen(V, v, box) { var k = V.W / v.w; return { x: V.W / 2 + (box[0] - v.cx) * k, y: V.H / 2 + (box[1] - v.cy) * k, w: box[2] * k, h: box[3] * k }; }
  function boxPx(V, st) { var m = V.I[st.i || 0]; if (!m || !m.ok || !st.b) return null; return [m.x0 + st.b[0] * m.cw, m.y0 + st.b[1] * m.ch, st.b[2] * m.cw, st.b[3] * m.ch]; }
  // đường viền bo góc KHÔNG mở path mới (để khoét lỗ bằng evenodd)
  function rrp(ctx, x, y, w, h, r) { r = Math.max(0, Math.min(r, w / 2, h / 2)); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath(); }
  function vignette(ctx, W, H, a) {
    var g = ctx.createRadialGradient(W / 2, H / 2, Math.min(W, H) * 0.35, W / 2, H / 2, Math.max(W, H) * 0.75);
    g.addColorStop(0, "rgba(0,0,0,0)"); g.addColorStop(1, "rgba(0,0,0," + a + ")"); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  }
  function spotlight(ctx, V, r, a, num, prog) {
    var W = V.W, H = V.H, cover = (r.w * r.h) / (W * H);
    if (a <= 0.01) return;
    var rad = Math.min(18 * (W / 720), r.w / 6, r.h / 6);
    if (cover < 0.62) {
      ctx.save(); ctx.fillStyle = "rgba(3,6,12," + (0.56 * a) + ")"; ctx.beginPath(); ctx.rect(0, 0, W, H);
      rrp(ctx, r.x, r.y, r.w, r.h, rad); ctx.fill("evenodd"); ctx.restore();
    }
    // góc khung vàng (kiểu ống ngắm) + viền mảnh, vẽ dần theo prog
    var u = W / 720, L1 = Math.min(r.w, r.h) * 0.22 * clamp(prog * 1.6, 0, 1), lw = Math.max(2, 3.2 * u);
    ctx.save(); ctx.strokeStyle = GOLD; ctx.lineWidth = lw; ctx.lineCap = "round"; ctx.globalAlpha = a; ctx.shadowColor = "rgba(242,193,78,0.85)"; ctx.shadowBlur = 12 * u;
    var x0 = Math.max(lw, r.x), y0 = Math.max(lw, r.y), x1 = Math.min(W - lw, r.x + r.w), y1 = Math.min(H - lw, r.y + r.h);
    if (L1 > 1) {
      ctx.beginPath();
      ctx.moveTo(x0, y0 + L1); ctx.lineTo(x0, y0); ctx.lineTo(x0 + L1, y0);
      ctx.moveTo(x1 - L1, y0); ctx.lineTo(x1, y0); ctx.lineTo(x1, y0 + L1);
      ctx.moveTo(x1, y1 - L1); ctx.lineTo(x1, y1); ctx.lineTo(x1 - L1, y1);
      ctx.moveTo(x0 + L1, y1); ctx.lineTo(x0, y1); ctx.lineTo(x0, y1 - L1);
      ctx.stroke();
    }
    if (cover < 0.62) { ctx.shadowBlur = 0; ctx.globalAlpha = a * 0.45 * clamp(prog * 2 - 0.4, 0, 1); ctx.lineWidth = Math.max(1, 1.2 * u); rr(ctx, x0, y0, x1 - x0, y1 - y0, rad); ctx.stroke(); }
    ctx.restore();
    if (num && V.O.nums && cover < 0.62) {
      var R = 17 * u, cx = clamp(x0, R + 4, W - R - 4), cy = clamp(y0, R + 4, H - R - 4), s = easeOut(clamp(prog * 2, 0, 1));
      ctx.save(); ctx.globalAlpha = a; ctx.translate(cx, cy); ctx.scale(s, s);
      ctx.fillStyle = GOLD; ctx.beginPath(); ctx.arc(0, 0, R, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = NAVY; ctx.font = F(900, R * 1.1); ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText(String(num), 0, R * 0.06);
      ctx.restore();
    }
  }
  function panel(ctx, x, y, w, h, r, fill) { ctx.save(); ctx.fillStyle = fill || "rgba(10,18,32,0.82)"; rr(ctx, x, y, w, h, r); ctx.fill(); ctx.restore(); }
  // phụ đề sáng dần theo lời đọc (karaoke)
  function caption(ctx, V, text, p, y, maxW, px, opts) {
    opts = opts || {};
    ctx.save(); ctx.font = F(opts.weight || 700, px); var lines = wrap(ctx, text, maxW, 0), lh = px * 1.32;
    var maxL = opts.maxLines || 3, total = text.length, said = Math.floor(total * clamp(p, 0, 1));
    // cửa sổ trượt khi câu dài hơn số dòng tối đa
    var startL = 0; if (lines.length > maxL) { var acc = 0, cur = 0; for (var i = 0; i < lines.length; i++) { acc += lines[i].length + 1; if (acc >= said) { cur = i; break; } cur = i; } startL = clamp(cur - (maxL - 2), 0, lines.length - maxL); }
    var shown = lines.slice(startL, startL + maxL), bw = 0; shown.forEach(function (l) { bw = Math.max(bw, ctx.measureText(l).width); });
    var bh = shown.length * lh + px * 0.7, bx = V.W / 2 - bw / 2 - px * 0.55, by = y - bh / 2;
    if (opts.box !== false) panel(ctx, bx, by, bw + px * 1.1, bh, px * 0.45, "rgba(8,14,26," + (opts.boxA || 0.66) + ")");
    var before = 0; for (var j = 0; j < startL; j++) before += lines[j].length + 1;
    ctx.textAlign = "left"; ctx.textBaseline = "middle";
    shown.forEach(function (l, i) {
      var lx = V.W / 2 - ctx.measureText(l).width / 2, ly = by + px * 0.35 + lh * (i + 0.5);
      ctx.fillStyle = "#ffffff"; ctx.shadowColor = "rgba(0,0,0,0.6)"; ctx.shadowBlur = 4; ctx.fillText(l, lx, ly); ctx.shadowBlur = 0;
      var k = clamp(said - before, 0, l.length);
      if (k > 0 && opts.karaoke !== false) { var sw = ctx.measureText(l.slice(0, k)).width; ctx.save(); ctx.beginPath(); ctx.rect(lx - 2, ly - lh / 2, sw + 2, lh); ctx.clip(); ctx.fillStyle = GOLD; ctx.fillText(l, lx, ly); ctx.restore(); }
      before += l.length + 1;
    });
    ctx.restore();
    return { y0: by, y1: by + bh };
  }
  function sentProgress(sc, tau, i) { var st = sc.sentT && sc.sentT[i]; if (!st) return 1; return clamp((tau - st.t0) / Math.max(0.3, st.t1 - st.t0), 0, 1); }
  function currentCaption(sc, tau) { var i = sentIdx(sc, tau); if (i < 0 || !sc.narr[i]) return null; var st = sc.sentT[i]; if (tau > st.t1 + 0.6 && i === sc.narr.length - 1) return null; return { text: sc.narr[i].c, p: sentProgress(sc, tau, i) }; }

  function renderArt(ctx, V, t) {
    var W = V.W, H = V.H, O = V.O, Ly = LY(W, H), u = Ly.u, i = sceneAt(V, t), sc = V.scenes[i], tau = t - sc.t0;
    ctx.save(); ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, W, H);
    var cam = camOf(sc, tau), v = cam.v;
    // ảnh: chuyển ảnh thì hoà dần
    if (cam.fade >= 0 && cam.A && cam.B && cam.A.k !== cam.B.k) { drawImageView(ctx, V, cam.A, 1); drawImageView(ctx, V, { k: cam.B.k, cx: cam.B.cx, cy: cam.B.cy, w: cam.B.w * (1 + 0.06 * (1 - cam.fade)) }, cam.fade); }
    else if (!drawImageView(ctx, V, v, 1)) drawMissing(ctx, V);
    vignette(ctx, W, H, 0.38);
    var T = sc.type;
    if (T === "trend") drawTrend(ctx, V, sc, tau, Ly);
    else if (T === "hook") { var c = currentCaption(sc, tau); if (c) caption(ctx, V, c.text, c.p, H * (Ly.port ? 0.5 : 0.5), Ly.capW, 34 * u, { weight: 800, maxLines: 5, boxA: 0.5 }); }
    else if (T === "info") drawInfo(ctx, V, sc, tau, Ly);
    else if (T === "q" || T === "a") drawStep(ctx, V, sc, tau, Ly, cam);
    else if (T === "end") drawEnd(ctx, V, sc, tau, Ly, cam);
    else if (T === "outro") drawOutro(ctx, V, sc, tau, Ly);
    // chữ ký góc + thanh tiến độ
    if (O.credit && T !== "outro") { ctx.save(); ctx.font = F(700, 15 * u); ctx.fillStyle = "rgba(255,255,255,0.72)"; ctx.textAlign = "right"; ctx.textBaseline = "bottom"; ctx.shadowColor = "rgba(0,0,0,0.7)"; ctx.shadowBlur = 4; ctx.fillText("✦ " + O.credit, W - Ly.pad * 0.6, H - 10 * u); ctx.restore(); }
    ctx.fillStyle = "rgba(255,255,255,0.14)"; ctx.fillRect(0, H - 4 * u, W, 4 * u); ctx.fillStyle = GOLD; ctx.fillRect(0, H - 4 * u, W * clamp(t / V.total, 0, 1), 4 * u);
    ctx.restore();
  }
  function drawMissing(ctx, V) {
    var W = V.W, H = V.H, u = Math.min(W, H) / 720, g = ctx.createLinearGradient(0, 0, W, H); g.addColorStop(0, "#1b2f52"); g.addColorStop(1, "#0b1424");
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    ctx.save(); ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillStyle = "rgba(255,255,255,0.18)"; ctx.font = F(400, 160 * u); ctx.fillText(typeOf(V.w.type).icon, W / 2, H * 0.36);
    ctx.fillStyle = "rgba(255,255,255,0.75)"; ctx.font = F(800, 26 * u); ctx.fillText(V.w.img.some(function (d) { return d.user; }) ? "📂 Hãy nạp ảnh của anh cho tác phẩm này" : "Chưa tải được ảnh", W / 2, H * 0.5);
    ctx.restore();
  }
  // hiện từng chữ (từ) một
  function wordsReveal(ctx, lines, x, y, lh, p, align) {
    var total = 0; lines.forEach(function (l) { total += l.split(" ").length; });
    var shown = p * total, gi = 0;
    ctx.textAlign = "left";
    lines.forEach(function (l, k) {
      var lw = ctx.measureText(l).width, sx = align === "center" ? x - lw / 2 : x, parts = l.split(" "), acc = "";
      parts.forEach(function (wd, j) {
        if (j) acc += " "; var before = ctx.measureText(acc).width; acc += wd;
        var a = clamp(shown - gi, 0, 1); gi++; if (a <= 0) return;
        ctx.save(); ctx.globalAlpha *= a; ctx.fillText(wd, sx + before, y + k * lh + (1 - a) * lh * 0.25); ctx.restore();
      });
    });
  }
  function drawTrend(ctx, V, sc, tau, Ly) {
    var W = V.W, H = V.H, u = Ly.u, line = trendLine(V.w, V.O), a = seg(tau, 0.1, 0.6) * (1 - seg(tau, sc.dur - 0.45, sc.dur));
    ctx.save(); ctx.globalAlpha = a;
    var g = ctx.createLinearGradient(0, H * 0.2, 0, H * 0.8); g.addColorStop(0, "rgba(4,7,14,0)"); g.addColorStop(0.3, "rgba(4,7,14,0.72)"); g.addColorStop(0.7, "rgba(4,7,14,0.72)"); g.addColorStop(1, "rgba(4,7,14,0)");
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    var m = line.match(/^(Giờ thì tôi mới hiểu)\s*(.*)$/i), head = m ? m[1].toUpperCase() : "", rest = m ? m[2] : line;
    var maxW = W * (Ly.port || Ly.sq ? 0.86 : 0.7), y = H * 0.4;
    if (head) { ctx.font = F(900, (Ly.port ? 46 : 52) * u); var hl = wrap(ctx, head, maxW, 2); ctx.fillStyle = GOLD; ctx.textBaseline = "middle"; wordsReveal(ctx, hl, W / 2, y, 56 * u, seg(tau, 0.2, 1.0), "center"); y += hl.length * 56 * u + 18 * u; }
    ctx.font = FS(700, (Ly.port ? 36 : 40) * u, true); var rl = wrap(ctx, rest, maxW, 4); ctx.fillStyle = "#ffffff"; ctx.textBaseline = "middle";
    var ip = sc.sentT && sc.sentT[0] ? clamp((tau - sc.sentT[0].t0) / Math.max(0.5, sc.sentT[0].t1 - sc.sentT[0].t0), 0, 1) : seg(tau, 0.6, sc.dur * 0.7);
    wordsReveal(ctx, rl, W / 2, y + 10 * u, 46 * u, Math.max(seg(tau, 0.9, 2.2), ip * 1.2), "center");
    ctx.restore();
  }
  function chip(ctx, x, y, text, px, fill, color, align) {
    ctx.save(); ctx.font = F(800, px); var tw = ctx.measureText(text).width, w = tw + px * 1.2, h = px * 1.75, xx = align === "right" ? x - w : align === "center" ? x - w / 2 : x;
    ctx.fillStyle = fill; rr(ctx, xx, y, w, h, h / 2); ctx.fill(); ctx.fillStyle = color; ctx.textBaseline = "middle"; ctx.textAlign = "left"; ctx.fillText(text, xx + px * 0.6, y + h / 2 + px * 0.04);
    ctx.restore(); return { w: w, h: h, x: xx };
  }
  function drawInfo(ctx, V, sc, tau, Ly) {
    var W = V.W, H = V.H, u = Ly.u, w = V.w, a = easeOut(seg(tau, 0.15, 0.85)), out = 1 - seg(tau, sc.dur - 0.4, sc.dur);
    var x = Ly.pad, maxW = W - Ly.pad * 2, t = typeOf(w.type);
    ctx.save(); ctx.globalAlpha = a * out;
    ctx.font = FS(800, (Ly.port ? 44 : 46) * u); var tl = wrap(ctx, w.title, maxW - 30 * u, 3);
    ctx.font = F(600, 21 * u); var meta = [w.artist, w.date].filter(Boolean).join(" · "), ml = wrap(ctx, meta, maxW - 30 * u, 2);
    var sub = [w.medium, w.where].filter(Boolean).join(" · "); ctx.font = F(500, 18 * u); var sl = wrap(ctx, sub, maxW - 30 * u, 3);
    var h = 40 * u + tl.length * 50 * u + ml.length * 27 * u + sl.length * 24 * u + 30 * u, y = (Ly.port ? H * 0.64 : H * 0.6) - h / 2 + (1 - a) * 40 * u;
    panel(ctx, x, y, maxW, h, 22 * u, "rgba(9,16,30,0.84)");
    ctx.fillStyle = GOLD; ctx.fillRect(x, y + 22 * u, 5 * u, h - 44 * u);
    chip(ctx, x + 18 * u, y - 18 * u, t.icon + " " + t.vi, 17 * u, GOLD, NAVY);
    var yy = y + 38 * u; ctx.textBaseline = "middle"; ctx.textAlign = "left";
    ctx.font = FS(800, (Ly.port ? 44 : 46) * u); ctx.fillStyle = "#fff"; tl.forEach(function (l) { ctx.fillText(l, x + 22 * u, yy + 12 * u); yy += 50 * u; });
    ctx.font = F(700, 21 * u); ctx.fillStyle = GOLD; ml.forEach(function (l) { ctx.fillText(l, x + 22 * u, yy + 4 * u); yy += 27 * u; });
    ctx.font = F(500, 18 * u); ctx.fillStyle = "rgba(255,255,255,0.82)"; sl.forEach(function (l) { ctx.fillText(l, x + 22 * u, yy + 4 * u); yy += 24 * u; });
    ctx.restore();
    var c = currentCaption(sc, tau); if (c && V.O.caps) caption(ctx, V, c.text, c.p, Ly.capY + 30 * u, Ly.capW, 25 * u, { maxLines: 2 });
  }
  function drawCard(ctx, V, st, a, Ly) {
    var W = V.W, H = V.H, u = Ly.u;
    ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = "rgba(5,9,17,0.72)"; ctx.fillRect(0, 0, W, H);
    var big = st.card.big || "", sub = st.card.sub || "", cy = H * (Ly.port ? 0.44 : 0.46);
    var bpx = (big.length <= 4 ? 150 : big.length <= 8 ? 96 : 60) * u; ctx.font = FS(800, bpx); ctx.textAlign = "center"; ctx.textBaseline = "middle";
    var bl = wrap(ctx, big, W * 0.84, 3); ctx.fillStyle = GOLD; ctx.shadowColor = "rgba(242,193,78,0.45)"; ctx.shadowBlur = 24 * u;
    bl.forEach(function (l, i) { ctx.fillText(l, W / 2, cy - (bl.length - 1) * bpx * 0.55 + i * bpx * 1.1); }); ctx.shadowBlur = 0;
    if (sub) { ctx.font = FS(700, 30 * u, true); ctx.fillStyle = "rgba(255,255,255,0.9)"; wrap(ctx, sub, W * 0.8, 2).forEach(function (l, i) { ctx.fillText(l, W / 2, cy + bl.length * bpx * 0.62 + 30 * u + i * 38 * u); }); }
    ctx.restore();
  }
  function drawQuestion(ctx, V, sc, text, p, Ly, alpha, small) {
    var W = V.W, u = Ly.u, px = (small ? 25 : 31) * u;
    ctx.save(); ctx.globalAlpha = alpha; ctx.font = F(800, px);
    var lines = wrap(ctx, text, Ly.qW - 44 * u, 4), lh = px * 1.28, h = 54 * u + lines.length * lh, x = Ly.qX, y = Ly.qY;
    panel(ctx, x, y, Ly.qW, h, 20 * u, "rgba(12,24,46,0.86)");
    ctx.strokeStyle = "rgba(242,193,78,0.55)"; ctx.lineWidth = 1.5 * u; rr(ctx, x, y, Ly.qW, h, 20 * u); ctx.stroke();
    ctx.font = F(900, 16 * u); ctx.fillStyle = GOLD; ctx.textAlign = "left"; ctx.textBaseline = "middle";
    ctx.fillText("❓ CHI TIẾT " + sc.num + "/" + sc.of, x + 22 * u, y + 24 * u);
    // chấm tiến độ
    for (var d = 0; d < sc.of && sc.of <= 14; d++) { ctx.beginPath(); ctx.arc(x + Ly.qW - 22 * u - (sc.of - 1 - d) * 13 * u, y + 24 * u, 4 * u, 0, Math.PI * 2); ctx.fillStyle = d < sc.num ? GOLD : "rgba(255,255,255,0.28)"; ctx.fill(); }
    ctx.font = F(800, px); ctx.fillStyle = "#fff";
    var total = text.length, shown = Math.floor(total * clamp(p, 0, 1)), acc = 0;
    lines.forEach(function (l, i) { var k = clamp(shown - acc, 0, l.length); if (k > 0) ctx.fillText(l.slice(0, k), x + 22 * u, y + 46 * u + lh * (i + 0.5)); acc += l.length + 1; });
    ctx.restore();
    return y + h;
  }
  function drawStep(ctx, V, sc, tau, Ly, cam) {
    var W = V.W, H = V.H, u = Ly.u, st = sc.st, O = V.O, qs = sc.type === "q" ? sc : sc.qs;
    var bp = boxPx(V, st);
    if (sc.card) {
      var ca = sc.type === "q" ? seg(tau, 0.05, 0.6) : 1; if (st.card) drawCard(ctx, V, st, ca, Ly);
    } else if (bp && O.spot) {
      var r = toScreen(V, cam.v, bp), fly = sc.fly || 0;
      var a = sc.type === "q" ? seg(tau, fly * 0.7, fly + 0.3) : 1, prog = sc.type === "q" ? seg(tau, fly * 0.6, fly + 0.9) : 1;
      if (sc.type === "a") a = 1 - 0.0 * seg(tau, sc.dur - 0.4, sc.dur);
      spotlight(ctx, V, r, a, sc.num, prog);
    }
    var qBottom = Ly.qY;
    if (O.qcard) {
      var qtext = (st.q || "");
      var qp = sc.type === "q" ? (qs.sentT && qs.sentT.length ? clamp((tau - qs.sentT[0].t0) / Math.max(0.4, qs.sentT[qs.sentT.length - 1].t1 - qs.sentT[0].t0) * 1.15, 0, 1) : seg(tau, 0.2, 0.2 + qtext.length / 22)) : 1;
      var qa = sc.type === "q" ? seg(tau, 0.0, 0.35) : 1 - 0.25 * seg(tau, 0.2, 0.8);
      qBottom = drawQuestion(ctx, V, sc, qtext, qp, Ly, qa, sc.type === "a");
    }
    if (sc.type === "a") {
      if (st.tag) { var ta = easeOut(seg(tau, 0.15, 0.6)); ctx.save(); ctx.globalAlpha = ta; chip(ctx, Ly.port ? W / 2 : Ly.qX, qBottom + 14 * u + (1 - ta) * 10 * u, st.tag, 20 * u, "rgba(242,193,78,0.95)", NAVY, Ly.port ? "center" : "left"); ctx.restore(); }
      var c = currentCaption(sc, tau); if (c && O.caps) caption(ctx, V, c.text, c.p, Ly.capY, Ly.capW, 27 * u, { maxLines: 3 });
    } else if (O.caps && !O.qcard) { var c2 = currentCaption(sc, tau); if (c2) caption(ctx, V, c2.text, c2.p, Ly.capY, Ly.capW, 27 * u, { maxLines: 3 }); }
  }
  function drawEnd(ctx, V, sc, tau, Ly, cam) {
    var W = V.W, H = V.H, u = Ly.u, fly = sc.fly || 0;
    if (V.O.nums && tau > fly * 0.8) {
      V.steps.forEach(function (st, j) {
        if (st.card || (st.i || 0) !== cam.v.k) return; var bp = boxPx(V, st); if (!bp || st.b[2] * st.b[3] > 0.45) return;
        var r = toScreen(V, cam.v, bp), a = seg(tau, fly * 0.8 + j * 0.14, fly * 0.8 + j * 0.14 + 0.4), R = 15 * u, cx = r.x + r.w / 2, cy = r.y + r.h / 2;
        ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = "rgba(242,193,78,0.85)"; ctx.lineWidth = 2 * u; ctx.beginPath(); ctx.arc(cx, cy, R * (1.5 + 0.25 * Math.sin(tau * 3 + j)), 0, Math.PI * 2); ctx.stroke();
        ctx.fillStyle = GOLD; ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); ctx.fill(); ctx.fillStyle = NAVY; ctx.font = F(900, R * 1.1); ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText(String(j + 1), cx, cy + 1);
        ctx.restore();
      });
    }
    var c = currentCaption(sc, tau); if (c && V.O.caps) caption(ctx, V, c.text, c.p, Ly.port ? H * 0.78 : H * 0.82, Ly.capW, 30 * u, { weight: 800, maxLines: 4 });
  }
  function drawOutro(ctx, V, sc, tau, Ly) {
    var W = V.W, H = V.H, u = Ly.u, O = V.O, w = V.w, a = easeOut(seg(tau, 0.1, 0.8));
    ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = "rgba(5,9,17,0.78)"; ctx.fillRect(0, 0, W, H);
    var qrOn = !!(O.qr && O.qrUrl), qrS = Math.min(W, H) * (Ly.port ? 0.34 : Ly.sq ? 0.25 : 0.3);
    var x = Ly.pad, maxW = W - Ly.pad * 2 - (!Ly.port && qrOn ? qrS + 40 * u : 0), y = H * (Ly.port ? 0.16 : 0.12);
    ctx.textAlign = "left"; ctx.textBaseline = "top";
    ctx.font = F(900, 18 * u); ctx.fillStyle = GOLD; ctx.fillText("🎨 GIẢI MÃ TÁC PHẨM", x, y); y += 34 * u;
    ctx.font = FS(800, 40 * u); ctx.fillStyle = "#fff"; wrap(ctx, w.title, maxW, 3).forEach(function (l) { ctx.fillText(l, x, y); y += 46 * u; });
    ctx.font = F(600, 19 * u); ctx.fillStyle = "rgba(255,255,255,0.85)"; wrap(ctx, [w.artist, w.date].filter(Boolean).join(" · "), maxW, 2).forEach(function (l) { ctx.fillText(l, x, y); y += 26 * u; });
    y += 14 * u;
    if (O.srcs) {
      var cred = [];
      w.img.forEach(function (d, k) { if (V.I[k] && V.I[k].ok) cred.push(V.I[k].src === "user" ? "Ảnh: tư liệu của tác giả video" : (d.by || "Ảnh: Wikimedia Commons") + (d.lic && !/Phạm vi|CC0/.test(d.by || "") ? " · " + d.lic : "")); });
      var seen = {}; cred = cred.filter(function (c) { if (seen[c]) return false; seen[c] = 1; return true; });
      var mu = O.music === "file" ? "Nhạc: do tác giả video chọn" : (O.music !== "off" ? "Nhạc nền tự tổng hợp" : "");
      if (mu) cred.push(mu); if (V.AP) cred.push("Giọng đọc AI: Piper (VAIS-1000, CC BY 4.0)");
      ctx.font = F(500, 15.5 * u); ctx.fillStyle = "rgba(255,255,255,0.7)";
      cred.slice(0, 6).forEach(function (c) { wrap(ctx, c, maxW, 2).forEach(function (l) { ctx.fillText(l, x, y); y += 21 * u; }); });
      if (w.sources && w.sources.length) { y += 6 * u; ctx.fillText("Nguồn tư liệu: " + w.sources.slice(0, 3).map(function (s) { return String(s.t).split(" — ")[0]; }).join(" · "), x, y); y += 21 * u; }
    }
    // QR + lời mời theo dõi
    var qy = Ly.port ? Math.max(y + 30 * u, H * 0.56) : H * 0.5 - qrS / 2 - 10 * u, qx = Ly.port ? W / 2 - qrS / 2 : W - Ly.pad - qrS;
    if (qrOn) {
      var cv = L.qrCanvas(O.qrUrl);
      if (cv) { ctx.fillStyle = "#fff"; rr(ctx, qx - 12 * u, qy - 12 * u, qrS + 24 * u, qrS + 24 * u, 16 * u); ctx.fill(); ctx.imageSmoothingEnabled = false; ctx.drawImage(cv, qx, qy, qrS, qrS); ctx.imageSmoothingEnabled = true; }
      ctx.font = F(700, 17 * u); ctx.fillStyle = "#fff"; ctx.textAlign = Ly.port ? "center" : "left";
      ctx.fillText(L.shortUrl(O.qrUrl), Ly.port ? W / 2 : qx, qy + qrS + 22 * u);
    }
    ctx.textAlign = "center"; ctx.font = F(900, 26 * u); ctx.fillStyle = GOLD;
    var ctaY = H * (Ly.port ? 0.9 : Ly.sq ? 0.875 : 0.86);
    ctx.fillText("Theo dõi để xem tác phẩm tiếp theo ✦", W / 2, ctaY);
    if (O.credit) { ctx.font = F(700, 18 * u); ctx.fillStyle = "rgba(255,255,255,0.85)"; ctx.fillText(O.credit, W / 2, ctaY + (Ly.sq ? 32 : 36) * u); }
    ctx.restore();
  }

  /* ---------------- 7. tiện ích đầu ra: chữ đăng bài, mục lục, phụ đề, ảnh bìa ---------------- */
  function chapters(V) {
    var out = ["0:00 Mở đầu"], last = 0;
    V.scenes.forEach(function (sc) { if (sc.type !== "q") return; if (sc.t0 - last < 6) return; out.push(fmtClock(sc.t0) + " " + sc.num + ". " + String(sc.st.tag || sc.st.q).replace(/^(?:[\d#*]\uFE0F?\u20E3|[^\wÀ-ỹ])+/u, "").trim().slice(0, 60)); last = sc.t0; });
    var e = V.scenes.filter(function (s) { return s.type === "end"; })[0]; if (e) out.push(fmtClock(e.t0) + " Lời kết");
    return out.join("\n");
  }
  function hashTag(x) { return "#" + String(x).normalize("NFC").split(/[^\p{L}\p{N}]+/u).filter(Boolean).map(function (p) { return p.charAt(0).toUpperCase() + p.slice(1); }).join(""); }
  function postText(w, V) {
    var t = typeOf(w.type), tags = ["#GiờThìTôiMớiHiểu", "#NghệThuậtViệtNam", hashTag(t.vi)].concat((w.tags || []).slice(0, 4).map(hashTag));
    var lines = [trendLine(w, V.O), "", "🎨 " + w.title + (w.artist ? " — " + w.artist : "") + (w.date ? " (" + w.date + ")" : ""), "", w.hook || ""];
    lines.push("", "Trong video:"); V.steps.slice(0, 8).forEach(function (s, i) { lines.push((i + 1) + ". " + (s.q || "")); });
    if (w.where) lines.push("", "📍 " + w.where);
    lines.push("", "Bạn đã để ý chi tiết nào trước khi xem video? Bình luận nhé 👇", "", tags.filter(function (x, i, a) { return x.length > 2 && a.indexOf(x) === i; }).join(" "));
    return lines.join("\n");
  }
  function posterT(V) { var sc = V.scenes[0]; return sc.type === "trend" ? Math.min(sc.dur - 0.6, 2.6) : Math.min(sc.dur - 0.3, 1.2); }
  async function cover(V) {
    var c = document.createElement("canvas"); c.width = V.W; c.height = V.H; var x = c.getContext("2d", { alpha: false });
    renderArt(x, V, posterT(V));
    return await new Promise(function (r) { c.toBlob(r, "image/jpeg", 0.9); });
  }

  /* ---------------- 8. CSS riêng ---------------- */
  var CSS = ".av-ed{display:grid;grid-template-columns:1fr;gap:12px}@media(min-width:900px){.av-ed{grid-template-columns:minmax(0,1.35fr) minmax(320px,1fr)}}" +
    ".av-stage{position:relative;background:#0c1b30;border-radius:12px;overflow:hidden;user-select:none;touch-action:none;display:flex;align-items:center;justify-content:center;min-height:260px}" +
    ".av-stage img{display:block;max-width:100%;max-height:62vh}.av-box{position:absolute;border:2px solid rgba(242,193,78,.85);border-radius:6px;box-shadow:0 0 0 1px rgba(0,0,0,.35);pointer-events:none}" +
    ".av-box b{position:absolute;left:-2px;top:-24px;background:#f2c14e;color:#0f2138;font:800 12px/20px sans-serif;padding:0 7px;border-radius:9px}" +
    ".av-box.on{border-color:#4fd1ff;border-width:3px;background:rgba(79,209,255,.12)}.av-box.on b{background:#4fd1ff}.av-crop{position:absolute;border:2px dashed #fff;pointer-events:none}" +
    ".av-list{display:flex;flex-direction:column;gap:8px;max-height:64vh;overflow:auto;padding-right:4px}" +
    ".av-st{background:#fff;border:1px solid #e7e3d6;border-radius:12px;padding:9px;display:flex;flex-direction:column;gap:6px}.av-st.on{border-color:#4fd1ff;box-shadow:0 0 0 2px rgba(79,209,255,.35)}" +
    ".av-st textarea,.av-st input[type=text],.av-meta textarea,.av-meta input[type=text],.av-meta select{width:100%;box-sizing:border-box;border:1px solid #d9d2bd;border-radius:8px;padding:7px 8px;font:13px/1.45 inherit;font-family:inherit;resize:vertical}" +
    ".av-st .hd{display:flex;gap:6px;align-items:center;font-weight:800;color:#152c4e;font-size:13px}.av-st .hd span{flex:1}.av-mini{border:1px solid #d9d2bd;background:#fff;border-radius:8px;padding:4px 8px;font-weight:700;cursor:pointer;font-size:12.5px;min-height:30px}" +
    ".av-tip{font-size:12px;color:#5c6773;line-height:1.5}.av-meta{display:grid;gap:6px;background:#fff;border:1px solid #e7e3d6;border-radius:12px;padding:10px}" +
    ".av-imgs{display:flex;gap:6px;flex-wrap:wrap}.av-imgs button{border:1px solid #d9d2bd;background:#fff;border-radius:9px;padding:5px 9px;font-weight:700;cursor:pointer;font-size:12.5px}.av-imgs button.on{background:#152c4e;color:#fff;border-color:#152c4e}" +
    ".av-post{width:100%;min-height:150px;font-size:12.5px;border:1px solid #d9d2bd;border-radius:8px;padding:8px;box-sizing:border-box}";
  function ensureCSS() {
    if (!document.getElementById("tv-css")) { var s = document.createElement("style"); s.id = "tv-css"; s.textContent = L.CSS; document.head.appendChild(s); }
    if (!document.getElementById("av-css")) { var s2 = document.createElement("style"); s2.id = "av-css"; s2.textContent = CSS; document.head.appendChild(s2); }
  }

  /* ---------------- 9. studio ---------------- */
  function open(work0, opts) {
    opts = opts || {}; ensureCSS();
    var w = resolve(work0), O = loadOpts(), I = [], V = null, NRc = null, AUD = { nk: null, AP: null, mk: null, mix: null }, player = L.AudioPlayer();
    var userMusic = null, userMusicName = "", playing = false, raf = 0, last = 0, t = 0, atPoster = false, busy = false, cancelFn = null, dirty = true, editMode = false;
    var ov = document.createElement("div"); ov.className = "tv-ov";
    function seg3(k, label, o) { return '<div class="tv-f"><b>' + label + '</b><div class="tv-seg" data-k="' + k + '">' + o.map(function (x) { return '<button data-val="' + x[0] + '"' + (x[2] ? ' title="' + escH(x[2]) + '"' : "") + ">" + x[1] + "</button>"; }).join("") + "</div></div>"; }
    function chk(k, label) { return '<label><input type="checkbox" data-c="' + k + '"/> ' + label + "</label>"; }
    var musicBtns = '<button data-val="auto">✨ Tự chọn</button><button data-val="off">Tắt</button>' + Object.keys(MUSIC.PRE).map(function (k) { return '<button data-val="' + k + '">' + MUSIC.PRE[k].name + "</button>"; }).join("") + '<button data-val="file">📂 Nhạc của anh…</button>';
    ov.innerHTML = '<div class="tv-box"><div class="tv-top"><h2>🎨 Video giải mã: <span data-v="title"></span></h2><button class="tv-x" data-a="edit">✏️ Chỉnh chi tiết</button><button class="tv-x" data-a="close">✕ Đóng</button></div>' +
      '<div class="tv-main" data-v="main"><div><div class="tv-prev"><canvas></canvas></div>' +
      '<div class="tv-ctl"><button class="tv-b" data-a="prev" title="Chi tiết trước">⏮</button><button class="tv-b navy" data-a="play">▶ Xem thử</button><button class="tv-b" data-a="next" title="Chi tiết sau">⏭</button>' +
      '<input type="range" min="0" max="1000" value="0" data-a="seek"/><span class="tv-lbl" data-v="time">0:00</span></div>' +
      '<div class="tv-ctl"><button class="tv-b" data-a="build">🔊 Dựng tiếng</button><span class="tv-lbl" data-v="aud"></span></div>' +
      '<div class="tv-lbl" data-v="scene" style="margin-top:4px"></div>' +
      '<div class="tv-note" data-v="imgnote"></div>' +
      '<div class="tv-prog" data-v="prog"><b data-v="phase">…</b><div class="tv-bar"><i></i></div><button class="tv-b" data-a="cancel">Huỷ</button></div>' +
      '<div class="tv-res" data-v="res"></div></div>' +
      '<div class="tv-set">' +
      '<div class="tv-f tv-sub"><b>💬 Câu mở đầu (trend)</b><div class="tv-chk">' + chk("trend", "Mở đầu bằng câu «Giờ thì tôi mới hiểu…»") + '</div><input type="text" data-o="trendText"/></div>' +
      seg3("len", "Độ dài", [["short", "⚡ Ngắn (~1,5 phút · 4 chi tiết)"], ["full", "📖 Đầy đủ (3–4 phút)"]]) +
      seg3("aspect", "Khung hình", [["9:16", "▯ 9:16 dọc"], ["16:9", "▭ 16:9 ngang"], ["1:1", "◻ 1:1 vuông"]]) +
      seg3("res", "Độ nét", [[720, "720p"], [1080, "1080p (nét)"]]) +
      seg3("pace", "Nhịp máy quay", [["fast", "Nhanh"], ["mid", "Vừa"], ["slow", "Chậm"]]) +
      '<div class="tv-f tv-sub"><b>🎙️ Thuyết minh</b><div class="tv-seg" data-k="voice"><button data-val="ai">🤖 Giọng AI — có tiếng trong video</button><button data-val="off">🔇 Không đọc (chỉ chữ)</button></div>' +
      '<div class="tv-seg" data-k="rate" data-show="ai"><button data-val="0.9">🐢 Chậm</button><button data-val="1">Vừa</button><button data-val="1.12">🐇 Nhanh</button></div><div class="tv-note" data-v="aiinfo"></div></div>' +
      '<div class="tv-f tv-sub"><b>🎵 Nhạc nền</b><div class="tv-seg" data-k="music">' + musicBtns + '</div>' +
      '<input type="file" accept="audio/*,.mp3,.m4a,.aac,.wav,.ogg,.opus,.flac" data-v="mfile" class="tv-hide"/>' +
      '<div class="tv-row"><span>Âm lượng</span><input type="range" min="0" max="100" step="5" data-o="musicVol"/><button class="tv-b" data-a="hearm">▶ Nghe thử</button></div><div class="tv-note" data-v="minfo"></div></div>' +
      '<div class="tv-f"><b>Hiện trên video</b><div class="tv-chk">' + chk("caps", "Phụ đề lời đọc") + chk("qcard", "Thẻ câu hỏi") + chk("spot", "Khung sáng chi tiết") + chk("nums", "Đánh số chi tiết") + chk("srcs", "Nguồn ảnh cuối video") + chk("qr", "Mã QR cuối video") + "</div></div>" +
      '<div class="tv-f"><b>Chữ ký</b><input type="text" data-o="credit"/></div>' +
      '<div class="tv-f" data-show-qr="1"><b>Mã QR dẫn tới</b><input type="text" data-o="qrUrl" placeholder="https://fb.com/lopmaybay"/></div>' +
      '<div class="tv-lbl" data-v="est"></div>' +
      '<div class="tv-go"><button class="tv-b navy" data-a="export">⬇️ Xuất video MP4</button><button class="tv-b" data-a="post">📋 Chữ đăng bài + hashtag</button></div>' +
      '<div class="tv-note">Ảnh: Wikimedia Commons (phạm vi công cộng / giấy phép mở, tên tác giả ảnh hiện ở cuối video) hoặc ảnh của anh. Giọng AI chạy ngay trên máy: Piper — VAIS-1000 (CC BY 4.0). Nhạc dựng sẵn do trình duyệt tự tổng hợp. Video không trích lời bài hát.</div>' +
      "</div></div>" +
      '<div class="tv-main tv-hide" data-v="editor"></div></div>';
    document.body.appendChild(ov);
    var $ = function (s) { return ov.querySelector(s); }, canvas = $("canvas"), ctx = canvas.getContext("2d", { alpha: false });
    $('[data-o="credit"]').value = O.credit || ""; $('[data-o="qrUrl"]').value = O.qrUrl || ""; $('[data-o="musicVol"]').value = Math.round((+O.musicVol || 0) * 100);
    var trendInp = $('[data-o="trendText"]');
    function narrKey() { return JSON.stringify([w.id, w.edited ? JSON.stringify(w.steps).length + (w.hook || "").length : 0, O.len, O.voice, O.rate, O.trend, trendLine(w, O), O.qr && O.qrUrl ? 1 : 0]); }
    function mixKey(Vx) { return narrKey() + "|" + musicFor(w, O) + "|" + O.musicVol + "|" + userMusicName + "|" + Vx.total.toFixed(3); }
    function syncUI() {
      $('[data-v="title"]').textContent = w.title;
      ov.querySelectorAll(".tv-seg").forEach(function (sg) { var k = sg.dataset.k; sg.querySelectorAll("button").forEach(function (b) { b.classList.toggle("on", String(O[k]) === b.dataset.val); }); });
      ov.querySelectorAll("[data-c]").forEach(function (c) { c.checked = !!O[c.dataset.c]; });
      ov.querySelectorAll("[data-show]").forEach(function (el) { el.classList.toggle("tv-hide", el.dataset.show.split(" ").indexOf(O.voice) < 0); });
      ov.querySelectorAll("[data-show-qr]").forEach(function (el) { el.classList.toggle("tv-hide", !O.qr); });
      trendInp.placeholder = trendLine(w, Object.assign({}, O, { trendText: "" })); trendInp.disabled = !O.trend;
      $('[data-a="export"]').textContent = "⬇️ Xuất video MP4 " + (O.voice === "ai" ? (O.music !== "off" ? "(lời đọc + nhạc)" : "(có lời đọc)") : O.music !== "off" ? "(chỉ có nhạc)" : "(không tiếng)");
      var mu = musicFor(w, O); $('[data-v="minfo"]').textContent = O.music === "file" ? (userMusicName ? "🎵 " + userMusicName : "Chọn một tệp nhạc trên máy (MP3, M4A, WAV…)") : O.music === "off" ? "" : (O.music === "auto" ? "Tự chọn: " + (MUSIC.PRE[mu] ? MUSIC.PRE[mu].name : mu) + " · " : "") + "Nhạc tự nhỏ lại khi có lời đọc.";
      aiInfo(); audLabel();
    }
    async function aiInfo() {
      var el = $('[data-v="aiinfo"]'); if (O.voice !== "ai") { el.textContent = ""; return; }
      if (!AIV.supported()) { el.textContent = "⚠️ Trình duyệt này chưa chạy được giọng AI — hãy dùng Chrome hoặc Edge bản mới."; return; }
      var info = {}; try { info = await AIV.storageInfo(); } catch (e) { }
      el.textContent = "Giọng AI tiếng Việt: " + AIV.VOICES.vi.name + " (" + AIV.VOICES.vi.g + "). " + (info.vi ? "✅ Đã có sẵn trên máy." : "Lần đầu cần tải khoảng " + (AIV.VOICES.vi.mb + 30) + " MB (lưu lại, lần sau dùng ngay).");
    }
    function audLabel() {
      var need = O.voice === "ai" || O.music !== "off", ok = player.has();
      $('[data-a="build"]').classList.toggle("tv-hide", !need || ok);
      $('[data-v="aud"]').textContent = !need ? "🔇 Video không tiếng" : ok ? (O.voice === "ai" ? "🔊 Xem thử có tiếng (lời đọc" + (O.music !== "off" ? " + nhạc" : "") + ")" : "🎵 Xem thử có nhạc nền") : "Xem thử đang không tiếng — bấm 🔊 Dựng tiếng để nghe " + (O.voice === "ai" ? "lời đọc" + (O.music !== "off" ? " + nhạc" : "") : "nhạc nền");
    }
    function effO() { var o = {}; for (var k in O) o[k] = O[k]; o.music = musicFor(w, O); o.trendText = trendInp.value; return o; }
    function rebuild() {
      var o = effO(), d = L.dims(o); canvas.width = d.W; canvas.height = d.H;
      var steps = pickSteps(w, o), NR = narrate(w, o, steps), ap = (o.voice === "ai" && AUD.nk === narrKey()) ? AUD.AP : null;
      var wasPlaying = playing && player.playing(); player.stop();
      V = build(w, o, d.W, d.H, NR, ap, I); NRc = NR; t = Math.min(t, V.total - 0.01);
      player.set(AUD.mix && AUD.mk === mixKey(V) ? AUD.mix : null);
      if (wasPlaying && player.has()) player.play(t);
      $('[data-v="est"]').textContent = "⏱ Thời lượng ~" + fmtClock(V.total) + " · " + V.steps.length + " chi tiết · " + d.W + "×" + d.H + (ap ? "" : (o.voice === "ai" ? " (ước lượng — sẽ khớp đúng sau khi dựng tiếng)" : ""));
      dirty = true; audLabel(); imgNote();
    }
    function imgNote() {
      var el = $('[data-v="imgnote"]'), miss = w.img.map(function (d, k) { return (!I[k] || !I[k].ok) ? k : -1; }).filter(function (k) { return k >= 0; });
      if (!miss.length) { el.innerHTML = w.rights === "copyright" ? "⚠️ " + escH(w.rightsNote || "Tác phẩm còn bản quyền — cân nhắc khi đăng tải.") : ""; return; }
      el.innerHTML = "📷 " + (w.img[miss[0]] && w.img[miss[0]].user ? "Tác phẩm này còn bản quyền nên không kèm ảnh. " : "Chưa tải được ảnh. ") + '<button class="tv-b" data-a="upimg" data-k="' + miss[0] + '">📂 Nạp ảnh của anh</button> ' + escH((w.img[miss[0]] || {}).note || "");
    }
    function frame() { if (!V) return; renderArt(ctx, V, t); dirty = false; $('[data-a="seek"]').value = Math.round(t / V.total * 1000); $('[data-v="time"]').textContent = fmtClock(t) + " / " + fmtClock(V.total); var sc = V.scenes[sceneAt(V, t)]; $('[data-v="scene"]').textContent = sc.type === "q" || sc.type === "a" ? "Chi tiết " + sc.num + "/" + sc.of + ": " + (sc.st.tag || "") : ({ trend: "Câu mở đầu", hook: "Mở đầu", info: "Giới thiệu", end: "Lời kết", outro: "Nguồn & mã QR" })[sc.type] || ""; }
    function loop(ts) {
      if (!playing) return;
      var dt = last ? (ts - last) / 1000 : 0; last = ts;
      if (player.playing()) t = player.time(); else t += dt;
      if (t >= V.total) { t = V.total - 0.001; setPlay(false); }
      frame(); raf = requestAnimationFrame(loop);
    }
    function setPlay(on) { playing = on; $('[data-a="play"]').textContent = on ? "⏸ Dừng" : "▶ Xem thử"; cancelAnimationFrame(raf); if (on) { if (t >= V.total - 0.05 || atPoster) t = 0; atPoster = false; last = 0; if (player.has()) player.play(t); raf = requestAnimationFrame(loop); } else { player.stop(); frame(); } }
    function seekScene(dir) { atPoster = false; var idx = V.scenes.map(function (s) { return s.type === "q" || s.type === "end" || s.type === "trend" || s.type === "hook" ? s.t0 : -1; }).filter(function (x) { return x >= 0; }); var cur = t + 0.05, nt = dir > 0 ? idx.filter(function (x) { return x > cur; })[0] : idx.filter(function (x) { return x < cur - 0.6; }).pop(); if (nt == null) nt = dir > 0 ? V.total - 0.01 : 0; t = nt + 0.01; if (playing && player.has()) player.play(t); frame(); }
    var prog = $('[data-v="prog"]');
    function ui() { return { phase: function (txt, f) { prog.querySelector('[data-v="phase"]').textContent = txt; prog.querySelector(".tv-bar i").style.width = Math.round(clamp(f || 0, 0, 1) * 100) + "%"; } }; }
    async function withProgress(fn) {
      if (busy) return null; busy = true; setPlay(false); prog.style.display = "block"; var cancelled = false; cancelFn = function () { cancelled = true; };
      ov.querySelectorAll('[data-a="export"],[data-a="build"]').forEach(function (b) { b.disabled = true; });
      try { return await fn(ui(), function () { return cancelled; }); }
      catch (err) { if (String(err && err.message) !== "cancel") showErr(err); return null; }
      finally { busy = false; prog.style.display = "none"; cancelFn = null; ov.querySelectorAll('[data-a="export"],[data-a="build"]').forEach(function (b) { b.disabled = false; }); }
    }
    function showErr(err) { var r = $('[data-v="res"]'); r.style.display = "block"; r.innerHTML = '<b style="color:#b23b34">⚠️ Lỗi: ' + escH(err && err.message || err) + "</b>"; if (global.console) console.error(err); }
    async function buildAudio(u2, isC) {
      var o = effO(), steps = pickSteps(w, o), NR = narrate(w, o, steps), nk = narrKey(), AP = null;
      if (o.voice === "ai") {
        if (AUD.nk === nk && AUD.AP) AP = AUD.AP;
        else { AP = await AIV.synthNarration(NR, o, u2, isC); AUD.nk = nk; AUD.AP = AP; }
      }
      var d = L.dims(o), Vx = build(w, o, d.W, d.H, NR, AP, I), mk = mixKey(Vx), mix = null;
      if (AUD.mk === mk && AUD.mix) mix = AUD.mix;
      else { if (o.music === "file" && !userMusic) o.music = "off"; mix = await L.mixAudio(Vx, o, userMusic, u2); AUD.mk = mk; AUD.mix = mix; }
      return { V: Vx, NR: NR, mix: mix };
    }
    async function doBuild() { var r = await withProgress(buildAudio); if (r) { rebuild(); $('[data-v="res"]').style.display = "none"; } }
    async function doExport() {
      var res = $('[data-v="res"]'); res.style.display = "none";
      var out = await withProgress(async function (u2, isC) {
        var b = (O.voice === "ai" || O.music !== "off") ? await buildAudio(u2, isC) : { V: V, mix: null };
        if (O.qr && O.qrUrl) { await L.ensureQR(); L.qrCanvas(O.qrUrl); }
        var x = await L.exportVideo(b.V, { phase: u2.phase, onCancel: function (fn) { cancelFn = fn; } }, b.mix);
        return { r: x, V: b.V };
      });
      if (!out) return; rebuild();
      var r = out.r, Vx = out.V, url = URL.createObjectURL(r.blob), base = L.slug(w.title) + "-" + O.aspect.replace(":", "x") + (O.len === "short" ? "-ngan" : ""), name = base + "." + r.ext, mb = (r.blob.size / 1048576).toFixed(1);
      res.style.display = "block";
      res.innerHTML = "<b>✅ Xong: " + escH(name) + " · " + mb + " MB · " + fmtClock(Vx.total) + (r.audio ? (O.voice === "ai" ? " · 🔊 có lời đọc" + (O.music !== "off" ? " + nhạc" : "") : " · 🎵 có nhạc nền") : " · 🔇 không tiếng") + "</b>" +
        (r.noAudioCodec ? '<div class="tv-note" style="color:#b23b34">⚠️ Trình duyệt này không mã hoá được âm thanh — hãy dùng Chrome hoặc Edge bản mới.</div>' : "") +
        '<video controls playsinline src="' + url + '"></video><div class="tv-go" style="flex-direction:row;flex-wrap:wrap">' +
        '<a class="tv-b gold" href="' + url + '" download="' + escH(name) + '">⬇️ Tải video về máy</a>' +
        (Vx.AP ? '<button class="tv-b" data-a="srt">💬 Phụ đề .srt</button>' : "") + '<button class="tv-b" data-a="chap">📑 Mục lục YouTube</button><button class="tv-b" data-a="cov">🖼️ Ảnh bìa JPG</button>' +
        (navigator.canShare ? '<button class="tv-b" data-a="share">📤 Chia sẻ</button>' : "") + "</div>" +
        '<div class="tv-note">Mã hoá: ' + escH(r.codec || "") + "</div>";
      res._blob = r.blob; res._name = name; res._V = Vx; res._base = base;
    }
    function showPost() {
      var res = $('[data-v="res"]'); res.style.display = "block";
      res.innerHTML = "<b>📋 Chữ đăng bài (Facebook, TikTok, YouTube)</b><textarea class=\"av-post\" readonly>" + escH(postText(w, V)) + '</textarea><div class="tv-go" style="flex-direction:row"><button class="tv-b" data-a="copypost">📋 Chép</button></div>';
    }
    // ---------------- sự kiện ----------------
    ov.addEventListener("click", async function (e) {
      var b = e.target.closest("button, a"); if (!b || !ov.contains(b)) return;
      var a = b.dataset.a, sg = b.closest(".tv-seg");
      if (sg && b.dataset.val != null) {
        var k = sg.dataset.k, val = b.dataset.val; O[k] = (k === "res") ? +val : (k === "rate" ? +val : val);
        if (k === "music" && val === "file" && !userMusic) $('[data-v="mfile"]').click();
        saveOpts(O); syncUI(); rebuild(); return;
      }
      if (a === "close") close();
      else if (a === "play") setPlay(!playing);
      else if (a === "next") seekScene(1); else if (a === "prev") seekScene(-1);
      else if (a === "build") doBuild();
      else if (a === "export") doExport();
      else if (a === "post") showPost();
      else if (a === "cancel") { if (cancelFn) cancelFn(); }
      else if (a === "edit") toggleEditor(!editMode);
      else if (a === "upimg") pickImage(+b.dataset.k || 0);
      else if (a === "copypost") { var ta = ov.querySelector(".av-post"); try { await navigator.clipboard.writeText(ta.value); b.textContent = "✅ Đã chép"; } catch (er) { ta.select(); document.execCommand("copy"); b.textContent = "✅ Đã chép"; } }
      else if (a === "hearm") hearMusic(b);
      else if (a === "srt" || a === "chap" || a === "cov" || a === "share") {
        var res = $('[data-v="res"]'), Vx = res._V || V;
        if (a === "srt") L.dl(new Blob([L.makeSRT(Vx)], { type: "text/plain" }), res._base + ".srt");
        else if (a === "chap") { var tx = document.createElement("textarea"); tx.value = chapters(Vx); tx.readOnly = true; tx.style.cssText = "width:100%;min-height:120px;margin-top:8px"; res.appendChild(tx); }
        else if (a === "cov") { var cb = await cover(Vx); L.dl(cb, res._base + "-bia.jpg"); }
        else if (a === "share") { try { await navigator.share({ files: [new File([res._blob], res._name, { type: res._blob.type })], title: w.title }); } catch (er) { } }
      }
    });
    var hearNode = null;
    async function hearMusic(btn) {
      if (hearNode) { try { hearNode.stop(); } catch (e) { } hearNode = null; btn.textContent = "▶ Nghe thử"; return; }
      var mu = musicFor(w, O); if (mu === "off") return; btn.textContent = "…";
      try {
        var tr = await MUSIC.track({ music: mu }, 16, 48000, userMusic); if (!tr) { btn.textContent = "▶ Nghe thử"; return; }
        var AC = global.AudioContext || global.webkitAudioContext, ac = new AC(), buf = ac.createBuffer(2, tr[0].length, 48000); buf.getChannelData(0).set(tr[0]); buf.getChannelData(1).set(tr[1]);
        var s = ac.createBufferSource(), g = ac.createGain(); g.gain.value = clamp(+O.musicVol || 0.5, 0, 1); s.buffer = buf; s.connect(g); g.connect(ac.destination); s.start();
        hearNode = s; btn.textContent = "⏹ Dừng"; s.onended = function () { hearNode = null; btn.textContent = "▶ Nghe thử"; try { ac.close(); } catch (e) { } };
      } catch (e) { btn.textContent = "▶ Nghe thử"; }
    }
    ov.addEventListener("input", function (e) {
      var el = e.target;
      if (el.dataset.a === "seek") { atPoster = false; t = (+el.value / 1000) * V.total; if (playing && player.has()) player.play(t); frame(); return; }
      if (el.dataset.o === "musicVol") { O.musicVol = (+el.value) / 100; saveOpts(O); clearTimeout(el._t); el._t = setTimeout(rebuild, 300); return; }
      if (el.dataset.o === "trendText") { clearTimeout(el._t); el._t = setTimeout(rebuild, 400); return; }
      if (el.dataset.o) { O[el.dataset.o] = el.value; saveOpts(O); clearTimeout(el._t); el._t = setTimeout(rebuild, 350); }
    });
    ov.addEventListener("change", async function (e) {
      var el = e.target;
      if (el.dataset.c) { O[el.dataset.c] = el.checked; saveOpts(O); syncUI(); rebuild(); }
      if (el.dataset.v === "mfile" && el.files && el.files[0]) {
        var f = el.files[0]; try { userMusic = await MUSIC.decodeFile(f); userMusicName = f.name; O.music = "file"; } catch (er) { alert("Không đọc được tệp nhạc này."); }
        syncUI(); rebuild();
      }
    });
    function pickImage(k) {
      var inp = document.createElement("input"); inp.type = "file"; inp.accept = "image/*";
      inp.onchange = async function () {
        var f = inp.files && inp.files[0]; if (!f) return;
        await setUserImage(w.id, k, f); I = await loadWorkImages(w); rebuild(); frame(); if (editMode) renderEditor();
        if (opts.onChange) try { opts.onChange(w); } catch (er) { }
      };
      inp.click();
    }
    var cvObs = null;
    function close() {
      setPlay(false); player.close(); try { AIV.dispose(); } catch (e) { } if (hearNode) try { hearNode.stop(); } catch (e) { }
      document.removeEventListener("keydown", onKey); ov.remove(); if (opts.onClose) try { opts.onClose(w); } catch (e) { }
    }
    function onKey(e) { if (e.key === "Escape" && !busy) { if (editMode) toggleEditor(false); else close(); } else if (e.key === " " && !editMode && document.activeElement && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) { e.preventDefault(); setPlay(!playing); } }
    document.addEventListener("keydown", onKey);

    /* ---------- trình chỉnh chi tiết ---------- */
    var ED = { k: 0, sel: -1, mode: "box" };
    function toggleEditor(on) {
      editMode = on; setPlay(false);
      $('[data-v="main"]').classList.toggle("tv-hide", on); $('[data-v="editor"]').classList.toggle("tv-hide", !on);
      $('[data-a="edit"]').textContent = on ? "🎬 Về video" : "✏️ Chỉnh chi tiết";
      if (on) renderEditor(); else { rebuild(); frame(); }
    }
    function persist() {
      var o = {}; EDIT_FIELDS.forEach(function (f) { if (w[f] !== undefined) o[f] = w[f]; });
      if (w.custom) { var c = clone(w); delete c.edited; saveCustom(c); } else setOverride(w.id, o);
      w.edited = true; AUD.nk = null; AUD.mk = null; player.set(null);
      if (opts.onChange) try { opts.onChange(w); } catch (e) { }
    }
    function renderEditor() {
      var ed = $('[data-v="editor"]'), m = I[ED.k], steps = w.steps;
      var imgBtns = w.img.map(function (d, k) { return '<button data-ed="img" data-k="' + k + '" class="' + (k === ED.k ? "on" : "") + '">Ảnh ' + (k + 1) + (I[k] && I[k].ok ? "" : " ⚠️") + "</button>"; }).join("");
      ed.innerHTML = '<div class="av-ed"><div>' +
        '<div class="av-imgs">' + imgBtns + '<button data-ed="addimg">➕ Thêm ảnh</button><button data-ed="upimg">📂 Thay bằng ảnh của anh</button>' + (m && m.src === "user" ? '<button data-ed="rmimg">↩︎ Bỏ ảnh của anh</button>' : "") + '<button data-ed="crop" class="' + (ED.mode === "crop" ? "on" : "") + '">✂️ Khung tranh</button></div>' +
        '<div class="av-stage" data-ed="stage">' + (m && m.ok ? '<img draggable="false" src="' + escH(m.el.src) + '"/>' : '<div class="av-tip" style="color:#fff;padding:30px">Chưa có ảnh — bấm 📂 để nạp ảnh của anh.</div>') + '</div>' +
        '<div class="av-tip">👉 Chọn một chi tiết bên phải rồi <b>kéo chuột trên ảnh</b> để vẽ lại khung của nó. ' + (ED.mode === "crop" ? "<b>Đang chỉnh khung tranh:</b> kéo để chọn phần tác phẩm (bỏ viền, khung gỗ)." : "") + ' Các thay đổi được lưu ngay trên máy này.</div>' +
        '<div class="av-meta"><b>Lời mở đầu (hook)</b><textarea data-f="hook" rows="2">' + escH(w.hook || "") + '</textarea><b>Giới thiệu</b><textarea data-f="intro" rows="2">' + escH(w.intro || "") + '</textarea><b>Lời kết</b><textarea data-f="end" rows="2">' + escH(w.end || "") + "</textarea>" +
        (w.custom ? '<b>Tên tác phẩm</b><input type="text" data-f="title" value="' + escH(w.title) + '"/><b>Tác giả</b><input type="text" data-f="artist" value="' + escH(w.artist || "") + '"/><b>Năm / thời kỳ</b><input type="text" data-f="date" value="' + escH(w.date || "") + '"/><b>Nơi lưu giữ</b><input type="text" data-f="where" value="' + escH(w.where || "") + '"/><b>Thể loại</b><select data-f="type">' + DB().types.map(function (t) { return '<option value="' + t.id + '"' + (t.id === w.type ? " selected" : "") + ">" + t.icon + " " + t.vi + "</option>"; }).join("") + "</select>" : "") +
        '</div><div class="tv-go" style="flex-direction:row;flex-wrap:wrap"><button class="tv-b" data-ed="export">⬇️ Xuất kịch bản JSON</button><button class="tv-b" data-ed="import">📥 Nhập JSON</button>' + (w.custom ? '<button class="tv-b" data-ed="delwork">🗑️ Xoá tác phẩm này</button>' : '<button class="tv-b" data-ed="reset">↩︎ Khôi phục bản gốc</button>') + "</div></div>" +
        '<div><div class="av-list">' + steps.map(function (s, j) {
          return '<div class="av-st' + (j === ED.sel ? " on" : "") + '" data-j="' + j + '"><div class="hd"><span>' + (j + 1) + ". " + escH(s.tag || "Chi tiết") + (s.card ? " · thẻ chữ" : " · ảnh " + ((s.i || 0) + 1)) + '</span><label class="av-tip"><input type="checkbox" data-sf="k"' + (s.k ? " checked" : "") + '/> bản ngắn</label>' +
            '<button class="av-mini" data-ed="up">↑</button><button class="av-mini" data-ed="down">↓</button><button class="av-mini" data-ed="del">🗑️</button></div>' +
            '<input type="text" data-sf="tag" placeholder="Nhãn ngắn (vd 🐱 Mèo = quyền thế)" value="' + escH(s.tag || "") + '"/>' +
            '<textarea data-sf="q" rows="2" placeholder="Câu hỏi">' + escH(s.q || "") + '</textarea><textarea data-sf="a" rows="3" placeholder="Lời giải">' + escH(s.a || "") + '</textarea>' +
            '<textarea data-sf="s" rows="2" placeholder="Lời giải ngắn cho bản ~1 phút (tuỳ chọn)">' + escH(s.s || "") + "</textarea>" +
            (s.card ? '<input type="text" data-sf="cardbig" placeholder="Chữ lớn trên thẻ" value="' + escH(s.card.big || "") + '"/><input type="text" data-sf="cardsub" placeholder="Dòng phụ" value="' + escH(s.card.sub || "") + '"/>' : "") + "</div>";
        }).join("") + '</div><div class="tv-go" style="flex-direction:row;flex-wrap:wrap"><button class="tv-b navy" data-ed="add">➕ Thêm chi tiết (vẽ khung)</button><button class="tv-b" data-ed="addcard">🔤 Thêm thẻ chữ</button></div>' +
        '<div class="av-tip">Mẹo viết: câu hỏi ngắn gợi tò mò («Bạn có để ý…?», «Vì sao…?»), lời giải 2–3 câu, câu đầu là đáp án. Đánh dấu «bản ngắn» cho 5–6 chi tiết hay nhất.</div></div></div>';
      drawBoxes();
    }
    function drawBoxes() {
      var stage = ov.querySelector('[data-ed="stage"]'); if (!stage) return; var img = stage.querySelector("img"), m = I[ED.k]; if (!img || !m || !m.ok) return;
      stage.querySelectorAll(".av-box,.av-crop").forEach(function (x) { x.remove(); });
      function place() {
        var r = img.getBoundingClientRect(), sr = stage.getBoundingClientRect(), ox = r.left - sr.left, oy = r.top - sr.top, sx = r.width / m.W, sy = r.height / m.H;
        stage._map = { ox: ox, oy: oy, sx: sx, sy: sy };
        var cr = document.createElement("div"); cr.className = "av-crop"; cr.style.cssText = "left:" + (ox + m.x0 * sx) + "px;top:" + (oy + m.y0 * sy) + "px;width:" + (m.cw * sx) + "px;height:" + (m.ch * sy) + "px"; stage.appendChild(cr);
        w.steps.forEach(function (s, j) {
          if (s.card || (s.i || 0) !== ED.k || !s.b) return;
          var d = document.createElement("div"); d.className = "av-box" + (j === ED.sel ? " on" : "");
          d.style.cssText = "left:" + (ox + (m.x0 + s.b[0] * m.cw) * sx) + "px;top:" + (oy + (m.y0 + s.b[1] * m.ch) * sy) + "px;width:" + (s.b[2] * m.cw * sx) + "px;height:" + (s.b[3] * m.ch * sy) + "px";
          d.innerHTML = "<b>" + (j + 1) + "</b>"; stage.appendChild(d);
        });
      }
      if (img.complete) place(); else img.onload = place;
    }
    function stagePoint(e) { var stage = ov.querySelector('[data-ed="stage"]'), mp = stage && stage._map, m = I[ED.k]; if (!mp || !m) return null; var sr = stage.getBoundingClientRect(), x = ((e.clientX - sr.left) - mp.ox) / mp.sx, y = ((e.clientY - sr.top) - mp.oy) / mp.sy; return { x: clamp(x, 0, m.W), y: clamp(y, 0, m.H) }; }
    var drag = null;
    ov.addEventListener("pointerdown", function (e) {
      var stage = e.target.closest('[data-ed="stage"]'); if (!stage || !editMode) return;
      var p = stagePoint(e); if (!p) return;
      if (ED.mode !== "crop" && ED.sel < 0) { flash("Hãy chọn một chi tiết ở danh sách bên phải (hoặc bấm ➕ Thêm chi tiết) trước khi vẽ khung."); return; }
      drag = { p0: p, el: document.createElement("div") }; drag.el.className = ED.mode === "crop" ? "av-crop" : "av-box on"; stage.appendChild(drag.el); stage.setPointerCapture(e.pointerId); e.preventDefault();
    });
    ov.addEventListener("pointermove", function (e) {
      if (!drag) return; var p = stagePoint(e), stage = ov.querySelector('[data-ed="stage"]'), mp = stage._map; if (!p) return;
      var x = Math.min(p.x, drag.p0.x), y = Math.min(p.y, drag.p0.y), ww = Math.abs(p.x - drag.p0.x), hh = Math.abs(p.y - drag.p0.y);
      drag.el.style.cssText = "left:" + (mp.ox + x * mp.sx) + "px;top:" + (mp.oy + y * mp.sy) + "px;width:" + (ww * mp.sx) + "px;height:" + (hh * mp.sy) + "px"; drag.r = [x, y, ww, hh];
    });
    ov.addEventListener("pointerup", function () {
      if (!drag) return; var r = drag.r, m = I[ED.k]; drag.el.remove(); drag = null; if (!r || r[2] < 6 || r[3] < 6 || !m) return;
      if (ED.mode === "crop") {
        var d = w.img[ED.k]; d.crop = [r[0] / m.W, r[1] / m.H, r[2] / m.W, r[3] / m.H].map(function (v) { return +v.toFixed(4); });
        I[ED.k] = prepImage(m.el, d, m.src); ED.mode = "box"; persist(); renderEditor(); return;
      }
      var s = w.steps[ED.sel]; if (!s) return; s.i = ED.k; delete s.card;
      s.b = [(r[0] - m.x0) / m.cw, (r[1] - m.y0) / m.ch, r[2] / m.cw, r[3] / m.ch].map(function (v) { return +clamp(v, -0.2, 1.2).toFixed(4); });
      persist(); renderEditor();
    });
    function flash(msg) { var tip = ov.querySelector('[data-v="editor"] .av-tip'); if (tip) { tip.innerHTML = "⚠️ " + escH(msg); tip.style.color = "#b23b34"; } }
    ov.addEventListener("click", async function (e) {
      if (!editMode) return; var b = e.target.closest("[data-ed]"), card = e.target.closest(".av-st");
      if (card && (!b || b.dataset.ed === undefined) && !e.target.closest("textarea,input")) { ED.sel = +card.dataset.j; var s0 = w.steps[ED.sel]; if (s0 && !s0.card) ED.k = s0.i || 0; renderEditor(); return; }
      if (!b) return; var a = b.dataset.ed, j = card ? +card.dataset.j : -1;
      if (a === "img") { ED.k = +b.dataset.k; ED.mode = "box"; renderEditor(); }
      else if (a === "addimg") { w.img.push({ user: true, w: 1000, h: 1000 }); ED.k = w.img.length - 1; persist(); pickImage(ED.k); }
      else if (a === "upimg") pickImage(ED.k);
      else if (a === "rmimg") { await setUserImage(w.id, ED.k, null); I = await loadWorkImages(w); renderEditor(); }
      else if (a === "crop") { ED.mode = ED.mode === "crop" ? "box" : "crop"; renderEditor(); }
      else if (a === "add") { w.steps.push({ i: ED.k, b: [0.35, 0.35, 0.3, 0.3], q: "Bạn có để ý…?", a: "", tag: "" }); ED.sel = w.steps.length - 1; persist(); renderEditor(); }
      else if (a === "addcard") { w.steps.push({ card: { big: "?", sub: "" }, q: "Bạn có biết…?", a: "", tag: "" }); ED.sel = w.steps.length - 1; persist(); renderEditor(); }
      else if (a === "del" && j >= 0) { if (confirm("Xoá chi tiết " + (j + 1) + "?")) { w.steps.splice(j, 1); ED.sel = -1; persist(); renderEditor(); } }
      else if ((a === "up" || a === "down") && j >= 0) { var nj = a === "up" ? j - 1 : j + 1; if (nj < 0 || nj >= w.steps.length) return; var tmp = w.steps[j]; w.steps[j] = w.steps[nj]; w.steps[nj] = tmp; ED.sel = nj; persist(); renderEditor(); }
      else if (a === "export") { var c = clone(w); delete c.edited; L.dl(new Blob([JSON.stringify(c, null, 2)], { type: "application/json" }), L.slug(w.title) + ".kich-ban.json"); }
      else if (a === "import") {
        var inp = document.createElement("input"); inp.type = "file"; inp.accept = ".json,application/json";
        inp.onchange = async function () { try { var o = JSON.parse(await inp.files[0].text()); EDIT_FIELDS.forEach(function (f) { if (o[f] !== undefined) w[f] = o[f]; }); persist(); I = await loadWorkImages(w); renderEditor(); } catch (er) { alert("Tệp JSON không hợp lệ."); } };
        inp.click();
      }
      else if (a === "reset") { if (confirm("Bỏ mọi chỉnh sửa của anh và quay về kịch bản gốc?")) { setOverride(w.id, null); var base = (DB().works || []).filter(function (x) { return x.id === w.id; })[0]; if (base) { w = resolve(base); } I = await loadWorkImages(w); AUD.nk = null; renderEditor(); if (opts.onChange) opts.onChange(w); } }
      else if (a === "delwork") { if (confirm("Xoá hẳn tác phẩm «" + w.title + "» của anh?")) { deleteCustom(w.id); close(); } }
    });
    ov.addEventListener("input", function (e) {
      if (!editMode) return; var el = e.target, card = el.closest(".av-st");
      if (el.dataset.f) { w[el.dataset.f] = el.value; clearTimeout(el._t); el._t = setTimeout(persist, 400); return; }
      if (card && el.dataset.sf) {
        var s = w.steps[+card.dataset.j]; if (!s) return; var f = el.dataset.sf;
        if (f === "k") s.k = el.checked ? 1 : 0; else if (f === "cardbig") s.card = Object.assign(s.card || {}, { big: el.value }); else if (f === "cardsub") s.card = Object.assign(s.card || {}, { sub: el.value });
        else s[f] = el.value;
        clearTimeout(el._t); el._t = setTimeout(persist, 400);
      }
    });
    ov.addEventListener("change", function (e) { if (!editMode) return; var el = e.target; if (el.dataset.f === "type") { w.type = el.value; persist(); } if (el.dataset.sf === "k") { var card = el.closest(".av-st"), s = w.steps[+card.dataset.j]; s.k = el.checked ? 1 : 0; persist(); } });
    global.addEventListener("resize", function () { if (editMode) drawBoxes(); });

    // khởi động
    syncUI();
    (async function () {
      var ph = $('[data-v="scene"]'); ph.textContent = "⏳ Đang tải ảnh tác phẩm…";
      I = await loadWorkImages(w, function (d, n) { ph.textContent = "⏳ Đang tải ảnh " + d + "/" + n + "…"; });
      rebuild(); t = posterT(V); atPoster = true; frame();
      if (opts.edit) toggleEditor(true);
    })();
    return { close: close, get V() { return V; }, get work() { return w; } };
  }

  /* tác phẩm mới của anh */
  function newWork(seed) {
    var id = "my-" + Date.now().toString(36);
    var w = Object.assign({ id: id, custom: true, type: "painting", title: "Tác phẩm mới", artist: "", date: "", y: new Date().getFullYear(), era: "hien-dai", where: "", place: null,
      rights: "own", hook: "Thoạt nhìn… Nhưng nếu nhìn thật kỹ, bạn sẽ thấy…", intro: "", end: "Giờ thì bạn đã hiểu vì sao người ta có thể ngắm nó hàng giờ.",
      img: [{ user: true, w: 1000, h: 1000 }], steps: [], tags: [] }, seed || {});
    saveCustom(w); return w;
  }

  global.ArtVideo = {
    version: VERSION, open: open, edit: function (w, o) { o = o || {}; o.edit = true; return open(w, o); }, newWork: newWork,
    resolve: resolve, listCustom: listCustom, saveCustom: saveCustom, deleteCustom: deleteCustom, getOverride: getOverride,
    userImageURL: userImageURL, hasUserImage: hasUserImage, commonsThumb: commonsThumb, commonsPage: commonsPage, typeOf: typeOf, trendLine: trendLine,
    _t: { narrate: narrate, build: build, renderArt: renderArt, pickSteps: pickSteps, loadWorkImages: loadWorkImages, prepImage: prepImage, commonsCands: commonsCands, boxView: boxView, fullView: fullView,
          chapters: chapters, postText: postText, cover: cover, DEF: DEF, sceneAt: sceneAt, LY: LY }
  };
})(window);
