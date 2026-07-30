# -*- coding: utf-8 -*-
"""_add_places_chechnya_20260728.py — VÙNG: Cộng hòa Chechnya (Чеченская Республика)
(lần chạy tự động 2026-07-28).

Bối cảnh: chechnya.json hiện có 7 địa điểm. Bổ sung 24 địa điểm THẬT SỰ nổi tiếng/đặc
sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 31 (≥30, mục tiêu 31–32).

7 địa điểm đã có (KHÔNG trùng): heart-of-chechnya-mosque, grozny-city-towers,
pride-of-muslims-mosque-shali, lake-kezenoyam, ushkaloy-towers, nikaroy-tower-complex,
argun-mosque-mother-of-hearts.

Phân bố loại hình (24 bản ghi mới):
- museum (2): Национальный музей ЧР, Этнографический музей «Донди-Юрт» (Урус-Мартан).
- monument (1): Мемориальный комплекс Славы им. А. А. Кадырова.
- theatre (3): Драмтеатр им. Х. Нурадилова, ТЮЗ, Филармония им. А. Шахбулатова.
- square_street (1): Проспект В. В. Путина.
- park_garden (7): Цветочный парк, Грозненское море, Аргунское ущелье, Нихалоевские
  водопады, Галанчожское озеро, Бенойские водопады, водопад «Девичья коса» (Харачой).
- other (5): Национальная библиотека ЧР, Ахмат-Арена, Дворец танца «Вайнах»,
  курорт «Ведучи», гора Тебулосмта.
- fortress (4): Пхакоч (Итум-Кали), Цой-Педе (город мёртвых), село Хой, Веденская крепость.
- church/мечеть (1): мечеть/зиярат Ташу-Хаджи (Саясан).

TOẠ ĐỘ — xác minh chéo (2ГИС org/geo og:image center lon,lat → đảo lat,lon; ru.wikipedia
geo / academic.ru ruwiki mirror; openkavkaz; tourister; sputnik8; culture.ru; 2026-07-28).
Phạm vi Chechnya: lat ~42,5–44,5; lon ~44,8–46,7 — TẤT CẢ nằm trong phạm vi, KHÔNG đảo:
  Нацмузей 43.324061,45.682748 (2ГИС geo); Мемориал Славы 43.326204,45.678796 (2ГИС firm,
  Назарбаева 9в); Драмтеатр Нурадилова 43.323670,45.683356 (Угрюмова 73); ТЮЗ 43.320849,
  45.689444 (б-р Эсамбаева 9); Филармония 43.319101,45.698725 (Лорсанова 31); пр. Путина
  43.3170,45.6980 (điểm giữa đại diện); Цветочный парк 43.313919,45.698646 (Шерипова 12/21);
  Грозненское море 43.267802,45.665691 (2ГИС geo, Чернореченское вдхр); Нацбиблиотека
  43.324171,45.684730 (Угрюмова 75); Ахмат-Арена 43.323643,45.746142 (Льва Яшина 21); Дворец
  танца Вайнах 43.323311,45.696660 (Митаева 10); Аргунское ущелье 42.778122,45.617753 (đoạn
  Ушкалой, điểm đại diện); Нихалоевские водопады 42.839971,45.666855; Пхакоч 42.728689,
  45.571863 (2ГИС geo, Итум-Кали); Цой-Педе 42.707760,45.258350 (ru.wiki); Хой 42.750984,
  46.127223 (gần Кезеной-Ам); Ведучи 42.681471,45.573762; Галанчож 42.872160,45.303880
  (openkavkaz); Беной 42.977427,46.309420; Ведено 42.961601,46.103840; Донди-Юрт 43.122360,
  45.536599 (Урус-Мартан, điểm trung tâm đại diện); Ташу-Хаджи Саясан 43.061192,46.284940;
  Тебулосмта 42.573333,45.311944 (đỉnh 4492 m); Девичья коса Харачой 42.910278,46.140000.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.
Lưu ý văn hoá: mô tả tôn trọng, khách quan; nhắc du khách ăn mặc kín đáo khi vào nhà thờ
Hồi giáo/thánh tích.

Chạy:  python3 tools/_add_places_chechnya_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "chechnya"
REGION_NAME_VI = "Cộng hòa Chechnya"
FD = "Vùng Bắc Kavkaz"


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

# 1) Национальный музей Чеченской Республики -------------------------------------
RECORDS.append(rec(
    "national-museum-chechnya",
    "Bảo tàng Quốc gia Cộng hòa Chechnya",
    "Национальный музей Чеченской Республики",
    "National Museum of the Chechen Republic",
    ["museum"],
    43.324061, 45.682748,
    "Đại lộ Putin (пр. В. В. Путина), khu trung tâm Grozny, Cộng hòa Chechnya, Nga.",
    "Bảo tàng lớn nhất của Chechnya, đặt trong toà nhà hiện đại trang trí mô phỏng tháp canh đá vainakh; nơi lưu giữ lịch sử, khảo cổ, mỹ thuật và văn hoá dân tộc Chechen.",
    "Bảo tàng Quốc gia Cộng hòa Chechnya là bảo tàng trung tâm của vùng, hình thành từ năm 1924 và trải qua nhiều biến động của thế kỷ 20. Phần lớn sưu tập từng bị mất mát, hư hại trong các cuộc xung đột, nhưng những gì còn lại và được phục hồi vẫn đủ kể một câu chuyện phong phú: từ khảo cổ, dân tộc học, những thanh vũ khí lạnh chạm khắc tinh xảo, áo giáp chiến binh trung cổ, cho tới tranh của các danh hoạ Nga như Tropinin và Aivazovsky. Toà nhà mới khang trang được trang trí bằng bản sao các tháp canh đá vainakh — biểu tượng kiến trúc đặc trưng của vùng núi Chechnya. Đội ngũ bảo tàng nổi tiếng nhiệt tình trong việc giới thiệu di sản đã cứu vãn được. Đây là điểm khởi đầu lý tưởng để du khách hiểu bối cảnh lịch sử — văn hoá trước khi khám phá các danh thắng khác của cộng hoà.",
    [
        "Toà nhà hiện đại trang trí mô phỏng tháp canh đá vainakh cổ.",
        "Bộ sưu tập vũ khí lạnh chạm khắc và áo giáp chiến binh trung cổ.",
        "Có tranh của các danh hoạ Nga Tropinin và Aivazovsky.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Là điểm khởi đầu tốt để nắm bối cảnh lịch sử trước khi đi các nơi khác.",
    },
    [
        {"title": "2ГИС — Национальный музей Чеченской Республики, Грозный", "url": "https://2gis.ru/grozny/geo/70030076180673586"},
        {"title": "Культура.РФ — Национальный музей Чеченской Республики", "url": "https://www.culture.ru/institutes/26737/nacionalnyi-muzei-chechenskoi-respubliki"},
    ],
    ["museum", "history", "culture", "grozny", "vainakh"],
    maps_text("Национальный музей Чеченской Республики", "Грозный", "National Museum of the Chechen Republic", "Grozny", 43.324061, 45.682748),
))

# 2) Мемориальный комплекс Славы им. А. А. Кадырова ------------------------------
RECORDS.append(rec(
    "kadyrov-memorial-glory",
    "Quần thể Tưởng niệm Vinh quang mang tên A. A. Kadyrov",
    "Мемориальный комплекс Славы имени А. А. Кадырова",
    "Akhmad Kadyrov Memorial Complex of Glory",
    ["monument"],
    43.326204, 45.678796,
    "Số 9в phố Nursultan Nazarbayev, khu Akhmatovsky, trung tâm Grozny, Cộng hòa Chechnya, Nga.",
    "Quần thể tưởng niệm trang nghiêm ở trung tâm Grozny, tôn vinh chiến thắng trong Thế chiến II và tưởng nhớ tổng thống đầu tiên Akhmad Kadyrov; có bảo tàng và ngọn lửa vĩnh cửu.",
    "Khánh thành năm 2010, Quần thể Tưởng niệm Vinh quang mang tên Akhmad Kadyrov là một trong những công trình tưởng niệm quan trọng nhất Grozny. Quần thể vừa tưởng nhớ những người con Chechnya ngã xuống trong Chiến tranh Vệ quốc Vĩ đại, vừa tôn vinh vị tổng thống đầu tiên của cộng hoà. Trục chính là toà tháp — đài tưởng niệm bằng đá sáng màu, bao quanh là Đại lộ Vinh quang (Аллея Славы) với những hàng cột và bảng tên. Bên trong có bảo tàng trưng bày tư liệu, hiện vật, ảnh về lịch sử vùng, cùng ngọn lửa vĩnh cửu. Nằm giữa các đại lộ trung tâm, đây là nơi diễn ra nhiều nghi lễ nhà nước và là điểm dừng để hiểu ký ức lịch sử của người dân địa phương.",
    [
        "Đài tưởng niệm và Đại lộ Vinh quang (Аллея Славы) trang nghiêm.",
        "Bảo tàng trưng bày tư liệu lịch sử và ngọn lửa vĩnh cửu.",
        "Nằm ở trung tâm Grozny, nơi tổ chức nhiều nghi lễ nhà nước.",
    ],
    {
        "hours_vi": "Khuôn viên mở cả ngày; bảo tàng theo giờ hành chính.",
        "ticket_vi": "Vào khuôn viên miễn phí; bảo tàng vé bình dân.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Chiều mát hoặc buổi tối khi lên đèn.",
        "tips_vi": "Ăn mặc lịch sự, giữ trật tự tại nơi tưởng niệm.",
    },
    [
        {"title": "2ГИС — Мемориальный комплекс Славы им. А. А. Кадырова", "url": "https://2gis.ru/grozny/firm/70000001029399334"},
        {"title": "Википедия (RU) — Мемориальный комплекс Славы имени Ахмата Кадырова", "url": "https://ru.wikipedia.org/wiki/Мемориальный_комплекс_Славы_имени_Ахмата_Кадырова"},
    ],
    ["monument", "memorial", "war-memory", "grozny"],
    maps_text("Мемориальный комплекс Славы имени Кадырова", "Грозный", "Akhmad Kadyrov Memorial Complex", "Grozny", 43.326204, 45.678796),
))

# 3) Чеченский государственный драматический театр им. Х. Нурадилова -------------
RECORDS.append(rec(
    "nuradilov-drama-theatre",
    "Nhà hát Kịch Quốc gia Chechnya mang tên Kh. Nuradilov",
    "Чеченский государственный драматический театр имени Х. Нурадилова",
    "Chechen State Drama Theatre named after Kh. Nuradilov",
    ["theatre"],
    43.323670, 45.683356,
    "Khu trung tâm Grozny (gần đại lộ Makhmud Esambaev), Cộng hòa Chechnya, Nga.",
    "Nhà hát kịch quốc gia lâu đời nhất Chechnya, mang tên Anh hùng Liên Xô Khanpasha Nuradilov; sân khấu chủ lực của nghệ thuật kịch Chechen.",
    "Thành lập từ đầu thập niên 1930, Nhà hát Kịch Quốc gia Chechnya mang tên Khanpasha Nuradilov là sân khấu kịch nói lâu đời và quan trọng nhất của cộng hoà. Trải qua giai đoạn dân tộc bị lưu đày và phục dựng sau đó, nhà hát vẫn giữ vai trò trung tâm trong đời sống văn hoá, dàn dựng cả kịch cổ điển thế giới, kịch Nga lẫn các vở dựa trên văn học và truyền thống Chechen. Đoàn kịch biểu diễn bằng tiếng Chechen và tiếng Nga, góp phần gìn giữ ngôn ngữ và bản sắc dân tộc. Toà nhà nằm ở khu trung tâm Grozny, gần các công trình biểu tượng. Đây là lựa chọn thú vị cho du khách muốn tiếp cận nghệ thuật biểu diễn đương đại của vùng.",
    [
        "Nhà hát kịch lâu đời và quan trọng nhất Chechnya.",
        "Dàn dựng cả kịch cổ điển thế giới lẫn tác phẩm dựa trên văn hoá Chechen.",
        "Trình diễn bằng tiếng Chechen và tiếng Nga.",
    ],
    {
        "hours_vi": "Theo lịch diễn (thường buổi tối).",
        "ticket_vi": "Vé theo từng suất diễn.",
        "duration_vi": "Khoảng 2–3 giờ mỗi buổi.",
        "best_time_vi": "Kiểm tra lịch diễn (afisha) trước khi đến.",
        "tips_vi": "Đặt vé trước; đến sớm để ổn định chỗ ngồi.",
    },
    [
        {"title": "Культура.РФ — Чеченский госдрамтеатр им. Х. Нурадилова", "url": "https://www.culture.ru/institutes/10672/chechenskii-gosudarstvennyi-dramaticheskii-teatr-im-kh-nuradilova"},
        {"title": "2ГИС — Грозный (карта города)", "url": "https://2gis.ru/grozny"},
    ],
    ["theatre", "culture", "performing-arts", "grozny"],
    maps_text("Чеченский драматический театр им. Нурадилова", "Грозный", "Chechen State Drama Theatre", "Grozny", 43.323670, 45.683356),
))

# 4) Чеченский государственный театр юного зрителя (ТЮЗ) -------------------------
RECORDS.append(rec(
    "tyuz-grozny",
    "Nhà hát Khán giả Trẻ (ТЮЗ) Chechnya",
    "Чеченский государственный театр юного зрителя",
    "Chechen State Theatre for Young Audiences (TYUZ)",
    ["theatre"],
    43.320849, 45.689444,
    "Số 9 đại lộ Makhmud Esambaev, khu Akhmatovsky, Grozny, Cộng hòa Chechnya, Nga.",
    "Nhà hát dành cho thiếu nhi và thanh thiếu niên ở Grozny, dàn dựng các vở diễn giáo dục, cổ tích và kịch cho gia đình.",
    "Nhà hát Khán giả Trẻ (ТЮЗ) của Chechnya là sân khấu chuyên phục vụ thiếu nhi, thanh thiếu niên và các gia đình. Chương trình gồm những vở cổ tích, kịch thiếu nhi, tác phẩm mang tính giáo dục và cả các vở dựa trên văn học dân gian vainakh. Với không gian ấm cúng nằm trên đại lộ mang tên nghệ sĩ múa lừng danh Makhmud Esambaev, nhà hát là điểm đến quen thuộc của các gia đình địa phương vào cuối tuần. Đây cũng là nơi ươm mầm thẩm mỹ và tình yêu sân khấu cho thế hệ trẻ. Với du khách đi cùng trẻ em, một buổi diễn ở đây có thể là trải nghiệm văn hoá nhẹ nhàng, gần gũi.",
    [
        "Nhà hát chuyên phục vụ thiếu nhi và gia đình.",
        "Có các vở dựa trên văn học dân gian vainakh.",
        "Nằm trên đại lộ mang tên nghệ sĩ múa Makhmud Esambaev.",
    ],
    {
        "hours_vi": "Theo lịch diễn (nhiều suất vào cuối tuần).",
        "ticket_vi": "Vé bình dân.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Cuối tuần.",
        "tips_vi": "Phù hợp gia đình có trẻ nhỏ; kiểm tra lịch diễn trước.",
    },
    [
        {"title": "Культура.РФ — Чеченский государственный театр юного зрителя", "url": "https://www.culture.ru/institutes/12316/chechenskii-gosudarstvennyi-teatr-yunogo-zritelya"},
        {"title": "2ГИС — Грозный (карта города)", "url": "https://2gis.ru/grozny"},
    ],
    ["theatre", "family", "children", "grozny"],
    maps_text("Театр юного зрителя", "Грозный", "Theatre for Young Audiences", "Grozny", 43.320849, 45.689444),
))

# 5) Государственная филармония ЧР им. А. Шахбулатова ----------------------------
RECORDS.append(rec(
    "chechen-philharmonic",
    "Nhà hát Giao hưởng Quốc gia Chechnya mang tên A. Shakhbulatov",
    "Государственная филармония Чеченской Республики имени Аднана Шахбулатова",
    "Chechen State Philharmonic named after Adnan Shakhbulatov",
    ["theatre"],
    43.319101, 45.698725,
    "Khu trung tâm Grozny (gần phố Lorsanov), Cộng hòa Chechnya, Nga.",
    "Trung tâm âm nhạc hàn lâm và dân tộc của Chechnya, mang tên nhạc sĩ Adnan Shakhbulatov; nơi tổ chức hoà nhạc giao hưởng và các chương trình dân ca - dân vũ vainakh.",
    "Nhà hát Giao hưởng (Филармония) Quốc gia Cộng hòa Chechnya mang tên nhạc sĩ Adnan Shakhbulatov là trung tâm biểu diễn âm nhạc chủ chốt của vùng. Nơi đây tổ chức hoà nhạc giao hưởng, âm nhạc thính phòng, các chương trình dân ca — dân vũ vainakh và nhiều sự kiện văn hoá lớn. Các tập thể nghệ thuật trực thuộc vừa gìn giữ, phát triển di sản âm nhạc dân tộc Chechen, vừa trình diễn dòng nhạc hàn lâm châu Âu. Toà nhà biểu diễn khang trang ở trung tâm Grozny là địa chỉ quen thuộc của khán giả yêu nhạc. Với du khách, một buổi hoà nhạc dân tộc tại đây mở ra cánh cửa cảm nhận tâm hồn âm nhạc của người Chechen.",
    [
        "Trung tâm âm nhạc hàn lâm và dân tộc của Chechnya.",
        "Có các chương trình dân ca - dân vũ vainakh đặc sắc.",
        "Mang tên nhạc sĩ Adnan Shakhbulatov.",
    ],
    {
        "hours_vi": "Theo lịch diễn.",
        "ticket_vi": "Vé theo từng chương trình.",
        "duration_vi": "Khoảng 1,5–2 giờ.",
        "best_time_vi": "Xem lịch diễn (afisha) trước.",
        "tips_vi": "Các đêm dân ca - dân vũ rất đáng xem.",
    },
    [
        {"title": "2ГИС — Грозный (карта города)", "url": "https://2gis.ru/grozny"},
        {"title": "Википедия (RU) — Грозный", "url": "https://ru.wikipedia.org/wiki/Грозный"},
    ],
    ["theatre", "music", "philharmonic", "culture", "grozny"],
    maps_text("Государственная филармония Чеченской Республики", "Грозный", "Chechen State Philharmonic", "Grozny", 43.319101, 45.698725),
))

# 6) Проспект В. В. Путина -------------------------------------------------------
RECORDS.append(rec(
    "putin-avenue",
    "Đại lộ Putin (Prospekt V. V. Putina)",
    "Проспект В. В. Путина",
    "Vladimir Putin Avenue",
    ["square_street"],
    43.3170, 45.6980,
    "Trục phố trung tâm Grozny, Cộng hòa Chechnya, Nga (toạ độ là điểm giữa đại diện).",
    "Đại lộ trung tâm sầm uất của Grozny, trục chính nối các biểu tượng thành phố như nhà thờ Trái tim Chechnya và tổ hợp Grozny-City.",
    "Đại lộ Putin (Проспект В. В. Путина) là một trong những trục đường chính và sầm uất nhất trung tâm Grozny. Con phố rộng rãi, sạch sẽ, hai bên là các toà nhà hành chính, khách sạn, cửa hàng, quán cà phê cùng những khu vườn hoa được chăm chút. Đây là nơi người dân và du khách dạo bộ, đặc biệt vào buổi tối khi đèn chiếu sáng làm nổi bật kiến trúc hiện đại của thành phố tái thiết. Đại lộ kết nối nhiều điểm biểu tượng như nhà thờ Hồi giáo 'Trái tim Chechnya', tổ hợp cao ốc Grozny-City và các quảng trường trung tâm. Đi dọc đại lộ là cách tốt để cảm nhận diện mạo mới của thủ phủ Chechnya.",
    [
        "Trục phố trung tâm sầm uất, sạch đẹp của Grozny.",
        "Nối nhiều biểu tượng: Trái tim Chechnya, Grozny-City.",
        "Đặc biệt lung linh khi lên đèn buổi tối.",
    ],
    {
        "hours_vi": "Cả ngày (không gian công cộng).",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Dạo bộ khoảng 30–60 phút.",
        "best_time_vi": "Chiều tối khi lên đèn.",
        "tips_vi": "Kết hợp tham quan các điểm dọc phố; toạ độ chỉ mang tính điểm giữa đại diện.",
    },
    [
        {"title": "Википедия (RU) — Грозный", "url": "https://ru.wikipedia.org/wiki/Грозный"},
        {"title": "2ГИС — Грозный (карта города)", "url": "https://2gis.ru/grozny"},
    ],
    ["square_street", "promenade", "city-center", "grozny"],
    maps_text("Проспект Путина", "Грозный", "Putin Avenue", "Grozny", 43.3170, 45.6980),
))

# 7) Цветочный парк -------------------------------------------------------------
RECORDS.append(rec(
    "flower-park-grozny",
    "Công viên Hoa (Tsvetochny Park)",
    "Цветочный парк",
    "Flower Park (Grozny)",
    ["park_garden"],
    43.313919, 45.698646,
    "Số 12/21 phố Aslanbek Sheripov, trung tâm Grozny (cạnh Grozny-City), Cộng hòa Chechnya, Nga.",
    "Công viên hoa rực rỡ ở trung tâm Grozny cạnh Grozny-City, còn gọi là 'Công viên tình yêu' hay 'Công viên điều kỳ diệu'; điểm dạo chơi, chụp ảnh yêu thích.",
    "Khai trương năm 2017, Công viên Hoa (Цветочный парк) là một không gian xanh — hoa rực rỡ rộng khoảng 4,5 ha ngay trung tâm Grozny, sát tổ hợp cao ốc Grozny-City. Người dân còn gọi nơi đây là 'Công viên điều kỳ diệu' hay 'Công viên của những đôi tình nhân'. Công viên nổi bật với các luống hoa nhiều màu được tạo hình công phu, đài phun nước, lối đi lát đá, ghế nghỉ và những tiểu cảnh trang trí để chụp ảnh. Mở cửa suốt ngày đêm, đây là nơi lý tưởng để thư giãn, đi dạo buổi tối và ngắm khung cảnh cao ốc lên đèn phản chiếu trên nền hoa. Với du khách, công viên là điểm dừng nhẹ nhàng giữa hành trình khám phá trung tâm thủ phủ.",
    [
        "Công viên hoa rộng ~4,5 ha ngay cạnh Grozny-City.",
        "Nhiều luống hoa tạo hình, đài phun nước, tiểu cảnh chụp ảnh.",
        "Mở cửa cả ngày đêm, đẹp nhất khi lên đèn buổi tối.",
    ],
    {
        "hours_vi": "Mở cửa 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–60 phút.",
        "best_time_vi": "Mùa ấm và buổi tối.",
        "tips_vi": "Mang máy ảnh; kết hợp tham quan Grozny-City gần đó.",
    },
    [
        {"title": "2ГИС — Цветочный парк, Грозный", "url": "https://2gis.ru/grozny/geo/70030076167131225"},
        {"title": "Sputnik8 — Цветочный парк, Грозный", "url": "https://www.sputnik8.com/ru/grozny/sights/flower-park/info"},
    ],
    ["park_garden", "flowers", "family", "grozny", "photo-spot"],
    maps_text("Цветочный парк", "Грозный", "Flower Park", "Grozny", 43.313919, 45.698646),
))

# 8) Грозненское море (Чернореченское водохранилище) ----------------------------
RECORDS.append(rec(
    "grozny-sea-lake",
    "Biển Grozny (hồ chứa Chernorechenskoye)",
    "Грозненское море (Чернореченское водохранилище)",
    "Grozny Sea (Chernorechye Reservoir)",
    ["park_garden"],
    43.267802, 45.665691,
    "Vùng ven phía nam Grozny (gần khu Aldy), Cộng hòa Chechnya, Nga.",
    "Hồ chứa nước lớn ở ngoại ô Grozny, còn gọi là 'Biển Grozny'; điểm nghỉ ngơi, tắm mát và dạo chơi ven nước của người dân thành phố.",
    "'Biển Grozny' (Грозненское море), tên chính thức là hồ chứa Chernorechenskoye, được tạo thành năm 1961 bằng một con đập dài hơn 800 m trên sông. Mặt nước rộng khoảng một trăm hecta nhanh chóng trở thành nơi nghỉ ngơi ưa thích của cư dân thành phố, chỉ cách trung tâm Grozny khoảng 15 phút xe. Vào mùa hè, các bãi ven hồ đông người tới tắm mát, dạo chơi, câu cá và dã ngoại; gần hồ còn có công viên cây xanh (dendropark). Không gian thoáng đãng, mặt nước phẳng lặng phản chiếu bầu trời tạo cảm giác thư thái, khác hẳn nhịp sống đô thị. Đây là điểm đến dễ chịu cho du khách muốn tận hưởng thiên nhiên gần thành phố.",
    [
        "Hồ chứa rộng ~100 ha, 'biển' của cư dân Grozny.",
        "Bãi tắm, câu cá, dã ngoại mùa hè; có công viên cây xanh gần đó.",
        "Chỉ cách trung tâm Grozny khoảng 15 phút xe.",
    ],
    {
        "hours_vi": "Cả ngày.",
        "ticket_vi": "Miễn phí (một số dịch vụ có thu phí).",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Mùa hè.",
        "tips_vi": "Mang đồ dã ngoại; kiểm tra khu vực được phép tắm.",
    },
    [
        {"title": "2ГИС — Грозненское море, Грозный", "url": "https://2gis.ru/grozny/geo/70030076167166117"},
        {"title": "kavkaz.travel — Грозненское море", "url": "https://kavkaz.travel/attractions/117/groznenskoe-more"},
    ],
    ["park_garden", "lake", "recreation", "grozny", "nature"],
    maps_text("Грозненское море", "Грозный", "Grozny Sea reservoir", "Grozny", 43.267802, 45.665691),
))

# 9) Национальная библиотека ЧР им. А. Айдамирова -------------------------------
RECORDS.append(rec(
    "national-library-chechnya",
    "Thư viện Quốc gia Chechnya mang tên A. Aydamirov",
    "Национальная библиотека Чеченской Республики имени А. А. Айдамирова",
    "National Library of the Chechen Republic",
    ["other"],
    43.324171, 45.684730,
    "Khu trung tâm Grozny, Cộng hòa Chechnya, Nga.",
    "Thư viện Quốc gia Chechnya mang tên nhà văn Abuzar Aydamirov, đặt trong toà nhà cao tầng hiện đại ở trung tâm Grozny; trung tâm tri thức và văn hoá của cộng hoà.",
    "Thư viện Quốc gia Cộng hòa Chechnya mang tên nhà văn Abuzar Aydamirov là thư viện lớn nhất và quan trọng nhất của vùng. Sau khi phần lớn quỹ sách bị phá huỷ trong xung đột, thư viện được xây dựng lại trong một toà nhà cao tầng hiện đại ở trung tâm Grozny và dần khôi phục kho tư liệu đồ sộ. Nơi đây không chỉ lưu giữ sách, báo, tài liệu về Chechnya và thế giới mà còn là trung tâm sự kiện văn hoá, triển lãm, gặp gỡ văn học và không gian học tập. Kiến trúc hiện đại cùng tầm nhìn từ các tầng cao khiến toà nhà trở thành một điểm nhấn đô thị. Với du khách quan tâm văn hoá, đây là nơi cảm nhận đời sống trí thức đương đại của thủ phủ.",
    [
        "Thư viện lớn nhất Chechnya, mang tên nhà văn Abuzar Aydamirov.",
        "Toà nhà cao tầng hiện đại, điểm nhấn kiến trúc trung tâm Grozny.",
        "Trung tâm sự kiện văn hoá, triển lãm và học tập.",
    ],
    {
        "hours_vi": "Giờ hành chính; nghỉ Chủ nhật/ngày lễ.",
        "ticket_vi": "Miễn phí vào tham quan khu chung.",
        "duration_vi": "Khoảng 30 phút.",
        "best_time_vi": "Ngày thường.",
        "tips_vi": "Mang giấy tờ tuỳ thân nếu muốn dùng dịch vụ thư viện.",
    },
    [
        {"title": "2ГИС — Национальная библиотека ЧР, Грозный", "url": "https://2gis.ru/grozny"},
        {"title": "Википедия (RU) — Грозный", "url": "https://ru.wikipedia.org/wiki/Грозный"},
    ],
    ["other", "library", "culture", "architecture", "grozny"],
    maps_text("Национальная библиотека Чеченской Республики", "Грозный", "National Library of the Chechen Republic", "Grozny", 43.324171, 45.684730),
))

# 10) Стадион «Ахмат-Арена» -----------------------------------------------------
RECORDS.append(rec(
    "akhmat-arena",
    "Sân vận động Akhmat-Arena",
    "Стадион «Ахмат-Арена»",
    "Akhmat Arena Stadium",
    ["other"],
    43.323643, 45.746142,
    "Số 21 phố Lev Yashin, phía đông Grozny, Cộng hòa Chechnya, Nga.",
    "Sân vận động chính của Grozny, sân nhà của CLB bóng đá Akhmat Grozny; công trình thể thao hiện đại sức chứa hơn 30.000 chỗ.",
    "'Akhmat-Arena' là sân vận động lớn nhất Chechnya và là sân nhà của câu lạc bộ bóng đá Akhmat Grozny thi đấu ở giải hạng cao nhất nước Nga. Khánh thành năm 2011, sân có sức chứa hơn 30.000 khán giả, thiết kế hiện đại với mái che và hệ thống chiếu sáng đạt chuẩn. Xung quanh sân là quần thể thể thao gồm các cơ sở tập luyện và không gian công cộng. Vào những ngày có trận đấu, không khí cổ vũ sôi động phản ánh tình yêu bóng đá mạnh mẽ của người dân địa phương. Với du khách yêu thể thao, một trận đấu tại đây là dịp hoà mình vào đời sống đương đại của thành phố; ngoài ngày thi đấu, công trình vẫn là một điểm mốc kiến trúc đáng chú ý.",
    [
        "Sân vận động hiện đại sức chứa hơn 30.000 chỗ.",
        "Sân nhà của CLB bóng đá Akhmat Grozny.",
        "Nằm trong quần thể thể thao ở phía đông thành phố.",
    ],
    {
        "hours_vi": "Theo lịch thi đấu/sự kiện.",
        "ticket_vi": "Vé theo từng trận đấu/sự kiện.",
        "duration_vi": "Khoảng 2 giờ (một trận đấu).",
        "best_time_vi": "Ngày có trận đấu.",
        "tips_vi": "Mua vé trước; kiểm tra lịch giải đấu.",
    },
    [
        {"title": "2ГИС — Ахмат-Арена, Грозный", "url": "https://2gis.ru/grozny"},
        {"title": "Википедия (RU) — Ахмат-Арена", "url": "https://ru.wikipedia.org/wiki/Ахмат-Арена"},
    ],
    ["other", "sport", "stadium", "football", "grozny"],
    maps_text("Стадион Ахмат-Арена", "Грозный", "Akhmat Arena Stadium", "Grozny", 43.323643, 45.746142),
))

# 11) Дворец танца «Вайнах» -----------------------------------------------------
RECORDS.append(rec(
    "vaynakh-dance-palace",
    "Cung Điện Múa 'Vainakh'",
    "Дворец танца «Вайнах»",
    "Vainakh Dance Palace",
    ["other"],
    43.323311, 45.696660,
    "Khu trung tâm Grozny (gần đại lộ Putin), Cộng hòa Chechnya, Nga.",
    "'Cung Điện Múa Vainakh' ở Grozny, nơi biểu diễn của Đoàn Múa Dân gian Quốc gia 'Vainakh' trứ danh; sân khấu tôn vinh nghệ thuật múa Chechen.",
    "Cung Điện Múa 'Vainakh' (Дворец танца «Вайнах») là nơi hoạt động của Đoàn Múa Dân gian Hàn lâm Quốc gia 'Vainakh' — một trong những đoàn nghệ thuật múa nổi tiếng nhất vùng Bắc Kavkaz, từng lưu diễn khắp thế giới. Sân khấu tại đây thường xuyên trình diễn các điệu múa dân gian Chechnya và Kavkaz như lezginka đầy khí phách, cùng những chương trình nghệ thuật công phu về trang phục, âm nhạc và vũ đạo. Toà nhà biểu diễn hiện đại nằm ở khu trung tâm Grozny, gần đại lộ Putin. Với du khách, một buổi diễn của 'Vainakh' là cơ hội hiếm để chứng kiến tinh hoa nghệ thuật múa vainakh — nơi hội tụ sức mạnh, sự uyển chuyển và niềm tự hào dân tộc.",
    [
        "Nơi biểu diễn của Đoàn Múa Dân gian Quốc gia 'Vainakh' lừng danh.",
        "Các điệu múa Kavkaz đầy khí phách như lezginka.",
        "Trang phục, âm nhạc và vũ đạo công phu, giàu bản sắc.",
    ],
    {
        "hours_vi": "Theo lịch diễn.",
        "ticket_vi": "Vé theo từng suất diễn.",
        "duration_vi": "Khoảng 1,5–2 giờ.",
        "best_time_vi": "Xem lịch diễn (afisha) trước.",
        "tips_vi": "Đặt vé trước cho các chương trình lớn.",
    },
    [
        {"title": "2ГИС — Дворец танца «Вайнах», Грозный", "url": "https://2gis.ru/grozny"},
        {"title": "Википедия (RU) — Вайнах (ансамбль)", "url": "https://ru.wikipedia.org/wiki/Вайнах_(ансамбль)"},
    ],
    ["other", "dance", "folk", "culture", "grozny"],
    maps_text("Дворец танца Вайнах", "Грозный", "Vainakh Dance Palace", "Grozny", 43.323311, 45.696660),
))

# 12) Аргунское ущелье ----------------------------------------------------------
RECORDS.append(rec(
    "argun-gorge",
    "Hẻm núi Argun (Argunskoye Ushchelye)",
    "Аргунское ущелье",
    "Argun Gorge",
    ["park_garden"],
    42.778122, 45.617753,
    "Dọc sông Chanty-Argun, các huyện Shatoy và Itum-Kali, vùng núi Chechnya, Nga (toạ độ đại diện đoạn Ushkaloy).",
    "Hẻm núi Argun hùng vĩ - 'trái tim' của vùng núi Chechnya, nơi dòng Chanty-Argun xẻ qua dãy Kavkaz giữa những vách đá dựng đứng, tháp cổ và làng mạc.",
    "Hẻm núi Argun (Аргунское ущелье) là một trong những cảnh quan thiên nhiên — lịch sử ngoạn mục nhất Chechnya, nơi dòng sông Chanty-Argun cuộn chảy xẻ qua các dãy núi Kavkaz tạo thành một hành lang đá dài hun hút. Con đường men theo hẻm núi dẫn du khách qua những vách đá dựng đứng, thác nước, rừng và hàng loạt di tích tháp canh, tháp chiến vainakh cổ nằm rải rác trên sườn núi. Đoạn hẹp và nổi tiếng nhất là nơi có cụm tháp Ushkaloy dựng sát vách đá. Cả khu vực nằm trong Khu bảo tồn lịch sử — kiến trúc và thiên nhiên Argun, gìn giữ di sản kiến trúc đá độc đáo của người Chechen. Đây là tuyến đường không thể bỏ qua với ai muốn cảm nhận vẻ đẹp núi non và chiều sâu lịch sử của vùng.",
    [
        "Hẻm núi sâu nơi sông Chanty-Argun xẻ qua dãy Kavkaz.",
        "Rải rác tháp canh, tháp chiến vainakh cổ trên sườn núi.",
        "Nằm trong Khu bảo tồn lịch sử - kiến trúc và thiên nhiên Argun.",
    ],
    {
        "hours_vi": "Cả ngày (đường núi).",
        "ticket_vi": "Miễn phí (một số điểm tham quan thu phí nhỏ).",
        "duration_vi": "Nửa ngày đến cả ngày (tuyến dài).",
        "best_time_vi": "Cuối xuân đến đầu thu.",
        "tips_vi": "Đi xe gầm cao; mang giấy tờ (khu vực gần biên giới có thể cần đăng ký).",
    },
    [
        {"title": "Википедия (RU) — Аргунское ущелье", "url": "https://ru.wikipedia.org/wiki/Аргунское_ущелье"},
        {"title": "Аргунский музей-заповедник (Википедия RU)", "url": "https://ru.wikipedia.org/wiki/Аргунский_музей-заповедник"},
    ],
    ["park_garden", "canyon", "mountains", "nature", "argun"],
    maps_text("Аргунское ущелье", "Чечня", "Argun Gorge", "Chechnya", 42.778122, 45.617753),
))

# 13) Нихалоевские водопады -----------------------------------------------------
RECORDS.append(rec(
    "nikhaloy-waterfalls",
    "Thác Nikhaloy (Nikhaloyskiye Vodopady)",
    "Нихалоевские водопады",
    "Nikhaloy Waterfalls",
    ["park_garden"],
    42.839971, 45.666855,
    "Gần làng Nikhaloy, huyện Shatoy (hẻm Argun), vùng núi Chechnya, Nga.",
    "Chuỗi thác Nikhaloy nhiều tầng bên hẻm Argun gần làng Nikhaloy, thác cao nhất tới 32 m; điểm dừng thiên nhiên nổi tiếng trên đường lên vùng núi.",
    "Thác Nikhaloy (Нихалойские/Нихалоевские водопады) là một quần thể thác nước nhiều tầng nằm trên một nhánh phải của sông Chanty-Argun, gần làng Nikhaloy thuộc khu vực hẻm núi Argun. Cả cụm gồm nhiều dòng thác lớn nhỏ: thác thấp nhất chỉ khoảng 2 m, còn thác cao nhất đổ xuống từ độ cao tới 32 m giữa vách đá phủ rêu và cây. Để thuận tiện tham quan, khu vực đã được lắp cầu thang, lối đi và cầu vượt giúp du khách men theo các tầng thác. Nằm cách Grozny khoảng 60 km trên tuyến đường lên vùng núi, đây là điểm dừng chân mát lành, thích hợp chụp ảnh và nghỉ ngơi. Xung quanh có cơ sở lưu trú, ăn uống phục vụ khách du lịch.",
    [
        "Chuỗi thác nhiều tầng, cao nhất tới 32 m.",
        "Có cầu thang, lối đi thuận tiện men theo các tầng thác.",
        "Cách Grozny ~60 km trên đường lên hẻm Argun.",
    ],
    {
        "hours_vi": "Ban ngày.",
        "ticket_vi": "Phí nhỏ hoặc miễn phí tuỳ điểm.",
        "duration_vi": "Khoảng 30–60 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu (nước nhiều).",
        "tips_vi": "Mang giày chống trượt; kết hợp cụm tháp Ushkaloy gần đó.",
    },
    [
        {"title": "Википедия (RU) — Нихалоевские водопады", "url": "https://ru.wikipedia.org/wiki/Нихалоевские_водопады"},
        {"title": "Tourister — Нихалойские водопады", "url": "https://www.tourister.ru/world/europe/russia/city/nikhaloy/waterfall/45949"},
    ],
    ["park_garden", "waterfall", "nature", "argun", "mountains"],
    maps_org("https://yandex.com/maps/org/nikhaloyskiye_vodopady/146806420519/", "Nikhaloy Waterfalls", "Chechnya"),
))

# 14) Пхакоч (Итум-Кали) --------------------------------------------------------
RECORDS.append(rec(
    "itum-kale-phakoch",
    "Quần thể tháp cổ Pkhakoch, Itum-Kali",
    "Историко-архитектурный комплекс Пхакоч",
    "Phakoch Tower Complex (Itum-Kali)",
    ["fortress"],
    42.728689, 45.571863,
    "Rìa nam làng Itum-Kali, huyện Itum-Kali (hẻm Argun), vùng núi Chechnya, Nga.",
    "Quần thể lâu đài - tháp cổ Pkhakoch bên rìa làng Itum-Kali, có tháp chiến, tháp ở, cối xay nước và bảo tàng địa phương trưng bày vũ khí, đồ dùng cổ.",
    "Pkhakoch (Пхакоч) là một quần thể thành — tháp trung cổ, niên đại khoảng thế kỷ 11–15, nằm ở rìa nam làng Itum-Kali trong vùng hẻm Argun. Quần thể gồm nhiều tháp ở, một tháp chiến, cối xay nước và các công trình đá được bao quanh bởi tường thành, tiêu biểu cho kiến trúc pháo đài của người vainakh xưa. Bên trong một trong các tháp là bảo tàng địa phương trưng bày vũ khí cổ, vật dụng sinh hoạt và công cụ lao động hàng trăm năm tuổi; tầng trên có khu tưởng niệm dành cho chính khách Khusein Isaev. Quá trình trùng tu đã giữ lại nhiều yếu tố kiến trúc cổ, kể cả các hình khắc trên đá. Đây là một trong những điểm đến lịch sử — kiến trúc quan trọng nhất khi khám phá vùng núi Chechnya.",
    [
        "Quần thể thành - tháp trung cổ (thế kỷ 11-15) của người vainakh.",
        "Có bảo tàng trưng bày vũ khí, vật dụng và công cụ cổ.",
        "Giữ lại nhiều yếu tố kiến trúc gốc và hình khắc trên đá.",
    ],
    {
        "hours_vi": "Ban ngày (nên hỏi trước).",
        "ticket_vi": "Vé nhỏ vào bảo tàng.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Mùa ấm.",
        "tips_vi": "Kết hợp tuyến hẻm Argun và Itum-Kali; đường núi cần xe phù hợp.",
    },
    [
        {"title": "2ГИС — Историко-архитектурный комплекс Пхакоч, Итум-Кали", "url": "https://2gis.ru/geo/70030076445264475"},
        {"title": "Википедия (RU) — Пхакоч", "url": "https://ru.wikipedia.org/wiki/Пхакоч"},
    ],
    ["fortress", "tower", "medieval", "museum", "itum-kali"],
    maps_text("Историко-архитектурный комплекс Пхакоч", "Итум-Кали", "Phakoch complex", "Itum-Kali", 42.728689, 45.571863),
))

# 15) Цой-Педе (город мёртвых) --------------------------------------------------
RECORDS.append(rec(
    "tsoy-pede-necropolis",
    "Cố mộ Tsoy-Pede ('Thành phố người chết')",
    "Цой-Педе (Город мёртвых)",
    "Tsoy-Pede Necropolis (City of the Dead)",
    ["fortress"],
    42.707760, 45.258350,
    "Thượng nguồn hẻm Malkhista, gần hợp lưu Chanty-Argun và Meshi-khi, huyện Itum-Kali, Chechnya, Nga.",
    "'Thành phố của người chết' Tsoy-Pede ở thượng nguồn hẻm Malkhista - một trong những nghĩa địa (necropolis) trung cổ lớn nhất Kavkaz với hàng chục hầm mộ đá và tháp.",
    "Tsoy-Pede (Цой-Педе, tiếng Chechen nghĩa gần với 'thành của thần linh' hay 'thành phố người chết') là một quần thể mộ táng trung cổ nằm ở thượng nguồn hẻm Malkhista, gần nơi hợp lưu của hai dòng Chanty-Argun và Meshi-khi, cách Itum-Kali khoảng 40 km về phía tây nam. Đây là một trong những necropolis lớn và ấn tượng nhất vùng Bắc Kavkaz, gồm hàng chục hầm mộ đá xây trên sườn đồi cùng những tháp canh, tháp thờ vươn lên giữa khung cảnh núi non hoang sơ. Các hầm mộ có ô cửa nhỏ, bên trong từng lưu giữ hài cốt và di vật, phản ánh tập tục an táng cổ xưa của người vainakh. Năm 2024, di tích được đưa vào danh sách dự bị đề cử Di sản Thế giới UNESCO của Nga. Nằm sát vùng biên giới, đây là điểm đến độc đáo, giàu chiều sâu lịch sử và tâm linh.",
    [
        "Một trong những necropolis trung cổ lớn nhất Bắc Kavkaz.",
        "Hàng chục hầm mộ đá cùng tháp canh, tháp thờ trên sườn núi.",
        "Nằm trong danh sách dự bị đề cử Di sản Thế giới UNESCO (2024).",
    ],
    {
        "hours_vi": "Ban ngày.",
        "ticket_vi": "Thường miễn phí (đa số đi theo tour).",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Hè đến đầu thu.",
        "tips_vi": "Khu vực gần biên giới có thể cần giấy phép/đăng ký; nên đi cùng hướng dẫn viên và xe gầm cao.",
    },
    [
        {"title": "Википедия (RU) — Цой-Педе", "url": "https://ru.wikipedia.org/wiki/Цой-Педе"},
        {"title": "kavkaz.travel — Цой-Педе", "url": "https://kavkaz.travel/attractions/122"},
    ],
    ["fortress", "necropolis", "medieval", "unesco-tentative", "itum-kali"],
    maps_text("Цой-Педе", "Итум-Калинский район", "Tsoy-Pede necropolis", "Chechnya", 42.707760, 45.258350),
))

# 16) Село Хой (башенный комплекс) ----------------------------------------------
RECORDS.append(rec(
    "khoy-village",
    "Làng tháp cổ Khoy",
    "Село Хой (Хойский замковый комплекс)",
    "Khoy Tower Village",
    ["fortress"],
    42.750984, 46.127223,
    "Làng Khoy trên núi cao, huyện Vedeno (gần hồ Kezenoy-Am), Chechnya, Nga.",
    "Làng tháp cổ Khoy trên núi cao gần hồ Kezenoy-Am, một 'làng - pháo đài' trung cổ của người vainakh với nhiều tháp ở và tháp canh bằng đá.",
    "Khoy (Хой, nghĩa gần với 'lính canh' trong tiếng Chechen) là một ngôi làng cổ trên vùng núi cao thuộc huyện Vedeno, nằm gần hồ Kezenoy-Am nổi tiếng. Đây từng là một 'làng — pháo đài' chiến lược của người vainakh, án ngữ tuyến đường núi và được xây dựng thành một quần thể gồm nhiều tháp ở, tháp canh cùng nhà đá san sát trên sườn dốc. Trải qua thời gian và những biến động lịch sử, nhiều công trình đã hư hại nhưng vẫn để lại dấu ấn kiến trúc đá đặc trưng; một số đang được phục dựng. Khung cảnh làng cổ giữa núi non trập trùng, gần mặt hồ Kezenoy-Am xanh biếc, tạo nên một trong những bức tranh đẹp và giàu hoài niệm nhất của vùng núi Chechnya. Đây là điểm đến hấp dẫn cho những ai yêu lịch sử và nhiếp ảnh phong cảnh.",
    [
        "'Làng - pháo đài' trung cổ với nhiều tháp đá vainakh.",
        "Nằm trên núi cao, gần hồ Kezenoy-Am tuyệt đẹp.",
        "Cảnh quan làng cổ - núi non giàu chất hoài niệm.",
    ],
    {
        "hours_vi": "Ban ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu.",
        "tips_vi": "Kết hợp hồ Kezenoy-Am; đường núi cần xe phù hợp, mặc ấm.",
    },
    [
        {"title": "Википедия (RU) — Хой (село)", "url": "https://ru.wikipedia.org/wiki/Хой_(село)"},
        {"title": "kavkaz.travel — Хойский комплекс / Кезенойам", "url": "https://kavkaz.travel/attractions"},
    ],
    ["fortress", "tower-village", "medieval", "vedeno", "mountains"],
    maps_text("Село Хой", "Веденский район", "Khoy tower village", "Chechnya", 42.750984, 46.127223),
))

# 17) Всесезонный курорт «Ведучи» -----------------------------------------------
RECORDS.append(rec(
    "veduchi-resort",
    "Khu nghỉ dưỡng - trượt tuyết 'Veduchi'",
    "Всесезонный туристический курорт «Ведучи»",
    "Veduchi All-Season Resort",
    ["other"],
    42.681471, 45.573762,
    "Gần làng Veduchi, huyện Itum-Kali (sườn dãy Kavkaz), Chechnya, Nga.",
    "Khu nghỉ dưỡng - trượt tuyết quanh năm 'Veduchi' trên sườn dãy Kavkaz ở huyện Itum-Kali; khu du lịch núi hiện đại đầu tiên của Chechnya.",
    "'Veduchi' (Ведучи) là khu phức hợp du lịch — nghỉ dưỡng quanh năm nằm ở vùng núi cao huyện Itum-Kali, trên sườn dãy Kavkaz gần làng Veduchi. Đây là khu trượt tuyết và du lịch núi hiện đại đầu tiên được phát triển ở Chechnya, thuộc mạng lưới các khu nghỉ dưỡng du lịch Bắc Kavkaz. Vào mùa đông, Veduchi phục vụ trượt tuyết với đường trượt, cáp treo và cơ sở lưu trú; các mùa còn lại nơi đây hướng tới du lịch sinh thái, đi bộ đường dài và nghỉ dưỡng giữa cảnh quan núi non trong lành. Với hạ tầng khách sạn, nhà hàng và dịch vụ ngày càng hoàn thiện, Veduchi trở thành điểm đến mới thu hút du khách muốn kết hợp thể thao, thiên nhiên và khám phá vùng cao Chechnya.",
    [
        "Khu trượt tuyết - du lịch núi hiện đại đầu tiên của Chechnya.",
        "Mùa đông trượt tuyết; các mùa khác du lịch sinh thái, đi bộ.",
        "Cảnh quan núi Kavkaz trong lành, hạ tầng nghỉ dưỡng đang mở rộng.",
    ],
    {
        "hours_vi": "Theo mùa và dịch vụ.",
        "ticket_vi": "Vé cáp treo/đường trượt theo bảng giá.",
        "duration_vi": "Nửa ngày đến vài ngày.",
        "best_time_vi": "Mùa đông (trượt tuyết), mùa hè (đi bộ đường dài).",
        "tips_vi": "Kiểm tra thời tiết và lịch vận hành; đặt phòng trước mùa cao điểm.",
    },
    [
        {"title": "Википедия (RU) — Ведучи", "url": "https://ru.wikipedia.org/wiki/Ведучи"},
        {"title": "Tourister — Горнолыжный курорт «Ведучи»", "url": "https://www.tourister.ru/world/europe/russia/city/groznyy/snow/31708"},
    ],
    ["other", "ski-resort", "mountains", "nature", "itum-kali"],
    maps_text("Курорт Ведучи", "Итум-Калинский район", "Veduchi resort", "Chechnya", 42.681471, 45.573762),
))

# 18) Галанчожское озеро --------------------------------------------------------
RECORDS.append(rec(
    "galanchozh-lake",
    "Hồ Galanchozh (Galanchozhskoye Ozero)",
    "Галанчожское озеро",
    "Lake Galanchozh",
    ["park_garden"],
    42.872160, 45.303880,
    "Vùng núi cao tây Chechnya, thượng nguồn sông Gekhi (khu vực Nashkha), Chechnya, Nga.",
    "Hồ Galanchozh xanh ngọc huyền thoại trên núi cao tây Chechnya, được coi là vùng đất cội nguồn (Nashkha) của người Chechen; hồ thiêng gắn nhiều truyền thuyết.",
    "Hồ Galanchozh (Галанчожское озеро, tiếng Chechen Galayn-Am) là một trong những hồ đẹp và huyền bí nhất Chechnya, nằm ở vùng núi cao phía tây, trên độ cao khoảng 1.533 m so với mực nước biển, ở thượng nguồn lưu vực sông Gekhi. Hồ có hình bầu dục gần cân đối, mặt nước màu xanh ngọc trong vắt phản chiếu bầu trời và những sườn núi phủ hoa cỏ cận núi cao, tạo nên khung cảnh như một chiếc bát xanh khổng lồ giữa thảo nguyên núi. Vùng quanh hồ được xem là Nashkha — vùng đất cội nguồn theo truyền thuyết của người Chechen, nơi có nhiều tháp cổ và di tích. Hồ gắn với nhiều truyền thuyết linh thiêng, được công nhận là di tích thiên nhiên cấp cộng hoà và nằm trong danh mục tiềm năng các vùng đất ngập nước quan trọng. Đường tới hồ khó đi, càng làm tăng vẻ hoang sơ, quý giá của nơi này.",
    [
        "Hồ núi cao (~1.533 m) nước xanh ngọc, hình bầu dục.",
        "Nằm ở Nashkha - vùng đất cội nguồn truyền thuyết của người Chechen.",
        "Di tích thiên nhiên cấp cộng hoà, gắn nhiều truyền thuyết.",
    ],
    {
        "hours_vi": "Ban ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Cả ngày (đường xa, khó đi).",
        "best_time_vi": "Mùa hè.",
        "tips_vi": "Cần xe địa hình và đi cùng hướng dẫn; xuất phát sớm, chuẩn bị cho cả ngày.",
    },
    [
        {"title": "OpenKavkaz — Галанчожское озеро", "url": "https://openkavkaz.com/che/galay-am/"},
        {"title": "Нохчалла — Галанчожское озеро", "url": "https://nohchalla.com/o-chechne/856-galanchojskoe-ozero"},
    ],
    ["park_garden", "lake", "mountains", "nature", "sacred"],
    maps_text("Галанчожское озеро", "Чечня", "Lake Galanchozh", "Chechnya", 42.872160, 45.303880),
))

# 19) Бенойские водопады --------------------------------------------------------
RECORDS.append(rec(
    "benoy-waterfall",
    "Thác Benoy (Benoyskiye Vodopady)",
    "Бенойские водопады",
    "Benoy Waterfalls",
    ["park_garden"],
    42.977427, 46.309420,
    "Gần làng Beny (Beno), huyện Nozhay-Yurt, đông nam Chechnya, Nga.",
    "Thác Benoy giữa rừng núi huyện Nozhay-Yurt gần làng Beny - làng tổ của một trong những dòng tộc (teip) đông đảo của người Chechen; điểm dã ngoại thiên nhiên.",
    "Thác Benoy (Бенойские водопады) là một thắng cảnh thiên nhiên ở vùng núi rừng phía đông nam Chechnya, gần làng Beny thuộc huyện Nozhay-Yurt. Những dòng thác đổ xuống giữa rừng cây và vách đá tạo nên không gian mát lành, thơ mộng, được người dân địa phương và du khách chọn làm nơi dã ngoại, nghỉ ngơi cuối tuần. Beny cũng là làng tổ (đất gốc) của teip Benoy — một trong những dòng tộc lớn và đông đảo nhất của người Chechen, nên khu vực mang thêm ý nghĩa lịch sử — văn hoá. Xung quanh có khu vui chơi, nghỉ dưỡng sinh thái nhỏ phục vụ khách. Với hành trình khám phá miền đông Chechnya, thác Benoy là điểm dừng chân dễ chịu giữa thiên nhiên.",
    [
        "Thác nước giữa rừng núi huyện Nozhay-Yurt.",
        "Gần Beny - làng tổ của teip Benoy đông đảo của người Chechen.",
        "Điểm dã ngoại, nghỉ dưỡng sinh thái được ưa chuộng.",
    ],
    {
        "hours_vi": "Ban ngày.",
        "ticket_vi": "Miễn phí hoặc phí nhỏ.",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu.",
        "tips_vi": "Đường núi phía đông, nên đi xe phù hợp; mang theo đồ dã ngoại.",
    },
    [
        {"title": "Википедия (RU) — Беной (село)", "url": "https://ru.wikipedia.org/wiki/Беной_(село)"},
        {"title": "kavkaz.travel — Бенойские водопады", "url": "https://kavkaz.travel/attractions"},
    ],
    ["park_garden", "waterfall", "nature", "nozhay-yurt", "teip"],
    maps_text("Бенойские водопады", "Ножай-Юртовский район", "Benoy Waterfalls", "Chechnya", 42.977427, 46.309420),
))

# 20) Веденская крепость (резиденция Шамиля) ------------------------------------
RECORDS.append(rec(
    "vedeno-fortress",
    "Pháo đài Vedeno (đại bản doanh Imam Shamil)",
    "Веденская крепость (резиденция имама Шамиля)",
    "Vedeno Fortress (Imam Shamil's Residence)",
    ["fortress"],
    42.961601, 46.103840,
    "Làng Vedeno, trung tâm huyện Vedeno, đông nam Chechnya, Nga.",
    "Vedeno - làng miền núi lịch sử từng là đại bản doanh của Imam Shamil thời Chiến tranh Kavkaz; nơi có dấu tích pháo đài và ký ức về cuộc kháng chiến ở vùng cao.",
    "Vedeno (Ведено) là một làng miền núi lịch sử ở đông nam Chechnya, nổi tiếng vì từng là đại bản doanh (thủ phủ) của Imam Shamil — thủ lĩnh phong trào kháng chiến của các dân tộc Bắc Kavkaz giữa thế kỷ 19. Tại đây Shamil từng đặt tổng hành dinh và xây dựng công sự phòng thủ; sau khi vùng này thất thủ, quân đội Nga đã lập một pháo đài (Веденская крепость) tại chỗ. Ngày nay Vedeno giữ vai trò trung tâm hành chính của huyện cùng tên và là điểm đến gắn với ký ức Chiến tranh Kavkaz, với những dấu tích lịch sử và cảnh quan núi rừng đặc trưng. Khu vực xung quanh còn nhiều thắng cảnh như thác nước, làng cổ và hồ núi, biến Vedeno thành cửa ngõ khám phá miền đông nam Chechnya giàu lịch sử.",
    [
        "Từng là đại bản doanh của Imam Shamil thời Chiến tranh Kavkaz.",
        "Có dấu tích pháo đài lịch sử (Веденская крепость).",
        "Cửa ngõ khám phá miền núi đông nam Chechnya.",
    ],
    {
        "hours_vi": "Cả ngày (làng, không gian mở).",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–60 phút.",
        "best_time_vi": "Mùa ấm.",
        "tips_vi": "Kết hợp thác 'Devichya kosa' (Kharachoy) và hồ Kezenoy-Am gần đó.",
    },
    [
        {"title": "Википедия (RU) — Ведено", "url": "https://ru.wikipedia.org/wiki/Ведено"},
        {"title": "Википедия (RU) — Ведено (крепость)", "url": "https://ru.wikipedia.org/wiki/Ведено_(крепость)"},
    ],
    ["fortress", "history", "imam-shamil", "vedeno", "caucasus-war"],
    maps_text("Ведено", "Веденский район", "Vedeno village", "Chechnya", 42.961601, 46.103840),
))

# 21) Этнографический музей «Донди-Юрт» (Урус-Мартан) ---------------------------
RECORDS.append(rec(
    "dondi-yurt-museum",
    "Bảo tàng dân tộc học 'Dondi-Yurt', Urus-Martan",
    "Этнографический музей «Донди-Юрт»",
    "Dondi-Yurt Ethnographic Museum",
    ["museum"],
    43.122360, 45.536599,
    "Thành phố Urus-Martan, huyện Urus-Martan, Chechnya, Nga (bảo tàng nằm ở rìa tây thành phố).",
    "Bảo tàng dân tộc học ngoài trời tư nhân 'Dondi-Yurt' ở Urus-Martan, tái hiện một ngôi làng - pháo đài Chechen cổ với tháp đá, nhà, bia mộ và hàng nghìn hiện vật.",
    "'Dondi-Yurt' (Донди-Юрт) là một bảo tàng dân tộc học ngoài trời độc đáo ở thành phố Urus-Martan, do nhà sưu tầm Adam Satuev gây dựng từ tâm huyết cá nhân. Trên khuôn viên của mình, ông đã tái dựng cả một 'ngôi làng — pháo đài' Chechen cổ, gồm các tháp canh, tháp ở bằng đá, nhà truyền thống, cổng, bia mộ cổ (churt) và vô số hiện vật sinh hoạt, vũ khí, đồ dùng qua nhiều thế kỷ. Mỗi góc của bảo tàng kể một câu chuyện về đời sống, phong tục và lịch sử của người vainakh, từ thời trung cổ đến giai đoạn cận đại. Chủ nhân bảo tàng thường đích thân dẫn khách tham quan và kể chuyện, khiến trải nghiệm trở nên sống động, ấm áp. Đây là một trong những điểm đến văn hoá đáng nhớ nhất bên ngoài Grozny.",
    [
        "Bảo tàng dân tộc học ngoài trời tư nhân, tái dựng làng - pháo đài Chechen cổ.",
        "Có tháp đá, nhà truyền thống, bia mộ cổ và hàng nghìn hiện vật.",
        "Chủ nhân thường đích thân hướng dẫn và kể chuyện.",
    ],
    {
        "hours_vi": "Ban ngày; nên liên hệ trước.",
        "ticket_vi": "Đóng góp/vé nhỏ.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Hỏi đường tại Urus-Martan; nên gọi trước để có người dẫn tham quan.",
    },
    [
        {"title": "Википедия (RU) — Донди-Юрт", "url": "https://ru.wikipedia.org/wiki/Донди-Юрт"},
        {"title": "Википедия (RU) — Урус-Мартан", "url": "https://ru.wikipedia.org/wiki/Урус-Мартан"},
    ],
    ["museum", "ethnography", "open-air", "urus-martan", "vainakh"],
    maps_text("Этнографический музей Донди-Юрт", "Урус-Мартан", "Dondi-Yurt Museum", "Urus-Martan", 43.122360, 45.536599),
))

# 22) Мечеть/зиярат Ташу-Хаджи (Саясан) -----------------------------------------
RECORDS.append(rec(
    "tashu-hadji-mosque-sayasan",
    "Nhà thờ Hồi giáo và thánh tích Tashu-Hadji, Sayasan",
    "Мечеть и зиярат Ташу-Хаджи, Саясан",
    "Tashu-Hadji Mosque and Ziyarat (Sayasan)",
    ["church"],
    43.061192, 46.284940,
    "Làng Sayasan, huyện Nozhay-Yurt, đông Chechnya, Nga.",
    "Nhà thờ Hồi giáo cổ và khu thánh tích (ziyarat) Tashu-Hadji ở làng Sayasan, một trong những trung tâm tâm linh Sufi lâu đời của miền đông Chechnya.",
    "Tại làng Sayasan thuộc huyện Nozhay-Yurt có nhà thờ Hồi giáo cùng khu thánh tích (ziyarat) gắn với Tashu-Hadji (Tashev-Hadji) — một giáo sĩ, thủ lĩnh tinh thần và là một trong những cộng sự của Imam Shamil hồi thế kỷ 19. Đây là một trong những địa điểm tâm linh Sufi lâu đời và được tôn kính của miền đông Chechnya, thu hút tín đồ tới cầu nguyện và tưởng niệm. Công trình mang nét kiến trúc tôn giáo truyền thống, gắn bó mật thiết với lịch sử Hồi giáo và phong trào kháng chiến của vùng. Với du khách, nơi đây mở ra một lát cắt về đời sống đức tin và lịch sử tinh thần của người Chechnya. Khi tới thăm, khách cần ăn mặc kín đáo, giữ thái độ tôn trọng và tuân thủ quy định của cơ sở tôn giáo.",
    [
        "Nhà thờ Hồi giáo và ziyarat cổ gắn với giáo sĩ Tashu-Hadji.",
        "Một trong những trung tâm tâm linh Sufi lâu đời của đông Chechnya.",
        "Gắn với lịch sử Hồi giáo và phong trào kháng chiến thế kỷ 19.",
    ],
    {
        "hours_vi": "Giờ cầu nguyện/ban ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Ngoài các giờ lễ đông người.",
        "tips_vi": "Ăn mặc kín đáo, tôn trọng nghi lễ; phụ nữ nên trùm khăn.",
    },
    [
        {"title": "Википедия (RU) — Ташев-Хаджи", "url": "https://ru.wikipedia.org/wiki/Ташев-Хаджи"},
        {"title": "Википедия (RU) — Саясан", "url": "https://ru.wikipedia.org/wiki/Саясан"},
    ],
    ["church", "mosque", "sufi", "ziyarat", "nozhay-yurt"],
    maps_text("Зиярат Ташу-Хаджи", "Саясан", "Tashu-Hadji Ziyarat", "Sayasan", 43.061192, 46.284940),
))

# 23) Гора Тебулосмта -----------------------------------------------------------
RECORDS.append(rec(
    "mount-tebulosmta",
    "Đỉnh Tebulosmta (nóc nhà của Chechnya)",
    "Гора Тебулосмта",
    "Mount Tebulosmta",
    ["other"],
    42.573333, 45.311944,
    "Biên giới Chechnya - Dagestan - Gruzia, phần đông dãy Đại Kavkaz, Nga.",
    "Đỉnh Tebulosmta cao ~4.492 m - nóc nhà của Chechnya và là một trong những đỉnh cao nhất phía đông dãy Kavkaz, nằm trên biên giới với Dagestan và Gruzia.",
    "Tebulosmta (Тебулосмта) là đỉnh núi cao nhất Chechnya, vươn tới khoảng 4.492 m, đồng thời là một trong những đỉnh cao nhất của phần phía đông dãy Đại Kavkaz. Ngọn núi nằm trên vùng biên giới giữa Chechnya, Dagestan và Gruzia, quanh năm phủ tuyết và băng hà ở phần đỉnh. Với khung cảnh hùng vĩ của núi đá, sông băng và các thung lũng sâu, Tebulosmta là biểu tượng thiên nhiên của vùng cao Chechnya và là mục tiêu mơ ước của giới leo núi, thám hiểm. Việc chinh phục đỉnh đòi hỏi kinh nghiệm, trang bị chuyên dụng và thường phải có hướng dẫn viên do địa hình hiểm trở, gần khu vực biên giới. Ngay cả khi chỉ ngắm từ xa, dáng núi tuyết trắng vẫn là một phần không thể thiếu trong bức tranh thiên nhiên của miền núi Chechnya.",
    [
        "Đỉnh cao nhất Chechnya (~4.492 m), phủ tuyết và băng hà.",
        "Một trong những đỉnh cao nhất phần đông dãy Kavkaz.",
        "Nằm trên biên giới Chechnya - Dagestan - Gruzia.",
    ],
    {
        "hours_vi": "Không áp dụng (hành trình leo núi nhiều ngày).",
        "ticket_vi": "Không.",
        "duration_vi": "Nhiều ngày (đi cùng đoàn leo núi).",
        "best_time_vi": "Mùa hè.",
        "tips_vi": "Chỉ dành cho người có kinh nghiệm; cần hướng dẫn và giấy phép vùng biên; ngắm cảnh từ xa an toàn hơn.",
    },
    [
        {"title": "Википедия (RU) — Тебулосмта", "url": "https://ru.wikipedia.org/wiki/Тебулосмта"},
        {"title": "Википедия (RU) — Боковой хребет (Кавказ)", "url": "https://ru.wikipedia.org/wiki/Боковой_хребет"},
    ],
    ["other", "mountain", "peak", "alpinism", "nature"],
    maps_text("Гора Тебулосмта", "Чечня", "Mount Tebulosmta", "Chechnya", 42.573333, 45.311944),
))

# 24) Водопад «Девичья коса» (Харачой) ------------------------------------------
RECORDS.append(rec(
    "kharachoy-waterfall",
    "Thác 'Bím tóc thiếu nữ' (Devichya Kosa), Kharachoy",
    "Водопад «Девичья коса», Харачой",
    "Devichya Kosa Waterfall (Kharachoy)",
    ["park_garden"],
    42.910278, 46.140000,
    "Bên làng Kharachoy, huyện Vedeno (trên đường tới hồ Kezenoy-Am), Chechnya, Nga.",
    "Thác 'Bím tóc thiếu nữ' (Devichya kosa) bên làng Kharachoy, huyện Vedeno - dòng suối trắng mảnh mai chảy xuống vách đá; điểm dừng thiên nhiên trên đường tới hồ Kezenoy-Am.",
    "Thác 'Devichya kosa' (nghĩa là 'bím tóc thiếu nữ') là một thắng cảnh thiên nhiên duyên dáng bên làng Kharachoy thuộc huyện Vedeno. Dòng nước từ mạch nguồn trên cao chảy xuống vách đá thành một dải trắng mảnh, mềm mại như một bím tóc con gái — hình ảnh đã tạo nên cái tên gợi cảm cho thác. Khu vực được kè đá, làm lối đi và điểm ngắm cảnh, trở thành nơi dừng chân quen thuộc của du khách trên tuyến đường lên hồ Kezenoy-Am. Kharachoy cũng là quê hương của Zelimkhan — một nhân vật lịch sử nổi tiếng của vùng, nên nơi đây mang thêm chiều sâu văn hoá. Không gian mát lành, tiếng nước róc rách giữa núi rừng khiến thác trở thành một điểm nghỉ dễ chịu, thích hợp chụp ảnh và thư giãn.",
    [
        "Dòng thác trắng mảnh như 'bím tóc thiếu nữ' bên vách đá.",
        "Nằm bên làng Kharachoy, trên đường tới hồ Kezenoy-Am.",
        "Kharachoy là quê hương nhân vật lịch sử Zelimkhan.",
    ],
    {
        "hours_vi": "Ban ngày.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu.",
        "tips_vi": "Kết hợp Vedeno và hồ Kezenoy-Am; đường núi, mang giày phù hợp.",
    },
    [
        {"title": "Википедия (RU) — Харачой", "url": "https://ru.wikipedia.org/wiki/Харачой"},
        {"title": "kavkaz.travel — Источник «Девичья коса»", "url": "https://kavkaz.travel/attractions"},
    ],
    ["park_garden", "waterfall", "nature", "vedeno", "kharachoy"],
    maps_text("Водопад Девичья коса", "Харачой", "Devichya Kosa waterfall", "Kharachoy", 42.910278, 46.140000),
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
