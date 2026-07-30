# -*- coding: utf-8 -*-
"""_add_places_kirov_20260728_220325.py — VÙNG: Tỉnh Kirov (Кировская область)
(lần chạy tự động 2026-07-28).

Bối cảnh: kirov.json hiện có 7 địa điểm (Tu viện Trifonov, Bảo tàng đồ chơi Dymkovo,
làng Velikoretskoye, Bảo tàng cổ sinh vật Kotelnich, Vườn Aleksandrovsky, khu điều
dưỡng Nizhne-Ivkino, Bảo tàng Mỹ thuật Vasnetsov). Bổ sung 24 địa điểm THẬT SỰ nổi
tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 31.

Trung tâm là thành phố Kirov (Vyatka xưa). Phân bố loại hình (24 bản ghi mới):
- museum (7): Музей истории шоколада «Криолло», Вятская кунсткамера, Кировский обл.
  краеведческий музей (им. Алабина), Музей Циолковского/авиации и космонавтики,
  музей «Диорама», Дом-музей Салтыкова-Щедрина, Музей-усадьба художников Васнецовых (Рябово).
- church (4): Серафимовский собор, Спасский собор, Церковь Иоанна Предтечи, Троицкий
  собор (Яранск).
- palace (1): Особняк Т. Ф. Булычёва («дом-теремок»).
- theatre (1): Кировский драматический театр им. С. М. Кирова.
- square_street (3): Театральная площадь, улица Спасская («Вятский Арбат»), г. Слободской
  (Соборная площадь / колокольня).
- monument (1): Вечный огонь (набережная Грина).
- bridge (1): Старый мост через Вятку.
- park_garden (6): Ботанический сад, Кочуровский парк, заповедник «Нургуш», озеро Шайтан,
  Береснятский водопад, Атарская Лука.

TOẠ ĐỘ — xác minh chéo (ru.wikipedia coord-API/geohack, OpenStreetMap/Nominatim, 2026-07-28).
Phạm vi tỉnh Kirov lat ~56-61; lon ~46-54 — tất cả toạ độ trong phạm vi, KHÔNG đảo lat/lon:
  Серафимовский собор 58.596767,49.687738 (OSM way 170484214, «Свято-Серафимовский собор»,
  Успенская/б.Урицкого 25); Спасский собор 58.602836,49.684686 (ru.wiki coord-API);
  Церковь Иоанна Предтечи 58.607426,49.677507 (ru.wiki coord-API, ул.Свободы 54Д);
  Особняк Булычёва 58.597980,49.682173 (OSM, ул.Ленина 96А); Музей шоколада «Криолло»
  58.602352,49.683019 (OSM, ул.Спасская 15); Вятская кунсткамера 58.603557,49.678385 (OSM,
  ул.Московская 12а); Краеведческий музей 58.602048,49.683681 (OSM, ул.Спасская 6); Музей
  Циолковского 58.605298,49.678989 (OSM, ул.Преображенская 16); Диорама 58.590793,49.652933
  (OSM tourism=museum «Диорама», Октябрьский пр. 15); Дом-музей Салтыкова-Щедрина
  58.596705,49.681082 (OSM, ул.Ленина 93); Драмтеатр 58.604722,49.668056 (ru.wiki geohack,
  Театральная пл./ул.Московская 37); Театральная площадь 58.604000,49.668600 (центр,
  у драмтеатра); ул.Спасская 58.602090,49.676750 (OSM way 62332747, центр пешеходной зоны);
  Вечный огонь 58.603970,49.689940 (OSM node 1345594582, наб.Грина); Старый мост
  58.616160,49.689280 (OSM way 1092670147, середина моста Киров-Дымково); Ботанический сад
  58.596280,49.666860 (OSM way 25912744, ул.К.Маркса 95); Кочуровский парк 58.592483,49.602439
  (OSM way 173229559, Юго-Запад); заповедник «Нургуш» 57.948460,48.337950 (OSM node 1908631617,
  усадьба/офис, с.Боровка, Котельничский р-н); озеро Шайтан 57.096220,49.462170 (OSM way
  95778399 + ru.wiki, памятник природы); Береснятский водопад 57.388060,49.029850 (OSM node
  1292891079, р.Немда, Советский р-н); Музей-усадьба Васнецовых 58.198180,50.798050 (OSM way
  211999637, с.Рябово, Зуевский р-н); Троицкий собор (Яранск) 57.305280,47.875880 (OSM way
  230040330); Слободской/колокольня 58.731980,50.184500 (OSM way 87221539, Соборная пл.);
  Атарская Лука 57.521670,49.290000 (ru.wiki coord-API, излучина р.Вятки).

GHI CHÚ: озеро Шайтан theo OSM nay thuộc Уржумский округ (ranh giới huyện thay đổi, huyện
Лебяжский đã sáp nhập) — toạ độ khớp 2 nguồn nên vẫn dùng. Заповедник «Нургуш» ghi toạ độ
trụ sở/усадьба ở с.Боровка (vùng lõi rừng ngập không có node công khai). Атарская Лука là
điểm đại diện trung tâm khúc uốn sông rộng. KHÔNG bịa toạ độ.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_kirov_20260728_220325.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "kirov"
REGION_NAME_VI = "Tỉnh Kirov"
FD = "Vùng Volga"


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


def indoor_practical(hours, ticket, duration, best_time, tips):
    return {
        "hours_vi": hours,
        "ticket_vi": ticket,
        "duration_vi": duration,
        "best_time_vi": best_time,
        "tips_vi": tips,
    }


def outdoor_practical(duration, best_time, tips,
                      hours="Không gian ngoài trời, tham quan ban ngày; không có giờ cố định.",
                      ticket="Vào tự do (khu ngoài trời); một số dịch vụ/khu bảo tồn có thể thu phí."):
    return {
        "hours_vi": hours,
        "ticket_vi": ticket,
        "duration_vi": duration,
        "best_time_vi": best_time,
        "tips_vi": tips,
    }


RECORDS = []

# ============================ NHÀ THỜ / CHÍNH THỐNG (church) ============================

# 1) Серафимовский собор -------------------------------------------------------------
RECORDS.append(rec(
    "serafimovsky-cathedral-kirov",
    "Nhà thờ Serafimovsky (Serafimovsky sobor)",
    "Серафимовский собор",
    "St. Seraphim Cathedral",
    ["church"],
    58.596767, 49.687738,
    "Phố Uspenskaya (trước là Uritskogo) 25, thành phố Kirov 610002, tỉnh Kirov, Nga.",
    "Nhà thờ Serafimovsky là ngôi nhà thờ gạch đỏ duyên dáng xây năm 1904-1907 theo phong cách 'giả Nga' (pseudo-russkiy stil), mang tên thánh Serafim xứ Sarov. Đây là một trong số ít nhà thờ ở Kirov không bị đóng cửa suốt thời Xô Viết và từng giữ vai trò nhà thờ chính tòa của thành phố.",
    "Toạ lạc ở khu trung tâm cổ của Kirov, gần bờ cao sông Vyatka, Nhà thờ Serafimovsky (thường gọi 'nhà thờ đỏ') nổi bật với tường gạch đỏ chưa trát, các chi tiết trang trí kokoshnik, mái vòm hình củ hành và tháp chuông theo phong cách 'giả Nga' thịnh hành đầu thế kỷ 20. Công trình do kiến trúc sư I. A. Charushin thiết kế, khởi công năm 1904 và khánh thành năm 1907, cung hiến cho thánh Serafim xứ Sarov - vị thánh vừa được phong ngay trước đó. Điều đặc biệt là trong thời kỳ đàn áp tôn giáo dưới Liên Xô, nhà thờ này gần như không bao giờ ngừng hoạt động, có thời còn là nhà thờ chính tòa của giáo phận Vyatka và là nơi cất giữ nhiều thánh tích được chuyển về từ các nhà thờ bị phá. Nội thất giữ được nhiều biểu tượng (icon) cổ và giá tượng (iconostas) chạm khắc thếp vàng. Với du khách, đây là một trong những điểm nhấn kiến trúc dễ nhận biết nhất của Kirov: sắc đỏ rực của tường gạch tương phản với mái vòm xanh và thánh giá vàng tạo nên khung hình rất ăn ảnh, đặc biệt dưới nắng chiều.",
    [
        "Nhà thờ gạch đỏ phong cách 'giả Nga' (1904-1907), do kiến trúc sư Charushin thiết kế.",
        "Một trong số ít nhà thờ ở Kirov hoạt động liên tục suốt thời Xô Viết.",
        "Từng là nhà thờ chính tòa của thành phố; lưu giữ nhiều icon và thánh tích cổ.",
    ],
    indoor_practical(
        "Mở cửa hằng ngày theo giờ lễ (thường từ sáng sớm đến tối).",
        "Miễn phí vào viếng; tùy tâm công đức.",
        "Khoảng 30-45 phút.",
        "Quanh năm; đẹp nhất dưới nắng chiều khi tường gạch đỏ rực lên.",
        "Nữ giới nên trùm khăn và mặc kín đáo; giữ yên lặng khi có nghi lễ; kết hợp dạo phố cổ trung tâm.",
    ),
    [
        {"title": "Wikipedia (RU) — Серафимовская церковь (Киров)", "url": "https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%80%D0%B0%D1%84%D0%B8%D0%BC%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F_%D1%86%D0%B5%D1%80%D0%BA%D0%BE%D0%B2%D1%8C_(%D0%9A%D0%B8%D1%80%D0%BE%D0%B2)"},
        {"title": "Sobory.ru — Серафимовский собор в Кирове", "url": "https://sobory.ru/geo/city/Kirov"},
    ],
    ["church", "orthodox", "architecture", "red-brick", "kirov", "landmark"],
    maps_text("Серафимовский собор", "Киров", "St. Seraphim Cathedral", "Kirov", 58.596767, 49.687738),
))

# 2) Спасский собор ------------------------------------------------------------------
RECORDS.append(rec(
    "spassky-cathedral-kirov",
    "Nhà thờ Spassky (Spassky sobor)",
    "Спасский собор",
    "Spassky (Saviour) Cathedral",
    ["church"],
    58.602836, 49.684686,
    "Phố Kazanskaya 50, thành phố Kirov 610000, tỉnh Kirov, Nga.",
    "Nhà thờ Spassky thờ ảnh Chúa Cứu Thế 'không do tay người vẽ' (Spas Nerukotvorny), gắn với truyền thuyết bức icon kỳ diệu của Vyatka được đưa về Moskva - vì thế cổng Spasskaya của điện Kremlin mang tên này. Công trình baroque thế kỷ 18 vừa được phục dựng khang trang cùng tháp chuông cao.",
    "Nằm trên phố Kazanskaya ở lõi phố cổ Kirov, Nhà thờ Spassky (Spaso-Preobrazhensky/Spassky sobor) gắn với một trong những truyền thuyết được yêu thích nhất của vùng Vyatka: bức icon Chúa Cứu Thế 'không do tay người vẽ' (Spas Nerukotvorny) nổi tiếng linh nghiệm, được cho là đã được rước về Moskva thế kỷ 17, và theo dân gian, chính vì bản sao icon Vyatka treo trên cổng mà cổng đó của điện Kremlin mang tên 'Spasskie vorota' (Cổng Cứu Thế). Nhà thờ đá đầu tiên ở đây có từ đầu thế kỷ 18, mang dáng dấp baroque với những đường nét thanh thoát và tháp chuông vươn cao. Thời Xô Viết công trình bị đóng cửa, cải tạo thành nhà ở và cơ sở công cộng, phần chóp và tháp chuông bị phá. Từ đầu thế kỷ 21, nhà thờ được phục dựng công phu: tháp chuông và những mái vòm mạ vàng lại sáng lên trên nền trời trung tâm thành phố. Ngày nay đây là một trong những nhà thờ đẹp và nổi bật nhất Kirov, đồng thời là điểm dừng thú vị để nghe câu chuyện lịch sử ly kỳ về mối liên hệ giữa Vyatka và điện Kremlin Moskva.",
    [
        "Gắn truyền thuyết icon 'Spas Nerukotvorny' của Vyatka và tên cổng Spasskaya của Kremlin.",
        "Kiến trúc baroque thế kỷ 18 với tháp chuông cao, mái vòm mạ vàng.",
        "Được phục dựng công phu đầu thế kỷ 21 sau khi bị phá hoại thời Xô Viết.",
    ],
    indoor_practical(
        "Mở cửa hằng ngày theo giờ lễ.",
        "Miễn phí vào viếng; tùy tâm công đức.",
        "Khoảng 30-45 phút.",
        "Quanh năm; buổi sáng nắng đẹp để chụp mái vòm mạ vàng.",
        "Ăn mặc kín đáo, nữ trùm khăn; kết hợp dạo phố Spasskaya và bờ sông gần đó.",
    ),
    [
        {"title": "Wikipedia (RU) — Спасский собор (Киров)", "url": "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B0%D1%81%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BE%D0%B1%D0%BE%D1%80_(%D0%9A%D0%B8%D1%80%D0%BE%D0%B2)"},
        {"title": "Culture.ru — Спасский собор, Киров", "url": "https://www.culture.ru/institutes/search?query=%D0%A1%D0%BF%D0%B0%D1%81%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BE%D0%B1%D0%BE%D1%80%20%D0%9A%D0%B8%D1%80%D0%BE%D0%B2"},
    ],
    ["church", "orthodox", "baroque", "history", "kirov", "landmark"],
    maps_text("Спасский собор", "Киров", "Spassky Cathedral", "Kirov", 58.602836, 49.684686),
))

# 3) Церковь Иоанна Предтечи ---------------------------------------------------------
RECORDS.append(rec(
    "ioann-predtecha-church-kirov",
    "Nhà thờ Thánh Gioan Tẩy Giả (Ioanno-Predtechenskaya tserkov)",
    "Церковь Иоанна Предтечи",
    "Church of St. John the Baptist",
    ["church"],
    58.607426, 49.677507,
    "Phố Svobody 54Д, thành phố Kirov 610000, tỉnh Kirov, Nga.",
    "Nhà thờ Thánh Gioan Tẩy Giả (1714-1723) là kiệt tác của phong cách 'baroque Vyatka' với mặt tiền trang trí dày đặc cửa sổ và hoạ tiết đá trắng nhiều tầng lớp độc đáo. Đây là một trong những công trình tôn giáo cổ và tinh xảo bậc nhất còn lại của thành phố.",
    "Xây dựng trong các năm 1714-1723, Nhà thờ Thánh Gioan Tẩy Giả là một trong những ví dụ tiêu biểu và duyên dáng nhất của trường phái 'baroque Vyatka' (vyatskoye barokko) - dòng kiến trúc nhà thờ địa phương nổi bật với lối trang trí đá trắng cầu kỳ trên nền tường. Điều khiến ngôi nhà thờ này gây ấn tượng mạnh là mặt tiền dày đặc chi tiết: những khung cửa sổ đủ hình dáng, các dải hoa văn, cột giả và gờ chỉ chạm nổi tạo cảm giác 'thêu ren bằng đá'. Trải qua thời Xô Viết bị đóng cửa và sử dụng sai mục đích khiến công trình xuống cấp nặng, nhà thờ đã được trùng tu để trả lại dáng vẻ ban đầu và nay hoạt động trở lại. Với người yêu kiến trúc, đây là điểm đến bắt buộc để hiểu bản sắc của kiến trúc Nga cổ vùng Vyatka - vừa mộc mạc vừa tinh tế. Nhà thờ nằm không xa trung tâm và có thể kết hợp trong một buổi dạo bộ khám phá các công trình lịch sử của Kirov.",
    [
        "Kiệt tác 'baroque Vyatka' (1714-1723) với mặt tiền trang trí đá trắng cầu kỳ.",
        "Một trong những nhà thờ cổ và tinh xảo nhất còn lại ở Kirov.",
        "Được trùng tu trả lại dáng vẻ nguyên bản sau thời Xô Viết.",
    ],
    indoor_practical(
        "Mở cửa theo giờ lễ; nên xem lịch trước.",
        "Miễn phí vào viếng; tùy tâm công đức.",
        "Khoảng 30 phút.",
        "Quanh năm; ánh sáng ban ngày làm nổi bật hoa văn đá trắng trên mặt tiền.",
        "Ngắm kỹ phần trang trí mặt tiền; ăn mặc kín đáo khi vào trong.",
    ),
    [
        {"title": "Wikipedia (RU) — Церковь Иоанна Предтечи (Киров)", "url": "https://ru.wikipedia.org/wiki/%D0%A6%D0%B5%D1%80%D0%BA%D0%BE%D0%B2%D1%8C_%D0%98%D0%BE%D0%B0%D0%BD%D0%BD%D0%B0_%D0%9F%D1%80%D0%B5%D0%B4%D1%82%D0%B5%D1%87%D0%B8_(%D0%9A%D0%B8%D1%80%D0%BE%D0%B2)"},
        {"title": "Sobory.ru — Церкви Кирова", "url": "https://sobory.ru/geo/city/Kirov"},
    ],
    ["church", "orthodox", "vyatka-baroque", "architecture", "kirov", "heritage"],
    maps_text("Церковь Иоанна Предтечи", "Киров", "Church of St. John the Baptist", "Kirov", 58.607426, 49.677507),
))

# 4) Троицкий собор (Яранск) ---------------------------------------------------------
RECORDS.append(rec(
    "trinity-cathedral-yaransk",
    "Nhà thờ Chúa Ba Ngôi ở Yaransk (Troitsky sobor)",
    "Троицкий собор (Яранск)",
    "Trinity Cathedral (Yaransk)",
    ["church"],
    57.305280, 47.875880,
    "Phố Kirova 3, thành phố Yaransk, tỉnh Kirov, Nga (cách thành phố Kirov khoảng 220 km về phía tây nam).",
    "Nhà thờ Chúa Ba Ngôi là công trình lớn và bề thế nhất của thị trấn cổ Yaransk, xây cuối thế kỷ 19 theo thiết kế của kiến trúc sư trứ danh Konstantin Ton - tác giả Nhà thờ Chúa Cứu Thế ở Moskva. Ngôi nhà thờ năm mái vòm thống lĩnh cảnh quan cả vùng.",
    "Yaransk là một trong những thị trấn cổ ở tây nam tỉnh Kirov, và biểu tượng nổi bật nhất của nó là Nhà thờ Chúa Ba Ngôi (Troitsky sobor). Được xây trong các thập niên cuối thế kỷ 19 (khánh thành khoảng năm 1857-1889 tùy hạng mục) theo dự án gắn với kiến trúc sư Konstantin Ton - người thiết kế Nhà thờ Chúa Cứu Thế ở Moskva - công trình mang phong cách 'Nga-Byzantine' hoành tráng với khối nhà thờ đồ sộ, năm mái vòm lớn và tháp chuông cao vươn lên giữa nền nhà thấp của thị trấn. Đây được xem là một trong những nhà thờ lớn và đẹp bậc nhất tỉnh Kirov ngoài thành phố tỉnh lỵ. Nội thất rộng, cao thoáng, từng được trang trí bích họa. Sau thời Xô Viết, nhà thờ được khôi phục hoạt động và tiếp tục là trung tâm tôn giáo của cả huyện. Với du khách đi sâu vào tỉnh Kirov, Yaransk và nhà thờ Chúa Ba Ngôi là điểm dừng đáng giá để cảm nhận vẻ đẹp của một thị trấn tỉnh lẻ Nga cổ kính, yên bình.",
    [
        "Nhà thờ lớn nhất Yaransk, phong cách 'Nga-Byzantine' với năm mái vòm và tháp chuông cao.",
        "Thiết kế gắn với kiến trúc sư Konstantin Ton (tác giả Nhà thờ Chúa Cứu Thế ở Moskva).",
        "Biểu tượng của thị trấn cổ ở tây nam tỉnh Kirov, được khôi phục sau thời Xô Viết.",
    ],
    indoor_practical(
        "Mở cửa theo giờ lễ.",
        "Miễn phí vào viếng; tùy tâm công đức.",
        "Khoảng 40 phút (chưa kể quãng đường xa từ Kirov).",
        "Quanh năm; mùa hè thuận tiện cho chuyến đi xa.",
        "Yaransk cách Kirov khoảng 220 km, nên đi ô tô; kết hợp dạo trung tâm thị trấn cổ.",
    ),
    [
        {"title": "Wikipedia (RU) — Яранск", "url": "https://ru.wikipedia.org/wiki/%D0%AF%D1%80%D0%B0%D0%BD%D1%81%D0%BA"},
        {"title": "Sobory.ru — Троицкий собор в Яранске", "url": "https://sobory.ru/geo/city/Yaransk"},
    ],
    ["church", "orthodox", "cathedral", "yaransk", "history", "architecture"],
    maps_text("Троицкий собор", "Яранск", "Trinity Cathedral", "Yaransk", 57.305280, 47.875880),
))

# ============================ DINH THỰ (palace) ============================

# 5) Особняк Т. Ф. Булычёва ----------------------------------------------------------
RECORDS.append(rec(
    "bulychev-mansion-kirov",
    "Dinh thự Bulychyov ('lâu đài cổ tích', Osobnyak Bulychyova)",
    "Особняк Т. Ф. Булычёва",
    "Bulychyov Mansion",
    ["palace"],
    58.597980, 49.682173,
    "Phố Lenina 96, thành phố Kirov 610000, tỉnh Kirov, Nga.",
    "Dinh thự Bulychyov là toà biệt thự lãng mạn kiểu tân Gothic - 'lâu đài cổ tích' đẹp nhất Kirov, do thương gia T. F. Bulychyov cho xây năm 1911. Cổng vào canh bởi hai con sư tử, mặt tiền điểm những chú sư tử đầu chim (griffin) và đại bàng hai đầu.",
    "Được xây năm 1911 theo thiết kế của kiến trúc sư I. A. Charushin cho nhà buôn giàu có Tikhon Filippovich Bulychyov, dinh thự này là công trình dân dụng lãng mạn và cầu kỳ nhất Kirov. Với những tháp nhọn, cửa sổ vòm nhọn, lan can chạm ren và chi tiết trang trí kiểu tân Gothic pha chút phương Đông, toà nhà trông như một lâu đài bước ra từ truyện cổ tích - người dân quen gọi là 'dom-teremok' (nhà - lâu đài nhỏ). Trước cổng có hai tượng sư tử, còn mặt tiền được điểm những sư tử đầu chim (griffin) và đại bàng hai đầu bằng gang. Tương truyền Bulychyov xây toà nhà xa hoa này cho con gái sống ở thủ đô, nhưng cô không chịu chuyển về Vyatka, nên ông đã tặng lại nó cho thành phố làm nơi nuôi dưỡng thương binh và người già. Sau Cách mạng, toà nhà được dùng cho nhiều cơ quan và hiện là trụ sở cơ quan nhà nước, nên khách chỉ tham quan từ bên ngoài - nhưng chính mặt tiền lộng lẫy mới là thứ khiến ai đi qua cũng phải dừng lại ngắm và chụp ảnh. Đây là một trong những biểu tượng kiến trúc dễ nhận biết nhất của Kirov.",
    [
        "'Lâu đài cổ tích' tân Gothic đẹp nhất Kirov, xây năm 1911 (kiến trúc sư Charushin).",
        "Cổng có hai sư tử đá; mặt tiền điểm griffin và đại bàng hai đầu bằng gang.",
        "Gắn giai thoại thương gia Bulychyov tặng lại toà nhà cho thành phố làm nhà từ thiện.",
    ],
    indoor_practical(
        "Chỉ ngắm từ bên ngoài (hiện là trụ sở cơ quan nhà nước, không mở tham quan nội thất).",
        "Miễn phí (ngắm mặt tiền từ ngoài phố).",
        "Khoảng 15-20 phút.",
        "Quanh năm; buổi sáng hoặc chiều để chụp mặt tiền không bị ngược sáng.",
        "Chỉ tham quan ngoại thất; kết hợp dạo phố Lenina và trung tâm gần đó.",
    ),
    [
        {"title": "Wikipedia (RU) — Особняк Т. Ф. Булычёва", "url": "https://ru.wikipedia.org/wiki/%D0%9E%D1%81%D0%BE%D0%B1%D0%BD%D1%8F%D0%BA_%D0%A2._%D0%A4._%D0%91%D1%83%D0%BB%D1%8B%D1%87%D1%91%D0%B2%D0%B0"},
        {"title": "Culture.ru — Особняк Булычёва, Киров", "url": "https://www.culture.ru/institutes/search?query=%D0%9E%D1%81%D0%BE%D0%B1%D0%BD%D1%8F%D0%BA%20%D0%91%D1%83%D0%BB%D1%8B%D1%87%D1%91%D0%B2%D0%B0"},
    ],
    ["mansion", "neo-gothic", "architecture", "landmark", "kirov", "merchant"],
    maps_text("Особняк Булычёва", "Киров", "Bulychyov Mansion", "Kirov", 58.597980, 49.682173),
))

# ============================ BẢO TÀNG (museum) ============================

# 6) Музей истории шоколада «Криолло» ------------------------------------------------
RECORDS.append(rec(
    "chocolate-museum-kirov",
    "Bảo tàng Lịch sử Sô-cô-la 'Criollo' (Muzey istorii shokolada 'Kriollo')",
    "Музей истории шоколада «Криолло»",
    "Criollo Chocolate History Museum",
    ["museum"],
    58.602352, 49.683019,
    "Phố Spasskaya 15, thành phố Kirov 610000, tỉnh Kirov, Nga.",
    "Bảo tàng Sô-cô-la 'Criollo' trên phố cổ Spasskaya kể câu chuyện của ca cao và sô-cô-la từ người Maya, Aztec đến ngày nay. Khách được nếm thử, xem làm sô-cô-la thủ công và tự tay đổ khuôn trong các buổi masterclass.",
    "Nằm trong một toà nhà lịch sử trên phố đi bộ Spasskaya, Bảo tàng Lịch sử Sô-cô-la 'Criollo' là một điểm đến nhỏ nhưng thú vị và rất được lòng du khách, đặc biệt là gia đình có trẻ nhỏ. Trưng bày dẫn dắt người xem qua hành trình của cây ca cao và món sô-cô-la: từ nghi lễ dùng hạt ca cao của người Maya và Aztec ở Trung Mỹ, qua thời sô-cô-la trở thành thức uống quý tộc châu Âu, đến kỷ nguyên sản xuất công nghiệp và những phong bao, khuôn, dụng cụ, quảng cáo cổ. Điểm hấp dẫn nhất là phần trải nghiệm: khách được nếm thử nhiều loại sô-cô-la, xem nghệ nhân tạo hình các tác phẩm bằng sô-cô-la, và tham gia lớp học (masterclass) tự đổ khuôn, trang trí thanh sô-cô-la để mang về. Cửa hàng của bảo tàng bán các sản phẩm sô-cô-la thủ công làm quà. Đây là lựa chọn dễ chịu, ngọt ngào để đổi vị giữa các điểm tham quan lịch sử và nhà thờ ở trung tâm Kirov.",
    [
        "Hành trình ca cao và sô-cô-la từ người Maya, Aztec đến thời hiện đại.",
        "Nếm thử nhiều loại sô-cô-la và xem nghệ nhân tạo hình sô-cô-la thủ công.",
        "Lớp học (masterclass) tự đổ khuôn, trang trí thanh sô-cô-la mang về làm quà.",
    ],
    indoor_practical(
        "Mở cửa hằng ngày (thường 10:00-19:00); nên xem lịch masterclass.",
        "Vé vào cửa và các buổi masterclass tính phí; nên đăng ký trước.",
        "Khoảng 45 phút-1 giờ.",
        "Quanh năm (bảo tàng trong nhà); cuối tuần thường có nhiều buổi trải nghiệm.",
        "Đặt trước buổi masterclass nếu đi cùng trẻ; mua sô-cô-la thủ công làm quà.",
    ),
    [
        {"title": "Culture.ru — Музеи Кирова", "url": "https://www.culture.ru/institutes/search?query=%D0%9C%D1%83%D0%B7%D0%B5%D0%B9%20%D1%88%D0%BE%D0%BA%D0%BE%D0%BB%D0%B0%D0%B4%D0%B0%20%D0%9A%D0%B8%D1%80%D0%BE%D0%B2"},
        {"title": "Кировская область — туристический портал", "url": "https://www.kirovreg.ru/"},
    ],
    ["museum", "chocolate", "family", "tasting", "masterclass", "kirov"],
    maps_text("Музей истории шоколада Криолло", "Киров", "Criollo Chocolate Museum", "Kirov", 58.602352, 49.683019),
))

# 7) Вятская кунсткамера -------------------------------------------------------------
RECORDS.append(rec(
    "vyatka-kunstkamera-kirov",
    "Bảo tàng Vyatka Kunstkamera (Vyatskaya kunstkamera)",
    "Вятская кунсткамера",
    "Vyatka Kunstkamera Museum",
    ["museum"],
    58.603557, 49.678385,
    "Phố Moskovskaya 12а, thành phố Kirov 610000, tỉnh Kirov, Nga.",
    "Vyatka Kunstkamera là bảo tàng đời sống thị dân tỉnh lẻ cuối thế kỷ 19 - đầu thế kỷ 20, đặt trong một dinh thự thương gia cổ. Các phòng được phục dựng như phòng khách, phòng làm việc xưa với đồ sứ, nhạc cụ, đồ nội thất và vật dụng sinh hoạt nguyên bản.",
    "Đặt trong một biệt thự gỗ - đá xinh đẹp cuối thế kỷ 19 trên phố Moskovskaya ở trung tâm cổ Kirov, bảo tàng 'Vyatka Kunstkamera' tái hiện sinh động nếp sống của tầng lớp thị dân và thương nhân Vyatka thời cuối đế chế Nga. Khác với các bảo tàng lịch sử khô khan, nơi đây bài trí theo lối 'phòng thời đại' (interyer): phòng khách, phòng làm việc, phòng nhạc... được phục dựng với đồ nội thất, đồ sứ, đồng hồ, đèn, nhạc cụ, sách và những vật dụng sinh hoạt nguyên bản, khiến khách như bước vào một ngôi nhà quý tộc tỉnh lẻ hơn một thế kỷ trước. Bộ sưu tập nổi bật với đồ sứ và pha lê, quạt, hộp trang sức, ảnh gia đình cùng nhiều 'điều kỳ lạ' đúng tinh thần 'kunstkamera' (phòng sưu tầm hiếu kỳ). Không gian ấm cúng và chỉ dẫn tận tình khiến đây là một trong những bảo tàng được du khách yêu thích ở Kirov, phù hợp cho ai muốn cảm nhận đời sống thường nhật, thẩm mỹ và văn hoá vật chất của người Vyatka xưa.",
    [
        "Tái hiện đời sống thị dân, thương nhân Vyatka cuối thế kỷ 19 - đầu thế kỷ 20.",
        "Các 'phòng thời đại' phục dựng với đồ sứ, nhạc cụ, nội thất nguyên bản.",
        "Đặt trong dinh thự cổ, không gian ấm cúng, chỉ dẫn tận tình.",
    ],
    indoor_practical(
        "Mở cửa theo lịch bảo tàng (thường đóng cửa một ngày đầu tuần); nên kiểm tra trước.",
        "Vé vào cửa mức vừa phải; tham quan có hướng dẫn tính thêm.",
        "Khoảng 1 giờ.",
        "Quanh năm (bảo tàng trong nhà).",
        "Đi cùng hướng dẫn viên để nghe các câu chuyện về hiện vật; nằm ngay khu phố cổ trung tâm.",
    ),
    [
        {"title": "Culture.ru — Вятская кунсткамера", "url": "https://www.culture.ru/institutes/search?query=%D0%92%D1%8F%D1%82%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BA%D1%83%D0%BD%D1%81%D1%82%D0%BA%D0%B0%D0%BC%D0%B5%D1%80%D0%B0"},
        {"title": "Кировский областной краеведческий музей — филиалы", "url": "https://muzey43.ru/"},
    ],
    ["museum", "history", "interior", "merchant", "kirov", "indoor"],
    maps_text("Вятская кунсткамера", "Киров", "Vyatka Kunstkamera", "Kirov", 58.603557, 49.678385),
))

# 8) Кировский областной краеведческий музей ----------------------------------------
RECORDS.append(rec(
    "kirov-regional-museum",
    "Bảo tàng Địa phương học Tỉnh Kirov (mang tên P. V. Alabin)",
    "Кировский областной краеведческий музей имени П. В. Алабина",
    "Kirov Regional Museum of Local Lore (Alabin)",
    ["museum"],
    58.602048, 49.683681,
    "Phố Spasskaya 6, thành phố Kirov 610000, tỉnh Kirov, Nga.",
    "Đây là một trong những bảo tàng địa phương học lâu đời nhất nước Nga, thành lập năm 1866 theo sáng kiến của nhà hoạt động P. V. Alabin. Bộ sưu tập trải rộng từ thiên nhiên, khảo cổ, lịch sử đến dân tộc học vùng Vyatka.",
    "Được sáng lập năm 1866 theo sáng kiến của Pyotr Vladimirovich Alabin - một nhà hoạt động xã hội có công lớn với vùng Vyatka - Bảo tàng Địa phương học Tỉnh Kirov là một trong những bảo tàng công cộng ra đời sớm nhất ở tỉnh lẻ nước Nga. Trải qua hơn một thế kỷ rưỡi, bảo tàng đã tích lũy một bộ sưu tập đồ sộ gồm hàng trăm nghìn hiện vật, phân bố qua nhiều chi nhánh trong thành phố. Nội dung trưng bày bao quát nhiều mảng: thiên nhiên vùng Vyatka (địa chất, động thực vật, các loài hóa thạch), khảo cổ và lịch sử từ thời cổ đến hiện đại, dân tộc học của người Nga, Udmurt, Mari, Tatar cùng chung sống trong vùng, cùng đời sống, nghề thủ công và tôn giáo địa phương. Trụ sở chính trên phố Spasskaya trưng bày phần lịch sử - dân tộc học, trong khi các gian thiên nhiên và triển lãm chuyên đề nằm ở những cơ sở khác. Đây là điểm khởi đầu lý tưởng để hiểu tổng quan về vùng đất, con người và lịch sử tỉnh Kirov trước khi khám phá sâu hơn.",
    [
        "Một trong những bảo tàng địa phương học lâu đời nhất nước Nga (thành lập 1866).",
        "Bộ sưu tập lớn về thiên nhiên, khảo cổ, lịch sử và dân tộc học vùng Vyatka.",
        "Mang tên nhà hoạt động P. V. Alabin - người có công sáng lập.",
    ],
    indoor_practical(
        "Mở cửa theo lịch bảo tàng (thường đóng cửa Thứ Hai); nên kiểm tra trước.",
        "Vé vào cửa mức vừa phải tùy khu trưng bày; có vé liên tuyến giữa các chi nhánh.",
        "Khoảng 1-1,5 giờ.",
        "Quanh năm (bảo tàng trong nhà).",
        "Bảo tàng có nhiều chi nhánh - hỏi vé liên tuyến nếu muốn xem cả phần thiên nhiên.",
    ),
    [
        {"title": "Кировский областной краеведческий музей — официальный сайт", "url": "https://muzey43.ru/"},
        {"title": "Culture.ru — Кировский краеведческий музей", "url": "https://www.culture.ru/institutes/search?query=%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BA%D1%80%D0%B0%D0%B5%D0%B2%D0%B5%D0%B4%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BC%D1%83%D0%B7%D0%B5%D0%B9"},
    ],
    ["museum", "local-lore", "history", "ethnography", "nature", "kirov"],
    maps_text("Кировский областной краеведческий музей", "Киров", "Kirov Regional Museum", "Kirov", 58.602048, 49.683681),
    official_site="https://muzey43.ru/",
))

# 9) Музей Циолковского, авиации и космонавтики -------------------------------------
RECORDS.append(rec(
    "tsiolkovsky-aviation-museum-kirov",
    "Bảo tàng Tsiolkovsky, Hàng không và Vũ trụ (Muzey Tsiolkovskogo, aviatsii i kosmonavtiki)",
    "Музей К. Э. Циолковского, авиации и космонавтики",
    "Tsiolkovsky Museum of Aviation and Cosmonautics",
    ["museum"],
    58.605298, 49.678989,
    "Phố Preobrazhenskaya 16, thành phố Kirov 610000, tỉnh Kirov, Nga.",
    "Bảo tàng độc đáo này gắn với Konstantin Tsiolkovsky - 'cha đẻ của du hành vũ trụ' từng sống thời niên thiếu ở Vyatka - và với nhà du hành Viktor Savinykh, người con của tỉnh Kirov. Trưng bày mô hình tên lửa, tàu vũ trụ, đồ dùng phi hành gia và lịch sử hàng không.",
    "Đặt trong ngôi nhà nơi Konstantin Eduardovich Tsiolkovsky - nhà khoa học được coi là 'cha đẻ của ngành du hành vũ trụ lý thuyết' - từng sống cùng gia đình thời niên thiếu ở Vyatka, bảo tàng này là địa chỉ đặc biệt của Kirov dành cho những ai mê bầu trời và không gian. Trưng bày kể lại cuộc đời và ý tưởng tiên phong của Tsiolkovsky về tên lửa và du hành liên hành tinh, đồng thời tôn vinh mối liên hệ của vùng đất Vyatka với ngành vũ trụ Xô Viết - Nga, đặc biệt qua nhà du hành vũ trụ Viktor Savinykh, người sinh ra tại tỉnh Kirov. Khách tham quan được xem mô hình tên lửa và tàu vũ trụ, bộ đồ và thực phẩm phi hành gia, các hiện vật thật gắn với những chuyến bay, cùng phần lịch sử phát triển hàng không. Một số hiện vật liên quan trực tiếp đến các chuyến bay vũ trụ khiến trải nghiệm càng sống động. Đây là điểm đến hấp dẫn cho gia đình có trẻ em và những người quan tâm đến khoa học, công nghệ và lịch sử chinh phục không gian.",
    [
        "Gắn với K. E. Tsiolkovsky - 'cha đẻ du hành vũ trụ' từng sống thời niên thiếu ở Vyatka.",
        "Tôn vinh nhà du hành vũ trụ Viktor Savinykh, người con của tỉnh Kirov.",
        "Trưng bày mô hình tên lửa, tàu vũ trụ, đồ dùng phi hành gia và lịch sử hàng không.",
    ],
    indoor_practical(
        "Mở cửa theo lịch bảo tàng (thường đóng cửa Thứ Hai); nên kiểm tra trước.",
        "Vé vào cửa mức vừa phải; tham quan có hướng dẫn tính thêm.",
        "Khoảng 1 giờ.",
        "Quanh năm (bảo tàng trong nhà); dịp Ngày Vũ trụ 12/4 thường có sự kiện.",
        "Phù hợp gia đình có trẻ; hỏi lịch chương trình chuyên đề về vũ trụ.",
    ),
    [
        {"title": "Culture.ru — Музей К. Э. Циолковского, авиации и космонавтики", "url": "https://www.culture.ru/institutes/search?query=%D0%9C%D1%83%D0%B7%D0%B5%D0%B9%20%D0%A6%D0%B8%D0%BE%D0%BB%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%20%D0%9A%D0%B8%D1%80%D0%BE%D0%B2"},
        {"title": "Кировский областной краеведческий музей — филиалы", "url": "https://muzey43.ru/"},
    ],
    ["museum", "space", "aviation", "science", "family", "kirov"],
    maps_text("Музей Циолковского авиации и космонавтики", "Киров", "Tsiolkovsky Aviation Museum", "Kirov", 58.605298, 49.678989),
))

# 10) Музей «Диорама» ----------------------------------------------------------------
RECORDS.append(rec(
    "vyatka-diorama-kirov",
    "Bảo tàng 'Diorama' (Muzey 'Diorama')",
    "Музей «Диорама»",
    "Diorama Museum",
    ["museum"],
    58.590793, 49.652933,
    "Đại lộ Oktyabrsky 15, thành phố Kirov 610000, tỉnh Kirov, Nga.",
    "Trung tâm trưng bày 'Diorama' nổi bật với bức tranh toàn cảnh (diorama) khổng lồ tái hiện các sự kiện lịch sử Vyatka đầu thế kỷ 20, kết hợp âm thanh - ánh sáng. Toà nhà tròn kiểu hiện đại thập niên 1970 tự thân đã là một điểm nhấn kiến trúc.",
    "Nằm bên đại lộ Oktyabrsky, 'Diorama' là một trung tâm trưng bày - bảo tàng đặc biệt của Kirov, ra đời năm 1977. 'Ngôi sao' của bảo tàng là một bức diorama (tranh toàn cảnh cong kết hợp mô hình vật thể nổi ở tiền cảnh) khổ lớn, tái hiện những biến động lịch sử của vùng Vyatka đầu thế kỷ 20 - đặc biệt là các sự kiện cách mạng và nội chiến - với hiệu ứng âm thanh, ánh sáng thay đổi tạo cảm giác như đang chứng kiến khung cảnh 'sống động' trước mắt. Bản thân toà nhà tròn bằng bê tông kính kiểu kiến trúc hiện đại (modernism) thập niên 1970 cũng là một dấu ấn đô thị dễ nhận biết. Ngoài diorama, nơi đây còn tổ chức các triển lãm chuyên đề, sự kiện văn hoá và chương trình giáo dục. Với du khách, buổi trình diễn diorama là trải nghiệm khác lạ so với bảo tàng thông thường, giúp hình dung sinh động một giai đoạn lịch sử đầy kịch tính của địa phương.",
    [
        "Bức diorama khổng lồ tái hiện sự kiện lịch sử Vyatka đầu thế kỷ 20 với hiệu ứng âm thanh - ánh sáng.",
        "Toà nhà tròn kiến trúc hiện đại (modernism) thập niên 1970 - dấu ấn đô thị Kirov.",
        "Có thêm triển lãm chuyên đề và chương trình giáo dục.",
    ],
    indoor_practical(
        "Mở cửa theo lịch bảo tàng (thường đóng cửa Thứ Hai); buổi chiếu diorama theo suất.",
        "Vé vào cửa mức vừa phải; suất trình diễn diorama nên hỏi giờ trước.",
        "Khoảng 45 phút-1 giờ.",
        "Quanh năm (bảo tàng trong nhà).",
        "Hỏi giờ suất trình diễn diorama; kết hợp dạo khu công viên gần đó.",
    ),
    [
        {"title": "Culture.ru — Диорама, Киров", "url": "https://www.culture.ru/institutes/search?query=%D0%94%D0%B8%D0%BE%D1%80%D0%B0%D0%BC%D0%B0%20%D0%9A%D0%B8%D1%80%D0%BE%D0%B2"},
        {"title": "Кировский областной краеведческий музей — филиалы", "url": "https://muzey43.ru/"},
    ],
    ["museum", "diorama", "history", "modernism", "kirov", "indoor"],
    maps_text("Музей Диорама", "Киров", "Diorama Museum", "Kirov", 58.590793, 49.652933),
))

# 11) Дом-музей М. Е. Салтыкова-Щедрина ---------------------------------------------
RECORDS.append(rec(
    "saltykov-shchedrin-museum-kirov",
    "Nhà - Bảo tàng M. E. Saltykov-Shchedrin (Dom-muzey Saltykova-Shchedrina)",
    "Дом-музей М. Е. Салтыкова-Щедрина",
    "Saltykov-Shchedrin House Museum",
    ["museum"],
    58.596705, 49.681082,
    "Phố Lenina 93, thành phố Kirov 610000, tỉnh Kirov, Nga.",
    "Bảo tàng văn học đặt trong ngôi nhà nơi văn hào châm biếm Mikhail Saltykov-Shchedrin sống những năm bị lưu đày ở Vyatka (1848-1855). Nội thất được phục dựng cùng tư liệu về cuộc đời và sáng tác của ông.",
    "Ngôi nhà gỗ khiêm nhường trên phố Lenina này là nơi nhà văn châm biếm lừng danh Mikhail Evgrafovich Saltykov-Shchedrin đã sống trong những năm bị lưu đày về Vyatka (1848-1855) vì các tác phẩm bị chính quyền Sa hoàng cho là 'nguy hiểm'. Thời gian ở Vyatka để lại dấu ấn sâu đậm trong sáng tác của ông: chính những quan sát về bộ máy quan liêu và đời sống tỉnh lẻ nơi đây đã trở thành chất liệu cho nhiều tác phẩm nổi tiếng sau này. Bảo tàng phục dựng không gian sinh hoạt và làm việc của nhà văn, trưng bày bản thảo, sách, thư từ, ảnh và tư liệu về cuộc đời, sự nghiệp cùng bối cảnh xã hội nước Nga giữa thế kỷ 19. Đây là một trong những bảo tàng văn học đáng chú ý của Kirov, phù hợp với người yêu văn học Nga và muốn tìm hiểu một lát cắt lịch sử - xã hội qua số phận một nhà văn lớn. Không gian nhỏ, yên tĩnh, mang lại cảm giác gần gũi và gợi nhiều suy ngẫm.",
    [
        "Nơi văn hào Saltykov-Shchedrin sống những năm bị lưu đày ở Vyatka (1848-1855).",
        "Nội thất phục dựng cùng bản thảo, thư từ, tư liệu về cuộc đời và sáng tác.",
        "Bảo tàng văn học tiêu biểu của Kirov, không gian ấm cúng và giàu suy tưởng.",
    ],
    indoor_practical(
        "Mở cửa theo lịch bảo tàng (thường đóng cửa Thứ Hai); nên kiểm tra trước.",
        "Vé vào cửa mức vừa phải.",
        "Khoảng 45 phút.",
        "Quanh năm (bảo tàng trong nhà).",
        "Phù hợp người yêu văn học Nga; kết hợp dạo phố Lenina trung tâm.",
    ),
    [
        {"title": "Culture.ru — Дом-музей Салтыкова-Щедрина, Киров", "url": "https://www.culture.ru/institutes/search?query=%D0%A1%D0%B0%D0%BB%D1%82%D1%8B%D0%BA%D0%BE%D0%B2-%D0%A9%D0%B5%D0%B4%D1%80%D0%B8%D0%BD%20%D0%9A%D0%B8%D1%80%D0%BE%D0%B2"},
        {"title": "Кировский областной краеведческий музей — филиалы", "url": "https://muzey43.ru/"},
    ],
    ["museum", "literature", "writer", "history", "kirov", "indoor"],
    maps_text("Дом-музей Салтыкова-Щедрина", "Киров", "Saltykov-Shchedrin House Museum", "Kirov", 58.596705, 49.681082),
))

# 12) Музей-усадьба художников Васнецовых (Рябово) -----------------------------------
RECORDS.append(rec(
    "vasnetsov-estate-ryabovo",
    "Điền trang - Bảo tàng anh em họa sĩ Vasnetsov ở Ryabovo",
    "Музей-усадьба художников Васнецовых",
    "Vasnetsov Artists' Estate Museum (Ryabovo)",
    ["museum"],
    58.198180, 50.798050,
    "Phố Ryabovskaya 3, làng Ryabovo, huyện Zuyevsky, tỉnh Kirov, Nga (cách thành phố Kirov khoảng 90 km về phía đông).",
    "Đây là điền trang quê hương nơi hai danh họa Viktor và Apollinary Vasnetsov lớn lên - con của vị linh mục làng Ryabovo. Nhà - bảo tàng phục dựng nếp sống gia đình nông thôn thế kỷ 19 đã hun đúc nên hai họa sĩ Nga vĩ đại.",
    "Ẩn mình giữa vùng đồi rừng yên bình ở huyện Zuyevsky, làng Ryabovo là nơi ra đời và tuổi thơ của hai anh em họa sĩ trứ danh Viktor Vasnetsov (tác giả 'Ba tráng sĩ', 'Alyonushka') và Apollinary Vasnetsov (bậc thầy tranh lịch sử Moskva cổ). Cha của họ là linh mục làng Ryabovo, và chính khung cảnh làng quê, rừng cây, truyền thuyết dân gian và nếp sống mộc mạc nơi đây đã nuôi dưỡng trí tưởng tượng cổ tích - sử thi thấm đẫm trong tranh của hai ông. Nhà - bảo tàng điền trang phục dựng ngôi nhà của gia đình linh mục cùng nội thất, đồ dùng sinh hoạt và không gian sáng tác, giúp khách hình dung tuổi thơ và cội nguồn cảm hứng của các họa sĩ. Xung quanh là cảnh quan thiên nhiên và các công trình gắn với lịch sử làng. Hằng năm nơi đây tổ chức lễ hội 'Vasnetsovskiy plener' quy tụ họa sĩ về vẽ. Với người yêu hội họa Nga, hành trình về Ryabovo là dịp chạm đến 'nơi bắt đầu' của một dòng họ nghệ sĩ tài hoa, giữa khung cảnh đồng quê thơ mộng đúng như trong tranh.",
    [
        "Điền trang quê hương của hai danh họa Viktor và Apollinary Vasnetsov.",
        "Phục dựng ngôi nhà của gia đình linh mục làng Ryabovo và không gian sáng tác.",
        "Cảnh làng quê, rừng cây - cội nguồn cảm hứng cổ tích, sử thi trong tranh Vasnetsov.",
    ],
    indoor_practical(
        "Mở cửa theo lịch bảo tàng; nên đặt trước, đặc biệt cho đoàn.",
        "Vé vào cửa mức vừa phải; tham quan có hướng dẫn tính thêm.",
        "Khoảng 1-1,5 giờ (chưa kể quãng đường từ Kirov).",
        "Cuối xuân đến đầu thu; dịp lễ hội 'Vasnetsovskiy plener' rất đáng xem.",
        "Ryabovo cách Kirov khoảng 90 km về phía đông, nên đi ô tô hoặc tour; đường vào là vùng nông thôn.",
    ),
    [
        {"title": "Culture.ru — Музей-усадьба художников Васнецовых", "url": "https://www.culture.ru/institutes/search?query=%D0%92%D0%B0%D1%81%D0%BD%D0%B5%D1%86%D0%BE%D0%B2%D1%8B%20%D0%A0%D1%8F%D0%B1%D0%BE%D0%B2%D0%BE"},
        {"title": "Wikipedia (RU) — Рябово (Кировская область)", "url": "https://ru.wikipedia.org/wiki/%D0%A0%D1%8F%D0%B1%D0%BE%D0%B2%D0%BE_(%D0%97%D1%83%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D1%80%D0%B0%D0%B9%D0%BE%D0%BD)"},
    ],
    ["museum", "estate", "art", "vasnetsov", "village", "history"],
    maps_text("Музей-усадьба Васнецовых", "Рябово, Зуевский район", "Vasnetsov Estate Museum", "Ryabovo", 58.198180, 50.798050),
))

# ============================ NHÀ HÁT (theatre) ============================

# 13) Кировский драматический театр им. С. М. Кирова ---------------------------------
RECORDS.append(rec(
    "kirov-drama-theatre",
    "Nhà hát Kịch Tỉnh Kirov (mang tên S. M. Kirov)",
    "Кировский драматический театр им. С. М. Кирова",
    "Kirov Regional Drama Theatre",
    ["theatre"],
    58.604722, 49.668056,
    "Quảng trường Teatralnaya (phố Moskovskaya 37), thành phố Kirov 610000, tỉnh Kirov, Nga.",
    "Nhà hát Kịch Tỉnh Kirov là một trong những đoàn kịch lâu đời của Nga, có gốc từ năm 1877. Toà nhà bề thế theo phong cách tân cổ điển Xô Viết ngự trị Quảng trường Teatralnaya, trung tâm đời sống sân khấu của thành phố.",
    "Ra đời từ năm 1877, Nhà hát Kịch Tỉnh Kirov (Kirovsky dramatichesky teatr) mang tên S. M. Kirov là một trong những sân khấu kịch lâu đời và quan trọng nhất của vùng, giữ vai trò trung tâm đời sống nghệ thuật biểu diễn ở Kirov suốt gần một thế kỷ rưỡi. Toà nhà nhà hát hiện nay - công trình bề thế với hàng cột, mặt tiền đối xứng theo phong cách tân cổ điển Xô Viết - tọa lạc ngay trên Quảng trường Teatralnaya, trở thành một trong những kiến trúc tiêu biểu và bối cảnh quen thuộc của các sự kiện thành phố. Tiết mục của nhà hát trải rộng từ kịch kinh điển Nga (Chekhov, Ostrovsky, Gogol) và thế giới đến các vở đương đại, nhạc kịch và chương trình cho thiếu nhi. Với du khách, một buổi tối xem kịch tại đây không chỉ là thưởng thức nghệ thuật mà còn là cách hoà mình vào nhịp sống văn hoá của người dân Kirov; còn ban ngày, mặt tiền và quảng trường phía trước là điểm dạo bộ, chụp ảnh dễ chịu ở trung tâm.",
    [
        "Đoàn kịch lâu đời của Nga, có gốc từ năm 1877.",
        "Toà nhà tân cổ điển Xô Viết bề thế ngự trị Quảng trường Teatralnaya.",
        "Tiết mục đa dạng: kịch kinh điển Nga - thế giới, vở đương đại và chương trình thiếu nhi.",
    ],
    indoor_practical(
        "Mở theo lịch biểu diễn và giờ bán vé; nên xem lịch trước.",
        "Có bán vé xem kịch; giá tuỳ suất diễn và vị trí ghế.",
        "Buổi diễn thường 2-3 giờ; ngắm mặt tiền khoảng 10-15 phút.",
        "Mùa diễn (thu - xuân); ngắm quảng trường đẹp cả ngày.",
        "Đặt vé trước qua trang chính thức; các vở chủ yếu bằng tiếng Nga.",
    ),
    [
        {"title": "Wikipedia (RU) — Кировский драматический театр", "url": "https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%B4%D1%80%D0%B0%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D1%82%D0%B5%D0%B0%D1%82%D1%80"},
        {"title": "Culture.ru — Кировский драмтеатр им. С. М. Кирова", "url": "https://www.culture.ru/institutes/search?query=%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B4%D1%80%D0%B0%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%82%D0%B5%D0%B0%D1%82%D1%80"},
    ],
    ["theatre", "drama", "culture", "kirov", "architecture", "landmark"],
    maps_text("Кировский драматический театр", "Киров", "Kirov Drama Theatre", "Kirov", 58.604722, 49.668056),
))

# ============================ QUẢNG TRƯỜNG / PHỐ CỔ (square_street) ============================

# 14) Театральная площадь ------------------------------------------------------------
RECORDS.append(rec(
    "teatralnaya-square-kirov",
    "Quảng trường Teatralnaya (Teatralnaya ploshchad)",
    "Театральная площадь",
    "Theatre Square",
    ["square_street"],
    58.604000, 49.668600,
    "Quảng trường Teatralnaya, trung tâm thành phố Kirov, tỉnh Kirov, Nga.",
    "Quảng trường Teatralnaya là quảng trường trung tâm và lớn nhất Kirov - nơi diễn ra các sự kiện, lễ hội, hội chợ và là điểm hẹn quen thuộc. Bao quanh là Nhà hát Kịch, đài phun nước và tượng đài S. M. Kirov.",
    "Nằm ở trái tim thành phố, Quảng trường Teatralnaya (Quảng trường Nhà hát) là không gian công cộng lớn và quan trọng nhất của Kirov - nơi tổ chức các dịp lễ lớn, hòa nhạc ngoài trời, hội chợ, chợ Giáng sinh và là điểm tụ họp, dạo chơi của người dân. Chi phối quảng trường là toà nhà Nhà hát Kịch Tỉnh Kirov với hàng cột tân cổ điển bề thế; phía trước có đài phun nước và không gian rộng lát đá, còn gần đó là tượng đài Sergei Kirov - nhân vật mà thành phố được đặt tên. Vào mùa đông, quảng trường thường dựng cây thông và tiểu cảnh băng tuyết, trở thành trung tâm lễ hội đón năm mới; mùa hè lại là nơi diễn ra các sự kiện văn hoá, thể thao. Với du khách, đây là điểm định vị và khởi đầu tự nhiên để khám phá trung tâm Kirov, đồng thời cảm nhận nhịp sống đô thị và không khí lễ hội của thành phố.",
    [
        "Quảng trường trung tâm và lớn nhất Kirov, nơi diễn ra sự kiện, lễ hội, hội chợ.",
        "Bao quanh có Nhà hát Kịch tân cổ điển, đài phun nước và tượng đài S. M. Kirov.",
        "Trung tâm lễ hội đón năm mới mùa đông với cây thông và tiểu cảnh băng tuyết.",
    ],
    outdoor_practical(
        "Khoảng 20-30 phút.",
        "Chiều mát và buổi tối; mùa đông có không khí lễ hội năm mới.",
        "Điểm khởi đầu khám phá trung tâm; kết hợp Nhà hát Kịch và phố Spasskaya gần đó.",
        hours="Không gian mở, dạo chơi tự do mọi lúc.",
        ticket="Miễn phí.",
    ),
    [
        {"title": "Wikipedia (RU) — Театральная площадь (Киров)", "url": "https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D0%B0%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D0%BF%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D1%8C_(%D0%9A%D0%B8%D1%80%D0%BE%D0%B2)"},
        {"title": "Кировская область — туристический портал", "url": "https://www.kirovreg.ru/"},
    ],
    ["square", "city-center", "kirov", "landmark", "events", "free"],
    maps_text("Театральная площадь", "Киров", "Theatre Square", "Kirov", 58.604000, 49.668600),
))

# 15) Улица Спасская -----------------------------------------------------------------
RECORDS.append(rec(
    "spasskaya-street-kirov",
    "Phố Spasskaya ('Arbat của Vyatka', ulitsa Spasskaya)",
    "Улица Спасская",
    "Spasskaya Street",
    ["square_street"],
    58.602090, 49.676750,
    "Phố Spasskaya (đoạn đi bộ), trung tâm lịch sử thành phố Kirov, tỉnh Kirov, Nga.",
    "Phố Spasskaya là con phố cổ đẹp và giàu bản sắc nhất Kirov, được ví như 'Arbat của Vyatka'. Đoạn đi bộ lát đá với những dinh thự thương gia thế kỷ 19, quán cà phê, cửa hàng lưu niệm và nhiều bảo tàng nhỏ nằm san sát.",
    "Chạy qua lõi lịch sử của Kirov, phố Spasskaya là tuyến phố cổ được yêu thích nhất thành phố và thường được người dân gọi thân mật là 'Arbat của Vyatka'. Đoạn phố đi bộ lát đá được chỉnh trang gìn giữ dáng dấp cuối thế kỷ 19 - đầu thế kỷ 20, hai bên là những dinh thự thương gia, nhà buôn và công trình công cộng cổ với mặt tiền trang trí đẹp mắt. Dọc phố tập trung nhiều điểm đến văn hoá - du lịch: Bảo tàng Mỹ thuật Vasnetsov, Bảo tàng Địa phương học, Vyatka Kunstkamera, Bảo tàng Sô-cô-la 'Criollo'... xen kẽ với quán cà phê, tiệm bánh, cửa hàng đồ thủ công và lưu niệm (đặc biệt là tượng Dymkovo). Đây là nơi lý tưởng để đi bộ thong dong, ngắm kiến trúc, thưởng thức ẩm thực địa phương và cảm nhận không khí đô thị tỉnh lẻ Nga thanh bình. Vào các dịp lễ, phố thường có biểu diễn đường phố, hội chợ thủ công và trang trí rực rỡ, trở thành 'phòng khách ngoài trời' của Kirov.",
    [
        "Phố cổ đi bộ đẹp nhất Kirov, được ví như 'Arbat của Vyatka'.",
        "Dinh thự thương gia thế kỷ 19, quán cà phê, cửa hàng thủ công và lưu niệm.",
        "Tập trung nhiều bảo tàng: Mỹ thuật Vasnetsov, Địa phương học, Kunstkamera, Sô-cô-la.",
    ],
    outdoor_practical(
        "Khoảng 1-1,5 giờ (thong dong, ghé quán và bảo tàng).",
        "Chiều mát và buổi tối; dịp lễ có biểu diễn đường phố, hội chợ.",
        "Tuyến khám phá trung tâm lý tưởng; mua tượng Dymkovo và đồ thủ công làm quà.",
        hours="Không gian mở, dạo chơi tự do mọi lúc.",
        ticket="Miễn phí (dạo phố); các bảo tàng dọc phố thu vé riêng.",
    ),
    [
        {"title": "Wikipedia (RU) — Спасская улица (Киров)", "url": "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B0%D1%81%D1%81%D0%BA%D0%B0%D1%8F_%D1%83%D0%BB%D0%B8%D1%86%D0%B0_(%D0%9A%D0%B8%D1%80%D0%BE%D0%B2)"},
        {"title": "Кировская область — туристический портал", "url": "https://www.kirovreg.ru/"},
    ],
    ["street", "pedestrian", "historic", "kirov", "walking", "shopping"],
    maps_text("Улица Спасская", "Киров", "Spasskaya Street", "Kirov", 58.602090, 49.676750),
))

# 16) Город Слободской (Соборная площадь / колокольня) ------------------------------
RECORDS.append(rec(
    "slobodskoy-town",
    "Thị trấn cổ Slobodskoy (Slobodskoy)",
    "Город Слободской",
    "Slobodskoy Historic Town",
    ["square_street"],
    58.731980, 50.184500,
    "Quảng trường Sobornaya (khu trung tâm), thành phố Slobodskoy, tỉnh Kirov, Nga (cách thành phố Kirov khoảng 35 km về phía đông bắc).",
    "Slobodskoy là thị trấn thương mại cổ bên sông Vyatka, gần như còn nguyên vẹn quần thể phố cổ thế kỷ 18-19. Biểu tượng của thị trấn là tháp chuông cao của nhà thờ Chúa Biến Hình cùng nhà nguyện gỗ cổ trên Quảng trường Sobornaya - nơi được cho là nhà thờ gỗ cổ nhất tỉnh Kirov.",
    "Cách thành phố Kirov khoảng 35 km về phía đông bắc, bên bờ sông Vyatka, Slobodskoy là một trong những thị trấn cổ kính và được bảo tồn tốt nhất tỉnh Kirov. Từng là trung tâm buôn bán, thủ công và làm chuông sầm uất, thị trấn còn giữ được quần thể trung tâm lịch sử với nhiều dinh thự thương gia, dãy phố buôn (gostiny dvor) và nhà thờ thế kỷ 18-19. Trên Quảng trường Sobornaya nổi bật tháp chuông cao của nhà thờ Chúa Biến Hình (Spaso-Preobrazhensky) với chiếc đồng hồ cổ, cùng nhà nguyện Mikhail Tổng lãnh thiên thần bằng gỗ - được xem là công trình gỗ cổ nhất còn lại của vùng, thậm chí từng được đưa đi trưng bày ở Paris. Slobodskoy cũng là quê hương của nhiều nhân vật nổi tiếng và gắn với tuổi thơ của nhà văn Aleksandr Grin (tác giả 'Cánh buồm đỏ thắm'). Dạo bộ trong thị trấn, du khách như lạc vào một 'bảo tàng ngoài trời' của kiến trúc tỉnh lẻ Nga: những con phố yên tĩnh, nhà cổ, nhà thờ và khung cảnh ven sông thanh bình, rất khác nhịp sống thành phố.",
    [
        "Thị trấn thương mại cổ ven sông Vyatka với quần thể phố cổ thế kỷ 18-19 gần nguyên vẹn.",
        "Tháp chuông nhà thờ Chúa Biến Hình và nhà nguyện gỗ cổ trên Quảng trường Sobornaya.",
        "Gắn với nghề làm chuông và tuổi thơ nhà văn Aleksandr Grin.",
    ],
    outdoor_practical(
        "Khoảng 2-3 giờ dạo bộ trung tâm thị trấn.",
        "Cuối xuân đến đầu thu để dạo phố và ven sông; mùa đông cảnh tuyết cổ kính.",
        "Slobodskoy cách Kirov khoảng 35 km, tiện đi trong ngày bằng ô tô hoặc xe khách; nhiều nhà thờ mở theo giờ lễ.",
        hours="Không gian đô thị ngoài trời, dạo chơi tự do; các nhà thờ/bảo tàng mở theo giờ riêng.",
        ticket="Miễn phí (dạo phố); một số nhà thờ và bảo tàng thu phí riêng.",
    ),
    [
        {"title": "Wikipedia (RU) — Слободской", "url": "https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D0%BE%D0%B1%D0%BE%D0%B4%D1%81%D0%BA%D0%BE%D0%B9"},
        {"title": "Кировская область — туристический портал", "url": "https://www.kirovreg.ru/"},
    ],
    ["historic-town", "architecture", "river", "grin", "kirov-oblast", "heritage"],
    maps_text("Соборная площадь", "Слободской", "Slobodskoy Cathedral Square", "Slobodskoy", 58.731980, 50.184500),
))

# ============================ ĐÀI TƯỞNG NIỆM (monument) ============================

# 17) Вечный огонь -------------------------------------------------------------------
RECORDS.append(rec(
    "eternal-flame-kirov",
    "Ngọn lửa Vĩnh cửu và Đài tưởng niệm (Vechny ogon)",
    "Вечный огонь",
    "Eternal Flame Memorial",
    ["monument"],
    58.603970, 49.689940,
    "Bờ sông Grin (naberezhnaya Grina), trung tâm thành phố Kirov, tỉnh Kirov, Nga.",
    "Đài tưởng niệm Ngọn lửa Vĩnh cửu trên bờ cao sông Vyatka tưởng nhớ những người con Kirov đã ngã xuống trong Chiến tranh Vệ quốc Vĩ đại. Đây là nơi diễn ra các nghi lễ trọng thể và là điểm tưởng niệm thiêng liêng của thành phố.",
    "Nằm trên bờ cao sông Vyatka, cạnh Vườn Aleksandrovsky và bờ sông Grin, Đài tưởng niệm Ngọn lửa Vĩnh cửu là địa điểm tưởng niệm trang nghiêm nhất của Kirov dành cho những người con của vùng đất đã hy sinh trong Chiến tranh Vệ quốc Vĩ đại (1941-1945). Ngọn lửa cháy không ngừng bên các phiến đá và bảng khắc tên là biểu tượng của lòng biết ơn và ký ức không phai. Vào các dịp trọng đại - đặc biệt là Ngày Chiến thắng 9/5 - nơi đây diễn ra các nghi lễ đặt hoa, diễu hành và tưởng niệm với sự tham gia của đông đảo người dân, cựu chiến binh và học sinh; thanh thiếu niên thường đứng gác danh dự bên ngọn lửa. Không gian mở, hướng ra dòng sông, khiến đài tưởng niệm vừa trang nghiêm vừa gắn với cảnh quan đẹp của trung tâm thành phố. Đây là điểm dừng ý nghĩa để hiểu thêm về lịch sử và tình cảm của người dân Kirov, đồng thời thuận tiện kết hợp trong lộ trình dạo bộ ven sông.",
    [
        "Đài tưởng niệm tưởng nhớ người con Kirov hy sinh trong Chiến tranh Vệ quốc Vĩ đại.",
        "Ngọn lửa cháy không ngừng bên bờ cao sông Vyatka, cạnh Vườn Aleksandrovsky.",
        "Nơi diễn ra nghi lễ trọng thể dịp Ngày Chiến thắng 9/5, có gác danh dự.",
    ],
    outdoor_practical(
        "Khoảng 15-20 phút.",
        "Quanh năm; dịp 9/5 có nghi lễ trang trọng; chiều muộn ngắm sông đẹp.",
        "Giữ thái độ trang nghiêm; kết hợp dạo Vườn Aleksandrovsky và bờ sông Grin liền kề.",
        hours="Không gian mở, viếng tự do mọi lúc.",
        ticket="Miễn phí.",
    ),
    [
        {"title": "Кировская область — туристический портал", "url": "https://www.kirovreg.ru/"},
        {"title": "Wikipedia (RU) — Киров (город)", "url": "https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D1%80%D0%BE%D0%B2_(%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C)"},
    ],
    ["monument", "memorial", "wwii", "eternal-flame", "kirov", "riverside"],
    maps_text("Вечный огонь", "Киров", "Eternal Flame Memorial", "Kirov", 58.603970, 49.689940),
))

# ============================ CẦU (bridge) ============================

# 18) Старый мост через Вятку --------------------------------------------------------
RECORDS.append(rec(
    "old-bridge-kirov",
    "Cầu Cũ qua sông Vyatka (Staryi most)",
    "Старый мост через Вятку",
    "Old Bridge over the Vyatka",
    ["bridge"],
    58.616160, 49.689280,
    "Cầu Cũ (Staryi most) qua sông Vyatka, nối trung tâm Kirov với làng Dymkovo, tỉnh Kirov, Nga.",
    "Cầu Cũ là cây cầu bắc qua sông Vyatka nối trung tâm Kirov với làng Dymkovo bên kia sông - quê hương của đồ chơi Dymkovo. Từ trên cầu và hai đầu cầu, du khách có tầm nhìn đẹp ra dòng sông rộng và toàn cảnh bờ cao thành phố.",
    "Bắc qua dòng Vyatka rộng, Cầu Cũ (Staryi most) là cây cầu kết nối trung tâm lịch sử Kirov trên bờ cao với làng Dymkovo (Dymkovskaya sloboda) ở bờ đối diện - nơi khai sinh loại đồ chơi đất nung Dymkovo nổi tiếng. Trong nhiều thập niên, đây là cây cầu đường bộ chính vượt sông của thành phố (nay được bổ sung bởi cầu mới), gắn với sinh hoạt hằng ngày và ký ức của bao thế hệ cư dân. Với du khách, giá trị của cây cầu nằm ở tầm nhìn: từ trên cầu và các điểm ngắm hai đầu cầu, có thể phóng mắt ra khúc sông mênh mông, bãi bồi, và toàn cảnh bờ cao Kirov với những mái vòm nhà thờ, Vườn Aleksandrovsky nhô lên trên nền cây xanh - đặc biệt đẹp vào lúc hoàng hôn khi mặt sông ánh vàng. Đi bộ hoặc dừng chân trên cầu là cách thú vị để cảm nhận mối liên hệ giữa phố thị và làng nghề Dymkovo, cũng như vẻ đẹp của con sông đã làm nên tên gọi 'Vyatka' cho cả vùng đất.",
    [
        "Cầu qua sông Vyatka nối trung tâm Kirov với làng Dymkovo (quê đồ chơi Dymkovo).",
        "Điểm ngắm toàn cảnh bờ cao thành phố, mái vòm nhà thờ và Vườn Aleksandrovsky.",
        "Cảnh sông rộng đẹp nhất lúc hoàng hôn khi mặt nước ánh vàng.",
    ],
    outdoor_practical(
        "Khoảng 20-30 phút (dừng ngắm cảnh và chụp ảnh).",
        "Chiều muộn mùa hè để ngắm hoàng hôn trên sông Vyatka.",
        "Kết hợp thăm làng Dymkovo bên kia cầu; chú ý an toàn giao thông khi dừng chụp ảnh.",
        hours="Không gian ngoài trời, qua lại tự do mọi lúc.",
        ticket="Miễn phí.",
    ),
    [
        {"title": "Кировская область — туристический портал", "url": "https://www.kirovreg.ru/"},
        {"title": "Wikipedia (RU) — Вятка (река)", "url": "https://ru.wikipedia.org/wiki/%D0%92%D1%8F%D1%82%D0%BA%D0%B0_(%D1%80%D0%B5%D0%BA%D0%B0)"},
    ],
    ["bridge", "river", "viewpoint", "dymkovo", "kirov", "sunset"],
    maps_text("Старый мост", "Киров", "Old Bridge over the Vyatka", "Kirov", 58.616160, 49.689280),
))

# ============================ CÔNG VIÊN / THIÊN NHIÊN (park_garden) ============================

# 19) Ботанический сад ---------------------------------------------------------------
RECORDS.append(rec(
    "botanical-garden-kirov",
    "Vườn Bách thảo Kirov (Botanichesky sad)",
    "Ботанический сад",
    "Kirov Botanical Garden",
    ["park_garden"],
    58.596280, 49.666860,
    "Phố Karla Marksa 95, thành phố Kirov 610000, tỉnh Kirov, Nga.",
    "Vườn Bách thảo Kirov là ốc đảo xanh nhỏ xinh giữa trung tâm thành phố, lập từ năm 1912. Với hồ nước, hang giả, đài phun nước, nhà kính và bộ sưu tập cây cỏ đa dạng, đây là nơi dạo bộ và thư giãn được yêu thích.",
    "Được một đại tá về hưu là A. A. Istomin lập nên từ năm 1912 trên một khu đất nhỏ ở trung tâm Vyatka, Vườn Bách thảo (nay thuộc Đại học Tổng hợp Vyatka) là một trong những ốc đảo xanh cổ và duyên dáng nhất của Kirov. Dù diện tích không lớn, khu vườn được bố trí khéo léo với hồ nước, cầu nhỏ, hang giả (grotto) bằng đá, đài phun nước, các luống hoa và bộ sưu tập cây cối phong phú - từ cây bản địa đến nhiều loài ngoại nhập, cây cảnh và thực vật nhà kính nhiệt đới. Nhà kính (oranzhereya) cho phép ngắm cây xanh và hoa ngay cả trong mùa đông giá lạnh. Không gian yên tĩnh, nhiều bóng mát và tiểu cảnh khiến vườn trở thành điểm dạo bộ, chụp ảnh và nghỉ ngơi lý tưởng cho gia đình, các cặp đôi và cả những ai muốn tạm rời phố xá. Vào mùa ấm, các luống hoa nở rộ tạo nên khung cảnh rực rỡ; vườn cũng thường tổ chức các hoạt động giáo dục về thực vật. Đây là một điểm đến nhẹ nhàng, đáng ghé trong hành trình khám phá trung tâm Kirov.",
    [
        "Vườn bách thảo lập từ năm 1912, ốc đảo xanh giữa trung tâm Kirov.",
        "Hồ nước, hang giả, đài phun nước, luống hoa và nhà kính cây nhiệt đới.",
        "Không gian yên tĩnh, nhiều bóng mát, lý tưởng để dạo bộ và chụp ảnh.",
    ],
    outdoor_practical(
        "Khoảng 45 phút-1 giờ.",
        "Cuối xuân đến đầu thu khi hoa nở; nhà kính ngắm được cả mùa đông.",
        "Vé vào cửa mức thấp; kết hợp dạo trung tâm và các bảo tàng lân cận.",
        hours="Mở cửa ban ngày theo lịch (thường mở hằng ngày trong mùa ấm); nên kiểm tra giờ nhà kính.",
        ticket="Vé vào cửa mức thấp; nhà kính có thể tính phí riêng.",
    ),
    [
        {"title": "Wikipedia (RU) — Ботанический сад (Киров)", "url": "https://ru.wikipedia.org/wiki/%D0%91%D0%BE%D1%82%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%B0%D0%B4_(%D0%9A%D0%B8%D1%80%D0%BE%D0%B2)"},
        {"title": "Кировская область — туристический портал", "url": "https://www.kirovreg.ru/"},
    ],
    ["botanical-garden", "park", "greenhouse", "family", "kirov", "nature"],
    maps_text("Ботанический сад", "Киров", "Kirov Botanical Garden", "Kirov", 58.596280, 49.666860),
))

# 20) Кочуровский парк ---------------------------------------------------------------
RECORDS.append(rec(
    "kochurovsky-park-kirov",
    "Công viên Kochurovsky (Kochurovsky park)",
    "Кочуровский парк",
    "Kochurovsky Park",
    ["park_garden"],
    58.592483, 49.602439,
    "Khu Yugo-Zapad (Tây Nam), quận Leninsky, thành phố Kirov, tỉnh Kirov, Nga.",
    "Kochurovsky là công viên cảnh quan lớn ở khu tây nam Kirov, với chuỗi hồ, khe suối, đồi dốc và rừng cây. Đây là nơi dạo bộ, chạy bộ, đạp xe và nghỉ ngơi giữa thiên nhiên được người dân địa phương yêu thích.",
    "Trải rộng trên vùng khe suối và đồi dốc ở khu Yugo-Zapad (Tây Nam) của Kirov, Công viên Kochurovsky là một trong những mảng xanh - cảnh quan lớn của thành phố, mang tính chất một công viên rừng - hồ tự nhiên hơn là công viên trang trí. Điểm đặc trưng là chuỗi hồ, ao nối nhau theo dòng suối Khlynovka cùng những sườn dốc phủ cây, tạo nên địa hình nhấp nhô và nhiều góc nhìn đẹp. Người dân đến đây để đi bộ, chạy bộ, đạp xe, câu cá, dã ngoại; mùa đông có thể trượt tuyết, trượt băng trên các sườn dốc và mặt hồ đóng băng. Không khí trong lành, cây cối rậm rạp và mặt nước phản chiếu khiến công viên là nơi 'nạp năng lượng' và tránh xa ồn ào đô thị. Dù nằm hơi xa trung tâm lịch sử, Kochurovsky là lựa chọn thú vị cho du khách muốn cảm nhận đời sống thường nhật của người Kirov và tận hưởng thiên nhiên ngay trong lòng thành phố. Khu vực cũng dần được đầu tư thêm lối đi dạo và tiện ích công cộng.",
    [
        "Công viên cảnh quan lớn ở tây nam Kirov với chuỗi hồ, khe suối và đồi dốc.",
        "Nơi đi bộ, chạy bộ, đạp xe, dã ngoại và trượt tuyết mùa đông của người dân.",
        "Không gian rừng - hồ tự nhiên, trong lành, tránh xa ồn ào đô thị.",
    ],
    outdoor_practical(
        "Khoảng 1-1,5 giờ (dạo bộ, nghỉ ngơi).",
        "Cuối xuân đến đầu thu cho dạo bộ, dã ngoại; mùa đông cho hoạt động tuyết.",
        "Mang giày phù hợp địa hình dốc; kết hợp thư giãn nếu ở khu tây nam thành phố.",
        hours="Không gian ngoài trời, dạo chơi tự do mọi lúc.",
        ticket="Miễn phí.",
    ),
    [
        {"title": "Кировская область — туристический портал", "url": "https://www.kirovreg.ru/"},
        {"title": "Wikipedia (RU) — Киров (город)", "url": "https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D1%80%D0%BE%D0%B2_(%D0%9A%D0%B8%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C)"},
    ],
    ["park", "lake", "outdoor", "walking", "kirov", "nature"],
    maps_text("Кочуровский парк", "Киров", "Kochurovsky Park", "Kirov", 58.592483, 49.602439),
))

# 21) Государственный природный заповедник «Нургуш» ---------------------------------
RECORDS.append(rec(
    "nurgush-nature-reserve",
    "Khu bảo tồn thiên nhiên Nurgush (zapovednik 'Nurgush')",
    "Государственный природный заповедник «Нургуш»",
    "Nurgush Nature Reserve",
    ["park_garden"],
    57.948460, 48.337950,
    "Trụ sở khu bảo tồn: phố Sadovaya 37, làng Borovka, huyện Kotelnichsky, tỉnh Kirov, Nga.",
    "Nurgush là khu bảo tồn thiên nhiên nghiêm ngặt của tỉnh Kirov, bảo vệ vùng rừng ngập nước và hệ hồ móng ngựa ven sông Vyatka gần Kotelnich. Đây là 'vương quốc' của rừng nguyên sinh, đầm lầy, chim nước và nhiều loài quý hiếm.",
    "Được thành lập năm 1994, Khu bảo tồn thiên nhiên nhà nước 'Nurgush' bảo vệ một trong những vùng rừng ngập nước (poyma) còn nguyên vẹn và giàu sinh học nhất tỉnh Kirov, nằm ở hạ lưu sông Vyatka gần thành phố Kotelnich (phân khu chính 'Nurgush'). Đặc trưng của khu là hệ thống dày đặc các hồ móng ngựa (starnitsa) - dấu tích những khúc sông cũ - xen giữa rừng sồi, đoạn, tần bì và các cánh đồng cỏ ngập nước theo mùa. Đây là nơi cư trú và làm tổ của nhiều loài chim nước, chim ăn thịt, cùng các loài thú như hải ly, rái cá, nai sừng tấm; nhiều loài động - thực vật quý hiếm được ghi trong Sách Đỏ. Về sau khu bảo tồn được mở rộng thêm phân khu 'Tulashor' ở vùng rừng taiga phía bắc tỉnh, bảo vệ rừng lá kim ít bị tác động. Là vùng lõi bảo tồn nghiêm ngặt, việc vào tham quan phải theo tuyến sinh thái được phép và có hướng dẫn/đăng ký trước; khu bảo tồn có trung tâm thông tin và các chương trình giáo dục môi trường. Với người yêu thiên nhiên hoang dã và quan sát chim, Nurgush là điểm đến độc đáo để khám phá hệ sinh thái sông - rừng đặc trưng của vùng Vyatka.",
    [
        "Khu bảo tồn nghiêm ngặt bảo vệ rừng ngập nước và hệ hồ móng ngựa ven sông Vyatka.",
        "Nơi cư trú của hải ly, rái cá, nai sừng tấm, nhiều chim nước và loài trong Sách Đỏ.",
        "Có phân khu rừng taiga 'Tulashor' ở phía bắc tỉnh; tham quan theo tuyến sinh thái có phép.",
    ],
    outdoor_practical(
        "Nửa ngày trở lên tùy tuyến sinh thái.",
        "Cuối xuân đến đầu thu để quan sát chim và cây cỏ; nước lũ mùa xuân có thể hạn chế lối vào.",
        "PHẢI đăng ký trước và đi theo tuyến/hướng dẫn của khu bảo tồn; mang giày lội nước, chống muỗi; trụ sở ở làng Borovka gần Kotelnich.",
        hours="Vùng lõi bảo tồn - chỉ vào theo tuyến sinh thái được phép, có đăng ký/hướng dẫn.",
        ticket="Vào các tuyến sinh thái thường thu phí và cần đăng ký trước với ban quản lý.",
    ),
    [
        {"title": "Wikipedia (RU) — Нургуш (заповедник)", "url": "https://ru.wikipedia.org/wiki/%D0%9D%D1%83%D1%80%D0%B3%D1%83%D1%88_(%D0%B7%D0%B0%D0%BF%D0%BE%D0%B2%D0%B5%D0%B4%D0%BD%D0%B8%D0%BA)"},
        {"title": "Заповедник «Нургуш» — официальный сайт", "url": "https://nurgush.org/"},
    ],
    ["nature-reserve", "wetland", "birdwatching", "forest", "kirov-oblast", "wildlife"],
    maps_text("Заповедник Нургуш", "Боровка, Котельничский район", "Nurgush Nature Reserve", "Kirov Oblast", 57.948460, 48.337950),
    official_site="https://nurgush.org/",
))

# 22) Озеро Шайтан -------------------------------------------------------------------
RECORDS.append(rec(
    "shaitan-lake",
    "Hồ Shaitan (ozero Shaytan)",
    "Озеро Шайтан",
    "Lake Shaitan",
    ["park_garden"],
    57.096220, 49.462170,
    "Di tích thiên nhiên hồ Shaitan, gần làng Indygoyka, phía nam tỉnh Kirov, Nga (khu vực Urzhum/Lebyazhye).",
    "Hồ Shaitan là di tích thiên nhiên kỳ bí bậc nhất tỉnh Kirov, nổi tiếng với những 'đảo nổi' trôi trên mặt nước và hiện tượng phun trào nước bất chợt như mạch phun. Hồ có nguồn gốc karst, nằm giữa rừng, gắn nhiều truyền thuyết dân gian.",
    "Ẩn giữa rừng ở phía nam tỉnh Kirov, hồ Shaitan (tên gọi mang nghĩa 'quỷ' trong tiếng Turk) là một trong những di tích thiên nhiên độc đáo và bí ẩn nhất của vùng. Hồ có nguồn gốc karst - hình thành do nước ngầm hòa tan lớp đá vôi bên dưới - với đáy phễu sâu và mạch nước ngầm mạnh. Hai hiện tượng khiến hồ nổi danh khắp nước Nga: thứ nhất là những 'đảo nổi' - các mảng đất phủ cây bụi, thậm chí cây nhỏ, tách khỏi bờ và trôi lững lờ trên mặt nước, di chuyển theo gió; thứ hai là hiện tượng nước bất chợt phun vọt lên thành cột cao vài mét như mạch phun (do áp lực nước ngầm), xảy ra không báo trước. Chính sự kỳ lạ ấy đã sinh ra nhiều truyền thuyết dân gian về 'thần hồ' và khiến người xưa vừa nể sợ vừa tôn kính. Ngày nay hồ được xếp hạng di tích thiên nhiên và là điểm đến hấp dẫn cho du khách ưa khám phá, dã ngoại và chụp ảnh giữa khung cảnh rừng nguyên sơ. Do nằm khá xa và đường vào là vùng nông thôn - rừng, chuyến đi tới Shaitan thường được tổ chức theo tour hoặc bằng xe cá nhân gầm cao.",
    [
        "Di tích thiên nhiên nổi tiếng với 'đảo nổi' trôi trên mặt nước và hiện tượng nước phun.",
        "Hồ nguồn gốc karst, đáy phễu sâu, mạch nước ngầm mạnh, nằm giữa rừng.",
        "Gắn nhiều truyền thuyết dân gian về 'thần hồ', cảnh quan nguyên sơ, kỳ bí.",
    ],
    outdoor_practical(
        "Khoảng 1,5-2 giờ tại hồ (chưa kể quãng đường xa, nên đi trong ngày).",
        "Cuối xuân đến đầu thu; hiện tượng nước phun xảy ra bất chợt, không đoán trước được.",
        "Nên đi theo tour hoặc xe gầm cao; mang chống muỗi, nước; giữ gìn khu vực di tích thiên nhiên.",
        hours="Đối tượng thiên nhiên ngoài trời, tham quan ban ngày; không có giờ cố định.",
        ticket="Vào tự do (khu ngoài trời); có thể phát sinh phí tour/hướng dẫn.",
    ),
    [
        {"title": "Wikipedia (RU) — Шайтан (озеро)", "url": "https://ru.wikipedia.org/wiki/%D0%A8%D0%B0%D0%B9%D1%82%D0%B0%D0%BD_(%D0%BE%D0%B7%D0%B5%D1%80%D0%BE)"},
        {"title": "Кировская область — туристический портал", "url": "https://www.kirovreg.ru/"},
    ],
    ["lake", "natural-monument", "karst", "floating-islands", "kirov-oblast", "nature"],
    maps_text("Озеро Шайтан", "Кировская область", "Lake Shaitan", "Kirov Oblast", 57.096220, 49.462170),
))

# 23) Береснятский водопад -----------------------------------------------------------
RECORDS.append(rec(
    "beresnyatsky-waterfall",
    "Thác Beresnyatsky và vách đá Burzhatsky (Beresnyatsky vodopad)",
    "Береснятский водопад",
    "Beresnyatsky Waterfall",
    ["park_garden"],
    57.388060, 49.029850,
    "Trên sông Nemda, gần làng Chimbulat/Fokino, huyện Sovetsky, tỉnh Kirov, Nga.",
    "Thác Beresnyatsky là thác nước đẹp và cao vào bậc nhất tỉnh Kirov, nước đổ nhiều bậc xuống thung lũng sông Nemda. Gần đó là vách đá Burzhatsky sừng sững - cùng tạo thành quần thể cảnh quan thiên nhiên hùng vĩ hiếm có của vùng.",
    "Nằm trong khu cảnh quan thiên nhiên độc đáo bên sông Nemda thuộc huyện Sovetsky, thác Beresnyatsky (Beresnyatsky vodopad) là một trong những thác nước đẹp và ấn tượng nhất tỉnh Kirov - vùng vốn địa hình bằng phẳng nên thác nước là điều hiếm gặp. Dòng suối nhỏ từ trên cao đổ xuống thung lũng sông Nemda qua nhiều bậc đá, tổng độ cao đáng kể, tạo nên dải nước trắng xoá len giữa rừng cây và vách đá vôi - đặc biệt mạnh và đẹp vào mùa xuân khi tuyết tan. Ngay gần thác là vách đá Burzhatsky (Burzhatsky utyos) - một bức tường đá vôi dựng đứng cao hàng chục mét bên sông, điểm ngắm cảnh và leo trèo ưa thích. Cả khu vực thuộc vùng cảnh quan 'Bảy đồi/Skały' ven Nemda với nhiều tảng đá kỳ vĩ, hang hốc và di chỉ khảo cổ, được bảo vệ như di tích thiên nhiên. Đây là điểm đến hấp dẫn cho những ai yêu đi bộ đường dài, thiên nhiên hoang sơ và nhiếp ảnh phong cảnh, mang lại trải nghiệm 'núi rừng' bất ngờ giữa đồng bằng Vyatka. Đường tiếp cận là vùng nông thôn - rừng, nên chuẩn bị kỹ về phương tiện và giày dép.",
    [
        "Thác nước nhiều bậc đẹp và cao bậc nhất tỉnh Kirov, đổ xuống thung lũng sông Nemda.",
        "Gần vách đá vôi Burzhatsky sừng sững - điểm ngắm cảnh và leo trèo.",
        "Nằm trong vùng cảnh quan đá vôi ven Nemda, di tích thiên nhiên hoang sơ.",
    ],
    outdoor_practical(
        "Khoảng 2-3 giờ (đi bộ, ngắm thác và vách đá).",
        "Mùa xuân (tuyết tan) thác mạnh và đẹp nhất; mùa hè dễ đi lại hơn.",
        "Đi giày lội/đi bộ tốt, mang chống muỗi; đường tiếp cận là vùng nông thôn - rừng, nên đi xe gầm cao hoặc tour.",
        hours="Đối tượng thiên nhiên ngoài trời, tham quan ban ngày; không có giờ cố định.",
        ticket="Vào tự do (khu ngoài trời).",
    ),
    [
        {"title": "Wikipedia (RU) — Береснятский водопад", "url": "https://ru.wikipedia.org/wiki/%D0%91%D0%B5%D1%80%D0%B5%D1%81%D0%BD%D1%8F%D1%82%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%B4%D0%BE%D0%BF%D0%B0%D0%B4"},
        {"title": "Кировская область — туристический портал", "url": "https://www.kirovreg.ru/"},
    ],
    ["waterfall", "cliff", "nemda", "natural-monument", "kirov-oblast", "hiking"],
    maps_text("Береснятский водопад", "Советский район", "Beresnyatsky Waterfall", "Kirov Oblast", 57.388060, 49.029850),
))

# 24) Атарская Лука ------------------------------------------------------------------
RECORDS.append(rec(
    "atarskaya-luka",
    "Khúc uốn Atarskaya Luka (Atarskaya Luka)",
    "Атарская Лука",
    "Atarskaya Luka",
    ["park_garden"],
    57.521670, 49.290000,
    "Khúc uốn lớn của sông Vyatka gần làng Atary, khu Lebyazhye/Sovetsky, tỉnh Kirov, Nga.",
    "Atarskaya Luka là khúc uốn lớn tuyệt đẹp của sông Vyatka với những vách đá cao ven bờ, rừng già và làng cổ Atary hầu như bị bỏ hoang. Đây là di tích thiên nhiên - cảnh quan nổi tiếng, điểm đến cho du lịch bè mảng, đi bộ và nhiếp ảnh.",
    "Ở vùng trung tâm tỉnh Kirov, sông Vyatka uốn thành một khúc cong lớn kỳ vĩ gọi là Atarskaya Luka ('luka' nghĩa là khúc uốn sông). Đây là một trong những đoạn sông đẹp và hoang sơ nhất của cả dòng Vyatka: hai bên là những vách đá và bờ dốc cao phủ rừng già, bãi bồi, đồng cỏ và các mạch suối, tạo nên cảnh quan đa dạng được xếp hạng di tích thiên nhiên - cảnh quan. Trong khu vực có làng Atary cổ nay gần như bị bỏ hoang với nhà thờ đổ nát, mang vẻ đẹp trầm mặc, hoài niệm khiến nơi đây càng thu hút giới nhiếp ảnh và những người tìm kiếm sự tĩnh lặng. Atarskaya Luka là điểm đến quen thuộc cho các chuyến du lịch đường sông (chèo thuyền, bè mảng) xuôi Vyatka, cắm trại, câu cá và đi bộ khám phá; từ các điểm cao ven bờ, tầm nhìn bao quát khúc sông uốn lượn giữa rừng đặc biệt ngoạn mục. Do nằm ở vùng ít dân cư, việc tiếp cận thường qua đường sông hoặc đường đất, phù hợp với du khách ưa trải nghiệm thiên nhiên hoang dã và tự túc.",
    [
        "Khúc uốn lớn kỳ vĩ của sông Vyatka với vách đá cao, rừng già và bãi bồi.",
        "Làng cổ Atary gần như bỏ hoang, nhà thờ đổ nát - cảnh quan trầm mặc, hoài niệm.",
        "Điểm đến cho du lịch đường sông (chèo thuyền, bè mảng), cắm trại và nhiếp ảnh.",
    ],
    outdoor_practical(
        "Nửa ngày trở lên; nếu đi tour đường sông có thể nhiều ngày.",
        "Cuối xuân đến đầu thu; mùa hè thuận tiện cho chèo thuyền, cắm trại.",
        "Tiếp cận qua đường sông hoặc đường đất, nên đi tour/xe gầm cao và chuẩn bị tự túc; giữ gìn khu di tích thiên nhiên.",
        hours="Đối tượng thiên nhiên ngoài trời, tham quan ban ngày; không có giờ cố định.",
        ticket="Vào tự do (khu ngoài trời).",
    ),
    [
        {"title": "Wikipedia (RU) — Атарская Лука", "url": "https://ru.wikipedia.org/wiki/%D0%90%D1%82%D0%B0%D1%80%D1%81%D0%BA%D0%B0%D1%8F_%D0%9B%D1%83%D0%BA%D0%B0"},
        {"title": "Кировская область — туристический портал", "url": "https://www.kirovreg.ru/"},
    ],
    ["river-bend", "cliff", "natural-monument", "abandoned-village", "kirov-oblast", "rafting"],
    maps_text("Атарская Лука", "Кировская область", "Atarskaya Luka", "Kirov Oblast", 57.521670, 49.290000),
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
