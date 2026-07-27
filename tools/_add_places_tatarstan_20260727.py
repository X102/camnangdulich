# -*- coding: utf-8 -*-
"""_add_places_tatarstan_20260727.py — Bổ sung địa điểm cho VÙNG TIÊU ĐIỂM: Cộng hoà Tatarstan.

Chạy tự động 2026-07-27. Vùng tiêu điểm = 'tatarstan' (đầu danh sách ưu tiên, đang có 10 địa điểm < 50).
Bổ sung 16 địa điểm THỰC SỰ nổi tiếng còn THIẾU, đa dạng loại hình (nhà thờ/thánh đường, nhà hát,
bảo tàng, cầu, kè sông/phố đi bộ, đại học lịch sử, khu thiên nhiên, di tích khảo cổ, thị trấn cổ,
thánh đường hiện đại). Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch nguyên văn), có ghi nguồn.

CHỐNG TRÙNG: đã quét slug + toàn văn tatarstan.json (10 bản ghi hiện có):
  kazan-kremlin, sviyazhsk, bolgar, temple-all-religions, bauman-street, raifa-monastery,
  kazan-family-center, elabuga, palace-of-farmers, old-tatar-sloboda.
16 slug thêm dưới đây đều CHƯA có. Ghi chú phân biệt:
  - 'kazan-icon-cathedral' (Tu viện Bogoroditsky / Nhà thờ Biểu tượng Đức Mẹ Kazan) KHÁC Kul-Sharif trong kazan-kremlin.
  - 'bolgar-white-mosque' (Nhà thờ Hồi giáo Trắng, xây 2012) là công trình HIỆN ĐẠI cách khu di tích cổ 'bolgar' ~1,5 km về phía nam — đối tượng khác, không trùng.
  - 'epiphany-belltower' (Tháp chuông Nhà thờ Chúa Hiển Linh) nằm TRÊN phố Bauman nhưng là công trình riêng, khác bản ghi 'bauman-street' (bản thân con phố).
  - 'chak-chak-museum' & không trùng 'old-tatar-sloboda' (khu phố) dù cùng nằm trong Sloboda.

TOẠ ĐỘ THẬT — xác minh chéo (Wikidata / Wikipedia geohack / 2GIS org-card / Yandex Maps), 2026-07.
Kiểm tra thứ tự lat/lon: lat 54,97–55,91 (∈41–70), lon 49,06–52,32 (∈19–180), KHÔNG đảo; đều nằm đúng phạm vi vùng.

LINK BẢN ĐỒ dạng TRỎ-ĐỊA-ĐIỂM:
  - Ưu tiên URL trang địa điểm Yandex (geo/org) khi tra được: kremlin-embankment, millennium-bridge,
    tugan-avylym, chistopol (bảo tàng Pasternak).
  - Còn lại dùng helper maps_text(text=tên_ru + thành phố, ll=toạ độ đã kiểm chứng) → mở đúng thẻ địa điểm.
  Tất cả vẫn LƯU coordinates{lat,lon} chuẩn cho bản đồ nội bộ/GIS.

Chạy:  python3 tools/_add_places_tatarstan_20260727.py
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-27"

RID = "tatarstan"
RNAME_VI = "Cộng hoà Tatarstan"
FD = "Vùng Volga"
CITY_RU_KAZAN = "Казань"
CITY_EN_KAZAN = "Kazan"


def _google(name_en, region_en):
    parts = [name_en]
    if region_en.lower() not in name_en.lower():
        parts.append(region_en)
    parts.append("Russia")
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(", ".join(parts))


def maps_text(name_ru, region_ru, name_en, region_en, lat, lon):
    """Trỏ thẳng tới địa điểm bằng tên + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {region_ru}")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": _google(name_en, region_en),
    }


def rec(slug, name_vi, name_ru, name_en, cats, lat, lon, address_vi,
        short, long_, hl, practical, sources, tags, maps=None, official=None):
    return {
        "id": f"{RID}-{slug}",
        "slug": slug,
        "region": RID,
        "region_name_vi": RNAME_VI,
        "federal_district": FD,
        "name_vi": name_vi,
        "name_ru": name_ru,
        "name_en": name_en,
        "categories": cats,
        "coordinates": {"lat": lat, "lon": lon},
        "address_vi": address_vi,
        "rating": None,
        "presentation_short_vi": short,
        "presentation_long_vi": long_,
        "highlights_vi": hl,
        "practical": practical,
        "photo": None,
        "photo_credit": None,
        "maps": maps if maps else maps_text(name_ru, CITY_RU_KAZAN, name_en, CITY_EN_KAZAN, lat, lon),
        "official_site": official,
        "sources": sources,
        "tags": tags,
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia",
    }


RECORDS = []

# ============================================================ 1
RECORDS.append(rec(
    "kazan-icon-cathedral",
    "Nhà thờ Biểu tượng Đức Mẹ Kazan và Tu viện Bogoroditsky (Sobor Kazanskoy ikony Bozhiey Materi)",
    "Собор Казанской иконы Божией Матери (Казанско-Богородицкий монастырь)",
    "Cathedral of the Kazan Icon of the Mother of God (Kazan-Bogoroditsky Monastery)",
    ["church", "monument"],
    55.799426, 49.113391,
    "Phố Bolshaya Krasnaya (Большая Красная), số 5, trung tâm thành phố Kazan; cách Điện Kremlin khoảng 600 m về phía đông bắc, Cộng hoà Tatarstan.",
    ("Đây là nơi năm 1579 một bé gái đã tìm thấy biểu tượng «Đức Mẹ Kazan» dưới đống tro tàn sau vụ cháy lớn — "
     "bức icon trở thành một trong những thánh vật được tôn kính bậc nhất của Chính thống giáo Nga. Trên chính "
     "địa điểm ấy, Sa hoàng Ivan Bạo chúa cho lập tu viện nữ Bogoroditsky; nhà thờ chính đồ sộ về sau bị phá huỷ "
     "thời Xô-viết và được phục dựng, tái thánh hiến năm 2021."),
    ("Câu chuyện về địa điểm này gắn liền với sự kiện năm 1579: sau một trận hoả hoạn thiêu rụi phần lớn Kazan, "
     "theo truyền tụng, một bé gái tên Matrona đã mơ thấy Đức Mẹ chỉ dẫn và tìm được bức biểu tượng chôn dưới nền "
     "nhà. Bức «Đức Mẹ Kazan» nhanh chóng nổi tiếng linh thiêng, được sao chép và tôn kính khắp nước Nga, thậm chí "
     "được xem là vị thánh bảo trợ trong nhiều biến cố lịch sử. Trên nền nơi phát hiện, tu viện nữ Bogoroditsky ra "
     "đời theo lệnh Ivan Bạo chúa, dần trở thành một quần thể tu viện lớn với nhà thờ chính nguy nga xây đầu thế kỷ "
     "19. Thời Liên Xô, tu viện bị đóng cửa, nhà thờ chính bị giật đổ những năm 1930, khu đất bị trưng dụng làm cơ "
     "sở công nghiệp và nhà ở. Từ đầu thế kỷ 21, chính quyền Tatarstan cùng Giáo hội đã khởi động dự án phục dựng "
     "quy mô lớn; nhà thờ chính được xây lại theo nguyên mẫu và long trọng tái thánh hiến năm 2021, khôi phục lại "
     "một trong những trung tâm hành hương quan trọng nhất vùng Volga. Bên dưới nhà thờ còn có nhà thờ hầm nơi từng "
     "chôn giấu và tìm thấy biểu tượng. Ngày nay du khách có thể chiêm ngưỡng kiến trúc cổ điển bề thế, các bức "
     "bích hoạ mới và không khí trầm mặc của một địa chỉ tâm linh gắn với huyền thoại «Đức Mẹ Kazan»."),
    [
        "Địa điểm gắn với huyền thoại tìm thấy biểu tượng «Đức Mẹ Kazan» năm 1579 — một trong những thánh vật được tôn kính nhất của Chính thống giáo Nga.",
        "Nhà thờ chính đồ sộ được phục dựng theo nguyên mẫu và tái thánh hiến năm 2021 sau khi bị phá huỷ thời Xô-viết.",
        "Nhà thờ hầm (pescherny khram) ngay nơi từng chôn giấu biểu tượng — điểm hành hương của tín đồ khắp nước Nga.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày cho khách hành hương và tham quan (thường khoảng 7:00–20:00); giờ lễ có thể khác.",
        "ticket_vi": "Vào tham quan tự do (miễn phí); có thể quyên góp tuỳ tâm.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm; dịp lễ Đức Mẹ Kazan (21/7 và 4/11) rất đông tín đồ.",
        "tips_vi": "Ăn mặc kín đáo; nữ nên mang khăn trùm đầu. Nằm gần khu Kremlin nên dễ kết hợp trong lộ trình đi bộ trung tâm.",
    },
    [
        {"title": "Wikipedia (RU) — Казанский Богородицкий монастырь", "url": "https://ru.wikipedia.org/wiki/Казанский_Богородицкий_монастырь"},
        {"title": "Wikidata — Cathedral of the Kazan Icon", "url": "https://www.wikidata.org/wiki/Q125869013"},
        {"title": "Visit Tatarstan — Bogoroditsky Monastery", "url": "https://visit-tatarstan.com/en/places/religion/bogorodickij_monastyr/"},
    ],
    ["church", "orthodox", "our-lady-of-kazan", "icon", "monastery", "pilgrimage", "kazan"],
))

