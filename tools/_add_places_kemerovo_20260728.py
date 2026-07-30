# -*- coding: utf-8 -*-
"""_add_places_kemerovo_20260728.py — VÙNG: Tỉnh Kemerovo — Kuzbass (Кемеровская область — Кузбасс)
(lần chạy tự động 2026-07-28).

Bối cảnh: kemerovo.json hiện có 7 địa điểm. Bổ sung 25 địa điểm THẬT SỰ nổi tiếng/đặc sắc
CÒN THIẾU, đa dạng loại hình → đưa vùng lên 32 (≥30).

Federal district: Сибирский федеральный округ → "Vùng Siberia". region_name_vi = "Tỉnh Kemerovo"
(giữ y như 7 bản ghi cũ).

Phân bố loại hình (25 bản ghi mới):
- church (4): Знаменский собор (Кемерово), Спасо-Преображенский собор (Новокузнецк),
  Собор Рождества Христова (Новокузнецк), Свято-Серафимо-Покровский монастырь (Ленинск-Кузнецкий).
- museum (7): Кузбасский краеведческий музей, Музей ИЗО Кузбасса (Кемерово); музей Достоевского,
  Новокузнецкий краеведческий музей (Новокузнецк); Музей этнографии Горной Шории (Таштагол);
  Музей-заповедник «Шестаково»; Экомузей «Тюльберский городок».
- theatre (3): Театр драмы им. Луначарского, Музыкальный театр Кузбасса (Кемерово);
  Новокузнецкий драматический театр.
- monument (4): Парк Ангелов, Мемориал Славы (Кемерово); Скульптура «Золотая Шория» (Таштагол);
  Бульвар Героев (Новокузнецк).
- park_garden (5): Сосновый бор / Рудничный бор (Кемерово); Шорский национальный парк;
  озеро Большой Берчикуль; Липовый остров (Кузедеево); заповедник «Кузнецкий Алатау».
- square_street (1): Площадь Советов (Кемерово).
- other (1): скала «Царские Ворота» на р. Мрассу (kỳ quan đá tự nhiên).

TOẠ ĐỘ — xác minh chéo 2026-07-28 (2GIS point center [đã lật đúng lon,lat→lat,lon], sobory.ru,
ru.wikipedia geohack, Yandex Maps, okolo.city, culttourism, geocaching.su). Phạm vi Kemerovo:
lat ~52.0–56.9; lon ~84.5–89.3 — tất cả toạ độ nằm trong phạm vi, KHÔNG đảo lat/lon.
Các điểm toạ độ đại diện/độ tin cậy trung bình đã ghi chú: Мемориал Славы (GPS culttourism),
Царские Ворота (okolo.city crowdsource), Липовый остров (geocaching), Шорский НП (điểm đại diện
trong ranh giới; trụ sở ở Таштагол), Кузнецкий Алатау (điểm quản lý ở Междуреченск; khối núi ở
phía tây). Địa điểm không xác minh được toạ độ tin cậy đã BỎ QUA — KHÔNG bịa.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_kemerovo_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "kemerovo"
REGION_NAME_VI = "Tỉnh Kemerovo"
FD = "Vùng Siberia"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def maps_org(yandex_org_url, name_en, city_en):
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": yandex_org_url,
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

# ==================================================================================
# KEMEROVO (thủ phủ)
# ==================================================================================

# 1) Знаменский кафедральный собор -------------------------------------------------
RECORDS.append(rec(
    "znamensky-cathedral-kemerovo",
    "Nhà thờ chính tòa Znamensky (Nhà thờ Đức Mẹ Dấu Chỉ; phiên âm: Dna-men-xki)",
    "Знаменский кафедральный собор",
    "Znamensky Cathedral",
    ["church"],
    55.340183, 86.099268,
    "Phố Sobornaya (ул. Соборная), TP. Kemerovo, tỉnh Kemerovo (Kuzbass), Nga",
    "Znamensky là nhà thờ chính tòa lớn nhất của Kemerovo, khối nhà thờ trắng - vàng năm mái vòm dát vàng nổi bật bên bờ sông Iskitimka. Được xây lại sau thời Xô Viết và khánh thành cuối thập niên 1990, đây là trung tâm tinh thần của cả vùng Kuzbass.",
    "Nhà thờ chính tòa Znamensky (mang tên biểu tượng Đức Mẹ 'Dấu Chỉ') là ngôi thánh đường Chính thống giáo lớn và trang nghiêm bậc nhất tỉnh Kemerovo. Công trình được khởi công đầu thập niên 1990 trên nền một nhà thờ cũ từng bị phá bỏ thời Xô Viết, và khánh thành năm 1996 nhân dịp kỷ niệm nền Chính thống giáo ở Kuzbass. Với khối kiến trúc bề thế cao gần 50 mét, tường trắng điểm vàng cùng năm mái vòm hình củ hành dát vàng lấp lánh, nhà thờ có thể chứa tới vài nghìn người và trở thành nhà thờ mẹ của giáo phận Kemerovo. Bên trong là những bức tường chạm khắc, tranh thánh và một bàn thờ mạ vàng công phu. Tọa lạc gần bờ sông Iskitimka ở trung tâm thành phố, Znamensky vừa là nơi cử hành các đại lễ tôn giáo, vừa là một điểm nhấn kiến trúc dễ nhận ra của Kemerovo.",
    [
        "Nhà thờ chính tòa lớn nhất Kemerovo, biểu tượng đời sống Chính thống giáo Kuzbass",
        "Năm mái vòm dát vàng cùng khối kiến trúc trắng - vàng cao gần 50 mét",
        "Khánh thành năm 1996, xây trên nền nhà thờ cũ bị phá thời Xô Viết",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày phục vụ lễ, thường khoảng 7:00–19:00; các thánh lễ sáng và chiều.",
        "ticket_vi": "Miễn phí vào tham quan và dự lễ.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Quanh năm; đẹp nhất vào các dịp đại lễ Chính thống giáo (Phục Sinh, Giáng Sinh).",
        "tips_vi": "Ăn mặc kín đáo; nữ nên trùm khăn khi vào; giữ yên lặng trong giờ lễ; hạn chế chụp ảnh sát bàn thờ.",
    },
    [
        {"title": "Sobory.ru — Знаменский собор (Кемерово)", "url": "https://sobory.ru/article/?object=10787"},
        {"title": "Trang giáo xứ Znamensky", "url": "https://zsoborkem.cerkov.ru/"},
    ],
    ["church", "cathedral", "orthodox", "kemerovo", "kuzbass", "landmark"],
    maps_text("Знаменский кафедральный собор", "Кемерово", "Znamensky Cathedral", "Kemerovo", 55.340183, 86.099268),
    official_site="https://zsoborkem.cerkov.ru/",
))

# 2) Кузбасский государственный краеведческий музей --------------------------------
RECORDS.append(rec(
    "kuzbass-regional-museum-kemerovo",
    "Bảo tàng lịch sử - địa chí bang Kuzbass (Bảo tàng địa phương Kemerovo; phiên âm: Cra-ê-vét-che-xki)",
    "Кузбасский государственный краеведческий музей",
    "Kuzbass State Museum of Local Lore",
    ["museum"],
    55.356140, 86.080377,
    "Đại lộ Sovetsky (Советский пр.) số 51, TP. Kemerovo, tỉnh Kemerovo (Kuzbass), Nga",
    "Đây là bảo tàng lâu đời nhất tỉnh Kemerovo, thành lập năm 1929, lưu giữ toàn bộ câu chuyện thiên nhiên và lịch sử của vùng Kuzbass. Bộ sưu tập trải từ hóa thạch, khoáng sản than đá đến đời sống các dân tộc bản địa Siberia và lịch sử công nghiệp.",
    "Bảo tàng lịch sử - địa chí bang Kuzbass (trước đây là Bảo tàng địa phương tỉnh Kemerovo) là bảo tàng cổ nhất và lớn nhất vùng, ra đời năm 1929. Với hàng trăm nghìn hiện vật, bảo tàng chia thành nhiều phân khu: khu thiên nhiên trưng bày khoáng vật, mẫu than đá đặc trưng của Kuzbass, hóa thạch và hệ động thực vật Siberia; khu lịch sử kể lại quá trình khai phá vùng đất, đời sống của người Shor và Teleut bản địa, cùng lịch sử hình thành ngành than - luyện kim khổng lồ. Bảo tàng còn có phân khu lịch sử quân sự bên bờ sông Tom. Đây là điểm khởi đầu lý tưởng để hiểu vì sao Kuzbass được mệnh danh là 'trái tim công nghiệp' của Siberia, đồng thời khám phá thiên nhiên hùng vĩ và di sản văn hóa các dân tộc thiểu số nơi đây.",
    [
        "Bảo tàng lâu đời nhất tỉnh Kemerovo (thành lập 1929)",
        "Sưu tập than đá, khoáng vật và hóa thạch đặc trưng vùng Kuzbass",
        "Trưng bày văn hóa các dân tộc bản địa Shor, Teleut và lịch sử công nghiệp",
    ],
    {
        "hours_vi": "Mở cửa từ thứ Ba đến Chủ nhật, khoảng 10:00–18:00; thứ Hai nghỉ (nên kiểm tra lại trang chính thức).",
        "ticket_vi": "Vé vào khoảng 150–250 RUB/khu; có ưu đãi cho học sinh, sinh viên, người cao tuổi.",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Quanh năm; thích hợp cho ngày thời tiết xấu.",
        "tips_vi": "Bảo tàng có nhiều phân khu ở địa chỉ khác nhau (lịch sử, thiên nhiên, quân sự) — chọn khu quan tâm; nên đi cùng hướng dẫn viên để hiểu sâu.",
    },
    [
        {"title": "Wikipedia (RU) — Кузбасский краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Кузбасский_государственный_краеведческий_музей"},
        {"title": "Trang chính thức", "url": "https://kuzbasskray.ru/"},
    ],
    ["museum", "local-lore", "history", "nature", "kemerovo", "kuzbass"],
    maps_text("Кузбасский государственный краеведческий музей", "Кемерово", "Kuzbass State Museum of Local Lore", "Kemerovo", 55.356140, 86.080377),
    official_site="https://kuzbasskray.ru/",
))

# 3) Музей изобразительных искусств Кузбасса ---------------------------------------
RECORDS.append(rec(
    "kuzbass-fine-arts-museum-kemerovo",
    "Bảo tàng Mỹ thuật Kuzbass (phiên âm: Cút-bát)",
    "Музей изобразительных искусств Кузбасса",
    "Museum of Fine Arts of Kuzbass",
    ["museum"],
    55.356331, 86.083274,
    "Đại lộ Sovetsky (Советский пр.) số 48, TP. Kemerovo, tỉnh Kemerovo (Kuzbass), Nga",
    "Bảo tàng Mỹ thuật Kuzbass là bộ sưu tập nghệ thuật tạo hình lớn nhất vùng, mở cửa từ năm 1969. Nơi đây lưu giữ hội họa, đồ họa, điêu khắc và nghệ thuật trang trí Nga, cùng tác phẩm của các họa sĩ Siberia và nghệ nhân dân gian Shor.",
    "Bảo tàng Mỹ thuật Kuzbass mở cửa năm 1969 và trở thành trung tâm nghệ thuật tạo hình quan trọng nhất tỉnh Kemerovo. Bộ sưu tập gồm hàng nghìn tác phẩm hội họa, đồ họa, điêu khắc và nghệ thuật trang trí - ứng dụng, trải dài từ nghệ thuật Nga cổ điển thế kỷ XVIII–XIX đến mỹ thuật Xô Viết và đương đại. Điểm đặc sắc là mảng nghệ thuật Siberia và văn hóa bản địa: các tác phẩm phản ánh thiên nhiên Kuzbass, cùng đồ thủ công, trang phục và nghệ thuật dân gian của người Shor - dân tộc bản địa vùng núi Shoria. Bảo tàng thường xuyên tổ chức triển lãm luân phiên, workshop và các buổi giao lưu, là điểm dừng chân thú vị cho những ai muốn tiếp cận đời sống văn hóa - nghệ thuật của một vùng công nghiệp Siberia.",
    [
        "Bộ sưu tập mỹ thuật lớn nhất tỉnh Kemerovo (từ 1969)",
        "Hội họa, đồ họa, điêu khắc Nga và Xô Viết qua nhiều thời kỳ",
        "Mảng nghệ thuật Siberia và văn hóa dân gian người Shor bản địa",
    ],
    {
        "hours_vi": "Mở cửa từ thứ Ba đến Chủ nhật, khoảng 10:00–18:00; thứ Hai nghỉ.",
        "ticket_vi": "Vé vào khoảng 150–300 RUB; ưu đãi cho học sinh, sinh viên, người cao tuổi.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm; nên xem lịch các triển lãm chuyên đề.",
        "tips_vi": "Kiểm tra lịch triển lãm luân phiên trên trang chính thức; gần Quảng trường Sovetov nên dễ kết hợp tham quan trung tâm.",
    },
    [
        {"title": "Wikipedia (RU) — Музей изобразительных искусств Кузбасса", "url": "https://ru.wikipedia.org/wiki/Музей_изобразительных_искусств_Кузбасса"},
        {"title": "Trang chính thức", "url": "https://kuzbassizo.ru/"},
    ],
    ["museum", "art", "fine-arts", "siberia", "kemerovo", "kuzbass"],
    maps_text("Музей изобразительных искусств Кузбасса", "Кемерово", "Museum of Fine Arts of Kuzbass", "Kemerovo", 55.356331, 86.083274),
    official_site="https://kuzbassizo.ru/",
))

# 4) Площадь Советов ----------------------------------------------------------------
RECORDS.append(rec(
    "sovetov-square-kemerovo",
    "Quảng trường Sovetov (Quảng trường Xô Viết; phiên âm: Xa-vhê-tốp)",
    "Площадь Советов",
    "Sovetov (Soviets) Square",
    ["square_street"],
    55.354966, 86.088053,
    "Đại lộ Sovetsky, trung tâm TP. Kemerovo, tỉnh Kemerovo (Kuzbass), Nga",
    "Quảng trường Sovetov là quảng trường trung tâm và trái tim hành chính của Kemerovo, hình thành từ giữa thế kỷ XX. Xung quanh là các tòa nhà chính quyền, đài phun nước và bức tượng Lenin lớn - phông nền quen thuộc cho các sự kiện, lễ hội của thành phố.",
    "Quảng trường Sovetov là quảng trường chính và không gian công cộng quan trọng nhất của Kemerovo, được quy hoạch từ những năm 1950–1960 theo phong cách kiến trúc Xô Viết bề thế. Đây là nơi tọa lạc tòa nhà chính quyền tỉnh, các cơ quan hành chính, cùng một tượng đài Lenin cỡ lớn nhìn ra quảng trường. Vào mùa hè, những đài phun nước và luống hoa làm quảng trường thêm sinh động; mùa đông, nơi đây biến thành khu vui chơi băng tuyết với cây thông và tượng băng phục vụ dịp Năm Mới. Quảng trường là điểm tổ chức các cuộc diễu hành, lễ hội, hòa nhạc và sự kiện lớn của thành phố. Nằm ngay trục trung tâm, gần các bảo tàng và nhà hát, đây là điểm khởi đầu tự nhiên để dạo bộ khám phá bộ mặt đô thị của thủ phủ Kuzbass.",
    [
        "Quảng trường trung tâm và trái tim hành chính của Kemerovo",
        "Kiến trúc Xô Viết bề thế, tượng đài Lenin và đài phun nước",
        "Nơi diễn ra các lễ hội, diễu hành và khu băng tuyết dịp Năm Mới",
    ],
    {
        "hours_vi": "Không gian công cộng mở, dạo bộ tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Mùa hè cho đài phun nước; cuối tháng 12 – tháng 1 cho khu băng tuyết lễ hội.",
        "tips_vi": "Kết hợp tham quan bảo tàng, nhà hát quanh khu trung tâm; buổi tối quảng trường lên đèn đẹp để chụp ảnh.",
    },
    [
        {"title": "Wikipedia (RU) — Кемерово (центр города)", "url": "https://ru.wikipedia.org/wiki/Кемерово"},
        {"title": "2GIS — Площадь Советов", "url": "https://2gis.ru/kemerovo/geo/704374636544013"},
    ],
    ["square", "city-center", "soviet-architecture", "kemerovo", "kuzbass"],
    maps_text("Площадь Советов", "Кемерово", "Sovetov Square", "Kemerovo", 55.354966, 86.088053),
))

# 5) Театр драмы им. А.В. Луначарского ----------------------------------------------
RECORDS.append(rec(
    "kemerovo-drama-theatre",
    "Nhà hát Kịch Kemerovo mang tên Lunacharsky (phiên âm: Lu-na-chác-xki)",
    "Кемеровский областной театр драмы им. А.В. Луначарского",
    "Kemerovo Regional Drama Theatre named after A.V. Lunacharsky",
    ["theatre"],
    55.355367, 86.080996,
    "Phố Vesennyaya (ул. Весенняя) số 11, TP. Kemerovo, tỉnh Kemerovo (Kuzbass), Nga",
    "Nhà hát Kịch Kemerovo là nhà hát kịch lâu đời nhất vùng, hoạt động từ năm 1934. Tòa nhà mang phong cách tân cổ điển Xô Viết với hàng cột uy nghi là một biểu tượng kiến trúc của trung tâm thành phố.",
    "Nhà hát Kịch tỉnh Kemerovo mang tên nhà văn hóa A.V. Lunacharsky là sân khấu kịch chuyên nghiệp lâu đời nhất Kuzbass, thành lập năm 1934. Tòa nhà hiện nay được xây dựng giữa thập niên 1960 theo phong cách tân cổ điển (Stalin) với mặt tiền hàng cột đồ sộ, trở thành một trong những công trình kiến trúc tiêu biểu nhất của Kemerovo. Đoàn kịch dàn dựng cả kịch kinh điển Nga và thế giới (Chekhov, Ostrovsky, Shakespeare...) lẫn các vở đương đại, phục vụ nhiều thế hệ khán giả. Nằm ngay trung tâm gần Quảng trường Sovetov, nhà hát vừa là trung tâm đời sống sân khấu của tỉnh, vừa là điểm ngắm kiến trúc và chụp ảnh quen thuộc của du khách khi dạo bộ khu trung tâm.",
    [
        "Nhà hát kịch lâu đời nhất Kuzbass (từ 1934)",
        "Kiến trúc tân cổ điển Xô Viết với hàng cột bề thế",
        "Dàn dựng kịch kinh điển Nga - thế giới và các vở đương đại",
    ],
    {
        "hours_vi": "Biểu diễn theo lịch mùa diễn (thường thứ Tư–Chủ nhật, buổi tối); phòng vé mở ban ngày.",
        "ticket_vi": "Vé thường khoảng 300–1.000 RUB tùy vở và vị trí ghế.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ; ngắm bên ngoài khoảng 15 phút.",
        "best_time_vi": "Mùa diễn tháng 9 – tháng 6; nên đặt vé trước cho các vở nổi bật.",
        "tips_vi": "Xem lịch diễn và đặt vé trên trang chính thức; trang phục lịch sự khi vào xem; đến sớm để ngắm nội thất.",
    },
    [
        {"title": "Wikipedia (RU) — Кемеровский театр драмы", "url": "https://ru.wikipedia.org/wiki/Кемеровский_областной_театр_драмы_имени_А._В._Луначарского"},
        {"title": "Trang chính thức", "url": "https://kemdrama.ru/"},
    ],
    ["theatre", "drama", "architecture", "kemerovo", "kuzbass"],
    maps_text("Кемеровский областной театр драмы", "Кемерово", "Kemerovo Drama Theatre", "Kemerovo", 55.355367, 86.080996),
    official_site="https://kemdrama.ru/",
))

# 6) Музыкальный театр Кузбасса им. А. Боброва --------------------------------------
RECORDS.append(rec(
    "kuzbass-musical-theatre-kemerovo",
    "Nhà hát Ca kịch Kuzbass mang tên Bobrov (phiên âm: Bốp-rốp)",
    "Музыкальный театр Кузбасса им. А.К. Боброва",
    "Kuzbass Musical Theatre named after A.K. Bobrov",
    ["theatre"],
    55.356322, 86.085508,
    "Đại lộ Sovetsky (Советский пр.) số 52, TP. Kemerovo, tỉnh Kemerovo (Kuzbass), Nga",
    "Nhà hát Ca kịch Kuzbass là sân khấu nhạc kịch hàng đầu của vùng, dàn dựng operetta, nhạc kịch (musical), opera và ballet. Nằm ngay trung tâm Kemerovo, đây là điểm hẹn văn hóa sôi động của thành phố.",
    "Nhà hát Ca kịch Kuzbass mang tên nghệ sĩ A.K. Bobrov là nhà hát nhạc kịch chủ lực của tỉnh Kemerovo, có nguồn gốc từ đoàn operetta thành lập giữa thế kỷ XX. Sân khấu dàn dựng đa dạng thể loại: operetta cổ điển, nhạc kịch hiện đại (musical), opera, ballet cùng các chương trình hòa nhạc, biểu diễn cho cả người lớn và trẻ em. Tòa nhà nằm trên đại lộ Sovetsky ngay trung tâm, gần Quảng trường Sovetov và cụm bảo tàng, tạo thành một quần thể văn hóa của thủ phủ Kuzbass. Với dàn nghệ sĩ, nhạc công và vũ đoàn riêng, nhà hát là nơi mang đến những buổi tối giải trí chất lượng và cũng là niềm tự hào nghệ thuật của người dân Kemerovo.",
    [
        "Nhà hát nhạc kịch hàng đầu tỉnh Kemerovo (operetta, musical, opera, ballet)",
        "Vị trí trung tâm trên đại lộ Sovetsky, gần cụm bảo tàng - quảng trường",
        "Chương trình đa dạng cho cả người lớn và trẻ em",
    ],
    {
        "hours_vi": "Biểu diễn theo lịch mùa diễn, thường buổi tối và một số suất cuối tuần ban ngày.",
        "ticket_vi": "Vé thường khoảng 400–1.500 RUB tùy chương trình và vị trí ghế.",
        "duration_vi": "Một buổi diễn khoảng 2–2,5 giờ.",
        "best_time_vi": "Mùa diễn tháng 9 – tháng 6.",
        "tips_vi": "Đặt vé trước cho các vở musical/ballet nổi bật; kết hợp dạo trung tâm Sovetsky và Quảng trường Sovetov.",
    },
    [
        {"title": "Wikipedia (RU) — Музыкальный театр Кузбасса", "url": "https://ru.wikipedia.org/wiki/Музыкальный_театр_Кузбасса_имени_А._К._Боброва"},
        {"title": "Trang chính thức", "url": "https://muz42.ru/"},
    ],
    ["theatre", "musical", "operetta", "ballet", "kemerovo", "kuzbass"],
    maps_text("Музыкальный театр Кузбасса", "Кемерово", "Kuzbass Musical Theatre", "Kemerovo", 55.356322, 86.085508),
    official_site="https://muz42.ru/",
))

# 7) Парк Ангелов -------------------------------------------------------------------
RECORDS.append(rec(
    "park-of-angels-kemerovo",
    "Công viên Thiên thần (Đài tưởng niệm Park Angelov; phiên âm: Pác An-ghê-lốp)",
    "Парк Ангелов",
    "Park of Angels (Memorial)",
    ["monument", "park_garden"],
    55.343709, 86.078347,
    "Phố Ordzhonikidze (ул. Орджоникидзе), TP. Kemerovo, tỉnh Kemerovo (Kuzbass), Nga",
    "Công viên Thiên thần là đài tưởng niệm và không gian ký ức dành cho các nạn nhân - phần lớn là trẻ em - trong vụ hỏa hoạn trung tâm thương mại 'Zimnyaya Vishnya' năm 2018. Đây là nơi tưởng nhớ trang nghiêm và lay động lòng người ngay giữa lòng Kemerovo.",
    "Công viên Thiên thần (Park Angelov) được lập nên tại nơi từng là trung tâm thương mại 'Zimnyaya Vishnya', tưởng nhớ 60 nạn nhân, trong đó có rất nhiều trẻ em, đã thiệt mạng trong vụ hỏa hoạn thương tâm ngày 25 tháng 3 năm 2018 - một trong những thảm kịch gây chấn động nước Nga. Sau bi kịch, khu đất được cải tạo thành một công viên tưởng niệm yên tĩnh, với đài kỷ niệm khắc tên các nạn nhân, những tượng thiên thần, khu vườn và không gian cây xanh để mọi người tưởng nhớ và đặt hoa. Đây là nơi người dân Kemerovo tới để tưởng niệm, suy ngẫm và nhắc nhở về giá trị của sự an toàn và tình người. Với du khách, công viên là một điểm dừng chân lặng lẽ, trang nghiêm - nên được ghé thăm với sự tôn trọng và cảm thông sâu sắc.",
    [
        "Đài tưởng niệm 60 nạn nhân vụ hỏa hoạn 'Zimnyaya Vishnya' năm 2018",
        "Tượng thiên thần và đài khắc tên tưởng nhớ, phần lớn là trẻ em",
        "Không gian ký ức trang nghiêm giữa lòng thành phố Kemerovo",
    ],
    {
        "hours_vi": "Không gian ngoài trời mở, có thể viếng thăm mọi lúc; nên đến ban ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm; ngày 25/3 hằng năm là dịp tưởng niệm chính.",
        "tips_vi": "Đây là nơi tưởng niệm - hãy giữ thái độ trang nghiêm, im lặng; có thể đặt hoa; tránh chụp ảnh phản cảm hoặc ồn ào.",
    },
    [
        {"title": "Wikipedia (RU) — Пожар в «Зимней вишне»", "url": "https://ru.wikipedia.org/wiki/Пожар_в_торговом_центре_«Зимняя_вишня»"},
        {"title": "Yandex Maps — Парк Ангелов", "url": "https://yandex.ru/maps/org/park_angelov/231266434460"},
    ],
    ["memorial", "monument", "park", "remembrance", "kemerovo", "kuzbass"],
    maps_org("https://yandex.ru/maps/org/park_angelov/231266434460", "Park of Angels", "Kemerovo"),
))

# 8) Мемориал Славы воинам-кузбассовцам ---------------------------------------------
RECORDS.append(rec(
    "memorial-of-glory-kemerovo",
    "Đài tưởng niệm Vinh quang tưởng nhớ chiến sĩ Kuzbass (phiên âm: Me-mô-ri-an Xla-vư)",
    "Мемориал Славы воинам-кузбассовцам",
    "Memorial of Glory to Kuzbass Soldiers",
    ["monument"],
    55.358310, 86.059740,
    "Phố Vesennyaya, khu vực Bờ kè sông Tom (Притомская набережная), TP. Kemerovo, tỉnh Kemerovo, Nga",
    "Đài tưởng niệm Vinh quang tôn vinh những người con Kuzbass đã ngã xuống trong Chiến tranh Vệ quốc Vĩ đại (1941–1945). Quần thể có Ngọn lửa vĩnh cửu, tượng đài và các phù điêu, là nơi diễn ra lễ tưởng niệm ngày Chiến thắng 9/5.",
    "Đài tưởng niệm Vinh quang các chiến sĩ Kuzbass là quần thể tưởng niệm trung tâm của Kemerovo dành cho những người lính đã hy sinh trong Chiến tranh Vệ quốc Vĩ đại 1941–1945. Quần thể gồm Ngọn lửa vĩnh cửu, tượng đài người lính cùng các bức phù điêu và bia tưởng niệm khắc tên những người con của vùng đất công nghiệp này đã ngã xuống vì Tổ quốc. Nằm ở khu vực gần bờ kè sông Tom, đây là địa điểm trang nghiêm để đặt hoa, tổ chức lễ đổi gác danh dự và các nghi lễ tưởng niệm, đặc biệt vào ngày Chiến thắng 9/5 - dịp người dân toàn thành phố tề tựu. Với du khách, đây là điểm chạm đến lịch sử hào hùng và bi tráng của cả một thế hệ, đồng thời là nơi ngắm cảnh dòng sông Tom.",
    [
        "Ngọn lửa vĩnh cửu tưởng nhớ chiến sĩ Kuzbass hy sinh trong Thế chiến II",
        "Tượng đài, phù điêu và bia khắc tên người ngã xuống",
        "Trung tâm nghi lễ tưởng niệm ngày Chiến thắng 9/5",
    ],
    {
        "hours_vi": "Không gian ngoài trời mở, viếng thăm tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–30 phút.",
        "best_time_vi": "Quanh năm; trang nghiêm nhất vào ngày Chiến thắng 9/5.",
        "tips_vi": "Giữ thái độ tôn nghiêm gần Ngọn lửa vĩnh cửu; kết hợp dạo bờ kè sông Tom gần đó.",
    },
    [
        {"title": "Culttourism — Мемориал Славы (Кемерово)", "url": "https://culttourism.ru/kemerovskaya/kemerovo/memorial_slavy_voinam-kuzbassovcam.html"},
    ],
    ["memorial", "monument", "wwii", "eternal-flame", "kemerovo", "kuzbass"],
    maps_text("Мемориал Славы воинам-кузбассовцам", "Кемерово", "Memorial of Glory", "Kemerovo", 55.358310, 86.059740),
))

# 9) Сосновый бор (Рудничный бор) ---------------------------------------------------
RECORDS.append(rec(
    "sosnovy-bor-park-kemerovo",
    "Rừng thông Sosnovy Bor (Rudnichny Bor; phiên âm: Xót-nô-vưi Bo)",
    "Сосновый бор (Рудничный бор)",
    "Sosnovy Bor (Pine Forest Park)",
    ["park_garden"],
    55.377176, 86.100830,
    "Quận Rudnichny (Рудничный район), TP. Kemerovo, tỉnh Kemerovo (Kuzbass), Nga",
    "Sosnovy Bor (còn gọi Rudnichny bor) là khu rừng thông tự nhiên rộng lớn ngay trong lòng Kemerovo, được xếp hạng khu bảo tồn tự nhiên đặc biệt. Đây là 'lá phổi xanh' của thành phố với đường dạo, làn xe đạp và khu nghỉ ngơi giữa rừng thông cổ thụ.",
    "Sosnovy Bor (Rudnichny bor) là một khu rừng thông tự nhiên hiếm có nằm ngay bên tả ngạn sông Tom, thuộc quận Rudnichny của Kemerovo, và được công nhận là khu bảo tồn tự nhiên đặc biệt (ООПТ) của thành phố. Với những rặng thông cao vút hàng chục năm tuổi trải trên diện tích rộng, đây là nơi người dân đến đi bộ, chạy bộ, đạp xe, trượt tuyết mùa đông và hít thở không khí trong lành. Rừng có hệ thống lối mòn, ghế nghỉ, khu thể thao và không gian dã ngoại, đồng thời giữ vai trò quan trọng trong việc điều hòa khí hậu và bảo vệ hệ sinh thái ven đô. Với du khách, đây là điểm đến thư giãn giữa thiên nhiên mà không cần rời xa trung tâm, đặc biệt dễ chịu vào mùa hè và mùa thu lá vàng.",
    [
        "Khu rừng thông tự nhiên - khu bảo tồn đặc biệt ngay trong lòng Kemerovo",
        "'Lá phổi xanh' với lối dạo bộ, đường xe đạp, khu dã ngoại",
        "Trượt tuyết và đi bộ tuyết mùa đông, tản bộ mát mẻ mùa hè",
    ],
    {
        "hours_vi": "Khu rừng - công viên ngoài trời mở, dạo chơi tự do mọi lúc.",
        "ticket_vi": "Miễn phí (một số dịch vụ thuê thiết bị thể thao có thể thu phí).",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Mùa hè và mùa thu để đi bộ; mùa đông cho trượt tuyết băng đồng.",
        "tips_vi": "Mang giày đi bộ; mùa hè lưu ý bọ ve (kiểm tra người sau khi đi rừng); giữ gìn vệ sinh khu bảo tồn.",
    },
    [
        {"title": "Wikipedia (RU) — Рудничный бор", "url": "https://ru.wikipedia.org/wiki/Рудничный_бор"},
    ],
    ["park", "nature-reserve", "pine-forest", "recreation", "kemerovo", "kuzbass"],
    maps_text("Сосновый бор", "Кемерово", "Sosnovy Bor", "Kemerovo", 55.377176, 86.100830),
))

# ==================================================================================
# NOVOKUZNETSK
# ==================================================================================

# 10) Спасо-Преображенский собор ----------------------------------------------------
RECORDS.append(rec(
    "spaso-preobrazhensky-cathedral-novokuznetsk",
    "Nhà thờ chính tòa Chúa Hiển Dung (Spaso-Preobrazhensky; phiên âm: Xpa-xô Prê-ô-bra-den-xki)",
    "Спасо-Преображенский собор",
    "Spaso-Preobrazhensky (Transfiguration) Cathedral",
    ["church"],
    53.768858, 87.183058,
    "Phố Vodopadnaya (ул. Водопадная) số 18, khu Kuznetsk cổ, TP. Novokuznetsk, tỉnh Kemerovo, Nga",
    "Spaso-Preobrazhensky là nhà thờ đá cổ nhất và biểu tượng của Novokuznetsk, khởi dựng từ đầu thế kỷ XIX ở khu phố Kuznetsk cổ. Ngọn tháp chuông cao vút của nhà thờ là điểm nhấn dễ nhận ra bên dòng sông Tom.",
    "Nhà thờ chính tòa Chúa Hiển Dung (Spaso-Preobrazhensky) là công trình tôn giáo tiêu biểu và lâu đời nhất của Novokuznetsk, tọa lạc tại khu phố lịch sử Kuznetsk cổ bên bờ sông Tom. Ngôi nhà thờ đá được khởi công năm 1792 và hoàn thiện qua nhiều giai đoạn đầu thế kỷ XIX, mang phong cách baroque Siberia đặc trưng với tháp chuông cao vươn lên. Thời Xô Viết, nhà thờ bị đóng cửa và hư hại nặng; công cuộc trùng tu kéo dài đã hồi sinh diện mạo lộng lẫy vốn có. Là nhà thờ chính tòa của giáo phận Novokuznetsk, công trình vừa là trung tâm hành hương, vừa là một mốc lịch sử gắn với những ngày đầu của thành phố. Từ khu vực nhà thờ, du khách có thể kết hợp tham quan Pháo đài Kuznetsk gần kề - hai biểu tượng của Kuznetsk cổ.",
    [
        "Nhà thờ đá cổ nhất Novokuznetsk (khởi công 1792), phong cách baroque Siberia",
        "Tháp chuông cao là điểm nhấn của khu Kuznetsk cổ bên sông Tom",
        "Nhà thờ chính tòa giáo phận, gần Pháo đài Kuznetsk lịch sử",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày phục vụ lễ, thường khoảng 8:00–19:00.",
        "ticket_vi": "Miễn phí vào tham quan và dự lễ.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Quanh năm; đẹp vào các đại lễ Chính thống, đặc biệt lễ Chúa Hiển Dung (tháng 8).",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn; kết hợp tham quan Pháo đài Kuznetsk gần đó trong cùng buổi.",
    },
    [
        {"title": "Sobory.ru — Спасо-Преображенский собор (Новокузнецк)", "url": "https://sobory.ru/article/?object=08954"},
        {"title": "Trang chính thức", "url": "https://xn--80aasqgdhy.xn--p1ai/"},
    ],
    ["church", "cathedral", "orthodox", "baroque", "novokuznetsk", "kuzbass"],
    maps_text("Спасо-Преображенский собор", "Новокузнецк", "Spaso-Preobrazhensky Cathedral", "Novokuznetsk", 53.768858, 87.183058),
))

# 11) Литературно-мемориальный музей Ф.М. Достоевского ------------------------------
RECORDS.append(rec(
    "dostoevsky-museum-novokuznetsk",
    "Bảo tàng lưu niệm văn học Dostoevsky (phiên âm: Đô-xtôi-ép-xki)",
    "Литературно-мемориальный музей Ф.М. Достоевского",
    "F.M. Dostoevsky Literary-Memorial Museum",
    ["museum"],
    53.763197, 87.190516,
    "Phố Dostoevsky (ул. Достоевского) số 40, khu Kuznetsk cổ, TP. Novokuznetsk, tỉnh Kemerovo, Nga",
    "Bảo tàng nằm trong ngôi nhà gỗ nơi văn hào Fyodor Dostoevsky từng lưu lại và kết hôn tại Kuznetsk năm 1857. Đây là bảo tàng lưu niệm hiếm hoi tái hiện một chương đời đặc biệt của nhà văn vĩ đại người Nga.",
    "Bảo tàng lưu niệm văn học Dostoevsky ở Novokuznetsk gắn với một chương đời ít được biết đến của đại văn hào: trong những năm bị lưu đày ở Siberia, Fyodor Dostoevsky đã nhiều lần đến Kuznetsk và làm lễ cưới với Maria Isaeva tại đây năm 1857. Bảo tàng đặt trong ngôi nhà gỗ cổ nơi ông từng ở, tái hiện không gian sinh hoạt thế kỷ XIX cùng những hiện vật, thư từ, bản thảo và tư liệu về mối tình, cuộc hôn nhân và giai đoạn Siberia đã ảnh hưởng sâu sắc đến sáng tác của nhà văn. Đây là một trong số ít bảo tàng Dostoevsky trên thế giới, điểm đến ý nghĩa cho những ai yêu văn học Nga, giúp hiểu thêm về con người phía sau những kiệt tác như 'Tội ác và Trừng phạt'.",
    [
        "Ngôi nhà nơi Dostoevsky lưu lại và kết hôn ở Kuznetsk (1857)",
        "Một trong số ít bảo tàng tưởng niệm Dostoevsky trên thế giới",
        "Không gian và hiện vật tái hiện giai đoạn Siberia của nhà văn",
    ],
    {
        "hours_vi": "Mở cửa từ thứ Ba đến Chủ nhật, khoảng 10:00–18:00; thứ Hai nghỉ.",
        "ticket_vi": "Vé vào khoảng 150–250 RUB; ưu đãi cho học sinh, sinh viên, người cao tuổi.",
        "duration_vi": "Khoảng 45 phút – 1 giờ.",
        "best_time_vi": "Quanh năm; phù hợp mọi mùa.",
        "tips_vi": "Nên đi kèm hướng dẫn viên để hiểu bối cảnh; nằm trong khu Kuznetsk cổ, dễ kết hợp Pháo đài Kuznetsk và nhà thờ Spaso-Preobrazhensky.",
    },
    [
        {"title": "Wikipedia (RU) — Музей Достоевского в Новокузнецке", "url": "https://ru.wikipedia.org/wiki/Литературно-мемориальный_музей_Ф._М._Достоевского_(Новокузнецк)"},
        {"title": "Trang chính thức", "url": "https://dom-dostoevskogo.ru/"},
    ],
    ["museum", "literature", "dostoevsky", "memorial", "novokuznetsk", "kuzbass"],
    maps_text("Музей Достоевского", "Новокузнецк", "Dostoevsky Museum", "Novokuznetsk", 53.763197, 87.190516),
    official_site="https://dom-dostoevskogo.ru/",
))

# 12) Новокузнецкий драматический театр ---------------------------------------------
RECORDS.append(rec(
    "novokuznetsk-drama-theatre",
    "Nhà hát Kịch Novokuznetsk (phiên âm: Nô-vô-cút-nhét-xcơ)",
    "Новокузнецкий драматический театр",
    "Novokuznetsk Drama Theatre",
    ["theatre"],
    53.757275, 87.121097,
    "Đại lộ Metallurgov (пр. Металлургов) số 28, TP. Novokuznetsk, tỉnh Kemerovo, Nga",
    "Nhà hát Kịch Novokuznetsk là một trong những nhà hát đẹp nhất Kuzbass, tòa nhà tân cổ điển Xô Viết hoành tráng nằm trên đại lộ Metallurgov. Đây là trung tâm sân khấu của thành phố luyện kim lớn thứ hai vùng.",
    "Nhà hát Kịch Novokuznetsk là sân khấu kịch chủ lực của thành phố, với lịch sử từ thập niên 1930 gắn liền quá trình hình thành đô thị công nghiệp Novokuznetsk (thời kỳ là Stalinsk). Tòa nhà hiện nay xây giữa thế kỷ XX theo phong cách tân cổ điển Stalin, với mặt tiền hàng cột, tượng đắp và nội thất lộng lẫy - được xem là một trong những công trình nhà hát đẹp nhất Siberia. Nằm trên đại lộ Metallurgov ở trung tâm khu 'thành phố kiểu mẫu' được quy hoạch bài bản, nhà hát dàn dựng đa dạng từ kịch kinh điển Nga - thế giới đến các vở đương đại và chương trình cho thiếu nhi. Đây vừa là điểm hẹn văn hóa của người dân, vừa là một điểm ngắm kiến trúc nổi bật khi dạo trục trung tâm Novokuznetsk.",
    [
        "Nhà hát kịch tân cổ điển Stalin - một trong những nhà hát đẹp nhất Siberia",
        "Vị trí trung tâm trên đại lộ Metallurgov của thành phố kiểu mẫu",
        "Lịch sử từ thập niên 1930, dàn dựng kịch kinh điển và đương đại",
    ],
    {
        "hours_vi": "Biểu diễn theo lịch mùa diễn, thường buổi tối và một số suất cuối tuần ban ngày.",
        "ticket_vi": "Vé thường khoảng 300–1.200 RUB tùy vở và vị trí ghế.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ; ngắm ngoài khoảng 15 phút.",
        "best_time_vi": "Mùa diễn tháng 9 – tháng 6.",
        "tips_vi": "Đặt vé trước trên trang chính thức; kết hợp dạo đại lộ Metallurgov và cụm kiến trúc trung tâm.",
    },
    [
        {"title": "Wikipedia (RU) — Новокузнецкий драматический театр", "url": "https://ru.wikipedia.org/wiki/Новокузнецкий_драматический_театр"},
        {"title": "Trang chính thức", "url": "https://nvkteatr.ru/"},
    ],
    ["theatre", "drama", "stalin-architecture", "novokuznetsk", "kuzbass"],
    maps_text("Новокузнецкий драматический театр", "Новокузнецк", "Novokuznetsk Drama Theatre", "Novokuznetsk", 53.757275, 87.121097),
    official_site="https://nvkteatr.ru/",
))

# 13) Бульвар Героев (Вечный огонь) -------------------------------------------------
RECORDS.append(rec(
    "boulevard-of-heroes-novokuznetsk",
    "Đại lộ Anh hùng và Ngọn lửa vĩnh cửu (Bulvar Geroev; phiên âm: Bun-va Ghê-rô-ép)",
    "Бульвар Героев",
    "Boulevard of Heroes",
    ["monument", "square_street"],
    53.756005, 87.149073,
    "Bульвар Героев, quận Tsentralny, TP. Novokuznetsk, tỉnh Kemerovo, Nga",
    "Đại lộ Anh hùng là quần thể tưởng niệm trung tâm của Novokuznetsk, tôn vinh những người con của thành phố ngã xuống trong Chiến tranh Vệ quốc Vĩ đại. Trục đi bộ dẫn tới Ngọn lửa vĩnh cửu và bức tường tưởng niệm đầy xúc động.",
    "Đại lộ Anh hùng (Bulvar Geroev) là một trong những không gian tưởng niệm quan trọng và ấn tượng nhất Novokuznetsk. Được khánh thành năm 1975 nhân 30 năm Chiến thắng, đây là một trục đi bộ rộng dẫn tới quần thể đài tưởng niệm gồm Ngọn lửa vĩnh cửu, các bức phù điêu và bức tường ký ức tôn vinh những người dân Novokuznetsk - trong đó nhiều người là công nhân luyện kim - đã hy sinh vì Tổ quốc trong Thế chiến II. Hai bên đại lộ là hàng cây, ghế nghỉ và không gian xanh, biến nơi đây thành vừa là chốn tưởng niệm trang nghiêm, vừa là nơi dạo bộ quen thuộc của người dân. Vào ngày Chiến thắng 9/5, đại lộ trở thành trung tâm của các nghi lễ và dòng người tưởng niệm.",
    [
        "Quần thể tưởng niệm với Ngọn lửa vĩnh cửu (khánh thành 1975)",
        "Trục đi bộ và bức tường ký ức tôn vinh chiến sĩ Novokuznetsk",
        "Trung tâm các nghi lễ ngày Chiến thắng 9/5",
    ],
    {
        "hours_vi": "Không gian ngoài trời mở, dạo bộ và viếng thăm tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Quanh năm; trang nghiêm nhất vào ngày Chiến thắng 9/5.",
        "tips_vi": "Giữ thái độ tôn nghiêm gần Ngọn lửa vĩnh cửu; buổi tối đại lộ lên đèn đẹp để dạo bộ.",
    },
    [
        {"title": "Wikipedia (RU) — Бульвар Героев (Новокузнецк)", "url": "https://ru.wikipedia.org/wiki/Бульвар_Героев_(Новокузнецк)"},
    ],
    ["memorial", "monument", "boulevard", "wwii", "eternal-flame", "novokuznetsk"],
    maps_text("Бульвар Героев", "Новокузнецк", "Boulevard of Heroes", "Novokuznetsk", 53.756005, 87.149073),
))

# 14) Собор Рождества Христова ------------------------------------------------------
RECORDS.append(rec(
    "nativity-cathedral-novokuznetsk",
    "Nhà thờ chính tòa Chúa Giáng Sinh (đài tưởng niệm thợ mỏ; phiên âm: Rát-đê-xtva Khri-xtô-va)",
    "Собор Рождества Христова",
    "Cathedral of the Nativity of Christ",
    ["church", "monument"],
    53.790730, 87.347493,
    "Phố Zyryanovskaya (ул. Зыряновская) số 97а, quận Ordzhonikidze, TP. Novokuznetsk, tỉnh Kemerovo, Nga",
    "Nhà thờ chính tòa Chúa Giáng Sinh là ngôi nhà thờ - đài tưởng niệm dựng lên để tưởng nhớ những người thợ mỏ Kuzbass thiệt mạng trong các tai nạn hầm lò, đặc biệt là thảm họa mỏ Zyryanovskaya. Đây là một trong những nhà thờ mới lớn và ý nghĩa nhất vùng.",
    "Nhà thờ chính tòa Chúa Giáng Sinh ở Novokuznetsk là một quần thể vừa mang ý nghĩa tôn giáo vừa là đài tưởng niệm độc đáo, được xây dựng để tưởng nhớ những người thợ mỏ Kuzbass đã ngã xuống trong các tai nạn hầm lò - khởi nguồn từ thảm họa mỏ Zyryanovskaya năm 1997 khiến 67 thợ mỏ thiệt mạng. Khánh thành năm 2013 sau nhiều năm xây dựng, nhà thờ nổi bật với khối kiến trúc trắng bề thế, các mái vòm dát vàng và không gian nội thất rộng. Trong khuôn viên có nhà nguyện tưởng niệm và bia khắc tên các thợ mỏ tử nạn ở khắp vùng Kuzbass, biến nơi đây thành một địa điểm hành hương và tưởng niệm mang đậm dấu ấn của một vùng đất khai thác than. Đây là điểm đến vừa trang nghiêm về tâm linh, vừa lay động khi kể lại cái giá của lao động dưới lòng đất.",
    [
        "Nhà thờ - đài tưởng niệm thợ mỏ Kuzbass tử nạn (thảm họa mỏ Zyryanovskaya)",
        "Khối kiến trúc trắng bề thế, mái vòm dát vàng (khánh thành 2013)",
        "Nhà nguyện tưởng niệm và bia khắc tên thợ mỏ khắp vùng",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày phục vụ lễ, thường khoảng 8:00–19:00.",
        "ticket_vi": "Miễn phí vào tham quan và dự lễ.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Quanh năm; đặc biệt vào lễ Giáng Sinh Chính thống (7/1) và ngày tưởng niệm thợ mỏ.",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn; giữ thái độ tôn nghiêm tại khu tưởng niệm thợ mỏ.",
    },
    [
        {"title": "Wikipedia (RU) — Собор Рождества Христова (Новокузнецк)", "url": "https://ru.wikipedia.org/wiki/Собор_Рождества_Христова_(Новокузнецк)"},
        {"title": "Sobory.ru — Собор Рождества Христова (Новокузнецк)", "url": "https://sobory.ru/article/?object=24488"},
    ],
    ["church", "cathedral", "memorial", "miners", "novokuznetsk", "kuzbass"],
    maps_text("Собор Рождества Христова", "Новокузнецк", "Cathedral of the Nativity of Christ", "Novokuznetsk", 53.790730, 87.347493),
))

# 15) Новокузнецкий краеведческий музей ---------------------------------------------
RECORDS.append(rec(
    "novokuznetsk-local-lore-museum",
    "Bảo tàng lịch sử - địa chí Novokuznetsk (phiên âm: Cra-ê-vét-che-xki)",
    "Новокузнецкий краеведческий музей",
    "Novokuznetsk Museum of Local Lore",
    ["museum"],
    53.760585, 87.117775,
    "Đại lộ Pionersky (Пионерский пр.) số 24, TP. Novokuznetsk, tỉnh Kemerovo, Nga",
    "Đây là một trong những bảo tàng lâu đời nhất vùng Kuzbass, thành lập năm 1927, lưu giữ lịch sử thành phố Kuznetsk - Novokuznetsk từ thời sơ khai đến kỷ nguyên công nghiệp. Bộ sưu tập trải rộng từ khảo cổ, dân tộc học đến lịch sử công nghiệp luyện kim.",
    "Bảo tàng lịch sử - địa chí Novokuznetsk ra đời năm 1927, thuộc hàng bảo tàng lâu đời nhất Kuzbass. Với hàng chục nghìn hiện vật, bảo tàng kể lại toàn bộ hành trình của vùng đất: từ khảo cổ và cổ sinh vật, đời sống các dân tộc bản địa Siberia (người Shor, Teleut), lịch sử pháo đài và thành phố Kuznetsk cổ, cho đến kỷ nguyên xây dựng tổ hợp luyện kim khổng lồ biến Novokuznetsk thành 'thủ đô kim loại' của Siberia. Các phòng trưng bày kết hợp hiện vật gốc, mô hình, tài liệu và ảnh tư liệu, giúp du khách hình dung sự chuyển mình ngoạn mục của một đô thị công nghiệp Xô Viết. Đây là điểm dừng chân lý tưởng để hiểu bối cảnh lịch sử trước khi khám phá Pháo đài Kuznetsk hay khu Kuznetsk cổ.",
    [
        "Một trong những bảo tàng lâu đời nhất Kuzbass (thành lập 1927)",
        "Sưu tập khảo cổ, dân tộc học và lịch sử pháo đài Kuznetsk",
        "Câu chuyện hình thành 'thủ đô kim loại' Novokuznetsk",
    ],
    {
        "hours_vi": "Mở cửa từ thứ Ba đến Chủ nhật, khoảng 10:00–18:00; thứ Hai nghỉ.",
        "ticket_vi": "Vé vào khoảng 150–250 RUB; ưu đãi cho học sinh, sinh viên, người cao tuổi.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm; phù hợp cho ngày thời tiết xấu.",
        "tips_vi": "Kết hợp với Pháo đài Kuznetsk và bảo tàng Dostoevsky để có bức tranh trọn vẹn về lịch sử thành phố.",
    },
    [
        {"title": "Wikipedia (RU) — Новокузнецкий краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Новокузнецкий_краеведческий_музей"},
        {"title": "Trang chính thức", "url": "https://nkmuseum.ru/"},
    ],
    ["museum", "local-lore", "history", "archaeology", "novokuznetsk", "kuzbass"],
    maps_text("Новокузнецкий краеведческий музей", "Новокузнецк", "Novokuznetsk Museum of Local Lore", "Novokuznetsk", 53.760585, 87.117775),
    official_site="https://nkmuseum.ru/",
))

# ==================================================================================
# GORNAYA SHORIA / TASHTAGOL và các huyện khác
# ==================================================================================

# 16) Скульптура «Золотая Шория» ----------------------------------------------------
RECORDS.append(rec(
    "zolotaya-shoria-monument-tashtagol",
    "Tượng đài 'Zolotaya Shoria' (Xứ Shoria Vàng - thiếu nữ cưỡi nai sừng tấm; phiên âm: Dô-lô-tai-a Sô-ri-a)",
    "Скульптура «Золотая Шория»",
    "Golden Shoria Monument",
    ["monument"],
    52.757978, 87.850263,
    "Công viên Vinh quang Chiến đấu (парк Боевой Славы), TP. Tashtagol, tỉnh Kemerovo (Kuzbass), Nga",
    "'Zolotaya Shoria' (Xứ Shoria Vàng) là bức tượng đồng nổi tiếng khắc họa một thiếu nữ trẻ cưỡi trên lưng nai sừng tấm (elk), biểu tượng của vùng núi Shoria. Do nhà điêu khắc Dashi Namdakov sáng tác, đây là điểm nhấn nghệ thuật độc đáo của Tashtagol.",
    "Tượng đài 'Zolotaya Shoria' (Xứ Shoria Vàng) là một trong những biểu tượng nghệ thuật đặc sắc nhất tỉnh Kemerovo, đặt tại công viên trung tâm Tashtagol - cửa ngõ vào vùng núi Gornaya Shoria. Tác phẩm do nhà điêu khắc danh tiếng gốc Buryatia Dashi Namdakov thiết kế và khánh thành năm 2010: một thiếu nữ trẻ ngồi trên lưng con nai sừng tấm hùng dũng, tay nâng chiếc bát tượng trưng cho sự sống và lòng hiếu khách. Hình tượng lấy cảm hứng từ thần thoại và văn hóa của người Shor bản địa, kết hợp phong cách phương Đông huyền ảo đặc trưng của Namdakov, tạo nên một tác phẩm vừa mạnh mẽ vừa thơ mộng. Bức tượng đồng cao vài mét đứng nổi bật giữa công viên, trở thành nơi chụp ảnh và niềm tự hào của người dân Tashtagol, đồng thời là biểu tượng cho vẻ đẹp thiên nhiên - văn hóa của cả xứ Shoria.",
    [
        "Tượng đồng thiếu nữ cưỡi nai sừng tấm - biểu tượng xứ Shoria",
        "Tác phẩm của nhà điêu khắc danh tiếng Dashi Namdakov (2010)",
        "Cảm hứng từ thần thoại và văn hóa người Shor bản địa",
    ],
    {
        "hours_vi": "Tượng đài ngoài trời trong công viên, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Quanh năm; mùa hè xanh mát, mùa đông tuyết phủ thơ mộng (kết hợp trượt tuyết Sheregesh gần đó).",
        "tips_vi": "Kết hợp chuyến đi khu trượt tuyết Sheregesh và Bảo tàng Gornaya Shoria ở Tashtagol; đẹp nhất khi nắng chiếu ánh đồng.",
    },
    [
        {"title": "Wikipedia (RU) — Золотая Шория (скульптура)", "url": "https://ru.wikipedia.org/wiki/Золотая_Шория"},
    ],
    ["monument", "sculpture", "namdakov", "shoria", "tashtagol", "kuzbass"],
    maps_text("Скульптура Золотая Шория", "Таштагол", "Golden Shoria Monument", "Tashtagol", 52.757978, 87.850263),
))

# 17) Музей этнографии и природы Горной Шории ---------------------------------------
RECORDS.append(rec(
    "gornaya-shoria-museum-tashtagol",
    "Bảo tàng Dân tộc học và Thiên nhiên vùng núi Shoria (phiên âm: Goóc-nai-a Sô-ri-a)",
    "Музей этнографии и природы Горной Шории",
    "Museum of Ethnography and Nature of Gornaya Shoria",
    ["museum"],
    52.763019, 87.847644,
    "Phố 8 Marta (ул. 8 Марта) số 4, TP. Tashtagol, tỉnh Kemerovo (Kuzbass), Nga",
    "Bảo tàng chuyên sâu về văn hóa người Shor bản địa và thiên nhiên vùng núi Gornaya Shoria. Trưng bày trang phục, đồ dùng, tín ngưỡng shaman cùng hệ động thực vật của dãy núi taiga phía nam Kuzbass.",
    "Bảo tàng Dân tộc học và Thiên nhiên vùng núi Shoria ở Tashtagol là nơi lưu giữ và giới thiệu di sản độc đáo của người Shor - dân tộc bản địa nói ngôn ngữ Turk sinh sống lâu đời trên vùng núi phía nam tỉnh Kemerovo. Các gian trưng bày tái hiện đời sống truyền thống: nhà cửa, trang phục, công cụ săn bắn và đánh cá, nghề rèn, cùng tín ngưỡng shaman với trống thiêng và các nghi lễ. Bên cạnh đó, khu thiên nhiên giới thiệu hệ động thực vật phong phú của rừng taiga Gornaya Shoria - từ gấu, nai đến các loài chim và thảm thực vật núi cao. Bảo tàng còn kể về lịch sử khai thác vàng, sắt và sự hình thành các thị trấn miền núi. Đây là điểm đến giàu thông tin, giúp du khách hiểu chiều sâu văn hóa của vùng đất trước khi khám phá thiên nhiên Sheregesh và Shoria.",
    [
        "Chuyên sâu về văn hóa và tín ngưỡng shaman của người Shor bản địa",
        "Trưng bày hệ động thực vật rừng taiga Gornaya Shoria",
        "Lịch sử khai thác vàng, sắt và các thị trấn miền núi",
    ],
    {
        "hours_vi": "Mở cửa từ thứ Ba đến Chủ nhật, khoảng 9:00–17:00; thứ Hai nghỉ (nên kiểm tra lại).",
        "ticket_vi": "Vé vào khoảng 150–250 RUB; ưu đãi cho học sinh, sinh viên.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm; tiện kết hợp mùa trượt tuyết Sheregesh (đông) hoặc du lịch núi (hè).",
        "tips_vi": "Kết hợp tham quan tượng 'Zolotaya Shoria' cùng thành phố; hỏi về các tour văn hóa Shor.",
    },
    [
        {"title": "Wikipedia (RU) — Музей этнографии и природы Горной Шории", "url": "https://ru.wikipedia.org/wiki/Музей_этнографии_и_природы_Горной_Шории"},
    ],
    ["museum", "ethnography", "shor", "nature", "tashtagol", "kuzbass"],
    maps_text("Музей этнографии и природы Горной Шории", "Таштагол", "Museum of Ethnography and Nature of Gornaya Shoria", "Tashtagol", 52.763019, 87.847644),
))

# 18) Шорский национальный парк -----------------------------------------------------
RECORDS.append(rec(
    "shorsky-national-park",
    "Vườn quốc gia Shorsky (phiên âm: Sô-rơ-xki)",
    "Шорский национальный парк",
    "Shorsky National Park",
    ["park_garden"],
    52.583333, 88.333333,
    "Huyện Tashtagol (Таштагольский район), phía nam tỉnh Kemerovo (Kuzbass); trụ sở tại Tashtagol, Nga",
    "Vườn quốc gia Shorsky bảo vệ vùng rừng taiga núi non hoang sơ ở phía nam Kuzbass, quê hương của người Shor. Nổi tiếng với các dòng sông trong vắt (Mrassu, Kabyrza), thác nước, hang động và những vách đá kỳ vĩ như 'Царские Ворота'.",
    "Vườn quốc gia Shorsky, thành lập năm 1989, trải rộng trên vùng núi Gornaya Shoria ở cực nam tỉnh Kemerovo, bảo tồn hệ rừng taiga núi cao gần như nguyên vẹn - vương quốc của tuyết tùng Siberia, gấu nâu, nai và vô số loài chim, cây thuốc quý. Điểm hấp dẫn nhất là những dòng sông trong vắt chảy qua các hẻm núi, đặc biệt là sông Mrassu với hành trình chèo thuyền (rafting/kayak) nổi tiếng, ngang qua các vách đá dựng đứng, thác nước, hang động và mó nước khoáng. Trong công viên còn có các di chỉ khảo cổ và làng người Shor với văn hóa bản địa đặc sắc. Đây là điểm đến hàng đầu cho du lịch sinh thái, chèo thuyền và khám phá thiên nhiên hoang dã của miền nam Kuzbass, thường được kết hợp trong hành trình cùng Sheregesh và Tashtagol.",
    [
        "Rừng taiga núi non hoang sơ, quê hương văn hóa người Shor",
        "Chèo thuyền trên sông Mrassu qua thác, hang động và vách đá kỳ vĩ",
        "Du lịch sinh thái, khảo cổ và thiên nhiên hoang dã nam Kuzbass",
    ],
    {
        "hours_vi": "Khu thiên nhiên rộng lớn ngoài trời; tham quan theo mùa, chủ yếu tháng 5–9 cho tuyến sông.",
        "ticket_vi": "Có thu phí vào vườn quốc gia và phí tuyến tham quan/chèo thuyền; liên hệ ban quản lý ở Tashtagol.",
        "duration_vi": "Từ nửa ngày đến nhiều ngày tùy tuyến (rafting sông Mrassu thường 3–7 ngày).",
        "best_time_vi": "Cuối xuân đến đầu thu (tháng 5–9) khi nước sông thuận lợi cho chèo thuyền.",
        "tips_vi": "Đi theo tour có phép và hướng dẫn viên; chuẩn bị đồ chống nước, chống côn trùng; đăng ký trước với ban quản lý vườn.",
    },
    [
        {"title": "Wikipedia (RU) — Шорский национальный парк", "url": "https://ru.wikipedia.org/wiki/Шорский_национальный_парк"},
        {"title": "Trang chính thức", "url": "https://shorskynp.ru/"},
    ],
    ["national-park", "nature", "taiga", "rafting", "shoria", "kuzbass"],
    maps_text("Шорский национальный парк", "Таштагольский район", "Shorsky National Park", "Tashtagol District", 52.583333, 88.333333),
    official_site="https://shorskynp.ru/",
))

# 19) Скала «Царские Ворота» на р. Мрассу -------------------------------------------
RECORDS.append(rec(
    "tsarskiye-vorota-rock-mrassu",
    "Vách đá 'Tsarskiye Vorota' (Cổng Nhà Vua) trên sông Mrassu (phiên âm: Xa-rơ-xki-ê Va-rô-ta)",
    "Скала «Царские Ворота»",
    "Tsarskiye Vorota (Tsar's Gate) Rock",
    ["other"],
    53.057677, 88.463314,
    "Trên sông Mrassu, Vườn quốc gia Shorsky, huyện Tashtagol, tỉnh Kemerovo (Kuzbass), Nga",
    "'Tsarskiye Vorota' (Cổng Nhà Vua) là hai vách đá dựng đứng cao sừng sững hai bên sông Mrassu trong Vườn quốc gia Shorsky, tạo thành một 'cổng đá' hùng vĩ. Đây là điểm nhấn ngoạn mục nhất trên tuyến chèo thuyền sông Mrassu.",
    "'Tsarskiye Vorota' (Cổng Nhà Vua) là một trong những kỳ quan thiên nhiên tiêu biểu của Vườn quốc gia Shorsky: hai khối đá vôi khổng lồ dựng đứng ở hai bờ sông Mrassu, tạo nên hình ảnh như một chiếc cổng đá đồ sộ mà dòng sông chảy qua ở giữa. Những vách đá cao hàng chục mét phủ rêu và cây bám, in bóng xuống mặt nước trong vắt, tạo nên khung cảnh vừa uy nghi vừa nên thơ. Đây là điểm dừng chân được mong đợi nhất trên hành trình rafting/kayak dọc sông Mrassu - tuyến du lịch sinh thái nổi tiếng của miền nam Kuzbass. Khu vực quanh 'Cổng Nhà Vua' còn có các hang động và mó nước khoáng, cùng khung cảnh rừng taiga hoang sơ, mang lại trải nghiệm khó quên cho những ai ưa mạo hiểm và thiên nhiên.",
    [
        "Hai vách đá vôi dựng đứng tạo thành 'cổng đá' hai bên sông Mrassu",
        "Điểm nhấn ngoạn mục nhất trên tuyến chèo thuyền sông Mrassu",
        "Khung cảnh rừng taiga hoang sơ, hang động và mó nước khoáng gần kề",
    ],
    {
        "hours_vi": "Điểm thiên nhiên ngoài trời trong vườn quốc gia; tiếp cận theo tuyến sông mùa hè.",
        "ticket_vi": "Nằm trong Vườn quốc gia Shorsky - áp dụng phí vào vườn và phí tour chèo thuyền.",
        "duration_vi": "Là điểm dừng trong hành trình rafting nhiều ngày trên sông Mrassu.",
        "best_time_vi": "Cuối xuân đến đầu thu (tháng 5–9) mùa chèo thuyền.",
        "tips_vi": "Chỉ nên đến theo tour rafting có phép và hướng dẫn; mang đồ chống nước, áo phao; tôn trọng quy định bảo tồn.",
    },
    [
        {"title": "Wikipedia (RU) — Шорский национальный парк", "url": "https://ru.wikipedia.org/wiki/Шорский_национальный_парк"},
        {"title": "Okolo.city — Скала Царские Ворота", "url": "https://okolo.city/places/tsarskie-vorota/"},
    ],
    ["natural-landmark", "rock", "river", "mrassu", "shoria", "kuzbass"],
    maps_text("Скала Царские Ворота", "Таштагольский район", "Tsarskiye Vorota Rock", "Tashtagol District", 53.057677, 88.463314),
))

# 20) Музей-заповедник «Шестаково» --------------------------------------------------
RECORDS.append(rec(
    "shestakovo-dinosaur-museum",
    "Khu bảo tồn - bảo tàng Shestakovo (bãi hóa thạch khủng long; phiên âm: Se-xta-cô-vô)",
    "Музей-заповедник «Шестаково»",
    "Shestakovo Museum-Reserve (Dinosaur Site)",
    ["museum"],
    55.893889, 87.962778,
    "Làng Shestakovo (д. Шестаково), huyện Chebulinsky (Чебулинский район), tỉnh Kemerovo (Kuzbass), Nga",
    "Shestakovo là một trong những bãi hóa thạch khủng long lớn và nổi tiếng nhất nước Nga, nằm bên sông Kiya. Nơi đây phát hiện nhiều bộ xương khủng long, nổi bật là loài Psittacosaurus sibiricus - 'khủng long vẹt' Siberia đặc hữu.",
    "Khu bảo tồn - bảo tàng Shestakovo (thuộc quần thể bảo tàng Kuzbass) bảo vệ một trong những di chỉ cổ sinh vật học quan trọng bậc nhất nước Nga, nằm trên các vách đất đỏ ('Красная горка Шестаковская') bên bờ sông Kiya ở huyện Chebulinsky. Từ giữa thế kỷ XX, các nhà khoa học đã khai quật tại đây nhiều bộ xương và di cốt khủng long có niên đại kỷ Phấn Trắng sớm (khoảng 100–130 triệu năm trước), nổi tiếng nhất là loài Psittacosaurus sibiricus ('khủng long vẹt' Siberia) đặc hữu cùng nhiều loài bò sát, cá và động vật cổ khác. Khu vực gồm các điểm khai quật ngoài trời (Shestakovo-1, -3) và bảo tàng trưng bày hóa thạch, mô hình khủng long, giúp du khách - đặc biệt là trẻ em - hình dung sống động về sự sống thời tiền sử của Siberia. Đây là điểm đến khoa học - giáo dục độc đáo, được ví như 'công viên khủng long' của Kuzbass.",
    [
        "Một trong những bãi hóa thạch khủng long lớn nhất nước Nga bên sông Kiya",
        "Nơi phát hiện 'khủng long vẹt' Psittacosaurus sibiricus đặc hữu",
        "Điểm khai quật ngoài trời và bảo tàng hóa thạch - hấp dẫn trẻ em",
    ],
    {
        "hours_vi": "Bảo tàng mở theo giờ hành chính (thường 9:00–17:00); các điểm khai quật ngoài trời tham quan mùa ấm.",
        "ticket_vi": "Vé bảo tàng và tour khoảng 150–400 RUB; liên hệ ban quản lý để đặt tour khảo cổ.",
        "duration_vi": "Khoảng 1,5–3 giờ (kể cả điểm khai quật).",
        "best_time_vi": "Cuối xuân đến đầu thu (tháng 5–9) để tiện đi các điểm ngoài trời.",
        "tips_vi": "Đường tới làng khá xa các thành phố lớn - nên đi ô tô/tour; mang giày đi bộ; kết hợp ngắm sông Kiya.",
    },
    [
        {"title": "Wikipedia (RU) — Шестаково (местонахождение динозавров)", "url": "https://ru.wikipedia.org/wiki/Шестаково_(местонахождение_динозавров)"},
    ],
    ["museum", "paleontology", "dinosaurs", "science", "chebulinsky", "kuzbass"],
    maps_text("Музей-заповедник Шестаково", "Шестаково", "Shestakovo Dinosaur Museum", "Shestakovo", 55.893889, 87.962778),
))

# 21) Озеро Большой Берчикуль -------------------------------------------------------
RECORDS.append(rec(
    "bolshoy-berchikul-lake",
    "Hồ Bolshoy Berchikul (Hồ Berchikul Lớn; phiên âm: Ban-sôi Béc-chi-cun)",
    "Озеро Большой Берчикуль",
    "Bolshoy Berchikul Lake",
    ["park_garden"],
    55.601667, 88.329167,
    "Huyện Tisulsky (Тисульский район), tỉnh Kemerovo (Kuzbass), Nga",
    "Bolshoy Berchikul là hồ nước tự nhiên lớn nhất tỉnh Kemerovo, nằm giữa vùng đồi rừng ở huyện Tisulsky. Hồ nổi tiếng với nước sạch, bùn khoáng chữa bệnh và là điểm nghỉ dưỡng, câu cá, tắm hồ được yêu thích.",
    "Hồ Bolshoy Berchikul (Berchikul Lớn) là hồ tự nhiên lớn nhất tỉnh Kemerovo, trải rộng khoảng 20 km² giữa vùng đồi và rừng taiga phía đông bắc Kuzbass, thuộc huyện Tisulsky. Được hình thành từ thời cổ đại, hồ có làn nước tương đối sạch và ấm vào mùa hè, cùng lớp bùn sapropel giàu khoáng chất được cho là có tác dụng chữa bệnh - vì thế quanh hồ đã hình thành các khu nghỉ dưỡng, trại hè và nhà nghỉ. Đây là điểm đến quen thuộc của người dân Kuzbass để tắm hồ, câu cá (hồ nhiều cá diếc, cá rô), chèo thuyền và cắm trại giữa thiên nhiên. Cảnh quan yên bình với mặt hồ rộng, bờ cây xanh và hoàng hôn phản chiếu khiến Bolshoy Berchikul trở thành một 'ốc đảo' nghỉ ngơi giữa vùng công nghiệp Siberia.",
    [
        "Hồ tự nhiên lớn nhất tỉnh Kemerovo (khoảng 20 km²)",
        "Bùn khoáng sapropel chữa bệnh và các khu nghỉ dưỡng ven hồ",
        "Tắm hồ, câu cá, chèo thuyền và cắm trại mùa hè",
    ],
    {
        "hours_vi": "Khu vực hồ ngoài trời, tham quan tự do; dịch vụ nghỉ dưỡng hoạt động chủ yếu mùa hè.",
        "ticket_vi": "Vào khu vực hồ nhìn chung miễn phí; các khu nghỉ, bãi tắm, thuê thuyền thu phí riêng.",
        "duration_vi": "Từ nửa ngày đến vài ngày nếu nghỉ dưỡng.",
        "best_time_vi": "Mùa hè (tháng 6–8) để tắm và nghỉ dưỡng; đầu thu cho câu cá.",
        "tips_vi": "Xa các thành phố lớn - nên đi ô tô; đặt chỗ nghỉ trước vào cao điểm hè; mang đồ chống côn trùng.",
    },
    [
        {"title": "Wikipedia (RU) — Большой Берчикуль", "url": "https://ru.wikipedia.org/wiki/Большой_Берчикуль"},
    ],
    ["lake", "nature", "resort", "fishing", "tisulsky", "kuzbass"],
    maps_text("Озеро Большой Берчикуль", "Тисульский район", "Bolshoy Berchikul Lake", "Tisulsky District", 55.601667, 88.329167),
))

# 22) Липовый остров (заказник «Кузедеевский») -------------------------------------
RECORDS.append(rec(
    "kuzedeevo-linden-island",
    "Đảo Rừng Đoạn (rừng đoạn cổ Lipovy Ostrov, Kuzedeevo; phiên âm: Li-pô-vưi Ốt-trốp)",
    "Липовый остров (заказник «Кузедеевский»)",
    "Lipovy Ostrov (Linden Island) Nature Reserve",
    ["park_garden"],
    53.351550, 87.291400,
    "Gần làng Kuzedeevo (пгт Кузедеево), huyện Novokuznetsk, tỉnh Kemerovo (Kuzbass), Nga",
    "'Đảo Rừng Đoạn' (Lipovy Ostrov) là một cánh rừng đoạn (cây bồ đề - linden) cổ còn sót lại từ kỷ Đệ Tam, tồn tại lạc lõng giữa rừng taiga Siberia. Đây là hiện tượng thực vật độc đáo được bảo vệ nghiêm ngặt, cách xa mọi khu rừng đoạn khác hàng nghìn km.",
    "'Đảo Rừng Đoạn' (Lipovy Ostrov) gần làng Kuzedeevo là một trong những hiện tượng thực vật kỳ lạ và quý giá nhất Siberia: một quần thể rừng cây đoạn (linden - Tilia) rộng lớn còn sót lại từ kỷ Đệ Tam, khi khí hậu vùng này còn ấm áp. Trong khi loài cây đoạn lá rộng đã biến mất khỏi phần lớn Siberia sau các kỷ băng hà, thì tại đây - nhờ điều kiện tiểu khí hậu đặc biệt - cả một 'hòn đảo' rừng đoạn vẫn sống sót, tách biệt khỏi khu phân bố chính của loài này ở châu Âu tới hàng nghìn cây số. Khu rừng được bảo vệ dưới hình thức khu bảo tồn (заказник «Кузедеевский»), là 'bảo tàng sống' của thực vật cổ đại với hệ sinh thái độc đáo, nhiều loài cây thảo và động vật đặc trưng. Đây là điểm đến hấp dẫn cho những ai yêu thiên nhiên, thực vật học và muốn tận mắt thấy một 'tàn tích sống' của thời tiền sử.",
    [
        "Rừng đoạn (linden) cổ sót lại từ kỷ Đệ Tam giữa taiga Siberia",
        "Hiện tượng thực vật độc đáo, tách biệt khu phân bố chính hàng nghìn km",
        "Khu bảo tồn 'bảo tàng sống' của thực vật cổ đại",
    ],
    {
        "hours_vi": "Khu bảo tồn thiên nhiên ngoài trời, tham quan ban ngày mùa ấm.",
        "ticket_vi": "Là khu bảo tồn (заказник) - cần tuân thủ quy định bảo vệ; nên đi cùng hướng dẫn địa phương.",
        "duration_vi": "Khoảng nửa ngày (kể cả di chuyển).",
        "best_time_vi": "Cuối xuân đến đầu thu; đẹp nhất khi cây đoạn ra hoa (khoảng tháng 7).",
        "tips_vi": "Đường vào rừng khó - nên có người dẫn; không hái/chặt cây; mang giày lội và đồ chống côn trùng.",
    },
    [
        {"title": "Wikipedia (RU) — Липовый остров", "url": "https://ru.wikipedia.org/wiki/Липовый_остров"},
    ],
    ["nature-reserve", "relict-forest", "linden", "botany", "kuzedeevo", "kuzbass"],
    maps_text("Липовый остров", "Кузедеево", "Lipovy Ostrov Linden Island", "Kuzedeevo", 53.351550, 87.291400),
))

# 23) Заповедник «Кузнецкий Алатау» -------------------------------------------------
RECORDS.append(rec(
    "kuznetsky-alatau-reserve",
    "Khu bảo tồn thiên nhiên Kuznetsky Alatau (phiên âm: Cút-nhét-xki A-la-tau)",
    "Государственный природный заповедник «Кузнецкий Алатау»",
    "Kuznetsky Alatau Nature Reserve",
    ["park_garden"],
    53.699433, 88.039116,
    "Ban quản lý tại TP. Mezhdurechensk (đại lộ Shakhtyorov số 33); khu bảo tồn nằm ở dãy Kuznetsky Alatau, tỉnh Kemerovo (Kuzbass), Nga",
    "Kuznetsky Alatau là khu bảo tồn thiên nhiên quốc gia trải trên dãy núi cùng tên, bảo vệ hệ rừng taiga núi cao, các sông băng hiếm hoi ở độ cao thấp và nhiều loài động vật quý như tuần lộc rừng, gấu, chồn sable. Ban quản lý và trung tâm du khách đặt tại Mezhdurechensk.",
    "Khu bảo tồn thiên nhiên quốc gia 'Kuznetsky Alatau', thành lập năm 1989, bảo vệ phần trung tâm của dãy núi Kuznetsky Alatau - 'mái nhà' của vùng Kuzbass, nơi khởi nguồn nhiều con sông lớn. Đây là vùng thiên nhiên hoang sơ với rừng taiga tuyết tùng, đồng cỏ núi cao, hồ băng và điều đặc biệt là những khối băng - tuyết tồn tại quanh năm ở độ cao thấp bất thường (một hiện tượng hiếm gặp trên thế giới). Khu bảo tồn là nơi cư ngụ của tuần lộc rừng, gấu nâu, chồn sable, linh miêu cùng nhiều loài chim và thực vật quý hiếm. Bản thân vùng lõi được bảo vệ nghiêm ngặt, nhưng khu vực đệm có các tuyến du lịch sinh thái, trekking và trung tâm du khách; ban quản lý cùng bảo tàng thiên nhiên đặt tại thành phố Mezhdurechensk. Đây là điểm đến cho những ai yêu núi non hoang dã và muốn khám phá thiên nhiên nguyên vẹn của Siberia.",
    [
        "Khu bảo tồn dãy Kuznetsky Alatau - 'mái nhà' của Kuzbass (từ 1989)",
        "Băng tuyết tồn tại quanh năm ở độ cao thấp - hiện tượng hiếm gặp",
        "Nơi cư ngụ của tuần lộc rừng, gấu, chồn sable và thực vật quý",
    ],
    {
        "hours_vi": "Vùng lõi bảo vệ nghiêm ngặt; tuyến du lịch sinh thái ở khu đệm theo mùa (chủ yếu hè và đông cho trượt tuyết/trekking).",
        "ticket_vi": "Có thu phí tuyến tham quan và cần đăng ký/giấy phép với ban quản lý ở Mezhdurechensk.",
        "duration_vi": "Từ một ngày đến nhiều ngày tùy tuyến trekking.",
        "best_time_vi": "Tháng 6–9 cho trekking mùa hè; mùa đông cho trượt tuyết băng đồng.",
        "tips_vi": "Bắt buộc đi theo tour có phép và hướng dẫn viên; chuẩn bị trang bị leo núi, đồ ấm; ghé trung tâm du khách ở Mezhdurechensk trước.",
    },
    [
        {"title": "Wikipedia (RU) — Кузнецкий Алатау (заповедник)", "url": "https://ru.wikipedia.org/wiki/Кузнецкий_Алатау_(заповедник)"},
        {"title": "Trang chính thức", "url": "https://kuz-alatau.ru/"},
    ],
    ["nature-reserve", "mountains", "taiga", "trekking", "mezhdurechensk", "kuzbass"],
    maps_text("Заповедник Кузнецкий Алатау", "Междуреченск", "Kuznetsky Alatau Nature Reserve", "Mezhdurechensk", 53.699433, 88.039116),
    official_site="https://kuz-alatau.ru/",
))

# 24) Экомузей-заповедник «Тюльберский городок» ------------------------------------
RECORDS.append(rec(
    "tyulbersky-gorodok-ecomuseum",
    "Bảo tàng sinh thái 'Tyulbersky Gorodok' (Thành cổ người Tyulber; phiên âm: Chun-be-rơ-xki Ga-rô-đốc)",
    "Экомузей-заповедник «Тюльберский городок»",
    "Tyulbersky Gorodok Eco-Museum-Reserve",
    ["museum"],
    55.095417, 86.380361,
    "Làng Starochervovo (село Старочервово), huyện Kemerovo, tỉnh Kemerovo (Kuzbass), Nga",
    "'Tyulbersky Gorodok' là bảo tàng sinh thái ngoài trời tái hiện một thành lũy - khu định cư cổ của người Turk bản địa bên bờ sông Tom. Nơi đây phục dựng đền thờ, nhà ở, công sự gỗ và trưng bày khảo cổ về các dân tộc thời trung cổ vùng Tây Siberia.",
    "Bảo tàng sinh thái - khảo cổ ngoài trời 'Tyulbersky Gorodok' nằm trên một mỏm đất cao bên bờ sông Tom gần làng Starochervovo, được lập trên nền một di chỉ khảo cổ có người cư trú từ thời đồ đá đến trung cổ. Bảo tàng phục dựng hình ảnh một 'thành cổ' của các bộ tộc Turk bản địa (trong đó có người Tyulber) với hàng rào gỗ, tháp canh, nhà ở, đền thờ ngoài trời và các công trình tín ngưỡng shaman. Du khách có thể tìm hiểu về đời sống, tín ngưỡng và nghề thủ công của cư dân Tây Siberia thời trung cổ, xem hiện vật khảo cổ khai quật tại chỗ, và tham gia các lễ hội dân tộc, nghi lễ truyền thống được tổ chức định kỳ. Với khung cảnh thiên nhiên bên sông Tom, đây là điểm đến kết hợp lịch sử - văn hóa - thiên nhiên độc đáo, không xa thành phố Kemerovo.",
    [
        "Bảo tàng ngoài trời phục dựng 'thành cổ' của người Turk bản địa bên sông Tom",
        "Đền thờ, công sự gỗ, tháp canh và trưng bày khảo cổ trung cổ",
        "Lễ hội dân tộc và nghi lễ truyền thống định kỳ",
    ],
    {
        "hours_vi": "Bảo tàng ngoài trời, mở theo mùa và sự kiện; thường hoạt động từ mùa xuân đến mùa thu.",
        "ticket_vi": "Vé vào và tour khoảng 150–350 RUB; nên liên hệ trước, nhất là dịp lễ hội.",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu; đặc biệt dịp các lễ hội dân tộc.",
        "tips_vi": "Cách Kemerovo khoảng 1 giờ xe - nên đi ô tô; hỏi lịch lễ hội truyền thống; mang giày đi bộ.",
    },
    [
        {"title": "Okolo.city — Тюльберский городок", "url": "https://okolo.city/places/tyulberskii-gorodok/"},
        {"title": "Wikipedia (RU) — Тюльберский городок", "url": "https://ru.wikipedia.org/wiki/Тюльберский_городок"},
    ],
    ["museum", "archaeology", "ethnography", "open-air", "kemerovo-district", "kuzbass"],
    maps_text("Экомузей Тюльберский городок", "Старочервово", "Tyulbersky Gorodok Eco-Museum", "Starochervovo", 55.095417, 86.380361),
))

# 25) Свято-Серафимо-Покровский женский монастырь ----------------------------------
RECORDS.append(rec(
    "svyato-serafimo-pokrovsky-convent-leninsk-kuznetsky",
    "Tu viện nữ Thánh Serafim - Cầu Bầu (Svyato-Serafimo-Pokrovsky; phiên âm: Xvi-a-tô Xê-ra-phi-mô Pa-crốp-xki)",
    "Свято-Серафимо-Покровский женский монастырь",
    "Svyato-Serafimo-Pokrovsky Convent",
    ["church"],
    54.652533, 86.134226,
    "Phố Sovetskaya (ул. Советская) số 187, TP. Leninsk-Kuznetsky (Ленинск-Кузнецкий), tỉnh Kemerovo, Nga",
    "Đây là tu viện nữ Chính thống giáo đầu tiên và tiêu biểu của tỉnh Kemerovo, đặt tại thành phố Leninsk-Kuznetsky. Quần thể tu viện với nhà thờ mái vòm vàng là trung tâm hành hương và đời sống tâm linh của vùng.",
    "Tu viện nữ Thánh Serafim - Cầu Bầu (Svyato-Serafimo-Pokrovsky) ở Leninsk-Kuznetsky là một trong những tu viện Chính thống giáo quan trọng nhất tỉnh Kemerovo, được thành lập vào thập niên 1990 trên nền một nhà thờ cũ có từ đầu thế kỷ XX. Quần thể mang tên Thánh Serafim thành Sarov và lễ Đức Mẹ Cầu Bầu (Pokrov), gồm nhà thờ chính với các mái vòm dát vàng, nhà nguyện, khu nhà tu và vườn tược thanh tịnh. Đây là nơi các nữ tu sinh sống, cầu nguyện và giữ gìn truyền thống tu trì, đồng thời là điểm hành hương thu hút tín đồ đến chiêm bái các thánh tích và tham dự thánh lễ. Với kiến trúc nhà thờ Nga truyền thống và bầu không khí tĩnh lặng, tu viện là một điểm dừng chân tâm linh yên bình, phản ánh sự hồi sinh của đời sống tôn giáo ở vùng công nghiệp Kuzbass sau thời Xô Viết.",
    [
        "Tu viện nữ Chính thống giáo tiêu biểu của tỉnh Kemerovo",
        "Nhà thờ mái vòm dát vàng, trung tâm hành hương ở Leninsk-Kuznetsky",
        "Biểu tượng sự hồi sinh đời sống tôn giáo ở Kuzbass sau thời Xô Viết",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày phục vụ lễ, thường khoảng 7:00–19:00.",
        "ticket_vi": "Miễn phí vào tham quan và dự lễ.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Quanh năm; đặc biệt vào lễ Đức Mẹ Cầu Bầu (14/10) và lễ Thánh Serafim.",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn và mặc váy dài; giữ yên lặng, tôn trọng nếp sống tu viện; xin phép trước khi chụp ảnh.",
    },
    [
        {"title": "Sobory.ru — Свято-Серафимо-Покровский монастырь", "url": "https://sobory.ru/article/?object=58549"},
    ],
    ["church", "monastery", "convent", "orthodox", "leninsk-kuznetsky", "kuzbass"],
    maps_text("Свято-Серафимо-Покровский женский монастырь", "Ленинск-Кузнецкий", "Svyato-Serafimo-Pokrovsky Convent", "Leninsk-Kuznetsky", 54.652533, 86.134226),
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
