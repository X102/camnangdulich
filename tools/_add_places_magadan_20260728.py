# -*- coding: utf-8 -*-
"""_add_places_magadan_20260728.py — VÙNG: Tỉnh Magadan (Магаданская область).

Bổ sung địa điểm cho magadan (trước: 6) để đạt ≥30. Đợt này thêm 25 địa điểm THẬT SỰ
nổi tiếng/đặc sắc còn thiếu, đa dạng loại hình:
  museum 4 · theatre 2 · monument 7 · church 1 · square_street 1 · park_garden 8 · other 2

TOẠ ĐỘ — xác minh chéo, 2026-07-28:
  Nguồn chính cho cụm thành phố: autotravel.ru (mục "Координаты" dạng độ-phút-thập-phân
  N0DD MM.mmm / E1DD MM.mmm, đã đổi ra thập phân) + đối chiếu komandirovka.ru (mục "GPS
  координаты"). Thiên nhiên/vùng xa: idilesom.com (track GPS), ru.wikipedia geo (Bútugychag,
  Kadykchan, Kolyma HPP, Magadansky reserve/Matykil), academic.ru mirror (o. Nedorazumeniya).
  Kiểm phạm vi: tỉnh Magadan lat ~58,8–66; lon ~144–163; lat < lon; KHÔNG đảo trục — tất cả
  đều nằm trong tỉnh.
  Тrích một số: Краеведческий музей N059 33.507 E150 48.917 = 59.55845,150.815283;
  Монумент «Время»(мамонт) N059 33.857 E150 46.231 = 59.564283,150.770517;
  Каменный венец(мыс Замок) N059 31.264 E150 40.327 = 59.520733,150.672117;
  «Нулевая верста» N059 34.211 E150 48.606 = 59.570183,150.8101; Памятник Берзину
  N059 33.888 E150 48.478 = 59.5648,150.807967; «Олени» N059 35.719 E150 50.787 =
  59.595317,150.84645; Католич. церковь N059 33.240 E150 49.844 = 59.554,150.830733;
  Мыс Нюкля 59.586005,151.136298 (idilesom track); Бутугычаг 61.316667,149.188889;
  Матыкиль/Ямские о-ва 59.3292,155.5608; Серпантинка 62.702778,150.015; Колымская ГЭС
  ~62.058333,150.416667 (пос. Синегорье).

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_magadan_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "magadan"
REGION_NAME_VI = "Tỉnh Magadan"
FD = "Vùng Viễn Đông"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


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

# 1) Магаданский областной краеведческий музей ---------------------------------
RECORDS.append(rec(
    "krayevedchesky-museum-magadan",
    "Bảo tàng Nghiên cứu Địa phương tỉnh Magadan (Kraevedchesky muzey)",
    "Магаданский областной краеведческий музей",
    "Magadan Regional Museum (Museum of Local Lore)",
    ["museum"],
    59.55845, 150.815283,
    "Đại lộ Karl Marx (pr. Karla Marksa) 55, thành phố Magadan, tỉnh Magadan, Nga.",
    "Bảo tàng lớn và quan trọng nhất vùng Kolyma, mở cửa từ năm 1934 và chuyển về toà nhà hiện nay trên đại lộ Karl Marx năm 1983. Kho hiện vật hơn 250.000 đơn vị trải rộng từ thiên nhiên, dân tộc bản địa phương Bắc (người Even, Koryak) đến trang sử đau thương của các trại lao động Gulag ở Kolyma.",
    "Được thành lập ngày 30 tháng 3 năm 1934, Bảo tàng Nghiên cứu Địa phương tỉnh Magadan là cánh cửa toàn diện nhất để hiểu vùng Kolyma – Viễn Đông. Các gian trưng bày dẫn khách đi qua thiên nhiên khắc nghiệt của miền cực bắc, thế giới của các dân tộc bản địa (Even, Koryak, Itelmen, Yukaghir) với trang phục, đồ da và tín ngưỡng shaman, rồi tới lịch sử khai phá vàng và thiếc đã sinh ra thành phố. Nổi bật và ám ảnh nhất là bộ sưu tập về Dalstroy và hệ thống trại lao động Gulag – nơi hàng trăm nghìn tù nhân từng bị đưa qua cảng Nagaev; nhiều hiện vật gốc, ảnh và tài liệu ở đây thuộc loại hiếm có về giai đoạn đàn áp Stalin. Bảo tàng còn có phần khoáng vật, cổ sinh (voi ma-mút Kolyma) và nghệ thuật miền Bắc. Đây là điểm dừng chân đầu tiên nên có của bất kỳ ai muốn nắm được bức tranh lịch sử – văn hoá của Magadan.",
    [
        "Kho hơn 250.000 hiện vật, bảo tàng đầu ngành của cả vùng Kolyma từ năm 1934.",
        "Trưng bày sâu về Dalstroy và các trại lao động Gulag – đề tài trung tâm của lịch sử Magadan.",
        "Gian dân tộc bản địa phương Bắc và bộ sưu tập khoáng vật – cổ sinh vùng viễn đông.",
    ],
    {
        "hours_vi": "Thường mở cửa các ngày trong tuần (trừ thứ Hai); khoảng 10:00–18:00. Nên kiểm tra lịch trước khi đến.",
        "ticket_vi": "Vé vào cửa mức phổ thông (rẻ), có ưu đãi cho học sinh – hưu trí.",
        "duration_vi": "Khoảng 1,5–2,5 giờ.",
        "best_time_vi": "Quanh năm; là lựa chọn lý tưởng cho ngày thời tiết xấu.",
        "tips_vi": "Ở trung tâm, đi bộ tiện; nên dành thời gian cho khu trưng bày về Gulag; có thể thuê thuyết minh.",
    },
    [
        {"title": "Wikipedia (RU) — Магаданский областной краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Магаданский_областной_краеведческий_музей"},
        {"title": "Autotravel.ru — Магаданский областной краеведческий музей", "url": "https://autotravel.ru/otklik.php/32919"},
    ],
    ["museum", "history", "gulag", "kolyma", "local-lore", "magadan"],
    maps_text("Магаданский областной краеведческий музей", "Магадан", "Magadan Regional Museum", "Magadan", 59.55845, 150.815283),
    official_site="https://magadanmuseum.ru/",
))

# 2) Мемориальный музей-квартира Вадима Козина ----------------------------------
RECORDS.append(rec(
    "kozin-memorial-museum-magadan",
    "Bảo tàng - căn hộ lưu niệm Vadim Kozin (Muzey-kvartira Vadima Kozina)",
    "Мемориальный музей-квартира Вадима Козина",
    "Vadim Kozin Memorial Apartment Museum",
    ["museum"],
    59.565283, 150.800917,
    "Ngõ Shkolny (per. Shkolny) 1, thành phố Magadan, tỉnh Magadan, Nga.",
    "Căn hộ – bảo tàng gìn giữ nguyên trạng nơi ở của Vadim Kozin, danh ca tenor lừng lẫy của Liên Xô từng bị đày tới Kolyma. Đồ đạc, đàn piano, đĩa hát và thư từ cá nhân kể lại số phận nghiệt ngã mà tài hoa của một nghệ sĩ gắn liền với lịch sử Magadan.",
    "Vadim Kozin (1903–1994) là một trong những giọng tenor được yêu thích nhất của Liên Xô thập niên 1930–40, rồi bị bắt và đưa tới Kolyma trong làn sóng đàn áp; ông ở lại Magadan đến cuối đời. Bảo tàng – căn hộ được lập ngay trong nơi ông từng sống, giữ gần như nguyên vẹn không gian sinh hoạt: cây đàn piano, máy hát, hàng nghìn đĩa nhạc, ảnh, thư và những kỷ vật sân khấu. Qua đó, khách hình dung được cả một số phận nghệ sĩ tiêu biểu cho bi kịch “tài năng giữa gông cùm” của thời Stalin, đồng thời cảm nhận đời sống văn hoá bất ngờ phong phú của một thành phố nơi tận cùng đông bắc. Đây là điểm đến nhỏ nhưng giàu cảm xúc, thường được yêu thích bởi những ai quan tâm âm nhạc và lịch sử Xô-viết.",
    [
        "Không gian sống nguyên trạng của danh ca tenor Vadim Kozin – biểu tượng văn hoá Magadan.",
        "Bộ sưu tập đàn piano, máy hát, đĩa nhạc và kỷ vật sân khấu gốc.",
        "Câu chuyện nghệ sĩ tài hoa bị lưu đày tới Kolyma – lát cắt nhân văn của lịch sử Gulag.",
    ],
    {
        "hours_vi": "Mở cửa theo lịch bảo tàng (thường trừ thứ Hai); nên gọi/kiểm tra trước.",
        "ticket_vi": "Vé mức thấp; có thể có phụ phí thuyết minh.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Không gian nhỏ, đi theo nhóm ít người; kết hợp nghe các bản thu âm của Kozin để cảm nhận trọn vẹn.",
    },
    [
        {"title": "Autotravel.ru — Мемориальный музей-квартира Козина В.А.", "url": "https://autotravel.ru/otklik.php/28328"},
        {"title": "Komandirovka.ru — Мемориальный музей-квартира Вадима Козина", "url": "https://www.komandirovka.ru/sights/magadan/"},
    ],
    ["museum", "music", "memorial", "soviet", "magadan"],
    maps_text("Музей-квартира Вадима Козина", "Магадан", "Vadim Kozin Apartment Museum", "Magadan", 59.565283, 150.800917),
))

# 3) Магаданский геологический музей (СВКНИИ ДВО РАН) ---------------------------
RECORDS.append(rec(
    "geological-museum-svknii-magadan",
    "Bảo tàng Địa chất - Lịch sử Tự nhiên SVKNII (Geologichesky muzey)",
    "Геологический музей / Музей естественной истории СВКНИИ ДВО РАН",
    "SVKNII Geological (Natural History) Museum",
    ["museum"],
    59.565502, 150.792127,
    "Phố Portovaya, thành phố Magadan (thuộc Viện Nghiên cứu Liên ngành Đông Bắc SVKNII), tỉnh Magadan, Nga.",
    "Bảo tàng khoa học của Viện Nghiên cứu Liên ngành Đông Bắc (SVKNII), nổi tiếng với bộ sưu tập vàng, khoáng vật và hoá thạch của vùng Kolyma – quê hương của những mỏ vàng huyền thoại. Đây là nơi lý tưởng để hiểu vì sao Magadan ra đời từ cơn sốt vàng và thiếc.",
    "Trực thuộc Viện Nghiên cứu Liên ngành Đông Bắc thuộc Phân viện Viễn Đông Viện Hàn lâm Khoa học Nga (SVKNII DVO RAN), bảo tàng địa chất – lịch sử tự nhiên trưng bày một trong những bộ sưu tập khoáng vật và mẫu vật quý nhất Viễn Đông. Khách được chiêm ngưỡng các cục vàng tự nhiên, tinh thể khoáng, đá quý, mẫu quặng của các mỏ Kolyma, cùng hoá thạch cổ sinh trong đó có di cốt voi ma-mút – loài từng lang thang trên vùng đất này hàng trăm nghìn năm trước. Bộ sưu tập giúp lý giải sức hút đã biến vùng băng giá heo hút thành trung tâm khai khoáng chiến lược, đồng thời cho thấy sự đa dạng địa chất hiếm có của miền đông bắc nước Nga. Với người mê khoáng vật, vàng và lịch sử tự nhiên, đây là điểm đến chuyên sâu đáng giá ở Magadan.",
    [
        "Bộ sưu tập vàng tự nhiên và khoáng vật quý của vùng mỏ Kolyma.",
        "Mẫu hoá thạch cổ sinh, gồm di cốt voi ma-mút vùng viễn đông.",
        "Trưng bày khoa học của viện SVKNII – hiểu cội nguồn khai khoáng của Magadan.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ hành chính của viện; nên liên hệ trước vì lịch có thể hạn chế.",
        "ticket_vi": "Vé mức thấp hoặc theo thoả thuận đoàn.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm, trong giờ làm việc.",
        "tips_vi": "Vì là bảo tàng của viện nghiên cứu, nên đặt lịch/gọi trước; phù hợp cho ai yêu khoáng vật và địa chất.",
    },
    [
        {"title": "Autotravel.ru — Геологический музей (Магадан)", "url": "https://autotravel.ru/otklik.php/32949"},
        {"title": "Komandirovka.ru — Музей естественной истории СВКНИИ ДВО РАН", "url": "https://www.komandirovka.ru/sights/magadan/"},
    ],
    ["museum", "geology", "minerals", "gold", "science", "magadan"],
    maps_text("Геологический музей СВКНИИ", "Магадан", "SVKNII Geological Museum", "Magadan", 59.565502, 150.792127),
))

# 4) Магаданская галерея современного искусства --------------------------------
RECORDS.append(rec(
    "modern-art-gallery-magadan",
    "Phòng tranh Nghệ thuật Đương đại Magadan (Galereya sovremennogo iskusstva)",
    "Магаданская галерея современного искусства",
    "Magadan Gallery of Contemporary Art",
    ["museum"],
    59.567783, 150.802883,
    "Phố Pushkin (ul. Pushkina) 8, tầng 2, thành phố Magadan, tỉnh Magadan, Nga.",
    "Không gian trưng bày nghệ thuật đương đại giữa lòng Magadan, giới thiệu tác phẩm của các hoạ sĩ vùng Kolyma và các triển lãm luân phiên. Điểm đến thú vị cho ai muốn thấy một Magadan sáng tạo, hiện đại bên cạnh lịch sử nặng nề.",
    "Phòng tranh Nghệ thuật Đương đại Magadan là địa chỉ văn hoá dành cho mỹ thuật hiện thời của miền viễn đông. Tại đây, các triển lãm luân phiên giới thiệu tranh, đồ hoạ, điêu khắc nhỏ và nghệ thuật ứng dụng của những tác giả sống và làm việc ở Kolyma – nơi thiên nhiên khắc nghiệt và ký ức lịch sử trở thành nguồn cảm hứng đặc biệt. Bên cạnh sáng tác địa phương, phòng tranh còn đón các triển lãm khách mời, sự kiện giao lưu, buổi nói chuyện nghệ thuật, tạo nên một nhịp sống văn hoá đương đại cho thành phố. Đến đây, du khách cảm nhận được khía cạnh sáng tạo, trẻ trung của Magadan – một đối trọng nhẹ nhàng với những đài tưởng niệm Gulag trầm mặc. Quy mô nhỏ gọn nên rất hợp để ghé nhanh trong hành trình khám phá trung tâm.",
    [
        "Trưng bày mỹ thuật đương đại của các nghệ sĩ vùng Kolyma – Viễn Đông.",
        "Các triển lãm luân phiên và sự kiện văn hoá thường xuyên.",
        "Nằm ngay trung tâm, dễ kết hợp với các điểm tham quan khác.",
    ],
    {
        "hours_vi": "Mở cửa theo lịch triển lãm (thường trừ thứ Hai); kiểm tra trước khi đến.",
        "ticket_vi": "Vé thấp hoặc miễn phí tuỳ triển lãm.",
        "duration_vi": "Khoảng 30–60 phút.",
        "best_time_vi": "Quanh năm; hợp cho ngày thời tiết xấu.",
        "tips_vi": "Nội dung thay đổi theo triển lãm, nên xem lịch sự kiện trước để trúng chủ đề yêu thích.",
    },
    [
        {"title": "Autotravel.ru — Магаданская галерея современного искусства", "url": "https://autotravel.ru/otklik.php/32947"},
        {"title": "VisitKolyma — Достопримечательности Магадана", "url": "https://visitkolyma.ru/sights/"},
    ],
    ["museum", "art", "gallery", "contemporary", "magadan"],
    maps_text("Магаданская галерея современного искусства", "Магадан", "Magadan Gallery of Contemporary Art", "Magadan", 59.567783, 150.802883),
))

# 5) Магаданский музыкальный и драматический театр -----------------------------
RECORDS.append(rec(
    "music-drama-theatre-magadan",
    "Nhà hát Nhạc kịch và Kịch nói Magadan (Muzykalno-dramatichesky teatr)",
    "Магаданский государственный музыкальный и драматический театр им. М. Горького",
    "Magadan State Music and Drama Theatre",
    ["theatre"],
    59.56562, 150.800295,
    "Đại lộ Karl Marx (pr. Karla Marksa) 30, thành phố Magadan, tỉnh Magadan, Nga.",
    "Nhà hát chuyên nghiệp lâu đời và lớn nhất Magadan, mang tên đại văn hào Maxim Gorky. Trên sân khấu này, kịch nói, nhạc kịch và opereta được dàn dựng quanh năm trong một toà nhà bề thế – tâm điểm đời sống sân khấu của cả vùng Kolyma.",
    "Nhà hát Nhạc kịch và Kịch nói bang Magadan mang tên M. Gorky là trung tâm sân khấu chuyên nghiệp chủ chốt của tỉnh, có gốc rễ từ thời các đoàn nghệ thuật phục vụ cư dân và cả tù nhân vùng Dalstroy giữa thế kỷ 20 – khi Magadan bất ngờ quy tụ nhiều nghệ sĩ tài năng bị lưu đày. Ngày nay, nhà hát dàn dựng đa dạng thể loại: chính kịch, hài kịch, nhạc kịch, opereta và các chương trình cho thiếu nhi, với dàn diễn viên và nhạc công riêng. Toà nhà bề thế trên đại lộ Karl Marx là một trong những công trình văn hoá tiêu biểu của trung tâm thành phố. Với người dân Magadan, đây là nơi lui tới quen thuộc mỗi mùa diễn; còn với du khách, một buổi tối xem kịch ở đây là cách thú vị để chạm vào đời sống văn hoá đương đại bất ngờ sôi động của thành phố nơi cực đông.",
    [
        "Nhà hát chuyên nghiệp chủ lực của Kolyma, mang tên đại văn hào Maxim Gorky.",
        "Kịch nói, nhạc kịch, opereta và chương trình thiếu nhi diễn quanh mùa.",
        "Toà nhà văn hoá bề thế ngay trên đại lộ trung tâm Karl Marx.",
    ],
    {
        "hours_vi": "Biểu diễn theo lịch mùa diễn (thường buổi tối, thêm suất cuối tuần); phòng vé mở ban ngày.",
        "ticket_vi": "Giá vé phải chăng, tuỳ vở và vị trí ghế.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ.",
        "best_time_vi": "Mùa diễn thu – xuân; nên đặt vé trước cho các vở ăn khách.",
        "tips_vi": "Xem lịch diễn trên trang chính thức; đến sớm để gửi áo khoác mùa đông.",
    },
    [
        {"title": "Culture.ru — Магаданский музыкальный и драматический театр", "url": "https://www.culture.ru/institutes/10952/magadanskii-gosudarstvennyi-muzykalnyi-i-dramaticheskii-teatr"},
        {"title": "2GIS — Магаданский музыкальный и драматический театр", "url": "https://2gis.ru/magadan/firm/70000001027437377"},
    ],
    ["theatre", "drama", "music", "culture", "magadan"],
    maps_text("Магаданский музыкально-драматический театр", "Магадан", "Magadan Music and Drama Theatre", "Magadan", 59.56562, 150.800295),
    official_site="https://mmdt.ru/",
))

# 6) Магаданский областной театр кукол -----------------------------------------
RECORDS.append(rec(
    "puppet-theatre-magadan",
    "Nhà hát Múa rối tỉnh Magadan (Teatr kukol)",
    "Магаданский областной театр кукол",
    "Magadan Regional Puppet Theatre",
    ["theatre"],
    59.560136, 150.80422,
    "Trung tâm thành phố Magadan (gần đại lộ Karl Marx), tỉnh Magadan, Nga.",
    "Nhà hát múa rối được yêu thích nhất của tỉnh, điểm hẹn văn hoá của các gia đình Magadan. Những vở diễn con rối sinh động, ấm áp mang lại niềm vui cho trẻ nhỏ giữa mùa đông dài phương Bắc.",
    "Nhà hát Múa rối tỉnh Magadan là địa chỉ văn hoá dành cho thiếu nhi và gia đình, dàn dựng các vở diễn con rối dựa trên truyện cổ tích Nga, truyện dân gian phương Bắc và văn học thiếu nhi kinh điển. Với sân khấu ấm cúng, âm nhạc, ánh sáng và những con rối được chế tác công phu, nhà hát là nơi nhiều thế hệ trẻ em Magadan có buổi xem kịch đầu đời. Trong một thành phố có mùa đông dài và lạnh giá, những suất diễn cuối tuần ở đây trở thành hoạt động giải trí quen thuộc, gắn kết. Nhà hát cũng thường tham gia liên hoan nghệ thuật múa rối và đưa các chương trình lưu diễn tới các huyện xa của tỉnh. Với du khách đi cùng trẻ nhỏ, đây là lựa chọn dễ thương để trải nghiệm đời sống văn hoá bình dị của Magadan.",
    [
        "Nhà hát múa rối chủ lực của tỉnh, điểm hẹn của các gia đình có trẻ nhỏ.",
        "Vở diễn dựa trên cổ tích Nga và truyện dân gian phương Bắc.",
        "Không gian ấm cúng – hoạt động giải trí quen thuộc giữa mùa đông dài.",
    ],
    {
        "hours_vi": "Suất diễn chủ yếu cuối tuần và dịp lễ, thường vào ban ngày; kiểm tra lịch trước.",
        "ticket_vi": "Vé rẻ, hợp túi tiền gia đình.",
        "duration_vi": "Mỗi suất khoảng 45–60 phút.",
        "best_time_vi": "Cuối tuần, mùa thu – xuân.",
        "tips_vi": "Phù hợp trẻ em; nên đặt vé trước cho suất cuối tuần vì hay kín chỗ.",
    },
    [
        {"title": "Komandirovka.ru — Магаданский областной театр кукол", "url": "https://www.komandirovka.ru/sights/magadan/"},
        {"title": "VisitKolyma — Достопримечательности Магадана", "url": "https://visitkolyma.ru/sights/"},
    ],
    ["theatre", "puppet", "family", "children", "magadan"],
    maps_text("Магаданский областной театр кукол", "Магадан", "Magadan Puppet Theatre", "Magadan", 59.560136, 150.80422),
))

# 7) Монумент «Время» (мамонт) -------------------------------------------------
RECORDS.append(rec(
    "vremya-mammoth-monument-magadan",
    "Tượng đài «Thời gian» - Voi ma-mút (Monument «Vremya»)",
    "Скульптурная композиция «Время» (мамонт)",
    "Vremya (Time) Mammoth Sculpture",
    ["monument"],
    59.564283, 150.770517,
    "Đường Portovoye (Portovoye shosse), bên bờ vịnh Nagaev, thành phố Magadan, tỉnh Magadan, Nga.",
    "Tượng voi ma-mút khổng lồ cao chừng 6 mét, nặng khoảng 10 tấn, ghép từ vô số chi tiết máy móc kim loại rỉ sét màu nâu đỏ. Đặt bên bờ vịnh Nagaev, «Thời gian» là một trong những biểu tượng thị giác độc đáo và được chụp ảnh nhiều nhất của Magadan.",
    "Khánh thành ngày 7 tháng 9 năm 2013 nhân 60 năm thành lập tỉnh Magadan, tác phẩm «Thời gian» của nhà điêu khắc địa phương Yuri Rudenko khắc hoạ một con voi ma-mút hoàng gia – loài từng sinh sống ở vùng đất này hàng trăm nghìn năm trước (bằng chứng là chú voi ma-mút con “Dima” tìm thấy năm 1977, nổi tiếng thế giới). Điều đặc biệt là tượng không đúc liền khối mà được ghép từ hàng loạt chi tiết cơ khí, bánh răng, ống kim loại cũ; theo thời gian, lớp kim loại phủ gỉ chuyển sang sắc nâu đỏ, gợi đúng màu lông của loài thú thời tiền sử. Ý tưởng “mối liên hệ giữa các thời đại” hiện lên rõ nét: một bên là sinh vật đã tuyệt chủng, một bên là những mảnh ghép của thời công nghiệp hiện đại. Đứng bên bờ vịnh Nagaev lộng gió, con ma-mút kim loại trở thành phông nền chụp ảnh yêu thích và là một trong những “tấm danh thiếp” thị giác của Magadan.",
    [
        "Voi ma-mút kim loại cao ~6 m, nặng ~10 tấn, ghép từ hàng nghìn chi tiết máy móc rỉ sét.",
        "Tác phẩm của nhà điêu khắc Yuri Rudenko, khánh thành 2013 nhân 60 năm thành lập tỉnh.",
        "Vị trí bên bờ vịnh Nagaev – điểm chụp ảnh biểu tượng của thành phố.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–30 phút.",
        "best_time_vi": "Mùa hè và lúc trời quang; hoàng hôn trên vịnh rất đẹp.",
        "tips_vi": "Gió biển lạnh, mang áo ấm; kết hợp ghé bờ vịnh Nagaev và đài Vysotsky gần đó.",
    },
    [
        {"title": "Autotravel.ru — Скульптурная композиция «Время» (мамонт)", "url": "https://autotravel.ru/otklik.php/32920"},
        {"title": "Komandirovka.ru — Монумент «Время»", "url": "https://www.komandirovka.ru/sights/magadan/skulpturnaya-kompozitsiya-vremya/"},
    ],
    ["monument", "sculpture", "mammoth", "nagaev-bay", "symbol", "magadan"],
    maps_text("Монумент «Время» мамонт", "Магадан", "Vremya Mammoth Monument", "Magadan", 59.564283, 150.770517),
))

# 8) Памятник Владимиру Высоцкому ----------------------------------------------
RECORDS.append(rec(
    "vysotsky-monument-magadan",
    "Tượng đài Vladimir Vysotsky (Pamyatnik Vysotskomu)",
    "Памятник Владимиру Высоцкому",
    "Vladimir Vysotsky Monument",
    ["monument"],
    59.55605, 150.778833,
    "Phố Nagaevskaya, đài quan sát nhìn ra vịnh Nagaev, thành phố Magadan, tỉnh Magadan, Nga.",
    "Tượng đài dành cho Vladimir Vysotsky – ca sĩ, nhà thơ, diễn viên huyền thoại của Liên Xô, người từng viết bài hát nổi tiếng về Magadan. Tượng đặt trên đài quan sát bên vịnh Nagaev, gắn với câu thơ “Tôi bay tới Magadan…”.",
    "Vladimir Vysotsky (1938–1980) là bard (nghệ sĩ hát thơ) được yêu mến bậc nhất nước Nga thế kỷ 20, giọng ca khàn đặc trưng gắn với hàng trăm bài hát về thân phận con người. Ông có mối liên hệ tình cảm đặc biệt với Magadan qua bài hát dành tặng người bạn thân Igor Kokhanovsky đã tới đây sống, với câu mở đầu quen thuộc “Tôi bay tới Magadan”. Để tri ân, thành phố dựng tượng đài Vysotsky trên đài quan sát nhìn xuống vịnh Nagaev – đúng khung cảnh biển trời mà ông từng nhắc tới. Bức tượng khắc hoạ người nghệ sĩ với cây đàn ghi-ta, ánh mắt hướng ra biển, trở thành nơi người hâm mộ dừng chân, hát lại những ca khúc của ông. Vị trí đẹp bên vịnh khiến đây vừa là điểm tưởng niệm văn hoá, vừa là chỗ ngắm cảnh được ưa thích của cả người dân lẫn du khách.",
    [
        "Tôn vinh Vladimir Vysotsky – bard huyền thoại có bài hát nổi tiếng gắn với Magadan.",
        "Hình tượng nghệ sĩ ôm ghi-ta, hướng mắt ra biển vịnh Nagaev.",
        "Nằm trên đài quan sát – vừa tưởng niệm vừa ngắm cảnh vịnh đẹp.",
    ],
    {
        "hours_vi": "Ngoài trời, tự do 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–20 phút.",
        "best_time_vi": "Mùa hè, ngày trời quang để ngắm vịnh.",
        "tips_vi": "Kết hợp với đài quan sát vịnh Nagaev và tượng «Thời gian»; mang áo ấm vì lộng gió.",
    },
    [
        {"title": "Autotravel.ru — Памятник В.С. Высоцкому", "url": "https://autotravel.ru/otklik.php/25107"},
        {"title": "VisitKolyma — Достопримечательности Магадана", "url": "https://visitkolyma.ru/sights/"},
    ],
    ["monument", "vysotsky", "music", "nagaev-bay", "viewpoint", "magadan"],
    maps_text("Памятник Владимиру Высоцкому", "Магадан", "Vladimir Vysotsky Monument", "Magadan", 59.55605, 150.778833),
))

# 9) Монумент основателям города -----------------------------------------------
RECORDS.append(rec(
    "city-founders-monument-magadan",
    "Tượng đài Những người khai lập thành phố (Monument osnovatelyam goroda)",
    "Монумент основателям Магадана",
    "Monument to the Founders of Magadan",
    ["monument"],
    59.556267, 150.779083,
    "Phố Nagaevskaya, bên vịnh Nagaev (nơi đặt nền móng thành phố năm 1929), Magadan, tỉnh Magadan, Nga.",
    "Cụm tượng tưởng niệm những con người đầu tiên đặt nền móng cho Magadan năm 1929, khắc hoạ hình ảnh người thuộc nhiều ngành nghề. Đài đặt ngay tại điểm khởi sinh của thành phố bên vịnh Nagaev.",
    "Magadan khởi sinh từ một trạm tiếp vận bên vịnh Nagaev, nơi năm 1929 những nhóm người đầu tiên – kỹ sư, thợ xây, nhà địa chất, thuỷ thủ – đặt viên gạch đầu cho khu định cư sau này trở thành thủ phủ vùng Kolyma. Tượng đài dành cho những người khai lập được dựng đúng khu vực lịch sử ấy, thể hiện dưới dạng cụm tượng – phù điêu khắc hoạ con người thuộc nhiều nghề nghiệp cùng chung tay dựng nên thành phố. Công trình vừa tôn vinh công lao mở đất trong điều kiện khắc nghiệt của miền viễn đông, vừa nhắc nhớ khởi điểm khiêm nhường của một đô thị mọc lên nơi tận cùng bờ biển Okhotsk. Vị trí bên vịnh, gần đài Vysotsky và tượng «Thời gian», khiến đây là một điểm dừng trong tuyến tham quan bờ vịnh Nagaev – khu vực giàu ý nghĩa lịch sử nhất của thành phố.",
    [
        "Tưởng niệm những người đặt nền móng Magadan năm 1929 bên vịnh Nagaev.",
        "Cụm tượng khắc hoạ con người thuộc nhiều ngành nghề cùng dựng thành phố.",
        "Đặt tại khu vực khởi sinh lịch sử của đô thị Kolyma.",
    ],
    {
        "hours_vi": "Ngoài trời, tự do 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–20 phút.",
        "best_time_vi": "Mùa hè, ngày trời quang.",
        "tips_vi": "Đi cùng cụm điểm bờ vịnh Nagaev (Vysotsky, «Thời gian», bến cảng) trong một buổi.",
    },
    [
        {"title": "Autotravel.ru — Монумент основателям города", "url": "https://autotravel.ru/otklik.php/32924"},
        {"title": "VisitKolyma — Достопримечательности Магадана", "url": "https://visitkolyma.ru/sights/"},
    ],
    ["monument", "history", "nagaev-bay", "founders", "magadan"],
    maps_text("Монумент основателям Магадана", "Магадан", "Monument to Founders of Magadan", "Magadan", 59.556267, 150.779083),
))

# 10) Скульптура «Нулевая верста» ----------------------------------------------
RECORDS.append(rec(
    "zero-kilometer-kolyma-magadan",
    "Tượng «Cột mốc số 0» - khởi điểm đường Kolyma (Nulevaya versta)",
    "Скульптура «Нулевая верста»",
    "Zero Verst (Kilometre Zero) Sculpture",
    ["monument"],
    59.570183, 150.8101,
    "Quảng trường Magadanskaya (Magadanskaya ploshchad), thành phố Magadan, tỉnh Magadan, Nga.",
    "Tác phẩm đánh dấu “cột mốc số 0” – điểm khởi đầu tượng trưng của đại lộ Kolyma huyền thoại (Trassa) nối Magadan với vùng sâu trong nội địa. Một biểu tượng nhỏ nhưng đầy ý nghĩa về con đường đã định hình lịch sử cả vùng.",
    "«Nulevaya versta» (Cột mốc số 0) trên quảng trường Magadanskaya đánh dấu điểm xuất phát tượng trưng của đường Kolyma – tuyến đường bộ dài hơn 2.000 km nối Magadan với Yakutsk, được mệnh danh là “con đường xương trắng” vì đã được xây dựng bằng sức lao động và sinh mạng của vô số tù nhân Gulag. Từ chính điểm này, mọi khoảng cách trong vùng Kolyma theo truyền thống được tính đi. Tác phẩm điêu khắc – cột mốc trở thành nơi du khách chụp ảnh trước khi bắt đầu hành trình ngược lên nội địa, đồng thời gợi nhắc vai trò trung tâm của tuyến đường trong lịch sử khai phá và bi kịch của miền viễn đông. Nhỏ gọn nhưng giàu tính biểu tượng, đây là điểm dừng ý nghĩa ngay trong trung tâm thành phố.",
    [
        "Đánh dấu “cột mốc số 0” – khởi điểm tượng trưng của đường Kolyma (Trassa).",
        "Gợi nhắc tuyến đường huyền thoại nối Magadan – Yakutsk, gắn với lịch sử Gulag.",
        "Điểm chụp ảnh mang tính biểu tượng ngay trung tâm Magadan.",
    ],
    {
        "hours_vi": "Ngoài trời, tự do 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–15 phút.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Ghé chụp ảnh trước khi khởi hành theo đường Kolyma; nằm gần các quảng trường trung tâm.",
    },
    [
        {"title": "Autotravel.ru — Скульптура «Нулевая верста»", "url": "https://autotravel.ru/otklik.php/39859"},
        {"title": "VisitKolyma — Достопримечательности Магадана", "url": "https://visitkolyma.ru/sights/"},
    ],
    ["monument", "sculpture", "kolyma-highway", "symbol", "magadan"],
    maps_text("Скульптура «Нулевая верста»", "Магадан", "Zero Verst Sculpture", "Magadan", 59.570183, 150.8101),
))

# 11) Памятник Э. П. Берзину ---------------------------------------------------
RECORDS.append(rec(
    "berzin-monument-magadan",
    "Tượng đài Eduard Berzin (Pamyatnik Berzinu)",
    "Памятник Эдуарду Петровичу Берзину",
    "Eduard Berzin Monument",
    ["monument"],
    59.5648, 150.807967,
    "Quảng trường Gorky (ploshchad Gorkogo), thành phố Magadan, tỉnh Magadan, Nga.",
    "Tượng đài Eduard Berzin – người sáng lập và giám đốc đầu tiên của tổ hợp Dalstroy, nhân vật gắn liền với sự ra đời của Magadan và công cuộc khai thác vàng Kolyma những năm 1930. Một hình tượng lịch sử phức tạp, bản thân ông về sau cũng trở thành nạn nhân của thanh trừng Stalin.",
    "Eduard Berzin (1894–1938) là giám đốc đầu tiên của Dalstroy – tổ hợp nhà nước tổ chức khai thác vàng, thiếc và xây dựng hạ tầng ở Kolyma từ năm 1932, đặt nền cho sự phát triển thần tốc của Magadan. Dưới thời ông, thành phố và mạng lưới đường sá, mỏ, cảng hình thành nhanh chóng – nhưng cũng chính trên nền lao động cưỡng bức của hệ thống trại. Bản thân Berzin về sau bị bắt và xử bắn năm 1938 trong làn sóng Đại thanh trừng, rồi được phục hồi danh dự thời “tan băng”. Tượng đài trên quảng trường Gorky ghi dấu vai trò của ông trong lịch sử hình thành đô thị, đồng thời là lời nhắc về tính hai mặt bi kịch của giai đoạn Dalstroy – nơi thành tựu công nghiệp và tội ác đàn áp đan xen. Với người muốn tìm hiểu cội nguồn Magadan, đây là một mốc lịch sử không thể bỏ qua.",
    [
        "Tôn vinh Eduard Berzin – giám đốc đầu tiên của Dalstroy, gắn với sự ra đời của Magadan.",
        "Biểu tượng cho giai đoạn khai phá vàng Kolyma đầy mâu thuẫn thập niên 1930.",
        "Bản thân Berzin về sau là nạn nhân của Đại thanh trừng 1938.",
    ],
    {
        "hours_vi": "Ngoài trời, tự do 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–15 phút.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Kết hợp tìm hiểu lịch sử Dalstroy tại Bảo tàng địa phương để hiểu bối cảnh.",
    },
    [
        {"title": "Autotravel.ru — Памятник Э.П. Берзину", "url": "https://autotravel.ru/otklik.php/39848"},
        {"title": "Wikipedia (RU) — Берзин, Эдуард Петрович", "url": "https://ru.wikipedia.org/wiki/Берзин,_Эдуард_Петрович"},
    ],
    ["monument", "history", "dalstroy", "soviet", "magadan"],
    maps_text("Памятник Эдуарду Берзину", "Магадан", "Eduard Berzin Monument", "Magadan", 59.5648, 150.807967),
))

# 12) Скульптурная композиция «Олени» ------------------------------------------
RECORDS.append(rec(
    "deer-sculpture-magadan",
    "Cụm tượng «Đàn hươu» ở cửa ngõ thành phố (Skulptura «Oleni»)",
    "Скульптурная композиция «Олени»",
    "Deer (Reindeer) Sculpture",
    ["monument"],
    59.595317, 150.84645,
    "Đường Kolyma (Kolymskoye shosse), khu cửa ngõ vào thành phố Magadan, tỉnh Magadan, Nga.",
    "Cụm tượng đàn hươu đặt nơi cửa ngõ vào Magadan trên đường Kolyma, đón chào du khách đến với miền đất của tuần lộc và các dân tộc chăn nuôi phương Bắc. Một trong những hình ảnh quen thuộc đầu tiên khi đặt chân tới thành phố.",
    "Ở lối vào thành phố từ phía đường Kolyma, cụm tượng «Đàn hươu» hiện lên như lời chào của Magadan gửi tới lữ khách. Hình tượng những con hươu/tuần lộc gợi nhắc rằng đây là vùng đất của thảo nguyên rừng taiga và của các dân tộc bản địa phương Bắc (Even, Koryak, Chukchi) vốn gắn bó ngàn đời với nghề chăn nuôi tuần lộc. Đặt ở vị trí cửa ngõ, cụm tượng trở thành cột mốc thị giác đánh dấu ranh giới “đã tới Magadan”, là nơi nhiều người dừng lại chụp tấm ảnh lưu niệm đầu tiên hoặc cuối cùng của chuyến đi. Trên nền núi đồi và bầu trời phương Bắc, hình bóng đàn hươu mang lại cảm giác vừa hoang sơ vừa thân thiện – một biểu tượng nhẹ nhàng cho thiên nhiên và văn hoá của vùng Kolyma.",
    [
        "Cụm tượng đàn hươu/tuần lộc ở cửa ngõ vào thành phố trên đường Kolyma.",
        "Gợi nhắc văn hoá chăn nuôi tuần lộc của các dân tộc bản địa phương Bắc.",
        "Cột mốc “chào mừng đến Magadan” – điểm chụp ảnh lưu niệm quen thuộc.",
    ],
    {
        "hours_vi": "Ngoài trời, tự do 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–15 phút (điểm dừng ven đường).",
        "best_time_vi": "Ban ngày, mùa hè; tiện dừng khi ra/vào thành phố.",
        "tips_vi": "Nằm ven đường Kolyma nên hợp làm điểm dừng chụp ảnh trên hành trình; chú ý an toàn giao thông.",
    },
    [
        {"title": "Autotravel.ru — Скульптурная композиция «Олени»", "url": "https://autotravel.ru/otklik.php/32941"},
        {"title": "VisitKolyma — Достопримечательности Магадана", "url": "https://visitkolyma.ru/sights/"},
    ],
    ["monument", "sculpture", "reindeer", "city-gate", "north", "magadan"],
    maps_text("Скульптурная композиция «Олени»", "Магадан", "Deer Sculpture", "Magadan", 59.595317, 150.84645),
))

# 13) Католическая церковь Рождества Иисуса Христа -----------------------------
RECORDS.append(rec(
    "catholic-church-nativity-magadan",
    "Nhà thờ Công giáo Chúa Giáng Sinh (Tserkov Rozhdestva Iisusa)",
    "Католическая церковь Рождества Иисуса Христа",
    "Catholic Church of the Nativity of Jesus Christ",
    ["church"],
    59.554, 150.830733,
    "Phố Proletarskaya (ul. Proletarskaya) 63, thành phố Magadan, tỉnh Magadan, Nga.",
    "Một trong những nhà thờ Công giáo lớn và ấn tượng nhất vùng Viễn Đông Nga, xây bằng đá granit theo phong cách hiện đại. Công trình được dành riêng để tưởng nhớ các nạn nhân của những cuộc đàn áp trên đất Kolyma.",
    "Nhà thờ Công giáo Chúa Giáng Sinh ở Magadan là một trong những thánh đường Công giáo lớn nhất và nổi bật nhất của toàn miền Viễn Đông Nga. Được khánh thành đầu thập niên 2000, công trình gây ấn tượng bởi khối kiến trúc hiện đại, vững chãi ốp đá granit sẫm màu, khác hẳn dáng vẻ nhà thờ Chính thống giáo quen thuộc. Bên trong là không gian cầu nguyện trang nghiêm, sáng và tĩnh lặng. Điều đặc biệt là ngôi thánh đường được dâng hiến để tưởng niệm những nạn nhân của các cuộc đàn áp chính trị ở Kolyma – trong đó có rất nhiều người Công giáo thuộc nhiều dân tộc bị đưa tới các trại lao động. Nhà thờ vì thế vừa là nơi sinh hoạt tôn giáo của cộng đồng Công giáo địa phương, vừa là một biểu tượng của hoà giải và tưởng nhớ. Với du khách, đây là điểm tham quan kiến trúc thú vị, cho thấy tính đa dạng tôn giáo bất ngờ của một thành phố nơi cực đông.",
    [
        "Một trong những nhà thờ Công giáo lớn nhất Viễn Đông Nga, kiến trúc hiện đại ốp đá granit.",
        "Được dâng hiến tưởng niệm các nạn nhân đàn áp chính trị ở Kolyma.",
        "Không gian tôn giáo trang nghiêm, điểm nhấn về sự đa dạng tín ngưỡng của Magadan.",
    ],
    {
        "hours_vi": "Mở cửa cho khách tham quan và thánh lễ theo lịch giáo xứ; ngày thường có thể hạn chế.",
        "ticket_vi": "Miễn phí (có thể quyên góp tuỳ tâm).",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm; đẹp nhất khi có ánh sáng ban ngày qua cửa kính.",
        "tips_vi": "Ăn mặc lịch sự, giữ yên tĩnh; nên hỏi lịch thánh lễ nếu muốn dự.",
    },
    [
        {"title": "Autotravel.ru — Католическая церковь Рождества Иисуса", "url": "https://autotravel.ru/otklik.php/32927"},
        {"title": "VisitKolyma — Достопримечательности Магадана", "url": "https://visitkolyma.ru/sights/"},
    ],
    ["church", "catholic", "architecture", "memorial", "magadan"],
    maps_text("Католическая церковь Рождества Иисуса", "Магадан", "Catholic Church of the Nativity", "Magadan", 59.554, 150.830733),
))

# 14) Проспект Ленина ----------------------------------------------------------
RECORDS.append(rec(
    "lenin-avenue-magadan",
    "Đại lộ Lenin (Prospekt Lenina)",
    "Проспект Ленина",
    "Lenin Avenue (Prospekt Lenina)",
    ["square_street"],
    59.565483, 150.80535,
    "Đại lộ Lenin (prospekt Lenina), trung tâm thành phố Magadan, tỉnh Magadan, Nga.",
    "Trục phố chính và bộ mặt kiến trúc của Magadan, với những dãy nhà bề thế phong cách tân cổ điển Stalin thập niên 1950. Đây là nơi tập trung quảng trường, quán xá, tượng đài và nhịp sống đô thị của thành phố.",
    "Đại lộ Lenin là xương sống của trung tâm Magadan – con phố mà mọi du khách đều đi qua để cảm nhận diện mạo đô thị nơi cực đông. Hai bên đường là những toà nhà bề thế xây thời hậu chiến theo phong cách “đế chế Stalin” (tân cổ điển Xô-viết), với mặt tiền đối xứng, cột và phù điêu – di sản kiến trúc từ thời Magadan được quy hoạch thành thủ phủ khang trang của Kolyma. Dọc đại lộ là các quảng trường, cửa hàng, quán cà phê, rạp và nhiều tượng đài, cụm tượng nhỏ dễ thương. Vào mùa hè, phố được trang trí hoa và trở thành nơi dạo bộ, hẹn hò của người dân; mùa đông, tuyết phủ và đèn trang trí tạo nên khung cảnh phương Bắc đặc trưng. Đi bộ dọc đại lộ Lenin là cách tốt nhất để bắt nhịp đời sống thường nhật và chiêm ngưỡng quần thể kiến trúc lịch sử của thành phố.",
    [
        "Trục phố trung tâm với quần thể kiến trúc tân cổ điển Stalin thập niên 1950.",
        "Tập trung quảng trường, tượng đài, quán xá – nơi cảm nhận nhịp sống Magadan.",
        "Điểm dạo bộ lý tưởng, đẹp cả mùa hè hoa lá lẫn mùa đông tuyết phủ.",
    ],
    {
        "hours_vi": "Không gian công cộng, tự do 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Đi bộ ngắm phố khoảng 30–60 phút.",
        "best_time_vi": "Mùa hè để dạo bộ; buổi tối khi phố lên đèn.",
        "tips_vi": "Kết hợp ghé các quảng trường, tượng đài dọc đường; nhiều quán cà phê để nghỉ chân.",
    },
    [
        {"title": "Autotravel.ru — Достопримечательности Магадана", "url": "https://autotravel.ru/excite.php/4167/1"},
        {"title": "VisitKolyma — Магадан", "url": "https://visitkolyma.ru/sights/"},
    ],
    ["square_street", "avenue", "architecture", "stalin-empire", "city-center", "magadan"],
    maps_text("Проспект Ленина", "Магадан", "Lenin Avenue", "Magadan", 59.565483, 150.80535),
))

# 15) Магаданский городской парк -----------------------------------------------
RECORDS.append(rec(
    "city-park-magadan",
    "Công viên Thành phố Magadan (Gorodskoy park)",
    "Магаданский городской парк (Парк культуры и отдыха)",
    "Magadan City Park",
    ["park_garden"],
    59.560767, 150.803067,
    "Đại lộ Lenin (prospekt Lenina) 21A, thành phố Magadan, tỉnh Magadan, Nga.",
    "Công viên văn hoá – nghỉ ngơi trung tâm của Magadan, lá phổi xanh và nơi vui chơi quen thuộc của cư dân thành phố. Có lối đi dạo, trò chơi, sân khấu ngoài trời và các sự kiện lễ hội theo mùa.",
    "Nằm ngay trung tâm bên đại lộ Lenin, Công viên Thành phố Magadan là không gian giải trí công cộng lâu đời và được yêu thích nhất của người dân. Trong khuôn viên rợp cây phương Bắc là các lối đi dạo, khu trò chơi thiếu nhi, đu quay, sân khấu ngoài trời và những góc nghỉ ngơi. Vào mùa hè ngắn ngủi, công viên trở nên nhộn nhịp với các buổi hoà nhạc, hội chợ, lễ hội thành phố; mùa đông, một phần khuôn viên biến thành sân trượt băng và không gian trang trí đón năm mới. Đây là nơi các gia đình dắt trẻ nhỏ, thanh niên hẹn hò và người lớn tuổi dạo bộ – một lát cắt đời thường ấm áp của Magadan giữa thiên nhiên khắc nghiệt. Với du khách, công viên là chỗ nghỉ chân dễ chịu, đồng thời là dịp quan sát nhịp sống bình dị của cư dân miền cực đông.",
    [
        "Công viên văn hoá – nghỉ ngơi trung tâm, lá phổi xanh của Magadan.",
        "Khu trò chơi, sân khấu ngoài trời và các lễ hội, hội chợ theo mùa.",
        "Mùa đông có sân trượt băng và trang trí đón năm mới.",
    ],
    {
        "hours_vi": "Không gian mở, tự do; các trò chơi/khu dịch vụ hoạt động theo giờ và mùa.",
        "ticket_vi": "Vào cửa miễn phí; một số trò chơi tính phí.",
        "duration_vi": "Khoảng 30–60 phút.",
        "best_time_vi": "Mùa hè cho hoạt động ngoài trời; dịp lễ, năm mới cho không khí hội hè.",
        "tips_vi": "Điểm nghỉ chân tiện lợi ở trung tâm; hợp cho gia đình có trẻ nhỏ.",
    },
    [
        {"title": "Autotravel.ru — Городской парк (Магадан)", "url": "https://autotravel.ru/otklik.php/37472"},
        {"title": "VisitKolyma — Достопримечательности Магадана", "url": "https://visitkolyma.ru/sights/"},
    ],
    ["park_garden", "city-park", "recreation", "family", "magadan"],
    maps_text("Магаданский городской парк", "Магадан", "Magadan City Park", "Magadan", 59.560767, 150.803067),
))

# 16) Парк этнической культуры народов Севера «Дюкча» --------------------------
RECORDS.append(rec(
    "dukcha-ethnic-park-magadan",
    "Công viên văn hoá dân tộc phương Bắc «Dyukcha» (Park «Dyukcha»)",
    "Парк этнической культуры народов Севера «Дюкча»",
    "Dyukcha Ethnic Culture Park of the Peoples of the North",
    ["park_garden"],
    59.567283, 150.916667,
    "Đường Dukchinskoye (Dukchinskoye shosse), thành phố Magadan, tỉnh Magadan, Nga.",
    "Công viên văn hoá dân tộc tái hiện đời sống của các cộng đồng bản địa phương Bắc – Even, Koryak, Itelmen. Có lều truyền thống, các lễ hội dân tộc và không gian thiên nhiên ven suối Dukcha.",
    "Công viên «Dyukcha» là nơi giới thiệu văn hoá của các dân tộc bản địa vùng Bắc Cực – Even, Koryak, Itelmen, Chukchi – ngay gần Magadan. Trong khuôn viên ven suối Dukcha, khách có thể thấy các kiểu lều truyền thống (yaranga, chum), dụng cụ săn bắt, đánh cá, xe trượt tuần lộc và những góc tái hiện sinh hoạt du mục của cư dân miền cực. Đây cũng là địa điểm tổ chức các lễ hội dân tộc theo mùa như lễ đón cá hồi, ngày hội của người chăn tuần lộc, với ca múa, trò chơi dân gian và ẩm thực bản địa. Bao quanh là cảnh quan rừng taiga và dòng suối, tạo không gian vừa mang tính bảo tàng ngoài trời vừa gần gũi thiên nhiên. Với du khách, «Dyukcha» là cách sinh động để tiếp cận di sản của những dân tộc đã sống hài hoà với thiên nhiên khắc nghiệt phương Bắc suốt hàng nghìn năm, trước khi Magadan hình thành.",
    [
        "Tái hiện đời sống của các dân tộc bản địa phương Bắc (Even, Koryak, Itelmen).",
        "Lều truyền thống, dụng cụ săn – đánh cá, xe trượt tuần lộc; không gian ven suối Dukcha.",
        "Nơi diễn ra các lễ hội dân tộc theo mùa với ca múa, ẩm thực bản địa.",
    ],
    {
        "hours_vi": "Không gian ngoài trời; hoạt động sôi nổi nhất vào các dịp lễ hội theo mùa.",
        "ticket_vi": "Thường miễn phí hoặc phí thấp; sự kiện có thể tính phí riêng.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Vào các dịp lễ hội dân tộc (thường mùa hè – thu) để trải nghiệm trọn vẹn.",
        "tips_vi": "Xem lịch lễ hội trước để trúng dịp có biểu diễn; mang giày đi bộ, đồ chống muỗi mùa hè.",
    },
    [
        {"title": "Autotravel.ru — Парк этнической культуры народов Севера «Дюкча»", "url": "https://autotravel.ru/otklik.php/37469"},
        {"title": "VisitKolyma — Достопримечательности Магадана", "url": "https://visitkolyma.ru/sights/"},
    ],
    ["park_garden", "ethnography", "indigenous", "north", "culture", "magadan"],
    maps_text("Парк этнической культуры «Дюкча»", "Магадан", "Dyukcha Ethnic Park", "Magadan", 59.567283, 150.916667),
))

# 17) Гора Марчекан (Марчеканская сопка) ---------------------------------------
RECORDS.append(rec(
    "marchekan-mountain-magadan",
    "Núi Marchekan - đỉnh cao bán đảo Staritsky (Marchekanskaya sopka)",
    "Гора Марчекан (Марчеканская сопка)",
    "Marchekan Mountain (Marchekanskaya Sopka)",
    ["park_garden"],
    59.513056, 150.826667,
    "Bán đảo Staritsky, phía nam thành phố Magadan, tỉnh Magadan, Nga.",
    "Đỉnh cao nhất của bán đảo Staritsky (khoảng 705 m), điểm leo núi – ngắm cảnh được yêu thích ngay sát Magadan. Từ trên đỉnh phủ cây bụi kim tùng, tầm mắt trải ra biển Okhotsk, vịnh và toàn cảnh thành phố.",
    "Marchekanskaya sopka là đỉnh cao nhất (khoảng 705 m) trong hai dãy núi chạy dọc bán đảo Staritsky – dải đất gồ ghề nhô ra biển Okhotsk ngay phía nam Magadan. Sườn núi phủ dày kim tùng lùn (kedrovy stlanik) đặc trưng phương Bắc, xen những vạt đá và đồng rêu. Đây là một trong bốn tuyến đi bộ được đánh dấu của bán đảo, thu hút người dân thành phố vào những ngày cuối tuần đẹp trời. Đường lên không quá khó nhưng đủ để thưởng cho người leo một phần thưởng xứng đáng: từ đỉnh, tầm nhìn mở ra bao la với biển Okhotsk, các vịnh Nagaev và Gertner, những mũi đá, đảo nhỏ và toàn cảnh Magadan nằm gọn dưới chân. Vào mùa thu, thảm thực vật chuyển vàng đỏ rực rỡ; mùa hè là thời điểm lý tưởng để dã ngoại, hái quả việt quất dại. Gần thành phố mà vẫn hoang sơ, Marchekan là điểm hoà mình vào thiên nhiên Kolyma dễ tiếp cận nhất.",
    [
        "Đỉnh cao nhất bán đảo Staritsky (~705 m), sát cạnh Magadan.",
        "Tuyến đi bộ được đánh dấu, phủ kim tùng lùn phương Bắc.",
        "Tầm nhìn toàn cảnh biển Okhotsk, các vịnh và thành phố từ trên đỉnh.",
    ],
    {
        "hours_vi": "Ngoài trời, tự do; nên đi vào ban ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Leo lên – xuống khoảng 3–5 giờ tuỳ điểm xuất phát.",
        "best_time_vi": "Mùa hè và đầu thu (tháng 7–9); tránh ngày mù sương, gió lớn.",
        "tips_vi": "Mang giày leo núi, nước, áo gió; thời tiết đổi nhanh nên chuẩn bị đồ ấm; đi theo nhóm an toàn hơn.",
    },
    [
        {"title": "VisitKolyma — Полуостров Старицкого", "url": "https://visitkolyma.ru/sights/poluostrov-staritskogo-/"},
        {"title": "Wikipedia (RU) — Полуостров Старицкого", "url": "https://ru.wikipedia.org/wiki/Полуостров_Старицкого"},
    ],
    ["park_garden", "mountain", "hiking", "viewpoint", "staritsky", "magadan"],
    maps_text("Гора Марчекан", "Магадан", "Marchekan Mountain", "Magadan", 59.513056, 150.826667),
))

# 18) Скала «Каменный венец» ---------------------------------------------------
RECORDS.append(rec(
    "kamenny-venets-rock-magadan",
    "Vách đá «Vương miện đá» - mũi Zamok (Kamenny venets)",
    "Скала «Каменный венец» (мыс Замок)",
    "Kamenny Venets (Stone Crown) Rock",
    ["park_garden"],
    59.520733, 150.672117,
    "Mũi Zamok (mys Zamok), phần tây bán đảo Staritsky, bờ nam vịnh Nagaev, tỉnh Magadan, Nga.",
    "Khối đá răng cưa hình “vương miện” nhô lên trên sống núi bán đảo Staritsky, một trong những cảnh quan ngoạn mục và được dân leo núi Magadan yêu thích nhất. Từ đây phóng tầm mắt xuống vịnh Nagaev và biển Okhotsk.",
    "«Kamenny venets» – Vương miện đá – là dải đá granit lởm chởm nhô lên như những chiếc răng cưa trên đỉnh dãy núi phía bắc của bán đảo Staritsky, tại khu vực mũi Zamok (Lâu đài). Hình dáng độc đáo của các khối đá, tựa vành vương miện hay tường thành đổ nát, khiến nơi đây trở thành một trong những điểm đến ngoạn mục nhất quanh Magadan. Tuyến đi bộ lên Kamenny venets được đánh dấu, băng qua thảm kim tùng lùn và những triền dốc mở, phần thưởng là khung cảnh choáng ngợp: vách đá dựng đứng đổ xuống bờ nam vịnh Nagaev, biển Okhotsk xanh thẫm và những mũi đất, đảo đá phía xa. Đây là địa điểm ưa thích để chụp ảnh, ngắm hoàng hôn và cảm nhận vẻ hùng vĩ hoang sơ của bờ biển Kolyma – tất cả chỉ cách trung tâm thành phố một quãng đi bộ trong ngày. Vào mùa thu, sắc lá đỏ vàng càng làm khung cảnh thêm rực rỡ.",
    [
        "Dải đá granit răng cưa hình “vương miện” trên sống núi bán đảo Staritsky.",
        "Một trong những cảnh quan ngoạn mục nhất quanh Magadan, có tuyến đi bộ đánh dấu.",
        "Tầm nhìn xuống bờ nam vịnh Nagaev và biển Okhotsk – tuyệt đẹp lúc hoàng hôn.",
    ],
    {
        "hours_vi": "Ngoài trời, tự do; nên đi ban ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Đi bộ khứ hồi khoảng 3–5 giờ.",
        "best_time_vi": "Mùa hè – đầu thu, ngày trời quang; hoàng hôn rất đẹp.",
        "tips_vi": "Đá trơn, dốc cạnh vực – đi cẩn thận, không lại quá sát mép; mang giày bám tốt, nước và áo gió.",
    },
    [
        {"title": "Autotravel.ru — Каменный венец (мыс Замок)", "url": "https://autotravel.ru/otklik.php/39832"},
        {"title": "VisitKolyma — Полуостров Старицкого", "url": "https://visitkolyma.ru/sights/poluostrov-staritskogo-/"},
    ],
    ["park_garden", "rock", "cliff", "hiking", "viewpoint", "staritsky", "magadan"],
    maps_text("Скала «Каменный венец» мыс Замок", "Магадан", "Kamenny Venets Rock", "Magadan", 59.520733, 150.672117),
))

# 19) Бухта Гертнера -----------------------------------------------------------
RECORDS.append(rec(
    "gertner-bay-magadan",
    "Vịnh Gertner (Bukhta Gertnera)",
    "Бухта Гертнера",
    "Gertner Bay",
    ["park_garden"],
    59.543333, 150.9175,
    "Bờ đông thành phố Magadan (thuộc vịnh Taui, biển Okhotsk), tỉnh Magadan, Nga.",
    "Vịnh biển phía đông Magadan với bãi triều rộng, nơi người dân ra tắm nắng, câu cá, đi dạo và ngắm biển vào mùa hè. Một trong những “bãi biển” gần gũi nhất của cư dân thành phố.",
    "Nằm ở phía đông Magadan, vịnh Gertner mở ra biển Okhotsk và là chốn nghỉ ngơi ven biển quen thuộc của người dân thành phố. Khi thuỷ triều rút, bãi triều lộ ra rộng mênh mông với cát, sỏi và những vũng nước lấp lánh, trở thành nơi đi dạo, nhặt vỏ sò, thả diều và ngắm hoàng hôn. Vào những ngày hè hiếm hoi ấm áp, người Magadan ra đây tắm nắng, cắm trại, nướng đồ ăn (shashlyk); dân câu thì tìm cá và bắt các loài hải sản ven bờ. Nước biển lạnh quanh năm nên tắm biển thực sự chỉ dành cho những người gan lì, nhưng khung cảnh trời nước bao la, viền núi phương Bắc và không khí trong lành khiến vịnh Gertner trở thành điểm dã ngoại cuối tuần được yêu thích. Với du khách, đây là dịp cảm nhận “biển Okhotsk” theo cách dung dị và đời thường nhất của người dân địa phương.",
    [
        "Vịnh biển phía đông Magadan với bãi triều rộng lộ ra khi nước rút.",
        "Nơi người dân dã ngoại, câu cá, đi dạo và ngắm hoàng hôn mùa hè.",
        "Khung cảnh biển Okhotsk và viền núi phương Bắc bao la.",
    ],
    {
        "hours_vi": "Ngoài trời, tự do 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Mùa hè (tháng 7–8) cho dã ngoại; chú ý lịch thuỷ triều.",
        "tips_vi": "Nước biển rất lạnh – chỉ nên ngâm chân; mang đồ ấm, đồ chống muỗi; theo dõi con nước khi ra bãi triều.",
    },
    [
        {"title": "Wikipedia (RU) — Бухта Гертнера", "url": "https://ru.wikipedia.org/wiki/Гертнера_(бухта)"},
        {"title": "VisitKolyma — Достопримечательности Магадана", "url": "https://visitkolyma.ru/sights/"},
    ],
    ["park_garden", "bay", "beach", "sea-of-okhotsk", "recreation", "magadan"],
    maps_text("Бухта Гертнера", "Магадан", "Gertner Bay", "Magadan", 59.543333, 150.9175),
))

# 20) Мыс Нюкля («Спящий дракон») ----------------------------------------------
RECORDS.append(rec(
    "nyuklya-cape-magadan",
    "Mũi Nyuklya - «Rồng ngủ» (Mys Nyuklya)",
    "Мыс Нюкля («Спящий дракон» / «Спящая красавица»)",
    "Cape Nyuklya (Sleeping Dragon)",
    ["park_garden"],
    59.586005, 151.136298,
    "Km 23 đường đi Ola (Olskaya doroga), huyện Olsky, gần thành phố Magadan, tỉnh Magadan, Nga.",
    "Mũi đá vươn dài ra biển Okhotsk với đường viền giống một con rồng (hoặc nàng công chúa) đang ngủ – một trong những “tấm danh thiếp” cảnh quan của tỉnh Magadan. Đài quan sát ven đường Ola cho tầm nhìn tuyệt đẹp.",
    "Mũi Nyuklya, dân Magadan quen gọi là «Rồng ngủ» hay «Người đẹp ngủ», là dải đá nhô xa ra biển Okhotsk mà nhìn từ xa có đường sống lưng uốn lượn tựa một con rồng – hoặc một thiếu nữ đang say ngủ trong cổ tích. Tên gọi Nyuklya xuất phát từ tiếng Even, được cho là liên quan tới hiện tượng cá trích mắc cạn thối rữa khi thuỷ triều rút. Panorama nhìn ra mũi Nyuklya được xem là một trong những hình ảnh biểu tượng của cả tỉnh. Từ đài quan sát bên đường đi Ola (khoảng km 23, chỉ chừng nửa giờ chạy xe từ Magadan), du khách thu vào tầm mắt toàn cảnh mũi đất, bờ biển và mặt nước Okhotsk mênh mông. Cảnh đẹp nhất mở ra từ những bờ cao ở phía đông mũi. Đây là điểm dừng chân, chụp ảnh gần như bắt buộc trên cung đường ven biển ra hướng Ola, và là nơi cảm nhận rõ vẻ hùng vĩ, hoang sơ của bờ biển Kolyma.",
    [
        "Mũi đá hình «rồng ngủ» vươn ra biển Okhotsk – biểu tượng cảnh quan của tỉnh Magadan.",
        "Đài quan sát ven đường Ola (km 23), chỉ ~30 phút xe từ Magadan.",
        "Tầm nhìn toàn cảnh mũi đất và biển đẹp nhất từ các bờ cao phía đông.",
    ],
    {
        "hours_vi": "Ngoài trời, tự do; đi ban ngày để ngắm cảnh.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–60 phút tại điểm ngắm; lâu hơn nếu đi bộ khám phá mũi.",
        "best_time_vi": "Mùa hè – thu, ngày trời quang; lúc thuỷ triều xuống thấy rõ chân mũi.",
        "tips_vi": "Đi ô tô theo đường Ola là tiện nhất; dừng ở điểm ngắm cảnh; gió mạnh nên mang áo ấm.",
    },
    [
        {"title": "ИдиЛесом — Мыс Нюкля (маршрут, координаты)", "url": "https://idilesom.com/kolyma/places/3143"},
        {"title": "Tour.kolyma.ru — Мыс Нюкля", "url": "https://tour.kolyma.ru/turizm/mgdn/140-mys-njuklja.html"},
    ],
    ["park_garden", "cape", "coast", "sea-of-okhotsk", "viewpoint", "olsky", "magadan"],
    maps_text("Мыс Нюкля", "Магаданская область", "Cape Nyuklya", "Ola", 59.586005, 151.136298),
))

# 21) Остров Недоразумения -----------------------------------------------------
RECORDS.append(rec(
    "nedorazumeniya-island-magadan",
    "Đảo Nedorazumeniya - «Đảo Hiểu Lầm» (Ostrov Nedorazumeniya)",
    "Остров Недоразумения",
    "Nedorazumeniya (Misunderstanding) Island",
    ["park_garden"],
    59.59, 150.40,
    "Vịnh Taui / vịnh Amakhton, biển Okhotsk, phía tây thành phố Magadan, tỉnh Magadan, Nga.",
    "Hòn đảo nhỏ ngoài khơi phía tây Magadan với cái tên độc đáo «Đảo Hiểu Lầm», nổi tiếng là nơi trú ngụ của các đàn chim biển và hải cẩu. Điểm đến thú vị cho các chuyến du thuyền ngắm động vật hoang dã ven biển Okhotsk.",
    "«Ostrov Nedorazumeniya» – Đảo Hiểu Lầm – có cái tên gây tò mò được cho là bắt nguồn từ một sự nhầm lẫn khi lập bản đồ ven biển thời trước. Hòn đảo đá nhỏ nằm ngoài khơi phía tây Magadan, trong vùng vịnh Taui của biển Okhotsk. Dù khiêm tốn về diện tích, đảo lại là nơi cư trú đông đúc của nhiều loài chim biển làm tổ trên vách đá, cùng những đàn hải cẩu thường phơi mình trên các mỏm đá quanh đảo. Vì thế, đảo trở thành điểm đến hấp dẫn cho các tour du thuyền ngắm động vật hoang dã và câu cá biển xuất phát từ Magadan. Lướt quanh đảo, du khách có thể quan sát “thành phố chim” ồn ã, bắt gặp hải cẩu tò mò và tận hưởng khung cảnh biển đảo hoang sơ đặc trưng của bờ Okhotsk. Với người yêu thiên nhiên, đây là một trong những trải nghiệm ven biển đáng nhớ ở vùng Magadan.",
    [
        "Hòn đảo nhỏ với cái tên độc đáo «Đảo Hiểu Lầm» ngoài khơi tây Magadan.",
        "Nơi trú ngụ của các đàn chim biển và hải cẩu – điểm ngắm động vật hoang dã.",
        "Đích đến của các tour du thuyền, câu cá trên vịnh Taui – biển Okhotsk.",
    ],
    {
        "hours_vi": "Chỉ tới được bằng thuyền/tour; phụ thuộc thời tiết và mùa.",
        "ticket_vi": "Theo giá tour du thuyền (thu phí).",
        "duration_vi": "Tour thường nửa ngày.",
        "best_time_vi": "Mùa hè (tháng 6–9), khi biển lặng và chim biển làm tổ đông đúc.",
        "tips_vi": "Đặt tour thuyền có phép; mang áo ấm chống gió biển, đồ chống say sóng và ống nhòm để ngắm chim, hải cẩu.",
    },
    [
        {"title": "VisitKolyma — Остров Недоразумения", "url": "https://visitkolyma.ru/sights/"},
        {"title": "Wikipedia (RU) — Остров Недоразумения", "url": "https://ru.wikipedia.org/wiki/Остров_Недоразумения"},
    ],
    ["park_garden", "island", "birds", "wildlife", "sea-of-okhotsk", "magadan"],
    maps_text("Остров Недоразумения", "Магаданская область", "Nedorazumeniya Island", "Magadan", 59.59, 150.40),
))

# 22) Ямские острова / остров Матыкиль (Магаданский заповедник) ----------------
RECORDS.append(rec(
    "yamskie-islands-matykil-magadan",
    "Quần đảo Yamskie - đảo Matykil (Ostrova Yamskie, Khu bảo tồn Magadansky)",
    "Ямские острова (остров Матыкиль), Магаданский заповедник",
    "Yamsky Islands (Matykil), Magadansky Nature Reserve",
    ["park_garden"],
    59.3292, 155.5608,
    "Vịnh Shelikhov, biển Okhotsk, thuộc cụm Yamsky của Khu bảo tồn thiên nhiên Magadansky, tỉnh Magadan, Nga.",
    "Quần đảo hoang sơ giữa vịnh Shelikhov, nơi có một trong những đàn chim biển làm tổ lớn nhất Viễn Đông Nga (hàng triệu con) cùng các bầy sư tử biển Steller. Là “viên ngọc” của Khu bảo tồn thiên nhiên Magadansky.",
    "Ямские острова (nổi bật nhất là đảo Matykil) là cụm đảo đá nằm ở phần nam vịnh Shelikhov, thuộc cụm Yamsky của Khu bảo tồn thiên nhiên Magadansky – khu dự trữ thiên nhiên nghiêm ngặt được lập năm 1982. Nơi đây được ví như một trong những “thành phố chim” lớn nhất và ngoạn mục nhất của toàn miền Viễn Đông Nga: hàng triệu cá thể chim biển – hải âu cổ rụt (puffin), chim guillemot, mòng biển, chim kittiwake – tụ về làm tổ dày đặc trên các vách đá dựng đứng. Vùng nước quanh đảo giàu dinh dưỡng còn nuôi dưỡng những bầy sư tử biển Steller (sivuch) khổng lồ nằm phơi trên đá, cùng nhiều loài thú biển như cá voi, hải cẩu. Do là khu bảo tồn nghiêm ngặt và nằm rất xa, việc tiếp cận chỉ qua các chuyến khảo sát – du thuyền có tổ chức và giấy phép; nhưng với người đam mê thiên nhiên hoang dã, cảnh tượng và âm thanh của quần thể chim, thú biển nơi đây là trải nghiệm hiếm có bậc nhất nước Nga.",
    [
        "Một trong những đàn chim biển làm tổ lớn nhất Viễn Đông Nga (hàng triệu con).",
        "Bầy sư tử biển Steller và nhiều loài thú biển quanh đảo Matykil.",
        "“Viên ngọc” của Khu bảo tồn thiên nhiên Magadansky (lập năm 1982).",
    ],
    {
        "hours_vi": "Khu bảo tồn nghiêm ngặt; chỉ vào được khi có giấy phép và qua tour/khảo sát có tổ chức.",
        "ticket_vi": "Theo chi phí chuyến du thuyền – khảo sát (cao, do vị trí xa xôi).",
        "duration_vi": "Thường là chuyến nhiều ngày bằng tàu.",
        "best_time_vi": "Mùa hè (tháng 6–8), mùa chim làm tổ và biển tương đối lặng.",
        "tips_vi": "Phải liên hệ ban quản lý khu bảo tồn để xin phép; chuẩn bị cho điều kiện biển khắc nghiệt, mang ống nhòm và máy ảnh tele.",
    },
    [
        {"title": "Wikipedia (RU) — Магаданский заповедник", "url": "https://ru.wikipedia.org/wiki/Магаданский_заповедник"},
        {"title": "VisitKolyma — Ямский архипелаг", "url": "https://visitkolyma.ru/sights/yamskiy-arkhipelag-/"},
    ],
    ["park_garden", "nature-reserve", "birds", "steller-sea-lion", "wildlife", "magadansky", "magadan"],
    maps_text("Ямские острова остров Матыкиль", "Магаданская область", "Yamsky Islands Matykil", "Magadan Oblast", 59.3292, 155.5608),
))

# 23) Колымская ГЭС ------------------------------------------------------------
RECORDS.append(rec(
    "kolyma-hpp-sinegorye-magadan",
    "Nhà máy thuỷ điện Kolyma (Kolymskaya GES)",
    "Колымская ГЭС имени Фриштера",
    "Kolyma Hydroelectric Power Station",
    ["other"],
    62.058333, 150.416667,
    "Gần thị trấn Sinegorye (Sinegorye), huyện Yagodninsky, trên sông Kolyma, tỉnh Magadan, Nga.",
    "Nhà máy thuỷ điện lớn nhất vùng Kolyma và là một trong những công trình đập cao nhất nước Nga, xây trên sông Kolyma gần thị trấn Sinegorye. Con đập đá khổng lồ và hồ chứa mênh mông là điểm nhấn kỹ thuật ấn tượng giữa núi rừng viễn đông.",
    "Nhà máy thuỷ điện Kolyma trên sông Kolyma, gần thị trấn Sinegorye, là nguồn điện chủ lực cung cấp cho gần như toàn bộ tỉnh Magadan. Được khởi công từ thập niên 1970 và đưa vào vận hành dần trong các thập niên sau, đây là công trình thuỷ điện lớn nhất vùng, với con đập đá đổ (rock-fill) thuộc hàng cao nhất nước Nga – một kỳ tích xây dựng trong điều kiện băng giá vĩnh cửu và khí hậu khắc nghiệt bậc nhất hành tinh. Phía trên đập, hồ chứa Kolyma trải dài hàng chục km giữa núi rừng taiga, tạo nên cảnh quan hồ – núi hùng vĩ. Thị trấn Sinegorye được xây riêng để phục vụ nhà máy, gắn liền với câu chuyện chinh phục thiên nhiên của những người thợ Xô-viết. Với du khách trên cung đường Kolyma, con đập và hồ chứa là điểm dừng ngoạn mục, minh chứng cho quy mô công nghiệp hoá đã đặt dấu ấn lên vùng đất hoang vu này.",
    [
        "Thuỷ điện lớn nhất vùng Kolyma, cấp điện cho gần như toàn tỉnh Magadan.",
        "Đập đá đổ thuộc hàng cao nhất nước Nga, xây trên nền băng giá vĩnh cửu.",
        "Hồ chứa Kolyma mênh mông giữa núi rừng taiga – cảnh quan hồ núi hùng vĩ.",
    ],
    {
        "hours_vi": "Là công trình năng lượng đang vận hành – không tham quan bên trong tự do; ngắm cảnh đập/hồ từ bên ngoài.",
        "ticket_vi": "Không bán vé; tham quan có tổ chức cần liên hệ trước.",
        "duration_vi": "Khoảng 30–60 phút ngắm cảnh bên ngoài.",
        "best_time_vi": "Mùa hè, khi đường Kolyma dễ đi; mùa xả nước cảnh đập ấn tượng.",
        "tips_vi": "Đây là công trình an ninh – không quay phim/chụp khu vực hạn chế; kết hợp trên hành trình đường Kolyma qua Sinegorye.",
    },
    [
        {"title": "Wikipedia (RU) — Колымская ГЭС", "url": "https://ru.wikipedia.org/wiki/Колымская_ГЭС"},
        {"title": "EnergyBase.ru — Колымская ГЭС", "url": "https://energybase.ru/power-plant/Kolyma_HPP"},
    ],
    ["other", "hydro-power", "dam", "kolyma-river", "sinegorye", "magadan"],
    maps_text("Колымская ГЭС", "Синегорье", "Kolyma Hydroelectric Station", "Sinegorye", 62.058333, 150.416667),
))

# 24) Бутугычаг ----------------------------------------------------------------
RECORDS.append(rec(
    "butugychag-gulag-magadan",
    "Butugychag - trại lao động & mỏ uranium bỏ hoang (Butygychag)",
    "Бутугычаг (заброшенный лагерь и урановый рудник)",
    "Butugychag (abandoned Gulag camp and uranium mine)",
    ["other"],
    61.316667, 149.188889,
    "Huyện Tenkinsky, thung lũng suối Butugychag, tỉnh Magadan, Nga.",
    "Một trong những di tích Gulag ám ảnh nhất Kolyma: quần thể trại lao động và mỏ khai thác thiếc, uranium bỏ hoang giữa vùng núi hoang vu. Những dãy nhà đá, đường hầm và nghĩa địa tù nhân còn lại là chứng tích lạnh người về lịch sử đàn áp.",
    "Butugychag (theo tiếng Even nghĩa gần với “thung lũng chết”) là một trong những địa danh Gulag khét tiếng và bi thảm nhất vùng Kolyma. Từ thập niên 1930–50, tại đây tù nhân bị đưa tới khai thác thiếc và về sau là quặng uranium – công việc cực nhọc trong điều kiện phóng xạ và giá lạnh khủng khiếp, khiến tỷ lệ tử vong rất cao. Ngày nay, giữa vùng núi cao hoang vu của huyện Tenkinsky, khu trại bỏ hoang vẫn còn lại những dãy nhà giam bằng đá, xưởng tuyển quặng, đường hầm, thiết bị rỉ sét và đặc biệt là các nghĩa địa tù nhân với những cột mộ đánh số thay vì tên. Khung cảnh tĩnh lặng, khắc nghiệt và nặng trĩu ấy biến Butugychag thành điểm đến của “du lịch ký ức” – nơi hành hương của những người muốn tận mắt đối diện với quá khứ đau thương. Việc tiếp cận rất khó khăn, đòi hỏi xe địa hình, hướng dẫn viên và sự chuẩn bị kỹ; nhưng với nhiều người, đó là trải nghiệm lịch sử sâu sắc và day dứt bậc nhất ở Kolyma.",
    [
        "Quần thể trại lao động và mỏ thiếc – uranium bỏ hoang, biểu tượng bi thảm của Gulag Kolyma.",
        "Nhà giam đá, đường hầm, thiết bị rỉ sét và nghĩa địa tù nhân đánh số còn lại.",
        "Điểm đến của “du lịch ký ức”, đối diện trực tiếp với lịch sử đàn áp Stalin.",
    ],
    {
        "hours_vi": "Di tích ngoài trời hoang vu; không có dịch vụ – chỉ tới được qua chuyến đi có tổ chức.",
        "ticket_vi": "Không bán vé; chi phí thuê xe địa hình và hướng dẫn viên.",
        "duration_vi": "Chuyến đi thường trọn ngày hoặc nhiều ngày từ Magadan.",
        "best_time_vi": "Mùa hè (tháng 7–8), khi đường mòn khô ráo và tuyết tan.",
        "tips_vi": "Đường rất khó, cần xe 4x4 và người dẫn đường; lưu ý nguy cơ phóng xạ tồn dư ở khu mỏ; giữ thái độ trang nghiêm nơi tưởng niệm.",
    },
    [
        {"title": "Wikipedia (RU) — Бутугычаг", "url": "https://ru.wikipedia.org/wiki/Бутугычаг"},
        {"title": "Kolymastory.ru — Бутугычаг", "url": "https://www.kolymastory.ru/"},
    ],
    ["other", "gulag", "ghost-town", "mine", "dark-tourism", "tenkinsky", "magadan"],
    maps_text("Бутугычаг", "Магаданская область", "Butugychag", "Magadan Oblast", 61.316667, 149.188889),
))

# 25) Серпантинка (мемориал ГУЛАГ) ---------------------------------------------
RECORDS.append(rec(
    "serpantinka-memorial-magadan",
    "Serpantinka - đài tưởng niệm nạn nhân Gulag (Serpantinka)",
    "Серпантинка (место расстрелов и мемориал)",
    "Serpantinka (Gulag execution site and memorial)",
    ["monument"],
    62.702778, 150.015,
    "Gần làng Yagodnoye (Yagodnoye), huyện Yagodninsky, trên đường Kolyma, tỉnh Magadan, Nga.",
    "Nơi từng là trại giam trung chuyển và điểm hành quyết khét tiếng trong thời kỳ Đại thanh trừng ở Kolyma, nay có đài tưởng niệm các nạn nhân. Một địa điểm ký ức lặng lẽ nhưng nặng trĩu bên đường Kolyma.",
    "Serpantinka, gần làng Yagodnoye, là một trong những cái tên đáng sợ nhất trong lịch sử Gulag vùng Kolyma. Cuối thập niên 1930, trong cao trào Đại thanh trừng, nơi đây hoạt động như một nhà tù trung chuyển và điểm hành quyết, nơi hàng nghìn tù nhân bị xử bắn hoặc chết vì điều kiện giam giữ khủng khiếp. Bản thân toà nhà trại xưa không còn, nhưng địa điểm đã trở thành nơi tưởng niệm: một tượng đài – bia đá được dựng lên để tưởng nhớ những người đã ngã xuống, thường có hoa và nến do người thân, du khách để lại. Nằm ở khu vực hẻo lánh bên đường Kolyma, Serpantinka là điểm dừng chân trầm mặc trên hành trình khám phá “con đường xương trắng”, nhắc nhở về quy mô bi kịch của các cuộc đàn áp. Đến đây, người ta không tham quan mà đến để tưởng niệm và suy ngẫm về một chương đen tối của lịch sử.",
    [
        "Từng là điểm hành quyết khét tiếng thời Đại thanh trừng ở Kolyma.",
        "Nay có đài – bia tưởng niệm các nạn nhân Gulag, thường có hoa và nến.",
        "Điểm ký ức trầm mặc bên “con đường xương trắng” Kolyma.",
    ],
    {
        "hours_vi": "Đài tưởng niệm ngoài trời, tự do; khu vực hẻo lánh.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Mùa hè, khi đường Kolyma dễ đi.",
        "tips_vi": "Đây là nơi tưởng niệm – giữ thái độ trang nghiêm; kết hợp trên hành trình đường Kolyma qua Yagodnoye.",
    },
    [
        {"title": "Tour.kolyma.ru — Серпантинка", "url": "https://tour.kolyma.ru/"},
        {"title": "Wikipedia (RU) — Серпантинка", "url": "https://ru.wikipedia.org/wiki/Серпантинка"},
    ],
    ["monument", "gulag", "memorial", "soviet-repression", "kolyma-highway", "yagodninsky", "magadan"],
    maps_text("Серпантинка мемориал", "Магаданская область", "Serpantinka Memorial", "Yagodnoye", 62.702778, 150.015),
))


def main():
    path = os.path.join(REGIONS, f"{REGION}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    existing_slugs = {p.get("slug") for p in data}
    existing_ids = {p.get("id") for p in data}

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