# ============================================================ 2
RECORDS.append(rec(
    "peter-and-paul-cathedral",
    "Nhà thờ Thánh Phêrô và Phaolô (Petropavlovsky sobor)",
    "Петропавловский собор",
    "Saints Peter and Paul Cathedral",
    ["church"],
    55.793373, 49.113062,
    "Phố Musa Cälil (Мусы Джалиля), số 21, trung tâm Kazan; gần Điện Kremlin và phố đi bộ Bauman, Cộng hoà Tatarstan.",
    ("Nhà thờ Thánh Phêrô và Phaolô là một trong những công trình đẹp nhất của phong cách Baroque Naryshkin ở Nga. "
     "Được thương gia Ivan Mikhlyaev cho xây dựng vào những năm 1720 để chào mừng chuyến thăm Kazan của Pyotr Đại đế, "
     "nhà thờ nổi bật với thân cao nhiều tầng phủ kín hoạ tiết đắp nổi rực rỡ và tháp chuông thanh mảnh."),
    ("Nhà thờ khởi công đầu những năm 1720 (khánh thành khoảng 1726) do thương gia giàu có Ivan Afanasyevich Mikhlyaev "
     "tài trợ, để kỷ niệm dịp Pyotr Đại đế ghé thăm Kazan và mừng sinh nhật thứ 50 của nhà vua. Công trình được xem là "
     "kiệt tác của phong cách «Baroque Naryshkin» (Baroque Moskva): khối nhà thờ vươn cao theo kiểu «bát giác trên tứ "
     "giác», toàn bộ mặt ngoài phủ kín các chi tiết trang trí đắp nổi sơn màu tươi tắn — hoa lá, quả, gờ chỉ — tạo cảm "
     "giác lộng lẫy hiếm thấy. Bên trong lưu giữ bức tường icon (iconostasis) chạm khắc mạ vàng nhiều tầng tuyệt đẹp. "
     "Tháp chuông cao tách rời cũng là điểm nhấn quen thuộc trên nền trời khu trung tâm. Nhà thờ từng đón nhiều nhân vật "
     "lịch sử ghé thăm, và tương truyền danh ca opera Fyodor Shalyapin (Chaliapin) thời trẻ từng hát trong ca đoàn ở đây. "
     "Trải qua hoả hoạn, trùng tu và cả thời kỳ bị đóng cửa dưới chính quyền Xô-viết, ngày nay nhà thờ đã hoạt động trở "
     "lại và là một trong những điểm tham quan tôn giáo được yêu thích nhất Kazan nhờ vẻ ngoài rực rỡ độc đáo."),
    [
        "Kiệt tác Baroque Naryshkin với mặt ngoài phủ kín hoạ tiết đắp nổi sơn màu rực rỡ — độc đáo bậc nhất Kazan.",
        "Xây những năm 1720 nhờ thương gia Mikhlyaev, gắn với chuyến thăm Kazan của Pyotr Đại đế.",
        "Tường icon (iconostasis) chạm khắc mạ vàng nhiều tầng và tháp chuông cao thanh thoát.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày, thường khoảng 7:00–19:00 (giờ lễ có thể khác).",
        "ticket_vi": "Vào tham quan tự do (miễn phí); quyên góp tuỳ tâm.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Quanh năm; buổi sáng ánh sáng đẹp để chụp mặt tiền nhiều màu.",
        "tips_vi": "Ăn mặc kín đáo; nữ mang khăn trùm đầu. Cách phố Bauman và Kremlin chỉ vài phút đi bộ.",
    },
    [
        {"title": "Wikipedia (EN) — Saints Peter and Paul Cathedral, Kazan", "url": "https://en.wikipedia.org/wiki/Saints_Peter_and_Paul_Cathedral,_Kazan"},
        {"title": "Wikidata — Saints Peter and Paul Cathedral", "url": "https://www.wikidata.org/wiki/Q2655072"},
        {"title": "Advantour — Peter and Paul Cathedral, Kazan", "url": "https://www.advantour.com/russia/kazan/saints-peter-and-paul-cathedral.htm"},
    ],
    ["church", "orthodox", "naryshkin-baroque", "baroque", "peter-the-great", "kazan"],
))

# ============================================================ 3
RECORDS.append(rec(
    "epiphany-belltower",
    "Nhà thờ Chúa Hiển Linh và Tháp chuông trên phố Bauman (Bogoyavlensky sobor, kolokolnya)",
    "Богоявленский собор и колокольня",
    "Epiphany Cathedral and Bell Tower",
    ["church", "monument"],
    55.788339, 49.119290,
    "Phố đi bộ Bauman (Баумана), số 78, trung tâm Kazan, Cộng hoà Tatarstan.",
    ("Tháp chuông gạch đỏ cao khoảng 74 m của Nhà thờ Chúa Hiển Linh (xây 1893–1897) là một trong những công trình "
     "cao và dễ nhận ra nhất trên phố đi bộ Bauman. Danh ca opera lừng danh Fyodor Shalyapin (Chaliapin) đã được rửa "
     "tội tại nhà thờ này năm 1873. Trên đỉnh tháp có đài quan sát ngắm toàn cảnh trung tâm Kazan."),
    ("Cụm công trình gồm Nhà thờ Chúa Hiển Linh (Bogoyavlensky) và tháp chuông đứng riêng nổi bật giữa phố đi bộ Bauman "
     "sầm uất. Tháp chuông năm tầng bằng gạch đỏ, cao chừng 74 m, được dựng trong các năm 1893–1897 bằng tiền quyên góp "
     "của thương nhân địa phương, mang phong cách chiết trung pha nét Nga cổ, với những chi tiết trang trí gạch tinh xảo — "
     "vào thời điểm hoàn thành đây là một trong những kiến trúc cao nhất Kazan. Nhà thờ Chúa Hiển Linh cạnh đó có gốc từ "
     "thế kỷ 18. Địa điểm gắn với một tên tuổi lớn của âm nhạc thế giới: Fyodor Shalyapin, giọng bass huyền thoại người "
     "Kazan, đã được rửa tội tại đây năm 1873 — gần đó ngày nay có tượng đài và phố mang tên ông. Sau thời gian dài bị "
     "trưng dụng dưới chính quyền Xô-viết, cụm nhà thờ đã được trả lại cho Giáo hội và trùng tu. Hiện tháp chuông mở đài "
     "quan sát trên cao, cho phép du khách phóng tầm mắt xuống trục phố Bauman nhộn nhịp và mái vòm các nhà thờ trung tâm — "
     "một điểm dừng quen thuộc khi dạo bộ khu lõi lịch sử Kazan."),
    [
        "Tháp chuông gạch đỏ cao ~74 m (1893–1897) — công trình biểu tượng trên phố đi bộ Bauman.",
        "Nơi danh ca opera Fyodor Shalyapin (Chaliapin) được rửa tội năm 1873.",
        "Đài quan sát trên đỉnh tháp ngắm toàn cảnh trung tâm lịch sử Kazan.",
    ],
    {
        "hours_vi": "Nhà thờ mở cửa hằng ngày; đài quan sát trên tháp chuông thường mở khoảng 10:00–19:00 (có thể đổi theo mùa).",
        "ticket_vi": "Vào nhà thờ miễn phí; lên đài quan sát tháp chuông có thu phí ở mức thấp.",
        "duration_vi": "Khoảng 30–45 phút (gồm cả leo tháp).",
        "best_time_vi": "Chiều muộn để ngắm hoàng hôn trên phố Bauman từ đài quan sát.",
        "tips_vi": "Ngay trên phố đi bộ nên dễ kết hợp tham quan; leo tháp bằng cầu thang bộ, nên đi giày thoải mái.",
    },
    [
        {"title": "Wikipedia (EN) — Epiphany Cathedral (Kazan)", "url": "https://en.wikipedia.org/wiki/Epiphany_Cathedral_(Kazan,_Russia)"},
        {"title": "Wikipedia (RU) — Богоявленский собор (Казань)", "url": "https://ru.wikipedia.org/wiki/Богоявленский_собор_(Казань)"},
    ],
    ["church", "belltower", "bauman-street", "chaliapin", "viewpoint", "kazan"],
))

