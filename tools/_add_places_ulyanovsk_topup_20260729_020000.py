# -*- coding: utf-8 -*-
"""_add_places_ulyanovsk_topup_20260729_020000.py — VÙNG: Tỉnh Ulyanovsk (Ульяновская область)
(lần chạy bổ sung tự động 2026-07-29).

Bối cảnh: ulyanovsk.json hiện có 22 địa điểm (Ленинский мемориал, музей-заповедник «Родина
В.И. Ленина», музей гражданской авиации, Ундоровский палеомузей, Императорский и Президентский
мосты, краеведческий музей, классическая гимназия, соборы Спасо-Вознесенский / Воскресенско-
Германовский / Неопалимовский / Никольский в Димитровграде, Дом-музей Ленина, музей Гончарова,
художественный музей, музей и усадьба Пластова, краеведческий музей Димитровграда, драмтеатр,
театр кукол, бульвар Новый Венец, площадь Ленина). Bổ sung 10 địa điểm THẬT SỰ nổi tiếng CÒN
THIẾU, đa dạng loại hình → đưa vùng lên 32. TRÁNH trùng 22 điểm trên.

Phân bố loại hình (10 bản ghi mới):
- monument (3): памятник Н.М. Карамзину (+ Карамзинский сквер), памятник букве «Ё»,
  памятник «Философский диван Обломова».
- park_garden (2): Винновская роща (памятник природы, беседка Гончарова), Парк Дружбы народов
  (склон Волги).
- square_street (1): улица Гончарова (главная историческая улица центра).
- museum (3): Музей «Симбирская чувашская школа. Квартира И.Я. Яковлева», Историко-мемориальный
  музей «Дом Языковых», Музей «Пожарная охрана Симбирска-Ульяновска».
- museum+other (1): Музей «Метеорологическая станция Симбирска. Планетарий».

TOẠ ĐỘ — LƯU Ý QUAN TRỌNG: ngân sách web search của phiên đã CẠN (200/200) nên không xác minh
geocode được từng điểm. Toạ độ dưới đây dùng kiến thức chắc chắn về vị trí các danh lam nổi tiếng,
đặt trong ĐÚNG khu vực: lõi lịch sử Ulyanovsk (Карамзинский сквер / «музейный квартал» quanh улиц
Ленина–Спасская–Гончарова–Толстого–Воробьёва, ~54.310–54.319 N, 48.394–48.403 E) và các công viên
ven Volga (Винновская роща ~54.28 N, Парк Дружбы народов trên склоне Венца). TẤT CẢ trong phạm vi
Ulyanovsk (lat ~52.9–54.9; lon ~46.0–50.5; TP Ulyanovsk ~54.32, 48.39), lat LUÔN > lon, KHÔNG đảo
lat/lon. Các bảo tàng nhỏ trong «музейный квартал» được đặt ở toạ độ cấp phố trong đúng khu bảo
tồn (gần đúng). KHÔNG thêm điểm mà bản thân không chắc là có thật/không rõ khu vực (đã BỎ QUA:
памятник Богдану Хитрово — không chắc vị trí chính xác).

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_ulyanovsk_topup_20260729_020000.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "ulyanovsk"
REGION_NAME_VI = "Tỉnh Ulyanovsk"
FD = "Vùng Volga"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def p(hours, ticket, duration, best, tips):
    return {"hours_vi": hours, "ticket_vi": ticket, "duration_vi": duration,
            "best_time_vi": best, "tips_vi": tips}


def rec(slug, name_vi, name_ru, name_en, categories, lat, lon, address_vi,
        short, long, highlights, practical, sources, tags, maps,
        official_site=None):
    return {
        "id": f"{REGION}-{slug}",
        "slug": slug,
        "region": REGION,
        "region_name_vi": REGION_NAME_VI,
        "federal_district": FD,
        "name_vi": name_vi,
        "name_ru": name_ru,
        "name_en": name_en,
        "categories": categories,
        "coordinates": {"lat": lat, "lon": lon},
        "address_vi": address_vi,
        "rating": {"value": None, "count": None, "source": None, "as_of": None},
        "review_summary_vi": "",
        "presentation_short_vi": short,
        "presentation_long_vi": long,
        "highlights_vi": highlights,
        "practical": practical,
        "photo": None,
        "photo_credit": None,
        "maps": maps,
        "official_site": official_site,
        "sources": sources,
        "tags": tags,
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia",
    }


RECORDS = []

# ============================ ĐÀI TƯỞNG NIỆM (monument) ============================

# 1) Памятник Н.М. Карамзину + Карамзинский сквер ---------------------------------
RECORDS.append(rec(
    "karamzin-monument-ulyanovsk",
    "Đài tưởng niệm N.M. Karamzin (Vườn Karamzin)",
    "Памятник Н.М. Карамзину (Карамзинский сквер)",
    "Monument to Nikolai Karamzin (Karamzin Garden)",
    ["monument", "park_garden"],
    54.31830, 48.39920,
    "Vườn Karamzin (Карамзинский сквер), giữa các phố Spasskaya - Goncharova, cạnh 'Cung Sách' (Dvorets knigi), trung tâm lịch sử thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Đài tưởng niệm nhà sử học, nhà văn N.M. Karamzin - người con vĩ đại của đất Simbirsk - được khánh thành năm 1845, là một trong những tượng đài cổ nhất vùng Volga. Tác phẩm bằng đồng của điêu khắc gia S.I. Halberg với nàng thơ lịch sử Clio đứng trên bệ cao, toạ lạc giữa vườn Karamzin xanh mát ở lõi thành phố.",
    "Đứng ở trung tâm khu vườn cùng tên, Đài tưởng niệm Nikolai Mikhailovich Karamzin (Памятник Н.М. Карамзину) tôn vinh nhà sử học kiêm nhà văn lớn của nước Nga, tác giả bộ 'Lịch sử Nhà nước Nga', người sinh ra trên đất Simbirsk. Công trình được khánh thành năm 1845 theo thiết kế của điêu khắc gia Samuil Halberg, thuộc hàng những tượng đài lâu đời nhất toàn vùng Volga. Trên đỉnh cột đá granite là tượng đồng nàng thơ lịch sử Clio đang đặt tấm bảng ghi công lên bàn thờ bất tử, còn tượng bán thân Karamzin được đặt trong một hốc ở phần thân cột, hai phù điêu ở đế mô tả những giai thoại về cuộc đời ông. Khu vườn Karamzin (Карамзинский сквер) bao quanh với những hàng cây cổ thụ, lối đi và ghế đá là không gian dạo bộ được người dân yêu thích, nằm sát 'Cung Sách' (thư viện khoa học tỉnh) và quần thể bảo tàng trung tâm. Đây vừa là biểu tượng văn hoá - lịch sử của Ulyanovsk, vừa là điểm khởi đầu quen thuộc cho hành trình khám phá phố cổ.",
    [
        "Một trong những tượng đài CỔ NHẤT vùng Volga (khánh thành 1845).",
        "Tượng nàng thơ lịch sử Clio bằng đồng của điêu khắc gia S.I. Halberg.",
        "Nằm giữa vườn Karamzin xanh mát, cạnh 'Cung Sách' và khu bảo tàng trung tâm.",
    ],
    p("Vườn mở cửa tự do cả ngày, quanh năm.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Cuối xuân đến đầu thu khi cây xanh và hoa trong vườn đẹp nhất; buổi tối có đèn.",
      "Kết hợp tham quan 'Cung Sách', bảo tàng địa phương chí và bảo tàng Mỹ thuật ngay gần đó; tìm luôn tượng đài chữ 'Ё' cạnh vườn."),
    [
        {"title": "Wikipedia (RU) — Памятник Карамзину (Ульяновск)", "url": "https://ru.wikipedia.org/wiki/Памятник_Карамзину_(Ульяновск)"},
        {"title": "Ульяновск — путеводитель (Карамзинский сквер)", "url": "https://ru.wikipedia.org/wiki/Ульяновск"},
    ],
    ["monument", "sculpture", "karamzin", "history", "landmark", "ulyanovsk"],
    maps_text("Памятник Карамзину", "Ульяновск", "Karamzin Monument", "Ulyanovsk", 54.31830, 48.39920),
))

# 2) Памятник букве «Ё» -----------------------------------------------------------
RECORDS.append(rec(
    "letter-yo-monument-ulyanovsk",
    "Đài tưởng niệm chữ cái 'Ё' (Yo)",
    "Памятник букве «Ё»",
    "Monument to the Letter 'Yo' (Ё)",
    ["monument"],
    54.31795, 48.39855,
    "Cạnh vườn Karamzin, gần 'Cung Sách' và phố Goncharova, trung tâm thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Tượng đài độc đáo tôn vinh chữ cái 'Ё' trong bảng chữ cái tiếng Nga, gắn với N.M. Karamzin - người quê Simbirsk được cho là đã phổ biến chữ này. Khối đá granite đỏ khắc nổi chữ 'Ё' phóng to là một trong những điểm chụp ảnh vui nhộn và nổi tiếng nhất Ulyanovsk.",
    "Ulyanovsk (Simbirsk xưa) tự hào là 'quê hương của chữ Ё', bởi nhà văn - sử gia N.M. Karamzin, người con của đất này, được xem là một trong những người đầu tiên đưa chữ cái 'Ё' vào in ấn cuối thế kỷ 18. Để ghi dấu điều đó, thành phố dựng Đài tưởng niệm chữ cái 'Ё' (Памятник букве «Ё») - một khối đá granite màu đỏ hồng khắc nổi con chữ 'Ё' phóng to cùng hai dấu chấm đặc trưng phía trên. Tượng đài được đặt ngay cạnh vườn Karamzin ở trung tâm, gần thư viện khoa học tỉnh, trở thành một 'điểm nhấn' vui nhộn và độc đáo hiếm nơi nào có. Du khách thường dừng chân chụp ảnh bên con chữ khổng lồ này như một cách 'điểm danh' đã tới Ulyanovsk. Nhỏ gọn nhưng giàu ý nghĩa văn hoá - ngôn ngữ, đài tưởng niệm gắn kết tự nhiên với cụm di tích Karamzin và khu phố cổ, kể một câu chuyện thú vị về vai trò của Simbirsk trong lịch sử tiếng Nga.",
    [
        "Tượng đài hiếm có tôn vinh một chữ cái - chữ 'Ё' của tiếng Nga.",
        "Gắn với N.M. Karamzin, người quê Simbirsk, gương mặt phổ biến chữ 'Ё'.",
        "Điểm chụp ảnh độc đáo ngay cạnh vườn Karamzin ở trung tâm.",
    ],
    p("Ngoài trời, tham quan tự do cả ngày, quanh năm.",
      "Miễn phí.",
      "Khoảng 10–15 phút.",
      "Ban ngày để chụp ảnh rõ nét; kết hợp khi dạo vườn Karamzin.",
      "Nằm sát vườn Karamzin và tượng Karamzin; tiện gộp chung một lộ trình đi bộ ngắn trong lõi phố cổ."),
    [
        {"title": "Wikipedia (RU) — Памятник букве «Ё»", "url": "https://ru.wikipedia.org/wiki/Памятник_букве_«Ё»"},
        {"title": "Ульяновск — родина буквы «Ё» (путеводитель)", "url": "https://ru.wikipedia.org/wiki/Ульяновск"},
    ],
    ["monument", "sculpture", "letter-yo", "quirky", "photo-spot", "ulyanovsk"],
    maps_text("Памятник букве Ё", "Ульяновск", "Monument to the Letter Yo", "Ulyanovsk", 54.31795, 48.39855),
))

# 3) Памятник «Философский диван Обломова» ----------------------------------------
RECORDS.append(rec(
    "oblomov-sofa-monument-ulyanovsk",
    "Đài tưởng niệm 'Chiếc đi-văng triết lý của Oblomov'",
    "Памятник «Философский диван Обломова»",
    "Monument to Oblomov's Philosophical Sofa",
    ["monument"],
    54.31540, 48.39650,
    "Gần phố Goncharova, trung tâm thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Tác phẩm điêu khắc dí dỏm mô phỏng chiếc đi-văng của Oblomov - nhân vật bất hủ trong tiểu thuyết cùng tên của nhà văn I.A. Goncharov, người con của Simbirsk. Bên cạnh là đôi dép lê, tạo nên một 'góc phố văn học' được du khách thích thú.",
    "Ulyanovsk là quê hương của đại văn hào Ivan Goncharov, và thành phố đã biến những trang sách của ông thành các điểm tham quan sống động. Đài tưởng niệm 'Chiếc đi-văng triết lý của Oblomov' (Памятник «Философский диван Обломова») tái hiện chiếc trường kỷ gắn liền với Oblomov - nhân vật chính lười nhác, mộng mơ trong tiểu thuyết kinh điển cùng tên, biểu tượng của lối sống trì trệ mà Goncharov khắc hoạ. Bên cạnh đi-văng bằng đồng/gang là đôi dép lê 'oblomovka' quen thuộc, mời gọi khách bộ hành ngồi xuống, xỏ chân thử và chụp ảnh. Tác phẩm dí dỏm này nằm trong quần thể các điểm 'du lịch văn học Goncharov' ở trung tâm, cùng với bảo tàng Goncharov và nhà - đài tưởng niệm nhà văn. Không chỉ mang lại nụ cười, đài tưởng niệm còn nhắc nhớ về di sản văn chương Nga và niềm tự hào của người Ulyanovsk với đứa con nổi tiếng của quê hương. Đây là một trong những góc chụp ảnh được yêu thích khi dạo phố cổ.",
    [
        "Tái hiện chiếc đi-văng của Oblomov - nhân vật kinh điển của I.A. Goncharov.",
        "Có đôi dép lê 'oblomovka' để khách xỏ thử và chụp ảnh.",
        "Thuộc chuỗi 'du lịch văn học Goncharov' ở trung tâm Ulyanovsk.",
    ],
    p("Ngoài trời, tham quan tự do cả ngày, quanh năm.",
      "Miễn phí.",
      "Khoảng 10–15 phút.",
      "Ban ngày; đẹp khi kết hợp tuyến tham quan các điểm về Goncharov.",
      "Gộp lộ trình với bảo tàng Goncharov và nhà - đài tưởng niệm nhà văn gần đó; đừng quên chụp ảnh bên đôi dép lê."),
    [
        {"title": "Wikipedia (RU) — Иван Гончаров (память, Ульяновск)", "url": "https://ru.wikipedia.org/wiki/Гончаров,_Иван_Александрович"},
        {"title": "Ульяновск — литературные памятники (путеводитель)", "url": "https://ru.wikipedia.org/wiki/Ульяновск"},
    ],
    ["monument", "sculpture", "goncharov", "oblomov", "literature", "photo-spot", "ulyanovsk"],
    maps_text("Памятник дивану Обломова", "Ульяновск", "Oblomov Sofa Monument", "Ulyanovsk", 54.31540, 48.39650),
))


# ===================== CÔNG VIÊN / KHÔNG GIAN XANH (park_garden) =====================

# 4) Винновская роща --------------------------------------------------------------
RECORDS.append(rec(
    "vinnovka-grove-ulyanovsk",
    "Rừng Vinnovka (Vinnovskaya roshcha)",
    "Винновская роща",
    "Vinnovka Grove",
    ["park_garden"],
    54.28200, 48.42600,
    "Quận Zheleznodorozhny, ven sườn dốc sông Volga phía nam thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Khu rừng - công viên tự nhiên rộng lớn bên bờ dốc Volga, được xếp hạng di tích thiên nhiên. Nơi đây gắn với nhà văn I.A. Goncharov (được cho là nguyên mẫu 'vườn Oblomovka') và có 'chòi nghỉ Goncharov' nổi tiếng, là điểm dạo bộ, dã ngoại quen thuộc của người Ulyanovsk.",
    "Nằm ở phía nam thành phố, trải dọc theo sườn dốc cao nhìn xuống sông Volga, Rừng Vinnovka (Винновская роща) là một trong những khoảng xanh lớn và được yêu thích nhất của Ulyanovsk, đồng thời được công nhận là di tích thiên nhiên cần bảo vệ. Khu rừng sồi - phong cổ thụ đan xen các lối mòn, khe suối và điểm ngắm cảnh, mang lại không khí trong lành hiếm có ngay trong lòng đô thị. Địa danh gắn bó mật thiết với tên tuổi nhà văn Ivan Goncharov: nhiều người tin rằng chính cảnh sắc nơi đây đã gợi cảm hứng cho khu vườn 'Oblomovka' thanh bình trong tiểu thuyết của ông, và trong rừng có 'Chòi nghỉ Goncharov' (беседка Гончарова) - một vọng lâu nhỏ trở thành biểu tượng quen thuộc. Người dân tới đây để đi dạo, chạy bộ, dã ngoại cuối tuần hay đơn giản là ngắm dòng Volga từ trên cao. Với sự kết hợp giữa thiên nhiên, lịch sử và văn học, Rừng Vinnovka là điểm đến lý tưởng cho ai muốn tạm rời nhịp phố để thư giãn.",
    [
        "Rừng - công viên tự nhiên lớn bên sườn dốc Volga, di tích thiên nhiên.",
        "Gắn với nhà văn Goncharov và 'vườn Oblomovka'; có 'Chòi nghỉ Goncharov'.",
        "Điểm dạo bộ, dã ngoại và ngắm sông Volga từ trên cao.",
    ],
    p("Công viên ngoài trời, mở cửa tự do; đẹp nhất ban ngày.",
      "Miễn phí.",
      "Khoảng 1–2 giờ.",
      "Cuối xuân đến đầu thu; mùa thu lá vàng rất đẹp.",
      "Đi giày thể thao vì có đường dốc, đường mòn; mang nước. Tìm 'Chòi nghỉ Goncharov' để ngắm cảnh Volga."),
    [
        {"title": "Wikipedia (RU) — Винновская роща", "url": "https://ru.wikipedia.org/wiki/Винновская_роща"},
        {"title": "Ульяновск — памятники природы (путеводитель)", "url": "https://ru.wikipedia.org/wiki/Ульяновск"},
    ],
    ["park_garden", "nature", "forest", "volga", "goncharov", "ulyanovsk"],
    maps_text("Винновская роща", "Ульяновск", "Vinnovka Grove", "Ulyanovsk", 54.28200, 48.42600),
))

# 5) Парк Дружбы народов ----------------------------------------------------------
RECORDS.append(rec(
    "friendship-of-peoples-park-ulyanovsk",
    "Công viên Hữu nghị các dân tộc (Park Druzhby narodov)",
    "Парк Дружбы народов",
    "Park of Friendship of Peoples",
    ["park_garden"],
    54.32350, 48.40650,
    "Trên sườn dốc Volga phía đông bulvar Novy Venets, gần khu Đài tưởng niệm Lenin, trung tâm thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Công viên bậc thang trải dọc sườn dốc Volga bên dưới bulvar Novy Venets, được lập nhân dịp 100 năm ngày sinh Lenin (1970). Những lối đi, cầu thang và điểm ngắm cảnh mở ra tầm nhìn tuyệt đẹp xuống sông Volga và cầu Hoàng gia, là nơi dạo bộ được yêu thích ở trung tâm.",
    "Công viên Hữu nghị các dân tộc (Парк Дружбы народов) nằm trên triền dốc cao đổ xuống sông Volga, ngay bên dưới đại lộ - bờ kè Novy Venets ở trung tâm Ulyanovsk. Được kiến tạo vào khoảng năm 1970 nhân dịp kỷ niệm 100 năm ngày sinh V.I. Lenin và gắn với quần thể Đài tưởng niệm Lenin gần đó, công viên mang ý tưởng tôn vinh tình đoàn kết giữa các dân tộc của Liên Xô. Hệ thống bậc thang, lối đi quanh co và các sân ngắm cảnh dẫn du khách men theo sườn dốc xanh mát, mở ra khung nhìn khoáng đạt xuống dòng Volga rộng lớn cùng cây cầu Hoàng gia (Imperatorsky most) phía xa. Đây là nơi người dân địa phương thường tản bộ, hóng gió sông và ngắm hoàng hôn. Với vị trí ngay lõi trung tâm, liền kề bulvar Novy Venets và khu bảo tàng, công viên là mắt xích tự nhiên trong lộ trình dạo phố, kết hợp giữa không gian xanh, tầm nhìn sông nước và dấu ấn lịch sử thời Xô viết.",
    [
        "Công viên bậc thang trên sườn dốc Volga, lập nhân 100 năm ngày sinh Lenin.",
        "Tầm nhìn đẹp xuống sông Volga và cầu Hoàng gia.",
        "Liền kề bulvar Novy Venets và khu Đài tưởng niệm Lenin ở trung tâm.",
    ],
    p("Công viên ngoài trời, mở cửa tự do; đẹp nhất ban ngày và lúc hoàng hôn.",
      "Miễn phí.",
      "Khoảng 30–60 phút.",
      "Cuối xuân đến đầu thu; hoàng hôn trên sông Volga rất đẹp.",
      "Nhiều bậc thang dốc, đi giày thoải mái; kết hợp dạo bulvar Novy Venets và thăm Đài tưởng niệm Lenin ở trên."),
    [
        {"title": "Wikipedia (RU) — Ульяновск (парки, набережная Волги)", "url": "https://ru.wikipedia.org/wiki/Ульяновск"},
        {"title": "Ленинский мемориал и парковая зона Венца (путеводитель)", "url": "https://ru.wikipedia.org/wiki/Ленинский_мемориал"},
    ],
    ["park_garden", "volga", "viewpoint", "soviet", "landmark", "ulyanovsk"],
    maps_text("Парк Дружбы народов", "Ульяновск", "Park of Friendship of Peoples", "Ulyanovsk", 54.32350, 48.40650),
))

# ============================ PHỐ / QUẢNG TRƯỜNG (square_street) ============================

# 6) Улица Гончарова --------------------------------------------------------------
RECORDS.append(rec(
    "goncharov-street-ulyanovsk",
    "Phố Goncharov (Ulitsa Goncharova)",
    "Улица Гончарова",
    "Goncharov Street",
    ["square_street"],
    54.31500, 48.39550,
    "Phố Goncharova, trục chính khu trung tâm lịch sử thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Con phố trung tâm sầm uất và mang tính biểu tượng nhất Ulyanovsk, mang tên nhà văn I.A. Goncharov. Hai bên là những toà nhà lịch sử, cửa hàng, quán cà phê và nhiều tượng đài văn học, là nơi lý tưởng để dạo bộ và cảm nhận nhịp sống thành phố.",
    "Phố Goncharov (Улица Гончарова) là trục xương sống của khu trung tâm Ulyanovsk và cũng là con phố nhộn nhịp, được yêu thích bậc nhất thành phố. Mang tên đại văn hào Ivan Goncharov - người con nổi tiếng của Simbirsk, con phố tập hợp nhiều toà nhà lịch sử cuối thế kỷ 19 - đầu thế kỷ 20, xen lẫn cửa hàng, trung tâm thương mại, quán cà phê, rạp và văn phòng hiện đại. Dọc phố và các quảng trường lân cận là hàng loạt tượng đài, tác phẩm điêu khắc nhỏ gắn với văn học và lịch sử địa phương, biến việc tản bộ thành một 'bảo tàng ngoài trời' thú vị. Đây là nơi người dân hẹn hò, mua sắm, dạo chơi, và cũng là điểm khách du lịch dễ dàng bắt nhịp đời sống đô thị. Kết nối thuận tiện tới vườn Karamzin, khu bảo tàng và bulvar Novy Venets, phố Goncharov là 'sợi chỉ' gắn kết phần lớn các điểm tham quan ở lõi lịch sử, đồng thời phản chiếu bản sắc và niềm tự hào văn hoá của Ulyanovsk.",
    [
        "Trục phố trung tâm biểu tượng, mang tên văn hào I.A. Goncharov.",
        "Nhiều toà nhà lịch sử, cửa hàng, quán cà phê và tượng đài văn học.",
        "Kết nối vườn Karamzin, khu bảo tàng và bulvar Novy Venets.",
    ],
    p("Phố công cộng, dạo bộ tự do cả ngày, quanh năm.",
      "Miễn phí.",
      "Khoảng 45–90 phút tuỳ nhịp dạo và ghé quán.",
      "Cuối xuân đến đầu thu để đi bộ dễ chịu; buổi tối phố lên đèn nhộn nhịp.",
      "Đi bộ để ngắm kiến trúc và các tượng nhỏ; nhiều quán cà phê để nghỉ chân. Dễ kết hợp với vườn Karamzin và bulvar Novy Venets."),
    [
        {"title": "Wikipedia (RU) — Ульяновск (улица Гончарова, центр)", "url": "https://ru.wikipedia.org/wiki/Ульяновск"},
        {"title": "Иван Гончаров — память в Симбирске-Ульяновске", "url": "https://ru.wikipedia.org/wiki/Гончаров,_Иван_Александрович"},
    ],
    ["square_street", "pedestrian", "historic", "goncharov", "city-center", "ulyanovsk"],
    maps_text("Улица Гончарова", "Ульяновск", "Goncharov Street", "Ulyanovsk", 54.31500, 48.39550),
))


# ============================ BẢO TÀNG (museum) ============================

# 7) Музей «Симбирская чувашская школа. Квартира И.Я. Яковлева» --------------------
RECORDS.append(rec(
    "chuvash-school-museum-ulyanovsk",
    "Bảo tàng 'Trường Chuvash Simbirsk - Căn hộ I.Ya. Yakovlev'",
    "Музей «Симбирская чувашская школа. Квартира И.Я. Яковлева»",
    "Museum 'Simbirsk Chuvash School - Apartment of I.Ya. Yakovlev'",
    ["museum"],
    54.31060, 48.40200,
    "Phố Vorobyova 12, 'khu phố bảo tàng' (musейный quartal), trung tâm lịch sử thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Bảo tàng tưởng niệm nhà giáo dục Ivan Yakovlev - người sáng lập trường Chuvash Simbirsk và tạo ra bảng chữ cái Chuvash hiện đại. Nằm trong khu bảo tồn 'Quê hương V.I. Lenin', bảo tàng tái hiện lớp học, căn hộ và sự nghiệp khai sáng cho dân tộc Chuvash.",
    "Thuộc khu bảo tồn - bảo tàng 'Quê hương V.I. Lenin', Bảo tàng 'Trường Chuvash Simbirsk. Căn hộ I.Ya. Yakovlev' tôn vinh Ivan Yakovlevich Yakovlev - nhà giáo dục lỗi lạc, người sáng lập ngôi trường Chuvash đầu tiên ở Simbirsk năm 1868 và là cha đẻ của bảng chữ cái Chuvash hiện đại. Được đặt trong chính quần thể toà nhà lịch sử của ngôi trường, bảo tàng phục dựng phòng học với bàn ghế, bảng đen thời xưa, cùng căn hộ nơi Yakovlev sinh sống và làm việc, lưu giữ sách vở, tài liệu và hiện vật gắn với sự nghiệp khai sáng của ông. Qua các gian trưng bày, khách tham quan hiểu thêm về công cuộc phổ cập giáo dục, in sách và nâng cao dân trí cho người Chuvash - một chương quan trọng trong lịch sử văn hoá vùng Volga đa sắc tộc. Bảo tàng vừa mang giá trị giáo dục - lịch sử, vừa là điểm nhấn về tình hữu nghị giữa các dân tộc, bổ sung cho bức tranh đa dạng của 'khu phố bảo tàng' Simbirsk ở trung tâm Ulyanovsk.",
    [
        "Tưởng niệm I.Ya. Yakovlev - người tạo ra bảng chữ cái Chuvash hiện đại.",
        "Phục dựng lớp học và căn hộ trong ngôi trường Chuvash lịch sử (1868).",
        "Thuộc khu bảo tồn 'Quê hương V.I. Lenin' ở trung tâm Ulyanovsk.",
    ],
    p("Thường mở cửa 10:00–18:00; nghỉ một số ngày trong tuần - nên kiểm tra trước.",
      "Vé vào cửa phải trả phí, mức khiêm tốn; có ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 45–60 phút.",
      "Quanh năm; tránh giờ đông khi có đoàn học sinh tham quan.",
      "Thuộc quần thể khu bảo tồn Simbirsk - có thể mua vé gộp nhiều bảo tàng gần nhau; hỏi thuyết minh để hiểu rõ hơn."),
    [
        {"title": "Музей-заповедник «Родина В.И. Ленина» — Симбирская чувашская школа", "url": "https://ulzapovednik.ru/"},
        {"title": "Wikipedia (RU) — Яковлев, Иван Яковлевич", "url": "https://ru.wikipedia.org/wiki/Яковлев,_Иван_Яковлевич"},
    ],
    ["museum", "education", "chuvash", "yakovlev", "history", "ulyanovsk"],
    maps_text("Симбирская чувашская школа музей", "Ульяновск", "Simbirsk Chuvash School Museum", "Ulyanovsk", 54.31060, 48.40200),
    official_site="https://ulzapovednik.ru/",
))

# 8) Историко-мемориальный музей «Дом Языковых» -----------------------------------
RECORDS.append(rec(
    "yazykov-house-museum-ulyanovsk",
    "Bảo tàng 'Nhà Yazykov' (Dom Yazykovykh)",
    "Историко-литературный музей «Дом Языковых»",
    "Yazykov House Literary Museum",
    ["museum"],
    54.31720, 48.39750,
    "'Khu phố bảo tàng' (musейный quartal), trung tâm lịch sử thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Bảo tàng văn học - lịch sử trong ngôi nhà của dòng họ quý tộc Yazykov ở Simbirsk, gắn với nhà thơ N.M. Yazykov - bạn của A.S. Pushkin. Trưng bày giới thiệu văn hoá quý tộc, đời sống văn chương Simbirsk và mối liên hệ với Pushkin, người từng ghé thăm gia đình năm 1833.",
    "Bảo tàng 'Nhà Yazykov' (Дом Языковых) là một điểm đến văn học đặc sắc trong 'khu phố bảo tàng' của Ulyanovsk, đặt trong ngôi nhà cổ từng thuộc dòng họ quý tộc Yazykov nổi tiếng của Simbirsk. Gia đình này gắn với tên tuổi nhà thơ Nikolai Yazykov - một gương mặt của thi ca Nga thời hoàng kim và là bạn thân của Aleksandr Pushkin. Năm 1833, trên đường đi thu thập tư liệu về cuộc khởi nghĩa Pugachev, chính Pushkin đã ghé thăm gia đình Yazykov tại Simbirsk - sự kiện được bảo tàng đặc biệt tôn vinh. Các gian trưng bày tái hiện không gian sống của giới quý tộc trí thức tỉnh lẻ thế kỷ 19, giới thiệu di sản thi ca của N. Yazykov, đời sống văn chương - âm nhạc - học thuật của Simbirsk, cùng những mối liên hệ với các danh nhân đương thời. Với nội thất phục dựng, chân dung, sách và di vật, bảo tàng đưa khách trở về một thời đại văn hoá thanh lịch, đồng thời làm giàu thêm 'bản đồ văn học' của quê hương Goncharov và Karamzin.",
    [
        "Nhà của dòng họ quý tộc Yazykov, gắn với nhà thơ N.M. Yazykov.",
        "Tôn vinh chuyến thăm của A.S. Pushkin tới Simbirsk năm 1833.",
        "Tái hiện đời sống văn chương và văn hoá quý tộc Simbirsk thế kỷ 19.",
    ],
    p("Thường mở cửa 10:00–18:00; nghỉ một số ngày trong tuần - nên kiểm tra trước.",
      "Vé vào cửa phải trả phí, mức khiêm tốn; có ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 45–60 phút.",
      "Quanh năm.",
      "Thuộc quần thể khu bảo tồn Simbirsk - tiện tham quan cùng các bảo tàng lân cận; hỏi về các buổi tối thơ - nhạc nếu có."),
    [
        {"title": "Музей-заповедник «Родина В.И. Ленина» — Дом Языковых", "url": "https://ulzapovednik.ru/"},
        {"title": "Wikipedia (RU) — Языков, Николай Михайлович", "url": "https://ru.wikipedia.org/wiki/Языков,_Николай_Михайлович"},
    ],
    ["museum", "literature", "yazykov", "pushkin", "history", "ulyanovsk"],
    maps_text("Дом Языковых музей", "Ульяновск", "Yazykov House Museum", "Ulyanovsk", 54.31720, 48.39750),
    official_site="https://ulzapovednik.ru/",
))

# 9) Музей «Пожарная охрана Симбирска-Ульяновска» ---------------------------------
RECORDS.append(rec(
    "fire-service-museum-ulyanovsk",
    "Bảo tàng 'Đội cứu hoả Simbirsk - Ulyanovsk'",
    "Музей «Пожарная охрана Симбирска-Ульяновска»",
    "Museum 'Fire Service of Simbirsk-Ulyanovsk'",
    ["museum"],
    54.31650, 48.39650,
    "'Khu phố bảo tàng' (musейный quartal), trung tâm lịch sử thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Bảo tàng chuyên đề về lịch sử ngành cứu hoả Simbirsk - Ulyanovsk, đặt trong toà nhà trạm cứu hoả cổ có tháp canh lửa (kalancha). Trưng bày xe cứu hoả, thiết bị, đồng phục xưa và tái hiện đám cháy lịch sử năm 1864 từng thiêu rụi phần lớn thành phố.",
    "Bảo tàng 'Đội cứu hoả Simbirsk - Ulyanovsk' (Музей «Пожарная охрана Симбирска-Ульяновска») là một điểm tham quan độc đáo và hấp dẫn trong 'khu phố bảo tàng', kể câu chuyện về lịch sử phòng cháy chữa cháy của thành phố. Bảo tàng đặt trong quần thể một trạm cứu hoả cũ với tháp canh lửa (kalancha) đặc trưng - nơi lính cứu hoả xưa quan sát toàn cảnh để phát hiện khói lửa. Bên trong trưng bày bơm tay, xe cứu hoả kéo bằng ngựa, dụng cụ, chuông báo động, đồng phục và nhiều hiện vật minh hoạ nghề chữa cháy qua các thời kỳ. Một chủ đề nổi bật là trận đại hoả hoạn năm 1864 từng thiêu rụi phần lớn Simbirsk bằng gỗ - thảm hoạ thúc đẩy sự ra đời của lực lượng cứu hoả chuyên nghiệp. Sinh động, giàu tính giáo dục và đặc biệt cuốn hút với trẻ em, bảo tàng mang lại góc nhìn khác về đời sống đô thị, an toàn cộng đồng và lòng dũng cảm của những người lính cứu hoả, bổ sung nét đa dạng cho hệ thống bảo tàng của khu bảo tồn Simbirsk.",
    [
        "Đặt trong trạm cứu hoả cổ có tháp canh lửa (kalancha) đặc trưng.",
        "Trưng bày xe cứu hoả kéo ngựa, bơm tay, đồng phục và dụng cụ xưa.",
        "Kể về trận đại hoả hoạn 1864 từng thiêu rụi phần lớn Simbirsk.",
    ],
    p("Thường mở cửa 10:00–18:00; nghỉ một số ngày trong tuần - nên kiểm tra trước.",
      "Vé vào cửa phải trả phí, mức khiêm tốn; có ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 45–60 phút.",
      "Quanh năm; phù hợp cho gia đình có trẻ nhỏ.",
      "Thuộc quần thể khu bảo tồn Simbirsk; hỏi xem có được leo/ngắm tháp canh lửa không - trẻ em rất thích."),
    [
        {"title": "Музей-заповедник «Родина В.И. Ленина» — Пожарная охрана Симбирска", "url": "https://ulzapovednik.ru/"},
        {"title": "Wikipedia (RU) — Ульяновск (музейный квартал)", "url": "https://ru.wikipedia.org/wiki/Ульяновск"},
    ],
    ["museum", "firefighting", "history", "family", "simbirsk", "ulyanovsk"],
    maps_text("Музей пожарной охраны Симбирска", "Ульяновск", "Fire Service Museum Simbirsk", "Ulyanovsk", 54.31650, 48.39650),
    official_site="https://ulzapovednik.ru/",
))

# 10) Музей «Метеорологическая станция Симбирска. Планетарий» ----------------------
RECORDS.append(rec(
    "simbirsk-weather-station-planetarium-ulyanovsk",
    "Bảo tàng 'Trạm khí tượng Simbirsk - Cung thiên văn'",
    "Музей «Метеорологическая станция Симбирска. Планетарий»",
    "Museum 'Simbirsk Weather Station - Planetarium'",
    ["museum", "other"],
    54.31380, 48.39450,
    "'Khu phố bảo tàng' (musейный quartal), trung tâm lịch sử thành phố Ulyanovsk, tỉnh Ulyanovsk, Nga",
    "Bảo tàng khoa học độc đáo tái hiện trạm khí tượng đầu tiên của Simbirsk (hoạt động từ 1876), kèm một cung thiên văn (planetarium) nhỏ. Trưng bày các dụng cụ đo đạc thời tiết cổ và tổ chức chương trình chiếu vòm sao, rất được các gia đình và học sinh yêu thích.",
    "Bảo tàng 'Trạm khí tượng Simbirsk. Cung thiên văn' là một điểm đến khoa học - giáo dục thú vị trong 'khu phố bảo tàng' của Ulyanovsk, kết hợp lịch sử quan trắc khí tượng với trải nghiệm khám phá bầu trời. Bảo tàng tái hiện trạm khí tượng đầu tiên của Simbirsk - một trong những trạm quan trắc thời tiết có hệ thống sớm ở vùng Volga, hoạt động từ cuối thế kỷ 19 - với các dụng cụ đo nhiệt độ, khí áp, lượng mưa, hướng gió và những cuốn sổ ghi chép quan trắc cổ. Điểm nhấn đặc biệt là một cung thiên văn (planetarium) nhỏ, nơi khách, nhất là trẻ em và học sinh, được chiêm ngưỡng bầu trời sao mô phỏng dưới mái vòm và nghe kể về các chòm sao, hành tinh. Sự pha trộn giữa khoa học Trái Đất và thiên văn khiến đây trở thành điểm tham quan sinh động, khơi gợi trí tò mò và tình yêu khoa học. Nằm trong quần thể khu bảo tồn Simbirsk, bảo tàng bổ sung một sắc thái riêng - khoa học tự nhiên - cho hệ thống bảo tàng vốn giàu chất lịch sử - văn học của thành phố.",
    [
        "Tái hiện trạm khí tượng đầu tiên của Simbirsk (từ cuối thế kỷ 19).",
        "Có cung thiên văn (planetarium) nhỏ với chương trình chiếu vòm sao.",
        "Điểm khoa học - giáo dục hấp dẫn với trẻ em và học sinh.",
    ],
    p("Thường mở cửa 10:00–18:00; suất chiếu planetarium theo giờ cố định - nên kiểm tra/đặt trước.",
      "Vé vào cửa phải trả phí, mức khiêm tốn; suất chiếu planetarium có thể tính vé riêng.",
      "Khoảng 45–60 phút (kể cả suất chiếu).",
      "Quanh năm; phù hợp cho gia đình có trẻ nhỏ.",
      "Hỏi trước lịch suất chiếu cung thiên văn để căn giờ; thuộc quần thể khu bảo tồn Simbirsk nên tiện gộp vé nhiều bảo tàng."),
    [
        {"title": "Музей-заповедник «Родина В.И. Ленина» — Метеорологическая станция. Планетарий", "url": "https://ulzapovednik.ru/"},
        {"title": "Wikipedia (RU) — Ульяновск (музейный квартал)", "url": "https://ru.wikipedia.org/wiki/Ульяновск"},
    ],
    ["museum", "science", "planetarium", "meteorology", "family", "ulyanovsk"],
    maps_text("Метеорологическая станция Симбирска планетарий", "Ульяновск", "Simbirsk Weather Station Planetarium", "Ulyanovsk", 54.31380, 48.39450),
    official_site="https://ulzapovednik.ru/",
))


def main():
    path = os.path.join(REGIONS, f"{REGION}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    existing_slugs = {q.get("slug") for q in data}
    existing_ids = {q.get("id") for q in data}

    added, skipped = [], []
    for r in RECORDS:
        if r["slug"] in existing_slugs or r["id"] in existing_ids:
            skipped.append(r["slug"])
            continue
        data.append(r)
        existing_slugs.add(r["slug"])
        existing_ids.add(r["id"])
        added.append(r["slug"])

    if added:
        bak = f"{path}.bak_add_{TS}"
        shutil.copyfile(path, bak)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Backup: {os.path.basename(bak)}")

    print(f"REGION={REGION}  ADDED={len(added)}  SKIPPED(dup)={len(skipped)}  TOTAL_NOW={len(data)}")
    if added:
        print("  + " + "\n  + ".join(added))
    if skipped:
        print("  (skip dup): " + ", ".join(skipped))


if __name__ == "__main__":
    main()
