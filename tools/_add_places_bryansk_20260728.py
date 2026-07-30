# -*- coding: utf-8 -*-
"""_add_places_bryansk_20260728.py — VÙNG: Tỉnh Bryansk (Брянская область)
(lần chạy tự động 2026-07-28).

Bối cảnh: bryansk.json hiện có 7 địa điểm. Bổ sung 24 địa điểm THẬT SỰ nổi tiếng/đặc
sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 31 (≥30).

Phân bố loại hình (24 bản ghi mới):
- church (9): Покровский собор (Покровская гора), Спасо-Гробовская церковь,
  Петро-Павловский монастырь, храм «Неопалимая Купина» (хрустальный иконостас, Дятьково),
  Троицкий собор (Трубчевск), Площанская пустынь, Спасо-Преображенский монастырь (Севск),
  собор Рождества Христова (Стародуб), Николо-Одрин монастырь.
- museum (4): Художественный музейно-выставочный центр, Музей дятьковского хрусталя,
  Трубчевский музей и планетарий, Брянский государственный краеведческий музей.
- theatre (2): Театр драмы им. А. К. Толстого, Театр кукол.
- park_garden (2): Заповедник «Брянский лес», Парк-музей им. А. К. Толстого (деревянная скульптура).
- monument (3): Памятник Бояну (Трубчевск), мемориал «Хацунь», памятник воинам-водителям.
- square_street (3): Бульвар Гагарина, площадь Партизан, Славянская площадь.
- palace (1): Усадьба-дворец Завадовского в Ляличах.

TOẠ ĐỘ — xác minh chéo (sobory.ru khối «Координаты», ru.wikipedia geohack, Yandex Maps org,
2GIS firm/geo, russiancip.ru, tonkosti.ru; 2026-07-28). Phạm vi tỉnh Bryansk: lat ~51.5–54.0,
lon ~31.5–35.5; tất cả toạ độ nằm trong phạm vi, KHÔNG đảo lat/lon:
  Покровский собор 53.245888,34.373796 (sobory 00659); Спасо-Гробовская 53.253380,34.376950
  (sobory 00660); Петро-Павловский монастырь 53.254811,34.377567 (sobory 07767); Художественный
  музей 53.239094,34.354272 (Емлютина 39, Yandex org); Театр драмы 53.242525,34.361974 (Фокина 26);
  Театр кукол 53.264145,34.412469 (Пушкина 12); Парк-музей Толстого 53.246337,34.359696 (бул.
  Гагарина 33, Yandex org); Бульвар Гагарина 53.241670,34.367500 (ru.wiki); Площадь Партизан
  53.234720,34.353610 (ru.wiki); Славянская площадь 53.240280,34.373610 (2GIS); краеведческий
  музей 53.234001,34.352859 (пл. Партизан 6, 2GIS); памятник воинам-водителям 53.198437,34.529116
  (Осиновая горка, 2GIS); Заповедник «Брянский лес» 52.495871,33.991164 (ru.wiki); Неопалимая
  Купина Дятьково 53.601307,34.332603 (sobory 01755); Музей хрусталя Дятьково 53.598342,34.334814
  (Ленина 159, russiancip); Троицкий собор Трубчевск 52.574732,33.770886 (sobory 00679); Памятник
  Бояну 52.575397,33.771876 (Трубчевск, вал над Десной); Трубчевский музей 52.578599,33.765170
  (Ленина 72); Площанская пустынь 52.521275,34.468349 (sobory 01116, п. Пчела); Спасо-
  Преображенский монастырь Севск 52.171559,34.507996 (sobory 01621); собор Рождества Стародуб
  52.583070,32.760780 (sobory 00669, Первомайская 11); усадьба Ляличи 53.009450,32.541575
  (Суражский р-н, tonkosti); мемориал «Хацунь» 53.133855,34.637347 (Карачевский р-н, 2GIS);
  Николо-Одрин монастырь 53.166950,35.072844 (с. Одрина, sobory 07562).

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_bryansk_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "bryansk"
REGION_NAME_VI = "Tỉnh Bryansk"
FD = "Vùng Trung tâm"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def maps_org(yandex_org_url, name_en, city_en):
    """Ưu tiên URL trang tổ chức/địa điểm Yandex (chính xác nhất) + Google text-search."""
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

# 1) Покровский собор (Покровская гора) --------------------------------------------
RECORDS.append(rec(
    "pokrovsky-cathedral",
    "Nhà thờ Cầu Nguyện Đức Mẹ trên Đồi Pokrovskaya (Pokrovxki xobor)",
    "Покровский собор (Покровская гора)",
    "Pokrovsky (Intercession) Cathedral, Bryansk",
    ["church"],
    53.245888, 34.373796,
    "Phố Pokrovskaya Gora, số 2, quận Sovetsky, thành phố Bryansk, tỉnh Bryansk, Nga.",
    "Nhà thờ cổ nhất còn tồn tại ở Bryansk, dựng năm 1698 trên Đồi Pokrovskaya — nơi từng đặt thành lũy (kremlin) của thành phố xưa. Ngôi thánh đường hai tầng bằng gạch trắng là trái tim lịch sử của Bryansk.",
    "Vươn lên trên Đồi Pokrovskaya nhìn xuống sông Desna, đây là ngôi nhà thờ cổ nhất còn nguyên vẹn của thành phố Bryansk và là chứng nhân cho khởi nguồn của đô thị. Chính trên ngọn đồi này từng tọa lạc thành lũy gỗ (kremlin) của Bryansk thời trung cổ, khiến nơi đây được coi là cái nôi lịch sử của thành phố. Nhà thờ hiện nay được xây năm 1698 bằng tiền tài trợ của nhà quý tộc địa phương Evstrat Alymov, thay cho một ngôi nhà thờ gỗ đã được nhắc tới từ đầu thế kỷ 17. Công trình mang dáng dấp một thánh đường hai tầng đặc trưng lối kiến trúc Nga cuối thế kỷ 17, với các ô cửa trang trí và mái vòm khiêm nhường. Trải qua thời kỳ Xô viết bị đóng cửa và cải dụng, nhà thờ đã được trả lại cho Giáo hội và phục hồi sinh hoạt tôn giáo. Đứng trên khoảng sân trước nhà thờ, du khách có thể phóng tầm mắt bao quát khu trung tâm và dòng Desna, đồng thời cảm nhận bề dày lịch sử nghìn năm của vùng đất Bryansk.",
    [
        "Nhà thờ cổ nhất còn tồn tại của Bryansk, xây dựng năm 1698.",
        "Nằm trên Đồi Pokrovskaya — nơi từng đặt thành lũy kremlin của thành phố xưa.",
        "Điểm ngắm toàn cảnh trung tâm Bryansk và sông Desna.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Buổi sáng hoặc dịp lễ lớn của Chính Thống giáo; hoàng hôn để ngắm cảnh sông.",
        "tips_vi": "Ăn mặc kín đáo, nữ nên trùm khăn; kết hợp dạo trung tâm lịch sử và bờ kè Desna.",
    },
    [
        {"title": "Sobory.ru — Покровский собор (Брянск)", "url": "https://sobory.ru/article/?object=00659"},
        {"title": "Wikipedia (RU) — Покровский собор (Брянск)", "url": "https://ru.wikipedia.org/wiki/Покровский_собор_(Брянск)"},
    ],
    ["church", "cathedral", "orthodox", "history", "bryansk", "free"],
    maps_text("Покровский собор", "Брянск", "Pokrovsky Cathedral", "Bryansk", 53.245888, 34.373796),
))

# 2) Спасо-Гробовская церковь ------------------------------------------------------
RECORDS.append(rec(
    "spaso-grobovskaya-church",
    "Nhà thờ Chúa Biến Hình «Spaxo-Grobovxkaya»",
    "Спасо-Гробовская церковь (храм Спаса Преображения)",
    "Spaso-Grobovskaya Church, Bryansk",
    ["church"],
    53.253380, 34.376950,
    "Đại lộ Lenin, số 98, quận Sovetsky, thành phố Bryansk, tỉnh Bryansk, Nga.",
    "Ngôi nhà thờ duyên dáng theo phong cách tân-Nga, dựng năm 1904 trên nền một nhà thờ nghĩa trang cổ (nên có tên «trên những nấm mồ»). Với mái chóp nhọn và trang trí gạch tinh tế, đây là một trong những điểm nhấn kiến trúc của trung tâm Bryansk.",
    "Nằm ngay trên đại lộ Lenin nhộn nhịp giữa lòng Bryansk, nhà thờ Chúa Biến Hình quen được gọi là «Spaso-Grobovskaya» — cái tên gắn với việc nơi đây từng có một nhà thờ nghĩa trang cổ, tức «nhà thờ trên những nấm mồ». Ngôi thánh đường hiện nay được xây năm 1902–1904 theo thiết kế của kiến trúc sư N. Lebedev, mang phong cách tân-Nga (neo-russian) thịnh hành đầu thế kỷ 20. Công trình gây ấn tượng với khối tháp chóp nhọn kiểu «lều» (shatyor), những hàng cửa sổ trang trí cầu kỳ và lớp gạch nhiều màu tạo cảm giác như một hộp trang sức tinh xảo. Dù có kích thước không lớn, nhà thờ nổi bật giữa phố nhờ tỷ lệ thanh thoát và các chi tiết chạm khắc gạch đặc trưng. Sau thời kỳ Xô viết, nhà thờ được khôi phục và trở lại phục vụ tín đồ. Với du khách dạo bộ trên đại lộ Lenin, đây là điểm dừng chân lý tưởng để chiêm ngưỡng một mẫu mực kiến trúc nhà thờ Nga đầu thế kỷ 20.",
    [
        "Kiến trúc tân-Nga duyên dáng với tháp chóp «lều» và trang trí gạch cầu kỳ.",
        "Xây năm 1902–1904 trên nền một nhà thờ nghĩa trang cổ (nên có tên «trên những nấm mồ»).",
        "Vị trí ngay trung tâm trên đại lộ Lenin, dễ kết hợp dạo phố.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Ban ngày để ngắm rõ chi tiết gạch trang trí.",
        "tips_vi": "Nữ nên trùm khăn khi vào trong; kết hợp tham quan các điểm khác trên đại lộ Lenin.",
    },
    [
        {"title": "Sobory.ru — Спасо-Гробовская церковь (Брянск)", "url": "https://sobory.ru/article/?object=00660"},
        {"title": "Wikipedia (RU) — Спасо-Гробовская церковь", "url": "https://ru.wikipedia.org/wiki/Спасо-Гробовская_церковь"},
    ],
    ["church", "orthodox", "neo-russian", "architecture", "bryansk", "free"],
    maps_text("Спасо-Гробовская церковь", "Брянск", "Spaso-Grobovskaya Church", "Bryansk", 53.253380, 34.376950),
))

# 3) Петро-Павловский женский монастырь --------------------------------------------
RECORDS.append(rec(
    "petropavlovsky-monastery",
    "Tu viện Thánh Phêrô và Phaolô Bryansk (Petro-Pavlovxki monaxtyr)",
    "Петро-Павловский женский монастырь (Брянск)",
    "Saints Peter and Paul Convent, Bryansk",
    ["church"],
    53.254811, 34.377567,
    "Phố Kulkova, số 14, quận Sovetsky, thành phố Bryansk, tỉnh Bryansk, Nga.",
    "Tu viện lâu đời nhất của Bryansk, theo truyền thống được hoàng thân Oleg xứ Bryansk lập vào cuối thế kỷ 13. Đây là nơi lưu giữ thánh tích Thánh Oleg Bryansky và trung tâm hành hương của thành phố.",
    "Ẩn mình giữa khu trung tâm cổ của Bryansk, tu viện Thánh Phêrô và Phaolô được xem là tu viện cổ xưa nhất của thành phố. Theo truyền thống, tu viện do hoàng thân Oleg Romanovich xứ Bryansk sáng lập vào khoảng cuối thế kỷ 13 — vị hoàng thân đã từ bỏ ngai vàng để đi tu và sau này được Giáo hội phong thánh là Thánh Oleg Bryansky. Trải qua nhiều thế kỷ thăng trầm, ban đầu là tu viện nam, tu viện từng bị bãi bỏ, rồi tái lập thành tu viện nữ vào thế kỷ 19. Nhà thờ chính Vvedenskaya (Đức Mẹ Dâng Mình) có từ đầu thế kỷ 18 là công trình trung tâm của quần thể. Sau khi bị đóng cửa và tàn phá thời Xô viết, tu viện được hồi sinh từ thập niên 2000, các ni sư trở lại và thánh tích Thánh Oleg Bryansky được tôn kính tại đây. Ngày nay tu viện là một ốc đảo tĩnh lặng và linh thiêng ngay giữa thành phố, nơi du khách có thể tìm hiểu về vị thánh bảo trợ và cội nguồn tâm linh của vùng đất Bryansk.",
    [
        "Tu viện cổ xưa nhất Bryansk, tương truyền do hoàng thân Oleg lập cuối thế kỷ 13.",
        "Nơi lưu giữ thánh tích Thánh Oleg Bryansky — vị thánh bảo trợ của thành phố.",
        "Nhà thờ Vvedenskaya đầu thế kỷ 18 giữa không gian tĩnh lặng, linh thiêng.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (là tu viện đang hoạt động).",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Buổi sáng yên tĩnh hoặc các dịp lễ Chính Thống giáo.",
        "tips_vi": "Ăn mặc kín đáo, nữ mang khăn trùm đầu; giữ yên lặng, xin phép trước khi chụp ảnh.",
    },
    [
        {"title": "Sobory.ru — Петропавловский монастырь (Брянск)", "url": "https://sobory.ru/article/?object=07767"},
        {"title": "Wikipedia (RU) — Петропавловский монастырь (Брянск)", "url": "https://ru.wikipedia.org/wiki/Петропавловский_монастырь_(Брянск)"},
    ],
    ["church", "monastery", "convent", "orthodox", "history", "bryansk", "free"],
    maps_text("Петропавловский монастырь", "Брянск", "Saints Peter and Paul Convent", "Bryansk", 53.254811, 34.377567),
))

# 4) Храм «Неопалимая Купина» (хрустальный иконостас), Дятьково ---------------------
RECORDS.append(rec(
    "dyatkovo-crystal-church",
    "Nhà thờ «Bụi Gai Không Cháy» với bàn thờ pha lê, Dyatkovo",
    "Храм иконы Божией Матери «Неопалимая Купина» (Дятьково)",
    "Church of the Unburnt Bush Icon (Crystal Iconostasis), Dyatkovo",
    ["church"],
    53.601307, 34.332603,
    "Thành phố Dyatkovo, huyện Dyatkovsky, tỉnh Bryansk, Nga (cách Bryansk khoảng 45 km về phía bắc).",
    "Ngôi nhà thờ độc nhất vô nhị của nước Nga với bức tường thánh (iconostas) và nội thất làm từ pha lê Dyatkovo. Tái hiện thánh đường thế kỷ 19 từng nổi tiếng khắp châu Âu vì bàn thờ pha lê lộng lẫy.",
    "Ở thành phố Dyatkovo — cái nôi của nghề làm pha lê Nga — ngôi nhà thờ mang tên biểu tượng Đức Mẹ «Bụi Gai Không Cháy» được coi là độc nhất vô nhị trên thế giới nhờ bức tường thánh (iconostas) và phần lớn nội thất được chế tác từ pha lê. Truyền thống này bắt nguồn từ thế kỷ 19, khi gia tộc công nghiệp Maltsov chủ nhân nhà máy pha lê Dyatkovo cho dựng một thánh đường với bàn thờ pha lê rực rỡ từng khiến du khách châu Âu kinh ngạc. Nhà thờ nguyên bản đã bị phá hủy trong thời Xô viết, nhưng đến cuối thập niên 1990 và đầu những năm 2000, một ngôi nhà thờ mới được xây dựng và các nghệ nhân của nhà máy pha lê Dyatkovo đã phục dựng bức tường thánh bằng hàng vạn chi tiết pha lê lấp lánh. Dưới ánh đèn, cả gian thờ như tỏa sáng bởi những mảng pha lê phản chiếu muôn màu, tạo nên một không gian vừa thiêng liêng vừa huyền ảo hiếm thấy. Đây là điểm đến kết hợp hoàn hảo giữa nghệ thuật thủ công truyền thống và đời sống tôn giáo, xứng đáng cho một chuyến đi từ Bryansk lên phía bắc.",
    [
        "Bức tường thánh và nội thất bằng pha lê Dyatkovo — độc nhất vô nhị trên thế giới.",
        "Kế thừa truyền thống thánh đường pha lê của gia tộc Maltsov từ thế kỷ 19.",
        "Gian thờ lấp lánh huyền ảo dưới ánh đèn phản chiếu qua pha lê.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ; nên kiểm tra lịch trước khi đến.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Ban ngày nắng đẹp hoặc khi bật đèn để pha lê phản chiếu rực rỡ nhất.",
        "tips_vi": "Kết hợp tham quan Bảo tàng pha lê Dyatkovo gần đó; ăn mặc kín đáo khi vào nhà thờ.",
    },
    [
        {"title": "Sobory.ru — Церковь иконы Божией Матери «Неопалимая Купина» (Дятьково)", "url": "https://sobory.ru/article/?object=01755"},
        {"title": "Wikipedia (RU) — Дятьково", "url": "https://ru.wikipedia.org/wiki/Дятьково"},
    ],
    ["church", "orthodox", "crystal", "unique", "dyatkovo", "free"],
    maps_text("Храм Неопалимая Купина", "Дятьково", "Church of the Unburnt Bush", "Dyatkovo", 53.601307, 34.332603),
))

# 5) Музей дятьковского хрусталя ---------------------------------------------------
RECORDS.append(rec(
    "dyatkovo-crystal-museum",
    "Bảo tàng Pha lê Dyatkovo (Muzey khruxtalya)",
    "Музей дятьковского хрусталя",
    "Museum of Dyatkovo Crystal",
    ["museum"],
    53.598342, 34.334814,
    "Phố Lenin, số 159, thành phố Dyatkovo, huyện Dyatkovsky, tỉnh Bryansk, Nga.",
    "Một trong những bảo tàng pha lê lâu đời nhất nước Nga, trưng bày kiệt tác của nhà máy pha lê Dyatkovo qua hơn hai thế kỷ. Bộ sưu tập gồm hàng nghìn tác phẩm pha lê tinh xảo, từ đồ dùng hoàng gia tới các sáng tác đương đại.",
    "Thành lập năm 1976, Bảo tàng Pha lê Dyatkovo là một trong những bảo tàng pha lê lâu đời và phong phú nhất nước Nga, gắn liền với nhà máy pha lê Dyatkovo do gia tộc Maltsov sáng lập từ năm 1790. Bộ sưu tập trải dài hơn hai thế kỷ, kể lại toàn bộ lịch sử của một trong những trung tâm chế tác pha lê danh tiếng nhất nước Nga. Du khách được chiêm ngưỡng những chiếc bình, ly, chân đèn, bộ đồ ăn pha lê chạm khắc tinh vi, nhiều món từng phục vụ hoàng gia và giới quý tộc, bên cạnh các tác phẩm nghệ thuật độc bản và những thử nghiệm táo bạo của nghệ nhân thời Xô viết cũng như đương đại. Bảo tàng còn lưu giữ ký ức về bức tường thánh pha lê huyền thoại của thành phố. Ánh sáng chiếu qua những khối pha lê trong veo tạo nên hiệu ứng lung linh khiến chuyến tham quan như bước vào một thế giới thủy tinh kỳ ảo. Đây là điểm đến không thể bỏ qua để hiểu vì sao cái tên Dyatkovo gắn liền với nghệ thuật pha lê Nga.",
    [
        "Một trong những bảo tàng pha lê lâu đời nhất Nga (thành lập 1976).",
        "Hàng nghìn tác phẩm pha lê Dyatkovo qua hơn hai thế kỷ, từ đồ hoàng gia tới hiện đại.",
        "Gắn với lịch sử nhà máy pha lê Maltsov và bàn thờ pha lê nổi tiếng của thành phố.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nghỉ thứ Hai (nên kiểm tra lịch).",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Kết hợp tham quan nhà thờ pha lê «Neopalimaya Kupina» gần đó; cách Bryansk khoảng 45 km.",
    },
    [
        {"title": "russiancip.ru — Музей хрусталя (Дятьково)", "url": "https://russiancip.ru/map/points/muzey-khrustalya-dyatkovo/"},
        {"title": "Wikipedia (RU) — Дятьковский хрустальный завод", "url": "https://ru.wikipedia.org/wiki/Дятьковский_хрустальный_завод"},
    ],
    ["museum", "crystal", "craft", "dyatkovo", "art"],
    maps_text("Музей хрусталя", "Дятьково", "Museum of Dyatkovo Crystal", "Dyatkovo", 53.598342, 34.334814),
))

# 6) Заповедник «Брянский лес» -----------------------------------------------------
RECORDS.append(rec(
    "bryansky-les-reserve",
    "Khu bảo tồn thiên nhiên «Rừng Bryansk» (Bryanxki lex)",
    "Государственный природный биосферный заповедник «Брянский лес»",
    "Bryansky Les Nature Reserve",
    ["park_garden", "other"],
    52.495871, 33.991164,
    "Vùng giữa hai sông Nerussa và Desna, huyện Suzemsky và Trubchevsky, tỉnh Bryansk, Nga (văn phòng trung tâm gần ga Nerussa).",
    "Khu bảo tồn sinh quyển được UNESCO công nhận, thành lập năm 1987 giữa vùng rừng taiga - lá rộng ở nam Bryansk. Đây là thiên đường của chim hạc đen, bò rừng bison châu Âu và đủ loài chim gõ kiến của châu Âu.",
    "Trải rộng trên vùng đất giữa hai con sông Nerussa và Desna, khu bảo tồn thiên nhiên «Rừng Bryansk» được thành lập năm 1987 nhằm gìn giữ những cánh rừng nguyên sinh tiêu biểu của vùng Trung Nga. Với diện tích hơn 12.000 ha, đây là khu bảo tồn duy nhất của tỉnh Bryansk và được UNESCO đưa vào mạng lưới khu dự trữ sinh quyển thế giới. Rừng ở đây là nơi giao thoa giữa taiga phương bắc và rừng lá rộng phương nam, tạo nên đa dạng sinh học phong phú hiếm có: nơi đây tự hào có mặt cả mười loài chim gõ kiến của châu Âu, cùng biểu tượng của khu bảo tồn là loài hạc đen quý hiếm. Một trong những thành tựu nổi bật là chương trình tái thả bò rừng bison châu Âu (zubr) — loài từng suýt tuyệt chủng — nay đã hình thành đàn tự nhiên trong rừng. Du khách có thể theo các tuyến đường mòn sinh thái có lối đi gỗ và bảng thuyết minh, ghé trung tâm du khách, hoặc tham gia tour quan sát chim và thú cùng kiểm lâm. Đây là điểm đến lý tưởng cho những ai yêu thiên nhiên hoang dã và muốn khám phá lá phổi xanh của vùng Bryansk.",
    [
        "Khu dự trữ sinh quyển UNESCO, bảo tồn rừng nguyên sinh giữa Nerussa và Desna.",
        "Nơi có mặt cả 10 loài chim gõ kiến châu Âu; biểu tượng là loài hạc đen quý hiếm.",
        "Chương trình tái thả bò rừng bison châu Âu (zubr) thành công.",
    ],
    {
        "hours_vi": "Tham quan theo tuyến đường mòn sinh thái và tour có kiểm lâm; đăng ký trước qua ban quản lý.",
        "ticket_vi": "Có phí vào tuyến du lịch và phí hướng dẫn; xem bảng giá của khu bảo tồn.",
        "duration_vi": "Nửa ngày đến trọn ngày tùy tuyến.",
        "best_time_vi": "Cuối xuân đến đầu thu; mùa xuân để quan sát chim, mùa hè cho đường mòn.",
        "tips_vi": "Liên hệ trước ban quản lý để đặt tour; mang giày đi rừng, thuốc chống côn trùng và nước.",
    },
    [
        {"title": "Wikipedia (RU) — Брянский лес (заповедник)", "url": "https://ru.wikipedia.org/wiki/Брянский_лес"},
        {"title": "Минприроды России — заповедник «Брянский лес»", "url": "http://www.mnr.gov.ru/activity/oopt/bryanskiy_les_gosudarstvennyy_prirodnyy_biosfernyy_zapovednik/"},
    ],
    ["nature-reserve", "biosphere", "unesco", "wildlife", "forest", "bison"],
    maps_text("Заповедник Брянский лес", "Брянская область", "Bryansky Les Nature Reserve", "Bryansk Oblast", 52.495871, 33.991164),
    official_site="https://bryansky-les.ru/",
))

# 7) Троицкий собор, Трубчевск -----------------------------------------------------
RECORDS.append(rec(
    "trubchevsk-trinity-cathedral",
    "Nhà thờ chính tòa Chúa Ba Ngôi Trubchevsk (Troitxki xobor)",
    "Троицкий собор (Трубчевск)",
    "Trinity Cathedral, Trubchevsk",
    ["church"],
    52.574732, 33.770886,
    "Phố Uritskogo, số 80, thành phố Trubchevsk, huyện Trubchevsky, tỉnh Bryansk, Nga.",
    "Nhà thờ chính tòa cổ kính trên Đồi Nhà Thờ nhìn ra sông Desna ở Trubchevsk, một trong những đô thị lâu đời nhất vùng. Bên dưới là hầm mộ dòng họ các hoàng thân Trubetskoy.",
    "Đứng trên Đồi Nhà Thờ (Sobornaya gora) nhìn xuống dòng Desna, nhà thờ chính tòa Chúa Ba Ngôi là biểu tượng của Trubchevsk — một trong những thành phố cổ nhất vùng Bryansk, được nhắc tới từ thế kỷ 10. Ngôi thánh đường mang trong mình bề dày lịch sử của cả một dòng họ quý tộc: bên dưới nhà thờ là hầm mộ (usypalnitsa) của các hoàng thân Trubetskoy — dòng họ danh giá lấy tên chính từ Trubchevsk. Công trình đã trải qua nhiều lần xây dựng và tái thiết qua các thế kỷ, kết hợp những lớp kiến trúc khác nhau, với tháp chuông vươn cao trở thành điểm định hướng quen thuộc của thành phố. Từ khoảng sân trước nhà thờ, du khách có thể ngắm khung cảnh tuyệt đẹp của thung lũng sông Desna trải dài xanh mướt — chính vùng đất gắn với truyền thuyết về ca sĩ Boyan trong sử thi «Bài ca về đạo quân Igor». Sau thời kỳ Xô viết, nhà thờ được phục hồi và trở lại phục vụ tín đồ, đồng thời là điểm tham quan lịch sử không thể bỏ qua khi tới Trubchevsk.",
    [
        "Nhà thờ chính tòa cổ trên Đồi Nhà Thờ, nhìn ra thung lũng sông Desna.",
        "Bên dưới là hầm mộ dòng họ các hoàng thân Trubetskoy.",
        "Gắn với Trubchevsk — một trong những đô thị cổ nhất vùng và truyền thuyết ca sĩ Boyan.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ lễ; nên kiểm tra lịch trước khi đến.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Mùa hè và mùa thu để ngắm cảnh sông; buổi sáng yên tĩnh.",
        "tips_vi": "Kết hợp thăm Đài tưởng niệm Boyan và Bảo tàng Trubchevsk gần đó; ăn mặc kín đáo.",
    },
    [
        {"title": "Sobory.ru — Троицкий собор (Трубчевск)", "url": "https://sobory.ru/article/?object=00679"},
        {"title": "Wikipedia (RU) — Трубчевск", "url": "https://ru.wikipedia.org/wiki/Трубчевск"},
    ],
    ["church", "cathedral", "orthodox", "history", "trubchevsk", "free"],
    maps_text("Троицкий собор", "Трубчевск", "Trinity Cathedral", "Trubchevsk", 52.574732, 33.770886),
))

# 8) Памятник Бояну, Трубчевск -----------------------------------------------------
RECORDS.append(rec(
    "boyan-monument",
    "Đài tưởng niệm ca sĩ Boyan, Trubchevsk (Pamyatnik Boyanu)",
    "Памятник Бояну (Трубчевск)",
    "Monument to Boyan, Trubchevsk",
    ["monument"],
    52.575397, 33.771876,
    "Công viên thành phố trên bờ thành cổ nhìn ra sông Desna, thành phố Trubchevsk, huyện Trubchevsky, tỉnh Bryansk, Nga.",
    "Tượng đài vị ca sĩ - thi nhân huyền thoại Boyan, dựng năm 1975 trong công viên trên bờ thành cổ nhìn ra sông Desna. Boyan được nhắc tới trong sử thi «Bài ca về đạo quân Igor» và gắn liền với vùng đất Trubchevsk.",
    "Trong công viên thành phố Trubchevsk, trên bờ thành đất cổ nhìn xuống thung lũng sông Desna, sừng sững tượng đài ca sĩ - thi nhân Boyan. Boyan là nhân vật huyền thoại được nhắc đến trong áng sử thi lừng danh «Bài ca về đạo quân Igor» thế kỷ 12 — người nghệ sĩ dân gian gảy đàn gusli và ngợi ca các chiến công. Theo truyền thống, vùng đất Trubchevsk được gắn với quê hương của Boyan, nên năm 1975 nhân dịp kỷ niệm 1000 năm thành phố, đài tưởng niệm ông đã được dựng lên tại đây do nhà điêu khắc A. Kobilinets thực hiện. Bức tượng khắc họa hình ảnh người ca sĩ ngồi ôm cây đàn gusli, mái tóc và tấm áo choàng như đang bay trong gió, gợi lên khí chất phóng khoáng của một nghệ sĩ dân gian cổ xưa. Vị trí của tượng đài trên bờ thành cao mở ra khung cảnh sông Desna thơ mộng, biến nơi đây thành điểm dạo chơi và ngắm cảnh được yêu thích. Đây vừa là biểu tượng văn hóa của Trubchevsk, vừa là dịp để du khách chạm tới cội nguồn văn học Nga cổ.",
    [
        "Tượng ca sĩ - thi nhân huyền thoại Boyan ôm đàn gusli, dựng năm 1975.",
        "Gắn với sử thi «Bài ca về đạo quân Igor» và truyền thống quê hương Boyan ở Trubchevsk.",
        "Vị trí trên bờ thành cổ mở ra khung cảnh thung lũng sông Desna.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do suốt cả ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Mùa hè và mùa thu, đặc biệt lúc hoàng hôn để ngắm sông Desna.",
        "tips_vi": "Kết hợp thăm Nhà thờ Chúa Ba Ngôi và Bảo tàng Trubchevsk ngay gần đó.",
    },
    [
        {"title": "puteshestvie32.ru — Памятник Бояну (Трубчевск)", "url": "https://www.puteshestvie32.ru/content/boyanu"},
        {"title": "Wikipedia (RU) — Трубчевск", "url": "https://ru.wikipedia.org/wiki/Трубчевск"},
    ],
    ["monument", "culture", "literature", "trubchevsk", "free"],
    maps_text("Памятник Бояну", "Трубчевск", "Monument to Boyan", "Trubchevsk", 52.575397, 33.771876),
))

# 9) Трубчевский музей и планетарий ------------------------------------------------
RECORDS.append(rec(
    "trubchevsk-museum",
    "Bảo tàng và Nhà chiếu hình vũ trụ Trubchevsk",
    "Трубчевский музей и планетарий",
    "Trubchevsk Museum and Planetarium",
    ["museum"],
    52.578599, 33.765170,
    "Phố Lenin, số 72, thành phố Trubchevsk, huyện Trubchevsky, tỉnh Bryansk, Nga.",
    "Bảo tàng địa phương của một trong những thành phố cổ nhất vùng Bryansk, kèm nhà chiếu hình vũ trụ (planetarium) hiếm có ở đô thị nhỏ. Trưng bày phong phú về khảo cổ, lịch sử và thiên nhiên Trubchevsk.",
    "Tọa lạc trong một tòa nhà lịch sử ở trung tâm Trubchevsk, bảo tàng địa phương nơi đây kể lại câu chuyện của một trong những đô thị cổ xưa nhất vùng Bryansk — thành phố được nhắc tới từ năm 975. Bộ sưu tập của bảo tàng đặc biệt giàu hiện vật khảo cổ, phản ánh các nền văn hóa cổ từng sinh sống dọc sông Desna, bên cạnh các phần trưng bày về thiên nhiên, đời sống nông thôn, lịch sử thành phố qua các thời kỳ và phong trào du kích trong Thế chiến II. Điểm độc đáo khiến bảo tàng nổi bật là nhà chiếu hình vũ trụ (planetarium) — một tiện ích hiếm gặp ở các đô thị nhỏ, nơi du khách, đặc biệt là trẻ em, có thể chiêm ngưỡng bầu trời sao và tìm hiểu thiên văn. Sự kết hợp giữa di sản khảo cổ, lịch sử địa phương và không gian thiên văn khiến bảo tàng trở thành điểm dừng chân thú vị và giàu tính giáo dục. Đây là nơi lý tưởng để hiểu sâu hơn về bề dày nghìn năm của Trubchevsk trước khi dạo bước trên Đồi Nhà Thờ.",
    [
        "Bảo tàng của đô thị cổ Trubchevsk (nhắc tới từ năm 975), giàu hiện vật khảo cổ.",
        "Có nhà chiếu hình vũ trụ (planetarium) hiếm gặp ở đô thị nhỏ.",
        "Trưng bày thiên nhiên, lịch sử và phong trào du kích của vùng.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nghỉ thứ Hai (nên kiểm tra lịch).",
        "ticket_vi": "Vé vào cửa giá bình dân; suất chiếu planetarium có thể tính phí riêng.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Hỏi trước lịch chiếu planetarium; kết hợp tham quan Đồi Nhà Thờ và tượng Boyan.",
    },
    [
        {"title": "2GIS — Трубчевский музей и планетарий", "url": "https://2gis.ru/trubchevsk/firm/70000001062910914"},
        {"title": "Wikipedia (RU) — Трубчевск", "url": "https://ru.wikipedia.org/wiki/Трубчевск"},
    ],
    ["museum", "local-history", "planetarium", "archaeology", "trubchevsk"],
    maps_text("Трубчевский музей и планетарий", "Трубчевск", "Trubchevsk Museum and Planetarium", "Trubchevsk", 52.578599, 33.765170),
))

# 10) Площанская Богородицкая пустынь ----------------------------------------------
RECORDS.append(rec(
    "ploshchanskaya-pustyn",
    "Tu viện Площанская Богородицкая (Ploshanxkaya puxtyn)",
    "Площанская Богородицкая пустынь",
    "Ploshchanskaya Hermitage",
    ["church"],
    52.521275, 34.468349,
    "Làng Plodovoye (Pchela), huyện Brasovsky, tỉnh Bryansk, Nga (giữa rừng, cách Bryansk khoảng 90 km về phía nam).",
    "Tu viện cổ ẩn mình bên hồ giữa rừng ở huyện Brasovsky, gắn với truyền thống các trưởng lão tu đức (starets). Nơi đây từng nuôi dưỡng vị trưởng lão Makary nổi tiếng của tu viện Optina.",
    "Nép mình bên một hồ nước tĩnh lặng giữa rừng ở huyện Brasovsky, tu viện Площанская Богородицкая (Ploshchanskaya) là một trong những trung tâm tu đức cổ kính và linh thiêng của vùng Bryansk. Được thành lập từ khoảng thế kỷ 17, tu viện gắn liền với truyền thống «trưởng lão» (starchestvo) — dòng chảy tâm linh đề cao sự hướng dẫn của các bậc trưởng lão giàu kinh nghiệm thiêng liêng. Chính tại đây, vị trưởng lão lừng danh Makary — người sau này trở thành một trong những starets vĩ đại của tu viện Optina Pustyn — đã trải qua nhiều năm tu tập trước khi chuyển tới Optina. Trong thời kỳ hưng thịnh, tu viện có nhiều nhà thờ, thư viện phong phú và là điểm hành hương quan trọng. Bị đóng cửa và tàn phá thời Xô viết, tu viện bắt đầu hồi sinh từ thập niên 1990, các công trình dần được phục dựng giữa khung cảnh rừng và hồ nước thanh bình. Ngày nay, sự tĩnh lặng, không khí ẩn tu và vẻ đẹp thiên nhiên khiến Ploshchanskaya trở thành điểm đến ý nghĩa cho khách hành hương và những ai tìm kiếm sự an tĩnh nội tâm.",
    [
        "Tu viện cổ thế kỷ 17 bên hồ giữa rừng, gắn với truyền thống trưởng lão tu đức.",
        "Nơi trưởng lão Makary tu tập trước khi tới tu viện Optina Pustyn.",
        "Khung cảnh rừng và hồ nước tĩnh lặng, không khí ẩn tu thanh bình.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ; nằm ở nơi hẻo lánh nên nên đi trong ngày.",
        "ticket_vi": "Miễn phí (là tu viện đang hoạt động).",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu, ngày khô ráo vì đường vào qua vùng rừng.",
        "tips_vi": "Nên đi ô tô riêng; ăn mặc kín đáo, nữ mang khăn trùm đầu; mang theo nước.",
    },
    [
        {"title": "Sobory.ru — Площанская Богородицкая пустынь", "url": "https://sobory.ru/article/?object=01116"},
        {"title": "Wikipedia (RU) — Площанская пустынь", "url": "https://ru.wikipedia.org/wiki/Площанская_пустынь"},
    ],
    ["church", "monastery", "orthodox", "pilgrimage", "nature", "free"],
    maps_text("Площанская пустынь", "Брасовский район", "Ploshchanskaya Hermitage", "Bryansk Oblast", 52.521275, 34.468349),
))

# 11) Спасо-Преображенский монастырь, Севск ----------------------------------------
RECORDS.append(rec(
    "sevsk-monastery",
    "Tu viện Chúa Biến Hình Sevsk (Spaxo-Preobrazhenxki monaxtyr)",
    "Спасо-Преображенский монастырь (Севск)",
    "Transfiguration Monastery, Sevsk",
    ["church"],
    52.171559, 34.507996,
    "Thành phố Sevsk, huyện Sevsky, tỉnh Bryansk, Nga (cách Bryansk khoảng 140 km về phía nam).",
    "Tu viện cổ ở Sevsk — thành phố pháo đài biên giới lâu đời của nước Nga xưa. Quần thể tu viện với các nhà thờ cổ là điểm nhấn của một đô thị nhỏ giàu di sản lịch sử.",
    "Tọa lạc tại Sevsk — một trong những thành phố cổ và giàu lịch sử nhất vùng Bryansk, từng là pháo đài biên giới quan trọng bảo vệ nước Nga xưa ở phía tây nam — tu viện Chúa Biến Hình là chứng nhân cho quá khứ oai hùng của vùng đất này. Sevsk được nhắc tới từ thế kỷ 12 và trong nhiều thế kỷ đóng vai trò tiền đồn quân sự nơi giáp ranh với thảo nguyên và các vùng đất tranh chấp. Tu viện được hình thành trong bối cảnh đó, trở thành trung tâm tôn giáo của đô thị pháo đài, với các nhà thờ và tháp chuông mang đậm dấu ấn kiến trúc Nga cổ. Trải qua thời kỳ Xô viết bị đóng cửa và xuống cấp, tu viện đang trong quá trình phục hồi, đón các tu sĩ trở lại và dần khôi phục sinh hoạt tôn giáo. Dạo bước quanh quần thể tu viện và thành phố Sevsk nhỏ bé nhưng cổ kính, du khách có thể cảm nhận không khí trầm mặc của một vùng biên viễn từng chứng kiến bao thăng trầm lịch sử. Đây là điểm đến dành cho những ai yêu thích khám phá di sản chiều sâu ngoài các tuyến du lịch phổ biến.",
    [
        "Tu viện cổ ở Sevsk — thành phố pháo đài biên giới lịch sử của nước Nga xưa.",
        "Quần thể nhà thờ mang dấu ấn kiến trúc Nga cổ, đang được phục hồi.",
        "Không khí trầm mặc của một đô thị biên viễn giàu di sản.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ lễ; là điểm hẻo lánh nên nên đi trong ngày.",
        "ticket_vi": "Miễn phí (là tu viện đang hoạt động).",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu, ngày khô ráo.",
        "tips_vi": "Cách Bryansk khoảng 140 km, thuận tiện nhất đi ô tô; kết hợp dạo trung tâm cổ Sevsk.",
    },
    [
        {"title": "Sobory.ru — Спасо-Преображенский монастырь (Севск)", "url": "https://sobory.ru/article/?object=01621"},
        {"title": "Wikipedia (RU) — Севск", "url": "https://ru.wikipedia.org/wiki/Севск"},
    ],
    ["church", "monastery", "orthodox", "history", "sevsk", "free"],
    maps_text("Спасо-Преображенский монастырь", "Севск", "Transfiguration Monastery", "Sevsk", 52.171559, 34.507996),
))

# 12) Собор Рождества Христова, Стародуб -------------------------------------------
RECORDS.append(rec(
    "starodub-cathedral",
    "Nhà thờ chính tòa Giáng Sinh Chúa, Starodub",
    "Собор Рождества Христова (Стародуб)",
    "Cathedral of the Nativity of Christ, Starodub",
    ["church"],
    52.583070, 32.760780,
    "Phố Pervomayskaya, số 11, thành phố Starodub, huyện Starodubsky, tỉnh Bryansk, Nga.",
    "Nhà thờ chính tòa cổ kính của Starodub — một trong những đô thị lâu đời nhất vùng, có từ thời Rus cổ. Công trình mang phong cách baroque, là biểu tượng lịch sử của thành phố.",
    "Starodub là một trong những thành phố cổ xưa nhất vùng Bryansk, được nhắc tới từ thế kỷ 11 trong biên niên sử Rus cổ và từng đóng vai trò quan trọng như một trung tâm của vùng đất Seversk, sau này thuộc vùng Cossack Ukraine tự trị (Hetmanate). Nhà thờ chính tòa Giáng Sinh Chúa là công trình tôn giáo tiêu biểu và là biểu tượng lịch sử của thành phố. Ngôi thánh đường mang những đường nét baroque duyên dáng đặc trưng cho kiến trúc nhà thờ vùng biên giới Nga - Ukraine, với các mái vòm và tháp chuông vươn cao trên nền trời. Trải qua nhiều thế kỷ, nhà thờ chứng kiến những biến động lịch sử của một đô thị nằm ở ngã ba các nền văn hóa. Sau thời kỳ Xô viết, nhà thờ được khôi phục và trở lại là trung tâm đời sống tôn giáo của Starodub. Với du khách yêu lịch sử, đây là điểm đến để tìm hiểu về di sản Cossack và mối giao thoa văn hóa Nga - Ukraine nơi vùng đất tây nam Bryansk, kết hợp cùng việc dạo quanh trung tâm cổ kính của thành phố.",
    [
        "Nhà thờ chính tòa cổ, biểu tượng lịch sử của đô thị Starodub thời Rus cổ.",
        "Kiến trúc baroque đặc trưng vùng biên giới văn hóa Nga - Ukraine.",
        "Gắn với di sản Cossack và vùng đất Seversk cổ xưa.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Ban ngày; các dịp lễ lớn của Chính Thống giáo.",
        "tips_vi": "Kết hợp dạo trung tâm cổ Starodub; ăn mặc kín đáo khi vào nhà thờ.",
    },
    [
        {"title": "Sobory.ru — Собор Рождества Христова (Стародуб)", "url": "https://sobory.ru/article/?object=00669"},
        {"title": "Wikipedia (RU) — Стародуб", "url": "https://ru.wikipedia.org/wiki/Стародуб"},
    ],
    ["church", "cathedral", "orthodox", "baroque", "starodub", "free"],
    maps_text("Собор Рождества Христова", "Стародуб", "Cathedral of the Nativity of Christ", "Starodub", 52.583070, 32.760780),
))

# 13) Николо-Одрин женский монастырь -----------------------------------------------
RECORDS.append(rec(
    "nikolo-odrin-monastery",
    "Tu viện Thánh Nikolai Odrin (Nikolo-Odrin monaxtyr)",
    "Николо-Одрин женский монастырь",
    "Nikolo-Odrin Convent",
    ["church"],
    53.166950, 35.072844,
    "Làng Odrina, huyện Karachevsky, tỉnh Bryansk, Nga (gần thành phố Karachev, phía đông tỉnh).",
    "Tu viện cổ gần Karachev, nổi tiếng nhờ bức thánh tượng kỳ diệu Đức Mẹ «Người Bảo Lãnh Kẻ Tội Lỗi». Nơi hành hương thanh bình giữa vùng quê phía đông tỉnh Bryansk.",
    "Ẩn mình giữa vùng quê yên ả gần thành phố Karachev ở phía đông tỉnh Bryansk, tu viện Thánh Nikolai Odrin là một trung tâm hành hương cổ kính và được tôn kính. Tu viện có nguồn gốc từ khoảng thế kỷ 15, mang tên Thánh Nikolai và địa danh Odrin nơi nó tọa lạc. Điều làm nên danh tiếng của tu viện chính là bức thánh tượng kỳ diệu của Đức Mẹ mang tên «Sporuchnitsa greshnykh» — «Người Bảo Lãnh Kẻ Tội Lỗi» — được tin là đã làm nên nhiều phép lạ chữa lành, thu hút khách hành hương từ khắp nơi tìm đến cầu nguyện. Ban đầu là tu viện nam, sau thời kỳ Xô viết bị đóng cửa và tàn phá, tu viện được hồi sinh vào thập niên 1990 dưới hình thức tu viện nữ, các công trình dần được phục dựng giữa khung cảnh đồng quê thanh bình. Không khí tĩnh lặng, những nhà thờ và tháp chuông trắng nổi bật giữa nền xanh của cây cỏ tạo nên một không gian linh thiêng và bình yên. Đây là điểm đến ý nghĩa cho khách hành hương cũng như những ai muốn khám phá vùng phía đông ít được biết đến của tỉnh Bryansk.",
    [
        "Tu viện cổ (khoảng thế kỷ 15) gần Karachev, phía đông tỉnh Bryansk.",
        "Nổi tiếng nhờ thánh tượng kỳ diệu Đức Mẹ «Người Bảo Lãnh Kẻ Tội Lỗi».",
        "Khung cảnh đồng quê thanh bình, không khí hành hương tĩnh lặng.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ; nằm ở vùng quê nên nên đi trong ngày.",
        "ticket_vi": "Miễn phí (là tu viện đang hoạt động).",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu, ngày khô ráo.",
        "tips_vi": "Nên đi ô tô; ăn mặc kín đáo, nữ mang khăn trùm đầu; kết hợp thăm Karachev.",
    },
    [
        {"title": "Sobory.ru — Николо-Одрин монастырь", "url": "https://sobory.ru/article/?object=07562"},
        {"title": "Wikipedia (RU) — Одринский Николаевский монастырь", "url": "https://ru.wikipedia.org/wiki/Одринский_Николаевский_монастырь"},
    ],
    ["church", "monastery", "convent", "orthodox", "pilgrimage", "free"],
    maps_text("Николо-Одрин монастырь", "Карачевский район", "Nikolo-Odrin Convent", "Bryansk Oblast", 53.166950, 35.072844),
))

# 14) Усадьба-дворец Завадовского в Ляличах ----------------------------------------
RECORDS.append(rec(
    "lyalichi-palace",
    "Cung điện - điền trang Zavadovsky ở Lyalichi",
    "Усадьба-дворец П. В. Завадовского в Ляличах",
    "Zavadovsky Palace-Estate at Lyalichi",
    ["palace"],
    53.009450, 32.541575,
    "Làng Lyalichi, huyện Surazhsky, tỉnh Bryansk, Nga (phía tây tỉnh, gần thành phố Surazh).",
    "Phế tích tráng lệ của cung điện bá tước Zavadovsky, do kiến trúc sư lừng danh Giacomo Quarenghi thiết kế cuối thế kỷ 18. Từng là một trong những quần thể cung điện - công viên lớn nhất vùng, món quà của Nữ hoàng Ekaterina II.",
    "Giữa vùng quê phía tây tỉnh Bryansk, gần thành phố Surazh, ẩn giấu một trong những di tích kiến trúc quý tộc ấn tượng nhất vùng: cung điện của bá tước Pyotr Zavadovsky ở làng Lyalichi. Được xây dựng cuối thế kỷ 18 theo thiết kế của kiến trúc sư người Ý lừng danh Giacomo Quarenghi — người từng dựng nhiều công trình cổ điển ở Sankt-Peterburg — cung điện là món quà mà Nữ hoàng Ekaterina II ban tặng cho vị sủng thần Zavadovsky. Quần thể xưa kia gồm tòa cung điện nguy nga theo phong cách cổ điển, hệ thống công viên rộng lớn, đài phun nước và ngôi nhà thờ Thánh Ekaterina cũng do Quarenghi thiết kế, tạo thành một trong những điền trang lộng lẫy nhất miền tây nước Nga. Trải qua chiến tranh và thời gian, phần lớn cung điện nay chỉ còn là phế tích, nhưng những hàng cột, mảng tường và dấu vết công viên còn sót lại vẫn toát lên vẻ đẹp hùng vĩ và u hoài của một thời vàng son. Với những ai đam mê lịch sử, kiến trúc và không khí lãng mạn của các điền trang cổ, Lyalichi là điểm đến độc đáo gợi nhớ về đời sống quý tộc Nga thế kỷ 18.",
    [
        "Phế tích cung điện do kiến trúc sư lừng danh Giacomo Quarenghi thiết kế.",
        "Món quà của Nữ hoàng Ekaterina II tặng bá tước Zavadovsky cuối thế kỷ 18.",
        "Từng là một trong những quần thể cung điện - công viên lớn nhất miền tây nước Nga.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do (là phế tích, cần cẩn trọng khi tới gần công trình).",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu, ngày khô ráo để đi lại thuận tiện.",
        "tips_vi": "Nên đi ô tô; mang giày đi bộ; cẩn thận vì công trình đã xuống cấp, không leo trèo.",
    },
    [
        {"title": "tonkosti.ru — Усадьба Завадовского в Ляличах", "url": "https://tonkosti.ru/Усадьба_Завадовского_в_Ляличах"},
        {"title": "Wikipedia (RU) — Ляличи (Брянская область)", "url": "https://ru.wikipedia.org/wiki/Ляличи_(Брянская_область)"},
    ],
    ["palace", "estate", "ruins", "quarenghi", "history", "free"],
    maps_text("Усадьба Завадовского", "Ляличи", "Zavadovsky Palace Lyalichi", "Bryansk Oblast", 53.009450, 32.541575),
))

# 15) Мемориальный комплекс «Хацунь» -----------------------------------------------
RECORDS.append(rec(
    "khatsun-memorial",
    "Khu tưởng niệm «Khatsun» (Hatxun)",
    "Мемориальный комплекс «Хацунь»",
    "Khatsun Memorial Complex",
    ["monument", "museum"],
    53.133855, 34.637347,
    "Làng Khatsun, huyện Karachevsky, tỉnh Bryansk, Nga (cách Bryansk khoảng 30 km về phía đông nam).",
    "Khu tưởng niệm dành cho ngôi làng Khatsun bị phát xít Đức thảm sát năm 1941 — được ví như «Khatyn của nước Nga». Quần thể gồm bảo tàng và các tượng đài tưởng nhớ dân thường bị tàn sát khắp nước Nga trong Thế chiến II.",
    "Cách Bryansk khoảng 30 km về phía đông nam, khu tưởng niệm «Khatsun» được xây dựng trên nền ngôi làng nhỏ Khatsun — nơi diễn ra một trong những tội ác chiến tranh kinh hoàng đầu tiên trên đất Nga trong Chiến tranh Vệ quốc Vĩ đại. Ngày 25 tháng 10 năm 1941, quân phát xít Đức đã thảm sát 318 dân thường vô tội tại đây, gồm cả người già, phụ nữ và trẻ em, để trả đũa hành động của du kích. Vì bi kịch tương tự Khatyn ở Belarus, Khatsun được người dân gọi là «Khatyn của nước Nga». Khu tưởng niệm được khánh thành năm 2011 và trở thành đài tưởng niệm chung cho toàn bộ những ngôi làng và dân thường Nga bị hủy diệt trong chiến tranh. Quần thể gồm các tượng đài xúc động, tấm bia khắc tên những làng quê bị thiêu rụi, nhà nguyện tưởng niệm và một bảo tàng trưng bày tài liệu, hiện vật về tội ác chiến tranh và số phận người dân. Không gian trầm mặc, đầy sức nặng cảm xúc khiến nơi đây trở thành điểm đến sâu lắng để tưởng nhớ và suy ngẫm về những mất mát của thường dân trong chiến tranh.",
    [
        "Tưởng niệm 318 dân thường bị phát xít Đức thảm sát ngày 25/10/1941.",
        "Được ví như «Khatyn của nước Nga» — đài tưởng niệm chung cho các làng bị hủy diệt.",
        "Quần thể gồm tượng đài, bia tưởng niệm, nhà nguyện và bảo tàng, khánh thành năm 2011.",
    ],
    {
        "hours_vi": "Khuôn viên ngoài trời mở cửa tự do; bảo tàng mở giờ hành chính (nên kiểm tra lịch).",
        "ticket_vi": "Vào khuôn viên miễn phí; bảo tàng có thể bán vé.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Mùa hè khô ráo; dịp 9/5 (Ngày Chiến thắng) có hoạt động tưởng niệm.",
        "tips_vi": "Cách Bryansk khoảng 30 km, thuận tiện đi ô tô; giữ thái độ trang nghiêm.",
    },
    [
        {"title": "2GIS — Мемориальный комплекс «Хацунь»", "url": "https://2gis.ru/geo/70030076426318736"},
        {"title": "Wikipedia (RU) — Хацунь", "url": "https://ru.wikipedia.org/wiki/Хацунь"},
    ],
    ["monument", "memorial", "wwii", "museum", "history"],
    maps_text("Мемориальный комплекс Хацунь", "Брянская область", "Khatsun Memorial Complex", "Bryansk Oblast", 53.133855, 34.637347),
))

# 16) Памятник воинам-водителям, Брянск --------------------------------------------
RECORDS.append(rec(
    "monument-to-drivers",
    "Đài tưởng niệm chiến sĩ lái xe (Pamyatnik voinam-voditelyam)",
    "Памятник воинам-водителям",
    "Monument to Soldier-Drivers, Bryansk",
    ["monument"],
    53.198437, 34.529116,
    "Đồi Osinovaya Gorka, cửa ngõ phía đông thành phố Bryansk (cạnh đường M-3 «Ukraina»), huyện Bryansk, tỉnh Bryansk, Nga.",
    "Đài tưởng niệm hiếm có dành riêng cho những người lính lái xe quân sự trong Thế chiến II, dựng năm 1968 ở cửa ngõ phía đông Bryansk. Trên bệ đài là chiếc xe tải huyền thoại ZIS-5, biểu tượng của các đoàn xe tiếp tế thời chiến.",
    "Ngay cửa ngõ phía đông thành phố Bryansk, trên đồi Osinovaya Gorka cạnh tuyến đường lớn M-3, sừng sững một đài tưởng niệm độc đáo dành cho những người lính lái xe quân sự — một chủ đề hiếm khi được vinh danh bằng tượng đài riêng ở Liên Xô. Được khánh thành năm 1968, công trình tri ân hàng vạn tài xế quân đội đã ngày đêm băng qua bom đạn để chở lương thực, vũ khí, đạn dược và thương binh trên những cung đường tiền tuyến trong Chiến tranh Vệ quốc Vĩ đại — công việc thầm lặng nhưng sống còn với chiến thắng. Điểm nhấn của đài tưởng niệm là chiếc xe tải ZIS-5 nguyên bản đặt trên bệ cao — mẫu xe huyền thoại từng là xương sống của các đoàn xe tiếp vận Hồng quân. Vị trí bên đường cao tốc khiến đây trở thành hình ảnh quen thuộc chào đón du khách khi tiến vào Bryansk từ hướng Moskva. Đài tưởng niệm không chỉ là một biểu tượng của thành phố mà còn là lời nhắc nhở về những đóng góp âm thầm của hậu cần và giao thông trong chiến tranh, thu hút nhiều người dừng chân chụp ảnh và tưởng nhớ.",
    [
        "Đài tưởng niệm hiếm có dành riêng cho lính lái xe quân sự thời Thế chiến II.",
        "Trưng bày chiếc xe tải huyền thoại ZIS-5 trên bệ cao.",
        "Vị trí cửa ngõ phía đông Bryansk, hình ảnh quen thuộc chào đón du khách.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do suốt cả ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–20 phút.",
        "best_time_vi": "Ban ngày; dịp 9/5 (Ngày Chiến thắng) có ý nghĩa đặc biệt.",
        "tips_vi": "Nằm cạnh đường cao tốc, tiện dừng chân khi ra/vào Bryansk từ hướng Moskva; chú ý an toàn giao thông.",
    },
    [
        {"title": "2GIS — Памятник воинам-водителям (Брянск)", "url": "https://2gis.ru/bryansk/geo/8726420062732327"},
        {"title": "Wikipedia (RU) — Памятник воинам-водителям (Брянск)", "url": "https://ru.wikipedia.org/wiki/Памятник_воинам-водителям_(Брянск)"},
    ],
    ["monument", "memorial", "wwii", "bryansk", "free"],
    maps_text("Памятник воинам-водителям", "Брянск", "Monument to Soldier-Drivers", "Bryansk", 53.198437, 34.529116),
))

# 17) Брянский государственный краеведческий музей ---------------------------------
RECORDS.append(rec(
    "regional-museum",
    "Bảo tàng địa phương quốc gia Bryansk (Kraevedcheski muzey)",
    "Брянский государственный краеведческий музей",
    "Bryansk State Museum of Local Lore",
    ["museum"],
    53.234001, 34.352859,
    "Quảng trường Partizan (Ploshchad Partizan), số 6, quận Sovetsky, thành phố Bryansk, tỉnh Bryansk, Nga.",
    "Bảo tàng lịch sử - địa phương lớn nhất tỉnh Bryansk, thành lập năm 1921, tọa lạc ngay trên Quảng trường Partizan. Bộ sưu tập phong phú về thiên nhiên, khảo cổ, lịch sử và phong trào du kích của vùng.",
    "Nằm ngay trên Quảng trường Partizan trung tâm thành phố, Bảo tàng địa phương quốc gia Bryansk là bảo tàng lớn nhất và quan trọng nhất của tỉnh, một điểm khởi đầu lý tưởng để hiểu về vùng đất này. Được thành lập năm 1921 và chuyển vào tòa nhà hiện đại trên quảng trường vào thập niên 1980, bảo tàng sở hữu bộ sưu tập đồ sộ trải rộng nhiều lĩnh vực. Các gian trưng bày dẫn khách đi từ thế giới tự nhiên của rừng và sông ngòi Bryansk, qua những phát hiện khảo cổ về các nền văn hóa cổ dọc sông Desna, tới lịch sử hình thành và phát triển của thành phố qua các thời kỳ. Đặc biệt nổi bật là phần trưng bày về Chiến tranh Vệ quốc Vĩ đại và phong trào du kích Bryansk lừng danh — một trong những trang sử hào hùng nhất của vùng, với vũ khí, tài liệu, ảnh tư liệu và hiện vật gốc. Bên cạnh đó là các sưu tập về dân tộc học, nghệ thuật dân gian và đời sống truyền thống. Với vị trí trung tâm và nội dung phong phú, bảo tàng là điểm dừng chân không thể bỏ qua để nắm bắt bức tranh toàn cảnh về thiên nhiên, lịch sử và con người Bryansk.",
    [
        "Bảo tàng lớn nhất tỉnh Bryansk, thành lập năm 1921, ngay trên Quảng trường Partizan.",
        "Trưng bày trọn vẹn thiên nhiên, khảo cổ và lịch sử của vùng.",
        "Phần đặc sắc về phong trào du kích Bryansk trong Thế chiến II.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nghỉ thứ Hai (nên kiểm tra lịch).",
        "ticket_vi": "Vé vào cửa giá bình dân; có thêm phí cho tour hướng dẫn và triển lãm chuyên đề.",
        "duration_vi": "Khoảng 1,5–2 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà); tiện ghép với tham quan trung tâm.",
        "tips_vi": "Nằm ngay trung tâm, dễ kết hợp dạo Quảng trường Partizan, đại lộ Lenin và bờ kè Desna.",
    },
    [
        {"title": "Культура.РФ — Брянский государственный краеведческий музей", "url": "https://www.culture.ru/institutes/12290/bryanskii-gosudarstvennyi-kraevedcheskii-muzei"},
        {"title": "2GIS — Брянский государственный краеведческий музей", "url": "https://2gis.ru/bryansk/firm/8726252559010862"},
    ],
    ["museum", "local-history", "archaeology", "wwii", "partisans", "bryansk"],
    maps_text("Брянский краеведческий музей", "Брянск", "Bryansk State Museum of Local Lore", "Bryansk", 53.234001, 34.352859),
))

# 18) Брянский областной художественный музейно-выставочный центр ------------------
RECORDS.append(rec(
    "art-museum",
    "Trung tâm bảo tàng - triển lãm mỹ thuật tỉnh Bryansk",
    "Брянский областной художественный музейно-выставочный центр",
    "Bryansk Regional Art Museum and Exhibition Center",
    ["museum"],
    53.239094, 34.354272,
    "Phố Emlyutina, số 39, quận Sovetsky, thành phố Bryansk, tỉnh Bryansk, Nga.",
    "Bảo tàng mỹ thuật chủ chốt của tỉnh Bryansk, lưu giữ hội họa, đồ họa, điêu khắc và nghệ thuật trang trí Nga. Nổi bật với các tác phẩm của những họa sĩ Bryansk, trong đó có anh em họa sĩ Tkachev nổi tiếng.",
    "Là bảo tàng mỹ thuật lớn nhất tỉnh Bryansk, Trung tâm bảo tàng - triển lãm mỹ thuật lưu giữ và giới thiệu một bộ sưu tập nghệ thuật phong phú, từ tranh sơn dầu, đồ họa, điêu khắc tới nghệ thuật trang trí - ứng dụng của Nga qua nhiều thời kỳ. Bộ sưu tập bao gồm cả các thánh tượng (icon) cổ, hội họa hiện thực Nga và Xô viết, cùng những tác phẩm của các nghệ sĩ gắn bó với đất Bryansk. Niềm tự hào đặc biệt của bảo tàng là các tác phẩm của anh em họa sĩ Sergei và Aleksei Tkachev — hai bậc thầy hội họa Xô viết sinh ra ở vùng Bryansk, nổi tiếng với những bức tranh chan chứa tình yêu quê hương và đời sống nông thôn Nga. Bên cạnh trưng bày thường xuyên, trung tâm còn tổ chức các triển lãm chuyên đề, sự kiện nghệ thuật và chương trình giáo dục, trở thành một trong những địa chỉ văn hóa sôi động nhất thành phố. Với du khách yêu nghệ thuật, đây là nơi lý tưởng để cảm nhận tâm hồn và bản sắc của vùng đất Bryansk qua lăng kính hội họa.",
    [
        "Bảo tàng mỹ thuật lớn nhất tỉnh Bryansk với bộ sưu tập đa dạng.",
        "Nổi bật với tác phẩm của anh em họa sĩ Tkachev — bậc thầy hội họa Xô viết quê Bryansk.",
        "Thường xuyên tổ chức triển lãm chuyên đề và sự kiện nghệ thuật.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nghỉ thứ Hai (nên kiểm tra lịch).",
        "ticket_vi": "Vé vào cửa giá bình dân; triển lãm chuyên đề có thể tính phí riêng.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Kiểm tra lịch triển lãm hiện hành; nằm ở trung tâm, dễ kết hợp dạo phố.",
    },
    [
        {"title": "Yandex Maps — Брянский областной художественный музейно-выставочный центр", "url": "https://yandex.com/maps/org/bryansk_regional_art_museum_and_exhibition_center/1018966478/"},
        {"title": "Wikipedia (RU) — Брянск", "url": "https://ru.wikipedia.org/wiki/Брянск"},
    ],
    ["museum", "art", "painting", "tkachev", "bryansk"],
    maps_org("https://yandex.com/maps/org/bryansk_regional_art_museum_and_exhibition_center/1018966478/", "Bryansk Regional Art Museum", "Bryansk"),
))

# 19) Брянский театр драмы им. А. К. Толстого --------------------------------------
RECORDS.append(rec(
    "drama-theatre",
    "Nhà hát kịch tỉnh Bryansk mang tên A. K. Tolstoy",
    "Брянский театр драмы имени А. К. Толстого",
    "Bryansk Regional Drama Theatre named after A. K. Tolstoy",
    ["theatre"],
    53.242525, 34.361974,
    "Phố Fokina, số 26, quận Sovetsky, thành phố Bryansk, tỉnh Bryansk, Nga.",
    "Nhà hát kịch hàng đầu của tỉnh Bryansk, mang tên văn hào A. K. Tolstoy — người con của vùng đất này. Trung tâm đời sống sân khấu của thành phố với các vở kinh điển Nga và tác phẩm đương đại.",
    "Nằm trên phố Fokina ở trung tâm Bryansk, Nhà hát kịch tỉnh là trái tim của đời sống sân khấu thành phố. Nhà hát mang tên Aleksey Konstantinovich Tolstoy — nhà thơ, nhà viết kịch tài hoa gắn bó với vùng Bryansk (điền trang Krasny Rog của ông nằm trong tỉnh), như một sự tôn vinh di sản văn học địa phương. Ra đời từ giữa thập niên 1920, nhà hát đã trải qua gần một thế kỷ hoạt động, dàn dựng vô số vở diễn từ kịch kinh điển Nga của Chekhov, Ostrovsky, Gogol tới các tác phẩm hiện đại và kịch dành cho khán giả nhỏ tuổi. Tòa nhà nhà hát với sảnh trang trọng và khán phòng ấm cúng là nơi lui tới quen thuộc của người dân Bryansk trong những buổi tối văn hóa. Nằm ở vị trí trung tâm gần các bảo tàng, quảng trường và đại lộ chính, nhà hát dễ dàng kết hợp trong hành trình khám phá thành phố. Với du khách yêu nghệ thuật, một buổi tối thưởng thức kịch tại đây là cách thú vị để hòa vào nhịp sống văn hóa của người dân địa phương, ngay cả khi chỉ để cảm nhận không khí của một nhà hát tỉnh lỵ Nga.",
    [
        "Nhà hát kịch hàng đầu tỉnh Bryansk, hoạt động từ giữa thập niên 1920.",
        "Mang tên văn hào A. K. Tolstoy — người con gắn bó với vùng đất Bryansk.",
        "Dàn dựng cả kịch kinh điển Nga lẫn tác phẩm đương đại, vị trí trung tâm.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch mùa, thường vào buổi tối và cuối tuần; phòng vé mở ban ngày.",
        "ticket_vi": "Vé giá phải chăng, thay đổi theo vở diễn và hạng ghế.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ.",
        "best_time_vi": "Mùa diễn từ thu đến xuân; xem lịch trên trang chính thức của nhà hát.",
        "tips_vi": "Đặt vé trước cho các vở nổi tiếng; đến sớm để gửi áo khoác ở quầy garderob.",
    },
    [
        {"title": "2GIS — Брянский театр драмы им. А. К. Толстого", "url": "https://2gis.ru/bryansk/firm/8726252559031995"},
        {"title": "Wikipedia (RU) — Брянский театр драмы имени А. К. Толстого", "url": "https://ru.wikipedia.org/wiki/Брянский_театр_драмы_имени_А._К._Толстого"},
    ],
    ["theatre", "drama", "culture", "performing-arts", "bryansk"],
    maps_text("Брянский театр драмы", "Брянск", "Bryansk Drama Theatre", "Bryansk", 53.242525, 34.361974),
))

# 20) Брянский областной театр кукол -----------------------------------------------
RECORDS.append(rec(
    "puppet-theatre",
    "Nhà hát múa rối tỉnh Bryansk (Teatr kukol)",
    "Брянский областной театр кукол",
    "Bryansk Regional Puppet Theatre",
    ["theatre"],
    53.264145, 34.412469,
    "Phố Pushkina, số 12, thành phố Bryansk, tỉnh Bryansk, Nga.",
    "Nhà hát múa rối được yêu thích của Bryansk, điểm đến văn hóa lý tưởng cho gia đình và trẻ em. Sân khấu dàn dựng các vở cổ tích Nga và thế giới bằng nghệ thuật rối sinh động.",
    "Nhà hát múa rối tỉnh Bryansk là một trong những địa chỉ văn hóa được các gia đình và trẻ em yêu thích nhất thành phố. Hoạt động từ thập niên 1970, nhà hát chuyên dàn dựng các vở diễn dựa trên truyện cổ tích Nga và thế giới, những câu chuyện dân gian và tác phẩm thiếu nhi, được thể hiện bằng nghệ thuật rối phong phú — từ rối tay, rối dây tới các con rối lớn đầy màu sắc. Đằng sau mỗi buổi diễn là công sức của các nghệ sĩ điều khiển rối tài năng cùng đội ngũ họa sĩ, nhà thiết kế tạo nên những con rối và bối cảnh sân khấu sinh động, kích thích trí tưởng tượng của khán giả nhỏ tuổi. Không chỉ mang tính giải trí, các vở diễn còn lồng ghép những bài học nhẹ nhàng về lòng tốt, tình bạn và cái thiện, phù hợp với mọi lứa tuổi. Với du khách đi cùng trẻ nhỏ, một buổi xem múa rối tại đây là trải nghiệm đáng yêu và đậm chất văn hóa Nga, đồng thời là dịp để cảm nhận đời sống nghệ thuật dành cho thiếu nhi của thành phố Bryansk.",
    [
        "Nhà hát múa rối được yêu thích, lý tưởng cho gia đình và trẻ em.",
        "Dàn dựng các vở cổ tích Nga và thế giới bằng nghệ thuật rối sinh động.",
        "Hoạt động từ thập niên 1970, giàu tính giải trí và giáo dục.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch, thường vào cuối tuần và dịp lễ; phòng vé mở ban ngày.",
        "ticket_vi": "Vé giá bình dân, phù hợp với gia đình.",
        "duration_vi": "Một buổi diễn khoảng 45–60 phút.",
        "best_time_vi": "Cuối tuần và kỳ nghỉ; xem lịch diễn trước khi tới.",
        "tips_vi": "Đặt vé trước cho các suất cuối tuần; phù hợp nhất với trẻ em.",
    },
    [
        {"title": "2GIS — Брянский областной театр кукол", "url": "https://2gis.ru/bryansk/firm/8726252559009179"},
        {"title": "Wikipedia (RU) — Брянск", "url": "https://ru.wikipedia.org/wiki/Брянск"},
    ],
    ["theatre", "puppet", "family", "children", "bryansk"],
    maps_text("Брянский областной театр кукол", "Брянск", "Bryansk Regional Puppet Theatre", "Bryansk", 53.264145, 34.412469),
))

# 21) Парк-музей им. А. К. Толстого (деревянная скульптура) ------------------------
RECORDS.append(rec(
    "tolstoy-park-museum",
    "Công viên - bảo tàng A. K. Tolstoy (điêu khắc gỗ)",
    "Парк-музей имени А. К. Толстого",
    "A. K. Tolstoy Park-Museum, Bryansk",
    ["park_garden"],
    53.246337, 34.359696,
    "Bulvar Gagarina, số 33, quận Sovetsky, thành phố Bryansk, tỉnh Bryansk, Nga.",
    "Công viên trung tâm nổi tiếng khắp nước Nga nhờ bộ sưu tập điêu khắc gỗ độc đáo ngoài trời. Một bảo tàng nghệ thuật gỗ giữa lòng thành phố, mang tên văn hào A. K. Tolstoy.",
    "Nằm ngay trung tâm Bryansk gần Quảng trường Lenin, Công viên - bảo tàng mang tên A. K. Tolstoy là một trong những công viên độc đáo và nổi tiếng nhất nước Nga. Được lập từ năm 1936, công viên trở thành biểu tượng của thành phố nhờ bộ sưu tập điêu khắc gỗ ngoài trời phong phú, bắt đầu hình thành từ thập niên 1960 khi các nghệ nhân địa phương biến những thân cây thành tác phẩm nghệ thuật. Dạo bước dưới bóng cây, du khách sẽ bắt gặp hàng loạt tác phẩm gỗ sống động lấy cảm hứng từ truyện cổ tích Nga, thần thoại dân gian, các nhân vật văn học và cả những hình tượng ẩn dụ đầy sáng tạo — từ chú gấu, nàng tiên, dũng sĩ tới những khối tượng trừu tượng. Chính sự kết hợp giữa không gian xanh mát và nghệ thuật điêu khắc gỗ độc đáo đã biến nơi đây thành một «bảo tàng ngoài trời» thực thụ, khác hẳn các công viên thông thường. Công viên mang tên văn hào A. K. Tolstoy như một sự tôn vinh di sản văn hóa của vùng. Đây là điểm dạo chơi, chụp ảnh và thư giãn lý tưởng cho mọi lứa tuổi ngay giữa lòng Bryansk.",
    [
        "Công viên trung tâm nổi tiếng cả nước nhờ bộ sưu tập điêu khắc gỗ ngoài trời.",
        "Các tác phẩm gỗ lấy cảm hứng từ cổ tích, thần thoại và văn học Nga.",
        "Một «bảo tàng ngoài trời» độc đáo, mang tên văn hào A. K. Tolstoy.",
    ],
    {
        "hours_vi": "Công viên ngoài trời, mở cửa tự do hằng ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Mùa hè và mùa thu; buổi chiều mát để dạo bộ.",
        "tips_vi": "Nằm ngay trung tâm, dễ kết hợp dạo Quảng trường Lenin và bulvar Gagarina; mang máy ảnh.",
    },
    [
        {"title": "Yandex Maps — Парк-музей имени А. К. Толстого", "url": "https://yandex.com/maps/org/park_muzey_imeni_a_k_tolstogo/1108957021/"},
        {"title": "Wikipedia (RU) — Парк-музей имени А. К. Толстого", "url": "https://ru.wikipedia.org/wiki/Парк-музей_имени_А._К._Толстого"},
    ],
    ["park-garden", "sculpture", "wood-art", "open-air-museum", "bryansk", "free"],
    maps_org("https://yandex.com/maps/org/park_muzey_imeni_a_k_tolstogo/1108957021/", "A. K. Tolstoy Park-Museum", "Bryansk"),
))

# 22) Бульвар Гагарина -------------------------------------------------------------
RECORDS.append(rec(
    "bulvar-gagarina",
    "Đại lộ đi bộ Gagarin (Bulvar Gagarina)",
    "Бульвар Гагарина",
    "Gagarin Boulevard, Bryansk",
    ["square_street"],
    53.241670, 34.367500,
    "Bulvar Gagarina, quận Sovetsky, thành phố Bryansk, tỉnh Bryansk, Nga (nối Quảng trường Lenin xuống bờ sông Desna).",
    "Phố đi bộ trung tâm sầm uất của Bryansk, thường được gọi là «Arbat của Bryansk». Con phố dốc nối Quảng trường Lenin xuống bờ sông Desna qua «cầu thang Potyomkin» nổi tiếng.",
    "Bulvar Gagarina là con phố đi bộ nhộn nhịp và được yêu thích nhất của Bryansk, thường được người dân ví như «Arbat của Bryansk». Con đại lộ dốc thoai thoải nối từ Quảng trường Lenin trên cao xuống tận bờ sông Desna, tạo thành trục dạo bộ chính của khu trung tâm lịch sử. Dọc hai bên là những tòa nhà cổ kính, cửa hàng, quán cà phê, nhà hàng cùng nhiều tác phẩm điêu khắc và tiểu cảnh trang trí thú vị, biến nơi đây thành không gian tản bộ, mua sắm và gặp gỡ sôi động. Điểm nhấn đặc biệt của con phố là dãy bậc thang lớn dẫn xuống bờ sông — được người dân gọi vui là «cầu thang Potyomkin» của Bryansk (gợi nhớ cầu thang nổi tiếng ở Odessa) — nơi mở ra khung cảnh sông Desna thoáng đãng. Vào buổi tối và những ngày lễ, đại lộ càng thêm nhộn nhịp với đèn hoa, nghệ sĩ đường phố và dòng người dạo chơi. Đây là nơi lý tưởng để cảm nhận nhịp sống thường nhật của người dân Bryansk và là điểm khởi đầu tự nhiên cho hành trình khám phá trung tâm thành phố.",
    [
        "Phố đi bộ trung tâm sầm uất — «Arbat của Bryansk».",
        "Dốc nối Quảng trường Lenin xuống bờ sông Desna qua «cầu thang Potyomkin» nổi tiếng.",
        "Nhiều quán cà phê, cửa hàng, tượng trang trí và không khí dạo chơi về đêm.",
    ],
    {
        "hours_vi": "Phố đi bộ ngoài trời, tự do suốt cả ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Buổi chiều tối mùa hè, khi phố đông vui và lên đèn.",
        "tips_vi": "Đi bộ xuống bậc thang để ngắm sông Desna; nhiều quán cà phê để nghỉ chân.",
    },
    [
        {"title": "Wikipedia (RU) — Бульвар Гагарина (Брянск)", "url": "https://ru.wikipedia.org/wiki/Бульвар_Гагарина_(Брянск)"},
        {"title": "Wikipedia (RU) — Брянск", "url": "https://ru.wikipedia.org/wiki/Брянск"},
    ],
    ["square-street", "pedestrian", "promenade", "city-center", "bryansk", "free"],
    maps_text("Бульвар Гагарина", "Брянск", "Gagarin Boulevard", "Bryansk", 53.241670, 34.367500),
))

# 23) Площадь Партизан -------------------------------------------------------------
RECORDS.append(rec(
    "ploshchad-partizan",
    "Quảng trường Partizan (Ploshchad Partizan)",
    "Площадь Партизан",
    "Partizan Square, Bryansk",
    ["square_street", "monument"],
    53.234720, 34.353610,
    "Quảng trường Partizan (giao đại lộ Lenin và phố Krasnoarmeyskaya), quận Sovetsky, thành phố Bryansk, tỉnh Bryansk, Nga.",
    "Quảng trường trung tâm và biểu tượng của Bryansk, nơi đặt đài tưởng niệm hoành tráng dành cho những người lính và du kích giải phóng thành phố. Trái tim đô thị với tượng đài, bảo tàng và các sự kiện lớn.",
    "Quảng trường Partizan là quảng trường chính và biểu tượng bậc nhất của thành phố Bryansk, nơi hội tụ lịch sử và đời sống công cộng của đô thị. Trung tâm của quảng trường là một quần thể đài tưởng niệm hoành tráng tôn vinh những người lính và du kích đã chiến đấu và giải phóng Bryansk khỏi phát xít Đức trong Chiến tranh Vệ quốc Vĩ đại — chủ đề du kích vốn là niềm tự hào đặc biệt của vùng đất này. Tổ hợp gồm cột đài tưởng niệm vươn cao cùng các nhóm tượng khắc họa hình ảnh chiến sĩ và du kích quân đầy khí thế, gợi nhắc những năm tháng kháng chiến gian khổ trong rừng Bryansk. Ngay bên quảng trường là tòa nhà Bảo tàng địa phương quốc gia Bryansk, tạo thành một cụm văn hóa - lịch sử quan trọng. Đây cũng là nơi diễn ra các sự kiện trọng đại của thành phố, đặc biệt là lễ kỷ niệm Ngày Chiến thắng 9/5 và ngày giải phóng Bryansk 17/9, khi hàng nghìn người dân tụ họp dâng hoa và tưởng nhớ. Với vị trí trung tâm và ý nghĩa biểu tượng sâu sắc, Quảng trường Partizan là điểm khởi đầu quen thuộc cho mọi hành trình khám phá Bryansk.",
    [
        "Quảng trường trung tâm và biểu tượng của Bryansk.",
        "Đài tưởng niệm hoành tráng dành cho lính và du kích giải phóng thành phố.",
        "Nơi diễn ra các lễ kỷ niệm lớn, cạnh Bảo tàng địa phương quốc gia Bryansk.",
    ],
    {
        "hours_vi": "Quảng trường ngoài trời, tự do suốt cả ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Ban ngày; đặc biệt trang nghiêm dịp 9/5 và 17/9 (ngày giải phóng Bryansk).",
        "tips_vi": "Kết hợp tham quan Bảo tàng địa phương ngay cạnh; điểm khởi đầu để dạo đại lộ Lenin.",
    },
    [
        {"title": "Wikipedia (RU) — Площадь Партизан (Брянск)", "url": "https://ru.wikipedia.org/wiki/Площадь_Партизан_(Брянск)"},
        {"title": "Wikipedia (RU) — Брянск", "url": "https://ru.wikipedia.org/wiki/Брянск"},
    ],
    ["square-street", "monument", "memorial", "wwii", "partisans", "bryansk", "free"],
    maps_text("Площадь Партизан", "Брянск", "Partizan Square", "Bryansk", 53.234720, 34.353610),
))

# 24) Славянская площадь -----------------------------------------------------------
RECORDS.append(rec(
    "slavyanskaya-square",
    "Quảng trường Slavyanskaya (Slavyanxkaya ploshchad)",
    "Славянская площадь",
    "Slavyanskaya Square, Bryansk",
    ["square_street"],
    53.240280, 34.373610,
    "Quảng trường Slavyanskaya, khu bờ kè sông Desna, quận Sovetsky, thành phố Bryansk, tỉnh Bryansk, Nga.",
    "Quảng trường hiện đại bên bờ sông Desna, nổi bật với đài phun nước «Tình hữu nghị» và không gian dạo chơi ven sông. Điểm hẹn được yêu thích cho các buổi hòa nhạc và lễ hội thành phố.",
    "Nằm dưới chân đại lộ đi bộ Gagarina, ngay bên bờ kè sông Desna, Quảng trường Slavyanskaya là một trong những không gian công cộng hiện đại và sống động nhất của Bryansk. Được cải tạo thành quảng trường lễ hội, nơi đây gây ấn tượng với đài phun nước lớn — thường được gắn với tên gọi «Tình hữu nghị» (Druzhba) — cùng những bậc thang, lối dạo và không gian mở nhìn ra dòng sông. Vào mùa hè, đài phun nước và khung cảnh ven sông biến quảng trường thành điểm hẹn ưa thích của người dân và du khách để tản bộ, nghỉ ngơi và tránh nóng. Đây cũng là sân khấu ngoài trời cho nhiều sự kiện lớn của thành phố: các buổi hòa nhạc, lễ hội dân gian Slav, hội chợ và những màn trình diễn trong các dịp lễ trọng. Vị trí liền kề bulvar Gagarina và bờ kè Desna khiến Slavyanskaya trở thành mắt xích tự nhiên trong tuyến dạo bộ trung tâm, nơi du khách có thể kết hợp ngắm cảnh sông, thư giãn và hòa mình vào không khí lễ hội đặc trưng của Bryansk.",
    [
        "Quảng trường lễ hội hiện đại bên bờ sông Desna.",
        "Nổi bật với đài phun nước lớn và không gian dạo chơi ven sông.",
        "Sân khấu ngoài trời cho các buổi hòa nhạc và lễ hội thành phố.",
    ],
    {
        "hours_vi": "Quảng trường ngoài trời, tự do suốt cả ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Buổi tối mùa hè khi đài phun nước hoạt động và quảng trường lên đèn.",
        "tips_vi": "Kết hợp dạo bulvar Gagarina và bờ kè Desna; đông vui vào các dịp lễ hội.",
    },
    [
        {"title": "2GIS — Славянская площадь (Брянск)", "url": "https://2gis.ru/bryansk/geo/8726411472797712"},
        {"title": "Wikipedia (RU) — Брянск", "url": "https://ru.wikipedia.org/wiki/Брянск"},
    ],
    ["square-street", "embankment", "fountain", "city-center", "bryansk", "free"],
    maps_text("Славянская площадь", "Брянск", "Slavyanskaya Square", "Bryansk", 53.240280, 34.373610),
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