# ============================================================ 4
RECORDS.append(rec(
    "opera-ballet-theatre",
    "Nhà hát Opera và Ballet Tatar mang tên Musa Cälil (Musa Jalil)",
    "Татарский академический государственный театр оперы и балета имени Мусы Джалиля",
    "Musa Jalil Tatar Academic State Opera and Ballet Theatre",
    ["theatre"],
    55.795385, 49.124704,
    "Quảng trường Tự do (площадь Свободы), số 2, trung tâm Kazan, Cộng hoà Tatarstan.",
    ("Nhà hát Opera và Ballet Tatar mang tên Musa Cälil là một trong những nhà hát nhạc kịch lớn và uy tín nhất nước "
     "Nga. Toà nhà tân cổ điển bề thế với hàng cột lớn nằm bên Quảng trường Tự do, hoàn thành năm 1956, nội thất trang "
     "trí hoạ tiết dân tộc Tatar. Đây là nơi diễn ra hai liên hoan tầm cỡ quốc tế: Liên hoan Opera Shalyapin và Liên "
     "hoan Ballet Nureyev."),
    ("Nhà hát có bề dày từ đầu thế kỷ 20 và chuyển tới toà nhà hiện nay bên Quảng trường Tự do vào năm 1956. Công trình "
     "mang phong cách tân cổ điển Xô-viết đồ sộ: mặt tiền với hàng cột lớn kiểu portico, các sảnh và khán phòng lộng lẫy "
     "kết hợp hài hoà giữa trang trí cổ điển châu Âu và hoạ tiết trang trí dân tộc Tatar. Nhà hát mang tên Musa Cälil — "
     "nhà thơ Tatar, Anh hùng Liên Xô hy sinh trong Thế chiến II. Đây là một trong những sân khấu nhạc kịch hàng đầu nước "
     "Nga, đặc biệt nổi tiếng nhờ hai liên hoan thường niên thu hút nghệ sĩ và khán giả quốc tế: Liên hoan Opera quốc tế "
     "mang tên Fyodor Shalyapin (thường vào tháng 2) và Liên hoan Ballet cổ điển quốc tế mang tên Rudolf Nureyev (thường "
     "vào tháng 5) — Nureyev vốn gắn bó thời trẻ với Kazan. Vé xem biểu diễn tại đây được săn đón, và ngay cả khi không "
     "xem diễn, du khách vẫn thường ghé ngắm kiến trúc và quảng trường phía trước với tượng đài nhà thơ Musa Cälil."),
    [
        "Toà nhà tân cổ điển bề thế bên Quảng trường Tự do (1956), nội thất pha hoạ tiết dân tộc Tatar.",
        "Nơi tổ chức Liên hoan Opera quốc tế Shalyapin và Liên hoan Ballet quốc tế Nureyev tầm cỡ thế giới.",
        "Mang tên Musa Cälil — nhà thơ Tatar, Anh hùng Liên Xô; phía trước có tượng đài của ông.",
    ],
    {
        "hours_vi": "Theo lịch biểu diễn; phòng vé mở cửa ban ngày. Nên đặt vé trước, nhất là mùa liên hoan.",
        "ticket_vi": "Giá vé tuỳ chương trình và vị trí ghế; mùa liên hoan Shalyapin/Nureyev vé đắt và bán rất nhanh.",
        "duration_vi": "Một buổi diễn thường 2–3 giờ; ngắm kiến trúc bên ngoài khoảng 15–20 phút.",
        "best_time_vi": "Tháng 2 (Liên hoan Shalyapin) và tháng 5 (Liên hoan Nureyev) là cao điểm nghệ thuật.",
        "tips_vi": "Mua vé qua trang chính thức của nhà hát; trang phục lịch sự khi xem diễn. Quảng trường Tự do phía trước cũng đẹp để dạo và chụp ảnh.",
    },
    [
        {"title": "Wikidata — Musa Jalil Opera and Ballet Theatre", "url": "https://www.wikidata.org/wiki/Q2047744"},
        {"title": "Amazing Tatarstan — Jalil Opera & Ballet Theatre", "url": "https://tatarstan.eu/tourism-recreation/theatres-concert-halls/jalil-opera-ballet-tatar-state-academic-theatre/"},
    ],
    ["theatre", "opera", "ballet", "chaliapin-festival", "nureyev-festival", "kazan"],
    official="https://kazan-opera.ru",
))

# ============================================================ 5
RECORDS.append(rec(
    "kamal-theatre",
    "Nhà hát Hàn lâm Tatar Galiaskar Kamal bên hồ Kaban (Teatr im. G. Kamala)",
    "Татарский государственный академический театр имени Галиасгара Камала",
    "Galiaskar Kamal Tatar State Academic Theatre",
    ["theatre"],
    55.782782, 49.117323,
    "Toà nhà cũ mang tính biểu tượng: phố Tatarstan (Татарстан), số 1, bên hồ Nizhny Kaban; toà nhà mới (khánh thành 1/2025): phố Hadi Taktash (Хади Такташа), số 74 — cùng ở Kazan.",
    ("Nhà hát Hàn lâm Tatar mang tên nhà viết kịch Galiaskar Kamal là sân khấu kịch tiếng Tatar hàng đầu (thành lập "
     "1906). Toà nhà xây năm 1987 bên hồ Kaban với đường nét mái gợi hình cánh buồm/tảng băng từ lâu là biểu tượng của "
     "Kazan. Đầu năm 2025, nhà hát khánh thành toà nhà mới hiện đại ấn tượng ở phía bên kia hồ (có sự tham gia của các "
     "hãng kiến trúc quốc tế), nơi hiện diễn ra các buổi biểu diễn."),
    ("Nhà hát kịch tiếng Tatar Galiaskar Kamal có lịch sử từ năm 1906 và là biểu tượng của sân khấu dân tộc Tatar. Trong "
     "nhiều thập niên, nhà hát gắn với toà nhà xây năm 1987 bên bờ hồ Nizhny Kaban — công trình theo phong cách hiện đại "
     "Xô-viết với phần mái vươn nghiêng đặc trưng, thường được ví như cánh buồm hay khối băng, trở thành một trong những "
     "hình ảnh nhận diện của Kazan. Đến tháng 1 năm 2025, nhà hát khánh thành một toà nhà mới hoành tráng ngay phía bên "
     "kia hồ Kaban (địa chỉ phố Hadi Taktash, số 74), do liên danh kiến trúc trong nước và quốc tế (trong đó có sự tham "
     "gia của các kiến trúc sư tên tuổi) thiết kế, với những đường nét lấy cảm hứng từ «hoa băng» trên mặt hồ Kaban — "
     "công trình lập tức được xem là một điểm nhấn kiến trúc mới của thành phố và là nơi diễn ra các buổi biểu diễn hiện "
     "nay. Cả hai toà nhà nằm chéo nhau qua hồ, tạo nên một cụm điểm đến thú vị: du khách vừa có thể ngắm toà nhà biểu "
     "tượng cũ, vừa chiêm ngưỡng công trình mới hiện đại soi bóng xuống hồ Kaban."),
    [
        "Sân khấu kịch tiếng Tatar hàng đầu (thành lập 1906), mang tên nhà viết kịch Galiaskar Kamal.",
        "Toà nhà 1987 bên hồ Kaban với mái hình «cánh buồm» — biểu tượng quen thuộc của Kazan.",
        "Toà nhà mới hiện đại khánh thành đầu năm 2025 bên kia hồ, lấy cảm hứng «hoa băng» hồ Kaban.",
    ],
    {
        "hours_vi": "Theo lịch biểu diễn (chủ yếu bằng tiếng Tatar, thường có phụ đề/dịch tiếng Nga); phòng vé mở ban ngày.",
        "ticket_vi": "Giá vé tuỳ chương trình và vị trí; ở mức phải chăng so với nhà hát opera.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ; ngắm kiến trúc và dạo bờ hồ Kaban khoảng 30–45 phút.",
        "best_time_vi": "Quanh năm; hoàng hôn bên hồ Kaban đẹp để chụp ảnh cả hai toà nhà.",
        "tips_vi": "Kiểm tra trước xem buổi diễn ở toà nhà mới (Hadi Taktash 74) hay không; kết hợp dạo bộ khu Old Tatar Sloboda và kè hồ Kaban gần đó.",
    },
    [
        {"title": "The Moscow Times — New Tatar State Academic Theater Building Opens in Kazan (2025)", "url": "https://www.themoscowtimes.com/2025/01/21/in-photos-new-tatar-state-academic-theater-building-opens-in-kazan-a87679"},
        {"title": "Amazing Tatarstan — Kamal Tatar State Academic Theatre", "url": "https://tatarstan.eu/tourism-recreation/theatres-concert-halls/kamal-tatar-state-academic-theatre/"},
    ],
    ["theatre", "tatar-culture", "lake-kaban", "architecture", "kazan"],
    official="https://kamalteatr.ru",
))

