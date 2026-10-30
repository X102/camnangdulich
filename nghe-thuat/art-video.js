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
   v1.1: ghi nguồn dưới từng lời giải + danh sách nguồn cuối video + tên tác giả ảnh; nhãn «Có dùng AI» và lời nhắc
     có thể sai sót (đầu/cuối video, tuỳ chọn đọc); gợi ý câu mở đầu (riêng từng tác phẩm + mẫu chung, 🎲);
     vùng an toàn TikTok/Reels + cỡ chữ phụ đề; câu hỏi gợi bình luận; mẫu lệnh nhờ AI soạn kịch bản (JSON);
     tìm ảnh Wikimedia Commons trong trình chỉnh; xuất hàng loạt.
     Tham khảo mã nguồn mở: MoneyPrinterTurbo (vị trí phụ đề, lệnh soạn kịch bản), ShortGPT (lệnh trả JSON),
     short-video-maker (tuỳ chọn phụ đề), sign-ai-media (nhãn nội dung AI), Openverse (API ảnh Commons).
   v1.2: 🖼️ ảnh bìa chỉnh được (nền: ảnh/khung hình/ảnh của anh, tâm điểm, phóng to, kéo dịch, 3 dòng chữ, vị trí),
     PHẢI chốt trước khi xuất (cả khi xuất hàng loạt), chèn ảnh bìa vào 0,8 giây đầu video; 📤 tự tải về máy, lưu thẳng vào
     thư mục (File System Access), tự đăng YouTube (OAuth Google Identity Services + tải lên resumable như mẫu
     youtube/api-samples cors_upload.js, đặt ảnh thu nhỏ, khai báo nội dung tổng hợp), nút đăng nhanh Facebook/TikTok/Instagram.
   v1.3: trang Facebook «Giải mã Nghệ Thuật» (chữ ký, mã QR, logo ở màn kết — brand/brand.js); 🌐 video 6 thứ tiếng: Việt, Anh, Nhật,
     Trung (giản thể), Nga, Hàn — kịch bản dịch sẵn ở data/i18n/<lang>.js (dạng {chữ hiện|cách đọc} để giọng AI đọc đúng số, năm, tên),
     nhờ AI dịch cho tác phẩm của anh; phông và xuống dòng riêng cho chữ Nhật/Trung/Hàn; chữ đăng bài, hashtag, tiêu đề + ngôn ngữ
     YouTube, mục lục, phụ đề theo ngôn ngữ; chọn giọng cho từng tiếng: Piper (Việt, Anh, Nga, Trung «Chaowen» qua pinyin) hoặc
     10 giọng Supertonic 3 (Việt, Anh, Nhật, Hàn, Nga); xuất hàng loạt nhiều ngôn ngữ một lượt.
     Tham khảo mã nguồn mở: supertone-inc/supertonic (web/helper.js, MIT), OHF-Voice/piper1-gpl (phonemize_chinese.py — cách đánh số
     pinyin), pinyin-pro (MIT), ayutaz/piper-plus (so sánh cách làm giọng Nhật/Trung/Hàn trong trình duyệt).
   Phụ thuộc: ../assets/tour-video.js (v2.2+, TourVideo.lib).
   Gọi: ArtVideo.open(work)  ·  ArtVideo.edit(work)  ·  ArtVideo.newWork()
   ===================================================================== */
