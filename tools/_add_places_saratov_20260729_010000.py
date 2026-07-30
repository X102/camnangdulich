# -*- coding: utf-8 -*-
"""_add_places_saratov_20260729_010000.py — VÙNG: Tỉnh Saratov (Саратовская область)
(lần chạy tự động 2026-07-29).

Bối cảnh: saratov.json hiện có 7 địa điểm (Набережная Космонавтов, Место приземления Гагарина,
Парк Победы на Соколовой горе, музей Радищева, Национальный парк «Хвалынский», консерватория
им. Собинова, лимонарий). Bổ sung 25 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại
hình → đưa vùng lên 32. TRÁNH trùng 7 điểm trên (đặc biệt KHÔNG thêm lại museum Радищева,
Хвалынский нацпарк, набережная, Соколовая гора).

Phân bố loại hình (25 bản ghi mới):
- church (4): Троицкий собор, церковь «Утоли моя печали», Покровский храм, Соборная мечеть
  (mечеть xếp category "church" theo quy ước dự án cho công trình tôn giáo, kèm tag "mosque").
- museum (7): областной музей краеведения, музей-усадьба Чернышевского, музей Федина,
  Дом-музей Павла Кузнецова, музей Петрова-Водкина (Хвалынск), Энгельсский краеведческий музей,
  музей-усадьба Борисова-Мусатова.
- theatre (3): театр оперы и балета, театр драмы им. Слонова, ТЮЗ им. Киселёва.
- square_street (2): проспект Кирова (пешеходный), Театральная площадь.
- park_garden (3): парк «Липки», городской парк им. Горького, Утёс Степана Разина (памятник природы).
- bridge (1): Саратовский мост (Саратов–Энгельс).
- other (2): цирк братьев Никитиных, Крытый рынок.
- monument (3): памятник песне «Огней так много золотых…», СГУ (главный корпус, памятник архитектуры),
  памятник «Бык-солевоз» (Энгельс).

TOẠ ĐỘ — xác minh chéo (sobory.ru infobox «Координаты»; 2GIS firm/geo point; ru.wikipedia; Яндекс.Карты,
2026-07-29). Phạm vi Saratov lat ~50.2–52.9, lon ~42.5–50.7 (TP Саратов ~51.53, 46.03; Энгельс ~51.48,
46.12; Хвалынск ~52.50, 48.10) — tất cả toạ độ trong phạm vi, lat luôn > lon, KHÔNG đảo lat/lon:
  Троицкий собор 51.528063,46.055139 (sobory 02694); «Утоли моя печали» 51.530258,46.035760 (sobory 07134);
  Покровский храм 51.540370,46.035290 (sobory 06780); Соборная мечеть 51.537478,46.038216 (2gis firm);
  областной музей краеведения 51.527573,46.056017 (2gis firm); музей Чернышевского 51.524763,46.040787
  (2gis); музей Федина 51.526402,46.045539 (2gis); Дом-музей Кузнецова 51.533894,46.048234 (2gis);
  музей Петрова-Водкина/Хвалынск 52.475089,48.102930 (2gis firm); Энгельсский краеведческий музей
  51.502877,46.120173 (2gis); музей Борисова-Мусатова 51.524224,46.019384 (2gis); театр оперы и балета
  51.532955,46.031990 (2gis geo, Театральная пл. 1); театр драмы Слонова 51.534129,46.001656 (2gis);
  ТЮЗ Киселёва 51.534635,46.024396 (2gis); проспект Кирова 51.530224,46.032269 (2gis geo);
  Театральная площадь 51.532946,46.034033 (2gis geo); парк «Липки» 51.528241,46.037141 (2gis geo);
  парк им. Горького 51.519207,45.998754 (2gis); Утёс Степана Разина 50.615500,45.652600 (ru.wiki +
  Яндекс, Красноармейский р-н); Саратовский мост 51.529042,46.062535 (2gis geo); цирк братьев Никитиных
  51.533854,46.021203 (2gis, Чапаева 61); Крытый рынок 51.532126,46.020288 (2gis, Чапаева 59); памятник
  песне «Огней так много золотых» 51.531778,46.025933 (2gis geo, проспект Кирова); СГУ гл. корпус
  51.538922,46.010392 (2gis, Астраханская 83); памятник «Бык-солевоз» Энгельс 51.485503,46.126829 (2gis geo).

GHI CHÚ: BỎ QUA vì đã có trong file / trùng: музей Радищева, Хвалынский нацпарк, Соколовая гора,
набережная. Проспект Кирова năm 2023 đổi tên chính thức thành «проспект имени Петра Столыпина» — bản
ghi ghi rõ cả hai tên. Các điểm rủi ro toạ độ (Кудеярова пещера/Кудеяров стан — nhiều nguồn mâu thuẫn
vị trí) KHÔNG đưa vào để tránh bịa. KHÔNG bịa toạ độ, KHÔNG nhồi.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_saratov_20260729_010000.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "saratov"
REGION_NAME_VI = "Tỉnh Saratov"
FD = "Vùng Volga"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
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

# ============================ NHÀ THỜ / TÔN GIÁO (church) ============================

# 1) Троицкий собор ---------------------------------------------------------------
RECORDS.append(rec(
    "trinity-cathedral-saratov",
    "Nhà thờ chính toà Ba Ngôi (Trôi-txki xa-bo)",
    "Свято-Троицкий собор",
    "Holy Trinity Cathedral",
    ["church"],
    51.528063, 46.055139,
    "Quảng trường Bảo tàng (Музейная площадь), phố Moskovskaya 6, trung tâm lịch sử thành phố Saratov, tỉnh Saratov, Nga",
    "Nhà thờ chính toà Ba Ngôi là công trình cổ nhất còn lại của Saratov, xây dựng cuối thế kỷ 17 - đầu thế kỷ 18 theo phong cách baroque Moskva (baroque Naryshkin). Với tháp chuông cao và những mái vòm vàng bên bờ sông Volga, đây là biểu tượng kiến trúc và tâm linh lâu đời nhất thành phố.",
    "Đứng trên Quảng trường Bảo tàng ở lõi lịch sử của Saratov, Nhà thờ chính toà Ba Ngôi (Свято-Троицкий собор) được xem là công trình bằng đá cổ nhất còn tồn tại của thành phố. Được khởi dựng vào những năm cuối thế kỷ 17 và hoàn thiện đầu thế kỷ 18, nhà thờ mang phong cách baroque Moskva (còn gọi là baroque Naryshkin) đặc trưng với khối hai tầng, các gờ trang trí bằng gạch trắng nổi trên nền tường ấm, hành lang bao quanh và tháp chuông vươn cao đội chóp nhọn. Qua hơn ba thế kỷ, công trình đã trải qua nhiều lần trùng tu sau hoả hoạn, lún nền và những biến động thời Xô viết, song vẫn giữ được diện mạo cổ kính hiếm hoi giữa một đô thị hiện đại. Bên trong lưu giữ những bức tượng thánh (iconostas) và di vật được người dân địa phương đặc biệt sùng kính. Nằm gần bờ kè và các bảo tàng trung tâm, ngôi thánh đường với những mái vòm dát vàng lấp lánh trở thành điểm khởi đầu tự nhiên cho hành trình khám phá phố cổ Saratov, đồng thời là chốn hành hương và chiêm ngưỡng kiến trúc Nga cổ truyền.",
    [
        "Công trình bằng đá CỔ NHẤT còn lại của Saratov (cuối thế kỷ 17 - đầu 18).",
        "Kiến trúc baroque Moskva (Naryshkin) với tháp chuông cao và mái vòm dát vàng.",
        "Toạ lạc trên Quảng trường Bảo tàng, sát bờ kè và khu bảo tàng trung tâm.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 7:00–19:00; nên kiểm tra lịch lễ trước.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 30–45 phút.",
      "Quanh năm; dịp lễ Chính thống giáo (Giáng sinh, Phục sinh) không khí đặc biệt trang nghiêm.",
      "Ăn mặc kín đáo, nữ nên có khăn trùm đầu; giữ yên lặng trong giờ lễ. Kết hợp dạo Quảng trường Bảo tàng và bờ kè gần đó."),
    [
        {"title": "Wikipedia (RU) — Свято-Троицкий собор (Саратов)", "url": "https://ru.wikipedia.org/wiki/Свято-Троицкий_собор_(Саратов)"},
        {"title": "Sobory.ru — Собор Троицы Живоначальной", "url": "https://sobory.ru/article/?object=02694"},
    ],
    ["church", "orthodox", "baroque", "historic", "landmark", "saratov"],
    maps_text("Свято-Троицкий собор", "Саратов", "Holy Trinity Cathedral", "Saratov", 51.528063, 46.055139),
))

# 2) Церковь «Утоли моя печали» ---------------------------------------------------
RECORDS.append(rec(
    "utoli-moya-pechali-church-saratov",
    "Nhà thờ 'Xoa dịu nỗi buồn của con' (U-tô-li mai-a pê-tra-li)",
    "Церковь «Утоли моя печали»",
    "Church 'Assuage My Sorrows'",
    ["church"],
    51.530258, 46.035760,
    "Phố Volzhskaya 36, trung tâm thành phố Saratov, tỉnh Saratov, Nga",
    "Ngôi nhà thờ nhỏ nổi tiếng với cụm mái vòm hành nhiều màu rực rỡ, phỏng theo Nhà thờ Thánh Vasily trên Quảng trường Đỏ ở Moskva. Xây năm 1906, đây là một trong những công trình được chụp ảnh nhiều nhất Saratov.",
    "Nhà thờ 'Utoli moya pechali' (nghĩa là 'Xoa dịu nỗi buồn của con', theo tên một biểu tượng Đức Mẹ) là một trong những công trình duyên dáng và dễ nhận ra nhất Saratov. Được xây dựng năm 1906 theo thiết kế của kiến trúc sư Pyotr Zybin, nhà thờ mô phỏng có chủ ý phong cách Nga cổ và đặc biệt gợi nhớ Nhà thờ Thánh Vasily (Pokrovsky) trên Quảng trường Đỏ Moskva, với cụm nhiều mái vòm hành (mái củ hành) sơn màu rực rỡ, xoắn ốc và hoa văn sặc sỡ. Dù có kích thước khiêm tốn, sự phong phú về màu sắc và hình khối khiến ngôi thánh đường nổi bật giữa những dãy phố trung tâm và trở thành một 'điểm nhấn thị giác' được du khách lẫn người dân yêu thích. Thời Xô viết, toà nhà từng bị trưng dụng làm cơ sở khác, nhưng sau này được trả lại cho Giáo hội và trùng tu, khôi phục vẻ lộng lẫy ban đầu. Nằm ngay trên phố Volzhskaya ở khu trung tâm, gần Quảng trường Bảo tàng và bờ kè, nhà thờ là điểm dừng chân lý tưởng để chiêm ngưỡng và chụp ảnh trên hành trình dạo phố cổ Saratov.",
    [
        "Cụm mái vòm hành nhiều màu rực rỡ, gợi nhớ Nhà thờ Thánh Vasily ở Moskva.",
        "Xây năm 1906 theo thiết kế kiến trúc sư Pyotr Zybin, phong cách Nga cổ.",
        "Một trong những công trình được chụp ảnh nhiều nhất trung tâm Saratov.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 8:00–19:00; nên kiểm tra trước.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 20–30 phút.",
      "Quanh năm; ánh nắng ban ngày làm nổi bật màu sắc các mái vòm khi chụp ảnh.",
      "Ăn mặc kín đáo khi vào trong; góc chụp đẹp nhất từ vỉa hè đối diện. Kết hợp dạo phố đi bộ Prospekt Kirova gần đó."),
    [
        {"title": "Wikipedia (RU) — Церковь «Утоли моя печали» (Саратов)", "url": "https://ru.wikipedia.org/wiki/Церковь_«Утоли_моя_печали»_(Саратов)"},
        {"title": "Sobory.ru — Церковь иконы Божией Матери «Утоли моя печали»", "url": "https://sobory.ru/article/?object=07134"},
    ],
    ["church", "orthodox", "colorful", "russian-revival", "landmark", "saratov"],
    maps_text("Церковь Утоли моя печали", "Саратов", "Church Assuage My Sorrows", "Saratov", 51.530258, 46.035760),
))

# 3) Покровский храм --------------------------------------------------------------
RECORDS.append(rec(
    "pokrovsky-church-saratov",
    "Nhà thờ Đức Mẹ Che Chở (Pô-crốp-xki khram)",
    "Храм в честь Покрова Пресвятой Богородицы",
    "Church of the Intercession of the Theotokos",
    ["church"],
    51.540370, 46.035290,
    "Phố Gorkogo 85 (khu 'Na Gorakh'), thành phố Saratov, tỉnh Saratov, Nga",
    "Nhà thờ Đức Mẹ Che Chở là một thánh đường gạch đỏ đồ sộ theo phong cách Nga - Byzantine, xây đầu thế kỷ 20 ở khu 'trên đồi' của Saratov. Với năm mái vòm xanh và tháp chuông cao, đây là một trong những nhà thờ lớn và đẹp nhất thành phố.",
    "Nhà thờ Đức Mẹ Che Chở (Покровский храм) toạ lạc ở khu 'Na Gorakh' ('trên các ngọn đồi') phía bắc trung tâm Saratov, là một trong những công trình tôn giáo bề thế và ấn tượng nhất thành phố. Được xây dựng trong thập niên đầu thế kỷ 20 bằng gạch đỏ trần theo phong cách Nga - Byzantine, nhà thờ nổi bật với khối kiến trúc cân đối, năm mái vòm hành sơn xanh điểm sao vàng và tháp chuông vươn cao. Nội thất rộng rãi với những bức bích hoạ và iconostas được khôi phục công phu sau thời kỳ đóng cửa và sử dụng sai mục đích dưới thời Xô viết. Ngôi thánh đường không chỉ là nơi thờ phụng đông đúc mà còn là trung tâm đời sống giáo xứ, với trường Chúa nhật và các hoạt động cộng đồng. Nằm hơi tách khỏi lõi du lịch nhưng dễ tiếp cận, Покровский храм mang lại trải nghiệm về một nhà thờ Chính thống giáo 'sống', đồng thời là ví dụ tiêu biểu cho kiến trúc tôn giáo Nga đầu thế kỷ 20 ở vùng Volga.",
    [
        "Thánh đường gạch đỏ đồ sộ phong cách Nga - Byzantine đầu thế kỷ 20.",
        "Năm mái vòm hành sơn xanh điểm sao vàng và tháp chuông cao.",
        "Trung tâm đời sống giáo xứ ở khu 'Na Gorakh' của Saratov.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường khoảng 7:00–19:00; nên kiểm tra trước.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 30 phút.",
      "Quanh năm; dịp lễ lớn Chính thống giáo không khí đông đúc, trang nghiêm.",
      "Ăn mặc kín đáo, nữ nên có khăn trùm đầu; giữ yên lặng trong giờ lễ."),
    [
        {"title": "Wikipedia (RU) — Покровская церковь (Саратов)", "url": "https://ru.wikipedia.org/wiki/Покровская_церковь_(Саратов)"},
        {"title": "Sobory.ru — Церковь Покрова Пресвятой Богородицы", "url": "https://sobory.ru/article/?object=06780"},
    ],
    ["church", "orthodox", "russian-byzantine", "brick", "saratov"],
    maps_text("Покровский храм", "Саратов", "Church of the Intercession", "Saratov", 51.540370, 46.035290),
))

# 4) Соборная мечеть --------------------------------------------------------------
RECORDS.append(rec(
    "saratov-cathedral-mosque",
    "Thánh đường Hồi giáo Saratov (Xa-bo-nai-a mê-trết)",
    "Саратовская соборная мечеть",
    "Saratov Cathedral Mosque",
    ["church"],
    51.537478, 46.038216,
    "Phố Tatarskaya 10/12 (góc phố Valovaya), thành phố Saratov, tỉnh Saratov, Nga",
    "Thánh đường Hồi giáo chính của Saratov, có nguồn gốc từ cuối thế kỷ 19 và được xây dựng lại khang trang với minaret cao. Đây là trung tâm tôn giáo, văn hoá của cộng đồng người Tatar và người Hồi giáo trong vùng Volga.",
    "Thánh đường Hồi giáo Saratov (Саратовская соборная мечеть) là trung tâm tinh thần của cộng đồng Hồi giáo - chủ yếu là người Tatar - đã sinh sống lâu đời tại vùng Volga đa sắc tộc. Nhà thờ Hồi giáo đầu tiên trên khu đất này xuất hiện từ cuối thế kỷ 19; công trình hiện nay được xây dựng lại và mở rộng vào những năm gần đây theo phong cách kiến trúc Hồi giáo cổ điển, với mái vòm và minaret (tháp gọi cầu nguyện) cao vươn lên giữa khu phố lịch sử. Đây không chỉ là nơi hành lễ mà còn là trung tâm giáo dục, sinh hoạt cộng đồng và bảo tồn văn hoá Tatar - Hồi giáo tại Saratov. Với du khách, thánh đường là dịp cảm nhận sự đa dạng tôn giáo hài hoà của thành phố, nơi nhà thờ Chính thống giáo, nhà thờ Hồi giáo và các cộng đồng tín ngưỡng khác cùng tồn tại. Vị trí ở góc phố Tatarskaya - Valovaya, gần trung tâm, khiến công trình dễ kết hợp trong hành trình khám phá di sản đa văn hoá của Saratov.",
    [
        "Thánh đường Hồi giáo chính của Saratov, gốc từ cuối thế kỷ 19.",
        "Kiến trúc Hồi giáo cổ điển với mái vòm và minaret cao.",
        "Trung tâm tôn giáo, văn hoá của cộng đồng Tatar - Hồi giáo vùng Volga.",
    ],
    p("Mở cửa hằng ngày, đông nhất vào giờ cầu nguyện và ngày thứ Sáu; nên kiểm tra trước.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 20–30 phút.",
      "Quanh năm; dịp lễ Eid không khí cộng đồng đặc biệt sôi động.",
      "Ăn mặc kín đáo, cởi giày khi vào sảnh lễ; nữ du khách nên trùm khăn. Tôn trọng giờ cầu nguyện."),
    [
        {"title": "Wikipedia (RU) — Саратовская соборная мечеть", "url": "https://ru.wikipedia.org/wiki/Саратовская_соборная_мечеть"},
        {"title": "2GIS — Саратовская соборная мечеть", "url": "https://2gis.ru/saratov/firm/6052240280303044"},
    ],
    ["church", "mosque", "islam", "tatar", "religion", "saratov"],
    maps_text("Саратовская соборная мечеть", "Саратов", "Saratov Cathedral Mosque", "Saratov", 51.537478, 46.038216),
))

# ============================ BẢO TÀNG (museum) ============================

# 5) Областной музей краеведения --------------------------------------------------
RECORDS.append(rec(
    "saratov-regional-lore-museum",
    "Bảo tàng Địa phương học tỉnh Saratov (Cra-ê-vét-tre-xki mu-dây)",
    "Саратовский областной музей краеведения",
    "Saratov Regional Museum of Local Lore",
    ["museum"],
    51.527573, 46.056017,
    "Phố Lermontova 34 (gần Quảng trường Bảo tàng), thành phố Saratov, tỉnh Saratov, Nga",
    "Bảo tàng địa phương học lâu đời nhất vùng Volga, thành lập năm 1886, đặt trong dinh thự cổ Ustinov. Bộ sưu tập trải rộng từ khảo cổ, tự nhiên, lịch sử vùng đất đến chiếc máy bay của phi công huyền thoại và di sản Gagarin.",
    "Bảo tàng Địa phương học tỉnh Saratov (Саратовский областной музей краеведения) là một trong những bảo tàng lâu đời và giàu bộ sưu tập nhất vùng Volga, được thành lập từ năm 1886. Bảo tàng đặt trụ sở trong dinh thự cổ của gia đình quý tộc Ustinov - một công trình kiến trúc thế kỷ 19 duyên dáng gần Quảng trường Bảo tàng. Hàng trăm nghìn hiện vật được trưng bày theo nhiều chủ đề: khảo cổ học và cổ sinh vật vùng Volga (kể cả hoá thạch), thiên nhiên và động thực vật địa phương, lịch sử khai phá và phát triển vùng đất Saratov, đời sống các dân tộc, cùng những trang sử thế kỷ 20. Một điểm nhấn đặc biệt gắn với niềm tự hào của vùng là các hiện vật liên quan đến hàng không - vũ trụ, trong đó có câu chuyện về Yuri Gagarin - người từng học ở Saratov và hạ cánh gần đây sau chuyến bay vũ trụ đầu tiên. Với cách trình bày phong phú, sinh động và toà nhà lịch sử đẹp, đây là điểm khởi đầu lý tưởng để hiểu bức tranh toàn cảnh về thiên nhiên, lịch sử và con người của cả tỉnh Saratov.",
    [
        "Bảo tàng địa phương học lâu đời nhất vùng Volga (thành lập 1886).",
        "Đặt trong dinh thự cổ Ustinov, kiến trúc quý tộc thế kỷ 19.",
        "Bộ sưu tập đa dạng: khảo cổ, tự nhiên, lịch sử vùng đất và di sản Gagarin.",
    ],
    p("Thường mở cửa thứ Ba–Chủ nhật khoảng 10:00–18:00, đóng cửa thứ Hai; nên kiểm tra trước.",
      "Vé vào cửa mức phải chăng; ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "Khoảng 1,5–2 giờ.",
      "Quanh năm; là điểm tham quan trong nhà lý tưởng cho ngày mưa hoặc mùa đông.",
      "Nên bắt đầu hành trình khám phá Saratov từ đây; gần Quảng trường Bảo tàng và Nhà thờ Ba Ngôi."),
    [
        {"title": "Wikipedia (RU) — Саратовский областной музей краеведения", "url": "https://ru.wikipedia.org/wiki/Саратовский_областной_музей_краеведения"},
        {"title": "Официальный сайт — comk.ru", "url": "https://comk.ru/"},
    ],
    ["museum", "history", "local-lore", "archaeology", "gagarin", "saratov"],
    maps_text("Саратовский областной музей краеведения", "Саратов", "Saratov Regional Museum of Local Lore", "Saratov", 51.527573, 46.056017),
    official_site="https://comk.ru/",
))

# 6) Музей-усадьба Чернышевского --------------------------------------------------
RECORDS.append(rec(
    "chernyshevsky-museum-estate",
    "Nhà - bảo tàng Chernyshevsky (Chéc-nư-sép-xki)",
    "Музей-усадьба Н. Г. Чернышевского",
    "N. G. Chernyshevsky Museum-Estate",
    ["museum"],
    51.524763, 46.040787,
    "Phố Chernyshevskogo 142, thành phố Saratov, tỉnh Saratov, Nga",
    "Ngôi nhà - bảo tàng tưởng niệm nhà văn, nhà tư tưởng cách mạng Nikolai Chernyshevsky (1828–1889), người con nổi tiếng của Saratov. Khu điền trang gỗ nơi ông sinh ra lưu giữ đồ đạc, bản thảo và không gian đời sống thế kỷ 19.",
    "Nhà - bảo tàng tưởng niệm Nikolai Gavrilovich Chernyshevsky là một trong những địa chỉ văn hoá quan trọng nhất Saratov, dành cho người con lừng danh của thành phố - nhà văn, nhà phê bình, triết gia và nhà tư tưởng cách mạng dân chủ (1828–1889), tác giả cuốn tiểu thuyết nổi tiếng 'Làm gì?'. Bảo tàng được lập trên chính khu điền trang nơi ông sinh ra và lớn lên, gồm ngôi nhà gỗ của gia đình cùng vài toà nhà phụ, gìn giữ nguyên vẹn không khí đời sống tỉnh lẻ Nga thế kỷ 19. Du khách được xem đồ nội thất nguyên bản, di vật cá nhân, thư từ, bản thảo và các tư liệu về cuộc đời, sự nghiệp cũng như những năm tháng lưu đày khổ sai của Chernyshevsky. Là một trong những bảo tàng văn học - tưởng niệm lâu đời của Nga (mở cửa từ đầu thế kỷ 20), nơi đây không chỉ tôn vinh một nhân vật có ảnh hưởng lớn tới tư tưởng Nga mà còn tái hiện sinh động nếp sống, kiến trúc gỗ và văn hoá đô thị Saratov xưa, mang lại trải nghiệm lắng đọng cho người yêu văn chương và lịch sử.",
    [
        "Nơi sinh của nhà tư tưởng, nhà văn cách mạng N. G. Chernyshevsky (tác giả 'Làm gì?').",
        "Điền trang gỗ thế kỷ 19 với đồ đạc, bản thảo, di vật nguyên bản.",
        "Một trong những bảo tàng văn học - tưởng niệm lâu đời của nước Nga.",
    ],
    p("Thường mở cửa thứ Ba–Chủ nhật khoảng 10:00–18:00, đóng cửa thứ Hai; nên kiểm tra trước.",
      "Vé vào cửa mức phải chăng; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; điểm tham quan trong nhà, đẹp cả khu vườn vào mùa ấm.",
      "Nên đi cùng thuyết minh để hiểu sâu về cuộc đời Chernyshevsky; kết hợp dạo trung tâm gần đó."),
    [
        {"title": "Wikipedia (RU) — Музей-усадьба Н. Г. Чернышевского", "url": "https://ru.wikipedia.org/wiki/Музей-усадьба_Н._Г._Чернышевского"},
        {"title": "Официальный сайт — ngc.sgu.ru", "url": "http://ngc.sgu.ru/"},
    ],
    ["museum", "literature", "memorial", "chernyshevsky", "history", "saratov"],
    maps_text("Музей-усадьба Чернышевского", "Саратов", "Chernyshevsky Museum-Estate", "Saratov", 51.524763, 46.040787),
    official_site="http://ngc.sgu.ru/",
))

# 7) Государственный музей К. А. Федина --------------------------------------------
RECORDS.append(rec(
    "fedin-literature-museum",
    "Bảo tàng Văn học Fedin (Phê-đin)",
    "Государственный музей К. А. Федина",
    "K. A. Fedin State Museum (literature)",
    ["museum"],
    51.526402, 46.045539,
    "Phố Chernyshevskogo 154, thành phố Saratov, tỉnh Saratov, Nga",
    "Bảo tàng văn học đặt trong toà nhà trường học cổ nhất còn lại của Saratov, dành cho nhà văn Konstantin Fedin. Ngày nay đây là một trung tâm văn học lớn, lưu giữ di sản của nhiều nhà văn Nga thế kỷ 20.",
    "Bảo tàng Nhà nước K. A. Fedin là một trong những bảo tàng văn học hàng đầu của Nga, tôn vinh nhà văn Konstantin Aleksandrovich Fedin (1892–1977) - người con của Saratov, một trong những cây bút Xô viết có ảnh hưởng. Bảo tàng toạ lạc trong một công trình quý: toà nhà trường học cổ nhất còn tồn tại của thành phố (trường trung học thế kỷ 18–19), gắn với thời niên thiếu của chính Fedin. Từ một bảo tàng tưởng niệm, nơi đây đã phát triển thành một trung tâm văn học rộng lớn, lưu giữ hàng chục nghìn hiện vật: bản thảo, thư từ, sách quý, ảnh và đồ dùng cá nhân không chỉ của Fedin mà của nhiều nhà văn Nga và thế giới thế kỷ 20 mà ông từng quen biết. Bảo tàng thường xuyên tổ chức triển lãm, hội thảo, sự kiện văn học và các chương trình giáo dục. Với những ai quan tâm văn chương Nga, lịch sử trí thức và kiến trúc trường học cổ, đây là điểm đến giàu chiều sâu, phản ánh truyền thống văn hoá lâu đời của Saratov.",
    [
        "Đặt trong toà nhà trường học CỔ NHẤT còn lại của Saratov.",
        "Tôn vinh nhà văn Konstantin Fedin - người con nổi tiếng của thành phố.",
        "Trung tâm văn học lớn, lưu giữ di sản nhiều nhà văn Nga thế kỷ 20.",
    ],
    p("Thường mở cửa thứ Ba–Chủ nhật khoảng 10:00–18:00, đóng cửa thứ Hai; nên kiểm tra trước.",
      "Vé vào cửa mức phải chăng; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; kiểm tra lịch triển lãm và sự kiện văn học trước khi đến.",
      "Kết hợp với Nhà - bảo tàng Chernyshevsky gần đó trên cùng khu phố trung tâm."),
    [
        {"title": "Wikipedia (RU) — Государственный музей К. А. Федина", "url": "https://ru.wikipedia.org/wiki/Государственный_музей_К._А._Федина"},
        {"title": "Официальный сайт — fedinmuseum.ru", "url": "http://fedinmuseum.ru/"},
    ],
    ["museum", "literature", "fedin", "history", "saratov"],
    maps_text("Государственный музей Федина", "Саратов", "K. A. Fedin State Museum", "Saratov", 51.526402, 46.045539),
    official_site="http://fedinmuseum.ru/",
))

# 8) Дом-музей Павла Кузнецова -----------------------------------------------------
RECORDS.append(rec(
    "pavel-kuznetsov-house-museum",
    "Nhà - bảo tàng danh hoạ Pavel Kuznetsov (Cút-nhê-txốp)",
    "Дом-музей Павла Кузнецова",
    "Pavel Kuznetsov House-Museum",
    ["museum"],
    51.533894, 46.048234,
    "Phố Oktyabrskaya 56, thành phố Saratov, tỉnh Saratov, Nga",
    "Ngôi nhà - bảo tàng nơi sinh của danh hoạ Pavel Kuznetsov (1878–1968), bậc thầy hội hoạ biểu tượng Nga đầu thế kỷ 20. Khu nhà gỗ với khu vườn nghệ thuật là một không gian sáng tạo yên bình giữa lòng Saratov.",
    "Nhà - bảo tàng Pavel Kuznetsov là một 'ốc đảo' nghệ thuật đặc biệt của Saratov, nằm trong chính ngôi nhà gỗ nơi danh hoạ Pavel Varfolomeevich Kuznetsov (1878–1968) chào đời và lớn lên. Kuznetsov là một trong những hoạ sĩ hàng đầu của trường phái biểu tượng (symbolism) và tiên phong Nga đầu thế kỷ 20, nổi tiếng với những bức tranh mơ màng, giàu chất thơ về thảo nguyên phương Đông và đời sống du mục. Bảo tàng (một chi nhánh của Bảo tàng Nghệ thuật Radishchev) tái hiện không gian gia đình, trưng bày tác phẩm, tư liệu về cuộc đời, sự nghiệp của ông cùng bối cảnh 'trường phái Saratov' trong mỹ thuật Nga. Điểm quyến rũ riêng của nơi đây là khu vườn - sân nhỏ được cải tạo thành không gian nghệ thuật đương đại, thường xuyên tổ chức triển lãm, workshop, hoà nhạc, festival và các sự kiện sáng tạo dành cho cộng đồng. Sự kết hợp giữa di sản của một bậc thầy cổ điển và tinh thần nghệ thuật sống động đương đại khiến Дом-музей Кузнецова trở thành điểm đến ấm cúng, truyền cảm hứng, khác biệt với các bảo tàng truyền thống.",
    [
        "Nơi sinh của danh hoạ biểu tượng Nga Pavel Kuznetsov (1878–1968).",
        "Chi nhánh Bảo tàng Radishchev, gắn với 'trường phái Saratov' trong mỹ thuật.",
        "Khu vườn - sân nghệ thuật tổ chức triển lãm, workshop, festival sáng tạo.",
    ],
    p("Thường mở cửa thứ Ba–Chủ nhật khoảng 10:00–18:00, đóng cửa thứ Hai; nên kiểm tra trước.",
      "Vé vào cửa mức phải chăng; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 1–1,5 giờ.",
      "Mùa ấm để tận hưởng khu vườn - sân nghệ thuật và sự kiện ngoài trời.",
      "Kiểm tra lịch triển lãm, workshop trước khi đến; không gian nhỏ, hợp đi thong thả."),
    [
        {"title": "Wikipedia (RU) — Дом-музей Павла Кузнецова", "url": "https://ru.wikipedia.org/wiki/Дом-музей_Павла_Кузнецова"},
        {"title": "Radmuseumart.ru — Дом-музей П. В. Кузнецова", "url": "https://radmuseumart.ru/"},
    ],
    ["museum", "art", "house-museum", "kuznetsov", "symbolism", "saratov"],
    maps_text("Дом-музей Павла Кузнецова", "Саратов", "Pavel Kuznetsov House-Museum", "Saratov", 51.533894, 46.048234),
))

# 9) Музей Петрова-Водкина (Хвалынск) ---------------------------------------------
RECORDS.append(rec(
    "petrov-vodkin-museum-khvalynsk",
    "Nhà - bảo tàng danh hoạ Petrov-Vodkin (Pê-trốp Vốt-kin)",
    "Художественно-мемориальный музей К. С. Петрова-Водкина",
    "K. S. Petrov-Vodkin Art-Memorial Museum",
    ["museum"],
    52.475089, 48.102930,
    "Phố Lenina 208, thành phố Khvalynsk, tỉnh Saratov, Nga",
    "Bảo tàng tưởng niệm nơi sinh của Kuzma Petrov-Vodkin (1878–1939), một trong những danh hoạ Nga vĩ đại nhất thế kỷ 20, ở thị trấn Khvalynsk bên sông Volga. Ngôi nhà gỗ do chính ông xây tặng mẹ nay lưu giữ di sản và không khí quê hương nhà hoạ sĩ.",
    "Bảo tàng nghệ thuật - tưởng niệm Kuzma Sergeevich Petrov-Vodkin nằm ở thị trấn nhỏ Khvalynsk bên bờ Volga, quê hương của một trong những danh hoạ Nga có ảnh hưởng nhất thế kỷ 20 - tác giả của những kiệt tác như 'Tắm ngựa đỏ'. Trung tâm bảo tàng là ngôi nhà gỗ mà chính Petrov-Vodkin đã cho xây để tặng người mẹ của mình, nay được gìn giữ cùng đồ đạc, di vật gia đình và không khí đời sống tỉnh lẻ Nga cuối thế kỷ 19 - đầu thế kỷ 20 đã nuôi dưỡng tài năng của ông. Bảo tàng trưng bày tranh, phác thảo, tư liệu về cuộc đời, sự nghiệp và triết lý hội hoạ độc đáo của Petrov-Vodkin (đặc biệt là lý thuyết 'phối cảnh cầu' và bảng màu ba sắc đặc trưng). Chuyến thăm không chỉ đưa du khách đến gần một tên tuổi lớn của mỹ thuật Nga mà còn là cái cớ tuyệt vời để khám phá Khvalynsk - thị trấn cổ kính giữa những đồi phấn trắng, vườn táo và cảnh quan tuyệt đẹp của vùng Volga thượng, nơi cũng có Vườn quốc gia Khvalynsky nổi tiếng.",
    [
        "Nơi sinh danh hoạ Kuzma Petrov-Vodkin - tác giả 'Tắm ngựa đỏ'.",
        "Ngôi nhà gỗ do chính hoạ sĩ xây tặng mẹ, lưu giữ di vật gia đình.",
        "Điểm đến kết hợp khám phá thị trấn cổ Khvalynsk bên sông Volga.",
    ],
    p("Thường mở cửa thứ Ba–Chủ nhật khoảng 9:00–17:00, đóng cửa thứ Hai; nên kiểm tra trước.",
      "Vé vào cửa mức phải chăng; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 1–1,5 giờ.",
      "Cuối xuân đến đầu thu; kết hợp mùa hoa táo hoặc mùa lá vàng ở Khvalynsk.",
      "Khvalynsk cách Saratov ~200 km; nên đi ô tô, kết hợp Vườn quốc gia Khvalynsky và cảnh quan đồi phấn."),
    [
        {"title": "Wikipedia (RU) — Петров-Водкин, Кузьма Сергеевич", "url": "https://ru.wikipedia.org/wiki/Петров-Водкин,_Кузьма_Сергеевич"},
        {"title": "Culture.ru — Дом-музей К. С. Петрова-Водкина", "url": "https://www.culture.ru/institutes/"},
    ],
    ["museum", "art", "house-museum", "petrov-vodkin", "khvalynsk", "volga"],
    maps_text("Дом-музей Петрова-Водкина", "Хвалынск", "Petrov-Vodkin House-Museum", "Khvalynsk", 52.475089, 48.102930),
))

# 10) Энгельсский краеведческий музей ---------------------------------------------
RECORDS.append(rec(
    "engels-local-lore-museum",
    "Bảo tàng Địa phương học Engels (Ên-ghen)",
    "Энгельсский краеведческий музей",
    "Engels Museum of Local Lore",
    ["museum"],
    51.502877, 46.120173,
    "Phố Gorkogo 4, thành phố Engels, tỉnh Saratov, Nga",
    "Bảo tàng địa phương học của thành phố Engels bên kia sông Volga, lưu giữ lịch sử vùng đất từng là thủ phủ Cộng hoà Đức Volga. Bộ sưu tập phong phú về khảo cổ, dân tộc học, nghề muối và di sản người Đức vùng Volga.",
    "Bảo tàng Địa phương học Engels (Энгельсский краеведческий музей) là bảo tàng chính của thành phố Engels - đô thị nằm ngay đối diện Saratov qua sông Volga và nối với nhau bằng cây cầu Saratov nổi tiếng. Thành lập từ những năm 1920, bảo tàng gìn giữ và kể lại lịch sử độc đáo của vùng đất này: từ thời còn là khu định cư Pokrovskaya Sloboda gắn với nghề vận chuyển và buôn bán muối, đến giai đoạn Engels từng là thủ phủ của Cộng hoà Xã hội chủ nghĩa Xô viết tự trị Người Đức vùng Volga (ASSR Người Đức Volga) trong những năm 1920–1941. Bộ sưu tập trải rộng qua khảo cổ học, cổ sinh vật, dân tộc học, đời sống và văn hoá của người Đức Volga cùng nhiều dân tộc khác, nghệ thuật và lịch sử thế kỷ 20. Bảo tàng còn có bộ sưu tập mỹ thuật đáng chú ý. Đối với du khách, đây là nơi để hiểu một chương lịch sử ít được biết đến nhưng hấp dẫn của vùng Volga - câu chuyện di dân, đa văn hoá và những biến động thời cuộc - đồng thời là điểm dừng chân ý nghĩa khi khám phá thành phố 'sinh đôi' của Saratov.",
    [
        "Bảo tàng chính của Engels - thành phố 'sinh đôi' của Saratov qua sông Volga.",
        "Kể lịch sử vùng từng là thủ phủ Cộng hoà Xô viết Người Đức Volga (1920–1941).",
        "Bộ sưu tập khảo cổ, dân tộc học, nghề muối và di sản đa văn hoá.",
    ],
    p("Thường mở cửa thứ Ba–Chủ nhật khoảng 10:00–18:00, đóng cửa thứ Hai; nên kiểm tra trước.",
      "Vé vào cửa mức phải chăng; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; điểm tham quan trong nhà.",
      "Kết hợp qua cầu Saratov thăm Engels, tượng 'Bò chở muối' và các đài tưởng niệm gần đó."),
    [
        {"title": "Wikipedia (RU) — Энгельсский краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Энгельсский_краеведческий_музей"},
        {"title": "Culture.ru — Энгельсский краеведческий музей", "url": "https://www.culture.ru/institutes/"},
    ],
    ["museum", "history", "local-lore", "volga-germans", "engels", "saratov"],
    maps_text("Энгельсский краеведческий музей", "Энгельс", "Engels Museum of Local Lore", "Engels", 51.502877, 46.120173),
))

# 11) Музей-усадьба Борисова-Мусатова ---------------------------------------------
RECORDS.append(rec(
    "borisov-musatov-museum",
    "Nhà - bảo tàng danh hoạ Borisov-Musatov (Bô-ri-xốp Mu-xa-tốp)",
    "Музей-усадьба В. Э. Борисова-Мусатова",
    "V. E. Borisov-Musatov Museum-Estate",
    ["museum"],
    51.524224, 46.019384,
    "Phố Volskaya 33, thành phố Saratov, tỉnh Saratov, Nga",
    "Ngôi nhà - bảo tàng nơi sinh của Viktor Borisov-Musatov (1870–1905), danh hoạ biểu tượng Nga với những bức tranh mơ màng, hoài niệm. Khu nhà gỗ nhỏ với vườn cây là một góc lặng đầy chất thơ giữa lòng Saratov.",
    "Nhà - bảo tàng Viktor Elpidiforovich Borisov-Musatov là một địa chỉ nghệ thuật tinh tế của Saratov, nằm trong khu nhà nơi danh hoạ chào đời và trải qua tuổi thơ. Borisov-Musatov (1870–1905) là một trong những gương mặt tiêu biểu của trường phái biểu tượng Nga, nổi tiếng với những bức tranh trữ tình, phảng phất nỗi hoài niệm về những khu điền trang quý tộc, các thiếu nữ trong y phục xưa và không khí mơ màng nửa thực nửa mộng. Dù cuộc đời ngắn ngủi, ông để lại ảnh hưởng sâu sắc lên mỹ thuật Nga đầu thế kỷ 20 và được xem là một trong những trụ cột của 'trường phái Saratov'. Bảo tàng (chi nhánh của Bảo tàng Nghệ thuật Radishchev) tái hiện không gian sống của gia đình, trưng bày tư liệu, bản sao tác phẩm và kể câu chuyện về hành trình sáng tạo của hoạ sĩ. Khuôn viên nhà gỗ khiêm nhường cùng khoảng vườn nhỏ tạo nên một góc yên tĩnh, hoài cổ - nơi du khách yêu hội hoạ có thể lặng lẽ cảm nhận cái đẹp trầm buồn đặc trưng trong nghệ thuật của Borisov-Musatov.",
    [
        "Nơi sinh của danh hoạ biểu tượng Nga Viktor Borisov-Musatov (1870–1905).",
        "Chi nhánh Bảo tàng Radishchev, gắn với 'trường phái Saratov' trong mỹ thuật.",
        "Khu nhà gỗ nhỏ với vườn cây - một góc lặng đầy chất thơ trong thành phố.",
    ],
    p("Thường mở cửa thứ Ba–Chủ nhật khoảng 10:00–18:00, đóng cửa thứ Hai; nên kiểm tra trước.",
      "Vé vào cửa mức phải chăng; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 45 phút–1 giờ.",
      "Mùa ấm để tận hưởng khu vườn nhỏ; quanh năm cho không gian trong nhà.",
      "Không gian nhỏ, hợp đi thong thả; kết hợp Bảo tàng Radishchev và trung tâm gần đó."),
    [
        {"title": "Wikipedia (RU) — Борисов-Мусатов, Виктор Эльпидифорович", "url": "https://ru.wikipedia.org/wiki/Борисов-Мусатов,_Виктор_Эльпидифорович"},
        {"title": "Radmuseumart.ru — Музей-усадьба В. Э. Борисова-Мусатова", "url": "https://radmuseumart.ru/"},
    ],
    ["museum", "art", "house-museum", "borisov-musatov", "symbolism", "saratov"],
    maps_text("Музей-усадьба Борисова-Мусатова", "Саратов", "Borisov-Musatov Museum-Estate", "Saratov", 51.524224, 46.019384),
))

# ============================ NHÀ HÁT (theatre) ============================

# 12) Театр оперы и балета --------------------------------------------------------
RECORDS.append(rec(
    "saratov-opera-ballet-theatre",
    "Nhà hát Opera và Ballet Saratov (Ô-pê-ra i ba-lết)",
    "Саратовский академический театр оперы и балета",
    "Saratov Academic Opera and Ballet Theatre",
    ["theatre"],
    51.532955, 46.031990,
    "Quảng trường Nhà hát (Театральная площадь) 1, thành phố Saratov, tỉnh Saratov, Nga",
    "Nhà hát Opera và Ballet của Saratov, một trong những đoàn nhạc kịch lâu đời và uy tín của tỉnh lẻ Nga, có gốc từ thế kỷ 19. Toà nhà cổ điển trên Quảng trường Nhà hát là nơi tổ chức liên hoan âm nhạc danh tiếng mang tên Sobinov.",
    "Nhà hát Opera và Ballet Hàn lâm Saratov là trung tâm nghệ thuật sân khấu hàng đầu của thành phố, với lịch sử bắt nguồn từ thế kỷ 19 - thời kỳ Saratov đã là một đô thị thương mại - văn hoá sầm uất bên sông Volga. Toà nhà nhà hát bề thế theo phong cách cổ điển toạ lạc ngay trên Quảng trường Nhà hát (Театральная площадь), quảng trường trung tâm và lớn nhất thành phố. Đoàn nghệ thuật dàn dựng phong phú các vở opera kinh điển Nga và thế giới, ballet, hoà nhạc giao hưởng, quy tụ nhiều nghệ sĩ, ca sĩ tài năng. Nhà hát đặc biệt nổi tiếng với Liên hoan Âm nhạc Sobinov (Собиновский музыкальный фестиваль) - một trong những festival opera lâu đời và uy tín của Nga, mang tên danh ca Leonid Sobinov gắn bó với Saratov. Với kiến trúc trang nghiêm, sân khấu chất lượng cao và truyền thống biểu diễn lâu đời, đây là điểm đến không thể bỏ qua cho những ai yêu nhạc cổ điển, opera và ballet khi ghé thăm Saratov, đồng thời là niềm tự hào văn hoá của cả vùng Volga.",
    [
        "Một trong những nhà hát opera - ballet lâu đời, uy tín của tỉnh lẻ Nga (gốc thế kỷ 19).",
        "Toà nhà cổ điển bề thế trên Quảng trường Nhà hát - quảng trường trung tâm Saratov.",
        "Nơi tổ chức Liên hoan Âm nhạc Sobinov danh tiếng.",
    ],
    p("Biểu diễn chủ yếu buổi tối; phòng vé mở ban ngày. Xem lịch diễn và mua vé trên trang chính thức.",
      "Giá vé tuỳ chương trình và vị trí ghế, thường ở mức phải chăng.",
      "Buổi diễn khoảng 2–3 giờ.",
      "Mùa diễn từ thu đến xuân; dịp Liên hoan Sobinov (thường mùa xuân) đặc biệt hấp dẫn.",
      "Đặt vé trước cho các buổi nổi tiếng; đến sớm để ngắm nội thất và Quảng trường Nhà hát."),
    [
        {"title": "Wikipedia (RU) — Саратовский театр оперы и балета", "url": "https://ru.wikipedia.org/wiki/Саратовский_театр_оперы_и_балета"},
        {"title": "Официальный сайт — saratovopera.ru", "url": "https://saratovopera.ru/"},
    ],
    ["theatre", "opera", "ballet", "classical-music", "festival", "saratov"],
    maps_text("Саратовский театр оперы и балета", "Саратов", "Saratov Opera and Ballet Theatre", "Saratov", 51.532955, 46.031990),
    official_site="https://saratovopera.ru/",
))

# 13) Театр драмы им. Слонова -----------------------------------------------------
RECORDS.append(rec(
    "saratov-drama-theatre-slonov",
    "Nhà hát Kịch Saratov mang tên Slonov (Xlô-nốp)",
    "Саратовский академический театр драмы имени И. А. Слонова",
    "Saratov Academic Drama Theatre named after I. A. Slonov",
    ["theatre"],
    51.534129, 46.001656,
    "Phố Rabochaya 116, thành phố Saratov, tỉnh Saratov, Nga",
    "Nhà hát Kịch Hàn lâm Saratov là một trong những nhà hát kịch tỉnh lẻ lâu đời nhất nước Nga, có truyền thống từ cuối thế kỷ 18. Mang tên nghệ sĩ Ivan Slonov, đây là trung tâm nghệ thuật kịch nói danh giá của vùng Volga.",
    "Nhà hát Kịch Hàn lâm Saratov mang tên I. A. Slonov là một trong những nhà hát kịch nói lâu đời và có uy tín bậc nhất của nước Nga ngoài hai thủ đô, với truyền thống sân khấu chuyên nghiệp được cho là bắt nguồn từ cuối thế kỷ 18 - thuộc hàng những nhà hát tỉnh lẻ ra đời sớm nhất. Nhà hát mang tên Ivan Artemevich Slonov, một nghệ sĩ và nhà sư phạm sân khấu có ảnh hưởng, gắn bó lâu dài với Saratov. Trải qua hơn hai thế kỷ, đoàn kịch dàn dựng phong phú các tác phẩm kinh điển Nga (Ostrovsky, Chekhov, Gogol) và thế giới, cùng nhiều vở đương đại, và từng là bệ phóng cho nhiều tên tuổi lớn của sân khấu, điện ảnh Nga. Với danh hiệu 'hàn lâm' (академический) cao quý, đây là địa chỉ dành cho những ai muốn thưởng thức nghệ thuật kịch nói Nga đích thực trong một không gian giàu truyền thống. Nhà hát cũng thường xuyên tham gia và tổ chức các liên hoan sân khấu, góp phần khẳng định Saratov là một trung tâm văn hoá - sân khấu quan trọng của vùng Volga.",
    [
        "Một trong những nhà hát kịch tỉnh lẻ LÂU ĐỜI NHẤT nước Nga (gốc cuối thế kỷ 18).",
        "Mang tên nghệ sĩ - nhà sư phạm sân khấu Ivan Slonov.",
        "Sân khấu 'hàn lâm' dàn dựng kinh điển Nga - thế giới và tác phẩm đương đại.",
    ],
    p("Biểu diễn chủ yếu buổi tối; phòng vé mở ban ngày. Xem lịch diễn trên trang chính thức.",
      "Giá vé tuỳ chương trình, thường ở mức phải chăng.",
      "Buổi diễn khoảng 2–3 giờ.",
      "Mùa diễn từ thu đến xuân.",
      "Vở diễn chủ yếu bằng tiếng Nga; đặt vé trước cho các buổi nổi tiếng."),
    [
        {"title": "Wikipedia (RU) — Саратовский театр драмы", "url": "https://ru.wikipedia.org/wiki/Саратовский_театр_драмы"},
        {"title": "Официальный сайт — saratovdrama.com", "url": "https://saratovdrama.com/"},
    ],
    ["theatre", "drama", "academic", "historic", "saratov"],
    maps_text("Саратовский театр драмы имени Слонова", "Саратов", "Saratov Drama Theatre", "Saratov", 51.534129, 46.001656),
    official_site="https://saratovdrama.com/",
))

# 14) ТЮЗ им. Киселёва ------------------------------------------------------------
RECORDS.append(rec(
    "saratov-youth-theatre-kiselyov",
    "Nhà hát Thiếu nhi Saratov mang tên Kiselyov (Chiu-dơ)",
    "Саратовский театр юного зрителя имени Ю. П. Киселёва",
    "Saratov Youth Theatre named after Yu. P. Kiselyov",
    ["theatre"],
    51.534635, 46.024396,
    "Quảng trường Kiselyova 1 (phố Bolshaya Kazachya 40), thành phố Saratov, tỉnh Saratov, Nga",
    "Nhà hát Thiếu nhi (TYUZ) của Saratov được xem là nhà hát chuyên nghiệp đầu tiên dành cho khán giả trẻ trên thế giới, thành lập năm 1918. Toà nhà mới hiện đại là sân khấu hàng đầu cho trẻ em và thanh thiếu niên của cả nước Nga.",
    "Nhà hát Thiếu nhi Saratov mang tên Yuri Kiselyov (Саратовский ТЮЗ) là một địa chỉ có ý nghĩa lịch sử đặc biệt: được thành lập năm 1918, nơi đây thường được ghi nhận là một trong những - nếu không phải là - nhà hát chuyên nghiệp đầu tiên trên thế giới dành riêng cho khán giả nhỏ tuổi. Nhà hát mang tên Yuri Petrovich Kiselyov, đạo diễn tài năng đã lãnh đạo và đưa đoàn lên tầm vóc quốc gia trong nhiều thập niên. TYUZ Saratov nổi tiếng với những vở diễn chất lượng cao dựa trên truyện cổ tích, văn học thiếu nhi và cả các tác phẩm dành cho thanh thiếu niên, người lớn, luôn chú trọng giá trị giáo dục và nghệ thuật. Sau nhiều năm, nhà hát được xây thêm một toà nhà mới khang trang, hiện đại với trang thiết bị sân khấu tiên tiến, trở thành niềm tự hào của thành phố. Đây là điểm đến lý tưởng cho các gia đình có trẻ nhỏ khi thăm Saratov, đồng thời là biểu tượng cho truyền thống lâu đời và sáng tạo của nghệ thuật sân khấu dành cho tuổi thơ ở nước Nga.",
    [
        "Được xem là một trong những nhà hát chuyên nghiệp ĐẦU TIÊN cho thiếu nhi trên thế giới (1918).",
        "Mang tên đạo diễn Yuri Kiselyov, sân khấu thiếu nhi hàng đầu nước Nga.",
        "Toà nhà mới hiện đại với trang thiết bị sân khấu tiên tiến.",
    ],
    p("Biểu diễn buổi chiều/tối, đông vào cuối tuần; phòng vé mở ban ngày. Xem lịch trên trang chính thức.",
      "Giá vé ở mức phải chăng; nhiều suất dành cho gia đình và trẻ em.",
      "Buổi diễn khoảng 1–2 giờ.",
      "Mùa diễn từ thu đến xuân; cuối tuần nhiều suất cho thiếu nhi.",
      "Lý tưởng cho gia đình có trẻ nhỏ; vở diễn bằng tiếng Nga, đặt vé trước cho suất cuối tuần."),
    [
        {"title": "Wikipedia (RU) — Саратовский ТЮЗ", "url": "https://ru.wikipedia.org/wiki/Саратовский_ТЮЗ"},
        {"title": "Официальный сайт — tuzkiselev.ru", "url": "https://tuzkiselev.ru/"},
    ],
    ["theatre", "youth-theatre", "children", "family", "historic", "saratov"],
    maps_text("Саратовский ТЮЗ имени Киселёва", "Саратов", "Saratov Youth Theatre", "Saratov", 51.534635, 46.024396),
    official_site="https://tuzkiselev.ru/",
))

# ============================ QUẢNG TRƯỜNG / PHỐ (square_street) ============================

# 15) Проспект Кирова -------------------------------------------------------------
RECORDS.append(rec(
    "kirov-avenue-saratov",
    "Đại lộ đi bộ Kirov - 'Arbat của Saratov' (Prô-xpếch Ki-rốp)",
    "Проспект Кирова (проспект имени Петра Столыпина)",
    "Kirov Avenue (Prospekt Kirova)",
    ["square_street"],
    51.530224, 46.032269,
    "Đại lộ đi bộ trung tâm, từ phố Radishcheva đến phố Chapaeva, thành phố Saratov, tỉnh Saratov, Nga",
    "Đại lộ Kirov là phố đi bộ trung tâm sầm uất nhất Saratov, được người dân gọi thân mật là 'Arbat của Saratov'. Con phố lát đá với những toà nhà cổ, quán cà phê, cửa hàng và các tác phẩm điêu khắc đường phố là nơi dạo chơi được yêu thích nhất thành phố.",
    "Đại lộ Kirov (Проспект Кирова) là trục đi bộ chính và sinh động bậc nhất của Saratov, thường được so sánh và gọi trìu mến là 'Arbat của Saratov' - theo tên con phố đi bộ nổi tiếng ở Moskva. Trải dài qua khu trung tâm lịch sử, con phố lát đá dành riêng cho người đi bộ được bao quanh bởi những toà nhà kiến trúc cuối thế kỷ 19 - đầu thế kỷ 20 duyên dáng, nay là các cửa hàng, nhà hàng, quán cà phê, hiệu sách và rạp chiếu bóng. Dọc đại lộ có nhiều đài phun nước, tiểu cảnh, ghế nghỉ và các tác phẩm điêu khắc đường phố thú vị - trong đó nổi tiếng nhất là tượng đài dành cho bài hát 'Огней так много золотых' (chủ đề về những chàng trai độc thân). Đây là nơi người dân Saratov và du khách tản bộ, hẹn hò, mua sắm, thưởng thức nghệ sĩ đường phố và cảm nhận nhịp sống đô thị. (Năm 2023 phố được đổi tên chính thức thành 'Đại lộ Pyotr Stolypin', song tên Kirov vẫn quen thuộc với nhiều người.) Là 'trái tim đi bộ' của thành phố, đại lộ này là điểm dừng chân không thể thiếu để cảm nhận tinh thần Saratov.",
    [
        "Phố đi bộ trung tâm sầm uất nhất, được gọi là 'Arbat của Saratov'.",
        "Kiến trúc cổ cuối thế kỷ 19 - đầu 20, quán cà phê, cửa hàng và điêu khắc đường phố.",
        "Có tượng đài bài hát 'Огней так много золотых' và nhiều tiểu cảnh (đã đổi tên thành đại lộ Stolypin, 2023).",
    ],
    p("Không gian công cộng ngoài trời, dạo chơi tự do suốt ngày đêm.",
      "Miễn phí (mua sắm, ăn uống tính riêng).",
      "Khoảng 1–1,5 giờ.",
      "Chiều tối mùa hè khi phố lên đèn và đông vui; cuối tuần nhộn nhịp nhất.",
      "Kết hợp thăm nhà thờ 'Утоли моя печали', Bảo tàng Radishchev và bờ kè gần đó; nhiều chỗ ăn uống dọc phố."),
    [
        {"title": "Wikipedia (RU) — Проспект Кирова (Саратов)", "url": "https://ru.wikipedia.org/wiki/Проспект_Кирова_(Саратов)"},
        {"title": "Wikipedia (RU) — Саратов", "url": "https://ru.wikipedia.org/wiki/Саратов"},
    ],
    ["square_street", "pedestrian", "arbat", "shopping", "walking", "saratov"],
    maps_text("Проспект Кирова", "Саратов", "Kirov Avenue Prospekt Kirova", "Saratov", 51.530224, 46.032269),
))

# 16) Театральная площадь ---------------------------------------------------------
RECORDS.append(rec(
    "theatre-square-saratov",
    "Quảng trường Nhà hát (Chê-a-tran-nai-a plô-shad)",
    "Театральная площадь",
    "Theatre Square",
    ["square_street"],
    51.532946, 46.034033,
    "Trung tâm thành phố Saratov (giữa các phố Kirova, Moskovskaya, Radishcheva), tỉnh Saratov, Nga",
    "Quảng trường Nhà hát là quảng trường trung tâm và lớn nhất Saratov, được bao quanh bởi Nhà hát Opera và Ballet, Bảo tàng Radishchev, đại học và các công trình quan trọng. Đây là nơi diễn ra sự kiện, lễ hội và chợ phiên lớn của thành phố.",
    "Quảng trường Nhà hát (Театральная площадь) là quảng trường trung tâm, rộng lớn và quan trọng nhất của Saratov - trái tim hành chính và văn hoá của thành phố. Xung quanh quảng trường tập trung nhiều công trình tiêu biểu: Nhà hát Opera và Ballet Hàn lâm, Bảo tàng Nghệ thuật Radishchev nổi tiếng, các toà nhà của Đại học Kinh tế và những kiến trúc lịch sử khác, tạo nên một quần thể đô thị bề thế. Trong lịch sử, khu vực này từng là quảng trường chợ (Хлебная/Театральная), và đến nay vẫn giữ vai trò không gian công cộng trung tâm - nơi tổ chức các sự kiện lớn: mít tinh, hoà nhạc ngoài trời, hội chợ, lễ hội thành phố, chợ Giáng sinh và các buổi lễ mừng ngày lễ quốc gia. Ở giữa quảng trường có tượng đài và không gian mở rộng rãi để người dân tụ họp, dạo chơi. Với vị trí kết nối phố đi bộ Kirov và nhiều điểm tham quan, Quảng trường Nhà hát là điểm định hướng tự nhiên cho du khách và là nơi cảm nhận rõ quy mô, sức sống của một trong những thành phố lớn bên sông Volga.",
    [
        "Quảng trường trung tâm và LỚN NHẤT Saratov - trái tim của thành phố.",
        "Bao quanh bởi Nhà hát Opera - Ballet, Bảo tàng Radishchev và các công trình lịch sử.",
        "Nơi tổ chức hoà nhạc, hội chợ, lễ hội và chợ Giáng sinh của thành phố.",
    ],
    p("Không gian công cộng ngoài trời, dạo chơi tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 30–45 phút.",
      "Quanh năm; dịp lễ hội thành phố và chợ Giáng sinh mùa đông đặc biệt náo nhiệt.",
      "Kết hợp thăm Nhà hát Opera, Bảo tàng Radishchev và phố đi bộ Kirov liền kề; kiểm tra lịch sự kiện."),
    [
        {"title": "Wikipedia (RU) — Театральная площадь (Саратов)", "url": "https://ru.wikipedia.org/wiki/Театральная_площадь_(Саратов)"},
        {"title": "Wikipedia (RU) — Саратов", "url": "https://ru.wikipedia.org/wiki/Саратов"},
    ],
    ["square_street", "square", "city-center", "events", "walking", "saratov"],
    maps_text("Театральная площадь", "Саратов", "Theatre Square", "Saratov", 51.532946, 46.034033),
))

# ============================ CÔNG VIÊN / THIÊN NHIÊN (park_garden) ============================

# 17) Парк «Липки» ----------------------------------------------------------------
RECORDS.append(rec(
    "lipki-park-saratov",
    "Vườn 'Lipki' (Li-pki)",
    "Городской парк «Липки»",
    "Lipki City Garden",
    ["park_garden"],
    51.528241, 46.037141,
    "Trung tâm thành phố Saratov (gần Nhà hát Opera, phố Volzhskaya - Radishcheva), tỉnh Saratov, Nga",
    "'Lipki' là công viên - vườn dạo lâu đời và duyên dáng nhất Saratov, được lập từ năm 1876 với những hàng cây đoạn (lipa) cổ thụ. Hàng rào gang uốn nghệ thuật, đài phun nước và bóng cây rợp mát khiến đây thành ốc đảo yên bình ngay trung tâm thành phố.",
    "Vườn 'Lipki' (парк «Липки») là công viên - vườn dạo cổ kính và được yêu mến bậc nhất của Saratov, nằm ngay trung tâm lịch sử, sát Nhà hát Opera và các con phố chính. Vườn được lập vào năm 1876 và lấy tên từ những cây đoạn (lipa - đoạn/bồ đề) được trồng khắp khuôn viên, nay đã thành cổ thụ toả bóng mát rợp các lối đi. Nét quyến rũ đặc trưng của 'Lipki' là hàng rào gang uốn theo phong cách Art Nouveau (modern) tinh xảo được chế tác đầu thế kỷ 20 - một tác phẩm nghệ thuật kim loại được xem là biểu tượng của vườn. Bên trong là những lối đi rợp bóng, bồn hoa, đài phun nước, ghế nghỉ, khu vui chơi trẻ em và các tác phẩm điêu khắc nhỏ. Qua gần một thế kỷ rưỡi, 'Lipki' vẫn là nơi người dân Saratov đủ mọi thế hệ tìm đến để dạo bộ, hóng mát, đọc sách và thư giãn giữa thiên nhiên ngay trong lòng phố. Với du khách, đây là một góc xanh lãng mạn, giàu chất hoài cổ, lý tưởng để nghỉ chân giữa hành trình khám phá trung tâm Saratov.",
    [
        "Công viên - vườn dạo LÂU ĐỜI NHẤT Saratov (lập năm 1876) với cây đoạn cổ thụ.",
        "Hàng rào gang uốn nghệ thuật phong cách Art Nouveau - biểu tượng của vườn.",
        "Ốc đảo xanh yên bình ngay trung tâm, cạnh Nhà hát Opera và phố chính.",
    ],
    p("Không gian công cộng ngoài trời, mở cửa tự do (ban ngày an toàn và dễ chịu nhất).",
      "Miễn phí.",
      "Khoảng 45 phút–1 giờ.",
      "Cuối xuân đến đầu thu khi cây xanh mát; mùa hè tránh nắng dưới bóng cổ thụ.",
      "Kết hợp thăm Nhà hát Opera, Quảng trường Nhà hát và phố Kirov liền kề; hợp cho gia đình có trẻ nhỏ."),
    [
        {"title": "Wikipedia (RU) — Липки (парк, Саратов)", "url": "https://ru.wikipedia.org/wiki/Липки_(парк)"},
        {"title": "Wikipedia (RU) — Саратов", "url": "https://ru.wikipedia.org/wiki/Саратов"},
    ],
    ["park_garden", "garden", "historic", "art-nouveau", "walking", "saratov"],
    maps_text("Городской парк Липки", "Саратов", "Lipki City Garden", "Saratov", 51.528241, 46.037141),
))

# 18) Городской парк им. Горького -------------------------------------------------
RECORDS.append(rec(
    "gorky-city-park-saratov",
    "Công viên Văn hoá - Nghỉ ngơi mang tên Gorky (Pác Goóc-ki)",
    "Городской парк культуры и отдыха имени М. Горького",
    "Gorky Central Park of Culture and Leisure",
    ["park_garden"],
    51.519207, 45.998754,
    "Ngõ 1-y Vakurovsky, khu Oktyabrsky, thành phố Saratov, tỉnh Saratov, Nga",
    "Công viên văn hoá - nghỉ ngơi lớn của Saratov, có gốc từ khu vườn điền trang quý tộc thế kỷ 19 với những hồ nước và cây cổ thụ. Ngày nay là khu vui chơi giải trí với trò chơi cảm giác mạnh, mặt hồ và không gian xanh cho gia đình.",
    "Công viên Văn hoá và Nghỉ ngơi mang tên Maxim Gorky là một trong những công viên giải trí lớn và được yêu thích của Saratov. Khu đất này vốn có nguồn gốc từ một điền trang quý tộc (vườn Vakurov) thế kỷ 19, với hệ thống hồ nước, kênh đào và những hàng cây cổ thụ được quy hoạch từ xưa, nay vẫn tạo nên bộ khung cảnh quan đặc trưng của công viên. Từ thời Xô viết, nơi đây được cải tạo thành công viên văn hoá - nghỉ ngơi kiểu 'ЦПКиО' phục vụ đông đảo người dân. Công viên kết hợp giữa không gian xanh yên tĩnh - những lối đi rợp bóng, mặt hồ để chèo thuyền, đài phun nước - với khu vui chơi sôi động gồm vòng đu quay, tàu lượn và nhiều trò chơi cảm giác mạnh cho mọi lứa tuổi. Vào mùa hè, đây là điểm hẹn quen thuộc của các gia đình, giới trẻ và trẻ em; mùa đông một phần công viên phục vụ trượt băng, trượt tuyết. Với sự pha trộn giữa di sản cảnh quan lịch sử và các hoạt động giải trí hiện đại, công viên Gorky là lựa chọn lý tưởng cho một buổi thư giãn, vui chơi năng động ở Saratov.",
    [
        "Công viên giải trí lớn có gốc từ điền trang quý tộc thế kỷ 19 với hồ nước, cây cổ thụ.",
        "Khu trò chơi cảm giác mạnh, vòng đu quay và tàu lượn cho mọi lứa tuổi.",
        "Mặt hồ chèo thuyền mùa hè, trượt băng mùa đông - điểm hẹn của gia đình.",
    ],
    p("Không gian mở, dạo chơi tự do; các trò chơi theo giờ (thường ban ngày đến tối, mùa ấm).",
      "Vào công viên miễn phí; các trò chơi, thuê thuyền tính phí riêng.",
      "Khoảng 1,5–2,5 giờ.",
      "Mùa hè cho trò chơi và chèo thuyền; mùa đông cho trượt băng.",
      "Hợp cho gia đình có trẻ nhỏ; kiểm tra lịch hoạt động các trò chơi theo mùa."),
    [
        {"title": "Wikipedia (RU) — Парк Горького (Саратов)", "url": "https://ru.wikipedia.org/wiki/Парк_Горького_(Саратов)"},
        {"title": "Официальный сайт — parkgorkogo64.ru", "url": "https://parkgorkogo64.ru/"},
    ],
    ["park_garden", "amusement", "recreation", "family", "lake", "saratov"],
    maps_text("Городской парк культуры и отдыха имени Горького", "Саратов", "Gorky Central Park", "Saratov", 51.519207, 45.998754),
))

# 19) Утёс Степана Разина ---------------------------------------------------------
RECORDS.append(rec(
    "stepan-razin-cliff",
    "Vách đá Stepan Razin (U-chi-ốt Xtê-pan Ra-din)",
    "Утёс Степана Разина",
    "Stepan Razin's Cliff",
    ["park_garden"],
    50.615500, 45.652600,
    "Bờ phải sông Volga, gần làng Belogorskoe, huyện Krasnoarmeysky, tỉnh Saratov, Nga (phía nam Saratov)",
    "Vách đá Stepan Razin là một mỏm núi hiểm trở nhô ra sông Volga ở phía nam tỉnh Saratov, gắn với truyền thuyết về thủ lĩnh nông dân khởi nghĩa Stepan Razin. Đây là một di tích thiên nhiên - lịch sử và điểm ngắm cảnh Volga hùng vĩ nổi tiếng.",
    "Vách đá Stepan Razin (Утёс Степана Разина) là một trong những thắng cảnh thiên nhiên - lịch sử độc đáo nhất tỉnh Saratov, nằm ở bờ phải sông Volga thuộc huyện Krasnoarmeysky phía nam, gần làng Belogorskoe. Đây là một mỏm đất cao dựng đứng nhô ra mặt nước, được bao quanh bởi các khe núi và cảnh quan thảo nguyên - đồi ven sông ngoạn mục. Vách đá gắn liền với truyền thuyết dân gian về Stepan (Stenka) Razin - thủ lĩnh cuộc khởi nghĩa nông dân - Cossack lớn ở thế kỷ 17 chống lại chính quyền Nga hoàng. Theo các câu chuyện được truyền tụng và cả trong bài dân ca nổi tiếng, Razin cùng nghĩa quân đã từng dừng chân, đóng trại và giấu 'kho báu' ở khu vực này. Nơi đây cũng là một địa điểm khảo cổ với dấu tích cư trú cổ. Ngày nay, vách đá được xếp là di tích thiên nhiên cấp vùng, thu hút du khách ưa khám phá, dân phượt và người yêu lịch sử tìm đến để phóng tầm mắt ngắm dòng Volga rộng mênh mông, tận hưởng không gian hoang sơ và cảm nhận hơi thở của những huyền thoại vùng sông nước.",
    [
        "Mỏm vách đá hiểm trở nhô ra sông Volga - di tích thiên nhiên cấp vùng.",
        "Gắn với truyền thuyết thủ lĩnh khởi nghĩa Stepan Razin và bài dân ca nổi tiếng.",
        "Điểm ngắm toàn cảnh sông Volga hùng vĩ và cảnh quan đồi - thảo nguyên ven sông.",
    ],
    p("Khu vực thiên nhiên hoang sơ ngoài trời, tham quan tự do; không có hạ tầng dịch vụ chính quy.",
      "Miễn phí.",
      "Nên dành nửa ngày đến trọn ngày (kể cả di chuyển).",
      "Cuối xuân đến đầu thu khi thời tiết khô ráo, đường dễ đi và cảnh quan đẹp.",
      "Cách Saratov ~50–60 km về phía nam; nên đi ô tô gầm cao, mang nước, thức ăn và định vị GPS. Cẩn thận ở mép vách đá."),
    [
        {"title": "Wikipedia (RU) — Утёс Степана Разина", "url": "https://ru.wikipedia.org/wiki/Утёс_Степана_Разина"},
        {"title": "Wikipedia (RU) — Красноармейский район (Саратовская область)", "url": "https://ru.wikipedia.org/wiki/Красноармейский_район_(Саратовская_область)"},
    ],
    ["park_garden", "nature", "cliff", "volga", "legend", "viewpoint"],
    maps_text("Утёс Степана Разина", "Саратовская область", "Stepan Razin Cliff", "Saratov Oblast", 50.615500, 45.652600),
))

# ============================ CẦU (bridge) ============================

# 20) Саратовский мост ------------------------------------------------------------
RECORDS.append(rec(
    "saratov-bridge",
    "Cầu Saratov bắc qua sông Volga (nối Saratov - Engels)",
    "Саратовский мост",
    "Saratov Bridge",
    ["bridge"],
    51.529042, 46.062535,
    "Bắc qua sông Volga, nối thành phố Saratov với thành phố Engels, tỉnh Saratov, Nga",
    "Cầu Saratov là cây cầu đường bộ dài gần 2,8 km bắc qua sông Volga, nối Saratov với thành phố Engels. Khánh thành năm 1965, khi ấy đây từng là một trong những cây cầu dài nhất châu Âu và là biểu tượng kỹ thuật, cảnh quan của thành phố.",
    "Cầu Saratov (Саратовский мост) là công trình giao thông biểu tượng nối liền hai thành phố 'sinh đôi' Saratov và Engels ở hai bờ sông Volga. Khánh thành năm 1965 với chiều dài gần 2,8 km, đây từng được xem là một trong những cây cầu đường bộ dài nhất châu Âu vào thời điểm đó và là niềm tự hào kỹ thuật của cả vùng - công trình còn xuất hiện trong bộ phim hài Xô viết nổi tiếng 'Строится мост'. Cầu có dáng vòm nhẹ nhàng, uốn lượn duyên dáng trên mặt nước rộng mênh mông của sông Volga (tại đây đã mở rộng thành hồ chứa Volgograd), tạo nên một trong những khung cảnh đẹp và dễ nhận ra nhất của Saratov. Từ trên cầu, từ bờ kè hay từ các điểm cao như đồi Sokolovaya, du khách có thể chiêm ngưỡng toàn cảnh dòng Volga, đường chân trời hai thành phố và những chiếc tàu xuôi ngược. Không chỉ là huyết mạch giao thông quan trọng, cầu Saratov còn là điểm ngắm cảnh, chụp ảnh và là hình ảnh gắn bó với bản sắc của một thành phố lớn bên bờ sông Volga.",
    [
        "Cầu đường bộ dài gần 2,8 km bắc qua sông Volga, nối Saratov với Engels.",
        "Khánh thành 1965, từng thuộc hàng những cây cầu dài nhất châu Âu thời đó.",
        "Biểu tượng cảnh quan của thành phố, điểm ngắm sông Volga và hai bờ đô thị.",
    ],
    p("Không gian công cộng, qua lại và ngắm cảnh tự do mọi lúc.",
      "Miễn phí.",
      "Khoảng 20–40 phút (kể cả ngắm cảnh từ bờ kè).",
      "Mùa hè và mùa thu; đẹp nhất lúc hoàng hôn và khi thành phố lên đèn.",
      "Ngắm và chụp cầu đẹp từ bờ kè Các Nhà Du hành Vũ trụ hoặc đồi Sokolovaya; chú ý an toàn giao thông."),
    [
        {"title": "Wikipedia (RU) — Саратовский автодорожный мост", "url": "https://ru.wikipedia.org/wiki/Саратовский_автодорожный_мост"},
        {"title": "Wikipedia (RU) — Саратов", "url": "https://ru.wikipedia.org/wiki/Саратов"},
    ],
    ["bridge", "volga", "engels", "cityscape", "viewpoint", "saratov"],
    maps_text("Саратовский мост", "Саратов", "Saratov Bridge over Volga", "Saratov", 51.529042, 46.062535),
))

# ============================ KHÁC (other) ============================

# 21) Цирк братьев Никитиных ------------------------------------------------------
RECORDS.append(rec(
    "saratov-circus",
    "Rạp xiếc Quốc gia Saratov mang tên anh em Nikitin (Txiếc)",
    "Саратовский государственный цирк имени братьев Никитиных",
    "Saratov State Circus named after the Nikitin Brothers",
    ["other"],
    51.533854, 46.021203,
    "Phố Chapaeva 61, thành phố Saratov, tỉnh Saratov, Nga",
    "Rạp xiếc Saratov là một trong những rạp xiếc cố định lâu đời nhất nước Nga: chính tại Saratov, anh em nhà Nikitin đã mở rạp xiếc Nga đầu tiên năm 1873. Đây là cái nôi của nghệ thuật xiếc dân tộc Nga và vẫn là điểm giải trí hấp dẫn cho gia đình.",
    "Rạp xiếc Quốc gia Saratov mang tên anh em Nikitin (Саратовский цирк) giữ một vị trí đặc biệt trong lịch sử nghệ thuật giải trí Nga: chính tại thành phố này, ba anh em nhà Nikitin - những nghệ sĩ xuất thân bình dân - đã sáng lập rạp xiếc cố định 'thuần Nga' đầu tiên vào năm 1873, đặt nền móng cho truyền thống xiếc dân tộc Nga sau này. Vì vậy, Saratov được xem là một trong những cái nôi của nghệ thuật xiếc nước Nga. Toà nhà rạp xiếc hiện nay tiếp nối truyền thống ấy, thường xuyên tổ chức các chương trình biểu diễn hấp dẫn với nghệ sĩ nhào lộn, ảo thuật gia, chú hề, tiết mục thăng bằng, xiếc thú và các đoàn lưu diễn danh tiếng trong và ngoài nước. Không gian tròn đặc trưng, ánh đèn rực rỡ và bầu không khí sôi động khiến đây trở thành điểm đến được các gia đình, đặc biệt là trẻ em, yêu thích. Đến với rạp xiếc Saratov, du khách không chỉ thưởng thức một buổi biểu diễn giải trí đầy màu sắc mà còn chạm vào một trang sử đáng tự hào của nghệ thuật xiếc Nga.",
    [
        "Nơi anh em Nikitin lập rạp xiếc Nga cố định ĐẦU TIÊN (năm 1873) - cái nôi xiếc Nga.",
        "Chương trình đa dạng: nhào lộn, ảo thuật, chú hề, xiếc thú, đoàn lưu diễn danh tiếng.",
        "Điểm giải trí sôi động, hấp dẫn cho gia đình và trẻ em.",
    ],
    p("Biểu diễn chủ yếu cuối tuần và ngày lễ, thường buổi chiều/tối; xem lịch trên trang chính thức.",
      "Giá vé tuỳ chương trình và vị trí ghế, thường ở mức phải chăng.",
      "Buổi diễn khoảng 2–2,5 giờ.",
      "Quanh năm, nhiều suất vào cuối tuần và kỳ nghỉ học sinh.",
      "Lý tưởng cho gia đình có trẻ nhỏ; đặt vé trước cho các suất cuối tuần đông khách."),
    [
        {"title": "Wikipedia (RU) — Саратовский цирк", "url": "https://ru.wikipedia.org/wiki/Саратовский_цирк"},
        {"title": "Официальный сайт — circ-saratov (Росгосцирк)", "url": "https://circus.saratov.ru/"},
    ],
    ["other", "circus", "entertainment", "family", "historic", "saratov"],
    maps_text("Саратовский цирк имени братьев Никитиных", "Саратов", "Saratov State Circus", "Saratov", 51.533854, 46.021203),
))

# 22) Крытый рынок ----------------------------------------------------------------
RECORDS.append(rec(
    "saratov-covered-market",
    "Chợ Có Mái Che Saratov (Crứt-tưi rư-nốc)",
    "Крытый рынок",
    "Saratov Covered Market",
    ["other"],
    51.532126, 46.020288,
    "Phố Chapaeva 59, thành phố Saratov, tỉnh Saratov, Nga",
    "Chợ Có Mái Che Saratov là một công trình kiến trúc độc đáo đầu thế kỷ 20 (khánh thành 1916), vừa là di tích kiến trúc vừa là khu chợ sầm uất còn hoạt động. Mái vòm rộng lớn không cột chống giữa là kỳ công kỹ thuật thời bấy giờ.",
    "Chợ Có Mái Che Saratov (Крытый рынок) là một trong những công trình kiến trúc dân dụng ấn tượng và được yêu mến nhất thành phố - một trường hợp hiếm hoi nơi một khu chợ trở thành di tích kiến trúc và biểu tượng đô thị. Được xây dựng theo thiết kế của kiến trúc sư Vasily Lyukshin và khánh thành năm 1916, toà nhà mang phong cách tân cổ điển pha modern, nổi bật với mặt tiền bề thế và đặc biệt là không gian nội thất khổng lồ được phủ bởi một mái vòm - kết cấu thép rộng lớn gần như không có cột chống ở giữa, một kỳ công kỹ thuật vào thời điểm đó. Hơn một thế kỷ qua, công trình vẫn giữ nguyên chức năng ban đầu: là khu chợ thực phẩm nhộn nhịp, nơi người dân Saratov mua rau quả tươi, thịt cá, mật ong, các loại đặc sản địa phương và hàng hoá đủ loại. Với du khách, đây là dịp vừa chiêm ngưỡng một công trình kiến trúc đẹp và độc đáo, vừa hoà mình vào nhịp sống thường nhật đầy màu sắc, âm thanh và hương vị của một khu chợ Nga truyền thống ngay giữa lòng thành phố.",
    [
        "Công trình chợ kiến trúc độc đáo, khánh thành 1916 - di tích kiến trúc của thành phố.",
        "Mái vòm - kết cấu thép rộng gần như không cột chống giữa, kỳ công kỹ thuật đầu thế kỷ 20.",
        "Vẫn là khu chợ thực phẩm sầm uất bán rau quả, đặc sản và hàng hoá địa phương.",
    ],
    p("Thường mở cửa hằng ngày ban ngày (khoảng 8:00–19:00), có thể thay đổi theo quầy; nên đến buổi sáng.",
      "Vào chợ miễn phí (mua sắm tính riêng).",
      "Khoảng 30–45 phút.",
      "Buổi sáng khi hàng tươi phong phú và chợ nhộn nhịp nhất.",
      "Dịp mua đặc sản địa phương làm quà; ngắm kiến trúc mái vòm bên trong; giữ đồ cẩn thận nơi đông người."),
    [
        {"title": "Wikipedia (RU) — Крытый рынок (Саратов)", "url": "https://ru.wikipedia.org/wiki/Крытый_рынок_(Саратов)"},
        {"title": "Wikipedia (RU) — Саратов", "url": "https://ru.wikipedia.org/wiki/Саратов"},
    ],
    ["other", "market", "architecture", "landmark", "food", "saratov"],
    maps_text("Крытый рынок", "Саратов", "Saratov Covered Market", "Saratov", 51.532126, 46.020288),
))

# ============================ TƯỢNG ĐÀI / KIẾN TRÚC (monument) ============================

# 23) Памятник песне «Огней так много золотых» -----------------------------------
RECORDS.append(rec(
    "monument-so-many-golden-lights-saratov",
    "Tượng đài bài hát 'Bao ánh đèn vàng' (Ốp-nhây tắc mnô-gô)",
    "Памятник песне «Огней так много золотых»",
    "Monument to the Song 'So Many Golden Lights'",
    ["monument"],
    51.531778, 46.025933,
    "Trên đại lộ đi bộ Kirov, trung tâm thành phố Saratov, tỉnh Saratov, Nga",
    "Tượng đài đường phố độc đáo trên phố đi bộ Kirov, tái hiện chàng trai độc thân trong bài hát Xô viết nổi tiếng 'Огней так много золотых' - bài ca gắn liền với Saratov. Đây là một trong những điểm chụp ảnh được yêu thích nhất thành phố.",
    "Tượng đài dành cho bài hát 'Огней так много золотых, а я люблю женатого' ('Bao ánh đèn vàng lấp lánh, mà em lại yêu người đã có vợ') là một trong những tác phẩm điêu khắc đường phố duyên dáng và được chụp ảnh nhiều nhất Saratov, đặt ngay trên đại lộ đi bộ Kirov. Bài hát trữ tình nổi tiếng thời Xô viết này, ra đời những năm 1950–60, có bối cảnh gắn với Saratov và từ lâu đã trở thành một 'bài ca không chính thức' của thành phố. Tác phẩm điêu khắc khắc hoạ hình ảnh chàng trai trẻ 'độc thân đáng thương' đứng bên trụ đèn, tay cầm bó hoa, chờ đợi trong tâm trạng vấn vương của câu chuyện tình đơn phương trong lời bài hát. Bức tượng mang phong cách sinh động, gần gũi, hài hước, mời gọi du khách và người dân dừng lại, tạo dáng chụp ảnh và ngân nga giai điệu quen thuộc. Là một phần của bộ sưu tập tượng đài - tiểu cảnh trang trí trên phố Kirov, tác phẩm góp phần tạo nên bầu không khí ấm áp, lãng mạn và đậm chất địa phương cho trục phố đi bộ trung tâm - nơi lịch sử, âm nhạc và đời sống thường nhật của Saratov giao hoà.",
    [
        "Tái hiện chàng trai độc thân trong bài hát Xô viết nổi tiếng gắn với Saratov.",
        "Điêu khắc đường phố sinh động, hài hước trên đại lộ đi bộ Kirov.",
        "Một trong những điểm tạo dáng chụp ảnh được yêu thích nhất thành phố.",
    ],
    p("Không gian công cộng ngoài trời, tham quan và chụp ảnh tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 10–15 phút.",
      "Chiều tối khi phố đi bộ đông vui và lên đèn.",
      "Kết hợp dạo trọn đại lộ Kirov; tìm nghe bài hát 'Огней так много золотых' để hiểu ý nghĩa tượng."),
    [
        {"title": "Wikipedia (RU) — Огней так много золотых", "url": "https://ru.wikipedia.org/wiki/Огней_так_много_золотых"},
        {"title": "Wikipedia (RU) — Проспект Кирова (Саратов)", "url": "https://ru.wikipedia.org/wiki/Проспект_Кирова_(Саратов)"},
    ],
    ["monument", "sculpture", "street-art", "song", "photo-spot", "saratov"],
    maps_text("Памятник песне Огней так много золотых", "Саратов", "Monument to the Song So Many Golden Lights", "Saratov", 51.531778, 46.025933),
))

# 24) СГУ (главный корпус) --------------------------------------------------------
RECORDS.append(rec(
    "saratov-state-university",
    "Đại học Quốc gia Saratov (toà nhà lịch sử)",
    "Саратовский государственный университет (СГУ)",
    "Saratov State University (historic campus)",
    ["monument"],
    51.538922, 46.010392,
    "Phố Astrakhanskaya 83, thành phố Saratov, tỉnh Saratov, Nga",
    "Đại học Quốc gia Saratov, thành lập năm 1909, là trường đại học lâu đời và danh giá của vùng Volga. Quần thể các toà nhà học xá lịch sử do kiến trúc sư Karl Müfke thiết kế là một di sản kiến trúc trường học tráng lệ đầu thế kỷ 20.",
    "Đại học Quốc gia Saratov mang tên N. G. Chernyshevsky (СГУ) là một trong những trường đại học lâu đời, lớn và uy tín nhất vùng Volga cũng như cả nước Nga. Trường được thành lập năm 1909, ban đầu chỉ có khoa Y, và nhanh chóng phát triển thành một trung tâm giáo dục - khoa học đa ngành hàng đầu. Điểm thu hút du khách chính là quần thể các toà nhà học xá lịch sử (университетский городок) được xây dựng trong những năm 1910 theo thiết kế của kiến trúc sư tài năng Karl Ludvigovich Müfke. Những toà nhà bằng gạch bề thế, cân đối, kết hợp phong cách tân cổ điển với các chi tiết trang trí tinh tế, được đánh giá là một trong những quần thể kiến trúc đại học đẹp nhất nước Nga đầu thế kỷ 20 và nay là di tích kiến trúc được bảo vệ. Khuôn viên rợp bóng cây với những lối đi, quảng trường nhỏ mang lại bầu không khí học thuật trang nhã, yên bình. Đối với du khách yêu kiến trúc và lịch sử giáo dục, dạo bước quanh khu học xá cổ của СГУ là dịp cảm nhận truyền thống trí thức lâu đời và vẻ đẹp cổ điển của một trong những cái nôi khoa học của vùng Volga.",
    [
        "Đại học lâu đời (thành lập 1909) và danh giá bậc nhất vùng Volga.",
        "Quần thể học xá lịch sử do kiến trúc sư Karl Müfke thiết kế, di tích kiến trúc đầu thế kỷ 20.",
        "Khuôn viên tân cổ điển rợp bóng cây với bầu không khí học thuật trang nhã.",
    ],
    p("Khuôn viên ngoài trời có thể dạo xem ban ngày; bên trong các toà nhà phục vụ hoạt động giảng dạy.",
      "Miễn phí (dạo khuôn viên bên ngoài).",
      "Khoảng 30–45 phút.",
      "Cuối xuân đến đầu thu khi khuôn viên xanh mát; ngày thường có không khí sinh viên.",
      "Tôn trọng hoạt động học tập; chỉ dạo và chụp ảnh khu vực công cộng bên ngoài các toà nhà."),
    [
        {"title": "Wikipedia (RU) — Саратовский государственный университет", "url": "https://ru.wikipedia.org/wiki/Саратовский_государственный_университет"},
        {"title": "Официальный сайт — sgu.ru", "url": "https://www.sgu.ru/"},
    ],
    ["monument", "architecture", "university", "historic", "neoclassical", "saratov"],
    maps_text("Саратовский государственный университет", "Саратов", "Saratov State University", "Saratov", 51.538922, 46.010392),
    official_site="https://www.sgu.ru/",
))

# 25) Памятник «Бык-солевоз» (Энгельс) --------------------------------------------
RECORDS.append(rec(
    "engels-ox-monument",
    "Tượng đài 'Bò chở muối' ở Engels (Bức-xô-lê-vốt)",
    "Памятник «Бык-солевоз»",
    "Monument to the Salt-Carrying Ox",
    ["monument"],
    51.485503, 46.126829,
    "Phố Telmana, thành phố Engels, tỉnh Saratov, Nga",
    "Tượng đài 'Bò chở muối' là biểu tượng của thành phố Engels, tôn vinh những con bò từng kéo xe chở muối từ hồ Elton - nền tảng cho sự ra đời và phát triển của thành phố. Tác phẩm gắn liền với lịch sử nghề muối vùng Volga.",
    "Tượng đài 'Bò chở muối' (Памятник быку-солевозу) là biểu tượng đặc trưng và niềm tự hào của thành phố Engels - đô thị đối diện Saratov qua sông Volga. Tác phẩm điêu khắc khắc hoạ hình ảnh một con bò to khoẻ, gắn liền với chương lịch sử đã khai sinh ra thành phố: vào thế kỷ 18–19, khu định cư Pokrovskaya Sloboda (tiền thân của Engels) hình thành và phát triển thịnh vượng nhờ nghề vận chuyển và buôn bán muối khai thác từ hồ Elton. Chính những đàn bò kéo xe - 'bò chở muối' (быки-солевозы) - đã cần mẫn vận chuyển hàng nghìn tấn muối vượt thảo nguyên về bến sông, mang lại sự trù phú cho vùng đất. Bức tượng là lời tri ân dành cho những 'người lao động bốn chân' thầm lặng ấy và cho cả một thời kỳ lịch sử kinh tế quan trọng. Đặt ở vị trí dễ thấy trong thành phố, tượng đài không chỉ là điểm nhận diện, chụp ảnh của Engels mà còn là cách kể chuyện lịch sử độc đáo, giúp du khách hiểu vì sao vùng đất bên tả ngạn Volga này lại gắn bó mật thiết với 'vàng trắng' - muối - từ thuở lập nghiệp.",
    [
        "Biểu tượng của thành phố Engels, tôn vinh nghề vận chuyển muối từ hồ Elton.",
        "Gắn với lịch sử khai sinh Pokrovskaya Sloboda (tiền thân Engels) nhờ 'vàng trắng' - muối.",
        "Điểm nhận diện, chụp ảnh và kể chuyện lịch sử độc đáo của Engels.",
    ],
    p("Không gian công cộng ngoài trời, tham quan và chụp ảnh tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 10–15 phút.",
      "Quanh năm; ban ngày thuận tiện cho chụp ảnh.",
      "Kết hợp qua cầu Saratov thăm Engels: Bảo tàng Địa phương học và các đài tưởng niệm gần đó."),
    [
        {"title": "Wikipedia (RU) — Энгельс (город)", "url": "https://ru.wikipedia.org/wiki/Энгельс_(город)"},
        {"title": "Culture.ru — Памятник быку-солевозу", "url": "https://www.culture.ru/objects/"},
    ],
    ["monument", "sculpture", "salt", "history", "engels", "landmark"],
    maps_text("Памятник Бык-солевоз", "Энгельс", "Monument to the Salt-Carrying Ox", "Engels", 51.485503, 46.126829),
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