# ============================================================ 6
RECORDS.append(rec(
    "national-museum-tatarstan",
    "Bảo tàng Quốc gia Cộng hoà Tatarstan (Natsionalny muzey RT)",
    "Национальный музей Республики Татарстан",
    "National Museum of the Republic of Tatarstan",
    ["museum"],
    55.795787, 49.109721,
    "Phố Kremlyovskaya (Кремлёвская), số 2, đối diện tháp Spasskaya của Điện Kremlin, trung tâm Kazan, Cộng hoà Tatarstan.",
    ("Bảo tàng Quốc gia Cộng hoà Tatarstan là bảo tàng lịch sử – văn hoá lớn nhất vùng, thành lập năm 1895. Bảo tàng "
     "toạ lạc trong toà Gostiny Dvor (thương xá) cổ ngay đối diện cổng Kremlin, lưu giữ hàng trăm nghìn hiện vật về "
     "lịch sử Bulgar Volga, hãn quốc Kazan, dân tộc học và thiên nhiên Tatarstan."),
    ("Được thành lập năm 1895 trên cơ sở bộ sưu tập cá nhân của nhà sưu tầm địa phương và các hiện vật từ triển lãm khoa "
     "học – công nghiệp, đây là bảo tàng lâu đời và lớn nhất Tatarstan. Bảo tàng đặt trong toà Gostiny Dvor (thương xá cũ) "
     "bề thế nằm ngay đầu phố Kremlyovskaya, đối diện tháp Spasskaya — cổng chính của Điện Kremlin Kazan. Bộ sưu tập lên "
     "tới hàng trăm nghìn hiện vật, trải rộng nhiều lĩnh vực: khảo cổ và lịch sử nhà nước Bulgar Volga cùng hãn quốc Kazan, "
     "dân tộc học các dân tộc vùng Volga, tiền cổ, vũ khí, trang phục và đồ trang sức truyền thống Tatar, cùng các phòng "
     "trưng bày thiên nhiên. Trong số hiện vật quý có cỗ xe ngựa mạ vàng gắn với chuyến kinh lý của Nữ hoàng Ekaterina II "
     "tới Kazan, các sưu tập khảo cổ Bulgar và những bảo vật văn hoá Tatar. Bảo tàng vừa là nơi giới thiệu súc tích lịch "
     "sử đa tầng của vùng đất giao thoa Đông – Tây này, vừa là một công trình kiến trúc đẹp trong quần thể trung tâm lịch "
     "sử Kazan; xung quanh còn nhiều bảo tàng chi nhánh chuyên đề."),
    [
        "Bảo tàng lớn và lâu đời nhất Tatarstan (từ 1895) với hàng trăm nghìn hiện vật.",
        "Đặt trong toà Gostiny Dvor cổ, ngay đối diện cổng Kremlin Kazan — vị trí trung tâm đắc địa.",
        "Sưu tập khảo cổ Bulgar Volga, dân tộc học Tatar và cỗ xe ngựa mạ vàng gắn với Nữ hoàng Ekaterina II.",
    ],
    {
        "hours_vi": "Thường mở 10:00–18:00, một số ngày tới muộn hơn; nghỉ thứ Hai (nên kiểm tra trước).",
        "ticket_vi": "Vé vào ở mức phải chăng; có vé gộp cho các phòng/chi nhánh và ưu đãi cho học sinh, người cao tuổi.",
        "duration_vi": "Khoảng 1,5–2,5 giờ.",
        "best_time_vi": "Quanh năm; thuận tiện ghép cùng tham quan Kremlin ngay bên cạnh.",
        "tips_vi": "Nằm sát cổng Kremlin nên rất tiện kết hợp. Có thể thuê audio-guide; nhiều bảng chú thích song ngữ Nga – Tatar.",
    },
    [
        {"title": "Wikidata — National Museum of the Republic of Tatarstan", "url": "https://www.wikidata.org/wiki/Q4315032"},
        {"title": "Wikipedia (RU) — Национальный музей Республики Татарстан", "url": "https://ru.wikipedia.org/wiki/Национальный_музей_Республики_Татарстан"},
    ],
    ["museum", "history", "ethnography", "gostiny-dvor", "kazan"],
    official="https://tatmuseum.ru",
))

# ============================================================ 7
RECORDS.append(rec(
    "kremlin-embankment",
    "Kè sông Kremlin (Kremlyovskaya naberezhnaya)",
    "Кремлёвская набережная",
    "Kremlin Embankment (Kremlyovskaya Naberezhnaya)",
    ["square_street", "park_garden"],
    55.803828, 49.116763,
    "Dọc sông Kazanka dưới chân Điện Kremlin, trung tâm Kazan, Cộng hoà Tatarstan.",
    ("Kè sông Kremlin là tuyến đi bộ – vui chơi ven sông Kazanka dài khoảng 1,5 km chạy dưới chân Điện Kremlin. Sau khi "
     "được cải tạo trong thập niên 2010, nơi đây trở thành không gian dạo chơi được yêu thích nhất Kazan với lối đi lát "
     "gỗ, quán cà phê, làn xe đạp, các sự kiện lễ hội và sân trượt băng dài về mùa đông."),
    ("Chạy dọc bờ sông Kazanka ngay dưới những bức tường trắng của Điện Kremlin, Kè sông Kremlin là một dự án chỉnh trang "
     "đô thị tiêu biểu của Kazan hiện đại. Từ một dải bờ sông ít được khai thác, khu vực đã được cải tạo trong thập niên "
     "2010 thành tuyến promenade dài khoảng 1,5 km nhiều tầng bậc, với sàn đi bộ, ghế nghỉ, tiểu cảnh, hàng quán cà phê – "
     "nhà hàng, làn dành cho xe đạp và patin. Đây là nơi diễn ra nhiều lễ hội, chợ phiên, sự kiện âm nhạc và bắn pháo hoa; "
     "về mùa đông, một phần kè biến thành sân trượt băng ngoài trời rất dài và nổi tiếng. Từ kè, du khách có góc nhìn đẹp "
     "lên quần thể Kremlin, sông Kazanka và các cây cầu, đặc biệt lung linh khi lên đèn buổi tối. Nối liền với kè hồ "
     "Nizhny Kaban ở khu trung tâm, tuyến đi bộ ven nước này giúp cảm nhận nhịp sống thư thái, năng động của người Kazan "
     "và là điểm thư giãn lý tưởng sau khi tham quan Kremlin."),
    [
        "Promenade ven sông Kazanka dài ~1,5 km ngay dưới chân Điện Kremlin.",
        "Không gian dạo chơi sôi động: quán cà phê, làn xe đạp, lễ hội, bắn pháo hoa.",
        "Sân trượt băng ngoài trời rất dài về mùa đông và góc ngắm Kremlin lên đèn buổi tối.",
    ],
    {
        "hours_vi": "Không gian công cộng ngoài trời, mở tự do cả ngày; các quán và dịch vụ theo giờ riêng.",
        "ticket_vi": "Đi dạo miễn phí; thuê xe đạp, patin hay vào sân trượt băng mùa đông có phí.",
        "duration_vi": "Khoảng 1–2 giờ tuỳ nhịp dạo.",
        "best_time_vi": "Chiều tối mùa hè để dạo mát và ngắm hoàng hôn; mùa đông để trượt băng.",
        "tips_vi": "Kết hợp ngay sau khi tham quan Kremlin; cuối tuần rất đông, nên đi sớm nếu muốn không gian yên tĩnh.",
    },
    [
        {"title": "Yandex Maps — Кремлёвская набережная", "url": "https://yandex.com/maps/43/kazan/geo/kremlyovskaya_naberezhnaya/23992043/"},
        {"title": "Wikipedia (RU) — Кремлёвская набережная (Казань)", "url": "https://ru.wikipedia.org/wiki/Кремлёвская_набережная_(Казань)"},
    ],
    ["embankment", "promenade", "park", "riverside", "kazanka", "kazan"],
    maps={
        "yandex": "https://yandex.com/maps/43/kazan/geo/kremlyovskaya_naberezhnaya/23992043/",
        "google": _google("Kremlin Embankment (Kremlyovskaya Naberezhnaya)", "Kazan"),
    },
))

# ============================================================ 8
RECORDS.append(rec(
    "millennium-bridge",
    "Cầu Thiên niên kỷ (Most «Millenium»)",
    "Мост «Миллениум»",
    "Millennium Bridge",
    ["bridge"],
    55.806100, 49.144400,
    "Bắc qua sông Kazanka, nối các khu vực trung tâm Kazan, Cộng hoà Tatarstan.",
    ("Cầu Thiên niên kỷ dài 835 m bắc qua sông Kazanka, nổi bật với trụ tháp cao 45 m hình chữ «M» — chữ cái đầu của "
     "«Millennium» (và của «Meñyıllıq», nghĩa là «một nghìn năm» trong tiếng Tatar). Cầu được xây dựng năm 2005–2007 "
     "nhân dịp kỷ niệm 1000 năm thành lập Kazan và trở thành biểu tượng của thành phố hiện đại, đặc biệt lung linh khi "
     "lên đèn về đêm."),
    ("Cầu Thiên niên kỷ là một trong những biểu tượng của Kazan đương đại. Công trình dây văng dài khoảng 835 m vắt qua "
     "sông Kazanka, có điểm nhấn là trụ tháp đơn cao 45 m tạo hình chữ «M» khổng lồ. Chữ «M» mang ý nghĩa kép: vừa là "
     "chữ đầu của từ «Millennium» (Thiên niên kỷ), vừa gợi tới «Meñyıllıq» — «một nghìn năm» trong tiếng Tatar, gắn với "
     "dịp đại lễ kỷ niệm 1000 năm thành lập Kazan. Cầu được khởi công năm 2004 và hoàn thiện làm hai giai đoạn: phần đầu "
     "thông xe năm 2005 đúng dịp đại lễ, phần còn lại hoàn thành năm 2007, phục vụ cả giao thông đô thị lẫn tạo cảnh quan. "
     "Với dáng trụ tháp độc đáo soi bóng xuống mặt nước và hệ thống chiếu sáng đổi màu về đêm, cây cầu trở thành phông nền "
     "quen thuộc trong ảnh chụp Kazan, nhìn rõ từ Kè sông Kremlin và các khu ven sông Kazanka. Đây là ví dụ tiêu biểu cho "
     "diện mạo hiện đại, năng động mà Kazan xây dựng trong hai thập niên qua bên cạnh di sản cổ kính."),
    [
        "Cầu dây văng dài 835 m với trụ tháp cao 45 m tạo hình chữ «M» độc đáo.",
        "Biểu tượng cho đại lễ 1000 năm Kazan (xây 2005–2007); «M» = Millennium / «Meñyıllıq».",
        "Lung linh đổi màu về đêm — phông nền chụp ảnh quen thuộc bên sông Kazanka.",
    ],
    {
        "hours_vi": "Cầu giao thông, có thể ngắm bất cứ lúc nào; đẹp nhất khi lên đèn buổi tối.",
        "ticket_vi": "Miễn phí (ngắm từ hai bờ hoặc từ kè sông).",
        "duration_vi": "Khoảng 15–30 phút để ngắm và chụp ảnh.",
        "best_time_vi": "Buổi tối để xem hệ thống đèn đổi màu; hoàng hôn cho ảnh đẹp.",
        "tips_vi": "Góc chụp đẹp từ Kè sông Kremlin và các công viên ven Kazanka; không có lối đi bộ ngắm cảnh chuyên biệt trên cầu nên nên ngắm từ bờ.",
    },
    [
        {"title": "Wikipedia (EN) — Millennium Bridge (Kazan)", "url": "https://en.wikipedia.org/wiki/Millennium_Bridge_(Kazan)"},
        {"title": "Wikidata — Millennium Bridge", "url": "https://www.wikidata.org/wiki/Q4304520"},
    ],
    ["bridge", "kazanka", "modern", "millennium", "landmark", "kazan"],
    maps={
        "yandex": "https://yandex.com/maps/43/kazan/geo/most_millenium/51318841/",
        "google": _google("Millennium Bridge", "Kazan"),
    },
))