(function (global) {
  "use strict";
  var TVv = global.TourVideo;
  if (!TVv || !TVv.lib) { if (global.console) console.error("art-video.js cần assets/tour-video.js (v2.1+)"); return; }
  var L = TVv.lib, VERSION = "1.3";
  var clamp = L.clamp, lerp = L.lerp, seg = L.seg, ease = L.ease, easeOut = L.easeOut, F = L.F, C = L.C, wrap = L.wrap, rr = L.rr, escH = L.escH,
      fmtClock = L.fmtClock, SAY = L.SAY, AIV = L.AIV, MUSIC = L.MUSIC, sleep = L.sleep;
  var SERIF = '"Times New Roman", "Noto Serif", "Liberation Serif", Georgia, serif';
  function FS(weight, px, italic) { return (italic ? "italic " : "") + weight + " " + Math.max(1, Math.round(px)) + "px " + SERIF; }
  var GOLD = "#f2c14e", GOLD2 = "#c8a24b", NAVY = "#0f2138";
  var DB = function () { return global.ART_DB || { types: [], eras: [], works: [] }; };
  function typeOf(id) { var t = (DB().types || []).filter(function (x) { return x.id === id; })[0]; return t || { id: id, vi: id, icon: "🎨", noun: "một tác phẩm" }; }
  function clone(o) { return JSON.parse(JSON.stringify(o)); }

  /* ---------------- 1b. NGÔN NGỮ VIDEO (v1.3) ----------------
     Video xuất được bằng 6 thứ tiếng: 🇻🇳 Việt · 🇬🇧 Anh · 🇯🇵 Nhật · 🇨🇳 Trung (giản thể) · 🇷🇺 Nga · 🇰🇷 Hàn.
     - Kịch bản dịch nằm ở data/i18n/<lang>.js (ART_I18N[lang].works[id]) — tải khi chọn ngôn ngữ; bản dịch của anh (nhờ AI dịch)
       lưu ở localStorage «av_tr_<lang>_<id>» và được ưu tiên.
     - Chữ hiện / chữ đọc: {hiển thị|cách đọc} — người xem thấy «1930», giọng đọc đọc «nineteen thirty» (số, năm, thế kỷ, chữ khó).
     - Phông riêng cho Nhật/Trung/Hàn, xuống dòng theo từ (Intl.Segmenter) và không để dấu câu đứng đầu dòng (kinsoku).
     - Chữ trên video (nhãn, lời nhắc AI, lời mời theo dõi, chữ đăng bài, tiêu đề YouTube, mục lục) theo bảng TX bên dưới. */
  var LANGS = ["vi", "en", "ja", "zh", "ru", "ko"], I18N_V = 1;
  var LINFO = { vi: { name: "Tiếng Việt", flag: "🇻🇳", yt: "vi" }, en: { name: "English", flag: "🇬🇧", yt: "en" }, ja: { name: "日本語", flag: "🇯🇵", yt: "ja" },
                zh: { name: "中文 (简体)", flag: "🇨🇳", yt: "zh-Hans" }, ru: { name: "Русский", flag: "🇷🇺", yt: "ru" }, ko: { name: "한국어", flag: "🇰🇷", yt: "ko" } };
  var LCUR = "vi";                                           // ngôn ngữ của khung hình đang vẽ (phông, xuống dòng)
  function isCJK(l) { return l === "ja" || l === "zh"; }
  function plRu(n, a, b, c) { n = Math.abs(n) % 100; var n1 = n % 10; if (n > 10 && n < 20) return c; if (n1 > 1 && n1 < 5) return b; if (n1 === 1) return a; return c; }
  function koHas(word) { var s = String(word || "").replace(/[\s》」』)\]”"'.!?…]+$/, ""), c = s.charCodeAt(s.length - 1); return c >= 0xAC00 && c <= 0xD7A3 ? (c - 0xAC00) % 28 !== 0 : false; }
  function josa(word, a, b) { return word + (koHas(word) ? a : b); }
  function quoteT(title, l) {
    var t = String(title || ""); if (/[«»“”"『』「」《》]/.test(t)) return t;
    return l === "en" ? "“" + t + "”" : l === "ja" ? "『" + t + "』" : l === "zh" || l === "ko" ? "《" + t + "》" : l === "ru" ? "«" + t + "»" : "«" + t + "»";
  }
  var EN_N = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen"];
  var JA_TSU = ["", "ひとつ", "ふたつ", "みっつ", "よっつ", "いつつ", "むっつ", "ななつ", "やっつ", "ここのつ"], JA_KO = { 10: "じゅっこ", 11: "じゅういっこ", 12: "じゅうにこ", 13: "じゅうさんこ", 14: "じゅうよんこ" };
  var RU_NF = ["ноль", "одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать"];
  var KO_N = ["", "한", "두", "세", "네", "다섯", "여섯", "일곱", "여덟", "아홉", "열", "열한", "열두", "열세", "열네"];
  function cap1(s) { return s ? s.charAt(0).toUpperCase() + s.slice(1) : s; }
  // số đếm chi tiết kèm cách đọc, dùng trong mẫu câu mở đầu
  function numX(l, n, capital) {
    if (l === "en") return "{" + n + "|" + (capital ? cap1(EN_N[n] || String(n)) : (EN_N[n] || String(n))) + "}";
    if (l === "ja") return n <= 9 ? "{" + n + "つ|" + JA_TSU[n] + "}" : "{" + n + "個|" + (JA_KO[n] || n + "こ") + "}";
    if (l === "zh") return "{" + n + "个|" + (n === 2 ? "两" : AIV.zhNumbers(String(n))) + "个}";
    if (l === "ru") return "{" + n + "|" + (capital ? cap1(RU_NF[n] || String(n)) : (RU_NF[n] || String(n))) + "}";
    if (l === "ko") return "{" + n + "가지|" + (KO_N[n] || n) + " 가지}";
    return String(n);
  }
  var TX = {
    vi: {
      types: { folk: ["Tranh dân gian", "một bức tranh"], painting: ["Hội họa", "một bức tranh"], sculpture: ["Điêu khắc", "một pho tượng"], artifact: ["Cổ vật", "một cổ vật"], architecture: ["Kiến trúc", "một công trình"], music: ["Âm nhạc", "một bài hát"] },
      detail: "❓ CHI TIẾT ", src: "📚 Nguồn: ", cta: "💬 Chi tiết số mấy làm bạn bất ngờ nhất? Bình luận số nhé!",
      aiBadge: "🤖 Có dùng AI", aiStart: "🤖 Video có dùng AI và có thể còn sai sót — rất mong bạn góp ý.",
      follow: "Theo dõi để xem những tác phẩm tiếp theo nhé.", followCta: "Theo dõi để xem tác phẩm tiếp theo ✦", outroHead: "🎨 GIẢI MÃ TÁC PHẨM",
      refs: "📚 Nguồn tham khảo", photos: "📷 Ảnh: ", musicOwn: "Nhạc: do tác giả video chọn", musicSyn: "Nhạc nền tự tổng hợp", voice: "Giọng đọc AI: ",
      ownPhoto: "Ảnh: tư liệu của tác giả video", commons: "Ảnh: Wikimedia Commons", noImg: "Chưa tải được ảnh", noImgUser: "📂 Hãy nạp ảnh của anh cho tác phẩm này",
      coverL1: "GIỜ THÌ TÔI MỚI HIỂU…", coverL1b: "GIẢI MÃ TÁC PHẨM", coverL3: "{n} chi tiết ít ai để ý",
      chIntro: "Mở đầu", chEnd: "Lời kết", inVideo: "Trong video:", comment: "Bạn đã để ý chi tiết nào trước khi xem video? Bình luận nhé 👇", postRefs: "📚 Nguồn tham khảo:",
      hashtags: ["#GiờThìTôiMớiHiểu", "#NghệThuậtViệtNam"], tagline: "Giải mã nghệ thuật Việt Nam",
      sample: "Xin chào! Đây là giọng đọc thử cho các video giải mã tác phẩm nghệ thuật Việt Nam."
    },
    en: {
      types: { folk: ["Folk print", "folk print"], painting: ["Painting", "painting"], sculpture: ["Sculpture", "statue"], artifact: ["Artifact", "artifact"], architecture: ["Architecture", "building"], music: ["Music", "song"] },
      head: /^(Now I (?:finally )?(?:understand|get it|see))[,:]?\s*(.*)$/i,
      trend: function (noun, music) { return music ? "Now I finally understand why people can listen to one song for hours…" : "Now I finally understand why people can spend hours looking at a single " + noun + "…"; },
      detail: "❓ DETAIL ", src: "📚 Source: ", cta: "💬 Which detail surprised you most? Comment its number!",
      aiBadge: "🤖 Made with AI", aiStart: "🤖 This video uses AI and may contain mistakes — corrections are welcome.",
      aiText: "This video was made with AI assistance (AI voice, automated editing). The creator is not an art historian, so there may be mistakes — please check the sources and let us know.",
      aiSay: "This video uses artificial intelligence and may contain mistakes. Corrections are always welcome.",
      follow: "Follow for more Vietnamese art, decoded.", followCta: "Follow for the next artwork ✦", outroHead: "🎨 VIETNAMESE ART, DECODED",
      refs: "📚 Sources", photos: "📷 Images: ", musicOwn: "Music: chosen by the creator", musicSyn: "Music: synthesized", voice: "AI voice: ",
      ownPhoto: "Photo: the creator's own", commons: "Image: Wikimedia Commons", noImg: "Image not available",
      coverL1: "NOW I GET IT…", coverL1b: "ART, DECODED", coverL3: "{n} details most people miss",
      chIntro: "Intro", chEnd: "Conclusion", inVideo: "In this video:", comment: "Which detail did you notice before watching? Tell us in the comments 👇", postRefs: "📚 Sources:",
      hashtags: ["#VietnameseArt", "#ArtHistory", "#ArtExplained", "#Vietnam"], tagline: "Vietnamese art, decoded",
      yt: function (t, n) { return "Decoding " + t + ": " + n + " details most people miss"; },
      end: function (T) { return "Now you understand why people can spend hours with " + T + "."; },
      sample: "Hello! This is a sample of the AI voice for our Vietnamese art videos.",
      pos: { tl: "top-left corner", tr: "top-right corner", bl: "bottom-left corner", br: "bottom-right corner", t: "top", b: "bottom", l: "left side", r: "right side", c: "center" },
      openers: function (T, F, n, music, pos) {
        var a = /^[aeiou]/i.test(F) ? "an " : "a ";
        return music ? ["You've heard " + T + " many times, but have you ever really listened?", n >= 2 ? numX("en", n, true) + " stories behind " + T + " that not everyone knows." : "",
          "Everyone has heard " + T + ", but few know how it was born.", "Wait! Hear the story behind this " + F + "."]
        : ["There's a detail in " + T + " that most people look right past.", n >= 2 ? numX("en", n, true) + " small details in " + T + " tell one big story." : "",
          "You've seen " + T + " many times, but have you ever really looked?", pos ? "Wait! Look at the " + pos + " of this " + F + "." : "Wait! Take a closer look at this " + F + ".",
          "Pause the video and count: how many strange details can you find in this " + F + "?", "Everyone has seen " + T + ", but few know the story behind it.", "Think this is just " + a + F + "? Look again."];
      }
    },
    ja: {
      types: { folk: ["民間版画", "版画"], painting: ["絵画", "絵"], sculpture: ["彫刻", "像"], artifact: ["古美術", "古美術品"], architecture: ["建築", "建物"], music: ["音楽", "歌"] },
      trend: function (noun, music) { return music ? "一曲の歌を何時間も聴いていられる理由が、やっと分かった…" : noun + "を何時間も眺めていられる理由が、やっと分かった…"; },
      detail: "❓ 細部 ", src: "📚 出典：", cta: "💬 いちばん驚いたのは何番？番号でコメントしてね！",
      aiBadge: "🤖 AI使用", aiStart: "🤖 この動画はAIを使用しており、誤りがあるかもしれません。ご指摘お待ちしています。",
      aiText: "この動画はAIの支援で制作しています（AI音声・自動編集）。制作者は専門家ではないため、誤りが含まれる可能性があります。出典もあわせてご確認ください。",
      aiSay: "この動画は人工知能を使っており、誤りがあるかもしれません。ご指摘をお待ちしています。",
      follow: "フォローして、次の作品もお楽しみに。", followCta: "フォローして次の作品へ ✦", outroHead: "🎨 ベトナム美術を読み解く",
      refs: "📚 参考資料", photos: "📷 画像：", musicOwn: "音楽：制作者が選曲", musicSyn: "音楽：自動生成", voice: "AI音声：",
      ownPhoto: "写真：制作者所蔵", commons: "画像：ウィキメディア・コモンズ", noImg: "画像を読み込めません",
      coverL1: "やっと分かった…", coverL1b: "名作を読み解く", coverL3: "見落としがちな{nつ}の秘密",
      chIntro: "はじめに", chEnd: "まとめ", inVideo: "この動画で紹介する細部：", comment: "動画を見る前に気づいた細部はありましたか？コメントで教えてください👇", postRefs: "📚 参考資料：",
      hashtags: ["#ベトナム美術", "#美術解説", "#アート", "#ベトナム"], tagline: "ベトナム美術を、ひとつずつ読み解く",
      yt: function (t, n) { return t + " 見落としがちな" + n + (n <= 9 ? "つ" : "") + "の秘密"; },
      end: function (T) { return "これで、" + T + "を何時間も眺めていられる理由が分かりましたね。"; },
      sample: "こんにちは。ベトナム美術を読み解く動画の、AI音声のサンプルです。",
      pos: { tl: "左上の隅", tr: "右上の隅", bl: "左下の隅", br: "右下の隅", t: "上の部分", b: "下の部分", l: "左側", r: "右側", c: "真ん中" },
      openers: function (T, F, n, music, pos) {
        return music ? [T + "を何度も聞いたことがあっても、本当に耳を傾けたことはありますか？", n >= 2 ? T + "には、あまり知られていない" + numX("ja", n) + "の物語があります。" : "",
          "誰もが" + T + "を知っています。でも、この歌がどう生まれたかを知る人は多くありません。", "スクロールする前に、この歌の物語を聞いてください。"]
        : [T + "には、多くの人が見過ごしてしまう細部があります。", n >= 2 ? T + "の" + numX("ja", n) + "の小さな細部が、ひとつの大きな物語を語っています。" : "",
          T + "を何度も見たことがあっても、じっくり見たことはありますか？", pos ? "ちょっと待って！この作品の" + pos + "を見てください。" : "ちょっと待って！この作品をよく見てください。",
          "動画を止めて数えてみてください。この作品の不思議な細部、いくつ見つかりますか？", "誰もが" + T + "を見たことがあります。でも、その裏の物語を知る人は多くありません。", "ただの" + F + "だと思いますか？もう一度よく見てください。"];
      }
    },
    zh: {
      types: { folk: ["民间年画", "年画"], painting: ["绘画", "画作"], sculpture: ["雕塑", "雕像"], artifact: ["文物", "文物"], architecture: ["建筑", "建筑"], music: ["音乐", "歌曲"] },
      trend: function (noun, music) { return music ? "现在我终于明白，为什么有人能把一首歌听上好几个小时……" : "现在我终于明白，为什么有人能盯着" + noun + "看上好几个小时……"; },
      head: /^(现在我终于明白)[，,]?\s*(.*)$/,
      detail: "❓ 细节 ", src: "📚 出处：", cta: "💬 哪个细节最让你意外？评论区打出编号！",
      aiBadge: "🤖 AI辅助制作", aiStart: "🤖 本视频使用了AI，内容可能有误，欢迎指正。",
      aiText: "本视频在AI辅助下制作（AI配音、自动剪辑）。作者并非艺术史专家，内容可能存在错误，欢迎核对出处并指正。",
      aiSay: "本视频使用了人工智能，内容可能有误，欢迎指正。",
      follow: "关注我们，下期继续解读越南艺术。", followCta: "关注我们，看下一件作品 ✦", outroHead: "🎨 解码越南艺术",
      refs: "📚 参考资料", photos: "📷 图片：", musicOwn: "音乐：作者自选", musicSyn: "音乐：自动合成", voice: "AI配音：",
      ownPhoto: "图片：作者自有", commons: "图片：维基共享资源", noImg: "图片无法加载",
      coverL1: "现在我终于明白了……", coverL1b: "名作解码", coverL3: "{n}个容易被忽略的细节",
      chIntro: "开场", chEnd: "结语", inVideo: "本期细节：", comment: "看视频之前，你注意到哪个细节了？评论区告诉我们👇", postRefs: "📚 参考资料：",
      hashtags: ["#越南艺术", "#艺术解读", "#名画解读", "#越南"], tagline: "一件一件，读懂越南艺术",
      yt: function (t, n) { return "解码" + t + "：" + n + "个容易被忽略的细节"; },
      end: function (T) { return "现在你明白了，为什么有人能对着" + T + "看上好几个小时。"; },
      sample: "你好！这是越南艺术解读视频的AI配音试听。",
      pos: { tl: "左上角", tr: "右上角", bl: "左下角", br: "右下角", t: "上方", b: "下方", l: "左侧", r: "右侧", c: "正中间" },
      openers: function (T, F, n, music, pos) {
        return music ? [T + "你可能听过很多遍，可你真的仔细听过吗？", n >= 2 ? "关于" + T + "，有" + numX("zh", n) + "不为人知的故事。" : "",
          "人人都听过" + T + "，却很少有人知道它是怎么诞生的。", "先别划走！听听这首歌背后的故事。"]
        : [T + "里有一个细节，很多人看了却没看见。", n >= 2 ? T + "里的" + numX("zh", n) + "小细节，讲的是一个大故事。" : "",
          T + "你可能看过很多次，但真的仔细看过吗？", pos ? "先别划走！看看这件作品的" + pos + "。" : "先别划走！仔细看看这件作品。",
          "暂停视频数一数：这件作品里，你能找到几个奇怪的细节？", "人人都见过" + T + "，却很少有人知道背后的故事。", "你以为这只是普通的" + F + "？再仔细看看。"];
      }
    },
    ru: {
      types: { folk: ["Народная гравюра", "гравюра", "гравюру", "гравюре", "этой гравюры", "этой гравюре"], painting: ["Живопись", "картина", "картину", "картине", "этой картины", "этой картине"],
               sculpture: ["Скульптура", "статуя", "статую", "статуе", "этой статуи", "этой статуе"], artifact: ["Древности", "артефакт", "артефакт", "артефакте", "этого артефакта", "этом артефакте"],
               architecture: ["Архитектура", "постройка", "постройку", "постройке", "этой постройки", "этой постройке"], music: ["Музыка", "песня", "песню", "песне", "этой песни", "этой песне"] },
      head: /^(Теперь я (?:наконец )?понимаю)[,:]?\s*(.*)$/i,
      trend: function (noun, music) { return music ? "Теперь я понимаю, почему одну песню можно слушать часами…" : "Теперь я понимаю, почему на одно произведение можно смотреть часами…"; },
      detail: "❓ ДЕТАЛЬ ", src: "📚 Источник: ", cta: "💬 Какая деталь удивила вас больше всего? Напишите её номер!",
      aiBadge: "🤖 Сделано с ИИ", aiStart: "🤖 В видео использован ИИ, возможны ошибки — будем рады поправкам.",
      aiText: "Видео создано с помощью ИИ (синтез речи, автоматический монтаж). Автор не искусствовед, поэтому возможны неточности — сверяйтесь с источниками и пишите нам.",
      aiSay: "В этом видео использован искусственный интеллект, возможны ошибки. Будем рады вашим поправкам.",
      follow: "Подписывайтесь, чтобы не пропустить новые разборы.", followCta: "Подписывайтесь — дальше новое произведение ✦", outroHead: "🎨 ВЬЕТНАМСКОЕ ИСКУССТВО: РАЗБОР",
      refs: "📚 Источники", photos: "📷 Изображения: ", musicOwn: "Музыка: выбор автора", musicSyn: "Музыка: синтезирована", voice: "ИИ-голос: ",
      ownPhoto: "Фото: из архива автора", commons: "Изображение: Викисклад", noImg: "Изображение недоступно",
      coverL1: "ТЕПЕРЬ Я ПОНИМАЮ…", coverL1b: "РАЗБОР ШЕДЕВРА", coverL3: "{n} {n:деталь|детали|деталей}, которые мало кто замечает",
      chIntro: "Вступление", chEnd: "Итог", inVideo: "В этом видео:", comment: "Какую деталь вы заметили ещё до просмотра? Пишите в комментариях 👇", postRefs: "📚 Источники:",
      hashtags: ["#ВьетнамскоеИскусство", "#ИсторияИскусства", "#Искусство", "#Вьетнам"], tagline: "Вьетнамское искусство — деталь за деталью",
      yt: function (t, n) { return t + ": " + n + " " + plRu(n, "деталь", "детали", "деталей") + ", которые мало кто замечает"; },
      end: function (T) { return "Теперь вы понимаете, почему на произведение " + T + " можно смотреть часами."; },
      sample: "Здравствуйте! Это пример ИИ-голоса для наших видео о вьетнамском искусстве.",
      pos: { tl: "левый верхний угол", tr: "правый верхний угол", bl: "левый нижний угол", br: "правый нижний угол", t: "верхнюю часть", b: "нижнюю часть", l: "левую сторону", r: "правую сторону", c: "центр" },
      openers: function (T, F, n, music, pos, f) {
        f = f || ["", "произведение", "произведение", "произведении", "этого произведения", "этом произведении"];
        return music ? ["Вы слышали " + T + " много раз, но вслушивались ли по-настоящему?", n >= 2 ? numX("ru", n, true) + " " + plRu(n, "история", "истории", "историй") + " о песне " + T + ", которые знает не каждый." : "",
          "Все слышали песню " + T + ", но мало кто знает, как она родилась.", "Не листайте! Послушайте историю этой песни."]
        : ["В " + f[3] + " " + T + " есть деталь, которую большинство не замечает.", n >= 2 ? numX("ru", n, true) + " " + plRu(n, "маленькая деталь", "маленькие детали", "маленьких деталей") + " в " + f[3] + " " + T + " рассказывают целую историю." : "",
          "Вы видели " + f[2] + " " + T + " много раз, но присматривались ли по-настоящему?", pos ? "Не листайте! Посмотрите на " + pos + " " + f[4] + "." : "Не листайте! Присмотритесь к " + f[5].replace(/^этом /, "этому ").replace(/^этой /, "этой ") + ".",
          "Поставьте видео на паузу и посчитайте: сколько странных деталей вы найдёте в " + f[5] + "?", "Все видели " + f[2] + " " + T + ", но мало кто знает историю этого произведения.", "Думаете, это просто " + f[1] + "? Посмотрите ещё раз."];
      }
    },
    ko: {
      types: { folk: ["민화", "민화"], painting: ["회화", "그림"], sculpture: ["조각", "조각상"], artifact: ["유물", "유물"], architecture: ["건축", "건축물"], music: ["음악", "노래"] },
      head: /^(이제야 알겠다)[,，]?\s*(.*)$/,
      trend: function (noun, music) { return music ? "이제야 알겠다, 왜 사람들이 노래 한 곡을 몇 시간씩 듣는지…" : "이제야 알겠다, 왜 사람들이 " + noun + " 하나를 몇 시간씩 바라보는지…"; },
      detail: "❓ 디테일 ", src: "📚 출처: ", cta: "💬 가장 놀라웠던 디테일은 몇 번인가요? 번호로 댓글 남겨 주세요!",
      aiBadge: "🤖 AI 활용", aiStart: "🤖 이 영상은 AI를 활용해 만들어서 오류가 있을 수 있어요. 바로잡아 주시면 감사하겠습니다.",
      aiText: "이 영상은 AI의 도움을 받아 만들었습니다(AI 음성, 자동 편집). 제작자는 전문가가 아니어서 오류가 있을 수 있어요. 출처를 함께 확인해 주세요.",
      aiSay: "이 영상은 인공지능을 활용해서 오류가 있을 수 있어요. 의견을 남겨 주세요.",
      follow: "팔로우하고 다음 작품도 함께 봐요.", followCta: "팔로우하고 다음 작품 보기 ✦", outroHead: "🎨 베트남 미술 해설",
      refs: "📚 참고 자료", photos: "📷 이미지: ", musicOwn: "음악: 제작자 선택", musicSyn: "음악: 자동 합성", voice: "AI 음성: ",
      ownPhoto: "사진: 제작자 소장", commons: "이미지: 위키미디어 공용", noImg: "이미지를 불러올 수 없어요",
      coverL1: "이제야 알겠다…", coverL1b: "명작 해설", coverL3: "대부분 놓치는 디테일 {n}가지",
      chIntro: "인트로", chEnd: "마무리", inVideo: "이번 영상의 디테일:", comment: "영상을 보기 전에 눈치챈 디테일이 있었나요? 댓글로 알려 주세요 👇", postRefs: "📚 참고 자료:",
      hashtags: ["#베트남미술", "#미술해설", "#명화", "#베트남"], tagline: "베트남 미술, 하나씩 풀어 보기",
      yt: function (t, n) { return t + " 대부분 놓치는 디테일 " + n + "가지"; },
      end: function (T) { return "이제 " + josa(T, "을", "를") + " 몇 시간씩 바라보는 이유를 아시겠죠?"; },
      sample: "안녕하세요! 베트남 미술 해설 영상의 AI 음성 샘플이에요.",
      pos: { tl: "왼쪽 위 구석을", tr: "오른쪽 위 구석을", bl: "왼쪽 아래 구석을", br: "오른쪽 아래 구석을", t: "위쪽을", b: "아래쪽을", l: "왼쪽을", r: "오른쪽을", c: "한가운데를" },
      openers: function (T, F, n, music, pos) {
        return music ? [T + ", 여러 번 들어 보셨죠? 그런데 정말 귀 기울여 들어 본 적 있나요?", n >= 2 ? T + "에 숨은, 잘 알려지지 않은 이야기 " + numX("ko", n) + "." : "",
          "누구나 아는 노래 " + T + ". 하지만 이 노래가 어떻게 태어났는지 아는 사람은 많지 않아요.", "넘기지 마세요! 이 노래에 얽힌 이야기를 들어 보세요."]
        : [T + "에는 많은 사람이 그냥 지나치는 디테일이 있어요.", n >= 2 ? T + " 속 작은 디테일 " + numX("ko", n) + "가 하나의 큰 이야기를 들려줘요." : "",
          T + ", 여러 번 보셨죠? 그런데 정말 자세히 본 적 있나요?", pos ? "넘기지 마세요! 이 " + F + "의 " + pos + " 보세요." : "넘기지 마세요! 이 " + josa(F, "을", "를") + " 자세히 보세요.",
          "영상을 멈추고 세어 보세요. 이 " + F + "에서 이상한 디테일을 몇 개나 찾을 수 있나요?", "누구나 본 적 있는 " + T + ". 하지만 그 뒤에 숨은 이야기를 아는 사람은 많지 않아요.", "그냥 평범한 " + josa(F, "이라고요", "라고요") + "? 다시 한번 보세요."];
      }
    }
  };
  function TXL(l) { return TX[l] || TX.vi; }
  function typeName(type, l) { var t = TXL(l).types[type]; return t ? t[0] : typeOf(type).vi; }

  /* phông chữ theo ngôn ngữ (chữ La-tinh vẫn lấy Segoe UI/Times; chữ Nhật/Trung/Hàn lấy phông đúng vùng để không lẫn nét chữ Hán) */
  var FONTS = {
    ja: { s: '"Segoe UI", "Yu Gothic UI", "Yu Gothic", YuGothic, "Hiragino Sans", "Hiragino Kaku Gothic ProN", Meiryo, "Noto Sans CJK JP", "Noto Sans JP", "Segoe UI Emoji", "Apple Color Emoji", "Noto Color Emoji", sans-serif',
          r: '"Times New Roman", "Yu Mincho", YuMincho, "Hiragino Mincho ProN", "Noto Serif CJK JP", "Noto Serif JP", "MS PMincho", "Segoe UI Emoji", "Noto Color Emoji", serif' },
    zh: { s: '"Segoe UI", "Microsoft YaHei UI", "Microsoft YaHei", "PingFang SC", "Noto Sans CJK SC", "Noto Sans SC", "Source Han Sans SC", "Segoe UI Emoji", "Apple Color Emoji", "Noto Color Emoji", sans-serif',
          r: '"Times New Roman", "Noto Serif CJK SC", "Noto Serif SC", "Songti SC", STSong, SimSun, "Segoe UI Emoji", "Noto Color Emoji", serif' },
    ko: { s: '"Segoe UI", "Malgun Gothic", "Apple SD Gothic Neo", "Noto Sans CJK KR", "Noto Sans KR", "Segoe UI Emoji", "Apple Color Emoji", "Noto Color Emoji", sans-serif',
          r: '"Times New Roman", "Noto Serif CJK KR", "Noto Serif KR", Batang, "Nanum Myeongjo", "Segoe UI Emoji", "Noto Color Emoji", serif' }
  };
  F = function (weight, px, italic) { var f = FONTS[LCUR]; return f ? weight + " " + Math.max(1, Math.round(px)) + "px " + f.s : L.F(weight, px, italic); };
  FS = function (weight, px, italic) { var f = FONTS[LCUR]; return (italic && !f ? "italic " : "") + weight + " " + Math.max(1, Math.round(px)) + "px " + (f ? f.r : SERIF); };
  // xuống dòng: Nhật/Trung theo từ (Intl.Segmenter), không để dấu câu đứng đầu dòng / ngoặc mở đứng cuối dòng
  var SEGR = {}, KCLOSE = /^[、。，．,.！？!?：:；;）)」』】〉》”’…ー〜~％%・]+$/, KOPEN = /^[（(「『【〈《“‘]+$/;
  var KSTART = /^[、。，．,.！？!?：:；;）)」』】〉》”’…ー〜~％%・ぁぃぅぇぉっゃゅょゎゕゖァィゥェォッャュョヮヵヶ々]+/;   // không đứng đầu dòng (kinsoku)
  function segOf(l) { if (SEGR[l] !== undefined) return SEGR[l]; try { SEGR[l] = new Intl.Segmenter(l === "zh" ? "zh-Hans" : l, { granularity: "word" }); } catch (e) { SEGR[l] = null; } return SEGR[l]; }
  function cjkTokens(text, l) {
    var sg = segOf(l), raw = [], out = [];
    if (sg) { var it = sg.segment(text)[Symbol.iterator](), r; while (!(r = it.next()).done) raw.push(r.value.segment); } else raw = Array.from(text);
    raw.forEach(function (t) { if (out.length && (KCLOSE.test(t) || KOPEN.test(out[out.length - 1]))) out[out.length - 1] += t; else out.push(t); });
    return out;
  }
  wrap = function (ctx, text, maxW, maxLines) {
    if (!isCJK(LCUR)) return L.wrap(ctx, text, maxW, maxLines);
    text = String(text || "").replace(/\s+/g, " ").trim(); if (!text) return [];
    var toks = cjkTokens(text, LCUR), lines = [], cur = "", trunc = false;
    for (var i = 0; i < toks.length && !trunc; i++) {
      var tk = toks[i];
      if (ctx.measureText(cur + tk).width <= maxW) { cur += tk; continue; }
      var km = cur && tk.match(KSTART); if (km) { cur += km[0]; tk = tk.slice(km[0].length); if (!tk) continue; if (ctx.measureText(cur + tk).width <= maxW) { cur += tk; continue; } }
      if (cur) { lines.push(cur); cur = ""; if (maxLines && lines.length >= maxLines) { trunc = true; break; } }
      var ch = Array.from(tk.replace(/^\s+/, ""));
      for (var c = 0; c < ch.length; c++) {
        if (cur && ctx.measureText(cur + ch[c]).width > maxW && !KSTART.test(ch[c])) { lines.push(cur); cur = ""; if (maxLines && lines.length >= maxLines) { trunc = true; break; } }
        cur += ch[c];
      }
    }
    if (!trunc && cur) lines.push(cur);
    if (maxLines && lines.length > maxLines) { lines.length = maxLines; trunc = true; }
    if (trunc && lines.length) { var last = lines[lines.length - 1]; while (last.length > 1 && ctx.measureText(last + "…").width > maxW) last = last.slice(0, -1); lines[lines.length - 1] = last.replace(/[、。，\s]+$/, "") + "…"; }
    return lines.map(function (s) { return s.trim(); });
  };
  function wordsOf(line) { return isCJK(LCUR) ? cjkTokens(line, LCUR) : line.split(" "); }
  function JOIN() { return isCJK(LCUR) ? 0 : 1; }

  /* chữ hiện / chữ đọc */
  var MK = /\{([^{}|]*)\|([^{}|]*)\}/g;
  function disp(s) { return String(s == null ? "" : s).replace(MK, "$1"); }
  function spk(s) { return String(s == null ? "" : s).replace(MK, "$2"); }
  var EMOX = /[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}\u{2300}-\u{23FF}\u{FE0F}\u{200D}\u{20E3}]/gu;
  // tách câu (giữ nguyên các cặp {…|…})
  function splitX(text, l) {
    var M = [], s = String(text || "").replace(MK, function (m) { M.push(m); return "\u0001" + (M.length - 1) + "\u0002"; }).replace(/\s+/g, " ").trim();
    if (!s) return [];
    var out = isCJK(l) ? (s.match(/[^。！？!?]+(?:[。！？!?]+[」』）)”"’]*|$)/g) || [s])
      : s.split(/(?<![A-Z][a-z]?\.)(?<=[.!?…]+["»”’)]*)\s+(?=["«“(]?[\p{Lu}\p{Lo}\d\u0001])/u);
    return out.map(function (x) { return x.trim().replace(/\u0001(\d+)\u0002/g, function (m, i) { return M[+i]; }); }).filter(Boolean);
  }
  // chuẩn hoá chữ cho giọng đọc từng tiếng
  function speakX(s, l) {
    s = spk(s).replace(EMOX, " ").replace(/[«»“”„"『』「」《》〈〉【】]/g, "");
    if (l === "en") s = s.normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/đ/g, "d").replace(/Đ/g, "D").replace(/\s*&\s*/g, " and ").replace(/(\d)\s*%/g, "$1 percent");
    if (l === "ja") s = s.replace(/・/g, "");
    s = s.replace(/\s*[—–]\s*/g, isCJK(l) ? "、" : ", ").replace(/\s*[·•]\s*/g, isCJK(l) ? "、" : ", ").replace(/\s*\(\s*/g, isCJK(l) ? "、" : ", ").replace(/\s*\)\s*/g, isCJK(l) ? "、" : ", ");
    s = s.replace(/\s*（\s*/g, "、").replace(/\s*）\s*/g, "、").replace(/、+/g, "、").replace(/、([。！？])/g, "$1");
    return s.replace(/\s+([,.!?;:])/g, "$1").replace(/,\s*([.!?])/g, "$1").replace(/^[\s,、]+|[\s,、]+$/g, "").replace(/\s{2,}/g, " ").trim();
  }
  // số → chữ tiếng Việt (chỉ dùng khi đọc bằng giọng Supertonic: giọng này không tự đọc số)
  var VD = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"];
  function vi3(n, full) {
    var tr = Math.floor(n / 100), ch = Math.floor(n / 10) % 10, dv = n % 10, out = [];
    if (tr || full) out.push(VD[tr] + " trăm");
    if (ch === 0) { if (dv && (tr || full)) out.push("linh"); } else if (ch === 1) out.push("mười"); else out.push(VD[ch] + " mươi");
    if (dv) out.push(dv === 1 && ch > 1 ? "mốt" : dv === 5 && ch > 0 ? "lăm" : dv === 4 && ch > 1 ? "tư" : VD[dv]);
    return out.join(" ");
  }
  function viInt(n) {
    if (!n) return "không"; var U = ["", " nghìn", " triệu", " tỷ"], parts = [], i = 0;
    while (n > 0 && i < 4) { parts.unshift({ v: n % 1000, u: U[i] }); n = Math.floor(n / 1000); i++; }
    return parts.map(function (p, k) { return !p.v && k > 0 ? "" : vi3(p.v, k > 0) + p.u; }).filter(Boolean).join(" ");
  }
  function viNumbers(s) { return String(s || "").replace(/\d+/g, function (m) { return m.length > 12 ? m.split("").map(function (d) { return VD[+d]; }).join(" ") : viInt(+m); }); }

  /* bản dịch */
  function trKey(l, id) { return "av_tr_" + l + "_" + id; }
  function trOf(w, l) {
    if (!l || l === "vi" || !w) return null;
    var my = lsGet(trKey(l, w.id), null); if (my && typeof my === "object") { my._mine = true; return my; }
    var b = global.ART_I18N && global.ART_I18N[l] && global.ART_I18N[l].works && global.ART_I18N[l].works[w.id];
    return b || null;
  }
  function ensureLang(l) {
    if (!l || l === "vi" || (global.ART_I18N && global.ART_I18N[l])) return Promise.resolve(true);
    return L.loadScript("data/i18n/" + l + ".js?v=" + I18N_V).then(function () { return !!(global.ART_I18N && global.ART_I18N[l]); }).catch(function () { return false; });
  }
  function baseWork(id) { return (DB().works || []).filter(function (x) { return x.id === id; })[0] || null; }
  // tác phẩm theo ngôn ngữ video: thay chữ bằng bản dịch, giữ nguyên ảnh, khung chi tiết, nguồn
  function localize(w, l) {
    if (!w || !l || l === "vi") return w;
    var t = trOf(w, l), o = clone(w); o.lang = l; o.titleVi = w.title; o.trMissing = 0; o.trMine = !!(t && t._mine);
    if (!t) { o.trMissing = -1; return o; }
    ["title", "artist", "date", "medium", "where", "hook", "intro", "end", "trendLine"].forEach(function (k) { if (t[k]) o[k] = t[k]; });
    if (!t.trendLine) delete o.trendLine;
    if (t.place && o.place) o.place = Object.assign({}, o.place, { name: t.place.name || o.place.name, prov: t.place.prov || o.place.prov });
    if (Array.isArray(t.tags)) o.tags = t.tags.slice();
    o.openers = Array.isArray(t.openers) ? t.openers.slice() : [];
    if (Array.isArray(t.img)) o.img = o.img.map(function (m, i) { var x = t.img[i]; return x ? Object.assign({}, m, { by: x.by || m.by, lic: x.lic || m.lic }) : m; });
    var base = w.custom ? null : baseWork(w.id), ts = Array.isArray(t.steps) ? t.steps : []; o.trStale = 0;
    o.steps = o.steps.map(function (st, i) {
      var j = i;
      if (t._mine) { if (t.n != null && t.n !== w.steps.length) j = -1; }          // bản dịch của anh: theo đúng thứ tự kịch bản lúc dịch
      else if (w.edited && base) {                                                  // bản có sẵn: dò theo câu hỏi / nhãn của kịch bản gốc
        j = -1; (base.steps || []).some(function (b, k) { if ((b.q && b.q === st.q) || (b.tag && b.tag === st.tag)) { j = k; return true; } return false; });
        if (j >= 0 && (base.steps[j].q !== st.q || base.steps[j].a !== st.a)) o.trStale++;
      }
      var x = j >= 0 ? ts[j] : null;
      if (!x || !(x.q || x.a)) { o.trMissing++; var keep = clone(st); keep.untr = 1; return keep; }
      var s2 = Object.assign({}, st, { tag: x.tag || st.tag, q: x.q || st.q, a: x.a || st.a });
      if (st.s || x.s) s2.s = x.s || null;
      if (st.card) s2.card = x.card ? { big: x.card.big || st.card.big, sub: x.card.sub || "" } : st.card;
      return s2;
    });
    return o;
  }
  function trStatus(w, l) {
    if (!l || l === "vi") return { ok: true };
    var lw = localize(w, l); return { ok: lw.trMissing === 0, none: lw.trMissing < 0, miss: Math.max(0, lw.trMissing), mine: lw.trMine, stale: lw.trStale || 0 };
  }
  // lệnh nhờ AI dịch (khi tác phẩm là của anh hoặc anh đã sửa kịch bản tiếng Việt)
  var TR_NOTE = {
    en: "tiếng Anh (Mỹ), giọng kể tự nhiên, câu ngắn; giữ tên riêng tiếng Việt có dấu (Tô Ngọc Vân, Đông Hồ).",
    ja: "tiếng Nhật, thể です・ます, dấu câu toàn khổ; tên người Việt viết katakana có «・» (トー・ゴック・ヴァン), tên tác phẩm trong 『』.",
    zh: "tiếng Trung giản thể; tên người Việt viết bằng chữ Hán tương ứng (苏玉云, 阮潘正), tên tác phẩm trong 《》, không để chữ La-tinh trong lời đọc.",
    ru: "tiếng Nga; tên tiếng Việt phiên âm Kirin theo lối quen dùng (То Нгок Ван, Донгхо), tên tác phẩm trong «».",
    ko: "tiếng Hàn thể 해요체; tên tiếng Việt phiên âm Hangul theo quy tắc Viện Quốc ngữ Hàn (또 응옥 번, 동호), tên tác phẩm trong 《》."
  };
  var TR_NUM = { en: "{1930|nineteen thirty}, {17th century|seventeenth century}", ja: "{1930年|せんきゅうひゃくさんじゅうねん}, {17世紀|じゅうななせいき}",
                 zh: "{1930年|一九三〇年}, {17世纪|十七世纪}", ru: "{в 1930 году|в тысяча девятьсот тридцатом году}, {XVII века|семнадцатого века}", ko: "{1930년|천구백삼십 년}, {17세기|십칠 세기}" };
  function trSource(w) {
    return { title: w.title, artist: w.artist || "", date: w.date || "", medium: w.medium || "", where: w.where || "", place: { name: w.place && w.place.name || "", prov: w.place && w.place.prov || "" },
      tags: w.tags || [], hook: w.hook || "", intro: w.intro || "", openers: w.openers || [], trendLine: w.trendLine || "", end: w.end || "",
      img: (w.img || []).map(function (m) { return { by: m.by || "", lic: m.lic || "" }; }),
      steps: (w.steps || []).map(function (s) { var x = { tag: s.tag || "", q: s.q || "", a: s.a || "" }; if (s.s) x.s = s.s; if (s.card) x.card = { big: s.card.big || "", sub: s.card.sub || "" }; return x; }) };
  }
  function trPrompt(w, l) {
    var src = trSource(w);
    return ["Bạn là dịch giả kịch bản video ngắn giới thiệu nghệ thuật Việt Nam cho khán giả quốc tế (TikTok/Reels/Shorts). Kịch bản được giọng AI đọc thành tiếng và hiện thành phụ đề.",
      "Hãy dịch JSON dưới đây sang " + (TR_NOTE[l] || l) + " Trả về DUY NHẤT một khối JSON cùng cấu trúc, cùng số phần tử và cùng thứ tự các mảng (steps, img, openers).",
      "", "YÊU CẦU",
      "1. Dịch trung thành, giọng kể sinh động, không thêm sự kiện, con số hay tên riêng không có trong bản gốc; giữ các cách nói rào đón («theo một số tài liệu», «theo các nghệ nhân»).",
      "2. Mỗi «q» là câu hỏi, kết thúc bằng dấu hỏi. «tag» giữ nguyên emoji đầu, ngắn (≤ 24 ký tự La-tinh, ≤ 12 ký tự Nhật/Trung/Hàn). «trendLine» là một câu kiểu «Giờ thì tôi mới hiểu vì sao người ta có thể ngắm … hàng giờ…».",
      "3. Chữ hiện khác cách đọc (số, năm, thế kỷ, số La Mã, chữ viết tắt) thì viết {chữ hiện|cách đọc}, ví dụ: " + (TR_NUM[l] || "") + ". Không dùng { } | vào việc khác; các trường title, artist, date, medium, where, place, tags, img, tag, card chỉ để hiện, không dùng cách viết này.",
      "4. Không trích hay dịch lời bài hát; tên bài hát thì được.",
      "5. «tags»: 3–5 từ khoá để làm hashtag (không có dấu #).",
      "", "JSON CẦN DỊCH:", JSON.stringify(src, null, 1)].join("\n");
  }
  function applyTr(w, l, o) {
    if (!o || typeof o !== "object") throw new Error("Không có JSON");
    if (o.works && o.works[w.id]) o = o.works[w.id];
    var n = (w.steps || []).length, ns = Array.isArray(o.steps) ? o.steps.length : 0;
    if (!ns) throw new Error("Bản dịch không có mục «steps».");
    if (ns !== n) throw new Error("Bản dịch có " + ns + " chi tiết, kịch bản tiếng Việt có " + n + " — hãy dịch lại cho đủ, đúng thứ tự.");
    var keep = { n: n, at: Date.now() };
    ["title", "artist", "date", "medium", "where", "hook", "intro", "end", "trendLine"].forEach(function (k) { if (o[k] != null) keep[k] = String(o[k]).slice(0, 900); });
    if (o.place) keep.place = { name: String(o.place.name || "").slice(0, 120), prov: String(o.place.prov || "").slice(0, 80) };
    if (Array.isArray(o.tags)) keep.tags = o.tags.map(function (x) { return String(x).replace(/^#/, "").slice(0, 40); }).filter(Boolean).slice(0, 6);
    if (Array.isArray(o.openers)) keep.openers = o.openers.map(function (x) { return String(x).slice(0, 220); }).filter(Boolean).slice(0, 6);
    if (Array.isArray(o.img)) keep.img = o.img.map(function (x) { return { by: String(x && x.by || "").slice(0, 160), lic: String(x && x.lic || "").slice(0, 60) }; });
    keep.steps = o.steps.map(function (x) { var s = { tag: String(x.tag || "").slice(0, 60), q: String(x.q || "").slice(0, 300), a: String(x.a || "").slice(0, 1200) }; if (x.s) s.s = String(x.s).slice(0, 400); if (x.card) s.card = { big: String(x.card.big || "").slice(0, 30), sub: String(x.card.sub || "").slice(0, 120) }; return s; });
    lsSet(trKey(l, w.id), keep);
    return { n: n };
  }

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
  var EDIT_FIELDS = ["title", "artist", "date", "medium", "where", "hook", "intro", "end", "trendLine", "steps", "img", "type", "y", "era", "place", "size", "status", "alt", "tags", "openers", "sources", "facts"];
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
  // trang Facebook «Giải mã Nghệ Thuật» (v1.3): chữ ký, mã QR, logo cuối video
  var BRAND_NAME = "Giải mã Nghệ Thuật", BRAND_URL = "https://www.facebook.com/profile.php?id=61596148916409", OLD_CREDIT = "Phạm Đăng Hiển · fb.com/lopmaybay", OLD_QR = "https://fb.com/lopmaybay";
  var DEF = { aspect: "9:16", res: 720, len: "full", pace: "mid", voice: "ai", rate: 1, music: "auto", musicVol: 0.5, trend: true, caps: true,
              qcard: true, nums: true, spot: true, credit: BRAND_NAME, qr: true, qrUrl: BRAND_URL, srcs: true, lang: "vi", vlang: "vi", brand: true,
              voices: { vi: "vi", en: "en", ja: "st:F1", zh: "zh", ru: "ru", ko: "st:F2" },
              srcStep: true, imgCredit: true, ai: true, aiPos: "both", aiBadge: true, aiSay: false, aiText: "", safe: true, capSize: "m", cta: true,
              coverIntro: true, autoDl: true, ytAuto: false, ytPrivacy: "private", ytTitle: "" };
  // lời nhắc minh bạch về AI (anh sửa được trong studio)
  var AI_TEXT = "Video được dựng với sự hỗ trợ của AI (giọng đọc AI, dựng hình tự động). Người dựng không phải chuyên gia nên nội dung có thể còn sai sót — rất mong bạn góp ý và đối chiếu nguồn.";
  var AI_SAY = "Video có sử dụng trí tuệ nhân tạo và có thể còn sai sót, rất mong bạn góp ý.";
  function aiText(O) { return (O && O.aiText && String(O.aiText).trim()) || AI_TEXT; }
  function aiAt(O, where) { return !!(O && O.ai && (O.aiPos === where || O.aiPos === "both")); }
  // nguồn: tên ngắn hiện trên video
  function srcLabel(s) { return s ? (s.s || String(s.t || "").split(" — ")[0] || domainOf(s.u)) : ""; }
  function domainOf(u) { var m = String(u || "").match(/^https?:\/\/(?:www\.)?([^\/?#]+)/i); return m ? m[1] : ""; }
  function stepSources(w, st) { return (st && st.src || []).map(function (i) { return (w.sources || [])[i]; }).filter(Boolean); }
  function imgCreditOf(d, m) { var T = TXL(LCUR); if (m && m.src === "user") return T.ownPhoto; if (!d) return ""; var by = d.by || T.commons; return by + (d.lic && by.indexOf(d.lic) < 0 && !/Phạm vi|CC0/.test(d.by || "") ? " · " + d.lic : ""); }
  function loadOpts() {
    var o = {}, s = lsGet("av_opts", {}) || {};
    if ((s.v || 0) < 13) { if (s.credit === OLD_CREDIT) delete s.credit; if (s.qrUrl === OLD_QR) delete s.qrUrl; }   // đổi sang trang mới nếu anh chưa tự sửa
    for (var k in DEF) o[k] = (s[k] !== undefined) ? s[k] : DEF[k];
    o.voices = Object.assign({}, DEF.voices, s.voices && typeof s.voices === "object" ? s.voices : {});
    if (LANGS.indexOf(o.vlang) < 0) o.vlang = "vi";
    o.lang = "vi"; o.v = 13; return o;
  }
  function saveOpts(O) { var c = {}; for (var k in O) if (k !== "trendText") c[k] = O[k]; lsSet("av_opts", c); }
  function musicFor(w, O) { if (O.music && O.music !== "auto") return O.music; return w.type === "painting" || w.type === "music" ? "zen" : "ngu"; }
  function trendLine(w, O) {
    if (O.trendText && String(O.trendText).trim()) return String(O.trendText).trim();
    if (w.trendLine) return w.trendLine;
    var noun = w.trend || typeOf(w.type).noun || "một tác phẩm";
    if (/^(nghe|đứng|ngồi|lắng)/.test(noun)) return "Giờ thì tôi mới hiểu vì sao người ta có thể dành hàng giờ " + noun + "…";
    return "Giờ thì tôi mới hiểu vì sao người ta có thể dành hàng giờ ngắm nhìn " + noun + "…";
  }
  // gợi ý câu mở đầu: riêng từng tác phẩm (dữ liệu openers) + mẫu chung theo nhóm móc câu (tò mò, câu hỏi, thử thách…)
  function posPhrase(b) {
    var cx = b[0] + b[2] / 2, cy = b[1] + b[3] / 2, h = cx < 0.36 ? "trái" : cx > 0.64 ? "phải" : "", v = cy < 0.36 ? "trên" : cy > 0.64 ? "dưới" : "";
    return h && v ? "góc " + v + " bên " + h : v ? "phần " + (v === "trên" ? "phía trên" : "phía dưới") : h ? "phía bên " + h : "chính giữa";
  }
  function openerList(w, O) {
    var lx = O && O.vlang || "vi"; if (lx !== "vi") return openerListX(w, O, lx);
    var t = typeOf(w.type), music = w.type === "music", noun = (w.trend && !/^(nghe|đứng|ngồi|lắng)/.test(w.trend) ? w.trend : t.noun) || "một tác phẩm";
    var noun2 = noun.replace(/^một\s+/, ""), n = pickSteps(w, O || {}).length, T = w.title;
    var first = (w.steps || []).filter(function (s) { return !s.card && s.b && s.b[2] * s.b[3] < 0.4; })[0], out = [];
    (w.openers || []).forEach(function (x) { if (x && String(x).trim()) out.push({ t: String(x).trim(), g: "Riêng cho tác phẩm này" }); });
    (music ? [
      "Bạn đã nghe " + T + " rất nhiều lần, nhưng đã bao giờ thật sự lắng nghe?",
      n >= 2 ? n + " câu chuyện phía sau " + T + " mà không phải ai cũng biết." : "",
      "Ai cũng từng nghe " + T + ", nhưng ít ai biết bài hát đã ra đời thế nào.",
      "Khoan lướt! Hãy nghe câu chuyện phía sau " + noun2 + " này."
    ] : [
      "Có một chi tiết trong " + T + " mà rất nhiều người nhìn qua mà không thấy.",
      n >= 2 ? n + " chi tiết nhỏ trong " + T + " kể cả một câu chuyện lớn." : "",
      "Bạn đã thấy " + T + " nhiều lần, nhưng đã bao giờ thật sự nhìn kỹ?",
      first ? "Khoan lướt! Hãy nhìn vào " + posPhrase(first.b) + " của " + noun2 + " này." : "Khoan lướt! Hãy nhìn thật kỹ " + noun2 + " này.",
      "Thử dừng video và đếm xem: bạn tìm được mấy chi tiết lạ trong " + noun2 + " này?",
      "Ai cũng từng thấy " + T + ", nhưng ít ai biết câu chuyện phía sau.",
      "Bạn nghĩ đây chỉ là " + noun + "? Hãy nhìn kỹ lại một lần nữa."
    ]).forEach(function (x) { if (x) out.push({ t: x, g: "Mẫu chung" }); });
    return out;
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
              [/\bFukuoka\b/g, "Phu-cu-ô-ca"], [/\bfranc\b/g, "phrăng"], [/\bminuet\b/g, "mi-nu-ét"], [/\bUNESCO\b/g, "U-nét-xcô"], [/\bCông nguyên\b/g, "Công nguyên"],
              [/\bAI\b/g, "trí tuệ nhân tạo"], [/\bTikTok\b/g, "Tích Tóc"], [/\bReels\b/g, "Rin"]];
  function speakable(c) { var t = String(c || ""); PRON.forEach(function (p) { t = t.replace(p[0], p[1]); }); return t; }
  function narrate(w, O, steps) {
    if ((O.vlang || "vi") !== "vi") return narrateX(w, O, steps, O.vlang);
    var NR = {}, ctx = { lang: "vi", ru: false };
    // chỉ dùng giọng Việt cho video giải mã (không tải thêm giọng Nga/Anh): đoạn bị nhận nhầm là tiếng nước ngoài thì đọc bằng chữ gốc
    function sent(c) { var segs = SAY.segs(speakable(c), ctx).map(function (g) { return g.l === "vi" ? g : { l: "vi", t: (g.o != null && g.o !== "") ? g.o : g.t }; }); return { c: c, segs: L.mergeSegs(segs) }; }
    function many(text) { return sentencesOf(text).map(sent); }
    if (O.trend) NR.trend = [sent(trendLine(w, O).replace(/…$/, ".").replace(/\s*\|\s*/g, " "))];
    NR.hook = many(w.hook || "");
    var info = w.intro || (w.title + (w.artist ? ", " + w.artist : "") + (w.date ? ", " + w.date : "") + ".");
    if (O.len !== "short") NR.info = many(info);          // bản ngắn: thẻ tên tác phẩm hiện im lặng, không đọc
    steps.forEach(function (st, i) {
      NR["q:" + i] = many(st.q || "");
      NR["a:" + i] = many(O.len === "short" ? shortAnswer(st) : (st.a || ""));
    });
    NR.end = many(w.end || ("Giờ thì bạn đã hiểu vì sao người ta có thể ngắm " + w.title + " hàng giờ."));
    var out = [];
    if (O.ai && O.aiSay) out = out.concat(many(O.aiText && String(O.aiText).trim() ? String(O.aiText).trim() : AI_SAY));
    if (O.qr && O.qrUrl) out.push(sent("Theo dõi để xem những tác phẩm tiếp theo nhé."));
    NR.outro = out;
    Object.keys(NR).forEach(function (k) { if (!NR[k].length) delete NR[k]; });
    // giọng Supertonic không tự đọc chữ số → đổi số sang chữ (giọng Piper/espeak vẫn đọc số như cũ)
    var vv = AIV.VOICES[AIV.voiceFor("vi", O)]; if (vv && vv.eng === "st") Object.keys(NR).forEach(function (k) { NR[k].forEach(function (s) { s.segs.forEach(function (g) { if (g.l === "vi") g.t = viNumbers(g.t); }); }); });
    return NR;
  }

  // lời đọc cho video tiếng nước ngoài: mỗi câu một đoạn, đọc bằng giọng của ngôn ngữ đó; chi tiết chưa dịch thì đọc tiếng Việt
  function readSecL(chars, l) { return chars / (isCJK(l) ? 6.5 : l === "ko" ? 8 : 14.5) + 0.35; }
  function trendLineX(w, O, l) {
    if (O && O.trendText && String(O.trendText).trim()) return String(O.trendText).trim();
    if (w.trendLine && w.lang === l) return w.trendLine;
    var T = TXL(l), ty = T.types[w.type]; return T.trend ? T.trend(ty ? ty[1] : "", w.type === "music") : trendLine(w, O);
  }
  function trendLineV(V) { var l = V.lang || "vi"; return l === "vi" ? trendLine(V.w, V.O) : trendLineX(V.w, V.O, l); }
  function posKey(b) { var cx = b[0] + b[2] / 2, cy = b[1] + b[3] / 2, h = cx < 0.36 ? "l" : cx > 0.64 ? "r" : "", v = cy < 0.36 ? "t" : cy > 0.64 ? "b" : ""; return h && v ? v + h : v || h || "c"; }
  function openerListX(w, O, l) {
    var T = TXL(l), out = [], n = pickSteps(w, O || {}).length, music = w.type === "music", ty = T.types[w.type] || [], noun = ty[1] || "";
    var first = (w.steps || []).filter(function (s) { return !s.card && s.b && s.b[2] * s.b[3] < 0.4; })[0], pos = first && T.pos ? T.pos[posKey(first.b)] : "";
    (w.openers || []).forEach(function (x) { if (x && String(x).trim()) out.push({ t: String(x).trim(), g: "Riêng cho tác phẩm này" }); });
    if (T.openers) T.openers(quoteT(w.title, l), noun, n, music, pos, l === "ru" ? ty : null).forEach(function (x) { if (x) out.push({ t: x, g: "Mẫu chung" }); });
    return out;
  }
  function shortAnswerX(st, l) { if (st.s) return st.s; var ss = splitX(st.a, l), out = ss[0] || ""; if (disp(out).length < (isCJK(l) ? 30 : l === "ko" ? 40 : 70) && ss[1]) out += (isCJK(l) ? "" : " ") + ss[1]; return out; }
  function viSent(c) { var segs = SAY.segs(speakable(c), { lang: "vi", ru: false }).map(function (g) { return g.l === "vi" ? g : { l: "vi", t: (g.o != null && g.o !== "") ? g.o : g.t }; }); return { c: c, segs: L.mergeSegs(segs) }; }
  function narrateX(w, O, steps, l) {
    var NR = {}, T = TXL(l);
    function sent(raw) { var c = disp(raw).replace(/\s+/g, " ").trim(), t = speakX(raw, l); return { c: c, segs: t ? [{ l: l, t: t }] : [] }; }
    function many(text, vi) { return vi ? sentencesOf(text).map(viSent) : splitX(text, l).map(sent).filter(function (s) { return s.c; }); }
    if (O.trend) NR.trend = [sent(trendLineX(w, O, l).replace(/\s*(?:…+|\.{3,})$/, isCJK(l) ? "。" : "."))];
    NR.hook = many(w.hook || "");
    var info = w.intro || [w.title, w.artist, w.date].filter(Boolean).join(isCJK(l) ? "、" : ", ") + (isCJK(l) ? "。" : ".");
    if (O.len !== "short") NR.info = many(info);
    steps.forEach(function (st, i) {
      NR["q:" + i] = many(st.q || "", st.untr);
      NR["a:" + i] = many(O.len === "short" ? (st.untr ? shortAnswer(st) : shortAnswerX(st, l)) : (st.a || ""), st.untr);
    });
    NR.end = many(w.end || (T.end ? T.end(quoteT(w.title, l)) : ""));
    var out = [];
    if (O.ai && O.aiSay) out = out.concat(many(T.aiSay || AI_SAY));
    if (O.qr && O.qrUrl) out.push(sent(T.follow));
    NR.outro = out;
    Object.keys(NR).forEach(function (k) { if (!NR[k].length) delete NR[k]; });
    return NR;
  }

  var BRAND = { img: null, p: null };
  function ensureBrand() {
    return BRAND.p || (BRAND.p = (global.ART_BRAND ? Promise.resolve() : L.loadScript("brand/brand.js?v=1").catch(function () { })).then(function () {
      var src = global.ART_BRAND && global.ART_BRAND.logo; if (!src) return null;
      return new Promise(function (res) { var im = new Image(); im.onload = function () { BRAND.img = im; res(im); }; im.onerror = function () { res(null); }; im.src = src; });
    }));
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
    var cu = await userImageURL(w.id, "cover"); if (cu) res.coverEl = await loadOne(cu);
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
    var Ly = LY(W, H, O), u = Ly.u, gap = 24 * u, top = 0.05 * H;
    if (O.qcard) top = Math.max(qCardBottom(Ly, disp(st.q), false), qCardBottom(Ly, disp(st.q), true) + (st.tag ? 49 * u : 0)) + gap;
    else if (st.tag) top = Ly.qY + 49 * u + gap;
    var bot = O.caps ? Ly.capY - capHalf(Ly) - 12 * u : (Ly.safe ? Ly.botY : H - 34 * u);
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
    var lang = O.vlang || "vi"; LCUR = lang;
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
        var t = lead; sc.sentT = sc.narr.map(function (s) { var d = readSecL((s.c || "").length, lang) * pace, r = { t0: t, t1: t + d }; t = r.t1 + 0.3; return r; });
        sc.dur = Math.max(minDur || 0, sc.fly || 0, t - 0.3 + tail);
      }
      return sc;
    }
    var vFull = fullView(I, k0, FA), last = vFull;
    if (O.coverIntro !== false) push({ key: "cover", type: "cover", dur: 0.8, A: vFull, B: vFull, narr: [], sentT: [] });   // khung đầu = ảnh bìa
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
    var outMin = (O.qr && O.qrUrl ? (sh ? 5.2 : 6.2) : 4.2) + (O.srcs && (w.sources || []).length ? (sh ? 0.8 : 1.4) : 0) + (aiAt(O, "end") ? (sh ? 0.8 : 1.2) : 0);
    push(voiced({ key: "outro", type: "outro", A: drift(endV, 0.03), B: drift(endV, 0.05) }, 0.6, 0.6, outMin));
    var V = { scenes: scenes, total: tt, W: W, H: H, FA: FA, O: O, w: w, I: I, NR: NR, AP: AP || null, steps: steps, k0: k0, C: O.coverC || coverDefaults(w, O), lang: lang };
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
  // bố cục khung hình. Vùng an toàn TikTok/Reels/Shorts (khung dọc): chừa ~1/3 dưới (tên kênh, mô tả, nút bấm) và mép phải
  // (cột nút) — tham khảo số đo vùng an toàn của các nền tảng (OpenClip, visu.network) và vị trí phụ đề kiểu MoneyPrinterTurbo.
  function LY(W, H, O) {
    O = O || {};
    var port = H > W * 1.2, sq = !port && H > W * 0.9, u = Math.min(W, H) / 720, safe = port && !!O.safe;
    var cs = O.capSize === "s" ? 0.88 : O.capSize === "l" ? 1.16 : 1;
    return { port: port, sq: sq, u: u, safe: safe, cs: cs, pad: Math.round((port ? 0.06 : 0.045) * W),
             capY: port ? H * (safe ? 0.64 : 0.80) : H * 0.84, capW: W * (port ? (safe ? 0.78 : 0.88) : 0.74),
             qY: port ? H * (safe ? 0.105 : 0.085) : sq ? H * 0.05 : H * 0.07, qW: port ? W * 0.88 : sq ? W * 0.92 : W * 0.56, qX: port ? W * 0.06 : W * 0.04,
             midY: port && safe ? H * 0.40 : H * 0.5, infoY: port ? H * (safe ? 0.50 : 0.64) : H * 0.6, endY: port ? H * (safe ? 0.62 : 0.78) : H * 0.82,
             trendY: port && safe ? H * 0.30 : H * 0.4, botY: port && safe ? H * 0.70 : H * 0.93,
             badgeY: port && safe ? H * 0.072 : H * 0.022 };
  }
  // chiều cao hộp phụ đề tối đa (3 dòng) để chừa chỗ
  function capHalf(Ly) { var px = 27 * Ly.u * Ly.cs; return (3 * px * 1.32 + 0.7 * px) / 2; }
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
    var startL = 0; if (lines.length > maxL) { var acc = 0, cur = 0; for (var i = 0; i < lines.length; i++) { acc += lines[i].length + JOIN(); if (acc >= said) { cur = i; break; } cur = i; } startL = clamp(cur - (maxL - 2), 0, lines.length - maxL); }
    var shown = lines.slice(startL, startL + maxL), bw = 0; shown.forEach(function (l) { bw = Math.max(bw, ctx.measureText(l).width); });
    var bh = shown.length * lh + px * 0.7, bx = V.W / 2 - bw / 2 - px * 0.55, by = y - bh / 2;
    if (opts.box !== false) panel(ctx, bx, by, bw + px * 1.1, bh, px * 0.45, "rgba(8,14,26," + (opts.boxA || 0.66) + ")");
    var before = 0, jn = JOIN(); for (var j = 0; j < startL; j++) before += lines[j].length + jn;
    ctx.textAlign = "left"; ctx.textBaseline = "middle";
    shown.forEach(function (l, i) {
      var lx = V.W / 2 - ctx.measureText(l).width / 2, ly = by + px * 0.35 + lh * (i + 0.5);
      ctx.fillStyle = "#ffffff"; ctx.shadowColor = "rgba(0,0,0,0.6)"; ctx.shadowBlur = 4; ctx.fillText(l, lx, ly); ctx.shadowBlur = 0;
      var k = clamp(said - before, 0, l.length);
      if (k > 0 && opts.karaoke !== false) { var sw = ctx.measureText(l.slice(0, k)).width; ctx.save(); ctx.beginPath(); ctx.rect(lx - 2, ly - lh / 2, sw + 2, lh); ctx.clip(); ctx.fillStyle = GOLD; ctx.fillText(l, lx, ly); ctx.restore(); }
      before += l.length + jn;
    });
    ctx.restore();
    return { y0: by, y1: by + bh };
  }
  function sentProgress(sc, tau, i) { var st = sc.sentT && sc.sentT[i]; if (!st) return 1; return clamp((tau - st.t0) / Math.max(0.3, st.t1 - st.t0), 0, 1); }
  function currentCaption(sc, tau) { var i = sentIdx(sc, tau); if (i < 0 || !sc.narr[i]) return null; var st = sc.sentT[i]; if (tau > st.t1 + 0.6 && i === sc.narr.length - 1) return null; return { text: sc.narr[i].c, p: sentProgress(sc, tau, i) }; }

  function renderArt(ctx, V, t) {
    LCUR = V.lang || "vi";
    var W = V.W, H = V.H, O = V.O, Ly = LY(W, H, O), u = Ly.u, i = sceneAt(V, t), sc = V.scenes[i], tau = t - sc.t0;
    if (sc.type === "cover") { renderCover(ctx, V, V.C); return; }
    ctx.save(); ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, W, H);
    var cam = camOf(sc, tau), v = cam.v;
    // ảnh: chuyển ảnh thì hoà dần
    if (cam.fade >= 0 && cam.A && cam.B && cam.A.k !== cam.B.k) { drawImageView(ctx, V, cam.A, 1); drawImageView(ctx, V, { k: cam.B.k, cx: cam.B.cx, cy: cam.B.cy, w: cam.B.w * (1 + 0.06 * (1 - cam.fade)) }, cam.fade); }
    else if (!drawImageView(ctx, V, v, 1)) drawMissing(ctx, V);
    vignette(ctx, W, H, 0.38);
    var T = sc.type;
    if (T === "trend") drawTrend(ctx, V, sc, tau, Ly);
    else if (T === "hook") { var c = currentCaption(sc, tau); if (c) caption(ctx, V, c.text, c.p, Ly.midY, Ly.capW, 34 * u * Ly.cs, { weight: 800, maxLines: 5, boxA: 0.5 }); }
    else if (T === "info") drawInfo(ctx, V, sc, tau, Ly);
    else if (T === "q" || T === "a") drawStep(ctx, V, sc, tau, Ly, cam);
    else if (T === "end") drawEnd(ctx, V, sc, tau, Ly, cam);
    else if (T === "outro") drawOutro(ctx, V, sc, tau, Ly);
    // minh bạch: tên tác giả ảnh (dọc mép trái), nhãn «Có dùng AI», lời nhắc ở cảnh đầu
    if (T !== "outro") overlays(ctx, V, sc, tau, Ly, cam, i);
    // chữ ký góc + thanh tiến độ
    if (O.credit && T !== "outro") { ctx.save(); ctx.font = F(700, 15 * u); ctx.fillStyle = "rgba(255,255,255,0.72)"; ctx.textAlign = "right"; ctx.textBaseline = "bottom"; ctx.shadowColor = "rgba(0,0,0,0.7)"; ctx.shadowBlur = 4; ctx.fillText("✦ " + O.credit, W - Ly.pad * 0.6, H - 10 * u); ctx.restore(); }
    ctx.fillStyle = "rgba(255,255,255,0.14)"; ctx.fillRect(0, H - 4 * u, W, 4 * u); ctx.fillStyle = GOLD; ctx.fillRect(0, H - 4 * u, W * clamp(t / V.total, 0, 1), 4 * u);
    ctx.restore();
  }
  function overlays(ctx, V, sc, tau, Ly, cam, idx) {
    var W = V.W, H = V.H, u = Ly.u, O = V.O, cardOn = (sc.type === "q" || sc.type === "a") && sc.card;
    if (O.imgCredit && cam && cam.v && !cam.v.none && !cardOn) {
      var m = V.I[cam.v.k], d = V.w.img[cam.v.k], txt = imgCreditOf(d, m);
      if (m && m.ok && txt) {
        ctx.save(); ctx.translate(Math.max(10 * u, W * 0.022), Ly.safe ? H * 0.42 : H * 0.5); ctx.rotate(-Math.PI / 2);
        ctx.font = F(600, 12.5 * u); var line = wrap(ctx, "📷 " + txt, H * (Ly.safe ? 0.5 : 0.62), 1)[0] || "";
        ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillStyle = "rgba(255,255,255,0.62)"; ctx.shadowColor = "rgba(0,0,0,0.8)"; ctx.shadowBlur = 4;
        ctx.fillText(line, 0, 0); ctx.restore();
      }
    }
    if (O.ai && O.aiBadge) {
      ctx.save(); ctx.font = F(800, 12.5 * u); var bt = TXL(V.lang).aiBadge, bw = ctx.measureText(bt).width + 16 * u, bh = 22 * u, bx = Ly.pad * 0.6, by = Ly.badgeY;
      panel(ctx, bx, by, bw, bh, bh / 2, "rgba(10,18,32,0.55)"); ctx.fillStyle = "rgba(255,255,255,0.85)"; ctx.textBaseline = "middle"; ctx.textAlign = "left"; ctx.fillText(bt, bx + 8 * u, by + bh / 2 + 0.5 * u); ctx.restore();
    }
    if (idx === (V.scenes[0] && V.scenes[0].type === "cover" ? 1 : 0) && aiAt(O, "start")) {
      var a = seg(tau, 0.4, 1.0) * (1 - seg(tau, sc.dur - 0.5, sc.dur));
      if (a > 0.01) { ctx.save(); ctx.globalAlpha = a; notice(ctx, V, TXL(V.lang).aiStart, Ly.port ? Ly.botY - 30 * u : H * 0.9, W * (Ly.port ? 0.86 : 0.6), 15.5 * u, 0.6); ctx.restore(); }
    }
  }
  // hộp chữ nhỏ canh giữa (lời nhắc, câu hỏi gợi bình luận)
  function notice(ctx, V, text, cy, maxW, px, boxA, color) {
    ctx.save(); ctx.font = F(700, px); var lines = wrap(ctx, text, maxW - px * 1.6, 3), lh = px * 1.3, bw = 0;
    lines.forEach(function (l) { bw = Math.max(bw, ctx.measureText(l).width); });
    var h = lines.length * lh + px * 0.9, x = V.W / 2 - bw / 2 - px * 0.8, y = cy - h / 2;
    panel(ctx, x, y, bw + px * 1.6, h, px * 0.6, "rgba(8,14,26," + (boxA == null ? 0.7 : boxA) + ")");
    ctx.fillStyle = color || "rgba(255,255,255,0.92)"; ctx.textAlign = "center"; ctx.textBaseline = "middle";
    lines.forEach(function (l, i) { ctx.fillText(l, V.W / 2, y + px * 0.45 + lh * (i + 0.5)); });
    ctx.restore(); return { y0: y, y1: y + h };
  }
  function drawMissing(ctx, V) {
    var W = V.W, H = V.H, u = Math.min(W, H) / 720, g = ctx.createLinearGradient(0, 0, W, H); g.addColorStop(0, "#1b2f52"); g.addColorStop(1, "#0b1424");
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    ctx.save(); ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillStyle = "rgba(255,255,255,0.18)"; ctx.font = F(400, 160 * u); ctx.fillText(typeOf(V.w.type).icon, W / 2, H * 0.36);
    ctx.fillStyle = "rgba(255,255,255,0.75)"; ctx.font = F(800, 26 * u); ctx.fillText(V.w.img.some(function (d) { return d.user; }) && (V.lang || "vi") === "vi" ? TX.vi.noImgUser : TXL(V.lang).noImg, W / 2, H * 0.5);
    ctx.restore();
  }
  // hiện từng chữ (từ) một
  function wordsReveal(ctx, lines, x, y, lh, p, align) {
    var total = 0, sep = isCJK(LCUR) ? "" : " "; lines.forEach(function (l) { total += wordsOf(l).length; });
    var shown = p * total, gi = 0;
    ctx.textAlign = "left";
    lines.forEach(function (l, k) {
      var lw = ctx.measureText(l).width, sx = align === "center" ? x - lw / 2 : x, parts = wordsOf(l), acc = "";
      parts.forEach(function (wd, j) {
        if (j) acc += sep; var before = ctx.measureText(acc).width; acc += wd;
        var a = clamp(shown - gi, 0, 1); gi++; if (a <= 0) return;
        ctx.save(); ctx.globalAlpha *= a; ctx.fillText(wd, sx + before, y + k * lh + (1 - a) * lh * 0.25); ctx.restore();
      });
    });
  }
  function drawTrend(ctx, V, sc, tau, Ly) {
    var W = V.W, H = V.H, u = Ly.u, line = disp(trendLineV(V)), a = seg(tau, 0.1, 0.6) * (1 - seg(tau, sc.dur - 0.45, sc.dur)), TL = TXL(V.lang);
    ctx.save(); ctx.globalAlpha = a;
    var g = ctx.createLinearGradient(0, H * 0.2, 0, H * 0.8); g.addColorStop(0, "rgba(4,7,14,0)"); g.addColorStop(0.3, "rgba(4,7,14,0.72)"); g.addColorStop(0.7, "rgba(4,7,14,0.72)"); g.addColorStop(1, "rgba(4,7,14,0)");
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    line = line.replace(/\s*\|\s*/g, " ");
    var m = (V.lang || "vi") === "vi" ? (line.match(/^(Giờ thì tôi mới hiểu)\s*(.*)$/i) || line.match(/^(.{2,34}?[!?:])\s+(.{12,})$/)) : (TL.head ? line.match(TL.head) : null), head = m ? (m[1].length <= 24 ? m[1].toUpperCase() : m[1]) : "", rest = m ? m[2] : line;
    var maxW = W * (Ly.port || Ly.sq ? 0.86 : 0.7), y = Ly.trendY;
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
    ctx.font = F(600, 21 * u); var meta = [w.titleVi && w.titleVi !== w.title ? "🇻🇳 " + w.titleVi : "", w.artist, w.date].filter(Boolean).join(" · "), ml = wrap(ctx, meta, maxW - 30 * u, 3);
    var sub = [w.medium, w.where].filter(Boolean).join(" · "); ctx.font = F(500, 18 * u); var sl = wrap(ctx, sub, maxW - 30 * u, 3);
    var h = 40 * u + tl.length * 50 * u + ml.length * 27 * u + sl.length * 24 * u + 30 * u, y = Ly.infoY - h / 2 + (1 - a) * 40 * u;
    panel(ctx, x, y, maxW, h, 22 * u, "rgba(9,16,30,0.84)");
    ctx.fillStyle = GOLD; ctx.fillRect(x, y + 22 * u, 5 * u, h - 44 * u);
    chip(ctx, x + 18 * u, y - 18 * u, t.icon + " " + typeName(w.type, V.lang), 17 * u, GOLD, NAVY);
    var yy = y + 38 * u; ctx.textBaseline = "middle"; ctx.textAlign = "left";
    ctx.font = FS(800, (Ly.port ? 44 : 46) * u); ctx.fillStyle = "#fff"; tl.forEach(function (l) { ctx.fillText(l, x + 22 * u, yy + 12 * u); yy += 50 * u; });
    ctx.font = F(700, 21 * u); ctx.fillStyle = GOLD; ml.forEach(function (l) { ctx.fillText(l, x + 22 * u, yy + 4 * u); yy += 27 * u; });
    ctx.font = F(500, 18 * u); ctx.fillStyle = "rgba(255,255,255,0.82)"; sl.forEach(function (l) { ctx.fillText(l, x + 22 * u, yy + 4 * u); yy += 24 * u; });
    ctx.restore();
    var c = currentCaption(sc, tau); if (c && V.O.caps) caption(ctx, V, c.text, c.p, Ly.capY + (Ly.safe ? 0 : 30 * u), Ly.capW, 25 * u * Ly.cs, { maxLines: 2 });
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
    ctx.fillText(TXL(V.lang).detail + sc.num + "/" + sc.of, x + 22 * u, y + 24 * u);
    // chấm tiến độ
    for (var d = 0; d < sc.of && sc.of <= 14; d++) { ctx.beginPath(); ctx.arc(x + Ly.qW - 22 * u - (sc.of - 1 - d) * 13 * u, y + 24 * u, 4 * u, 0, Math.PI * 2); ctx.fillStyle = d < sc.num ? GOLD : "rgba(255,255,255,0.28)"; ctx.fill(); }
    ctx.font = F(800, px); ctx.fillStyle = "#fff";
    var total = text.length, shown = Math.floor(total * clamp(p, 0, 1)), acc = 0;
    lines.forEach(function (l, i) { var k = clamp(shown - acc, 0, l.length); if (k > 0) ctx.fillText(l.slice(0, k), x + 22 * u, y + 46 * u + lh * (i + 0.5)); acc += l.length + JOIN(); });
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
      var qtext = disp(st.q || "");
      var qp = sc.type === "q" ? (qs.sentT && qs.sentT.length ? clamp((tau - qs.sentT[0].t0) / Math.max(0.4, qs.sentT[qs.sentT.length - 1].t1 - qs.sentT[0].t0) * 1.15, 0, 1) : seg(tau, 0.2, 0.2 + qtext.length / 22)) : 1;
      var qa = sc.type === "q" ? seg(tau, 0.0, 0.35) : 1 - 0.25 * seg(tau, 0.2, 0.8);
      qBottom = drawQuestion(ctx, V, sc, qtext, qp, Ly, qa, sc.type === "a");
    }
    if (sc.type === "a") {
      if (st.tag) { var ta = easeOut(seg(tau, 0.15, 0.6)); ctx.save(); ctx.globalAlpha = ta; chip(ctx, Ly.port ? W / 2 : Ly.qX, qBottom + 14 * u + (1 - ta) * 10 * u, st.tag, 20 * u, "rgba(242,193,78,0.95)", NAVY, Ly.port ? "center" : "left"); ctx.restore(); }
      var c = currentCaption(sc, tau); if (c && O.caps) caption(ctx, V, c.text, c.p, Ly.capY, Ly.capW, 27 * u * Ly.cs, { maxLines: 3 });
      if (O.srcStep) {
        var ss = stepSources(V.w, st).slice(0, 3);
        if (ss.length) {
          var fa = seg(tau, 0.5, 1.1); ctx.save(); ctx.globalAlpha = fa; ctx.font = FS(700, 15 * u * Ly.cs, true);
          var ft = wrap(ctx, TXL(V.lang).src + ss.map(srcLabel).join(" · "), Ly.capW, 1)[0] || "", fy = (O.caps ? Ly.capY + capHalf(Ly) : Ly.capY) + 13 * u * Ly.cs;
          ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillStyle = "rgba(255,255,255,0.8)"; ctx.shadowColor = "rgba(0,0,0,0.85)"; ctx.shadowBlur = 5;
          ctx.fillText(ft, W / 2, fy); ctx.restore();
        }
      }
    } else if (O.caps && !O.qcard) { var c2 = currentCaption(sc, tau); if (c2) caption(ctx, V, c2.text, c2.p, Ly.capY, Ly.capW, 27 * u * Ly.cs, { maxLines: 3 }); }
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
    var c = currentCaption(sc, tau); if (c && V.O.caps) caption(ctx, V, c.text, c.p, Ly.endY, Ly.capW, 30 * u * Ly.cs, { weight: 800, maxLines: 4 });
    if (V.O.cta) {
      var ca = seg(tau, fly + 0.6, fly + 1.2);
      if (ca > 0.01) { ctx.save(); ctx.globalAlpha = ca; notice(ctx, V, TXL(V.lang).cta, Ly.qY + 26 * u, W * (Ly.port ? 0.9 : 0.62), 20 * u, 0.78, GOLD); ctx.restore(); }
    }
  }
  function imgCredits(V) {
    var w = V.w, O = V.O, cred = [], seen = {};
    var T = TXL(V.lang), prevL = LCUR; LCUR = V.lang || "vi";
    w.img.forEach(function (d, k) { if (V.I[k] && V.I[k].ok) { var c = imgCreditOf(d, V.I[k]).replace(/^(?:Ảnh|Photo|Image|写真|画像|图片|Фото|Изображение|사진|이미지)\s*[:：]\s*/i, ""); if (c && !seen[c]) { seen[c] = 1; cred.push(c); } } });
    LCUR = prevL;
    var mu = O.music === "file" ? T.musicOwn : (O.music !== "off" ? T.musicSyn : "");
    return { img: cred, other: [mu, V.AP ? T.voice + AIV.credit(V.AP.voices || AIV.voicesUsed(V.NR, O)) : ""].filter(Boolean) };
  }
  function drawOutro(ctx, V, sc, tau, Ly) {
    var W = V.W, H = V.H, u = Ly.u, O = V.O, w = V.w, a = easeOut(seg(tau, 0.1, 0.8)), port = Ly.port;
    ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = "rgba(5,9,17,0.84)"; ctx.fillRect(0, 0, W, H);
    var qrOn = !!(O.qr && O.qrUrl), qrS = Math.min(W, H) * (port ? (Ly.safe ? 0.25 : 0.32) : Ly.sq ? 0.25 : 0.3);
    var ctaY = port ? (Ly.safe ? H * 0.715 : H * 0.9) : H * (Ly.sq ? 0.875 : 0.86);
    var x = Ly.pad, maxW = W - Ly.pad * 2 - (!port && qrOn ? qrS + 40 * u : 0), y = port ? H * (Ly.safe ? 0.1 : 0.12) : H * 0.08;
    var yLim = port ? (qrOn ? (Ly.safe ? H * 0.47 : H * 0.6) : ctaY - 40 * u) : ctaY - 44 * u;      // chữ không lấn xuống mã QR / lời mời
    ctx.textAlign = "left"; ctx.textBaseline = "top";
    var TL = TXL(V.lang); ctx.font = F(900, 18 * u); ctx.fillStyle = GOLD; ctx.fillText(TL.outroHead, x, y); y += 32 * u;
    ctx.font = FS(800, 38 * u); ctx.fillStyle = "#fff"; wrap(ctx, w.title, maxW, 2).forEach(function (l) { ctx.fillText(l, x, y); y += 44 * u; });
    ctx.font = F(600, 18 * u); ctx.fillStyle = "rgba(255,255,255,0.85)"; wrap(ctx, [w.artist, w.date].filter(Boolean).join(" · "), maxW, 2).forEach(function (l) { ctx.fillText(l, x, y); y += 24 * u; });
    y += 10 * u;
    function line(t, font, color, lh, max) { if (y + lh > yLim) return false; ctx.font = font; ctx.fillStyle = color; wrap(ctx, t, maxW, max || 1).forEach(function (l) { if (y + lh <= yLim) { ctx.fillText(l, x, y); y += lh; } }); return true; }
    // ô lời nhắc AI (vẽ trước khi hết chỗ)
    var aiLines = [];
    if (aiAt(O, "end")) { ctx.font = F(600, 14.5 * u); aiLines = wrap(ctx, "🤖 " + ((V.lang || "vi") === "vi" ? aiText(O) : TL.aiText), maxW - 24 * u, 4); }
    var aiH = aiLines.length ? aiLines.length * 19.5 * u + 18 * u + 10 * u : 0;
    if (O.srcs) {
      var refs = (w.sources || []).filter(function (r) { return r && (r.t || r.u); }), cr = imgCredits(V), keep = yLim - aiH;
      var yl = yLim; yLim = keep;
      if (refs.length && line(TL.refs, F(800, 15.5 * u), GOLD, 22 * u)) {
        refs.slice(0, port ? 7 : 5).forEach(function (r) { line("• " + srcLabel(r) + (r.u ? " — " + domainOf(r.u) : ""), F(500, 14 * u), "rgba(255,255,255,0.78)", 19 * u); });
        y += 6 * u;
      }
      if (cr.img.length) line(TL.photos + cr.img.join(" · "), F(500, 14 * u), "rgba(255,255,255,0.7)", 19 * u, 2);
      if (cr.other.length) line("🎵 " + cr.other.join(" · "), F(500, 14 * u), "rgba(255,255,255,0.7)", 19 * u, 2);
      yLim = yl;
    }
    if (aiLines.length) {
      y += 8 * u; var bh = aiLines.length * 19.5 * u + 16 * u;
      ctx.save(); ctx.fillStyle = "rgba(242,193,78,0.10)"; rr(ctx, x, y, maxW, bh, 10 * u); ctx.fill(); ctx.strokeStyle = "rgba(242,193,78,0.6)"; ctx.lineWidth = 1.4 * u; rr(ctx, x, y, maxW, bh, 10 * u); ctx.stroke(); ctx.restore();
      ctx.font = F(600, 14.5 * u); ctx.fillStyle = "rgba(255,255,255,0.92)"; aiLines.forEach(function (l, i) { ctx.fillText(l, x + 12 * u, y + 8 * u + i * 19.5 * u); });
      y += bh;
    }
    // mã QR + lời mời theo dõi
    if (qrOn) {
      var qx = port ? W / 2 - qrS / 2 : W - Ly.pad - qrS, qy = port ? Math.max(y + 26 * u, Ly.safe ? H * 0.44 : H * 0.56) : H * 0.5 - qrS / 2 - 10 * u;
      if (port && qy + qrS + 34 * u > ctaY - 16 * u) { var s2 = Math.max(W * 0.16, ctaY - 50 * u - qy); qx += (qrS - s2) / 2; qrS = s2; }
      var cv = L.qrCanvas(O.qrUrl);
      if (cv) { ctx.fillStyle = "#fff"; rr(ctx, qx - 10 * u, qy - 10 * u, qrS + 20 * u, qrS + 20 * u, 14 * u); ctx.fill(); ctx.imageSmoothingEnabled = false; ctx.drawImage(cv, qx, qy, qrS, qrS); ctx.imageSmoothingEnabled = true; }
      ctx.font = F(700, 16 * u); ctx.fillStyle = "#fff"; ctx.textAlign = port ? "center" : "left";
      ctx.fillText(/facebook\.com\/profile\.php\?id=/.test(O.qrUrl) ? "Facebook · " + (O.credit || BRAND_NAME) : L.shortUrl(O.qrUrl), port ? W / 2 : qx, qy + qrS + 16 * u);
    }
    ctx.textAlign = "center"; ctx.font = F(900, 25 * u); ctx.fillStyle = GOLD;
    ctx.fillText(TL.followCta, W / 2, ctaY);
    if (O.credit) {
      var cy2 = ctaY + (Ly.sq || Ly.safe ? 31 : 36) * u, logo = O.brand !== false && BRAND.img && BRAND.img.complete && BRAND.img.naturalWidth ? BRAND.img : null, ls = 28 * u, lcy = cy2 + 9 * u;
      ctx.font = F(700, 17 * u); var cw2 = ctx.measureText(O.credit).width, gx = W / 2 - (cw2 + (logo ? ls + 8 * u : 0)) / 2;
      if (logo) { ctx.save(); ctx.beginPath(); ctx.arc(gx + ls / 2, lcy, ls / 2, 0, Math.PI * 2); ctx.clip(); ctx.drawImage(logo, gx, lcy - ls / 2, ls, ls); ctx.restore(); ctx.save(); ctx.strokeStyle = "rgba(242,193,78,0.85)"; ctx.lineWidth = 1.5 * u; ctx.beginPath(); ctx.arc(gx + ls / 2, lcy, ls / 2, 0, Math.PI * 2); ctx.stroke(); ctx.restore(); gx += ls + 8 * u; }
      ctx.fillStyle = "rgba(255,255,255,0.85)"; ctx.textAlign = "left"; ctx.fillText(O.credit, gx, cy2);
      if ((V.lang || "vi") !== "vi" && TL.tagline) { ctx.font = F(600, 13.5 * u); ctx.fillStyle = "rgba(242,193,78,0.85)"; ctx.textAlign = "center"; ctx.fillText(TL.tagline, W / 2, cy2 + 21 * u); }
    }
    ctx.restore();
  }


  /* ---------------- 6b. ẢNH BÌA (thumbnail) ----------------
     Học ý từ FabricJS-Youtube-Thumbnail-Creator (mẫu ảnh bìa lưu dạng JSON, chữ có viền + bóng cho dễ đọc)
     và SoTrxII/thumbnail-generator (preset nền + tiêu đề + phụ đề, tự co cỡ chữ cho vừa khung).
     C = { src: "img"|"frame"|"user", k: số ảnh, focus: chi tiết làm tâm (-1 = cả bức), zoom, px, py (tâm 0–1), fit: "fill"|"fit",
           t: giây (khi lấy khung hình), l1/l2/l3: 3 dòng chữ ({tên}, {n} tự thay), pos: "top"|"mid"|"bot", dim: độ tối nền chữ } */
  var COVER_KEYS = ["src", "k", "focus", "zoom", "px", "py", "fit", "t", "l1", "l2", "l3", "pos", "dim", "tx"];
  function coverDefaults(w, O) {
    var k0 = 0; (w.img || []).some(function (d, k) { if (d && d.file) { k0 = k; return true; } return false; });
    return { src: "img", k: k0, focus: -1, zoom: 1, px: 0.5, py: 0.5, fit: "fill", t: 3, l1: O && O.trend === false ? "GIẢI MÃ TÁC PHẨM" : "GIỜ THÌ TÔI MỚI HIỂU…", l2: "{tên}", l3: "{n} chi tiết ít ai để ý", pos: "mid", dim: 0.55 };
  }
  function coverSig(C) { return JSON.stringify(COVER_KEYS.map(function (k) { return C[k]; })); }
  function coverLoad(w, O) {
    var s = lsGet("av_cover_" + w.id, null), C = coverDefaults(w, O);
    if (s && s.C) COVER_KEYS.forEach(function (k) { if (s.C[k] !== undefined) C[k] = s.C[k]; });
    return { C: C, ok: (s && s.sig === coverSig(C) && s.ok) || {}, sig: s && s.sig };
  }
  function coverSave(w, C, okAspect) {
    var old = lsGet("av_cover_" + w.id, null), sig = coverSig(C), ok = old && old.sig === sig && old.ok ? old.ok : {};
    if (okAspect) ok[okAspect] = Date.now();
    lsSet("av_cover_" + w.id, { C: COVER_KEYS.reduce(function (o, k) { o[k] = C[k]; return o; }, {}), ok: ok, sig: sig });
    return ok;
  }
  function coverIsOk(w, O) { var st = coverLoad(w, O); return !!st.ok[O.aspect]; }
  function coverText(x, V) {
    var n = (V.steps || []).length;
    return disp(String(x || "").replace(/\{n:([^|{}]+)\|([^|{}]+)\|([^|{}]+)\}/g, function (m, a, b, c) { return plRu(n, a, b, c); }).replace(/\{nつ\}/g, n <= 9 ? n + "つ" : String(n)).replace(/\{n\}/g, String(n)).replace(/\{tên\}/g, V.w.title)).replace(/\s+/g, " ").trim();
  }
  // 3 dòng chữ của ảnh bìa theo ngôn ngữ video (tiếng Việt: l1/l2/l3 như cũ; tiếng khác: C.tx[lang] hoặc mẫu mặc định)
  function coverLines(C, l, O) {
    if (!l || l === "vi") return { l1: C.l1, l2: C.l2, l3: C.l3 };
    var x = C.tx && C.tx[l], T = TXL(l);
    return x || { l1: O && O.trend === false ? T.coverL1b : T.coverL1, l2: "{tên}", l3: T.coverL3 };
  }
  // vùng ảnh nguồn sẽ lấp khung bìa (đơn vị điểm ảnh gốc)
  function coverView(V, C) {
    var W = V.W, H = V.H, FA = W / H, el = null, R = null, I = V.I || [];
    if (C.src === "user" && I.coverEl) { el = I.coverEl; R = { x: 0, y: 0, w: el.naturalWidth || el.width, h: el.naturalHeight || el.height }; }
    else {
      var k = C.k, m = I[k]; if (!m || !m.ok) { k = -1; I.some(function (x, j) { if (x && x.ok) { k = j; return true; } return false; }); m = I[k]; }
      if (!m || !m.ok) return null;
      el = m.el; R = { x: m.x0, y: m.y0, w: m.cw, h: m.ch };
      var st = C.focus >= 0 ? (V.w.steps || [])[C.focus] : null;
      if (st && st.b && !st.card && (st.i || 0) === k) {
        var bx = m.x0 + st.b[0] * m.cw, by = m.y0 + st.b[1] * m.ch, bw = st.b[2] * m.cw, bh = st.b[3] * m.ch;
        var gw = Math.max(bw * 1.5, bh * 1.5 * FA), gh = gw / FA;
        R = { x: bx + bw / 2 - gw / 2, y: by + bh / 2 - gh / 2, w: gw, h: gh };
      }
    }
    var IW = el.naturalWidth || el.width, IH = el.naturalHeight || el.height, z = clamp(+C.zoom || 1, 1, 4), vw, vh;
    if (C.fit === "fit") { if (R.w / R.h > FA) { vw = R.w / z; vh = vw / FA; } else { vh = R.h / z; vw = vh * FA; } }
    else { if (R.w / R.h > FA) { vh = R.h / z; vw = vh * FA; } else { vw = R.w / z; vh = vw / FA; } }
    var cx = R.x + R.w * clamp(C.px == null ? 0.5 : C.px, 0, 1), cy = R.y + R.h * clamp(C.py == null ? 0.5 : C.py, 0, 1);
    if (C.fit !== "fit") { if (vw <= IW) cx = clamp(cx, vw / 2, IW - vw / 2); if (vh <= IH) cy = clamp(cy, vh / 2, IH - vh / 2); }
    return { el: el, R: R, cx: cx, cy: cy, vw: vw, vh: vh, IW: IW, IH: IH, blur: (I[C.k] && I[C.k].blur) || null };
  }
  function renderCover(ctx, V, C, guides) {
    LCUR = V.lang || "vi";
    var W = V.W, H = V.H, O = V.O, Ly = LY(W, H, O), u = Ly.u; C = C || V.C || coverDefaults(V.w, O);
    ctx.save(); ctx.fillStyle = "#070b14"; ctx.fillRect(0, 0, W, H);
    if (C.src === "frame") {
      var c0 = V.scenes[0] && V.scenes[0].type === "cover" ? V.scenes[0].dur : 0, tt = clamp(+C.t || 0, c0 + 0.05, V.total - 0.05);
      renderArt(ctx, V, tt);
    } else {
      var cv = coverView(V, C);
      if (cv) {
        var x0 = cv.cx - cv.vw / 2, y0 = cv.cy - cv.vh / 2;
        if (x0 < 0 || y0 < 0 || x0 + cv.vw > cv.IW || y0 + cv.vh > cv.IH) {   // ảnh không phủ kín khung: nền mờ
          var b = cv.blur || cv.el, s0 = Math.max(W / (b.width || b.naturalWidth), H / (b.height || b.naturalHeight)) * 1.1;
          ctx.imageSmoothingEnabled = true; ctx.drawImage(b, (W - (b.width || b.naturalWidth) * s0) / 2, (H - (b.height || b.naturalHeight) * s0) / 2, (b.width || b.naturalWidth) * s0, (b.height || b.naturalHeight) * s0);
          ctx.fillStyle = "rgba(6,10,18,0.5)"; ctx.fillRect(0, 0, W, H);
        }
        ctx.imageSmoothingEnabled = true; ctx.imageSmoothingQuality = "high";
        var k = W / cv.vw; ctx.drawImage(cv.el, (0 - x0) * k, (0 - y0) * k, cv.IW * k, cv.IH * k);
      } else drawMissing(ctx, V);
    }
    // chữ: 3 dòng, tự co cỡ chữ cho vừa
    var CL = coverLines(C, V.lang, O), l1 = coverText(CL.l1, V), l2 = coverText(CL.l2, V), l3 = coverText(CL.l3, V);
    if (l1 || l2 || l3) {
      var port = Ly.port, maxW = W * (port ? 0.86 : Ly.sq ? 0.86 : 0.78), p2 = (port ? 76 : Ly.sq ? 64 : 70) * u, lines2 = [];
      if (l2) { for (; p2 > 30 * u; p2 -= 3 * u) { ctx.font = FS(800, p2); lines2 = wrap(ctx, l2, maxW, 0); if (lines2.length <= (port ? 3 : 2)) break; } if (lines2.length > (port ? 3 : 2)) lines2 = wrap(ctx, l2, maxW, port ? 3 : 2); }
      var p1 = (port ? 30 : 28) * u, p3 = (port ? 28 : 26) * u;
      ctx.font = F(900, p1); var lines1 = l1 ? wrap(ctx, l1.toUpperCase(), maxW, 2) : [];
      ctx.font = F(800, p3); var lines3 = l3 ? wrap(ctx, l3, maxW, 2) : [];
      var g = 14 * u, h = lines1.length * p1 * 1.2 + (lines1.length ? g : 0) + lines2.length * p2 * 1.08 + (lines3.length ? g : 0) + lines3.length * p3 * 1.25;
      var top = port ? (Ly.safe ? H * 0.12 : H * 0.09) : H * 0.08, bot = port ? (Ly.safe ? H * 0.66 : H * 0.9) : H * 0.92;
      var y = C.pos === "top" ? top : C.pos === "bot" ? bot - h : clamp((port ? H * 0.42 : H * 0.5) - h / 2, top, bot - h);
      var dm = clamp(C.dim == null ? 0.55 : +C.dim, 0, 0.9);
      if (dm > 0) { var gr = ctx.createLinearGradient(0, y - 70 * u, 0, y + h + 70 * u); gr.addColorStop(0, "rgba(4,7,14,0)"); gr.addColorStop(0.22, "rgba(4,7,14," + dm + ")"); gr.addColorStop(0.78, "rgba(4,7,14," + dm + ")"); gr.addColorStop(1, "rgba(4,7,14,0)"); ctx.fillStyle = gr; ctx.fillRect(0, y - 70 * u, W, h + 140 * u); }
      ctx.textAlign = "center"; ctx.textBaseline = "top"; ctx.lineJoin = "round";
      function txt(l, yy, color, sw) { ctx.lineWidth = sw; ctx.strokeStyle = "rgba(0,0,0,0.75)"; ctx.strokeText(l, W / 2, yy); ctx.shadowColor = "rgba(0,0,0,0.55)"; ctx.shadowBlur = 10 * u; ctx.fillStyle = color; ctx.fillText(l, W / 2, yy); ctx.shadowBlur = 0; }
      ctx.font = F(900, p1); lines1.forEach(function (l) { txt(l, y, GOLD, p1 * 0.16); y += p1 * 1.2; }); if (lines1.length) y += g;
      ctx.font = FS(800, p2); lines2.forEach(function (l) { txt(l, y, "#ffffff", p2 * 0.12); y += p2 * 1.08; }); if (lines3.length) y += g;
      ctx.font = F(800, p3); lines3.forEach(function (l) { txt(l, y, "#ffe9b0", p3 * 0.16); y += p3 * 1.25; });
    }
    if (guides) {                                                    // chỉ hiện khi xem thử: vùng giữa (ảnh thu nhỏ bị cắt vuông/3:4)
      ctx.save(); ctx.setLineDash([10 * u, 8 * u]); ctx.lineWidth = 2 * u; ctx.strokeStyle = "rgba(79,209,255,0.8)";
      var sq = Math.min(W, H); ctx.strokeRect((W - sq) / 2 + u, (H - sq) / 2 + u, sq - 2 * u, sq - 2 * u);
      if (H > W) { var h34 = W * 4 / 3; ctx.strokeStyle = "rgba(255,255,255,0.45)"; ctx.strokeRect(u, (H - h34) / 2, W - 2 * u, h34); }
      ctx.setLineDash([]); ctx.font = F(700, 13 * u); ctx.fillStyle = "rgba(79,209,255,0.95)"; ctx.textAlign = "left"; ctx.textBaseline = "top";
      ctx.fillText("Khung xanh: phần ảnh bìa hay bị cắt vuông khi hiện ở lưới/ô nhỏ", 10 * u, (H - sq) / 2 + 6 * u); ctx.restore();
    }
    ctx.restore();
  }

  /* ---------------- 7. tiện ích đầu ra: chữ đăng bài, mục lục, phụ đề, ảnh bìa ---------------- */
  function chapters(V) {
    var TL = TXL(V.lang), out = ["0:00 " + TL.chIntro], last = 0;
    V.scenes.forEach(function (sc) { if (sc.type !== "q") return; if (sc.t0 - last < 6) return; out.push(fmtClock(sc.t0) + " " + sc.num + ". " + disp(String(sc.st.tag || sc.st.q)).replace(/^(?:[\d#*]\uFE0F?\u20E3|[\p{Extended_Pictographic}\p{Regional_Indicator}\uFE0F\u200D\p{P}\p{S}\s])+/u, "").trim().slice(0, 60)); last = sc.t0; });
    var e = V.scenes.filter(function (s) { return s.type === "end"; })[0]; if (e) out.push(fmtClock(e.t0) + " " + TL.chEnd);
    return out.join("\n");
  }
  function hashTag(x) { return "#" + String(x).normalize("NFC").split(/[^\p{L}\p{N}]+/u).filter(Boolean).map(function (p) { return p.charAt(0).toUpperCase() + p.slice(1); }).join(""); }
  function postText(w, V) {
    var l = V.lang || "vi", TL = TXL(l), tags = TL.hashtags.concat([hashTag(typeName(w.type, l))]).concat((w.tags || []).slice(0, 4).map(hashTag));
    if (l !== "vi") tags.push("#GiảiMãNghệThuật");
    var tl = l === "vi" ? trendLine(w, V.O) : trendLineX(w, V.O, l);
    var lines = [disp(tl), "", "🎨 " + w.title + (w.titleVi && w.titleVi !== w.title ? " (" + w.titleVi + ")" : "") + (w.artist ? " — " + w.artist : "") + (w.date ? " (" + w.date + ")" : ""), "", disp(w.hook || "")];
    lines.push("", TL.inVideo); V.steps.slice(0, 8).forEach(function (s, i) { lines.push((i + 1) + ". " + disp(s.q || "")); });
    if (w.where) lines.push("", "📍 " + w.where);
    lines.push("", TL.comment);
    var O = V.O || {}, refs = (w.sources || []).filter(function (r) { return r && r.u; });
    if (refs.length) { lines.push("", TL.postRefs); refs.slice(0, 8).forEach(function (r) { lines.push("• " + srcLabel(r) + ": " + r.u); }); }
    if (V.I) { var cr = imgCredits(V); if (cr.img.length) lines.push(TL.photos + cr.img.join(" · ")); }
    if (O.ai) lines.push("", "🤖 " + (l === "vi" ? aiText(O) : TL.aiText));
    if (l !== "vi" && O.qrUrl) lines.push("", "✦ " + (O.credit || BRAND_NAME) + " · " + O.qrUrl);
    lines.push("", tags.filter(function (x, i, a) { return x.length > 2 && a.indexOf(x) === i; }).join(" "));
    return lines.join("\n");
  }
  function posterT(V) { var sc = V.scenes[0]; return sc.type === "cover" ? 0.3 : sc.type === "trend" ? Math.min(sc.dur - 0.6, 2.6) : Math.min(sc.dur - 0.3, 1.2); }
  async function cover(V) {
    var c = document.createElement("canvas"); c.width = V.W; c.height = V.H; var x = c.getContext("2d", { alpha: false });
    renderCover(x, V, V.C);
    return await new Promise(function (r) { c.toBlob(r, "image/jpeg", 0.92); });
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
    ".av-post{width:100%;min-height:150px;font-size:12.5px;border:1px solid #d9d2bd;border-radius:8px;padding:8px;box-sizing:border-box}" +
    ".av-op select{flex:1 1 0;width:0;min-width:0;border:1px solid #d9d2bd;border-radius:8px;padding:7px;font-size:13px;font-family:inherit;background:#fff}" +
    ".tv-ov .tv-main>*{min-width:0}.tv-ov .tv-set{min-width:0}" +
    ".av-ta{width:100%;box-sizing:border-box;border:1px solid #d9d2bd;border-radius:8px;padding:7px 8px;font-size:12.5px;line-height:1.45;font-family:inherit;resize:vertical;margin-top:6px}" +
    ".av-dlg{position:fixed;inset:0;z-index:100000;background:rgba(5,10,20,.55);display:flex;align-items:flex-start;justify-content:center;padding:4vh 12px;overflow:auto}" +
    ".av-dlg-box{background:#f7f4ec;border-radius:16px;max-width:1000px;width:100%;box-shadow:0 20px 60px rgba(0,0,0,.4);color:#1e2733}" +
    ".av-dlg-hd{display:flex;align-items:center;gap:10px;padding:12px 16px;background:linear-gradient(135deg,#152c4e,#0f2138);color:#fff;border-radius:16px 16px 0 0}.av-dlg-hd b{flex:1;font-size:16px}" +
    ".av-dlg-bd{padding:14px 16px;display:grid;gap:10px}.av-dlg-bd input[type=text],.av-dlg-bd textarea,.av-dlg-bd select{width:100%;box-sizing:border-box;border:1px solid #d9d2bd;border-radius:8px;padding:8px;font-size:13.5px;font-family:inherit;background:#fff}" +
    ".av-dlg-bd label{display:grid;gap:4px;font-weight:700;font-size:13px;color:#152c4e}.av-dlg-bd label.av-inl{display:flex;align-items:center;gap:6px}.av-dlg-bd .tv-row input[type=text]{flex:1}" +
    ".av-grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:8px;align-items:end}" +
    ".av-cms{display:grid;grid-template-columns:repeat(auto-fill,minmax(185px,1fr));gap:10px}.av-cm{background:#fff;border:1px solid #e7e3d6;border-radius:10px;padding:6px;display:grid;gap:4px;align-content:start}" +
    ".av-cm img{width:100%;height:130px;object-fit:cover;border-radius:6px;background:#eee}.av-cm-t{font-weight:700;font-size:12px;word-break:break-word}.av-cm-b{display:flex;gap:4px;flex-wrap:wrap}.av-cm-b a{text-decoration:none;color:#152c4e;display:inline-flex;align-items:center}" +
    ".av-srcs{display:grid;gap:5px}.av-src{display:grid;grid-template-columns:22px 1fr 2fr 2fr auto;gap:4px;align-items:center}.av-sn{font-weight:800;color:#152c4e;text-align:center}" +
    "@media(max-width:760px){.av-src{grid-template-columns:22px 1fr auto}.av-src input[data-sx=t],.av-src input[data-sx=u]{grid-column:2/4}}" +
    ".av-chips{display:flex;flex-wrap:wrap;gap:4px;align-items:center}.av-chip{display:inline-flex;gap:3px;align-items:center;border:1px solid #d9d2bd;border-radius:999px;padding:2px 8px;font-size:12px;background:#fff;cursor:pointer;font-weight:600}" +
    ".av-bseg{display:flex;flex-wrap:wrap;gap:4px;margin-top:4px}.av-bseg button{border:1px solid #d9d2bd;background:#fff;border-radius:9px;padding:6px 10px;font-weight:700;cursor:pointer;font-size:13px}.av-bseg button.on{background:#152c4e;color:#fff;border-color:#152c4e}" +
    ".av-bl{display:grid;gap:4px;max-height:38vh;overflow:auto;background:#fff;border:1px solid #e7e3d6;border-radius:10px;padding:8px}.av-bl label{display:flex!important;gap:6px;align-items:center;font-weight:600!important}" +
    ".av-bres{display:grid;gap:4px;font-size:13.5px}.av-brow a{color:#152c4e;font-weight:700}.av-chkcol{display:grid;gap:4px}.av-chkcol select{width:auto!important;display:inline-block}" +
    ".av-covst{font-size:12px;font-weight:800;margin-left:6px;padding:2px 8px;border-radius:999px}.av-covst.ok{background:#e8f6ee;color:#1d6b43}.av-covst.no{background:#fff1e6;color:#a4501b}" +
    ".av-cov{border:2px solid rgba(200,162,75,.55)!important}.av-g2{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin:6px 0}.av-g2 label{display:grid;gap:3px;font-size:12px;font-weight:700;color:#152c4e;min-width:0}" +
    ".av-g2 select,.av-cov input[type=text],.av-cov select{width:100%;min-width:0;box-sizing:border-box;border:1px solid #d9d2bd;border-radius:8px;padding:6px 7px;font-size:12.5px;font-family:inherit;background:#fff}.av-cov input[type=text]{margin-top:5px}" +
    ".av-btns{flex-wrap:wrap;gap:4px!important}.av-btns span{font-size:12px;font-weight:700;color:#5c6773}.av-btns button{border:1px solid #d9d2bd;background:#fff;border-radius:8px;padding:5px 9px;font-weight:700;cursor:pointer;font-size:12.5px}.av-btns button.on{background:#152c4e;color:#fff;border-color:#152c4e}" +
    ".av-gate{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:14px;align-items:start}@media(max-width:700px){.av-gate{grid-template-columns:1fr}}.av-gate-img{display:flex;justify-content:center}.av-gate-tx p{margin:0 0 10px;line-height:1.5}" +
    ".av-pub{margin-top:10px;background:#fff;border:1px solid #e7e3d6;border-radius:12px;padding:10px;display:grid;gap:6px}.av-pubst{display:grid;gap:4px;font-size:13px}.av-pubst a{color:#152c4e;font-weight:700}" +
    ".av-steps{margin:0;padding-left:20px;display:grid;gap:6px;font-size:13.5px;line-height:1.5}.av-steps a{color:#152c4e;font-weight:700}.av-steps code{background:#fff;border:1px solid #e7e3d6;border-radius:6px;padding:1px 5px}" +
    ".av-cvg{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:8px}.av-cvi{background:#fff;border:2px solid #e7e3d6;border-radius:10px;padding:5px;display:grid;gap:4px;font-size:12px}.av-cvi.ok{border-color:#3aa76d}.av-cvi canvas{width:100%;height:auto;border-radius:6px;background:#0c1b30}.av-cvi label{display:flex!important;gap:4px;align-items:center;font-weight:700!important}";
  function ensureCSS() {
    if (!document.getElementById("tv-css")) { var s = document.createElement("style"); s.id = "tv-css"; s.textContent = L.CSS; document.head.appendChild(s); }
    if (!document.getElementById("av-css")) { var s2 = document.createElement("style"); s2.id = "av-css"; s2.textContent = CSS; document.head.appendChild(s2); }
  }

  /* ---------------- 10. Wikimedia Commons: tìm ảnh có giấy phép mở ----------------
     API MediaWiki (CORS: origin=*): generator=search trong không gian File, prop=imageinfo + extmetadata
     (cách Openverse lấy ảnh Commons: LicenseShortName/LicenseUrl, Artist là HTML → bóc chữ). */
  function textOf(html) {
    try { return (new DOMParser().parseFromString(String(html || ""), "text/html").body.textContent || "").replace(/\s+/g, " ").trim(); }
    catch (e) { return String(html || "").replace(/<[^>]*>/g, " ").replace(/\s+/g, " ").trim(); }
  }
  function normLic(l) { l = String(l || "").trim(); return /^(public domain|pd)\b/i.test(l) ? "Phạm vi công cộng" : l; }
  async function commonsSearch(q, n) {
    var url = "https://commons.wikimedia.org/w/api.php?action=query&format=json&formatversion=2&origin=*&generator=search&gsrnamespace=6&gsrlimit=" + (n || 30) +
      "&gsrsearch=" + encodeURIComponent(q) + "&prop=imageinfo&iiprop=url|size|mime|extmetadata&iiurlwidth=330&iiextmetadatafilter=LicenseShortName|Artist|Credit|ImageDescription|DateTimeOriginal";
    var r = await fetch(url); if (!r.ok) throw new Error("Commons trả lỗi " + r.status);
    var j = await r.json(), pages = (j.query && j.query.pages) || [];
    pages.sort(function (a, b) { return (a.index || 0) - (b.index || 0); });
    return pages.map(function (p) {
      var ii = (p.imageinfo || [])[0] || {}, em = ii.extmetadata || {};
      function g(k) { return textOf(em[k] && em[k].value); }
      return { file: String(p.title || "").replace(/^File:/, ""), w: ii.width || 0, h: ii.height || 0, mime: ii.mime || "", thumb: ii.thumburl || "", page: ii.descriptionurl || "",
               lic: normLic(g("LicenseShortName")), by: g("Artist") || g("Credit"), desc: g("ImageDescription").slice(0, 160), date: g("DateTimeOriginal") };
    }).filter(function (x) { return /^image\/(jpeg|png|webp|svg\+xml)$/.test(x.mime) && x.w >= 500 && x.h >= 300; });
  }

  /* ---------------- 11. mẫu lệnh nhờ AI soạn kịch bản ----------------
     Cấu trúc lệnh học theo MoneyPrinterTurbo (vai trò → mục tiêu → ràng buộc → tham số) và ShortGPT (bắt trả đúng một khối JSON);
     thêm yêu cầu riêng: nguồn thật cho từng lời giải, nói rõ chỗ còn tranh cãi, không chép lời bài hát. */
  function aiPrompt(w, P) {
    P = P || {}; var t = typeOf(w.type), n = P.n || 8, ex = null;
    (DB().works || []).some(function (x) { var st = (x.steps || []).filter(function (y) { return y.b && y.src && y.s; })[0]; if (st) { ex = { w: x, st: st }; return true; } return false; });
    var types = (DB().types || []).map(function (x) { return x.id + " = " + x.vi; }).join("; "), eras = (DB().eras || []).map(function (x) { return x.id + " = " + x.vi; }).join("; ");
    var L1 = [
      "Bạn là biên kịch video ngắn kiểu «Giờ thì tôi mới hiểu vì sao người ta có thể dành hàng giờ ngắm nhìn một bức tranh»: dẫn người xem đi qua từng chi tiết của một tác phẩm; mỗi chi tiết là một câu hỏi gợi tò mò và một lời giải ngắn, đúng sự thật.",
      "",
      "TÁC PHẨM: " + (P.title || w.title) + (P.by ? " — " + P.by : ""),
      "THỂ LOẠI: " + t.vi + " (" + (w.type || "painting") + ")",
      P.notes ? "GHI CHÚ CỦA TÔI: " + P.notes : "",
      P.img ? "Tôi đính kèm ảnh tác phẩm: hãy ước lượng khung của từng chi tiết trên chính ảnh này." : "Tôi chưa đính kèm ảnh: để \"b\": null, tôi sẽ tự vẽ khung sau.",
      "",
      "YÊU CẦU",
      "1. Tiếng Việt tự nhiên, câu ngắn, dễ đọc thành tiếng bằng giọng máy. Không dùng ký hiệu lạ, không viết tắt.",
      "2. Chỉ viết điều có nguồn đáng tin. Điều còn tranh cãi thì nói rõ «theo một số tài liệu», «có ý kiến cho rằng». Không bịa trích dẫn, số liệu, giai thoại. Không chép lời bài hát hay thơ.",
      "3. \"hook\": 1–2 câu mở đầu gây tò mò, tối đa 220 ký tự.",
      "4. \"openers\": 3 câu mở đầu khác nhau (một câu hỏi; một câu «Có một chi tiết…»; một lời thách tìm chi tiết), mỗi câu tối đa 100 ký tự, không phóng đại kiểu «99% người…».",
      "5. \"steps\": đúng " + n + " chi tiết, kể theo trình tự hợp lý (từ nổi bật đến tinh tế). Mỗi chi tiết có:",
      "   - \"tag\": nhãn ngắn tối đa 24 ký tự, mở đầu bằng 1 emoji (ví dụ \"🐱 Mèo = kẻ quyền thế\");",
      "   - \"q\": câu hỏi gợi tò mò, tối đa 90 ký tự;",
      "   - \"a\": lời giải 2–3 câu, tối đa 260 ký tự, câu đầu là đáp án;",
      "   - \"s\": lời giải rút gọn một câu, tối đa 120 ký tự (cho bản 1 phút);",
      "   - \"k\": 1 cho đúng 4 chi tiết hay nhất (bản ngắn), còn lại 0;",
      "   - \"b\": [x, y, w, h] khung chi tiết trên ảnh, tỉ lệ 0–1 tính từ góc trên bên trái (null nếu không có ảnh);",
      "   - \"card\": chỉ dùng cho chuyện không chỉ ra được trên hình (năm tháng, con số): {\"big\": \"1944\", \"sub\": \"dòng phụ\"}, khi đó \"b\": null;",
      "   - \"src\": mảng số thứ tự (bắt đầu từ 0) của các nguồn trong \"sources\" đỡ cho lời giải.",
      "6. \"sources\": 3–8 nguồn thật, ưu tiên bảo tàng, cơ quan di sản, báo lớn, sách và bài nghiên cứu: {\"t\": \"Nơi đăng — tên bài\", \"u\": \"đường dẫn đầy đủ\", \"s\": \"tên ngắn tối đa 24 ký tự\"}. Chỉ ghi đường dẫn bạn chắc chắn tồn tại; không chắc thì để \"u\": \"\".",
      "7. Thông tin chung: \"title\", \"artist\", \"date\", \"y\" (năm, dạng số), \"type\" (một trong: " + types + "), \"era\" (một trong: " + eras + "), \"medium\", \"where\" (nơi lưu giữ), \"place\" {\"name\", \"prov\", \"lat\", \"lon\"}, \"tags\" (3–5 từ khoá), \"intro\" (1 câu giới thiệu), \"end\" (1–2 câu kết, có thể bắt đầu bằng «Giờ thì bạn đã hiểu…»).",
      "8. Chỉ trả về MỘT khối JSON hợp lệ, không giải thích, không markdown.",
      "",
      "KHUÔN JSON:",
      "{\"title\": \"…\", \"artist\": \"…\", \"date\": \"…\", \"y\": 1900, \"type\": \"" + (w.type || "painting") + "\", \"era\": \"…\", \"medium\": \"…\", \"where\": \"…\", \"place\": {\"name\": \"…\", \"prov\": \"…\", \"lat\": 21.03, \"lon\": 105.85}, \"tags\": [\"…\"], \"hook\": \"…\", \"intro\": \"…\", \"openers\": [\"…\", \"…\", \"…\"], \"steps\": [{\"tag\": \"…\", \"q\": \"…\", \"a\": \"…\", \"s\": \"…\", \"k\": 1, \"b\": [0.1, 0.2, 0.3, 0.3], \"src\": [0]}], \"end\": \"…\", \"sources\": [{\"t\": \"…\", \"u\": \"https://…\", \"s\": \"…\"}]}"
    ];
    if (ex) L1.push("", "VÍ DỤ MỘT CHI TIẾT ĐẠT YÊU CẦU (tranh " + ex.w.title + "):", JSON.stringify({ tag: ex.st.tag, q: ex.st.q, a: ex.st.a, s: ex.st.s, k: 1, b: ex.st.b, src: ex.st.src }));
    return L1.filter(function (x, i, a) { return x !== "" || a[i - 1] !== ""; }).join("\n");
  }
  function parseAIJSON(txt) {
    var t = String(txt || "").trim().replace(/^```(?:json)?\s*/i, "").replace(/```\s*$/, "");
    var a = t.indexOf("{"), b = t.lastIndexOf("}"); if (a < 0 || b <= a) throw new Error("Không thấy khối JSON trong nội dung dán vào.");
    try { return JSON.parse(t.slice(a, b + 1)); } catch (e) { throw new Error("JSON chưa hợp lệ: " + (e.message || e)); }
  }
  // áp kết quả của AI vào tác phẩm; trả về thống kê để báo lại
  function applyAI(w, o) {
    function str(x, max) { x = x == null ? "" : String(x).replace(/\s+/g, " ").trim(); return max ? x.slice(0, max) : x; }
    var srcs = (Array.isArray(o.sources) ? o.sources : []).filter(function (r) { return r && (r.t || r.u); }).slice(0, 10).map(function (r) { var u = str(r.u); return { t: str(r.t, 200), u: /^https?:\/\//i.test(u) ? u : "", s: str(r.s, 28) }; });
    var nImg = Math.max(1, (w.img || []).length);
    var steps = (Array.isArray(o.steps) ? o.steps : []).filter(function (x) { return x && (x.q || x.a); }).slice(0, 14).map(function (x) {
      var st = { tag: str(x.tag, 40), q: str(x.q, 200), a: str(x.a, 600) };
      if (x.s) st.s = str(x.s, 260); if (x.k) st.k = 1;
      if (x.card && (x.card.big || x.card.sub)) st.card = { big: str(x.card.big, 24), sub: str(x.card.sub, 90) };
      else {
        var b = Array.isArray(x.b) && x.b.length === 4 && x.b.every(function (v) { return typeof v === "number" && isFinite(v); }) ? x.b : null;
        if (b) { var bx = clamp(b[0], 0, 0.97), by = clamp(b[1], 0, 0.97); st.b = [bx, by, clamp(b[2], 0.03, 1 - bx), clamp(b[3], 0.03, 1 - by)].map(function (v) { return +v.toFixed(4); }); }
        else { st.b = [0.3, 0.3, 0.4, 0.4]; st.nobox = 1; }
        st.i = typeof x.i === "number" && x.i >= 0 && x.i < nImg ? Math.floor(x.i) : 0;
      }
      var sr = Array.isArray(x.src) ? x.src.filter(function (i) { return i === Math.floor(i) && i >= 0 && i < srcs.length; }) : []; if (sr.length) st.src = sr.slice(0, 3);
      return st;
    });
    if (!steps.length) throw new Error("Kết quả không có chi tiết nào (mục \"steps\").");
    var kk = steps.filter(function (x) { return x.k; }); if (!kk.length) steps.slice(0, 4).forEach(function (x) { x.k = 1; }); else kk.slice(6).forEach(function (x) { delete x.k; });
    w.steps = steps; if (srcs.length) w.sources = srcs;
    ["hook", "intro", "end"].forEach(function (k) { if (o[k]) w[k] = str(o[k], 500); });
    if (Array.isArray(o.openers)) w.openers = o.openers.map(function (x) { return str(x, 140); }).filter(Boolean).slice(0, 5);
    if (w.custom) {
      ["title", "artist", "date", "medium", "where"].forEach(function (k) { if (o[k]) w[k] = str(o[k], 200); });
      if (typeof o.y === "number" && isFinite(o.y)) w.y = Math.round(o.y);
      if (o.type && (DB().types || []).some(function (t) { return t.id === o.type; })) w.type = o.type;
      if (o.era && (DB().eras || []).some(function (e) { return e.id === o.era; })) w.era = o.era;
      if (o.place && typeof o.place.lat === "number" && typeof o.place.lon === "number") w.place = { name: str(o.place.name, 80), prov: str(o.place.prov, 60), lat: o.place.lat, lon: o.place.lon, approx: true };
      if (Array.isArray(o.tags)) w.tags = o.tags.map(function (x) { return str(x, 30); }).filter(Boolean).slice(0, 6);
    }
    return { n: steps.length, k: steps.filter(function (x) { return x.k; }).length, src: srcs.length, nobox: steps.filter(function (x) { return x.nobox; }).length,
             nosrc: steps.filter(function (x) { return !x.src; }).length, nourl: srcs.filter(function (x) { return !x.u; }).length };
  }

  /* ---------------- 12. hộp thoại dùng chung ---------------- */
  function dialog(host, title, html) {
    ensureCSS();
    var d = document.createElement("div"); d.className = "av-dlg";
    d.innerHTML = '<div class="av-dlg-box"><div class="av-dlg-hd"><b>' + title + '</b><button class="tv-x" data-dlg="x">✕ Đóng</button></div><div class="av-dlg-bd">' + html + "</div></div>";
    (host || document.body).appendChild(d);
    d.addEventListener("click", function (e) { if (e.target === d || e.target.closest('[data-dlg="x"]')) { if (d._onClose) try { d._onClose(); } catch (er) { } d.remove(); } });
    return d;
  }

  /* ---------------- 13. xuất hàng loạt ----------------
     Dựng lần lượt từng video (giống nút Xuất trong studio), tải về ngay khi xong; giữ màn hình sáng (Wake Lock) trong lúc chạy. */
  function findWork(id) {
    var c = listCustom().filter(function (x) { return x.id === id; })[0]; if (c) return clone(c);
    var b = (DB().works || []).filter(function (x) { return x.id === id; })[0]; return b ? resolve(b) : null;
  }
  async function produce(w, o, I, ui, isC, onCancel) {
    await ensureBrand();
    var steps = pickSteps(w, o), NR = narrate(w, o, steps), AP = null;
    if (o.voice === "ai") AP = await AIV.synthNarration(NR, o, ui, isC);
    if (isC()) throw new Error("cancel");
    var d = L.dims(o), V = build(w, o, d.W, d.H, NR, AP, I);
    var mix = (o.voice === "ai" || o.music !== "off") ? await L.mixAudio(V, o, null, ui) : null;
    if (o.qr && o.qrUrl) { await L.ensureQR(); L.qrCanvas(o.qrUrl); }
    var r = await L.exportVideo(V, { phase: ui.phase, onCancel: onCancel }, mix);
    return { r: r, V: V };
  }
  function openKeyOf(id, l) { return "av_open_" + id + (l && l !== "vi" ? "@" + l : ""); }
  function batch(ids, bo) {
    bo = bo || {}; var O = loadOpts(), works = (ids || []).map(findWork).filter(Boolean);
    var S = { aspect: O.aspect, len: "short", res: O.res, voice: O.voice, music: O.music === "file" ? "auto" : O.music, extras: true, dl: O.autoDl !== false, dir: false, yt: !!(O.ytAuto && YT.cid()), ytPrivacy: O.ytPrivacy || "private", langs: [O.vlang || "vi"] };
    function segB(k, label, opts) { return '<div><b>' + label + '</b><div class="av-bseg" data-bk="' + k + '">' + opts.map(function (x) { return '<button data-dlg="seg" data-v="' + x[0] + '"' + (String(S[k]) === String(x[0]) ? ' class="on"' : "") + ">" + x[1] + "</button>"; }).join("") + "</div></div>"; }
    var d = dialog(document.body, "📦 Xuất hàng loạt (" + works.length + " tác phẩm)",
      '<div class="av-tip">Máy dựng lần lượt từng video. Hãy để trang này mở (không thu nhỏ trình duyệt) cho tới khi xong; lần đầu Chrome có thể hỏi «cho phép tải nhiều tệp» — bấm Cho phép. Các tuỳ chọn khác (nguồn, nhãn AI, vùng an toàn, chữ ký, mã QR, câu mở đầu, ảnh bìa đã chốt) lấy theo studio.</div>' +
      '<div class="av-grid2">' + segB("aspect", "Khung hình", [["9:16", "▯ Dọc"], ["16:9", "▭ Ngang"], ["1:1", "◻ Vuông"]]) + segB("len", "Độ dài", [["short", "⚡ Ngắn"], ["full", "📖 Đầy đủ"]]) +
      segB("res", "Độ nét", [[720, "720p"], [1080, "1080p"]]) + segB("voice", "Lời đọc", [["ai", "🤖 Giọng AI"], ["off", "🔇 Không"]]) + segB("music", "Nhạc nền", [["auto", "✨ Tự chọn"], ["off", "Tắt"]]) + "</div>" +
      '<div><b>🌐 Ngôn ngữ video</b><div class="av-bseg">' + LANGS.map(function (l) { return '<label class="av-inl"><input type="checkbox" data-blang="' + l + '"' + (S.langs.indexOf(l) >= 0 ? " checked" : "") + "/> " + LINFO[l].flag + " " + LINFO[l].name + "</label>"; }).join("") +
      '</div><div class="av-tip">Mỗi tác phẩm xuất một video cho mỗi ngôn ngữ được chọn (giọng đọc theo lựa chọn trong studio). Ảnh bìa chốt một lần cho mỗi khung hình; chữ trên ảnh bìa tự đổi theo ngôn ngữ. Tác phẩm chưa có bản dịch sẽ bị bỏ qua.</div></div>' +
      '<div class="tv-row"><button class="av-mini" data-dlg="all">Chọn tất cả</button><button class="av-mini" data-dlg="none">Bỏ chọn</button><span class="av-tip" data-dlg="cnt"></span></div>' +
      '<div class="av-bl">' + works.map(function (w, i) { var need = (w.img || []).some(function (m) { return m.user; }); return '<label><input type="checkbox" data-bi="' + i + '" checked/> ' + typeOf(w.type).icon + " " + escH(w.title) + (need ? ' <span class="av-tip">(cần ảnh của anh)</span>' : "") + "</label>"; }).join("") + "</div>" +
      '<b>🖼️ Ảnh bìa — phải chốt trước khi xuất</b><div class="av-tip">Xem từng ảnh bìa bên dưới; ảnh nào chưa ưng thì bấm ✏️ để sửa trong studio. Tick «Chốt» (hoặc bấm «Chốt tất cả») rồi mới bắt đầu được.</div>' +
      '<div class="tv-row"><button class="av-mini" data-dlg="okall">✅ Chốt tất cả ảnh bìa đang hiện</button><span class="av-tip" data-dlg="covcnt"></span></div><div class="av-cvg" data-dlg="covers"></div>' +
      '<b>📤 Lưu & đăng mỗi video</b><div class="av-chkcol">' +
      '<label class="av-inl"><input type="checkbox" data-dlg="extras"' + (S.extras ? " checked" : "") + '/> Kèm ảnh bìa, phụ đề .srt và lời đăng .txt (có mục lục YouTube)</label>' +
      '<label class="av-inl"><input type="checkbox" data-dlg="dl"' + (S.dl ? " checked" : "") + '/> ⬇️ Tự tải về máy (thư mục Tải về)</label>' +
      (FSX.ok() ? '<label class="av-inl"><input type="checkbox" data-dlg="dir"/> 📁 Lưu thẳng vào thư mục <b data-dlg="dirname">(chưa chọn)</b> <button class="av-mini" data-dlg="pickdir">Chọn…</button></label>' : "") +
      '<label class="av-inl"><input type="checkbox" data-dlg="yt"' + (S.yt ? " checked" : "") + (YT.cid() ? "" : " disabled") + '/> ▶️ Tự đăng YouTube ' + (YT.cid() ? "" : '<span class="av-tip">(cài đặt trong studio: 📤 Lưu & đăng → ⚙️)</span>') +
      ' <select data-dlg="ytpriv"><option value="private">🔒 Riêng tư</option><option value="unlisted">🔗 Không công khai</option><option value="public">🌐 Công khai</option></select></label></div>' +
      '<div class="tv-go" style="flex-direction:row;flex-wrap:wrap"><button class="tv-b navy" data-dlg="start">▶ Bắt đầu xuất</button><button class="tv-b tv-hide" data-dlg="stop">⏹ Dừng</button></div>' +
      '<div class="tv-prog" data-dlg="prog" style="display:none"><b data-dlg="ph">…</b><div class="tv-bar"><i></i></div></div><div class="av-bres" data-dlg="res"></div>');
    var $d = function (q) { return d.querySelector(q); }, running = false, cancelled = false, cancelFn = null, lock = null, urls = [], dirH = null, IMGS = {}, done = [];
    $d('[data-dlg="ytpriv"]').value = S.ytPrivacy;
    FSX.get().then(function (h) { dirH = h; var dn = $d('[data-dlg="dirname"]'); if (dn) dn.textContent = h ? h.name : "(chưa chọn)"; var dc = $d('[data-dlg="dir"]'); if (dc && h) dc.checked = true; });
    function picked() { return Array.prototype.map.call(d.querySelectorAll("[data-bi]:checked"), function (c) { return works[+c.dataset.bi]; }); }
    function cnt() { var nb = d.querySelectorAll("[data-bi]:checked").length; $d('[data-dlg="cnt"]').textContent = nb + " / " + works.length + " được chọn" + (S.langs.length > 1 ? " × " + S.langs.length + " ngôn ngữ = " + nb * S.langs.length + " video" : ""); }
    function optsFor(w, l) { var o = loadOpts(); Object.keys(S).forEach(function (k) { if (["aspect", "len", "res", "voice", "music"].indexOf(k) >= 0) o[k] = S[k]; }); o.vlang = l || S.langs[0] || "vi"; o.music = musicFor(w, o); o.trendText = lsGet(openKeyOf(w.id, o.vlang), "") || ""; o.ytPrivacy = S.ytPrivacy; o.coverC = coverLoad(w, o).C; return o; }
    var covTok = 0;
    async function covers() {                                   // vẽ ảnh bìa của các tác phẩm đang chọn
      var my = ++covTok, box = $d('[data-dlg="covers"]'), list = picked(), l0 = S.langs[0] || "vi"; box.innerHTML = "";
      await ensureLang(l0); if (my !== covTok) return;
      for (var i = 0; i < list.length; i++) {
        if (my !== covTok) return;
        var w = list[i], o = optsFor(w), ok = !!coverLoad(w, o).ok[S.aspect], it = document.createElement("div");
        it.className = "av-cvi" + (ok ? " ok" : ""); it.dataset.id = w.id;
        it.innerHTML = '<canvas></canvas><div><b>' + escH(w.title) + '</b></div><label><input type="checkbox" data-cok="' + escH(w.id) + '"' + (ok ? " checked" : "") + '/> Chốt</label><button class="av-mini" data-dlg="edit" data-id="' + escH(w.id) + '">✏️ Sửa</button>';
        box.appendChild(it);
        try {
          var I = IMGS[w.id] || (IMGS[w.id] = await loadWorkImages(w)); if (my !== covTok) return;
          var dd = L.dims(o), sc = 300 / Math.max(dd.W, dd.H), cw = Math.round(dd.W * sc), ch = Math.round(dd.H * sc), lw = localize(w, l0), Vs = build(lw, o, cw, ch, narrate(lw, o, pickSteps(lw, o)), null, I), c = it.querySelector("canvas");
          c.width = cw; c.height = ch; renderCover(c.getContext("2d"), Vs, o.coverC);
        } catch (er) { it.querySelector("div").innerHTML += ' <span class="av-tip">(lỗi ảnh)</span>'; }
      }
      covCnt();
    }
    function covCnt() { var all = d.querySelectorAll("[data-cok]"), ok = d.querySelectorAll("[data-cok]:checked"); $d('[data-dlg="covcnt"]').textContent = ok.length + " / " + all.length + " ảnh bìa đã chốt"; return all.length && ok.length === all.length; }
    function setOk(id, on) { var w = works.filter(function (x) { return x.id === id; })[0]; if (!w) return; var o = optsFor(w), st = coverLoad(w, o); if (on) coverSave(w, st.C, S.aspect); else { var raw = lsGet("av_cover_" + w.id, null); if (raw && raw.ok) { delete raw.ok[S.aspect]; lsSet("av_cover_" + w.id, raw); } } var it = d.querySelector('.av-cvi[data-id="' + id + '"]'); if (it) it.classList.toggle("ok", on); covCnt(); }
    cnt(); covers();
    d._onClose = function () { cancelled = true; covTok++; if (cancelFn) try { cancelFn(); } catch (e) { } urls.forEach(function (u) { try { URL.revokeObjectURL(u); } catch (e) { } }); if (lock) try { lock.release(); } catch (e) { } };
    d.addEventListener("change", function (e) {
      var t = e.target;
      if (t.dataset.bi != null) { cnt(); clearTimeout(t._t); t._t = setTimeout(covers, 250); }
      if (t.dataset.cok) setOk(t.dataset.cok, t.checked);
      if (t.dataset.blang) { S.langs = LANGS.filter(function (l) { var c = d.querySelector('[data-blang="' + l + '"]'); return c && c.checked; }); if (!S.langs.length) { t.checked = true; S.langs = [t.dataset.blang]; } cnt(); covers(); }
      if (t.dataset.dlg === "extras") S.extras = t.checked; if (t.dataset.dlg === "dl") S.dl = t.checked; if (t.dataset.dlg === "yt") S.yt = t.checked; if (t.dataset.dlg === "ytpriv") S.ytPrivacy = t.value;
    });
    d.addEventListener("click", async function (e) {
      var b = e.target.closest("[data-dlg]"); if (!b) return; var k = b.dataset.dlg;
      if (k === "seg" && !running) { var g = b.closest("[data-bk]"), key = g.dataset.bk; S[key] = key === "res" ? +b.dataset.v : b.dataset.v; g.querySelectorAll("button").forEach(function (x) { x.classList.toggle("on", x === b); }); if (key === "aspect" || key === "len") covers(); }
      else if (k === "all" || k === "none") { d.querySelectorAll("[data-bi]").forEach(function (c) { c.checked = k === "all"; }); cnt(); covers(); }
      else if (k === "okall") { d.querySelectorAll("[data-cok]").forEach(function (c) { c.checked = true; setOk(c.dataset.cok, true); }); }
      else if (k === "edit" && !running) { var id = b.dataset.id, w = works.filter(function (x) { return x.id === id; })[0]; d._onClose(); d.remove(); if (w) open(w, { onClose: function () { batch(ids, bo); } }); }
      else if (k === "pickdir") { e.preventDefault(); try { dirH = await FSX.pick(); $d('[data-dlg="dirname"]').textContent = dirH.name; $d('[data-dlg="dir"]').checked = true; } catch (er) { } }
      else if (k === "stop") { cancelled = true; if (cancelFn) try { cancelFn(); } catch (er) { } $d('[data-dlg="ph"]').textContent = "Đang dừng…"; }
      else if (k === "start" && !running) run();
      else if (k === "ytrest" && !running) ytRest(b);
    });
    async function run() {
      var pick = picked(); if (!pick.length) return;
      if (!covCnt()) { alert("Còn ảnh bìa chưa chốt — hãy xem lại và tick «Chốt» (hoặc «Chốt tất cả») trước khi xuất."); $d('[data-dlg="covers"]').scrollIntoView({ behavior: "smooth", block: "center" }); return; }
      var useDir = !!($d('[data-dlg="dir"]') && $d('[data-dlg="dir"]').checked && dirH), useYt = !!(S.yt && YT.cid());
      if (useYt) { try { await YT.token(); } catch (er) { alert("⚠️ YouTube: " + (er && er.message || er) + "\nVideo vẫn được xuất, chưa đăng YouTube."); useYt = false; } }
      if (useDir && !(await FSX.ensure(dirH))) { useDir = false; alert("Trình duyệt chưa cho ghi vào thư mục — video sẽ được tải về thư mục Tải về."); }
      running = true; cancelled = false; b2(true); done = [];
      for (var li = 0; li < S.langs.length; li++) await ensureLang(S.langs[li]);
      var jobs = []; pick.forEach(function (w) { S.langs.forEach(function (l) { jobs.push({ w: w, l: l }); }); });
      try { if (navigator.wakeLock) lock = await navigator.wakeLock.request("screen"); } catch (e) { lock = null; }
      var prog = $d('[data-dlg="prog"]'), ph = $d('[data-dlg="ph"]'), bar = prog.querySelector(".tv-bar i"), res = $d('[data-dlg="res"]'), ok = 0;
      prog.style.display = "block";
      for (var n = 0; n < jobs.length && !cancelled; n++) {
        var w0 = jobs[n].w, lg = jobs[n].l, w = localize(w0, lg), tag = (S.langs.length > 1 || lg !== "vi" ? LINFO[lg].flag + " " : ""), head = "[" + (n + 1) + "/" + jobs.length + "] " + tag + w0.title + " · ";
        var ui = { phase: function (txt, f) { ph.textContent = head + txt; bar.style.width = Math.round(clamp((n + clamp(f || 0, 0, 1)) / jobs.length, 0, 1) * 100) + "%"; } };
        var row = document.createElement("div"); row.className = "av-brow"; row.innerHTML = "⏳ " + tag + escH(w0.title); res.appendChild(row);
        try {
          if (lg !== "vi" && w.trMissing < 0) { row.innerHTML = "⏭️ " + tag + escH(w0.title) + ' <span class="av-tip">— bỏ qua: chưa có bản dịch ' + escH(LINFO[lg].name) + " (mở studio → 🌐 → 🤖 Nhờ AI dịch)</span>"; continue; }
          ui.phase("Đang tải ảnh…", 0);
          var I = IMGS[w0.id] || (IMGS[w0.id] = await loadWorkImages(w0));
          if (!I.some(function (m) { return m && m.ok; })) { row.innerHTML = "⏭️ " + tag + escH(w0.title) + ' <span class="av-tip">— bỏ qua: chưa có ảnh (tranh còn bản quyền cần ảnh của anh)</span>'; continue; }
          var o = optsFor(w0, lg);
          var out = await produce(w, o, I, ui, function () { return cancelled; }, function (fn) { cancelFn = fn; });
          var base = L.slug(w0.title) + "-" + o.aspect.replace(":", "x") + (o.len === "short" ? "-ngan" : "") + (lg !== "vi" ? "-" + lg : ""), name = base + "." + out.r.ext, url = URL.createObjectURL(out.r.blob); urls.push(url);
          var files = S.extras ? await bundleFiles(w, out.V, out.r, base) : [{ name: name, blob: out.r.blob, kind: "video" }], notes = [];
          if (S.dl) { files.forEach(function (f, i) { setTimeout(function () { L.dl(f.blob, f.name); }, i * 450); }); notes.push("đã tải về"); }
          if (useDir) { try { for (var fi = 0; fi < files.length; fi++) await FSX.write(dirH, L.slug(w0.title), files[fi].name, files[fi].blob); notes.push("đã lưu vào «" + escH(dirH.name + "/" + L.slug(w0.title)) + "»"); } catch (er) { notes.push("⚠️ lưu thư mục lỗi: " + escH(er.message)); } }
          ok++; row.innerHTML = "✅ " + tag + '<a href="' + url + '" download="' + escH(name) + '">' + escH(name) + "</a> · " + (out.r.blob.size / 1048576).toFixed(1) + " MB · " + fmtClock(out.V.total) + (notes.length ? " · " + notes.join(" · ") : "");
          var item = { w: w, o: o, V: out.V, files: files.length > 1 ? files : await bundleFiles(w, out.V, out.r, base), row: row, yt: null }; done.push(item);
          if (useYt && !cancelled) { ui.phase("Đang đăng YouTube…", 1); await ytOne(item); }
        } catch (er) {
          if (String(er && er.message) === "cancel" || cancelled) { row.innerHTML = "⏹ " + tag + escH(w0.title) + " — đã dừng"; break; }
          row.innerHTML = "⚠️ " + tag + escH(w0.title) + " — lỗi: " + escH(er && er.message || er);
        }
        cancelFn = null; await sleep(300);
      }
      try { AIV.dispose(); } catch (e) { }
      if (lock) try { await lock.release(); } catch (e) { } lock = null;
      ph.textContent = (cancelled ? "Đã dừng. " : "Xong! ") + ok + "/" + jobs.length + " video đã xuất."; if (!cancelled) bar.style.width = "100%";
      var miss = done.filter(function (x) { return !x.yt; });
      if (useYt && miss.length) { var rr2 = document.createElement("div"); rr2.innerHTML = '<button class="tv-b" data-dlg="ytrest">▶️ Đăng nốt ' + miss.length + " video lên YouTube</button>"; res.appendChild(rr2); }
      running = false; b2(false);
    }
    async function ytOne(item) {
      var sp = document.createElement("span"); sp.textContent = " · ▶️ đang đăng YouTube…"; item.row.appendChild(sp);
      try {
        var vf = item.files[0], cv = item.files.filter(function (f) { return f.kind === "cover"; })[0];
        var v = await YT.upload(vf.blob, ytMeta(item.w, item.V, item.o), function (p) { sp.textContent = " · ▶️ YouTube " + Math.round(p * 100) + "%"; });
        item.yt = v.id; sp.innerHTML = ' · ▶️ <a href="https://youtu.be/' + escH(v.id || "") + '" target="_blank" rel="noopener">youtu.be/' + escH(v.id || "") + "</a>";
        if (cv && v.id) { try { await YT.thumb(v.id, cv.blob); sp.innerHTML += " (ảnh thu nhỏ ✅)"; } catch (er) { sp.innerHTML += ' <span class="av-tip">(ảnh thu nhỏ: ' + escH(er.message) + ")</span>"; } }
      } catch (er) { sp.innerHTML = ' · <span style="color:#b23b34">▶️ YouTube lỗi: ' + escH(er && er.message || er) + "</span>"; }
    }
    async function ytRest(btn) {
      try { await YT.token(); } catch (er) { alert("⚠️ " + (er && er.message || er)); return; }
      btn.disabled = true; var miss = done.filter(function (x) { return !x.yt; });
      for (var i = 0; i < miss.length; i++) await ytOne(miss[i]);
      btn.closest("div").remove();
    }
    function b2(on) { $d('[data-dlg="start"]').classList.toggle("tv-hide", on); $d('[data-dlg="stop"]').classList.toggle("tv-hide", !on); d.querySelectorAll("[data-bi],[data-blang],[data-dlg=all],[data-dlg=none],[data-dlg=extras],[data-dlg=dl],[data-dlg=dir],[data-dlg=yt],[data-dlg=okall],[data-cok]").forEach(function (x) { x.disabled = on; }); }
    return d;
  }


  /* ---------------- 14. LƯU & ĐĂNG ----------------
     14a. Lưu thẳng vào một thư mục trên máy: File System Access API (Chrome/Edge máy tính). Thư mục chọn một lần,
          «chìa khoá» (handle) cất trong IndexedDB; mỗi phiên trình duyệt hỏi lại quyền ghi một lần. */
  var FSX = {
    ok: function () { return typeof global.showDirectoryPicker === "function"; },
    get: async function () { try { var h = await IDB.get("__dir"); return h && h.kind === "directory" ? h : null; } catch (e) { return null; } },
    pick: async function () { var h = await global.showDirectoryPicker({ id: "giai-ma-video", mode: "readwrite" }); await IDB.put("__dir", h); return h; },
    granted: async function (h) { try { return (await h.queryPermission({ mode: "readwrite" })) === "granted"; } catch (e) { return false; } },
    ensure: async function (h) { if (!h) return false; if (await FSX.granted(h)) return true; try { return (await h.requestPermission({ mode: "readwrite" })) === "granted"; } catch (e) { return false; } },
    write: async function (h, sub, name, blob) { var d = sub ? await h.getDirectoryHandle(sub, { create: true }) : h; var f = await d.getFileHandle(name, { create: true }); var wr = await f.createWritable(); await wr.write(blob); await wr.close(); }
  };
  /* 14b. YouTube: đăng nhập Google Identity Services (mô hình token, gọi từ cú bấm) + tải lên kiểu «resumable» theo mẫu chính thức
          youtube/api-samples/javascript/cors_upload.js (POST mở phiên → Location → PUT dữ liệu). Postiz (mã nguồn mở) dùng cùng cách
          và đặt ảnh thu nhỏ sau khi tải (thumbnails.set — kênh phải xác minh số điện thoại). */
  var YT = {
    tok: null, exp: 0, ch: "",
    cid: function () { return lsGet("av_yt_cid", "") || ""; },
    setCid: function (v) { lsSet("av_yt_cid", String(v || "").trim() || null); YT.tok = null; YT.ch = ""; },
    ready: function () { return !!(global.google && google.accounts && google.accounts.oauth2); },
    gis: function () { return YT.ready() ? Promise.resolve() : L.loadScript("https://accounts.google.com/gsi/client"); },
    has: function () { return !!(YT.tok && Date.now() < YT.exp - 90000); },
    token: function () {                                              // phải gọi trong lúc người dùng vừa bấm (để mở được cửa sổ đăng nhập)
      if (YT.has()) return Promise.resolve(YT.tok);
      if (!YT.cid()) return Promise.reject(new Error("Chưa có Client ID — bấm ⚙️ Cài đặt YouTube."));
      return YT.gis().then(function () {
        return new Promise(function (res, rej) {
          var tc = google.accounts.oauth2.initTokenClient({
            client_id: YT.cid(), scope: "https://www.googleapis.com/auth/youtube.upload https://www.googleapis.com/auth/youtube.readonly",
            callback: function (r) { if (r && r.access_token) { YT.tok = r.access_token; YT.exp = Date.now() + (+r.expires_in || 3600) * 1000; res(YT.tok); } else rej(new Error((r && (r.error_description || r.error)) || "Google không cấp quyền")); },
            error_callback: function (e) { rej(new Error(e && e.type === "popup_closed" ? "Cửa sổ đăng nhập Google đã bị đóng." : e && e.type === "popup_failed_to_open" ? "Trình duyệt chặn cửa sổ đăng nhập Google — cho phép cửa sổ bật lên rồi thử lại." : "Không đăng nhập được Google.")); }
          });
          tc.requestAccessToken({ prompt: "" });
        });
      });
    },
    channel: async function () {
      var r = await fetch("https://www.googleapis.com/youtube/v3/channels?part=snippet&mine=true", { headers: { Authorization: "Bearer " + YT.tok } });
      var j = await r.json(); var c = j && j.items && j.items[0]; YT.ch = c ? c.snippet.title : ""; return YT.ch;
    },
    upload: function (blob, meta, onProg) {
      return new Promise(function (res, rej) {
        var x = new XMLHttpRequest(); x.open("POST", "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status", true);
        x.setRequestHeader("Authorization", "Bearer " + YT.tok); x.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
        x.setRequestHeader("X-Upload-Content-Length", String(blob.size)); x.setRequestHeader("X-Upload-Content-Type", blob.type || "video/mp4");
        x.onload = function () { if (x.status >= 400) return rej(ytErr(x)); var loc = x.getResponseHeader("Location"); if (!loc) return rej(new Error("YouTube không trả về địa chỉ tải lên.")); put(loc); };
        x.onerror = function () { rej(new Error("Lỗi mạng khi bắt đầu tải lên YouTube.")); };
        x.send(JSON.stringify(meta));
        function put(loc) {
          var y = new XMLHttpRequest(); y.open("PUT", loc, true); y.setRequestHeader("Content-Type", blob.type || "video/mp4");
          if (y.upload) y.upload.onprogress = function (e) { if (e.lengthComputable && onProg) onProg(e.loaded / e.total); };
          y.onload = function () { if (y.status >= 200 && y.status < 300) { var v = {}; try { v = JSON.parse(y.responseText); } catch (er) { } res(v); } else rej(ytErr(y)); };
          y.onerror = function () { rej(new Error("Lỗi mạng khi tải video lên YouTube.")); };
          y.send(blob);
        }
      });
    },
    thumb: async function (id, jpg) {
      var r = await fetch("https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId=" + encodeURIComponent(id) + "&uploadType=media", { method: "POST", headers: { Authorization: "Bearer " + YT.tok, "Content-Type": "image/jpeg" }, body: jpg });
      if (!r.ok) { var t = ""; try { t = await r.text(); } catch (e) { } throw new Error(r.status === 403 ? "kênh chưa được đặt ảnh thu nhỏ riêng (cần xác minh số điện thoại kênh; với Shorts có thể chưa hỗ trợ)" : "lỗi " + r.status + (t ? ": " + t.slice(0, 120) : "")); }
      return true;
    }
  };
  function ytErr(x) {
    var m = ""; try { var j = JSON.parse(x.responseText); m = (j.error && (j.error.message || (j.error.errors && j.error.errors[0] && j.error.errors[0].reason))) || ""; } catch (e) { }
    if (x.status === 401) YT.tok = null;
    return new Error("YouTube báo lỗi " + x.status + (m ? ": " + m : "") + (x.status === 403 && /quota/i.test(m) ? " (đã hết hạn mức tải lên trong ngày)" : ""));
  }
  function ytTitle(w, V, O) {
    var l = V.lang || "vi"; if (l !== "vi") return TXL(l).yt(quoteT(w.title, l), V.steps.length).replace(/[<>]/g, "").slice(0, 100);
    var t = O && O.ytTitle && String(O.ytTitle).trim(); return (t || "Giải mã " + (/[«»"]/.test(w.title) ? w.title : "«" + w.title + "»") + (/:/.test(w.title) ? " — " : ": ") + V.steps.length + " chi tiết ít ai để ý").replace(/[<>]/g, "").slice(0, 100); }
  function ytMeta(w, V, O) {
    var desc = postText(w, V) + "\n\n" + chapters(V) + (V.H > V.W ? "\n\n#Shorts" : ""), seen = {};
    var tags = (desc.match(/#[\p{L}\p{N}_]+/gu) || []).map(function (x) { return x.slice(1); }).concat(["giải mã tác phẩm", w.title, w.titleVi || ""]).filter(Boolean).filter(function (x) { var k = x.toLowerCase(); if (seen[k]) return false; seen[k] = 1; return true; });
    var tl = 0; tags = tags.filter(function (x) { tl += x.length + 3; return tl < 480; });
    return { snippet: { title: ytTitle(w, V, O), description: desc.replace(/[<>]/g, "").slice(0, 4900), tags: tags, categoryId: "27", defaultLanguage: LINFO[V.lang || "vi"].yt, defaultAudioLanguage: LINFO[V.lang || "vi"].yt },
             status: { privacyStatus: O.ytPrivacy || "private", selfDeclaredMadeForKids: false, containsSyntheticMedia: !!(O.ai && O.voice === "ai") } };
  }
  // 14c. các tệp đi kèm một video
  async function bundleFiles(w, V, r, base) {
    var out = [{ name: base + "." + r.ext, blob: r.blob, kind: "video" }];
    try { var cb = await cover(V); if (cb) out.push({ name: base + "-anh-bia.jpg", blob: cb, kind: "cover" }); } catch (e) { }
    if (V.AP) out.push({ name: base + ".srt", blob: new Blob([L.makeSRT(V)], { type: "text/plain" }), kind: "srt" });
    out.push({ name: base + "-loi-dang.txt", blob: new Blob([postText(w, V) + "\n\n" + chapters(V)], { type: "text/plain" }), kind: "txt" });
    return out;
  }
  // 14d. đăng bán tự động: Facebook, TikTok, Instagram chỉ cho đăng thẳng qua máy chủ (API cần khoá bí mật, chặn gọi từ trình duyệt)
  // độ dài khi đăng tay qua web (10/2026): Facebook bỏ mức 90 giây cho Reels từ 6/2025 (chỉ API còn 3–90 giây);
  // Instagram Reels tới 3 phút; YouTube: video dọc/vuông từ 3 phút trở xuống mới thành Shorts
  var PUB = [
    { id: "fb", name: "📘 Facebook Reels", url: "https://www.facebook.com/reels/create" },
    { id: "tt", name: "🎵 TikTok", url: "https://www.tiktok.com/upload" },
    { id: "ig", name: "📷 Instagram", url: "https://www.instagram.com/", max: 180, warn: "Instagram có thể không nhận làm Reels, nên dùng bản ⚡ Ngắn" },
    { id: "yt", name: "▶️ YouTube Studio", url: "https://www.youtube.com/upload", max: 180, port: true, warn: "video dọc/vuông dài hơn 3 phút sẽ không được tính là Shorts" }
  ];
  async function copyText(t) { try { await navigator.clipboard.writeText(t); return true; } catch (e) { var ta = document.createElement("textarea"); ta.value = t; ta.style.cssText = "position:fixed;left:-9999px"; document.body.appendChild(ta); ta.select(); var ok = false; try { ok = document.execCommand("copy"); } catch (er) { } ta.remove(); return ok; } }

  /* ---------------- 9. studio ---------------- */
  function open(work0, opts) {
    opts = opts || {}; ensureCSS();
    var w0 = resolve(work0), w = w0, O = loadOpts(), I = [], V = null, NRc = null, AUD = { nk: null, AP: null, mk: null, mix: null }, player = L.AudioPlayer();
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
      '<div class="tv-f tv-sub"><b>🌐 Ngôn ngữ video</b><div class="tv-seg av-langs" data-k="vlang">' + LANGS.map(function (l) { return '<button data-val="' + l + '">' + LINFO[l].flag + " " + LINFO[l].name + "</button>"; }).join("") + "</div>" +
      '<div class="tv-note" data-v="trinfo"></div><div class="tv-row av-btns" data-v="trbtns"><button data-a="trai">🤖 Nhờ AI dịch / dịch lại</button><button data-a="trclear">↺ Dùng bản dịch có sẵn</button></div></div>' +
      '<div class="tv-f tv-sub"><b>💬 Câu mở đầu</b><div class="tv-chk">' + chk("trend", "Có câu mở đầu (chữ lớn + lời đọc)") + '</div>' +
      '<div class="tv-row av-op"><select data-v="opsel" title="Gợi ý câu mở đầu"></select><button class="tv-b" data-a="oprnd" title="Đổi sang một gợi ý khác">🎲 Gợi ý khác</button></div>' +
      '<input type="text" data-o="trendText"/><div class="tv-note">Chọn gợi ý hoặc tự gõ; để trống là câu trend «Giờ thì tôi mới hiểu…». Câu đã chọn được nhớ riêng cho tác phẩm này (và riêng từng ngôn ngữ). Viết {chữ hiện|cách đọc} để giọng AI đọc đúng số, ví dụ {10|ten}.</div></div>' +
      '<div class="tv-f tv-sub av-cov" data-v="covbox"><b>🖼️ Ảnh bìa <span class="av-covst" data-v="covst"></span></b>' +
      '<div class="tv-row"><button class="tv-b" data-a="covview">👁 Xem ảnh bìa</button><button class="tv-b gold" data-a="covok">✅ Chốt ảnh bìa</button></div>' +
      '<div class="av-g2"><label>Nền<select data-cv="bg"></select></label><label>Tâm điểm<select data-cv="focus"></select></label></div>' +
      '<div class="tv-row"><span>Phóng to</span><input type="range" min="100" max="300" step="5" data-cv="zoom"/></div>' +
      '<div class="tv-row av-btns"><span>Khung</span><button data-a="covfit" data-val="fill">Lấp đầy</button><button data-a="covfit" data-val="fit">Cả bức</button><span>Chữ</span><button data-a="covpos" data-val="top">Trên</button><button data-a="covpos" data-val="mid">Giữa</button><button data-a="covpos" data-val="bot">Dưới</button></div>' +
      '<input type="text" data-cv="l1" placeholder="Dòng nhỏ màu vàng (vd GIỜ THÌ TÔI MỚI HIỂU…)"/><input type="text" data-cv="l2" placeholder="Dòng lớn — {tên} là tên tác phẩm"/><input type="text" data-cv="l3" placeholder="Dòng phụ — {n} là số chi tiết"/>' +
      '<div class="tv-row"><span>Nền chữ tối</span><input type="range" min="0" max="90" step="5" data-cv="dim"/></div>' +
      '<div class="tv-row av-btns"><button data-a="covframe">📸 Lấy khung hình đang xem</button><button data-a="covup">📂 Ảnh bìa của anh</button><button data-a="covreset">↺ Mặc định</button></div>' +
      '<div class="tv-chk">' + chk("coverIntro", "Chèn ảnh bìa vào 0,8 giây đầu video (để YouTube, TikTok lấy đúng khung)") + "</div>" +
      '<div class="tv-note">Trong ô chữ: {tên} tự thay bằng tên tác phẩm, {n} bằng số chi tiết. Kéo trên khung xem thử để dịch ảnh, lăn chuột để phóng to. Mỗi khung dọc/ngang/vuông phải chốt ảnh bìa một lần trước khi xuất. Shorts đăng bằng điện thoại: chọn khung hình đầu làm ảnh thu nhỏ; trên máy tính có thể tải tệp «…-anh-bia.jpg» lên.</div></div>' +
      seg3("len", "Độ dài", [["short", "⚡ Ngắn (~1,5 phút · 4 chi tiết)"], ["full", "📖 Đầy đủ (3–4 phút)"]]) +
      seg3("aspect", "Khung hình", [["9:16", "▯ 9:16 dọc"], ["16:9", "▭ 16:9 ngang"], ["1:1", "◻ 1:1 vuông"]]) +
      seg3("res", "Độ nét", [[720, "720p"], [1080, "1080p (nét)"]]) +
      seg3("pace", "Nhịp máy quay", [["fast", "Nhanh"], ["mid", "Vừa"], ["slow", "Chậm"]]) +
      '<div class="tv-f tv-sub"><b>🎙️ Thuyết minh</b><div class="tv-seg" data-k="voice"><button data-val="ai">🤖 Giọng AI — có tiếng trong video</button><button data-val="off">🔇 Không đọc (chỉ chữ)</button></div>' +
      '<div class="tv-row av-op" data-show="ai"><select data-v="vsel" title="Giọng đọc cho ngôn ngữ đang chọn"></select><button class="tv-b" data-a="vtest">▶ Nghe thử giọng</button></div>' +
      '<div class="tv-seg" data-k="rate" data-show="ai"><button data-val="0.9">🐢 Chậm</button><button data-val="1">Vừa</button><button data-val="1.12">🐇 Nhanh</button></div><div class="tv-note" data-v="aiinfo"></div></div>' +
      '<div class="tv-f tv-sub"><b>🎵 Nhạc nền</b><div class="tv-seg" data-k="music">' + musicBtns + '</div>' +
      '<input type="file" accept="audio/*,.mp3,.m4a,.aac,.wav,.ogg,.opus,.flac" data-v="mfile" class="tv-hide"/>' +
      '<div class="tv-row"><span>Âm lượng</span><input type="range" min="0" max="100" step="5" data-o="musicVol"/><button class="tv-b" data-a="hearm">▶ Nghe thử</button></div><div class="tv-note" data-v="minfo"></div></div>' +
      '<div class="tv-f"><b>Hiện trên video</b><div class="tv-chk">' + chk("caps", "Phụ đề lời đọc") + chk("qcard", "Thẻ câu hỏi") + chk("spot", "Khung sáng chi tiết") + chk("nums", "Đánh số chi tiết") + chk("cta", "Câu hỏi gợi bình luận ở cuối") + chk("qr", "Mã QR cuối video") + chk("safe", "📱 Chừa chỗ nút bấm TikTok/Reels (khung dọc)") + "</div>" +
      seg3("capSize", "Cỡ chữ phụ đề", [["s", "Nhỏ"], ["m", "Vừa"], ["l", "Lớn"]]) + "</div>" +
      '<div class="tv-f tv-sub"><b>📚 Nguồn & minh bạch</b><div class="tv-chk">' + chk("srcStep", "Ghi nguồn dưới mỗi lời giải") + chk("imgCredit", "Tên tác giả ảnh ở mép ảnh") + chk("srcs", "Danh sách nguồn ở cuối video") + chk("ai", "🤖 Ghi rõ video có dùng AI") + "</div>" +
      '<div data-show-ai="1">' + seg3("aiPos", "Lời nhắc «có thể còn sai sót»", [["start", "Đầu video"], ["end", "Cuối video"], ["both", "Cả hai"]]) +
      '<div class="tv-chk">' + chk("aiBadge", "Nhãn nhỏ «🤖 Có dùng AI» suốt video") + chk("aiSay", "Đọc lời nhắc ở cuối video") + "</div>" +
      '<textarea data-o="aiText" rows="3" class="av-ta" placeholder="' + escH(AI_TEXT) + '"></textarea><div class="tv-note">Để trống là dùng lời nhắc mặc định (chữ mờ trong ô). Khi đăng, nên bật thêm mục khai báo nội dung AI có sẵn của nền tảng.</div></div></div>' +
      '<div class="tv-f"><b>Chữ ký</b><input type="text" data-o="credit"/></div>' +
      '<div class="tv-f" data-show-qr="1"><b>Mã QR dẫn tới</b><input type="text" data-o="qrUrl" placeholder="https://fb.com/lopmaybay"/></div>' +
      '<div class="tv-lbl" data-v="est"></div>' +
      '<div class="tv-f tv-sub"><b>📤 Lưu & đăng sau khi xuất</b><div class="tv-chk">' + chk("autoDl", "⬇️ Tự tải về máy: video + ảnh bìa + phụ đề + lời đăng") + "</div>" +
      '<div class="tv-row" data-v="fsrow"><button class="tv-b" data-a="pickdir">📁 Lưu thẳng vào thư mục…</button><span class="tv-lbl" data-v="dirname"></span><button class="tv-b tv-hide" data-a="nodir" title="Thôi lưu vào thư mục này">✕</button></div>' +
      '<div class="tv-chk">' + chk("ytAuto", "▶️ Tự đăng lên YouTube") + "</div>" +
      '<div data-show-yt="1"><div class="tv-row av-btns"><span>Chế độ</span><button data-a="ytpriv" data-val="private">🔒 Riêng tư</button><button data-a="ytpriv" data-val="unlisted">🔗 Không công khai</button><button data-a="ytpriv" data-val="public">🌐 Công khai</button></div>' +
      '<input type="text" data-o="ytTitle" placeholder="Tiêu đề YouTube (để trống: Giải mã «tên»: n chi tiết ít ai để ý)"/>' +
      '<div class="tv-row"><button class="tv-b" data-a="ytconn">🔑 Kết nối YouTube</button><span class="tv-lbl" data-v="ytst"></span><button class="tv-b" data-a="ytset">⚙️ Cài đặt</button></div></div>' +
      '<div class="tv-note">Facebook, TikTok, Instagram chỉ cho đăng thẳng qua máy chủ riêng, nên sau khi xuất sẽ có nút cho từng mạng: lời đăng được chép sẵn, trang đăng mở ra, anh kéo tệp video vào.</div></div>' +
      '<div class="tv-go"><button class="tv-b navy" data-a="export">⬇️ Xuất video MP4</button><button class="tv-b" data-a="post">📋 Chữ đăng bài + hashtag</button></div>' +
      '<div class="tv-note">Ảnh: Wikimedia Commons (phạm vi công cộng / giấy phép mở, tên tác giả ảnh hiện ở cuối video) hoặc ảnh của anh. Giọng AI chạy ngay trên máy: Piper (VAIS-1000 CC BY 4.0, Denis CC0, LJSpeech, Chaowen CC0) hoặc Supertonic 3 (10 giọng, OpenRAIL-M — phải ghi rõ có dùng AI). Nhạc dựng sẵn do trình duyệt tự tổng hợp. Video không trích lời bài hát.</div>' +
      "</div></div>" +
      '<div class="tv-main tv-hide" data-v="editor"></div></div>';
    document.body.appendChild(ov);
    var $ = function (s) { return ov.querySelector(s); }, canvas = $("canvas"), ctx = canvas.getContext("2d", { alpha: false });
    $('[data-o="credit"]').value = O.credit || ""; $('[data-o="qrUrl"]').value = O.qrUrl || ""; $('[data-o="musicVol"]').value = Math.round((+O.musicVol || 0) * 100); $('[data-o="aiText"]').value = O.aiText || "";
    var trendInp = $('[data-o="trendText"]'); trendInp.value = lsGet(openKeyOf(w0.id, O.vlang), "") || "";
    var CV = coverLoad(w, O), coverMode = false, dirH = null, cvSaveT = 0;
    $('[data-o="ytTitle"]').value = O.ytTitle || "";
    FSX.get().then(function (h) { dirH = h; syncPub(); });
    function syncCover() {
      var C = CV.C, okA = !!CV.ok[O.aspect];
      var st = $('[data-v="covst"]'); st.textContent = okA ? "✅ đã chốt (" + O.aspect + ")" : "⚠️ chưa chốt (" + O.aspect + ")"; st.className = "av-covst " + (okA ? "ok" : "no");
      var bg = $('[data-cv="bg"]'), html = "";
      w.img.forEach(function (d, k) { if (I[k] && I[k].ok) html += '<option value="img:' + k + '"' + (C.src === "img" && C.k === k ? " selected" : "") + ">Ảnh " + (k + 1) + " · " + escH(String(d.file || "ảnh của anh").replace(/\.[a-z]+$/i, "").slice(0, 40)) + "</option>"; });
      if (I.coverEl) html += '<option value="user"' + (C.src === "user" ? " selected" : "") + ">📂 Ảnh bìa của anh</option>";
      html += '<option value="frame"' + (C.src === "frame" ? " selected" : "") + ">📸 Khung hình lúc " + fmtClock(+C.t || 0) + "</option>";
      bg.innerHTML = html;
      var fo = $('[data-cv="focus"]'), fh = '<option value="-1">Cả bức</option>';
      (w.steps || []).forEach(function (s2, j) { if (!s2.card && s2.b && (s2.i || 0) === C.k) fh += '<option value="' + j + '"' + (C.focus === j ? " selected" : "") + ">Chi tiết " + (j + 1) + " · " + escH(String(s2.tag || "").slice(0, 34)) + "</option>"; });
      fo.innerHTML = fh; fo.disabled = C.src !== "img";
      $('[data-cv="zoom"]').value = Math.round((+C.zoom || 1) * 100); $('[data-cv="dim"]').value = Math.round((C.dim == null ? 0.55 : +C.dim) * 100);
      var CLn = coverLines(C, O.vlang, O); ["l1", "l2", "l3"].forEach(function (k) { var el = $('[data-cv="' + k + '"]'); if (document.activeElement !== el) el.value = CLn[k] || ""; });
      ov.querySelectorAll('[data-a="covfit"]').forEach(function (b) { b.classList.toggle("on", (C.fit || "fill") === b.dataset.val); });
      ov.querySelectorAll('[data-a="covpos"]').forEach(function (b) { b.classList.toggle("on", (C.pos || "mid") === b.dataset.val); });
      $('[data-a="covview"]').textContent = coverMode ? "🎬 Về xem video" : "👁 Xem ảnh bìa";
    }
    function coverChanged(redrawOnly) {
      coverMode = true; clearTimeout(cvSaveT);
      cvSaveT = setTimeout(function () { CV.ok = coverSave(w, CV.C); syncCover(); }, redrawOnly ? 350 : 0);
      if (!redrawOnly) { CV.ok = coverSave(w, CV.C); syncCover(); }
      frame();
    }
    function syncPub() {
      $('[data-v="fsrow"]').classList.toggle("tv-hide", !FSX.ok());
      $('[data-v="dirname"]').textContent = dirH ? "📁 " + dirH.name : "";
      $('[data-a="nodir"]').classList.toggle("tv-hide", !dirH);
      ov.querySelectorAll("[data-show-yt]").forEach(function (el) { el.classList.toggle("tv-hide", !O.ytAuto); });
      ov.querySelectorAll('[data-a="ytpriv"]').forEach(function (b) { b.classList.toggle("on", (O.ytPrivacy || "private") === b.dataset.val); });
      $('[data-v="ytst"]').textContent = YT.has() ? "✅ " + (YT.ch || "đã kết nối") : YT.cid() ? "chưa kết nối" : "chưa cài đặt — bấm ⚙️";
      if (O.ytAuto && YT.cid()) YT.gis().catch(function () { });
    }
    function saveOpener() { lsSet(openKeyOf(w0.id, O.vlang), trendInp.value.trim() ? trendInp.value.trim() : null); }
    function fillOpeners() {
      var sel = $('[data-v="opsel"]'), list = openerList(w, effO()), cur = trendInp.value.trim(), g = "", html = '<option value="">— ' + ((O.vlang || "vi") === "vi" ? "Câu trend «Giờ thì tôi mới hiểu…»" : "Câu trend (" + LINFO[O.vlang].name + ")") + " —</option>";
      list.forEach(function (o, i) { if (o.g !== g) { if (g) html += "</optgroup>"; html += '<optgroup label="' + escH(o.g) + '">'; g = o.g; } var lb = disp(o.t); html += '<option value="' + i + '"' + (o.t === cur ? " selected" : "") + ">" + escH(lb.length > 92 ? lb.slice(0, 90) + "…" : lb) + "</option>"; });
      if (g) html += "</optgroup>";
      if (cur && !list.some(function (o) { return o.t === cur; })) html += '<option value="custom" selected>✏️ Câu anh tự gõ</option>';
      sel.innerHTML = html; sel._list = list; sel.disabled = !O.trend;
    }
    function curTrend(o) { return (O.vlang || "vi") === "vi" ? trendLine(w, o) : trendLineX(w, o, O.vlang); }
    function narrKey() { var tr = (O.vlang || "vi") !== "vi" ? lsGet(trKey(O.vlang, w0.id), null) : null; return JSON.stringify([w.id, O.vlang || "vi", AIV.voiceFor(O.vlang || "vi", O), tr && tr.at || 0, w.edited ? JSON.stringify(w.steps).length + (w.hook || "").length : 0, O.len, O.voice, O.rate, O.trend, curTrend(effO()), O.qr && O.qrUrl ? 1 : 0, O.ai && O.aiSay ? (O.aiText || 1) : 0]); }
    function mixKey(Vx) { return narrKey() + "|" + musicFor(w, O) + "|" + O.musicVol + "|" + userMusicName + "|" + Vx.total.toFixed(3); }
    function syncUI() {
      $('[data-v="title"]').textContent = w.title + (w.titleVi && w.titleVi !== w.title ? " · " + w.titleVi : "");
      ov.querySelectorAll(".tv-seg").forEach(function (sg) { var k = sg.dataset.k; sg.querySelectorAll("button").forEach(function (b) { b.classList.toggle("on", String(O[k]) === b.dataset.val); }); });
      ov.querySelectorAll("[data-c]").forEach(function (c) { c.checked = !!O[c.dataset.c]; });
      ov.querySelectorAll("[data-show]").forEach(function (el) { el.classList.toggle("tv-hide", el.dataset.show.split(" ").indexOf(O.voice) < 0); });
      ov.querySelectorAll("[data-show-qr]").forEach(function (el) { el.classList.toggle("tv-hide", !O.qr); });
      trendInp.placeholder = disp(curTrend(Object.assign({}, O, { trendText: "" }))); trendInp.disabled = !O.trend; fillOpeners();
      ov.querySelectorAll("[data-show-ai]").forEach(function (el) { el.classList.toggle("tv-hide", !O.ai); });
      CV.ok = coverLoad(w, O).ok; syncCover(); syncPub();
      $('[data-a="export"]').textContent = "⬇️ Xuất video MP4 " + (O.voice === "ai" ? (O.music !== "off" ? "(lời đọc + nhạc)" : "(có lời đọc)") : O.music !== "off" ? "(chỉ có nhạc)" : "(không tiếng)");
      var mu = musicFor(w, O); $('[data-v="minfo"]').textContent = O.music === "file" ? (userMusicName ? "🎵 " + userMusicName : "Chọn một tệp nhạc trên máy (MP3, M4A, WAV…)") : O.music === "off" ? "" : (O.music === "auto" ? "Tự chọn: " + (MUSIC.PRE[mu] ? MUSIC.PRE[mu].name : mu) + " · " : "") + "Nhạc tự nhỏ lại khi có lời đọc.";
      aiInfo(); audLabel(); trInfo(); fillVoices();
    }
    function trInfo() {
      var l = O.vlang || "vi", el = $('[data-v="trinfo"]'), bt = $('[data-v="trbtns"]');
      bt.classList.toggle("tv-hide", l === "vi");
      if (l === "vi") { el.innerHTML = "Video tiếng Việt — kịch bản gốc."; return; }
      var st = trStatus(w0, l), nm = LINFO[l].name;
      $('[data-a="trclear"]').classList.toggle("tv-hide", !st.mine);
      el.innerHTML = st.none ? '<b style="color:#b23b34">⚠️ Tác phẩm này chưa có bản dịch ' + escH(nm) + "</b> — bấm 🤖 Nhờ AI dịch (dán kết quả JSON vào là xong)."
        : st.miss ? "⚠️ " + st.miss + " chi tiết chưa có bản dịch (anh đã sửa kịch bản tiếng Việt) — các chi tiết này sẽ được đọc bằng tiếng Việt. Bấm 🤖 để dịch lại cả bài."
        : "✅ Bản dịch " + escH(nm) + (st.mine ? " của anh (nhờ AI dịch)." : " có sẵn (Claude dịch, đã kiểm tra tên riêng và cách đọc số).") + " Tên tác phẩm gốc tiếng Việt vẫn hiện trên video. Nên nhờ người biết tiếng xem lại trước khi đăng." +
          (st.stale ? " ⚠️ " + st.stale + " chi tiết anh đã sửa tiếng Việt sau khi dịch — nếu đã đổi ý thì bấm 🤖 để dịch lại." : "");
    }
    function voiceLabel(v) { var d = AIV.VOICES[v]; if (!d) return v; if (d.eng === "st") return "🌟 Supertonic · " + (d.g === "nữ" ? "Nữ " : "Nam ") + d.style.slice(1) + " (" + d.style + ")"; return "🎙️ Piper · " + d.name + (d.g ? " (" + d.g + ")" : "") + " · " + d.lic; }
    function fillVoices() {
      var sel = $('[data-v="vsel"]'), l = O.vlang || "vi", cur = AIV.voiceFor(l, O);
      sel.innerHTML = AIV.voicesFor(l).map(function (v) { return '<option value="' + v + '"' + (v === cur ? " selected" : "") + ">" + escH(voiceLabel(v)) + "</option>"; }).join("");
    }
    async function setLang(l) {
      if (LANGS.indexOf(l) < 0) l = "vi";
      O.vlang = l; saveOpts(O);
      if (l !== "vi") { $('[data-v="scene"]').textContent = "⏳ Đang tải bản dịch " + LINFO[l].name + "…"; await ensureLang(l); }
      w = localize(w0, l); AUD.nk = null; AUD.mk = null; player.set(null);
      trendInp.value = lsGet(openKeyOf(w0.id, l), "") || "";
      syncUI(); rebuild();
    }
    function openTrAI() {
      var l = O.vlang || "vi"; if (l === "vi") return;
      var d = dialog(ov, "🤖 Nhờ AI dịch sang " + escH(LINFO[l].name),
        '<div class="av-tip"><b>Cách dùng:</b> bấm <b>📋 Chép lệnh</b>, dán vào Claude hoặc ChatGPT, rồi dán khối JSON trả về vào ô dưới và bấm <b>📥 Lưu bản dịch</b>. Bản dịch lưu trên máy này và được ưu tiên hơn bản có sẵn. Hãy đọc lại tên riêng và nhờ người biết tiếng xem giúp trước khi đăng.</div>' +
        '<div class="tv-go" style="flex-direction:row;flex-wrap:wrap"><button class="tv-b navy" data-dlg="copy">📋 Chép lệnh</button><button class="tv-b" data-dlg="show">👁 Xem lệnh</button><button class="tv-b" data-dlg="cur">📤 Chép bản dịch đang dùng (để sửa tay)</button></div>' +
        '<textarea class="av-post tv-hide" data-dlg="prompt" readonly></textarea>' +
        '<label>Dán JSON bản dịch vào đây<textarea class="av-post" data-dlg="json" placeholder="{ &quot;title&quot;: …, &quot;steps&quot;: [ … ] }"></textarea></label>' +
        '<div class="tv-go" style="flex-direction:row;flex-wrap:wrap"><button class="tv-b navy" data-dlg="imp">📥 Lưu bản dịch</button></div><div class="av-tip" data-dlg="rep"></div>');
      d.addEventListener("click", async function (e) {
        var b2 = e.target.closest("[data-dlg]"); if (!b2) return; var k = b2.dataset.dlg, ta = d.querySelector('[data-dlg="prompt"]'), rep2 = d.querySelector('[data-dlg="rep"]');
        if (k === "copy") { var txt = trPrompt(w0, l); ta.value = txt; if (await copyText(txt)) b2.textContent = "✅ Đã chép — dán vào Claude/ChatGPT"; else { ta.classList.remove("tv-hide"); ta.select(); } }
        else if (k === "show") { ta.value = trPrompt(w0, l); ta.classList.toggle("tv-hide"); }
        else if (k === "cur") { var cur = trOf(w0, l); var tx = JSON.stringify(cur ? Object.assign({}, cur, { _mine: undefined }) : {}, null, 1); d.querySelector('[data-dlg="json"]').value = tx; await copyText(tx); b2.textContent = "✅ Đã chép và dán vào ô dưới"; }
        else if (k === "imp") {
          try { var r2 = applyTr(w0, l, parseAIJSON(d.querySelector('[data-dlg="json"]').value)); w = localize(w0, l); AUD.nk = null; AUD.mk = null; player.set(null); syncUI(); rebuild(); rep2.style.color = "#1d6b43"; rep2.textContent = "✅ Đã lưu bản dịch (" + r2.n + " chi tiết)."; }
          catch (er) { rep2.style.color = "#b23b34"; rep2.textContent = "⚠️ " + (er && er.message || er); }
        }
      });
    }
    async function voiceTest(btn) {
      var o = effO(), l = o.vlang || "vi", T = TXL(l), NRs = { s: [{ c: T.sample, segs: [{ l: l, t: l === "vi" ? T.sample : speakX(T.sample, l) }] }] };
      var ap = await withProgress(function (u2, isC) { return AIV.synthNarration(NRs, o, u2, isC); }); if (!ap) return;
      var cl = ap.scenes.s && ap.scenes.s.clips[0]; if (!cl) return;
      try { var AC = global.AudioContext || global.webkitAudioContext, ac = new AC(), buf = ac.createBuffer(1, cl.pcm.length, cl.sr); buf.getChannelData(0).set(cl.pcm); var sn = ac.createBufferSource(); sn.buffer = buf; sn.connect(ac.destination); sn.start(); sn.onended = function () { try { ac.close(); } catch (e) { } }; } catch (e) { }
      aiInfo();
    }
    async function aiInfo() {
      var el = $('[data-v="aiinfo"]'); if (O.voice !== "ai") { el.textContent = ""; return; }
      if (!AIV.supported()) { el.textContent = "⚠️ Trình duyệt này chưa chạy được giọng AI — hãy dùng Chrome hoặc Edge bản mới."; return; }
      var info = {}; try { info = await AIV.storageInfo(); } catch (e) { }
      var l = O.vlang || "vi", vid = AIV.voiceFor(l, O), vd = AIV.VOICES[vid]; if (!vd) { el.textContent = "⚠️ Chưa có giọng AI cho " + LINFO[l].name + "."; return; }
      var st = vd.eng === "st", has = !!info[vid], ei = AIV.engineInfo ? AIV.engineInfo() : {};
      el.textContent = "Giọng " + LINFO[l].name + ": " + (st ? "Supertonic 3 · " + (vd.g === "nữ" ? "nữ " : "nam ") + vd.style.slice(1) : "Piper · " + vd.name + (vd.g ? " (" + vd.g + ")" : "")) + " — giấy phép " + vd.lic + ". " + (has ? "✅ Đã có sẵn trên máy." : "Lần đầu cần tải khoảng " + (vd.mb + (st ? 0 : 30)) + " MB (lưu lại, lần sau dùng ngay).") +
        (st ? " Supertonic chạy nhanh hơn nhiều trên máy có WebGPU (Chrome/Edge bản mới)" + (ei.st ? " — đang dùng " + ei.st.toUpperCase() : "") + "." : "") + (l === "zh" ? " Giọng Trung đọc qua phiên âm pinyin." : "");
    }
    function audLabel() {
      var need = O.voice === "ai" || O.music !== "off", ok = player.has();
      $('[data-a="build"]').classList.toggle("tv-hide", !need || ok);
      $('[data-v="aud"]').textContent = !need ? "🔇 Video không tiếng" : ok ? (O.voice === "ai" ? "🔊 Xem thử có tiếng (lời đọc" + (O.music !== "off" ? " + nhạc" : "") + ")" : "🎵 Xem thử có nhạc nền") : "Xem thử đang không tiếng — bấm 🔊 Dựng tiếng để nghe " + (O.voice === "ai" ? "lời đọc" + (O.music !== "off" ? " + nhạc" : "") : "nhạc nền");
    }
    function effO() { var o = {}; for (var k in O) o[k] = O[k]; o.music = musicFor(w, O); o.trendText = trendInp.value; o.coverC = CV.C; return o; }
    function rebuild() {
      var o = effO(), d = L.dims(o); canvas.width = d.W; canvas.height = d.H;
      var steps = pickSteps(w, o), NR = narrate(w, o, steps), ap = (o.voice === "ai" && AUD.nk === narrKey()) ? AUD.AP : null;
      var wasPlaying = playing && player.playing(); player.stop();
      V = build(w, o, d.W, d.H, NR, ap, I); NRc = NR; t = Math.min(t, V.total - 0.01);
      player.set(AUD.mix && AUD.mk === mixKey(V) ? AUD.mix : null);
      if (wasPlaying && player.has()) player.play(t);
      $('[data-v="est"]').textContent = "⏱ Thời lượng ~" + fmtClock(V.total) + " · " + V.steps.length + " chi tiết · " + d.W + "×" + d.H + (ap ? "" : (o.voice === "ai" ? " (ước lượng — sẽ khớp đúng sau khi dựng tiếng)" : ""));
      dirty = true; audLabel(); imgNote(); if (!playing) frame();      // vẽ lại ngay (đổi khung hình làm trắng canvas)
    }
    function imgNote() {
      var el = $('[data-v="imgnote"]'), miss = w.img.map(function (d, k) { return (!I[k] || !I[k].ok) ? k : -1; }).filter(function (k) { return k >= 0; });
      if (!miss.length) { el.innerHTML = w.rights === "copyright" ? "⚠️ " + escH(w.rightsNote || "Tác phẩm còn bản quyền — cân nhắc khi đăng tải.") : ""; return; }
      el.innerHTML = "📷 " + (w.img[miss[0]] && w.img[miss[0]].user ? "Tác phẩm này còn bản quyền nên không kèm ảnh. " : "Chưa tải được ảnh. ") + '<button class="tv-b" data-a="upimg" data-k="' + miss[0] + '">📂 Nạp ảnh của anh</button> ' + escH((w.img[miss[0]] || {}).note || "");
    }
    function frame() { if (!V) return; if (coverMode) { renderCover(ctx, V, CV.C, true); dirty = false; $('[data-v="scene"]').textContent = "🖼️ Ảnh bìa — khung xanh là phần hay bị cắt khi hiện ô vuông"; return; } renderArt(ctx, V, t); dirty = false; $('[data-a="seek"]').value = Math.round(t / V.total * 1000); $('[data-v="time"]').textContent = fmtClock(t) + " / " + fmtClock(V.total); var sc = V.scenes[sceneAt(V, t)]; $('[data-v="scene"]').textContent = sc.type === "q" || sc.type === "a" ? "Chi tiết " + sc.num + "/" + sc.of + ": " + (sc.st.tag || "") : ({ trend: "Câu mở đầu", hook: "Mở đầu", info: "Giới thiệu", end: "Lời kết", outro: "Nguồn & mã QR" })[sc.type] || ""; }
    function loop(ts) {
      if (!playing) return;
      var dt = last ? (ts - last) / 1000 : 0; last = ts;
      if (player.playing()) t = player.time(); else t += dt;
      if (t >= V.total) { t = V.total - 0.001; setPlay(false); }
      frame(); raf = requestAnimationFrame(loop);
    }
    function setPlay(on) { if (on) { coverMode = false; syncCover(); } playing = on; $('[data-a="play"]').textContent = on ? "⏸ Dừng" : "▶ Xem thử"; cancelAnimationFrame(raf); if (on) { if (t >= V.total - 0.05 || atPoster) t = 0; atPoster = false; last = 0; if (player.has()) player.play(t); raf = requestAnimationFrame(loop); } else { player.stop(); frame(); } }
    function seekScene(dir) { atPoster = false; coverMode = false; syncCover(); var idx = V.scenes.map(function (s) { return s.type === "q" || s.type === "end" || s.type === "trend" || s.type === "hook" ? s.t0 : -1; }).filter(function (x) { return x >= 0; }); var cur = t + 0.05, nt = dir > 0 ? idx.filter(function (x) { return x > cur; })[0] : idx.filter(function (x) { return x < cur - 0.6; }).pop(); if (nt == null) nt = dir > 0 ? V.total - 0.01 : 0; t = nt + 0.01; if (playing && player.has()) player.play(t); frame(); }
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
    // xuất: phải chốt ảnh bìa; xin quyền YouTube / thư mục ngay lúc bấm (trình duyệt chỉ cho mở cửa sổ đăng nhập khi người dùng vừa bấm)
    async function startExport() {
      if (busy) return;
      if ((O.vlang || "vi") !== "vi" && w.trMissing < 0) { alert("Tác phẩm này chưa có bản dịch " + LINFO[O.vlang].name + ". Bấm 🤖 Nhờ AI dịch (mục 🌐 Ngôn ngữ video) hoặc chọn lại tiếng Việt."); return; }
      CV.ok = coverLoad(w, O).ok; if (!CV.ok[O.aspect]) { coverGate(); return; }
      var pre = {};
      if (O.ytAuto && YT.cid()) { try { await YT.token(); pre.yt = true; YT.channel().then(syncPub).catch(function () { }); } catch (er) { pre.ytErr = er && er.message || String(er); } }
      if (dirH) { pre.dirOk = await FSX.ensure(dirH); if (pre.dirOk) pre.dir = dirH; }
      doExport(pre);
    }
    function coverGate() {
      var d0 = L.dims(effO()), sc0 = Math.min(1, 560 / Math.max(d0.W, d0.H)), c = document.createElement("canvas"); c.width = d0.W; c.height = d0.H;
      renderCover(c.getContext("2d"), V, CV.C);
      var dlg = dialog(ov, "🖼️ Chốt ảnh bìa trước khi xuất",
        '<div class="av-gate"><div class="av-gate-img"></div><div class="av-gate-tx"><p><b>Đây là ảnh bìa của video (khung ' + escH(O.aspect) + ').</b> Ảnh được ' + (O.coverIntro !== false ? "chèn vào 0,8 giây đầu video và " : "") + "lưu thành tệp «…-anh-bia.jpg» để tải lên làm ảnh thu nhỏ.</p>" +
        "<p>Hãy xem kỹ: ảnh có đẹp và dễ chịu không (tránh cận mặt tượng, ma-nơ-canh), chữ có đọc rõ không?</p>" +
        '<div class="tv-go" style="flex-direction:row;flex-wrap:wrap"><button class="tv-b gold" data-dlg="ok">✅ Chốt & xuất video</button><button class="tv-b" data-dlg="edit">✏️ Sửa ảnh bìa</button></div></div></div>');
      c.style.cssText = "width:" + Math.round(d0.W * sc0) + "px;max-width:100%;height:auto;border-radius:10px;display:block;box-shadow:0 6px 20px rgba(0,0,0,.3)";
      dlg.querySelector(".av-gate-img").appendChild(c);
      dlg.addEventListener("click", function (e) {
        var b2 = e.target.closest("[data-dlg]"); if (!b2) return;
        if (b2.dataset.dlg === "ok") { CV.ok = coverSave(w, CV.C, O.aspect); dlg.remove(); syncCover(); startExport(); }
        else if (b2.dataset.dlg === "edit") { dlg.remove(); coverMode = true; setPlay(false); syncCover(); frame(); var cb = $('[data-v="covbox"]'); if (cb) cb.scrollIntoView({ behavior: "smooth", block: "start" }); }
      });
    }
    async function doExport(pre) {
      pre = pre || {};
      var res = $('[data-v="res"]'); res.style.display = "none";
      var out = await withProgress(async function (u2, isC) {
        await ensureBrand();
        var b = (O.voice === "ai" || O.music !== "off") ? await buildAudio(u2, isC) : { V: V, mix: null };
        if (O.qr && O.qrUrl) { await L.ensureQR(); L.qrCanvas(O.qrUrl); }
        var x = await L.exportVideo(b.V, { phase: u2.phase, onCancel: function (fn) { cancelFn = fn; } }, b.mix);
        return { r: x, V: b.V };
      });
      if (!out) return; rebuild();
      var r = out.r, Vx = out.V, url = URL.createObjectURL(r.blob), base = L.slug(w0.title) + "-" + O.aspect.replace(":", "x") + (O.len === "short" ? "-ngan" : "") + ((O.vlang || "vi") !== "vi" ? "-" + O.vlang : ""), name = base + "." + r.ext, mb = (r.blob.size / 1048576).toFixed(1);
      res.style.display = "block";
      res.innerHTML = "<b>✅ Xong: " + escH(name) + " · " + mb + " MB · " + fmtClock(Vx.total) + (r.audio ? (O.voice === "ai" ? " · 🔊 có lời đọc" + (O.music !== "off" ? " + nhạc" : "") : " · 🎵 có nhạc nền") : " · 🔇 không tiếng") + "</b>" +
        (r.noAudioCodec ? '<div class="tv-note" style="color:#b23b34">⚠️ Trình duyệt này không mã hoá được âm thanh — hãy dùng Chrome hoặc Edge bản mới.</div>' : "") +
        '<video controls playsinline src="' + url + '"></video><div class="tv-go" style="flex-direction:row;flex-wrap:wrap">' +
        '<a class="tv-b gold" href="' + url + '" download="' + escH(name) + '">⬇️ Tải video về máy</a>' +
        (Vx.AP ? '<button class="tv-b" data-a="srt">💬 Phụ đề .srt</button>' : "") + '<button class="tv-b" data-a="chap">📑 Mục lục YouTube</button><button class="tv-b" data-a="cov">🖼️ Ảnh bìa JPG</button></div>' +
        '<div class="av-pub"><b>📤 Lưu & đăng</b><div class="av-pubst" data-v="pubst"></div>' +
        '<div class="tv-go" style="flex-direction:row;flex-wrap:wrap"><button class="tv-b navy" data-a="ytup">▶️ Đăng YouTube ngay</button>' + PUB.map(function (p) { return '<button class="tv-b" data-a="pub" data-p="' + p.id + '">' + p.name + " ↗</button>"; }).join("") +
        (navigator.canShare ? '<button class="tv-b" data-a="share">📲 Chia sẻ (điện thoại)</button>' : "") + "</div>" +
        '<div class="tv-note">Bấm nút một mạng: lời đăng được chép sẵn và trang đăng mở ở thẻ mới — kéo tệp video vào, chọn ảnh bìa (tệp «…-anh-bia.jpg» hoặc khung hình đầu), dán lời đăng và bật mục khai báo nội dung AI.' +
        (Vx.total > 180 && Vx.H >= Vx.W ? " ⚠️ Video dài " + fmtClock(Vx.total) + ": YouTube sẽ không tính là Shorts, Instagram có thể không nhận làm Reels — nên dùng bản ⚡ Ngắn." : "") + "</div></div>" +
        '<div class="tv-note">Mã hoá: ' + escH(r.codec || "") + "</div>";
      res._blob = r.blob; res._name = name; res._V = Vx; res._base = base;
      afterExport(res, Vx, r, base, pre);
    }
    function pubLine(res, html) { var st = res.querySelector('[data-v="pubst"]'), d = document.createElement("div"); d.innerHTML = html; if (st) st.appendChild(d); return d; }
    async function filesOf(res) { if (!res._files) res._files = await bundleFiles(w, res._V, { blob: res._blob, ext: res._name.split(".").pop() }, res._base); return res._files; }
    async function afterExport(res, Vx, r, base, pre) {
      var files = await filesOf(res);
      if (O.autoDl) { files.forEach(function (f, i) { setTimeout(function () { L.dl(f.blob, f.name); }, i * 450); }); res._dl = true; pubLine(res, "⬇️ Đã tự tải " + files.length + " tệp (video, ảnh bìa, " + (Vx.AP ? "phụ đề, " : "") + "lời đăng) về thư mục Tải về."); }
      if (pre.dir) await saveFiles(res, pre.dir);
      else if (dirH) pubLine(res, '📁 <button class="av-mini" data-a="savedir">Lưu vào thư mục «' + escH(dirH.name) + '»</button> <span class="av-tip">(trình duyệt cần anh bấm để cho phép ghi)</span>');
      if (O.ytAuto) { if (pre.yt) ytRun(res); else pubLine(res, "▶️ Chưa đăng YouTube: " + escH(pre.ytErr || "chưa kết nối") + ' — <button class="av-mini" data-a="ytup">Đăng ngay</button>'); }
    }
    async function saveFiles(res, h) {
      var files = await filesOf(res), sub = L.slug(w0.title), row = pubLine(res, "💾 Đang lưu vào thư mục…");
      try { for (var i = 0; i < files.length; i++) await FSX.write(h, sub, files[i].name, files[i].blob); row.innerHTML = "💾 Đã lưu " + files.length + " tệp vào «" + escH(h.name + "/" + sub) + "»."; }
      catch (er) { row.innerHTML = "⚠️ Không lưu được vào thư mục: " + escH(er && er.message || er); }
    }
    async function saveToDir(btn) { var res = $('[data-v="res"]'); if (!dirH) return; if (await FSX.ensure(dirH)) { btn.closest("div").remove(); saveFiles(res, dirH); } }
    async function ytRun(res) {
      var files = await filesOf(res), vid = files[0], cov = files.filter(function (f) { return f.kind === "cover"; })[0], Vx = res._V;
      var row = pubLine(res, "▶️ YouTube: đang tải lên 0%…"), pl = { private: "riêng tư", unlisted: "không công khai", public: "công khai" }[O.ytPrivacy || "private"];
      try {
        var v = await YT.upload(vid.blob, ytMeta(w, Vx, O), function (p) { row.textContent = "▶️ YouTube: đang tải lên " + Math.round(p * 100) + "%…"; });
        var url = "https://youtu.be/" + (v.id || ""); res._yt = v.id;
        row.innerHTML = "▶️ YouTube: ✅ đã đăng (" + pl + ") — <a href=\"" + escH(url) + "\" target=\"_blank\" rel=\"noopener\">" + escH(url) + "</a>";
        if (cov && v.id) { try { await YT.thumb(v.id, cov.blob); row.innerHTML += " · ảnh thu nhỏ ✅"; } catch (er) { row.innerHTML += " · <span class=\"av-tip\">ảnh thu nhỏ chưa đặt được: " + escH(er.message) + "</span>"; } }
      } catch (er) { row.innerHTML = "▶️ YouTube: ⚠️ " + escH(er && er.message || er) + ' — <button class="av-mini" data-a="ytup">Thử lại</button>'; }
    }
    async function ytUploadNow(btn) {
      var res = $('[data-v="res"]'); if (!res._blob) return;
      if (res._yt && !confirm("Video này đã đăng lên YouTube rồi. Đăng thêm một bản nữa?")) return;
      if (!YT.cid()) { ytSettings(); return; }
      try { await YT.token(); YT.channel().then(syncPub).catch(function () { }); } catch (er) { alert("⚠️ " + (er && er.message || er)); return; }
      if (btn && btn.classList.contains("av-mini")) btn.closest("div").remove();
      ytRun(res);
    }
    async function pubTo(id) {
      var res = $('[data-v="res"]'), p = PUB.filter(function (x) { return x.id === id; })[0]; if (!p || !res._V) return;
      var cap = postText(w, res._V); await copyText(id === "yt" ? ytTitle(w, res._V, O) + "\n\n" + cap : cap);
      if (!res._dl && !res._savedDl) { var files = await filesOf(res); files.filter(function (f) { return f.kind === "video" || f.kind === "cover"; }).forEach(function (f, i) { setTimeout(function () { L.dl(f.blob, f.name); }, i * 450); }); res._savedDl = true; }
      global.open(p.url, "_blank", "noopener");
      var Vp = res._V, long = p.max && Vp.total > p.max && (!p.port || Vp.H >= Vp.W);
      pubLine(res, "📋 Đã chép lời đăng cho " + escH(p.name) + " và mở trang đăng — kéo tệp «" + escH(res._name) + "» vào, dán lời đăng (Ctrl+V)." + (long ? " ⚠️ Video dài " + fmtClock(Vp.total) + ": " + escH(p.warn) + "." : ""));
    }
    function ytSettings() {
      var fileProto = location.protocol === "file:", origin = location.origin;
      var d = dialog(ov, "⚙️ Cài đặt tự đăng YouTube",
        '<div class="av-tip">Làm một lần, khoảng 10 phút. Trang chỉ giữ <b>Client ID</b> trên trình duyệt này — không cần mật khẩu, không gửi đi đâu khác ngoài Google.</div>' +
        (fileProto ? '<div class="av-tip" style="color:#b23b34">⚠️ Trang đang mở từ tệp trên máy (file://). Google chỉ cho đăng nhập từ một địa chỉ web — hãy mở trang qua GitHub Pages của anh hoặc một máy chủ nội bộ (http://localhost:…).</div>' : "") +
        '<ol class="av-steps"><li>Mở <a href="https://console.cloud.google.com/projectcreate" target="_blank" rel="noopener">Google Cloud Console</a>, tạo một dự án (ví dụ «Giai ma video»).</li>' +
        '<li>Mở <a href="https://console.cloud.google.com/apis/library/youtube.googleapis.com" target="_blank" rel="noopener">YouTube Data API v3</a> → bấm <b>Bật (Enable)</b>.</li>' +
        '<li>Mở <a href="https://console.cloud.google.com/apis/credentials/consent" target="_blank" rel="noopener">Màn hình xin phép OAuth</a>: chọn <b>Bên ngoài (External)</b>, điền tên ứng dụng và email; ở mục <b>Người dùng thử nghiệm (Test users)</b> thêm Gmail sở hữu kênh YouTube.</li>' +
        '<li>Mở <a href="https://console.cloud.google.com/apis/credentials" target="_blank" rel="noopener">Thông tin xác thực</a> → <b>Tạo → ID ứng dụng khách OAuth</b> → loại <b>Ứng dụng web</b> → mục <b>Nguồn gốc JavaScript được phép</b> thêm <code>' + escH(fileProto ? "https://<địa chỉ trang của anh>" : origin) + "</code> → Tạo.</li>" +
        "<li>Chép <b>Client ID</b> (dạng …apps.googleusercontent.com), dán vào ô dưới, bấm <b>Lưu & kết nối</b>.</li></ol>" +
        '<label>Client ID<input type="text" data-dlg="cid" value="' + escH(YT.cid()) + '" placeholder="1234567890-abc….apps.googleusercontent.com"/></label>' +
        '<div class="tv-go" style="flex-direction:row;flex-wrap:wrap"><button class="tv-b navy" data-dlg="conn">🔑 Lưu & kết nối</button><button class="tv-b" data-dlg="save">💾 Chỉ lưu</button><button class="tv-b" data-dlg="clear">Xoá Client ID</button></div>' +
        '<div class="av-tip">Ghi chú: mỗi dự án tải được khoảng 100 video/ngày; muốn đặt ảnh thu nhỏ riêng, kênh phải xác minh số điện thoại (youtube.com/verify). Video dùng giọng AI sẽ được đánh dấu «nội dung tổng hợp» nếu bật 🤖 ghi rõ có dùng AI.</div><div class="av-tip" data-dlg="msg"></div>');
      d.addEventListener("click", async function (e) {
        var b2 = e.target.closest("[data-dlg]"); if (!b2) return; var k = b2.dataset.dlg, msg = d.querySelector('[data-dlg="msg"]'), cid = d.querySelector('[data-dlg="cid"]').value.trim();
        if (k === "save" || k === "conn") {
          if (cid && !/\.apps\.googleusercontent\.com$/.test(cid)) { msg.style.color = "#b23b34"; msg.textContent = "⚠️ Client ID phải kết thúc bằng .apps.googleusercontent.com"; return; }
          YT.setCid(cid); syncPub(); msg.style.color = "#1d6b43"; msg.textContent = "✅ Đã lưu.";
          if (k === "conn") { try { await YT.token(); var ch = await YT.channel(); msg.textContent = "✅ Đã kết nối kênh «" + (ch || "?") + "»."; if (!O.ytAuto) { O.ytAuto = true; saveOpts(O); syncUI(); } } catch (er) { msg.style.color = "#b23b34"; msg.textContent = "⚠️ " + (er && er.message || er); } syncPub(); }
        } else if (k === "clear") { YT.setCid(""); d.querySelector('[data-dlg="cid"]').value = ""; syncPub(); msg.textContent = "Đã xoá."; }
      });
    }
    function showPost() {
      var res = $('[data-v="res"]'); res.style.display = "block";
      res.innerHTML = "<b>📋 Chữ đăng bài (Facebook, TikTok, YouTube)</b><textarea class=\"av-post\" readonly>" + escH(postText(w, V)) + '</textarea><div class="tv-go" style="flex-direction:row"><button class="tv-b" data-a="copypost">📋 Chép</button></div>' +
        (O.voice === "ai" || O.ai ? '<div class="tv-note">🤖 Khi đăng: video dùng giọng đọc AI — nên bật thêm mục khai báo «nội dung tạo bằng AI» có sẵn của TikTok, YouTube, Facebook (ở bước đăng bài).</div>' : "");
    }
    // ---------------- sự kiện ----------------
    ov.addEventListener("click", async function (e) {
      var b = e.target.closest("button, a"); if (!b || !ov.contains(b)) return;
      var a = b.dataset.a, sg = b.closest(".tv-seg");
      if (sg && b.dataset.val != null) {
        if (sg.dataset.k === "vlang") { if (!busy) setLang(b.dataset.val); return; }
        var k = sg.dataset.k, val = b.dataset.val; O[k] = (k === "res") ? +val : (k === "rate" ? +val : val);
        if (k === "music" && val === "file" && !userMusic) $('[data-v="mfile"]').click();
        saveOpts(O); syncUI(); rebuild(); return;
      }
      if (a === "close") close();
      else if (a === "play") setPlay(!playing);
      else if (a === "next") seekScene(1); else if (a === "prev") seekScene(-1);
      else if (a === "build") doBuild();
      else if (a === "export") startExport();
      else if (a === "post") showPost();
      else if (a === "cancel") { if (cancelFn) cancelFn(); }
      else if (a === "edit") toggleEditor(!editMode);
      else if (a === "upimg") pickImage(+b.dataset.k || 0);
      else if (a === "copypost") { var ta = ov.querySelector(".av-post"); try { await navigator.clipboard.writeText(ta.value); b.textContent = "✅ Đã chép"; } catch (er) { ta.select(); document.execCommand("copy"); b.textContent = "✅ Đã chép"; } }
      else if (a === "hearm") hearMusic(b);
      else if (a === "covview") { coverMode = !coverMode; if (coverMode) setPlay(false); syncCover(); frame(); }
      else if (a === "covok") { CV.ok = coverSave(w, CV.C, O.aspect); coverMode = true; syncCover(); frame(); }
      else if (a === "covfit") { CV.C.fit = b.dataset.val; coverChanged(); }
      else if (a === "covpos") { CV.C.pos = b.dataset.val; coverChanged(); }
      else if (a === "covframe") { var c0 = V.scenes[0] && V.scenes[0].type === "cover" ? V.scenes[0].dur : 0; CV.C.src = "frame"; CV.C.t = Math.max(t, c0 + 0.3); coverChanged(); }
      else if (a === "covreset") { var keepTx = CV.C.tx; CV.C = coverDefaults(w0, O); if (keepTx && (O.vlang || "vi") !== "vi") { delete keepTx[O.vlang]; CV.C.tx = keepTx; } rebuild(); coverChanged(); }
      else if (a === "trai") openTrAI();
      else if (a === "trclear") { if (confirm("Bỏ bản dịch của anh, dùng lại bản dịch có sẵn?")) { lsSet(trKey(O.vlang, w0.id), null); w = localize(w0, O.vlang); AUD.nk = null; syncUI(); rebuild(); } }
      else if (a === "vtest") voiceTest(b);
      else if (a === "covup") {
        var ci = document.createElement("input"); ci.type = "file"; ci.accept = "image/*";
        ci.onchange = async function () { var f = ci.files && ci.files[0]; if (!f) return; await setUserImage(w.id, "cover", f); I = await loadWorkImages(w); CV.C.src = "user"; CV.C.px = 0.5; CV.C.py = 0.5; CV.C.zoom = 1; rebuild(); coverChanged(); };
        ci.click();
      }
      else if (a === "pickdir") { try { dirH = await FSX.pick(); syncPub(); } catch (er) { } }
      else if (a === "nodir") { await IDB.del("__dir"); dirH = null; syncPub(); }
      else if (a === "ytpriv") { O.ytPrivacy = b.dataset.val; saveOpts(O); syncPub(); }
      else if (a === "ytset") ytSettings();
      else if (a === "ytconn") { try { await YT.token(); await YT.channel(); } catch (er) { alert("⚠️ " + (er && er.message || er)); } syncPub(); }
      else if (a === "pub") pubTo(b.dataset.p);
      else if (a === "ytup") ytUploadNow(b);
      else if (a === "savedir") saveToDir(b);
      else if (a === "oprnd") {
        var ol = openerList(w, effO()), cur = trendInp.value.trim(), cands = ol.filter(function (o) { return o.t !== cur; });
        if (cands.length) { trendInp.value = cands[Math.floor(Math.random() * cands.length)].t; saveOpener(); if (!O.trend) { O.trend = true; saveOpts(O); } syncUI(); rebuild(); }
      }
      else if (a === "srt" || a === "chap" || a === "cov" || a === "share") {
        var res = $('[data-v="res"]'), Vx = res._V || V;
        if (a === "srt") L.dl(new Blob([L.makeSRT(Vx)], { type: "text/plain" }), res._base + ".srt");
        else if (a === "chap") { var tx = document.createElement("textarea"); tx.value = chapters(Vx); tx.readOnly = true; tx.style.cssText = "width:100%;min-height:120px;margin-top:8px"; res.appendChild(tx); }
        else if (a === "cov") { var cb = await cover(Vx); L.dl(cb, res._base + "-anh-bia.jpg"); }
        else if (a === "share") { var cap = postText(w, Vx); await copyText(cap); try { await navigator.share({ files: [new File([res._blob], res._name, { type: res._blob.type })], title: w.title, text: cap }); } catch (er) { } }
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
      if (el.dataset.a === "seek") { atPoster = false; if (coverMode) { coverMode = false; syncCover(); } t = (+el.value / 1000) * V.total; if (playing && player.has()) player.play(t); frame(); return; }
      if (el.dataset.cv === "l1" || el.dataset.cv === "l2" || el.dataset.cv === "l3") {
        var lc = O.vlang || "vi";
        if (lc === "vi") CV.C[el.dataset.cv] = el.value; else { CV.C.tx = CV.C.tx || {}; CV.C.tx[lc] = CV.C.tx[lc] || clone(coverLines(CV.C, lc, O)); CV.C.tx[lc][el.dataset.cv] = el.value; }
        coverChanged(true); return;
      }
      if (el.dataset.cv === "zoom") { CV.C.zoom = clamp(+el.value / 100, 1, 4); coverChanged(true); return; }
      if (el.dataset.cv === "dim") { CV.C.dim = clamp(+el.value / 100, 0, 0.9); coverChanged(true); return; }
      if (el.dataset.o === "musicVol") { O.musicVol = (+el.value) / 100; saveOpts(O); clearTimeout(el._t); el._t = setTimeout(rebuild, 300); return; }
      if (el.dataset.o === "trendText") { saveOpener(); clearTimeout(el._t); el._t = setTimeout(function () { fillOpeners(); rebuild(); }, 400); return; }
      if (el.dataset.o) { O[el.dataset.o] = el.value; saveOpts(O); clearTimeout(el._t); el._t = setTimeout(rebuild, 350); }
    });
    ov.addEventListener("change", async function (e) {
      var el = e.target;
      if (el.dataset.c) { O[el.dataset.c] = el.checked; saveOpts(O); syncUI(); rebuild(); }
      if (el.dataset.cv === "bg") { var bv = el.value; if (bv === "frame") { CV.C.src = "frame"; } else if (bv === "user") { CV.C.src = "user"; } else { CV.C.src = "img"; CV.C.k = +bv.split(":")[1] || 0; CV.C.focus = -1; } CV.C.px = 0.5; CV.C.py = 0.5; CV.C.zoom = 1; coverChanged(); return; }
      if (el.dataset.cv === "focus") { CV.C.focus = +el.value; CV.C.px = 0.5; CV.C.py = 0.5; CV.C.zoom = 1; coverChanged(); return; }
      if (el.dataset.v === "vsel") { O.voices = Object.assign({}, O.voices || {}); O.voices[O.vlang || "vi"] = el.value; saveOpts(O); AUD.nk = null; AUD.mk = null; player.set(null); aiInfo(); rebuild(); return; }
      if (el.dataset.v === "opsel") { var oi = el.value; if (oi !== "custom") trendInp.value = oi === "" ? "" : ((el._list || [])[+oi] || {}).t || ""; saveOpener(); syncUI(); rebuild(); }
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
      document.removeEventListener("keydown", onKey); ov.remove(); if (opts.onClose) try { opts.onClose(w0); } catch (e) { }
    }
    function onKey(e) { var dl = ov.querySelector(".av-dlg"); if (e.key === "Escape" && dl) { dl.remove(); return; } if (e.key === "Escape" && !busy) { if (editMode) toggleEditor(false); else close(); } else if (e.key === " " && !editMode && document.activeElement && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) { e.preventDefault(); setPlay(!playing); } }
    document.addEventListener("keydown", onKey);

    /* ---------- hộp thoại: tìm ảnh Commons · nhờ AI soạn kịch bản ---------- */
    function openCommons() {
      var d = dialog(ov, "🔎 Tìm ảnh trên Wikimedia Commons",
        '<div class="tv-row"><input type="text" data-dlg="q" value="' + escH(w.title) + '" placeholder="Tên tác phẩm, tác giả, nơi lưu giữ…"/><button class="tv-b navy" data-dlg="go">Tìm</button></div>' +
        '<div class="av-tip">Ảnh trên Commons có giấy phép mở; tác giả ảnh và giấy phép được tự điền để ghi công trong video. Nên mở «Trang ảnh» kiểm tra lại trước khi đăng. Gõ tiếng Anh thường ra nhiều ảnh hơn.</div><div class="av-cms" data-dlg="res"></div>');
      var res = d.querySelector('[data-dlg="res"]'), qi = d.querySelector('[data-dlg="q"]'), found = [];
      async function go() {
        res.innerHTML = '<div class="av-tip">⏳ Đang tìm…</div>';
        try {
          found = await commonsSearch(qi.value.trim() || w.title);
          res.innerHTML = found.length ? found.map(function (x, i) {
            return '<div class="av-cm"><img loading="lazy" src="' + escH(x.thumb) + '" alt=""/><div class="av-cm-t">' + escH(x.file) + '</div><div class="av-tip">' + escH(([x.lic, x.by].filter(Boolean).join(" · ") || "chưa rõ giấy phép").slice(0, 100)) + " · " + x.w + "×" + x.h + "</div>" +
              '<div class="av-cm-b"><button class="av-mini" data-dlg="use" data-i="' + i + '">✔ Dùng cho ảnh ' + (ED.k + 1) + '</button><button class="av-mini" data-dlg="add" data-i="' + i + '">➕ Thêm ảnh mới</button><a class="av-mini" href="' + escH(x.page) + '" target="_blank" rel="noopener">Trang ảnh ↗</a></div></div>';
          }).join("") : '<div class="av-tip">Không thấy ảnh phù hợp — thử từ khoá khác.</div>';
        } catch (er) { res.innerHTML = '<div class="av-tip" style="color:#b23b34">⚠️ Không tìm được: ' + escH(er && er.message || er) + "</div>"; }
      }
      d.addEventListener("click", async function (e) {
        var b = e.target.closest("[data-dlg]"); if (!b) return; var k = b.dataset.dlg;
        if (k === "go") go();
        else if (k === "use" || k === "add") {
          var x = found[+b.dataset.i]; if (!x) return; b.textContent = "…";
          var slot = k === "use" ? ED.k : w.img.length;
          w.img[slot] = { file: x.file, w: x.w, h: x.h, lic: x.lic || "xem trang ảnh", by: (x.by || "Wikimedia Commons").slice(0, 90) };
          await setUserImage(w.id, slot, null); ED.k = slot; ED.mode = "box"; persist(); I = await loadWorkImages(w); d.remove(); renderEditor();
        }
      });
      qi.addEventListener("keydown", function (e) { if (e.key === "Enter") go(); });
      go();
    }
    function openAI() {
      var n0 = Math.min(10, Math.max(5, (w.steps || []).length || 8));
      var d = dialog(ov, "🤖 Nhờ AI soạn kịch bản",
        '<div class="av-tip"><b>Cách dùng:</b> 1) điền thông tin → 2) bấm <b>📋 Chép lệnh</b>, dán vào Claude hoặc ChatGPT (nên đính kèm ảnh tác phẩm để AI ước lượng khung chi tiết) → 3) dán kết quả vào ô dưới, bấm <b>📥 Nhập</b>. AI có thể sai: hãy đọc lại từng lời giải và mở thử các đường dẫn nguồn trước khi đăng.</div>' +
        '<div class="av-grid2"><label>Tên tác phẩm<input type="text" data-dlg="t" value="' + escH(w.title) + '"/></label><label>Tác giả, năm<input type="text" data-dlg="by" value="' + escH([w.artist, w.date].filter(Boolean).join(", ")) + '"/></label>' +
        '<label>Số chi tiết<select data-dlg="n">' + [5, 6, 7, 8, 9, 10].map(function (x) { return "<option" + (x === n0 ? " selected" : "") + ">" + x + "</option>"; }).join("") + "</select></label>" +
        '<label class="av-inl"><input type="checkbox" data-dlg="img" checked/> Tôi sẽ đính kèm ảnh tác phẩm</label></div>' +
        '<label>Ghi chú thêm cho AI (tuỳ chọn)<textarea data-dlg="notes" rows="2" placeholder="Ví dụ: nơi lưu giữ, chi tiết muốn nói, nguồn nên dùng…"></textarea></label>' +
        '<div class="tv-go" style="flex-direction:row;flex-wrap:wrap"><button class="tv-b navy" data-dlg="copy">📋 Chép lệnh</button><button class="tv-b" data-dlg="show">👁 Xem lệnh</button></div>' +
        '<textarea class="av-post tv-hide" data-dlg="prompt" readonly></textarea>' +
        '<label>Dán kết quả JSON của AI vào đây<textarea class="av-post" data-dlg="json" placeholder="{ &quot;hook&quot;: …, &quot;steps&quot;: [ … ], &quot;sources&quot;: [ … ] }"></textarea></label>' +
        '<div class="tv-go" style="flex-direction:row;flex-wrap:wrap"><button class="tv-b navy" data-dlg="imp">📥 Nhập vào tác phẩm</button></div><div class="av-tip" data-dlg="rep"></div>');
      function v(k) { var el = d.querySelector('[data-dlg="' + k + '"]'); return el ? (el.type === "checkbox" ? el.checked : el.value) : ""; }
      function prompt() { return aiPrompt(w, { title: v("t"), by: v("by"), n: +v("n") || 8, img: v("img"), notes: String(v("notes")).trim() }); }
      d.addEventListener("click", async function (e) {
        var b = e.target.closest("[data-dlg]"); if (!b) return; var k = b.dataset.dlg, rep = d.querySelector('[data-dlg="rep"]');
        if (k === "copy") { var txt = prompt(), ta = d.querySelector('[data-dlg="prompt"]'); ta.value = txt; try { await navigator.clipboard.writeText(txt); b.textContent = "✅ Đã chép — dán vào Claude/ChatGPT"; } catch (er) { ta.classList.remove("tv-hide"); ta.select(); document.execCommand("copy"); b.textContent = "✅ Đã chép"; } }
        else if (k === "show") { var t2 = d.querySelector('[data-dlg="prompt"]'); t2.value = prompt(); t2.classList.toggle("tv-hide"); }
        else if (k === "imp") {
          try {
            var o = parseAIJSON(v("json"));
            if ((w.steps || []).length && !confirm("Thay kịch bản hiện tại (" + w.steps.length + " chi tiết) bằng kết quả của AI?")) return;
            var r = applyAI(w, o); persist(); ED.sel = -1; renderEditor();
            rep.style.color = "#1d6b43";
            rep.innerHTML = "✅ Đã nhập " + r.n + " chi tiết (" + r.k + " cho bản ngắn), " + r.src + " nguồn." + (r.nobox ? "<br>⚠️ " + r.nobox + " chi tiết chưa có khung — chọn từng chi tiết rồi kéo chuột trên ảnh để vẽ." : "") +
              (r.nosrc ? "<br>⚠️ " + r.nosrc + " lời giải chưa gắn nguồn." : "") + (r.nourl ? "<br>⚠️ " + r.nourl + " nguồn chưa có đường dẫn — hãy bổ sung hoặc kiểm tra lại." : "") + "<br>Hãy đọc lại toàn bộ trước khi dựng video.";
          } catch (er) { rep.style.color = "#b23b34"; rep.textContent = "⚠️ " + (er && er.message || er); }
        }
      });
    }

    /* ---------- trình chỉnh chi tiết ---------- */
    var ED = { k: 0, sel: -1, mode: "box" };
    function toggleEditor(on) {
      editMode = on; setPlay(false);
      if (on) w = w0; else { w0 = w; w = localize(w0, O.vlang || "vi"); }
      $('[data-v="main"]').classList.toggle("tv-hide", on); $('[data-v="editor"]').classList.toggle("tv-hide", !on);
      $('[data-a="edit"]').textContent = on ? "🎬 Về video" : "✏️ Chỉnh chi tiết";
      if (on) renderEditor(); else { syncUI(); rebuild(); frame(); }
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
        '<div class="av-imgs">' + imgBtns + '<button data-ed="addimg">➕ Thêm ảnh</button><button data-ed="upimg">📂 Thay bằng ảnh của anh</button>' + (m && m.src === "user" ? '<button data-ed="rmimg">↩︎ Bỏ ảnh của anh</button>' : "") + '<button data-ed="commons">🔎 Tìm ảnh Commons</button><button data-ed="crop" class="' + (ED.mode === "crop" ? "on" : "") + '">✂️ Khung tranh</button></div>' +
        '<div class="av-stage" data-ed="stage">' + (m && m.ok ? '<img draggable="false" src="' + escH(m.el.src) + '"/>' : '<div class="av-tip" style="color:#fff;padding:30px">Chưa có ảnh — bấm 📂 để nạp ảnh của anh.</div>') + '</div>' +
        '<div class="av-tip">👉 Chọn một chi tiết bên phải rồi <b>kéo chuột trên ảnh</b> để vẽ lại khung của nó. ' + (ED.mode === "crop" ? "<b>Đang chỉnh khung tranh:</b> kéo để chọn phần tác phẩm (bỏ viền, khung gỗ)." : "") + ' Các thay đổi được lưu ngay trên máy này.</div>' +
        '<div class="av-meta"><b>Lời mở đầu (hook)</b><textarea data-f="hook" rows="2">' + escH(w.hook || "") + '</textarea><b>Giới thiệu</b><textarea data-f="intro" rows="2">' + escH(w.intro || "") + '</textarea><b>Lời kết</b><textarea data-f="end" rows="2">' + escH(w.end || "") + "</textarea>" +
        '<b>💬 Gợi ý câu mở đầu <span class="av-tip">(mỗi dòng một câu)</span></b><textarea data-f="openers" rows="3">' + escH((w.openers || []).join("\n")) + "</textarea>" +
        '<b>📚 Nguồn tư liệu <span class="av-tip">(tick số nguồn ở từng chi tiết bên phải)</span></b><div class="av-srcs">' + (w.sources || []).map(function (r, i) {
          return '<div class="av-src" data-si="' + i + '"><span class="av-sn">' + (i + 1) + '</span><input type="text" data-sx="s" placeholder="Tên ngắn" value="' + escH(r.s || "") + '"/><input type="text" data-sx="t" placeholder="Nơi đăng — tên bài" value="' + escH(r.t || "") + '"/><input type="text" data-sx="u" placeholder="https://…" value="' + escH(r.u || "") + '"/><button class="av-mini" data-ed="srcdel" title="Xoá nguồn">🗑️</button></div>';
        }).join("") + '</div><div><button class="av-mini" data-ed="srcadd">➕ Thêm nguồn</button></div>' +
        (w.custom ? '<b>Tên tác phẩm</b><input type="text" data-f="title" value="' + escH(w.title) + '"/><b>Tác giả</b><input type="text" data-f="artist" value="' + escH(w.artist || "") + '"/><b>Năm / thời kỳ</b><input type="text" data-f="date" value="' + escH(w.date || "") + '"/><b>Nơi lưu giữ</b><input type="text" data-f="where" value="' + escH(w.where || "") + '"/><b>Thể loại</b><select data-f="type">' + DB().types.map(function (t) { return '<option value="' + t.id + '"' + (t.id === w.type ? " selected" : "") + ">" + t.icon + " " + t.vi + "</option>"; }).join("") + "</select>" : "") +
        '</div><div class="tv-go" style="flex-direction:row;flex-wrap:wrap"><button class="tv-b navy" data-ed="ai">🤖 Nhờ AI soạn kịch bản</button><button class="tv-b" data-ed="export">⬇️ Xuất kịch bản JSON</button><button class="tv-b" data-ed="import">📥 Nhập JSON</button>' + (w.custom ? '<button class="tv-b" data-ed="delwork">🗑️ Xoá tác phẩm này</button>' : '<button class="tv-b" data-ed="reset">↩︎ Khôi phục bản gốc</button>') + "</div></div>" +
        '<div><div class="av-list">' + steps.map(function (s, j) {
          return '<div class="av-st' + (j === ED.sel ? " on" : "") + '" data-j="' + j + '"><div class="hd"><span>' + (j + 1) + ". " + escH(s.tag || "Chi tiết") + (s.card ? " · thẻ chữ" : " · ảnh " + ((s.i || 0) + 1)) + (s.nobox ? ' <span style="color:#b23b34">⚠️ chưa có khung</span>' : "") + '</span><label class="av-tip"><input type="checkbox" data-sf="k"' + (s.k ? " checked" : "") + '/> bản ngắn</label>' +
            '<button class="av-mini" data-ed="up">↑</button><button class="av-mini" data-ed="down">↓</button><button class="av-mini" data-ed="del">🗑️</button></div>' +
            '<input type="text" data-sf="tag" placeholder="Nhãn ngắn (vd 🐱 Mèo = quyền thế)" value="' + escH(s.tag || "") + '"/>' +
            '<textarea data-sf="q" rows="2" placeholder="Câu hỏi">' + escH(s.q || "") + '</textarea><textarea data-sf="a" rows="3" placeholder="Lời giải">' + escH(s.a || "") + '</textarea>' +
            '<textarea data-sf="s" rows="2" placeholder="Lời giải ngắn cho bản ~1 phút (tuỳ chọn)">' + escH(s.s || "") + "</textarea>" +
            ((w.sources || []).length ? '<div class="av-chips"><span class="av-tip">📚 Nguồn:</span>' + w.sources.map(function (r, i) { return '<label class="av-chip"><input type="checkbox" data-srcj="' + i + '"' + ((s.src || []).indexOf(i) >= 0 ? " checked" : "") + "/>" + (i + 1) + ". " + escH(srcLabel(r) || "nguồn " + (i + 1)) + "</label>"; }).join("") + "</div>" : "") +
            (s.card ? '<input type="text" data-sf="cardbig" placeholder="Chữ lớn trên thẻ" value="' + escH(s.card.big || "") + '"/><input type="text" data-sf="cardsub" placeholder="Dòng phụ" value="' + escH(s.card.sub || "") + '"/>' : "") + "</div>";
        }).join("") + '</div><div class="tv-go" style="flex-direction:row;flex-wrap:wrap"><button class="tv-b navy" data-ed="add">➕ Thêm chi tiết (vẽ khung)</button><button class="tv-b" data-ed="addcard">🔤 Thêm thẻ chữ</button></div>' +
        '<div class="av-tip">Mẹo viết: câu hỏi ngắn gợi tò mò («Bạn có để ý…?», «Vì sao…?»), lời giải 2–3 câu, câu đầu là đáp án. Đánh dấu «bản ngắn» cho 4 chi tiết hay nhất. Tick nguồn cho từng lời giải để video ghi «Nguồn: …».</div></div></div>';
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
      var s = w.steps[ED.sel]; if (!s) return; s.i = ED.k; delete s.card; delete s.nobox;
      s.b = [(r[0] - m.x0) / m.cw, (r[1] - m.y0) / m.ch, r[2] / m.cw, r[3] / m.ch].map(function (v) { return +clamp(v, -0.2, 1.2).toFixed(4); });
      persist(); renderEditor();
    });
    function flash(msg) { var tip = ov.querySelector('[data-v="editor"] .av-tip'); if (tip) { tip.innerHTML = "⚠️ " + escH(msg); tip.style.color = "#b23b34"; } }
    ov.addEventListener("click", async function (e) {
      if (!editMode) return; var b = e.target.closest("[data-ed]"), card = e.target.closest(".av-st");
      if (card && (!b || b.dataset.ed === undefined) && !e.target.closest("textarea,input,label,select,a")) { ED.sel = +card.dataset.j; var s0 = w.steps[ED.sel]; if (s0 && !s0.card) ED.k = s0.i || 0; renderEditor(); return; }
      if (!b) return; var a = b.dataset.ed, j = card ? +card.dataset.j : -1;
      if (a === "img") { ED.k = +b.dataset.k; ED.mode = "box"; renderEditor(); }
      else if (a === "srcadd") { w.sources = (w.sources || []).concat([{ t: "", u: "", s: "" }]); persist(); renderEditor(); }
      else if (a === "srcdel") { var si = +b.closest(".av-src").dataset.si; w.sources.splice(si, 1); w.steps.forEach(function (st) { if (st.src) { st.src = st.src.filter(function (x) { return x !== si; }).map(function (x) { return x > si ? x - 1 : x; }); if (!st.src.length) delete st.src; } }); persist(); renderEditor(); }
      else if (a === "commons") openCommons();
      else if (a === "ai") openAI();
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
      if (el.dataset.f === "openers") { w.openers = el.value.split("\n").map(function (x) { return x.trim(); }).filter(Boolean); clearTimeout(el._t); el._t = setTimeout(persist, 400); return; }
      if (el.dataset.sx) { var sr = w.sources[+el.closest(".av-src").dataset.si]; if (sr) { sr[el.dataset.sx] = el.value; clearTimeout(el._t); el._t = setTimeout(persist, 400); } return; }
      if (el.dataset.f) { w[el.dataset.f] = el.value; clearTimeout(el._t); el._t = setTimeout(persist, 400); return; }
      if (card && el.dataset.sf) {
        var s = w.steps[+card.dataset.j]; if (!s) return; var f = el.dataset.sf;
        if (f === "k") s.k = el.checked ? 1 : 0; else if (f === "cardbig") s.card = Object.assign(s.card || {}, { big: el.value }); else if (f === "cardsub") s.card = Object.assign(s.card || {}, { sub: el.value });
        else s[f] = el.value;
        clearTimeout(el._t); el._t = setTimeout(persist, 400);
      }
    });
    ov.addEventListener("change", function (e) { if (!editMode) return; var el = e.target; if (el.dataset.f === "type") { w.type = el.value; persist(); }
      if (el.dataset.srcj != null) { var cd = el.closest(".av-st"), stp = cd && w.steps[+cd.dataset.j], si = +el.dataset.srcj; if (stp) { var arr = (stp.src || []).filter(function (x) { return x !== si; }); if (el.checked) arr.push(si); arr.sort(function (x, y) { return x - y; }); if (arr.length) stp.src = arr; else delete stp.src; persist(); } } if (el.dataset.sf === "k") { var card = el.closest(".av-st"), s = w.steps[+card.dataset.j]; s.k = el.checked ? 1 : 0; persist(); } });
    global.addEventListener("resize", function () { if (editMode) drawBoxes(); });
    var cdrag = null;
    canvas.addEventListener("pointerdown", function (e) { if (!coverMode || CV.C.src === "frame") return; cdrag = { x: e.clientX, y: e.clientY, px: CV.C.px == null ? 0.5 : CV.C.px, py: CV.C.py == null ? 0.5 : CV.C.py }; try { canvas.setPointerCapture(e.pointerId); } catch (er) { } e.preventDefault(); });
    canvas.addEventListener("pointermove", function (e) {
      if (!cdrag) return; var cv = coverView(V, CV.C); if (!cv) return; var r = canvas.getBoundingClientRect(), sc2 = canvas.width / Math.max(1, r.width);
      CV.C.px = clamp(cdrag.px - (e.clientX - cdrag.x) * sc2 * (cv.vw / V.W) / cv.R.w, 0, 1); CV.C.py = clamp(cdrag.py - (e.clientY - cdrag.y) * sc2 * (cv.vh / V.H) / cv.R.h, 0, 1); frame();
    });
    canvas.addEventListener("pointerup", function () { if (cdrag) { cdrag = null; coverChanged(); } });
    canvas.addEventListener("wheel", function (e) { if (!coverMode || CV.C.src === "frame") return; e.preventDefault(); CV.C.zoom = clamp((+CV.C.zoom || 1) * (e.deltaY < 0 ? 1.07 : 1 / 1.07), 1, 4); coverChanged(true); }, { passive: false });

    // khởi động
    syncUI();
    (async function () {
      var ph = $('[data-v="scene"]'); ph.textContent = "⏳ Đang tải ảnh tác phẩm…";
      if ((O.vlang || "vi") !== "vi") { await ensureLang(O.vlang); w = localize(w0, O.vlang); syncUI(); }
      ensureBrand().then(function () { if (!playing) frame(); });
      I = await loadWorkImages(w0, function (d, n) { ph.textContent = "⏳ Đang tải ảnh " + d + "/" + n + "…"; });
      rebuild(); t = posterT(V); atPoster = true; syncCover(); frame();
      if (opts.edit) toggleEditor(true);
      if (opts.ai) { if (!editMode) toggleEditor(true); openAI(); }
    })();
    return { close: close, get V() { return V; }, get work() { return w; }, setLang: setLang };
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
    batch: batch, aiPrompt: aiPrompt, commonsSearch: commonsSearch, srcLabel: srcLabel, openerList: openerList,
    LANGS: LANGS, LINFO: LINFO, ensureLang: ensureLang, localize: localize, trStatus: trStatus, trPrompt: trPrompt,
    _t: { narrate: narrate, build: build, renderArt: renderArt, pickSteps: pickSteps, loadWorkImages: loadWorkImages, prepImage: prepImage, commonsCands: commonsCands, boxView: boxView, fullView: fullView,
          chapters: chapters, postText: postText, cover: cover, DEF: DEF, sceneAt: sceneAt, LY: LY, applyAI: applyAI, parseAIJSON: parseAIJSON, produce: produce,
          splitX: splitX, speakX: speakX, disp: disp, spk: spk, viNumbers: viNumbers, narrateX: narrateX, openerListX: openerListX, ytMeta: ytMeta, ytTitle: ytTitle, renderCover: renderCover, coverLines: coverLines, loadOpts: loadOpts, applyTr: applyTr }
  };
})(window);