# ============================================================ 9
RECORDS.append(rec(
    "kazan-federal-university",
    "Đại học Liên bang Kazan – toà nhà chính (Kazansky federalny universitet)",
    "Казанский (Приволжский) федеральный университет — главное здание",
    "Kazan Federal University (main building)",
    ["monument", "other"],
    55.790830, 49.121940,
    "Phố Kremlyovskaya (Кремлёвская), số 18, trung tâm Kazan, Cộng hoà Tatarstan.",
    ("Thành lập năm 1804, Đại học Kazan là một trong những trường đại học lâu đời và danh giá nhất nước Nga. Toà nhà "
     "chính theo phong cách tân cổ điển (1825) với hàng cột trắng trải dài cả một dãy phố. Nhà toán học Lobachevsky — "
     "cha đẻ hình học phi Euclid — từng làm hiệu trưởng ở đây; văn hào Lev Tolstoy và Vladimir Ulyanov (Lenin) thời trẻ "
     "cũng từng theo học."),
    ("Đại học Kazan được thành lập năm 1804 theo sắc lệnh của Sa hoàng Aleksandr I, thuộc nhóm những đại học cổ xưa nhất "
     "nước Nga và là trung tâm khoa học – giáo dục hàng đầu của vùng Volga. Toà nhà chính tân cổ điển, hoàn thành năm "
     "1825 theo thiết kế của kiến trúc sư Pyatnitsky, gây ấn tượng với mặt tiền dài, hàng cột và portico trắng trang "
     "nghiêm, chiếm trọn một đoạn phố Kremlyovskaya. Ngôi trường gắn với nhiều tên tuổi lớn: nhà toán học Nikolai "
     "Lobachevsky — người đặt nền móng cho hình học phi Euclid — đã giảng dạy và làm hiệu trưởng nhiều năm tại đây (nay "
     "có tượng đài và quảng trường mang tên ông trước trường); văn hào Lev Tolstoy từng là sinh viên; và Vladimir Ulyanov "
     "(sau này là Lenin) cũng theo học luật ở Kazan thời trẻ trước khi bị đuổi vì tham gia phong trào sinh viên. Trong "
     "khuôn viên còn có tổ hợp các toà nhà lịch sử, đài thiên văn cổ, thư viện khoa học lớn và nhiều bảo tàng chuyên ngành. "
     "Với du khách, cụm kiến trúc đại học và quảng trường Lobachevsky là một điểm dừng đẹp và giàu chiều sâu lịch sử trên "
     "trục phố trung tâm nối Kremlin với Quảng trường Tự do."),
    [
        "Một trong những đại học lâu đời nhất nước Nga (thành lập 1804); toà nhà chính tân cổ điển 1825.",
        "Gắn với nhà toán học Lobachevsky (hình học phi Euclid) — có tượng đài và quảng trường mang tên ông.",
        "Nơi Lev Tolstoy và Vladimir Ulyanov (Lenin) thời trẻ từng theo học.",
    ],
    {
        "hours_vi": "Là cơ sở giáo dục đang hoạt động; ngắm kiến trúc bên ngoài tự do. Một số bảo tàng và không gian trong trường mở theo giờ riêng hoặc theo tour.",
        "ticket_vi": "Ngắm bên ngoài miễn phí; vào các bảo tàng chuyên ngành có thể cần đăng ký/tour và thu phí nhỏ.",
        "duration_vi": "Khoảng 30–45 phút cho khu toà nhà chính và quảng trường Lobachevsky.",
        "best_time_vi": "Quanh năm; ban ngày để ngắm mặt tiền tân cổ điển.",
        "tips_vi": "Nằm trên trục đi bộ trung tâm, dễ kết hợp với Kremlin, phố Bauman và Nhà hát Opera. Tôn trọng khu vực học tập khi tham quan.",
    },
    [
        {"title": "Wikipedia (EN) — Kazan Federal University", "url": "https://en.wikipedia.org/wiki/Kazan_Federal_University"},
        {"title": "Wikidata — Kazan Federal University", "url": "https://www.wikidata.org/wiki/Q113788"},
    ],
    ["university", "history", "architecture", "lobachevsky", "tolstoy", "lenin", "kazan"],
    official="https://kpfu.ru",
))

# ============================================================ 10
RECORDS.append(rec(
    "chak-chak-museum",
    "Bảo tàng Chak-chak (Muzey chak-chaka)",
    "Музей чак-чака",
    "Museum of Chak-Chak",
    ["museum"],
    55.782065, 49.112483,
    "Khu phố Tatar Cổ (Staro-Tatarskaya Sloboda), phố Parizhskoy Kommuny (Парижской Коммуны), số 18а, Kazan, Cộng hoà Tatarstan.",
    ("Bảo tàng Chak-chak là một bảo tàng tư nhân nhỏ ấm cúng nằm trong ngôi nhà gỗ thương gia Tatar thế kỷ 19 giữa Khu "
     "phố Tatar Cổ. Bảo tàng dành riêng cho ẩm thực và nếp sống truyền thống Tatar, với nghi thức trà kèm chak-chak — món "
     "bánh chiên rưới mật ong trứ danh — cùng các loại bánh kẹo dân tộc."),
    ("Mở cửa năm 2014, Bảo tàng Chak-chak là một trong những địa chỉ giúp du khách «chạm» vào văn hoá Tatar theo cách gần "
     "gũi và ngon miệng nhất. Bảo tàng đặt trong một ngôi nhà gỗ hai tầng kiểu thương gia Tatar thế kỷ 19, nằm giữa Khu "
     "phố Tatar Cổ ven hồ Kaban — nơi lưu giữ không khí sinh hoạt truyền thống của cộng đồng Tatar Kazan. Không gian được "
     "bài trí như một ngôi nhà xưa, với đồ nội thất, ấm samovar, bát đĩa và vật dụng sinh hoạt cổ. Điểm nhấn là buổi giới "
     "thiệu và thưởng trà: khách được nghe kể về phong tục hiếu khách, cách pha trà và nếm thử chak-chak — món bánh làm từ "
     "bột chiên kết dính bằng mật ong, biểu tượng ẩm thực của người Tatar — cùng nhiều loại bánh kẹo dân tộc khác như "
     "gubadiya, talkysh-kaleve. Quy mô tuy nhỏ nhưng trải nghiệm ấm cúng, thân thiện, phù hợp cho gia đình và những ai "
     "muốn hiểu thêm về đời sống, tín ngưỡng và văn hoá trà – bánh của vùng Tatarstan. Bảo tàng nằm trong cụm Sloboda "
     "cùng các thánh đường và nhà gỗ cổ, tiện kết hợp dạo bộ."),
    [
        "Bảo tàng tư nhân ấm cúng trong nhà gỗ thương gia Tatar thế kỷ 19 giữa Khu phố Tatar Cổ.",
        "Nghi thức trà truyền thống kèm nếm thử chak-chak (bánh chiên mật ong) và bánh kẹo dân tộc.",
        "Cách nhẹ nhàng, ngon miệng để tìm hiểu phong tục hiếu khách và ẩm thực Tatar.",
    ],
    {
        "hours_vi": "Thường mở hằng ngày khoảng 10:00–19:00; các suất giới thiệu – thưởng trà theo giờ, nên đặt trước.",
        "ticket_vi": "Vé vào kèm chương trình trà – nếm bánh ở mức phải chăng; đặt trước qua điện thoại/website.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm; hợp làm điểm dừng nghỉ khi dạo Khu phố Tatar Cổ.",
        "tips_vi": "Nên đặt chỗ trước vì không gian nhỏ; báo trước nếu ăn chay/kiêng. Kết hợp tham quan các thánh đường Mardzhani, Apanaevskaya và kè hồ Kaban gần đó.",
    },
    [
        {"title": "2GIS — Музей чак-чака (Казань)", "url": "https://2gis.ru/kazan/firm/70000001007247749"},
        {"title": "Visit Tatarstan — Museum of Chak-Chak", "url": "https://visit-tatarstan.com/en/places/museums/muzey-chak-chaka/"},
    ],
    ["museum", "tatar-cuisine", "chak-chak", "old-tatar-sloboda", "tea-ceremony", "kazan"],
))

# ============================================================ 11
RECORDS.append(rec(
    "tugan-avylym",
    "Tổ hợp làng quê Tatar «Tugan Avylym» (Làng Quê Hương)",
    "Туган Авылым",
    "Tugan Avylym (Native Village)",
    ["other", "park_garden"],
    55.779241, 49.135935,
    "Phố Tufan Minnullin (Туфана Миннуллина), số 14, trung tâm Kazan, Cộng hoà Tatarstan.",
    ("«Tugan Avylym» (Làng Quê Hương) là một tổ hợp dân tộc – giải trí tái hiện làng quê Tatar truyền thống ngay giữa "
     "trung tâm Kazan, với nhà gỗ, cối xay gió, cầu nhỏ, nhà hàng ẩm thực dân tộc và các xưởng thủ công. Đây là nơi được "
     "yêu thích để trải nghiệm kiến trúc gỗ và món ăn Tatar trong không gian làng quê thu nhỏ."),
    ("Nằm giữa lòng đô thị nhưng «Tugan Avylym» lại mang dáng dấp một ngôi làng Tatar cổ được dựng lại công phu bằng gỗ. "
     "Tổ hợp gồm các nếp nhà gỗ theo lối truyền thống, một cối xay gió, những cây cầu nhỏ bắc qua dòng nước, sân vườn và "
     "tiểu cảnh gợi khung cảnh nông thôn xưa. Bên trong bố trí nhiều nhà hàng, quán ăn phục vụ ẩm thực dân tộc Tatar và "
     "Nga (như echpochmak, chak-chak, các món nướng), cùng khu vui chơi, xưởng thủ công và cửa hàng quà lưu niệm. Đây là "
     "địa điểm được cả du khách lẫn người Kazan ưa chuộng để thư giãn, ăn uống, chụp ảnh và cảm nhận không khí làng quê "
     "Tatar mà không phải đi xa khỏi trung tâm. Về buổi tối, hệ thống đèn trang trí khiến khu làng thêm lung linh; nơi "
     "đây cũng thường tổ chức các sự kiện, lễ hội dân gian. Với gia đình có trẻ nhỏ và những ai muốn kết hợp khám phá văn "
     "hoá – ẩm thực trong một điểm đến, «Tugan Avylym» là lựa chọn tiện lợi và giàu bản sắc."),
    [
        "Làng Tatar truyền thống thu nhỏ bằng gỗ (nhà gỗ, cối xay gió, cầu nhỏ) ngay trung tâm Kazan.",
        "Cụm nhà hàng ẩm thực dân tộc Tatar – Nga, xưởng thủ công và khu vui chơi.",
        "Không gian chụp ảnh và trải nghiệm văn hoá lý tưởng cho gia đình, lung linh về đêm.",
    ],
    {
        "hours_vi": "Khu tổ hợp mở cửa tự do; các nhà hàng và cửa hàng theo giờ riêng (nhiều nơi mở tới khuya).",
        "ticket_vi": "Vào khu làng miễn phí; chi phí tuỳ ăn uống, vui chơi và mua sắm.",
        "duration_vi": "Khoảng 1–2 giờ (lâu hơn nếu dùng bữa).",
        "best_time_vi": "Buổi tối để ngắm đèn; giờ ăn trưa/tối để thưởng thức ẩm thực Tatar.",
        "tips_vi": "Thử các món echpochmak, chak-chak; cuối tuần khá đông. Gần khu trung tâm nên dễ kết hợp trong hành trình.",
    },
    [
        {"title": "Yandex Maps — Туган Авылым", "url": "https://yandex.ru/maps/org/tugan_avylym/174985818225/"},
        {"title": "Visit Tatarstan — Tugan Avylym", "url": "https://visit-tatarstan.com/en/places/restaurants/tugan-avylym/"},
    ],
    ["ethnographic", "tatar-village", "cuisine", "family", "kazan"],
    maps={
        "yandex": "https://yandex.ru/maps/org/tugan_avylym/174985818225/",
        "google": _google("Tugan Avylym", "Kazan"),
    },
))

# ============================================================ 12
RECORDS.append(rec(
    "blue-lakes",
    "Khu bảo tồn Hồ Xanh (Goluboye Ozero / Golubye ozyora)",
    "Голубое озеро (заказник «Голубые озёра»)",
    "Blue Lakes Nature Reserve (Goluboye Ozero)",
    ["park_garden"],
    55.906603, 49.155171,
    "Huyện Vysokogorsky (Высокогорский), gần làng Shcherbakovo, cách trung tâm Kazan khoảng 20 km về phía bắc, Cộng hoà Tatarstan.",
    ("Khu bảo tồn Hồ Xanh gồm những hồ nước ngọt hình thành từ mạch nước ngầm karst, nổi tiếng với làn nước trong vắt "
     "màu ngọc lam và nhiệt độ ổn định quanh năm chỉ khoảng 4–7°C. Được bảo vệ như một khu bảo tồn thiên nhiên, đây là "
     "điểm đến ưa thích cho lặn dưới băng mùa đông, tắm nước lạnh và dạo rừng."),
    ("Nằm ở phía bắc Kazan, «Hồ Xanh» (thực chất là một cụm gồm Hồ Xanh Lớn, Hồ Xanh Nhỏ và các hồ nhỏ khác) là một hiện "
     "tượng thiên nhiên độc đáo của Tatarstan. Các hồ được nuôi bằng những mạch nước ngầm karst phun lên từ đáy, nên nước "
     "trong vắt đến mức nhìn thấy tận đáy, ánh lên sắc xanh ngọc lam đặc trưng do khoáng chất và lớp bùn trắng dưới lòng "
     "hồ. Điểm đặc biệt là nhiệt độ nước gần như không đổi quanh năm, chỉ khoảng 4–7°C, khiến hồ không đóng băng hoàn toàn "
     "về mùa đông. Chính vì thế, đây là một trong những điểm lặn nổi tiếng nhất vùng: các thợ lặn tới đây quanh năm, đặc "
     "biệt hấp dẫn vào mùa đông khi có thể lặn dưới lớp băng và ngắm cảnh quan lòng hồ kỳ ảo. Nước giàu khoáng và lớp bùn "
     "sapropel dưới đáy còn được cho là có lợi cho sức khoẻ, nên nhiều người tới ngâm mình tắm nước lạnh. Khu vực đã được "
     "công nhận là khu bảo tồn thiên nhiên nhằm giữ gìn hệ sinh thái đặc biệt và cảnh quan rừng bao quanh. Với du khách, "
     "đây là điểm dã ngoại, chụp ảnh và trải nghiệm thiên nhiên trong ngày lý tưởng, chỉ cách trung tâm Kazan chừng 20 km."),
    [
        "Cụm hồ karst nước trong vắt màu ngọc lam, nhiệt độ ổn định quanh năm chỉ ~4–7°C.",
        "Điểm lặn nổi tiếng, đặc biệt hấp dẫn với lặn dưới băng vào mùa đông.",
        "Khu bảo tồn thiên nhiên với bùn khoáng sapropel và rừng bao quanh — điểm dã ngoại gần Kazan.",
    ],
    {
        "hours_vi": "Khu thiên nhiên ngoài trời, tham quan tự do cả ngày.",
        "ticket_vi": "Miễn phí; chi phí phát sinh nếu thuê dịch vụ lặn hoặc di chuyển.",
        "duration_vi": "Nửa ngày (gồm cả di chuyển từ Kazan).",
        "best_time_vi": "Mùa hè để dạo rừng và chụp ảnh; mùa đông cho trải nghiệm lặn dưới băng (có hướng dẫn chuyên nghiệp).",
        "tips_vi": "Nước rất lạnh — chỉ ngâm/lặn khi có kinh nghiệm hoặc hướng dẫn; giữ gìn vệ sinh môi trường khu bảo tồn. Tự lái xe hoặc đi tour tiện nhất.",
    },
    [
        {"title": "Wikidata — Голубое озеро (Казань)", "url": "https://www.wikidata.org/wiki/Q4142612"},
        {"title": "ShowCaves — Goluboe Ozero (Blue Lake) near Kazan", "url": "https://www.showcaves.com/english/ru/springs/GoluboeOzeroKazan.html"},
    ],
    ["nature", "lake", "karst-spring", "diving", "turquoise", "kazan-day-trip"],
))

# ============================================================ 13
RECORDS.append(rec(
    "bilyar",
    "Khu di tích khảo cổ Biliar («Đại Thành phố» Bulgar) và Suối Thiêng",
    "Билярское городище («Великий город») и Святой ключ",
    "Bilyar Ancient Settlement (Great City) and Holy Spring",
    ["monument", "museum"],
    54.971944, 50.403056,
    "Làng Bilyarsk (Билярск), huyện Alexeyevsky (Алексеевский), cách Kazan khoảng 130 km về phía đông nam, Cộng hoà Tatarstan.",
    ("Bilyar là nơi từng tồn tại thành phố lớn nhất của nhà nước Bulgar Volga trong các thế kỷ 10–13, được sử sách gọi "
     "là «Đại Thành phố» — có thời điểm được xem là một trong những đô thị rộng lớn nhất châu Âu trước khi bị quân Mông "
     "Cổ phá huỷ năm 1236. Ngày nay là khu bảo tồn khảo cổ rộng lớn với nền móng thánh đường lớn và thành luỹ; gần đó là "
     "«Suối Thiêng» — điểm hành hương của nhiều tôn giáo."),
    ("«Đại Thành phố» (Bilyar) là một trong những di chỉ khảo cổ quan trọng bậc nhất vùng Volga. Trong các thế kỷ 10–13, "
     "đây là một trung tâm đô thị lớn của nhà nước Bulgar Volga — có giai đoạn được coi là một trong những thành phố rộng "
     "lớn nhất châu Âu đương thời xét về diện tích, với vòng thành nhiều lớp, khu dân cư, thủ công và thương mại sầm uất "
     "nằm trên tuyến giao thương nối Trung Á với châu Âu. Thành bị quân Mông Cổ tàn phá năm 1236 và không bao giờ hồi sinh "
     "như trước. Ngày nay, khu «Bilyarskoye gorodishche» là một bảo tàng – khu bảo tồn ngoài trời, nơi du khách có thể "
     "thấy dấu tích nền móng của một thánh đường lớn (một trong những nhà thờ Hồi giáo lớn nhất Đông Âu thời trung cổ), "
     "các lớp thành luỹ, giếng và di chỉ khai quật, cùng một bảo tàng khảo cổ trưng bày hiện vật. Cách di chỉ vài km, dưới "
     "chân đồi Hujalar-tavy, là «Suối Thiêng» (Svyatoy klyuch) — một mạch nước được người Hồi giáo Tatar, tín đồ Chính "
     "thống giáo và cả tín ngưỡng dân gian cùng coi là linh thiêng; đây là điểm hành hương đa tôn giáo hiếm có, với dòng "
     "người tới cầu nguyện, lấy nước và leo đồi quanh năm. Bilyar vì thế vừa là địa chỉ lịch sử – khảo cổ, vừa là một "
     "trung tâm tâm linh đặc biệt của Tatarstan."),
    [
        "Di chỉ «Đại Thành phố» — đô thị lớn nhất của Bulgar Volga thế kỷ 10–13, bị Mông Cổ phá huỷ năm 1236.",
        "Nền móng thánh đường lớn và các lớp thành luỹ trong khu bảo tồn khảo cổ ngoài trời, kèm bảo tàng.",
        "«Suối Thiêng» dưới đồi Hujalar-tavy — điểm hành hương đa tôn giáo (Hồi giáo, Chính thống giáo, dân gian).",
    ],
    {
        "hours_vi": "Khu di tích và suối thiêng chủ yếu ngoài trời, tham quan ban ngày; bảo tàng khảo cổ mở theo giờ (thường nghỉ đầu tuần) — nên kiểm tra trước.",
        "ticket_vi": "Vào khu di tích/suối thiêng thường miễn phí; vé bảo tàng ở mức thấp.",
        "duration_vi": "Khoảng 2–3 giờ tại chỗ (chưa kể ~2–2,5 giờ đường từ Kazan mỗi chiều).",
        "best_time_vi": "Cuối xuân đến đầu thu; các dịp lễ tôn giáo suối thiêng rất đông người hành hương.",
        "tips_vi": "Ở xa nên đi tự lái hoặc theo tour trong ngày; mang giày đi bộ để leo đồi ra suối thiêng. Tôn trọng không gian tâm linh của người hành hương.",
    },
    [
        {"title": "Wikipedia (EN) — Bilyar", "url": "https://en.wikipedia.org/wiki/Bilyar"},
        {"title": "Wikidata — Bilyar (Biliar)", "url": "https://www.wikidata.org/wiki/Q2603563"},
    ],
    ["archaeology", "volga-bulgaria", "great-city", "holy-spring", "pilgrimage", "museum-reserve"],
))

# ============================================================ 14
RECORDS.append(rec(
    "lower-kama-national-park",
    "Vườn Quốc gia Hạ Kama (Nizhnyaya Kama)",
    "Национальный парк «Нижняя Кама»",
    "Nizhnyaya Kama (Lower Kama) National Park",
    ["park_garden"],
    55.801110, 52.323330,
    "Vùng đông bắc Tatarstan, trải dọc sông Kama gần các thành phố Elabuga và Naberezhnye Chelny, Cộng hoà Tatarstan.",
    ("Vườn Quốc gia Hạ Kama (thành lập 1991) rộng khoảng 265 km², bảo tồn những cánh rừng thông, đồng cỏ và vùng bãi bồi "
     "ven sông Kama ở đông bắc Tatarstan. Những rừng thông nổi tiếng gần Elabuga — như «Bolshoy Bor» và «Rừng Thuyền» "
     "(Korabelnaya roshcha) — chính là nguồn cảm hứng cho nhiều bức tranh phong cảnh trứ danh của hoạ sĩ Ivan Shishkin."),
    ("Vườn Quốc gia «Nizhnyaya Kama» (Hạ Kama) được thành lập năm 1991 nhằm bảo tồn cảnh quan rừng và bãi bồi đặc trưng "
     "vùng hạ lưu sông Kama. Với diện tích khoảng 265 km², vườn gồm những cánh rừng thông cổ thụ xen kẽ rừng lá rộng, "
     "đồng cỏ, đầm lầy và các vùng bãi bồi ngập nước theo mùa dọc hai bờ sông Kama, tạo nên hệ động – thực vật phong phú "
     "với nhiều loài chim, thú và cây quý. Khu vực nổi tiếng nhất nằm gần thành phố cổ Elabuga: các rừng thông như "
     "«Bolshoy Bor» (Rừng Lớn) và «Korabelnaya roshcha» (Rừng Thuyền — nơi xưa kia tuyển gỗ thông thẳng đóng tàu) chính "
     "là khung cảnh đã đi vào nhiều kiệt tác của hoạ sĩ phong cảnh Nga Ivan Shishkin, người con của Elabuga. Vườn có các "
     "tuyến đi bộ, đường mòn sinh thái, điểm ngắm cảnh bên sông Kama và các địa danh gắn với Shishkin, thích hợp cho du "
     "lịch thiên nhiên, đi bộ đường dài, ngắm chim và dã ngoại. Do trải trên vùng rộng và chia thành nhiều cụm rừng, du "
     "khách thường lấy Elabuga (hoặc Naberezhnye Chelny) làm điểm xuất phát để vào các khu vực tham quan chính."),
    [
        "Vườn quốc gia ~265 km² (từ 1991) với rừng thông, đồng cỏ và bãi bồi dọc sông Kama.",
        "Rừng «Bolshoy Bor» và «Rừng Thuyền» gần Elabuga — nguồn cảm hứng tranh phong cảnh Ivan Shishkin.",
        "Đường mòn sinh thái, ngắm chim và cảnh quan ven sông cho du lịch thiên nhiên.",
    ],
    {
        "hours_vi": "Khu thiên nhiên ngoài trời; một số tuyến/điểm cần đăng ký với ban quản lý vườn. Nên tìm hiểu trước khi đến.",
        "ticket_vi": "Có thể thu phí vào một số tuyến sinh thái hoặc dịch vụ hướng dẫn; nhiều khu vực rừng vào tự do.",
        "duration_vi": "Nửa ngày đến trọn ngày tuỳ tuyến; thường kết hợp tham quan Elabuga.",
        "best_time_vi": "Cuối xuân đến đầu thu cho đi bộ và ngắm cảnh; mùa thu lá vàng rất đẹp.",
        "tips_vi": "Lấy Elabuga làm điểm xuất phát để tới các rừng thông gắn với Shishkin; mang giày đi rừng, nước và thuốc chống côn trùng. Vườn rộng, nên xác định trước cụm định tham quan.",
    },
    [
        {"title": "Wikipedia (EN) — Nizhnyaya Kama National Park", "url": "https://en.wikipedia.org/wiki/Nizhnyaya_Kama_National_Park"},
        {"title": "Wikipedia (RU) — Нижняя Кама (национальный парк)", "url": "https://ru.wikipedia.org/wiki/Нижняя_Кама_(национальный_парк)"},
    ],
    ["national-park", "nature", "pine-forest", "shishkin", "kama-river", "hiking", "elabuga"],
    maps=maps_text("Национальный парк «Нижняя Кама»", "Елабуга, Республика Татарстан",
                   "Nizhnyaya Kama National Park", "Yelabuga, Tatarstan", 55.801110, 52.323330),
))

# ============================================================ 15
RECORDS.append(rec(
    "chistopol",
    "Thành phố cổ Chistopol và Nhà lưu niệm Boris Pasternak",
    "Чистополь (Мемориальный музей Б. Л. Пастернака)",
    "Chistopol (Boris Pasternak Memorial Museum)",
    ["museum", "other"],
    55.365931, 50.648959,
    "Thành phố Chistopol (Чистополь) bên sông Kama, cách Kazan khoảng 130 km về phía đông nam; bảo tàng Pasternak ở phố Lenin (Ленина), số 81, Cộng hoà Tatarstan.",
    ("Chistopol là một thành phố thương mại cổ bên sông Kama, còn giữ được nhiều dãy phố buôn bán và dinh thự thương gia "
     "thế kỷ 19. Trong Thế chiến II, nhiều nhà văn Xô-viết được sơ tán về đây, trong đó có Boris Pasternak — nay có nhà "
     "lưu niệm mang tên ông. Thành phố còn nổi tiếng với truyền thống chế tác đồng hồ Vostok/Chistopol."),
    ("Nằm bên hữu ngạn sông Kama, Chistopol từng là một trung tâm thương mại và chế biến ngũ cốc sầm uất của vùng, phát "
     "triển mạnh trong thế kỷ 19. Nhờ đó thành phố còn lưu giữ được một quần thể kiến trúc đô thị thương gia khá nguyên "
     "vẹn: các dãy cửa hiệu (trading rows), dinh thự, nhà thờ và công trình công cộng cổ tạo nên không khí một «thành phố "
     "thương gia» điển hình. Chistopol đặc biệt được nhắc đến trong lịch sử văn học Nga: thời Thế chiến II, nơi đây trở "
     "thành điểm sơ tán của nhiều văn nghệ sĩ Xô-viết, trong đó có Boris Pasternak, Nikolai Aseyev và nhiều người khác. "
     "Ngôi nhà nơi Pasternak sống và làm việc những năm 1941–1943 nay là Bảo tàng lưu niệm Boris Pasternak, trưng bày kỷ "
     "vật, bản thảo và tái hiện không gian sáng tác của nhà thơ – nhà văn đoạt giải Nobel. Bên cạnh đó, Chistopol còn nổi "
     "tiếng với nhà máy đồng hồ (thương hiệu Vostok/«Chistopol») từng nổi danh khắp Liên Xô. Với du khách yêu lịch sử và "
     "văn học, Chistopol là một chuyến đi trong ngày thú vị từ Kazan để dạo phố cổ, thăm bảo tàng và cảm nhận nhịp sống "
     "tỉnh lẻ ven sông Kama."),
    [
        "Thành phố thương gia cổ bên sông Kama với dãy cửa hiệu và dinh thự thế kỷ 19 được bảo tồn.",
        "Nhà lưu niệm Boris Pasternak — nơi nhà văn Nobel sơ tán và sáng tác thời Thế chiến II.",
        "Truyền thống chế tác đồng hồ Vostok/«Chistopol» từng nổi danh khắp Liên Xô.",
    ],
    {
        "hours_vi": "Bảo tàng Pasternak thường mở 10:00–17:00, nghỉ đầu tuần (nên kiểm tra trước); phố cổ dạo tự do cả ngày.",
        "ticket_vi": "Vé bảo tàng ở mức thấp; dạo phố cổ miễn phí.",
        "duration_vi": "Khoảng 2–3 giờ trong thành phố (chưa kể ~2–2,5 giờ đường từ Kazan mỗi chiều).",
        "best_time_vi": "Cuối xuân đến đầu thu cho dạo bộ dễ chịu; mùa hè có thể đi lại bằng đường sông.",
        "tips_vi": "Đi tự lái hoặc xe khách từ Kazan; kết hợp thăm phố cổ, bảo tàng Pasternak và bờ sông Kama. Một số mùa có tàu thuỷ nối Kazan – Chistopol.",
    },
    [
        {"title": "Yandex Maps — Мемориальный музей Бориса Пастернака (Чистополь)", "url": "https://yandex.com/maps/org/memorialny_muzey_borisa_pasternaka/1015972522/"},
        {"title": "Wikidata — Chistopol", "url": "https://www.wikidata.org/wiki/Q198102"},
    ],
    ["historic-town", "merchant-architecture", "pasternak", "literature", "wwii-evacuation", "kama-river"],
    maps={
        "yandex": "https://yandex.com/maps/org/memorialny_muzey_borisa_pasternaka/1015972522/",
        "google": _google("Boris Pasternak Memorial Museum", "Chistopol, Tatarstan"),
    },
))

# ============================================================ 16
RECORDS.append(rec(
    "bolgar-white-mosque",
    "Nhà thờ Hồi giáo Trắng ở Bolgar (Belaya mechet, Ak mechet)",
    "Белая мечеть (Ак мечеть)",
    "White Mosque (Ak Mosque), Bolgar",
    ["church"],
    54.966001, 49.061660,
    "Phố Kul Gali (Кул Гали), số 1, thành phố Bolgar, huyện Spassky (Спасский); cách khu di tích Bulgar cổ khoảng 1,5 km về phía nam và cách Kazan khoảng 180 km về phía nam, Cộng hoà Tatarstan.",
    ("Nhà thờ Hồi giáo Trắng là một thánh đường hiện đại bằng đá cẩm thạch trắng, khánh thành năm 2012 tại Bolgar. Với hồ "
     "nước phản chiếu, hàng cột vòm cung và đôi tháp minaret thanh mảnh, công trình thường được ví như «Taj Mahal của "
     "người Tatar». Đây là điểm nhấn tâm linh mới bên cạnh khu di tích Bulgar cổ được UNESCO công nhận."),
    ("Nhà thờ Hồi giáo Trắng (Belaya mechet) là một công trình tôn giáo hiện đại, hoàn thành năm 2012, nằm ở rìa nam thành "
     "phố Bolgar — vùng đất gắn với cái nôi Hồi giáo của người Bulgar Volga. Được xây dựng bằng đá cẩm thạch trắng, thánh "
     "đường lấy cảm hứng từ kiến trúc Hồi giáo cổ điển (gợi liên tưởng tới các thánh đường Trung Á và Trung Đông), với "
     "mái vòm trắng, đôi tháp minaret cao thanh thoát và một sân trong bao quanh bởi hàng cột vòm cung. Trước thánh đường "
     "là hồ nước phẳng lặng phản chiếu toàn bộ công trình, tạo nên khung cảnh đối xứng lộng lẫy khiến nhiều người ví von "
     "đây là «Taj Mahal của người Tatar» — một trong những địa điểm được chụp ảnh nhiều nhất Tatarstan. Nhà thờ Trắng "
     "nằm trong tổng thể phục hưng Bolgar thành trung tâm hành hương và du lịch Hồi giáo: cách đó khoảng 1,5 km về phía "
     "bắc là Khu bảo tồn lịch sử – khảo cổ Bulgar cổ (Di sản Thế giới UNESCO) với các di tích thế kỷ 13–14. Cần lưu ý đây "
     "là công trình mới, tách biệt và khác hẳn với cụm di tích cổ; du khách thường tham quan cả hai trong cùng một hành "
     "trình tới Bolgar."),
    [
        "Thánh đường đá cẩm thạch trắng hiện đại (khánh thành 2012) với hồ nước phản chiếu và đôi tháp minaret.",
        "Được ví như «Taj Mahal của người Tatar» — một trong những điểm chụp ảnh đẹp nhất Tatarstan.",
        "Nằm trong tổng thể phục hưng Bolgar, cách khu di tích Bulgar cổ (UNESCO) khoảng 1,5 km.",
    ],
    {
        "hours_vi": "Mở cửa cho khách tham quan hằng ngày (thường khoảng 9:00–19:00); giờ có thể thay đổi theo giờ cầu nguyện và mùa.",
        "ticket_vi": "Vào tham quan tự do (miễn phí); quyên góp tuỳ tâm.",
        "duration_vi": "Khoảng 45–60 phút (thường kết hợp tham quan khu Bulgar cổ).",
        "best_time_vi": "Cuối xuân đến đầu thu; sáng sớm hoặc chiều muộn khi mặt hồ phẳng lặng cho ảnh phản chiếu đẹp.",
        "tips_vi": "Ăn mặc kín đáo, cởi giày và nữ trùm khăn khi vào khu cầu nguyện. Kết hợp tham quan Khu bảo tồn Bulgar cổ (UNESCO) gần đó; tới Bolgar tiện nhất bằng tàu thuỷ mùa hè hoặc ô tô từ Kazan.",
    },
    [
        {"title": "Wikidata — White Mosque (Bolgar)", "url": "https://www.wikidata.org/wiki/Q28667373"},
        {"title": "2GIS — Белая мечеть (Болгар)", "url": "https://2gis.ru/bolgar/firm/70000001054313737"},
    ],
    ["mosque", "modern", "white-marble", "bolgar", "islam", "reflecting-pool"],
))


# ------------------------------------------------------------------ WRITE
def main():
    fname = f"{RID}.json"
    path = os.path.join(REGIONS, fname)
    arr = json.load(open(path, encoding="utf-8"))
    existing_slugs = {p.get("slug") for p in arr}
    existing_ids = {p.get("id") for p in arr}
    before = len(arr)

    to_add = []
    for r in RECORDS:
        if r["slug"] in existing_slugs or r["id"] in existing_ids:
            print(f"  = BỎ QUA (đã có): {r['slug']}")
            continue
        # sanity toạ độ
        lat, lon = r["coordinates"]["lat"], r["coordinates"]["lon"]
        assert 41 <= lat <= 70 and 19 <= lon <= 180, f"TOẠ ĐỘ NGHI NGỜ: {r['slug']} {lat},{lon}"
        to_add.append(r)

    if not to_add:
        print("Không có gì để thêm.")
        return

    bak = path + f".bak_add_{TS}"
    with open(bak, "w", encoding="utf-8") as f:
        json.dump(arr, f, ensure_ascii=False, indent=2)
    arr.extend(to_add)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(arr, f, ensure_ascii=False, indent=2)

    print(f"VÙNG TIÊU ĐIỂM: {RID} ({RNAME_VI})")
    print(f"  + Thêm {len(to_add)} địa điểm: {before} -> {len(arr)}  (backup: {os.path.basename(bak)})")
    for r in to_add:
        print(f"        - {r['name_vi']}  [{','.join(r['categories'])}]  ({r['coordinates']['lat']},{r['coordinates']['lon']})")


if __name__ == "__main__":
    main()
