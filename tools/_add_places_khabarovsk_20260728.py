# -*- coding: utf-8 -*-
"""_add_places_khabarovsk_20260728.py — VÙNG: Vùng Khabarovsk (Хабаровский край)
(lần chạy tự động 2026-07-28).

Bối cảnh: khabarovsk.json hiện có 7 địa điểm. Bổ sung 26 địa điểm THẬT SỰ nổi tiếng/đặc
sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 33 (đạt mục tiêu >=30).

Tránh trùng 7 slug đã có: khabarovsk-amur-embankment, amur-bridge-khabarovsk,
spaso-preobrazhensky-cathedral-khabarovsk, sikachi-alyan-petroglyphs,
komsomolsk-on-amur-monument, glory-square-khabarovsk, bolshekhekhtsirsky-reserve.

Phân bố loại hình (26 bản ghi mới):
- church (3): Успенский собор, Христорождественский собор, Иннокентьевская церковь.
- square_street (4): Соборная (Комсомольская) площадь, Площадь Ленина, Улица Муравьёва-
  Амурского, Набережная Комсомольска-на-Амуре.
- museum (6): Гродековский музей, Дальневосточный художественный музей, Военно-исторический
  музей, Музей истории Амурского моста, Комсомольский краеведческий музей, Комсомольский
  музей ИЗО.
- monument (2): Памятник Муравьёву-Амурскому, Амурский утёс.
- park_garden (6): Парк «Динамо», Городские пруды, Зоосад «Приамурский», Комсомольский
  заповедник, Озеро Амут, Национальный парк «Шантарские острова».
- theatre (3): Театр драмы, Музыкальный театр, Краевая филармония.
- other/park_garden (2): Амурские столбы, Анненские минеральные воды.

TOẠ ĐỘ — xác minh chéo (ru.wikipedia infobox/geohack, Wikidata, 2GIS, Yandex Maps, sobory.ru;
2026-07-28). Phạm vi Khabarovsk Krai: lat ~47.0–62.5; lon ~130–141 — tất cả toạ độ nằm trong
phạm vi, KHÔNG đảo lat/lon. Khabarovsk city ~48.48,135.07; Komsomolsk-on-Amur ~50.55,137.01.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_khabarovsk_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "khabarovsk"
REGION_NAME_VI = "Vùng Khabarovsk"
FD = "Vùng Viễn Đông"


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

# 1) Успенский собор ----------------------------------------------------------------
RECORDS.append(rec(
    "uspensky-cathedral-khabarovsk",
    "Nhà thờ chính tòa Đức Mẹ An Nghỉ (Uspensky)",
    "Градо-Хабаровский Успенский собор",
    "Assumption (Uspensky) Cathedral, Khabarovsk",
    ["church"],
    48.472953, 135.056493,
    "Quảng trường Nhà thờ (Sobornaya, xưa là Komsomolskaya), trung tâm Khabarovsk, Vùng Khabarovsk, Nga.",
    "Nhà thờ Đức Mẹ An Nghỉ là ngôi thánh đường gạch đỏ mái vòm vàng đứng trên quảng trường Nhà thờ, nhìn thẳng ra dòng Amur. Công trình gốc dựng cuối thế kỷ 19 bị phá năm 1930, được phục dựng đầu những năm 2000 và trở lại thành một biểu tượng tâm linh, kiến trúc của thành phố.",
    "Nhà thờ chính tòa Đức Mẹ An Nghỉ (Uspensky) toạ lạc ngay trên quảng trường Nhà thờ ở rìa cao nguyên trung tâm Khabarovsk, nơi tầm nhìn mở thẳng ra sông Amur mênh mông. Ngôi đền đầu tiên trên vị trí này được xây dựng và thánh hiến vào cuối thế kỷ 19, từng là một trong những công trình tôn giáo quan trọng nhất của thành phố non trẻ bên sông. Trong thời kỳ bài trừ tôn giáo thập niên 1930, nhà thờ cũ bị phá bỏ hoàn toàn. Đến đầu thế kỷ 21, thành phố cho phục dựng thánh đường trên nền cũ với dáng vẻ mới bằng gạch đỏ, những mái vòm mạ vàng vươn cao và tháp chuông thanh thoát, hoàn thành và mở cửa trở lại vào năm 2001. Ngày nay đây vừa là nơi hành lễ của cộng đồng Chính thống giáo, vừa là điểm nhấn thị giác nổi bật khi nhìn từ bờ kè hay từ dòng Amur nhìn vào. Cụm nhà thờ và quảng trường phía trước, với đài tưởng niệm và không gian thoáng đãng, là một trong những góc chụp ảnh được yêu thích nhất của Khabarovsk.",
    [
        "Thánh đường gạch đỏ mái vòm vàng đứng ở rìa cao nguyên nhìn thẳng ra sông Amur.",
        "Được phục dựng năm 2001 trên nền nhà thờ cũ bị phá hủy thập niên 1930.",
        "Cụm nhà thờ và quảng trường Sobornaya là góc ngắm cảnh, chụp ảnh biểu tượng.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường khoảng 8:00–19:00.",
        "ticket_vi": "Miễn phí (là nơi thờ phượng đang hoạt động).",
        "duration_vi": "30–45 phút.",
        "best_time_vi": "Quanh năm; buổi sáng có lễ, hoàng hôn ngắm nhà thờ trên nền sông Amur rất đẹp.",
        "tips_vi": "Ăn mặc kín đáo, nữ nên mang khăn trùm đầu; kết hợp dạo quảng trường Sobornaya và bờ kè ngay bên cạnh.",
    },
    [
        {"title": "Wikipedia (RU) — Градо-Хабаровский Успенский собор", "url": "https://ru.wikipedia.org/wiki/Градо-Хабаровский_Успенский_собор"},
        {"title": "Sobory.ru — Успенский собор Хабаровск", "url": "https://sobory.ru/geo/city/Хабаровск"},
    ],
    ["church", "cathedral", "orthodox", "khabarovsk", "amur", "landmark"],
    maps_text("Градо-Хабаровский Успенский собор", "Хабаровск", "Assumption Cathedral", "Khabarovsk", 48.472953, 135.056493),
))

# 2) Соборная (Комсомольская) площадь -----------------------------------------------
RECORDS.append(rec(
    "cathedral-square-khabarovsk",
    "Quảng trường Nhà thờ (Sobornaya, xưa là Komsomolskaya)",
    "Соборная площадь (бывшая Комсомольская площадь)",
    "Cathedral Square (former Komsomolskaya Square)",
    ["square_street"],
    48.47285, 135.05630,
    "Quảng trường Sobornaya (Komsomolskaya), trung tâm Khabarovsk, Vùng Khabarovsk, Nga.",
    "Quảng trường Nhà thờ là không gian mở lịch sử ở rìa cao nguyên trung tâm, nơi có Nhà thờ Đức Mẹ An Nghỉ và tầm nhìn thoáng ra sông Amur. Từng mang tên Komsomolskaya thời Xô Viết, quảng trường là điểm hẹn dạo chơi, lễ hội và khởi đầu con dốc dẫn xuống bờ kè.",
    "Quảng trường Nhà thờ (Sobornaya) là một trong những không gian công cộng lâu đời và giàu ý nghĩa nhất Khabarovsk, nằm ở rìa cao nguyên trung tâm nơi thành phố tiếp giáp với dòng Amur. Suốt thời kỳ Xô Viết, quảng trường mang tên Komsomolskaya và là nơi diễn ra các cuộc mít tinh, diễu hành; tại đây từng dựng đài tưởng niệm những chiến sĩ đã ngã xuống vì chính quyền Xô Viết ở vùng Viễn Đông. Sau khi Nhà thờ Đức Mẹ An Nghỉ được phục dựng đầu thế kỷ 21, quảng trường lấy lại tên gọi gắn với thánh đường và trở thành cụm không gian tâm linh - đô thị hài hoà. Ngày nay du khách đến đây để chiêm ngưỡng nhà thờ gạch đỏ mái vòm vàng, phóng tầm mắt ra khúc sông Amur rộng lớn, rồi theo con dốc và bậc thang đi xuống bờ kè Đô đốc Nevelskoy. Quảng trường cũng là nơi tổ chức nhiều sự kiện, lễ hội thành phố và là điểm khởi đầu quen thuộc cho các chuyến tản bộ khám phá trung tâm lịch sử.",
    [
        "Không gian mở lịch sử ở rìa cao nguyên, ôm trọn Nhà thờ Đức Mẹ An Nghỉ.",
        "Tầm nhìn thoáng ra sông Amur và lối dốc dẫn thẳng xuống bờ kè.",
        "Từng mang tên Komsomolskaya thời Xô Viết, nay là cụm không gian tâm linh - đô thị.",
    ],
    {
        "hours_vi": "Không gian ngoài trời, mở tự do 24/24.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "30–60 phút.",
        "best_time_vi": "Quanh năm; đẹp nhất vào chiều tối mùa hè và các dịp lễ hội thành phố.",
        "tips_vi": "Kết hợp tham quan Nhà thờ Đức Mẹ An Nghỉ và đi xuống bờ kè sông Amur ngay cạnh; buổi tối quảng trường lên đèn.",
    },
    [
        {"title": "Wikipedia (RU) — Соборная площадь (Хабаровск)", "url": "https://ru.wikipedia.org/wiki/Соборная_площадь_(Хабаровск)"},
    ],
    ["square", "cathedral-square", "khabarovsk", "amur", "center", "viewpoint"],
    maps_text("Соборная площадь", "Хабаровск", "Cathedral Square", "Khabarovsk", 48.47285, 135.05630),
))

# 3) Площадь Ленина -----------------------------------------------------------------
RECORDS.append(rec(
    "lenin-square-khabarovsk",
    "Quảng trường Lenin (Khabarovsk)",
    "Площадь Ленина",
    "Lenin Square, Khabarovsk",
    ["square_street"],
    48.48028, 135.07194,
    "Quảng trường Lenin, trung tâm Khabarovsk, Vùng Khabarovsk, Nga.",
    "Quảng trường Lenin là quảng trường chính, lớn thứ hai vùng Viễn Đông, trung tâm hành chính và lễ hội của Khabarovsk. Rộng rãi với đài phun nước, luống hoa và các tòa nhà lịch sử bao quanh, đây là nơi diễn ra mọi sự kiện lớn của thành phố suốt bốn mùa.",
    "Quảng trường Lenin là quảng trường trung tâm và tiêu biểu nhất của Khabarovsk, được xem là một trong những quảng trường lớn của toàn vùng Viễn Đông Nga. Được quy hoạch từ đầu thế kỷ 20 (khi đó mang tên Nikolaevskaya), quảng trường nhiều lần đổi tên theo thăng trầm lịch sử trước khi mang tên Lenin. Không gian rộng rãi được bao quanh bởi những công trình kiến trúc bề thế thời đầu thế kỷ 20 và thời Xô Viết, trong đó có trụ sở chính quyền vùng. Trung tâm quảng trường là hệ thống đài phun nước và các luống hoa được chăm chút, biến nơi đây thành điểm dạo chơi, hẹn hò được người dân yêu thích vào mùa hè. Mùa đông, quảng trường biến thành khu vui chơi băng tuyết với cây thông năm mới khổng lồ, các tác phẩm điêu khắc băng và trượt băng. Đây cũng là sân khấu chính cho các cuộc diễu hành, hòa nhạc và lễ hội lớn của thành phố, đồng thời là điểm khởi đầu tự nhiên của đại lộ trung tâm Muravyov-Amursky dẫn xuống phía sông.",
    [
        "Quảng trường trung tâm, thuộc hàng lớn nhất vùng Viễn Đông.",
        "Đài phun nước, luống hoa mùa hè; khu điêu khắc băng và cây thông năm mới mùa đông.",
        "Điểm khởi đầu đại lộ Muravyov-Amursky, trung tâm mọi lễ hội thành phố.",
    ],
    {
        "hours_vi": "Không gian mở, tham quan tự do 24/24.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "30–45 phút.",
        "best_time_vi": "Mùa hè ngắm đài phun nước; dịp Năm mới có khu điêu khắc băng và trang trí rực rỡ.",
        "tips_vi": "Bắt đầu tuyến đi bộ dọc đại lộ Muravyov-Amursky từ đây; buổi tối đài phun nước và đèn rất đẹp.",
    },
    [
        {"title": "Wikipedia (RU) — Площадь Ленина (Хабаровск)", "url": "https://ru.wikipedia.org/wiki/Площадь_Ленина_(Хабаровск)"},
    ],
    ["square", "lenin-square", "khabarovsk", "center", "fountains"],
    maps_text("Площадь Ленина", "Хабаровск", "Lenin Square", "Khabarovsk", 48.48028, 135.07194),
))

# 4) Хабаровский краевой музей им. Гродекова ----------------------------------------
RECORDS.append(rec(
    "grodekov-museum-khabarovsk",
    "Bảo tàng địa phương vùng Khabarovsk mang tên Grodekov",
    "Хабаровский краевой музей имени Н.И. Гродекова",
    "Grodekov Regional Museum of Local Lore",
    ["museum"],
    48.47334, 135.050472,
    "Phố Shevchenko 11, trung tâm Khabarovsk, Vùng Khabarovsk, Nga.",
    "Bảo tàng Grodekov là bảo tàng nghiên cứu địa phương lâu đời và lớn nhất vùng Khabarovsk, thành lập cuối thế kỷ 19. Bộ sưu tập phong phú về thiên nhiên, dân tộc học các dân tộc bản địa Amur và lịch sử vùng Viễn Đông trưng bày trong quần thể nhà cổ gần bờ kè.",
    "Bảo tàng địa phương vùng Khabarovsk mang tên tướng N.I. Grodekov là một trong những bảo tàng lâu đời và có uy tín nhất vùng Viễn Đông Nga, được thành lập vào năm 1894 dưới sự bảo trợ của toàn quyền Priamurye đương thời. Toạ lạc trong một quần thể nhà gạch cổ kính gần bờ kè sông Amur, bảo tàng lưu giữ hàng trăm nghìn hiện vật trải rộng nhiều lĩnh vực: địa chất, động thực vật vùng Amur - Ussuri (trong đó có tiêu bản hổ Amur, gấu, các loài chim quý), khảo cổ học và đặc biệt là bộ sưu tập dân tộc học đồ sộ về các dân tộc bản địa như Nanai, Ulchi, Udege, Nivkh. Du khách có thể chiêm ngưỡng trang phục truyền thống thêu hoa văn cá, thuyền độc mộc, dụng cụ săn bắt, cùng các mô hình tái hiện đời sống của cư dân sông nước Amur. Một điểm nhấn nổi tiếng là bộ xương cá voi lớn được treo trưng bày. Các gian trưng bày về lịch sử khai phá, phát triển vùng Viễn Đông, thời kỳ Nội chiến và Thế chiến giúp khách hình dung trọn vẹn hành trình của cả một vùng đất. Đây là điểm đến hàng đầu để hiểu về thiên nhiên và con người Priamurye.",
    [
        "Bảo tàng lâu đời (1894), lớn nhất về nghiên cứu địa phương ở vùng Khabarovsk.",
        "Bộ sưu tập dân tộc học đặc sắc về người Nanai, Ulchi, Nivkh và cư dân sông Amur.",
        "Thiên nhiên Amur - Ussuri: hổ Amur, chim quý và bộ xương cá voi nổi tiếng.",
    ],
    {
        "hours_vi": "Thường mở 10:00–18:00, nghỉ thứ Hai (nên kiểm tra lịch theo mùa).",
        "ticket_vi": "Có thu vé, giá phổ thông vừa phải; ưu đãi cho học sinh, sinh viên, người cao tuổi.",
        "duration_vi": "1,5–2,5 giờ.",
        "best_time_vi": "Quanh năm; lý tưởng cho ngày mưa hoặc mùa đông lạnh.",
        "tips_vi": "Có thể kết hợp Bảo tàng Mỹ thuật Viễn Đông và Bảo tàng Lịch sử Quân sự gần kề; nên thuê thuyết minh để hiểu sâu phần dân tộc học.",
    },
    [
        {"title": "Wikipedia (RU) — Хабаровский краевой музей имени Н. И. Гродекова", "url": "https://ru.wikipedia.org/wiki/Хабаровский_краевой_музей_имени_Н._И._Гродекова"},
        {"title": "Trang chính thức bảo tàng", "url": "https://hkm.ru/"},
    ],
    ["museum", "local-lore", "ethnography", "nanai", "khabarovsk", "far-east"],
    maps_text("Хабаровский краевой музей имени Гродекова", "Хабаровск", "Grodekov Regional Museum", "Khabarovsk", 48.47334, 135.050472),
    official_site="https://hkm.ru/",
))

# 5) Дальневосточный художественный музей -------------------------------------------
RECORDS.append(rec(
    "far-eastern-art-museum-khabarovsk",
    "Bảo tàng Mỹ thuật Viễn Đông",
    "Дальневосточный художественный музей",
    "Far Eastern Art Museum",
    ["museum"],
    48.47299, 135.052387,
    "Phố Shevchenko 7, trung tâm Khabarovsk, Vùng Khabarovsk, Nga.",
    "Bảo tàng Mỹ thuật Viễn Đông là bảo tàng nghệ thuật lớn nhất vùng Viễn Đông Nga, mở cửa từ năm 1931. Bộ sưu tập trải từ tranh tượng Nga, châu Âu cổ điển đến nghệ thuật dân gian và mỹ thuật đương đại của vùng.",
    "Bảo tàng Mỹ thuật Viễn Đông là bảo tàng nghệ thuật lớn và giàu có nhất toàn vùng Viễn Đông Nga, được thành lập năm 1931 và đặt trong một tòa nhà lịch sử duyên dáng trên phố Shevchenko, ngay cạnh cụm bảo tàng trung tâm Khabarovsk. Bộ sưu tập ban đầu được chuyển về từ các bảo tàng lớn ở Moskva và Leningrad, trong đó có cả những tác phẩm từ bộ sưu tập của Bảo tàng Hermitage và Bảo tàng Nga, nhờ vậy mà một thành phố ở tận cùng phương Đông lại sở hữu được nhiều kiệt tác đáng ngạc nhiên. Khách tham quan có thể chiêm ngưỡng tranh của các bậc thầy hội họa Nga thế kỷ 18–20, nghệ thuật cổ điển Tây Âu, các bức icon Chính thống giáo, đồ họa, điêu khắc, cùng bộ sưu tập nghệ thuật trang trí và dân gian. Một mảng đặc sắc riêng là nghệ thuật của các dân tộc bản địa vùng Amur và tác phẩm của các họa sĩ đương đại vùng Viễn Đông. Không gian trưng bày ấm cúng, được tổ chức mạch lạc theo chủ đề và thời kỳ, biến nơi đây thành điểm đến không thể bỏ qua cho người yêu nghệ thuật khi ghé Khabarovsk.",
    [
        "Bảo tàng nghệ thuật lớn nhất vùng Viễn Đông Nga, mở cửa từ 1931.",
        "Sở hữu tác phẩm chuyển về từ Hermitage và Bảo tàng Nga.",
        "Kết hợp mỹ thuật Nga - Tây Âu cổ điển với nghệ thuật bản địa Amur.",
    ],
    {
        "hours_vi": "Thường mở 10:00–19:00, nghỉ thứ Hai (kiểm tra lịch theo mùa).",
        "ticket_vi": "Có thu vé phổ thông vừa phải; ưu đãi cho nhóm học sinh, sinh viên.",
        "duration_vi": "1–2 giờ.",
        "best_time_vi": "Quanh năm; phù hợp ngày mưa hoặc mùa đông.",
        "tips_vi": "Nằm trong cụm bảo tàng phố Shevchenko, dễ ghép với Bảo tàng Grodekov; hỏi trước lịch triển lãm đặc biệt.",
    },
    [
        {"title": "Wikipedia (RU) — Дальневосточный художественный музей", "url": "https://ru.wikipedia.org/wiki/Дальневосточный_художественный_музей"},
    ],
    ["museum", "art", "fine-arts", "khabarovsk", "far-east"],
    maps_text("Дальневосточный художественный музей", "Хабаровск", "Far Eastern Art Museum", "Khabarovsk", 48.47299, 135.052387),
))

# 6) Военно-исторический музей -------------------------------------------------------
RECORDS.append(rec(
    "military-history-museum-khabarovsk",
    "Bảo tàng Lịch sử Quân sự Quân khu Viễn Đông",
    "Военно-исторический музей Восточного военного округа",
    "Military History Museum of the Eastern Military District",
    ["museum"],
    48.47345, 135.052735,
    "Phố Shevchenko 20, gần bờ kè sông Amur, Khabarovsk, Vùng Khabarovsk, Nga.",
    "Bảo tàng Lịch sử Quân sự trưng bày lịch sử quân sự vùng Viễn Đông từ thời khai phá, Nội chiến, các trận đánh ở Khalkhin Gol, Thế chiến II đến hiện đại. Điểm nhấn là khu trưng bày ngoài trời với xe tăng, pháo và khí tài.",
    "Bảo tàng Lịch sử Quân sự Quân khu Viễn Đông (nay thuộc Quân khu miền Đông) là một trong những bảo tàng chuyên đề quân sự lâu đời của vùng, nằm gần bờ kè sông Amur trong khu trung tâm lịch sử Khabarovsk. Bộ sưu tập tái hiện chặng đường bảo vệ và phát triển vùng biên viễn Viễn Đông của nước Nga: từ thời các đoàn Cossack khai phá, những xung đột biên giới, thời kỳ Nội chiến và can thiệp nước ngoài, các trận đánh nổi tiếng ở Khalkhin Gol và hồ Khasan, cho tới chiến dịch chống phát xít Nhật năm 1945 khép lại Thế chiến II. Bên trong bảo tàng trưng bày vũ khí, quân phục, cờ hiệu, huân chương, tài liệu và nhiều hiện vật gốc quý. Sức hút lớn nhất với du khách, đặc biệt trẻ em, là khu trưng bày ngoài trời với dàn xe tăng, pháo, xe bọc thép, hệ thống phòng không và các loại khí tài thật của nhiều thời kỳ. Đây là điểm đến hấp dẫn cho người quan tâm lịch sử quân sự và là nơi tổ chức các hoạt động giáo dục truyền thống của thành phố.",
    [
        "Trưng bày lịch sử quân sự Viễn Đông: Khalkhin Gol, hồ Khasan, chiến dịch 1945.",
        "Khu trưng bày ngoài trời với xe tăng, pháo, xe bọc thép và khí tài thật.",
        "Vị trí trung tâm, gần bờ kè và cụm bảo tàng phố Shevchenko.",
    ],
    {
        "hours_vi": "Thường mở 10:00–18:00, nghỉ đầu tuần (kiểm tra lịch).",
        "ticket_vi": "Vé phổ thông giá thấp; khu ngoài trời có thể xem miễn phí ở một số khu vực.",
        "duration_vi": "1–1,5 giờ.",
        "best_time_vi": "Quanh năm; khu khí tài ngoài trời đẹp nhất mùa khô ráo.",
        "tips_vi": "Rất hợp với gia đình có trẻ nhỏ; kết hợp với các bảo tàng lân cận và bờ kè sông Amur.",
    },
    [
        {"title": "Wikipedia (RU) — Военно-исторический музей (Хабаровск)", "url": "https://ru.wikipedia.org/wiki/Военно-исторический_музей_Восточного_военного_округа"},
    ],
    ["museum", "military", "history", "khabarovsk", "outdoor-exhibit", "far-east"],
    maps_text("Военно-исторический музей", "Хабаровск", "Military History Museum", "Khabarovsk", 48.47345, 135.052735),
))

# 7) Памятник Муравьёву-Амурскому ---------------------------------------------------
RECORDS.append(rec(
    "muravyov-amursky-monument-khabarovsk",
    "Tượng đài Bá tước Muravyov-Amursky",
    "Памятник Н.Н. Муравьёву-Амурскому",
    "Monument to Count Muravyov-Amursky",
    ["monument"],
    48.47278, 135.04972,
    "Đầu bờ kè, trên mỏm đá cao nhìn ra sông Amur, trung tâm Khabarovsk, Vùng Khabarovsk, Nga.",
    "Tượng đài Bá tước Muravyov-Amursky sừng sững trên mỏm đá cao đầu bờ kè, tôn vinh vị toàn quyền đã sáp nhập vùng Amur vào nước Nga và lập nên Khabarovsk. Chính hình ảnh tượng đài này được in trên tờ tiền 5000 rúp của Nga.",
    "Tượng đài Bá tước Nikolay Muravyov-Amursky là một trong những biểu tượng nổi tiếng nhất của Khabarovsk, đặt trên mỏm đá cao ở đầu bờ kè sông Amur, nơi tượng vươn lên trên cả tán cây và nhìn thẳng ra dòng sông rộng lớn. Muravyov-Amursky là toàn quyền Đông Siberia giữa thế kỷ 19, người có công lớn trong việc đưa vùng Amur trở lại với nước Nga qua Hiệp ước Aigun (1858) và trực tiếp gắn liền với sự ra đời của thành phố Khabarovka - tiền thân Khabarovsk. Bức tượng đồng bệ vệ ban đầu được khánh thành năm 1891; trong thời kỳ Xô Viết, tượng bị dỡ bỏ và bệ đá từng được dùng đặt tượng Lenin. Đến năm 1992, tượng đài được phục dựng theo nguyên mẫu và trở lại vị trí lịch sử. Hình ảnh tượng đài cùng cầu Amur nổi tiếng chính là họa tiết được in trên mặt tờ tiền 5000 rúp của Liên bang Nga, khiến đây trở thành điểm mà hầu như du khách nào tới Khabarovsk cũng muốn ghé để chụp ảnh. Từ khu vực tượng đài, tầm nhìn toàn cảnh bờ kè và sông Amur mở ra tuyệt đẹp.",
    [
        "Tôn vinh Muravyov-Amursky, người sáp nhập vùng Amur và khai sinh Khabarovsk.",
        "Hình ảnh được in trên tờ tiền 5000 rúp của Nga.",
        "Đứng trên mỏm đá cao đầu bờ kè, điểm ngắm toàn cảnh sông Amur.",
    ],
    {
        "hours_vi": "Không gian ngoài trời, tham quan tự do 24/24.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "20–30 phút.",
        "best_time_vi": "Chiều tối mùa hè để ngắm hoàng hôn trên sông Amur.",
        "tips_vi": "Mang theo tờ 5000 rúp để chụp ảnh so sánh với tượng; kết hợp dạo bờ kè và Mỏm đá Amur (Utyos) ngay cạnh.",
    },
    [
        {"title": "Wikipedia (RU) — Памятник Муравьёву-Амурскому", "url": "https://ru.wikipedia.org/wiki/Памятник_Муравьёву-Амурскому"},
    ],
    ["monument", "muravyov-amursky", "khabarovsk", "amur", "5000-ruble", "viewpoint"],
    maps_text("Памятник Муравьёву-Амурскому", "Хабаровск", "Muravyov-Amursky Monument", "Khabarovsk", 48.47278, 135.04972),
))

# 8) Амурский утёс ------------------------------------------------------------------
RECORDS.append(rec(
    "amur-cliff-utyos-khabarovsk",
    "Mỏm đá Amur (Utyos)",
    "Амурский утёс",
    "Amur Cliff (Utyos)",
    ["monument", "other"],
    48.472698, 135.049287,
    "Bờ kè Đô đốc Nevelskoy, trên vách đá ven sông, trung tâm Khabarovsk, Vùng Khabarovsk, Nga.",
    "Mỏm đá Amur (Utyos) là vách đá lịch sử vươn ra sông Amur, nơi những người lính đầu tiên đổ bộ lập nên Khabarovsk năm 1858. Tòa tháp quan sát duyên dáng trên mỏm đá là một trong những biểu tượng thị giác được yêu thích nhất thành phố.",
    "Mỏm đá Amur, người địa phương quen gọi là Utyos, là vách đá nhô ra dòng Amur ngay giữa bờ kè trung tâm Khabarovsk và gắn liền với chính khoảnh khắc khai sinh thành phố: mùa hè năm 1858, một đại đội lính biên phòng Nga đã đổ bộ lên đúng vị trí này để lập đồn quân sự Khabarovka. Trên đỉnh mỏm đá là một tòa nhà nhỏ xây năm 1943 với tháp tròn và mái chóp thanh thoát, ban đầu là trạm cứu hộ - quan sát trên sông, nay trở thành một trong những hình ảnh mang tính biểu tượng nhất của Khabarovsk, thường xuất hiện trên bưu thiếp và ảnh lưu niệm. Bên trong tòa tháp hiện có không gian triển lãm, quán cà phê và đài quan sát cho phép ngắm toàn cảnh sông Amur cùng bờ kè trải dài. Khu vực quanh mỏm đá được tô điểm bằng bậc thang, lối dạo và cây xanh, là điểm dừng chân lãng mạn để ngắm hoàng hôn, đặc biệt sống động vào những buổi tối mùa hè khi bờ kè đông vui. Utyos vừa là chứng nhân lịch sử, vừa là ban công ngắm cảnh đẹp nhất nhìn ra dòng sông biểu tượng của vùng Viễn Đông.",
    [
        "Nơi lính Nga đổ bộ lập đồn Khabarovka năm 1858 - khởi nguồn thành phố.",
        "Tòa tháp quan sát năm 1943 là biểu tượng thị giác nổi tiếng của Khabarovsk.",
        "Đài quan sát và không gian triển lãm ngắm toàn cảnh sông Amur.",
    ],
    {
        "hours_vi": "Khu vực ngoài trời mở tự do; không gian triển lãm/quán trong tháp theo giờ riêng.",
        "ticket_vi": "Dạo quanh miễn phí; vào khu triển lãm/đài quan sát có thể thu phí nhỏ.",
        "duration_vi": "30–45 phút.",
        "best_time_vi": "Chiều tối mùa hè để ngắm hoàng hôn; buổi tối có đèn chiếu sáng.",
        "tips_vi": "Kết hợp tượng đài Muravyov-Amursky và toàn tuyến bờ kè; gió sông khá mạnh, nên mang áo khoác nhẹ.",
    },
    [
        {"title": "Wikipedia (RU) — Амурский утёс", "url": "https://ru.wikipedia.org/wiki/Амурский_утёс"},
    ],
    ["cliff", "utyos", "viewpoint", "khabarovsk", "amur", "landmark"],
    maps_text("Амурский утёс", "Хабаровск", "Amur Cliff Utyos", "Khabarovsk", 48.472698, 135.049287),
))

# 9) Музей истории Амурского моста --------------------------------------------------
RECORDS.append(rec(
    "amur-bridge-museum-khabarovsk",
    "Bảo tàng Lịch sử cầu Amur",
    "Музей истории Амурского моста",
    "Amur Bridge History Museum",
    ["museum", "bridge"],
    48.5409, 135.0129,
    "Khu vực chân cầu Amur, phía tây bắc trung tâm Khabarovsk, Vùng Khabarovsk, Nga.",
    "Bảo tàng ngoài trời độc đáo trưng bày một nhịp thép nguyên bản của cầu Amur (khánh thành 1916) cùng đầu máy, toa tàu và hiện vật kỹ thuật đường sắt. Đây là nơi kể câu chuyện của cây cầu từng là dài nhất châu Á - đế Nga.",
    "Bảo tàng Lịch sử cầu Amur là một bảo tàng ngoài trời độc đáo nằm ngay dưới chân cầu Amur trứ danh - cây cầu đường sắt bắc qua sông Amur được khánh thành năm 1916, từng được mệnh danh là 'cầu Sa hoàng' và là một trong những cây cầu dài nhất châu Á thời bấy giờ. Khi cây cầu cũ được cải tạo, tái thiết vào những năm 1990–2000, một trong các nhịp dàn thép nguyên bản đầu thế kỷ 20 đã được giữ lại và dựng thành hiện vật trung tâm của bảo tàng - du khách có thể đi bộ ngay dưới và bên cạnh khối kết cấu thép khổng lồ này. Xung quanh trưng bày đầu máy hơi nước, các toa tàu, thiết bị và tài liệu kể lại lịch sử xây dựng tuyến đường sắt xuyên Siberia đoạn qua Amur, một kỳ công kỹ thuật của nước Nga. Bảo tàng đặc biệt hấp dẫn với người yêu đường sắt, kỹ thuật và lịch sử; đồng thời cũng là điểm để chiêm ngưỡng cận cảnh cây cầu hai tầng đường sắt - đường bộ hiện đại đang vận hành ngay bên cạnh, cây cầu mà hình ảnh của nó cùng tượng Muravyov-Amursky được in trên tờ 5000 rúp.",
    [
        "Bảo tàng ngoài trời với một nhịp thép nguyên bản của cầu Amur năm 1916.",
        "Đầu máy hơi nước, toa tàu và hiện vật lịch sử đường sắt xuyên Siberia.",
        "Ngắm cận cảnh cây cầu biểu tượng in trên tờ tiền 5000 rúp.",
    ],
    {
        "hours_vi": "Thường mở ban ngày, có thể nghỉ đầu tuần (nên kiểm tra lịch trước).",
        "ticket_vi": "Vé phổ thông giá thấp.",
        "duration_vi": "45 phút–1 giờ.",
        "best_time_vi": "Mùa khô ráo (cuối xuân đến đầu thu) vì là bảo tàng ngoài trời.",
        "tips_vi": "Cách trung tâm vài km, nên đi taxi/xe; kết hợp ngắm toàn cảnh cầu Amur từ bờ.",
    },
    [
        {"title": "Wikipedia (RU) — Амурский мост", "url": "https://ru.wikipedia.org/wiki/Амурский_мост"},
    ],
    ["museum", "bridge", "railway", "amur", "khabarovsk", "outdoor-exhibit"],
    maps_text("Музей истории Амурского моста", "Хабаровск", "Amur Bridge History Museum", "Khabarovsk", 48.5409, 135.0129),
))

# 10) Парк «Динамо» -----------------------------------------------------------------
RECORDS.append(rec(
    "dynamo-park-khabarovsk",
    "Công viên Dynamo",
    "Парк «Динамо»",
    "Dynamo Park",
    ["park_garden"],
    48.481531, 135.079305,
    "Trung tâm Khabarovsk, gần đại lộ Amursky, Vùng Khabarovsk, Nga.",
    "Công viên Dynamo là công viên trung tâm lớn và xanh mát nhất Khabarovsk, lá phổi của thành phố với những con đường dạo, hồ nước, đài phun và khu vui chơi. Đây là nơi người dân thư giãn, tập thể thao và dạo chơi quanh năm.",
    "Công viên Dynamo là công viên văn hóa - nghỉ ngơi trung tâm và lớn nhất của Khabarovsk, được ví như lá phổi xanh giữa lòng thành phố. Trải rộng trên một khu đất rợp bóng cây ngay sát trung tâm, công viên gồm những lối dạo bộ dài, các hồ nước và kênh nhỏ, đài phun nước, sân chơi trẻ em, khu trò chơi giải trí và nhiều không gian mở để nghỉ ngơi. Liền kề với công viên là hệ thống 'ao thành phố' (Городские пруды) trên đại lộ Ussuri với những đài phun nước nhạc nước nổi tiếng vào mùa hè. Người dân Khabarovsk đến đây quanh năm: mùa hè để dạo mát, đạp vịt, cho trẻ chơi và tập thể dục; mùa đông để trượt tuyết, đi bộ trên những lối phủ tuyết và ngắm cây cối đóng băng. Công viên cũng là nơi tổ chức nhiều sự kiện, lễ hội và biểu diễn ngoài trời. Với vị trí trung tâm dễ tiếp cận và không gian đa dạng, Dynamo là điểm dừng chân lý tưởng để cảm nhận nhịp sống thường nhật, thư thái của người dân thành phố bên sông Amur.",
    [
        "Công viên trung tâm lớn nhất Khabarovsk, lá phổi xanh của thành phố.",
        "Lối dạo, hồ nước, đài phun và khu vui chơi cho mọi lứa tuổi.",
        "Liền kề hệ thống 'ao thành phố' với đài phun nhạc nước mùa hè.",
    ],
    {
        "hours_vi": "Mở tự do; khu trò chơi giải trí có giờ riêng theo mùa.",
        "ticket_vi": "Vào công viên miễn phí; một số trò chơi thu phí.",
        "duration_vi": "1–2 giờ.",
        "best_time_vi": "Mùa hè cho đài phun nước và cây xanh; mùa đông cho cảnh tuyết.",
        "tips_vi": "Ghé đài phun nhạc nước ở 'ao thành phố' buổi tối mùa hè; gần các quán cà phê và đại lộ trung tâm.",
    },
    [
        {"title": "Wikipedia (RU) — Парк «Динамо» (Хабаровск)", "url": "https://ru.wikipedia.org/wiki/Динамо_(парк,_Хабаровск)"},
    ],
    ["park", "garden", "recreation", "khabarovsk", "fountains"],
    maps_text("Парк Динамо", "Хабаровск", "Dynamo Park", "Khabarovsk", 48.481531, 135.079305),
))

# 11) Городские пруды ---------------------------------------------------------------
RECORDS.append(rec(
    "city-ponds-khabarovsk",
    "Ao thành phố và đại lộ Ussuri",
    "Городские пруды (Уссурийский бульвар)",
    "City Ponds and Ussuri Boulevard",
    ["park_garden", "square_street"],
    48.476723, 135.073776,
    "Đại lộ Ussuri, trung tâm Khabarovsk, Vùng Khabarovsk, Nga.",
    "Ao thành phố là chuỗi hồ nhân tạo bậc thang dọc đại lộ Ussuri, nổi tiếng với những đài phun nhạc nước biểu diễn ánh sáng vào các buổi tối mùa hè. Đây là một trong những điểm dạo chơi buổi tối được yêu thích nhất trung tâm Khabarovsk.",
    "Ao thành phố (Городские пруды) là một chuỗi hồ nước nhân tạo xếp bậc thang chạy dọc theo đại lộ Ussuri ngay giữa trung tâm Khabarovsk, kề bên công viên Dynamo. Được cải tạo, chỉnh trang thành một không gian dạo chơi hiện đại, khu vực này nổi tiếng nhất với các đài phun nước lớn giữa hồ, biến thành sân khấu nhạc nước với đèn màu và nhạc vào những buổi tối mùa hè, thu hút đông đảo người dân lẫn du khách tới ngắm và chụp ảnh. Dọc theo đại lộ Ussuri là những lối đi lát đá, ghế nghỉ, luống hoa, tác phẩm điêu khắc nhỏ và các quán cà phê, tạo nên một trục dạo bộ dễ chịu nối trung tâm thành phố. Ban ngày, mặt hồ phản chiếu cây xanh và các tòa nhà lịch sử tạo nên khung cảnh yên bình; buổi tối, cả khu vực trở nên lung linh, sống động. Đây là điểm hẹn quen thuộc của các gia đình, cặp đôi và là nơi lý tưởng để kết thúc một ngày khám phá trung tâm Khabarovsk.",
    [
        "Chuỗi hồ bậc thang với đài phun nhạc nước nổi tiếng vào tối mùa hè.",
        "Trục dạo bộ dễ chịu dọc đại lộ Ussuri, kề công viên Dynamo.",
        "Điểm hẹn buổi tối lung linh giữa trung tâm thành phố.",
    ],
    {
        "hours_vi": "Không gian mở tự do; nhạc nước biểu diễn theo lịch buổi tối mùa hè.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "30–60 phút.",
        "best_time_vi": "Tối mùa hè (tháng 6–9) để xem nhạc nước và ánh đèn.",
        "tips_vi": "Kiểm tra lịch biểu diễn nhạc nước; kết hợp công viên Dynamo và các quán cà phê ven đại lộ.",
    },
    [
        {"title": "Wikipedia (RU) — Уссурийский бульвар (Хабаровск)", "url": "https://ru.wikipedia.org/wiki/Уссурийский_бульвар"},
    ],
    ["ponds", "boulevard", "fountains", "khabarovsk", "promenade", "evening"],
    maps_text("Городские пруды", "Хабаровск", "City Ponds Ussuri Boulevard", "Khabarovsk", 48.476723, 135.073776),
))

# 12) Улица Муравьёва-Амурского -----------------------------------------------------
RECORDS.append(rec(
    "muravyov-amursky-street-khabarovsk",
    "Đại lộ Muravyov-Amursky (phố lịch sử)",
    "Улица Муравьёва-Амурского",
    "Muravyov-Amursky Street",
    ["square_street"],
    48.47800, 135.06400,
    "Trục trung tâm nối quảng trường Lenin với quảng trường Nhà thờ, Khabarovsk, Vùng Khabarovsk, Nga.",
    "Đại lộ Muravyov-Amursky là con phố chính, lịch sử và đẹp nhất Khabarovsk, nối quảng trường Lenin với quảng trường Nhà thờ. Hai bên là dãy nhà đá cuối thế kỷ 19 - đầu thế kỷ 20 với kiến trúc gạch trang trí độc đáo.",
    "Đại lộ Muravyov-Amursky là trục phố trung tâm và biểu tượng của Khabarovsk, kéo dài từ quảng trường Lenin xuống tới quảng trường Nhà thờ ở rìa cao nguyên nhìn ra sông Amur. Đây là con phố lâu đời nhất và được xem là đẹp nhất thành phố, nơi tập trung phần lớn các công trình kiến trúc lịch sử cuối thế kỷ 19 - đầu thế kỷ 20 được xây bằng gạch đỏ và gạch xám với những chi tiết trang trí cầu kỳ, tạo nên diện mạo rất riêng của Khabarovsk. Dọc phố là các cửa hàng, quán cà phê, nhà hát, ngân hàng cổ, khách sạn và những tòa nhà từng thuộc về giới thương nhân giàu có thời Sa hoàng. Phố có nhiều đoạn dành cho người đi bộ, cây xanh, ghế nghỉ và các tác phẩm điêu khắc đường phố nhỏ, biến việc dạo bộ trở nên thú vị. Đây là tuyến đi bộ khám phá lý tưởng để cảm nhận lịch sử và nhịp sống đô thị của thành phố, kết nối tự nhiên các điểm tham quan trung tâm từ quảng trường Lenin đến bờ kè sông Amur.",
    [
        "Con phố chính, lâu đời và đẹp nhất Khabarovsk.",
        "Dãy nhà gạch trang trí cầu kỳ cuối thế kỷ 19 - đầu thế kỷ 20.",
        "Trục đi bộ nối quảng trường Lenin với quảng trường Nhà thờ và bờ kè.",
    ],
    {
        "hours_vi": "Phố mở tự do 24/24; cửa hàng, quán theo giờ riêng.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "1–1,5 giờ đi dạo.",
        "best_time_vi": "Quanh năm; chiều tối lên đèn rất đẹp.",
        "tips_vi": "Đi bộ toàn tuyến để ngắm kiến trúc; kết hợp quảng trường Lenin, quảng trường Nhà thờ và bờ kè.",
    },
    [
        {"title": "Wikipedia (RU) — Улица Муравьёва-Амурского", "url": "https://ru.wikipedia.org/wiki/Улица_Муравьёва-Амурского_(Хабаровск)"},
    ],
    ["street", "historic", "architecture", "khabarovsk", "walking", "center"],
    maps_text("Улица Муравьёва-Амурского", "Хабаровск", "Muravyov-Amursky Street", "Khabarovsk", 48.47800, 135.06400),
))

# 13) Театр драмы -------------------------------------------------------------------
RECORDS.append(rec(
    "drama-theatre-khabarovsk",
    "Nhà hát Kịch vùng Khabarovsk",
    "Хабаровский краевой театр драмы",
    "Khabarovsk Regional Drama Theatre",
    ["theatre"],
    48.47808, 135.065885,
    "Đại lộ Muravyov-Amursky 25, trung tâm Khabarovsk, Vùng Khabarovsk, Nga.",
    "Nhà hát Kịch vùng Khabarovsk là một trong những nhà hát lâu đời và uy tín nhất vùng Viễn Đông, tọa lạc ngay trên đại lộ trung tâm. Chương trình gồm kịch cổ điển Nga - thế giới và các vở đương đại.",
    "Nhà hát Kịch vùng Khabarovsk là một trong những sân khấu chuyên nghiệp lâu đời và có tiếng nhất ở vùng Viễn Đông Nga, nằm ngay trên đại lộ trung tâm Muravyov-Amursky, thuận tiện cho du khách. Với lịch sử kéo dài nhiều thập niên, nhà hát duy trì một đoàn kịch mạnh và chương trình phong phú, từ các tác phẩm kinh điển của văn học kịch Nga (Chekhov, Ostrovsky, Gogol) đến kịch thế giới và những vở đương đại. Không gian khán phòng ấm cúng cùng chất lượng dàn dựng ổn định khiến nhà hát trở thành điểm đến văn hóa quan trọng của người dân thành phố suốt mùa diễn. Đối với du khách, một buổi tối xem kịch tại đây không chỉ là trải nghiệm nghệ thuật mà còn là cách hòa vào đời sống văn hóa bản địa của Khabarovsk. Nhà hát cũng thường tham gia các liên hoan sân khấu vùng và toàn Nga, góp phần khẳng định vị thế của thành phố như một trung tâm văn hóa của miền Viễn Đông. Vị trí ngay trên trục phố chính giúp dễ dàng kết hợp với hành trình dạo bộ trung tâm.",
    [
        "Một trong những nhà hát kịch lâu đời, uy tín nhất vùng Viễn Đông.",
        "Chương trình đa dạng: kinh điển Nga, kịch thế giới và vở đương đại.",
        "Vị trí ngay trên đại lộ trung tâm Muravyov-Amursky.",
    ],
    {
        "hours_vi": "Biểu diễn theo lịch mùa diễn (thường tối và cuối tuần); phòng vé mở ban ngày.",
        "ticket_vi": "Vé theo vở và vị trí ghế, giá phải chăng.",
        "duration_vi": "2–3 giờ mỗi buổi diễn.",
        "best_time_vi": "Mùa diễn thu - đông - xuân; nghỉ hè.",
        "tips_vi": "Đặt vé trước qua trang chính thức; kết hợp dạo đại lộ trung tâm trước hoặc sau buổi diễn.",
    },
    [
        {"title": "Wikipedia (RU) — Хабаровский краевой театр драмы", "url": "https://ru.wikipedia.org/wiki/Хабаровский_краевой_театр_драмы"},
    ],
    ["theatre", "drama", "culture", "khabarovsk", "center"],
    maps_text("Хабаровский краевой театр драмы", "Хабаровск", "Khabarovsk Drama Theatre", "Khabarovsk", 48.47808, 135.065885),
))

# 14) Музыкальный театр -------------------------------------------------------------
RECORDS.append(rec(
    "musical-theatre-khabarovsk",
    "Nhà hát Nhạc kịch vùng Khabarovsk",
    "Хабаровский краевой музыкальный театр",
    "Khabarovsk Regional Musical Theatre",
    ["theatre"],
    48.484617, 135.078779,
    "Phố Karl Marx 64, Khabarovsk, Vùng Khabarovsk, Nga.",
    "Nhà hát Nhạc kịch vùng Khabarovsk là một trong những nhà hát nhạc kịch lâu đời nhất vùng Viễn Đông, chuyên các vở operetta, nhạc kịch và hài kịch âm nhạc. Sân khấu sôi động, phù hợp cả khán giả gia đình.",
    "Nhà hát Nhạc kịch vùng Khabarovsk là một trong những nhà hát ca nhạc - operetta lâu đời và được yêu thích của vùng Viễn Đông, có lịch sử từ giữa thế kỷ 20. Nhà hát chuyên dàn dựng các thể loại giàu tính giải trí và âm nhạc: operetta cổ điển, nhạc kịch (musical), hài kịch âm nhạc, các vở nhạc kịch dành cho thiếu nhi cùng những chương trình hòa nhạc, tạp kỹ. Với dàn diễn viên biết hát - diễn - múa, dàn nhạc sống và những màn dàn dựng rực rỡ, nhà hát mang tới không khí sân khấu sôi động, dễ tiếp cận ngay cả với khán giả không thạo tiếng Nga, đặc biệt hợp với các gia đình có trẻ em. Đây là một điểm đến văn hóa quan trọng trong đời sống về đêm của Khabarovsk và thường xuyên có các vở diễn được người dân thành phố mến mộ. Với du khách, một buổi tối tại nhà hát nhạc kịch là cách thư giãn thú vị, đầy màu sắc để cảm nhận tinh thần văn hóa nghệ thuật của thành phố bên sông Amur.",
    [
        "Nhà hát operetta - nhạc kịch lâu đời của vùng Viễn Đông.",
        "Chuyên operetta, musical, hài kịch âm nhạc và nhạc kịch thiếu nhi.",
        "Sân khấu rực rỡ, dễ tiếp cận, phù hợp khán giả gia đình.",
    ],
    {
        "hours_vi": "Biểu diễn theo lịch mùa diễn; phòng vé mở ban ngày.",
        "ticket_vi": "Vé theo vở và vị trí ghế, giá phải chăng.",
        "duration_vi": "2–2,5 giờ mỗi buổi diễn.",
        "best_time_vi": "Mùa diễn thu - đông - xuân.",
        "tips_vi": "Chọn vở operetta hoặc nhạc kịch nếu chưa thạo tiếng Nga; đặt vé trước cuối tuần.",
    },
    [
        {"title": "Wikipedia (RU) — Хабаровский краевой музыкальный театр", "url": "https://ru.wikipedia.org/wiki/Хабаровский_краевой_музыкальный_театр"},
    ],
    ["theatre", "musical", "operetta", "culture", "khabarovsk"],
    maps_text("Хабаровский краевой музыкальный театр", "Хабаровск", "Khabarovsk Musical Theatre", "Khabarovsk", 48.484617, 135.078779),
))

# 15) Краевая филармония ------------------------------------------------------------
RECORDS.append(rec(
    "philharmonic-khabarovsk",
    "Nhạc viện - Phòng hòa nhạc vùng Khabarovsk (Philharmonia)",
    "Хабаровская краевая филармония",
    "Khabarovsk Regional Philharmonic",
    ["theatre"],
    48.473129, 135.052338,
    "Phố Shevchenko 7, trung tâm Khabarovsk, Vùng Khabarovsk, Nga.",
    "Philharmonia vùng Khabarovsk là trung tâm âm nhạc hàn lâm của thành phố, nơi trình diễn nhạc giao hưởng, thính phòng, hợp xướng và dân ca. Đại sảnh hòa nhạc nằm trong tòa nhà lịch sử ở khu trung tâm.",
    "Philharmonia (Nhà hát giao hưởng - hòa nhạc) vùng Khabarovsk là trung tâm âm nhạc hàn lâm hàng đầu của thành phố và vùng, quy tụ các tập thể biểu diễn chuyên nghiệp như dàn nhạc giao hưởng, dàn nhạc dân tộc, các nhóm thính phòng, hợp xướng và nghệ sĩ độc tấu. Đặt trong một tòa nhà lịch sử duyên dáng ở khu trung tâm, gần cụm bảo tàng phố Shevchenko và bờ kè, Philharmonia tổ chức quanh mùa các buổi hòa nhạc giao hưởng, chương trình nhạc cổ điển thế giới và Nga, nhạc dân gian vùng Viễn Đông, cũng như các sự kiện dành cho thiếu nhi và gia đình. Với âm học tốt và không khí trang trọng, đây là điểm đến của những ai muốn thưởng thức âm nhạc cổ điển đích thực khi ở Khabarovsk, đồng thời là nơi ươm mầm và tôn vinh các tài năng âm nhạc địa phương. Việc thưởng thức một buổi hòa nhạc ở đây, với vị trí trung tâm dễ tiếp cận, là cách kết hợp trải nghiệm văn hóa tinh tế vào hành trình khám phá thành phố.",
    [
        "Trung tâm âm nhạc hàn lâm của Khabarovsk và vùng Viễn Đông.",
        "Nhạc giao hưởng, thính phòng, hợp xướng và dân ca vùng Amur.",
        "Đại sảnh trong tòa nhà lịch sử ngay khu trung tâm.",
    ],
    {
        "hours_vi": "Hòa nhạc theo lịch mùa diễn; phòng vé mở ban ngày.",
        "ticket_vi": "Vé theo chương trình, giá phải chăng.",
        "duration_vi": "1,5–2 giờ mỗi buổi.",
        "best_time_vi": "Mùa diễn thu - đông - xuân.",
        "tips_vi": "Xem lịch để chọn chương trình phù hợp; gần cụm bảo tàng phố Shevchenko và bờ kè.",
    },
    [
        {"title": "Wikipedia (RU) — Хабаровская краевая филармония", "url": "https://ru.wikipedia.org/wiki/Хабаровская_краевая_филармония"},
    ],
    ["philharmonic", "concert-hall", "classical-music", "culture", "khabarovsk"],
    maps_text("Хабаровская краевая филармония", "Хабаровск", "Khabarovsk Philharmonic", "Khabarovsk", 48.473129, 135.052338),
))

# 16) Христорождественский собор ----------------------------------------------------
RECORDS.append(rec(
    "christ-nativity-cathedral-khabarovsk",
    "Nhà thờ chính tòa Chúa Giáng Sinh",
    "Христорождественский собор",
    "Cathedral of the Nativity of Christ",
    ["church"],
    48.494582, 135.078976,
    "Phố Leningradskaya 65, Khabarovsk, Vùng Khabarovsk, Nga.",
    "Nhà thờ Chúa Giáng Sinh là một trong những nhà thờ Chính thống giáo lâu đời còn hoạt động liên tục của Khabarovsk, khởi nguồn từ đầu thế kỷ 20. Ngôi đền mái vòm xanh - vàng là điểm hành hương quen thuộc của người dân.",
    "Nhà thờ chính tòa Chúa Giáng Sinh (Khristorozhdestvensky) là một trong những nhà thờ Chính thống giáo giàu lịch sử và được người dân Khabarovsk gắn bó nhất, nằm ở khu vực phía bắc trung tâm thành phố. Ngôi đền có nguồn gốc từ đầu thế kỷ 20, ban đầu là nhà thờ nghĩa trang, và là một trong số ít thánh đường của thành phố duy trì được hoạt động thờ phượng gần như liên tục qua cả thời kỳ Xô Viết khi phần lớn các nhà thờ khác bị đóng cửa hay phá hủy. Chính vì thế, trong nhiều thập niên đây từng đóng vai trò như nhà thờ chính (cathedral) của Khabarovsk trước khi các thánh đường lớn được phục dựng. Công trình mang dáng vẻ Chính thống giáo Nga truyền thống với các mái vòm hành, tường sáng màu và không gian nội thất ấm áp với các bức icon, đèn nến. Với bề dày lịch sử và ý nghĩa tâm linh đặc biệt, nhà thờ là điểm đến cho những ai muốn tìm hiểu đời sống tôn giáo bản địa hoặc chiêm nghiệm trong không gian tĩnh lặng, tách khỏi nhịp sống sôi động của trung tâm thành phố.",
    [
        "Một trong những nhà thờ hoạt động liên tục lâu đời nhất Khabarovsk.",
        "Từng đóng vai trò nhà thờ chính của thành phố qua thời Xô Viết.",
        "Kiến trúc Chính thống giáo Nga truyền thống với mái vòm hành.",
    ],
    {
        "hours_vi": "Mở hằng ngày theo giờ lễ, thường khoảng 8:00–19:00.",
        "ticket_vi": "Miễn phí (nơi thờ phượng đang hoạt động).",
        "duration_vi": "30 phút.",
        "best_time_vi": "Quanh năm; các dịp lễ lớn Chính thống giáo có không khí đặc biệt.",
        "tips_vi": "Ăn mặc kín đáo, nữ nên mang khăn trùm đầu; giữ yên tĩnh và xin phép trước khi chụp ảnh bên trong.",
    },
    [
        {"title": "Wikipedia (RU) — Христорождественский собор (Хабаровск)", "url": "https://ru.wikipedia.org/wiki/Христорождественский_собор_(Хабаровск)"},
        {"title": "Sobory.ru — Хабаровск", "url": "https://sobory.ru/geo/city/Хабаровск"},
    ],
    ["church", "cathedral", "orthodox", "khabarovsk", "historic"],
    maps_text("Христорождественский собор", "Хабаровск", "Cathedral of the Nativity", "Khabarovsk", 48.494582, 135.078976),
))

# 17) Иннокентьевская церковь -------------------------------------------------------
RECORDS.append(rec(
    "innokentievsky-church-khabarovsk",
    "Nhà thờ Thánh Innokenty vùng Irkutsk (Innokentievskaya)",
    "Иннокентьевская церковь (Храм святителя Иннокентия Иркутского)",
    "Innokentievsky Church (St. Innocent of Irkutsk)",
    ["church"],
    48.47651, 135.050541,
    "Phố Turgeneva 73B, gần bờ kè, Khabarovsk, Vùng Khabarovsk, Nga.",
    "Nhà thờ Thánh Innokenty là nhà thờ bằng đá đầu tiên của Khabarovsk, xây dựng cuối thế kỷ 19. Ngôi đền cổ kính gần bờ kè là một trong những di tích kiến trúc tôn giáo quý giá nhất thành phố.",
    "Nhà thờ Thánh Innokenty vùng Irkutsk (Innokentievskaya) là ngôi nhà thờ bằng đá đầu tiên của Khabarovsk, được xây dựng và thánh hiến vào cuối thế kỷ 19, thay thế cho nhà thờ gỗ cũ trước đó. Nằm ở khu vực gần bờ kè sông Amur trong trung tâm lịch sử, đây là một trong những công trình tôn giáo cổ nhất còn lại của thành phố và mang giá trị di sản kiến trúc đặc biệt. Trong thời kỳ Xô Viết, nhà thờ bị đóng cửa và chuyển đổi công năng - từng được dùng làm cơ sở của đài thiên văn, khiến hình dáng bên ngoài bị thay đổi. Sau khi được trao trả lại cho Giáo hội vào thập niên 1990, ngôi đền được trùng tu, phục dựng những mái vòm và tháp chuông đặc trưng, trở lại vẻ đẹp Chính thống giáo Nga truyền thống với tường sơn màu tươi sáng và các mái vòm mạ vàng. Ngày nay nhà thờ là nơi hành lễ đang hoạt động, đồng thời là một điểm tham quan giàu ý nghĩa lịch sử cho du khách muốn tìm hiểu về những ngày đầu của Khabarovsk. Vị trí gần bờ kè giúp dễ dàng kết hợp trong tuyến dạo trung tâm.",
    [
        "Nhà thờ bằng đá đầu tiên của Khabarovsk (cuối thế kỷ 19).",
        "Từng bị dùng làm đài thiên văn thời Xô Viết, sau được phục dựng.",
        "Di tích kiến trúc tôn giáo cổ, gần bờ kè trung tâm.",
    ],
    {
        "hours_vi": "Mở hằng ngày theo giờ lễ, thường khoảng 8:00–19:00.",
        "ticket_vi": "Miễn phí (nơi thờ phượng đang hoạt động).",
        "duration_vi": "20–30 phút.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Ăn mặc kín đáo, nữ nên mang khăn trùm đầu; kết hợp bờ kè và cụm trung tâm ngay gần.",
    },
    [
        {"title": "Wikipedia (RU) — Иннокентьевская церковь (Хабаровск)", "url": "https://ru.wikipedia.org/wiki/Иннокентьевская_церковь_(Хабаровск)"},
        {"title": "Sobory.ru — Хабаровск", "url": "https://sobory.ru/geo/city/Хабаровск"},
    ],
    ["church", "orthodox", "oldest", "khabarovsk", "historic", "heritage"],
    maps_text("Иннокентьевская церковь", "Хабаровск", "Innokentievsky Church", "Khabarovsk", 48.47651, 135.050541),
))

# 18) Зоосад «Приамурский» им. Сысоева ----------------------------------------------
RECORDS.append(rec(
    "priamursky-zoo-khabarovsk",
    "Vườn thú Priamursky mang tên Sysoev",
    "Зоосад «Приамурский» имени В.П. Сысоева",
    "Priamursky Zoo named after V.P. Sysoev",
    ["park_garden"],
    48.622249, 135.069568,
    "Làng Voronezhskoye-2, ngoại ô phía bắc Khabarovsk, Vùng Khabarovsk, Nga.",
    "Vườn thú Priamursky nằm giữa rừng taiga ngoại ô Khabarovsk, chuyên nuôi giữ động vật bản địa vùng Viễn Đông - Amur như hổ Amur, gấu, báo, sói. Đặc điểm nổi bật: chỉ nhận thú không thể thả về tự nhiên.",
    "Vườn thú Priamursky mang tên nhà văn - nhà tự nhiên học V.P. Sysoev là một vườn thú độc đáo nằm giữa rừng taiga ở ngoại ô phía bắc Khabarovsk, gần làng Voronezhskoye-2. Điểm đặc biệt của vườn thú là chỉ tiếp nhận và nuôi giữ những con thú không còn khả năng sống sót trong tự nhiên - thú bị thương, mồ côi, hoặc bị tịch thu từ nạn săn bắt trái phép - vì thế nơi đây vừa là điểm tham quan vừa là trung tâm cứu hộ, bảo tồn. Bộ sưu tập tập trung vào hệ động vật đặc trưng của vùng Amur - Ussuri và Viễn Đông: hổ Amur uy nghi, báo Viễn Đông cực hiếm, gấu nâu và gấu ngựa, sói, linh miêu, đại bàng, cùng nhiều loài chim và thú khác. Các chuồng trại rộng, đặt ngay trong khung cảnh rừng tự nhiên, giúp du khách quan sát động vật trong môi trường gần với sinh cảnh thật. Đây là điểm đến lý tưởng cho gia đình có trẻ em và những ai muốn tận mắt thấy những loài mãnh thú biểu tượng của vùng Viễn Đông mà không phải vào rừng sâu, đồng thời hiểu thêm về công tác bảo tồn thiên nhiên nơi đây.",
    [
        "Chỉ nuôi giữ thú không thể thả về tự nhiên - vừa tham quan vừa cứu hộ.",
        "Hổ Amur, báo Viễn Đông hiếm, gấu, sói và động vật bản địa vùng Amur.",
        "Chuồng trại đặt giữa rừng taiga, gần với sinh cảnh tự nhiên.",
    ],
    {
        "hours_vi": "Thường mở ban ngày (khoảng 9:00/10:00–18:00), giờ có thể đổi theo mùa.",
        "ticket_vi": "Có thu vé; ưu đãi cho trẻ em.",
        "duration_vi": "1,5–2 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu; mùa đông thú vẫn xem được nhưng lạnh.",
        "tips_vi": "Cách trung tâm khoảng 25–30 km, nên đi ô tô/taxi hoặc tour; mang giày đi bộ và đồ ấm.",
    },
    [
        {"title": "Wikipedia (RU) — Приамурский зоосад", "url": "https://ru.wikipedia.org/wiki/Приамурский_зоосад"},
    ],
    ["zoo", "wildlife", "amur-tiger", "conservation", "khabarovsk", "family"],
    maps_text("Зоосад Приамурский имени Сысоева", "Хабаровск", "Priamursky Zoo Sysoev", "Khabarovsk", 48.622249, 135.069568),
))

# 19) Амурские столбы ---------------------------------------------------------------
RECORDS.append(rec(
    "amur-pillars",
    "Cột đá Amur (Amurskie Stolby)",
    "Амурские столбы",
    "Amur Pillars (Amurskie Stolby)",
    ["park_garden", "other"],
    51.06111, 138.14722,
    "Gần làng Nizhnetambovskoye, huyện Komsomolsky, Vùng Khabarovsk, Nga (bờ phải sông Amur).",
    "Cột đá Amur là quần thể những khối đá granit khổng lồ hình thù kỳ lạ mọc trên đỉnh đồi rừng taiga bên bờ phải sông Amur. Đây là một trong những kỳ quan thiên nhiên và điểm trekking nổi tiếng nhất vùng Khabarovsk.",
    "Cột đá Amur (Amurskie Stolby) là một quần thể kỳ quan thiên nhiên gồm những khối đá granit khổng lồ, cao tới hàng chục mét, mọc lên giữa rừng taiga trên một sườn núi ở bờ phải sông Amur, cách làng Nizhnetambovskoye thuộc huyện Komsomolsky không xa. Qua hàng triệu năm phong hóa, các khối đá tạo nên những hình thù kỳ dị được người dân đặt tên gợi hình như 'Đầu lâu', 'Người canh gác', 'Cây nấm'... nổi bật giữa biển rừng xanh. Nơi đây gắn với nhiều truyền thuyết của các dân tộc bản địa vùng Amur và từ lâu được coi là chốn linh thiêng. Để lên tới quần thể cột đá, du khách thường đi thuyền trên sông Amur rồi trekking ngược lên sườn núi qua rừng taiga - một hành trình đòi hỏi thể lực nhưng phần thưởng là khung cảnh hùng vĩ với những tháp đá sừng sững và tầm nhìn bao la xuống dòng Amur cùng biển rừng bất tận. Đây là điểm đến được giới yêu thiên nhiên, trekking và nhiếp ảnh đặc biệt yêu thích, tiêu biểu cho vẻ đẹp hoang sơ, kỳ vĩ của thiên nhiên vùng Viễn Đông Nga.",
    [
        "Quần thể cột đá granit khổng lồ hình thù kỳ lạ giữa rừng taiga.",
        "Gắn với truyền thuyết linh thiêng của các dân tộc bản địa Amur.",
        "Điểm trekking - nhiếp ảnh hùng vĩ với tầm nhìn bao la ra sông Amur.",
    ],
    {
        "hours_vi": "Khu thiên nhiên ngoài trời, không có giờ cố định; đi vào ban ngày.",
        "ticket_vi": "Không thu vé cố định; chi phí chủ yếu là thuyền và tour dẫn đường.",
        "duration_vi": "Cả ngày hoặc chuyến 2 ngày (gồm di chuyển đường sông và trekking).",
        "best_time_vi": "Mùa hè và đầu thu (tháng 6–9) khi sông thông thuyền và đường mòn khô ráo.",
        "tips_vi": "Nên đi theo tour có hướng dẫn địa phương; chuẩn bị giày trekking, nước, chống côn trùng và đồ ấm; kiểm tra thời tiết sông.",
    },
    [
        {"title": "Wikipedia (RU) — Амурские столбы", "url": "https://ru.wikipedia.org/wiki/Амурские_столбы"},
    ],
    ["nature", "rock-formation", "granite", "trekking", "amur", "khabarovsk"],
    maps_text("Амурские столбы", "Нижнетамбовское", "Amur Pillars", "Nizhnetambovskoye", 51.06111, 138.14722),
))

# 20) Национальный парк «Шантарские острова» ----------------------------------------
RECORDS.append(rec(
    "shantar-islands-national-park",
    "Vườn quốc gia Quần đảo Shantar",
    "Национальный парк «Шантарские острова»",
    "Shantar Islands National Park",
    ["park_garden"],
    55.0, 137.5,
    "Quần đảo Shantar trên biển Okhotsk, tây nam vịnh, Vùng Khabarovsk, Nga (điểm đại diện đảo Bolshoy Shantar).",
    "Vườn quốc gia Quần đảo Shantar là một quần đảo hoang sơ trên biển Okhotsk, nổi tiếng thế giới là nơi ngắm cá voi đầu cong (bowhead) và cá voi orca ở cự ly gần. Thiên nhiên nguyên vẹn với thác nước, vách đá, chim biển và hải cẩu.",
    "Vườn quốc gia Quần đảo Shantar là một trong những khu thiên nhiên hoang sơ và ngoạn mục nhất vùng Viễn Đông Nga, gồm khoảng 15 hòn đảo nằm ở phần tây nam của biển Okhotsk, thuộc Vùng Khabarovsk. Được thành lập làm vườn quốc gia năm 2013, quần đảo nổi tiếng toàn cầu là một trong những nơi hiếm hoi có thể ngắm cá voi hoang dã ở cự ly rất gần: cá voi đầu cong (bowhead) khổng lồ, cá voi xám, cùng những đàn cá voi sát thủ (orca) bơi lượn quanh các eo biển. Vùng biển lạnh giàu dinh dưỡng và những dòng thủy triều mạnh tạo nên hệ sinh thái phong phú với hải cẩu, sư tử biển, hàng vạn chim biển làm tổ trên vách đá, cùng cảnh quan đảo hùng vĩ: vách đá dựng đứng nhiều màu, thác nước đổ xuống biển, hồ nước ngọt và rừng taiga nguyên sinh. Do vị trí xa xôi và khí hậu khắc nghiệt, việc tới Shantar là một cuộc phiêu lưu thực sự - thường theo các tour thám hiểm chuyên biệt bằng đường không kết hợp đường thủy trong khoảng thời gian ngắn ngủi mùa hè. Đây là điểm đến trong mơ của những người mê thiên nhiên hoang dã, ngắm cá voi và nhiếp ảnh động vật.",
    [
        "Một trong những nơi ngắm cá voi đầu cong và orca gần bờ tốt nhất thế giới.",
        "Thiên nhiên hoang sơ: vách đá nhiều màu, thác đổ ra biển, chim biển, hải cẩu.",
        "Vườn quốc gia (2013) trên biển Okhotsk, hành trình thám hiểm đích thực.",
    ],
    {
        "hours_vi": "Khu bảo tồn hoang dã, tiếp cận theo mùa; cần xin phép vào vườn quốc gia.",
        "ticket_vi": "Cần giấy phép vào vườn quốc gia và thường đi qua tour trọn gói (chi phí cao).",
        "duration_vi": "Chuyến nhiều ngày (thường tour 7–12 ngày).",
        "best_time_vi": "Mùa hè ngắn (tháng 7–9) khi biển bớt băng và cá voi vào gần bờ.",
        "tips_vi": "Chỉ nên đi theo tour thám hiểm chuyên nghiệp; chuẩn bị đồ chống lạnh, chống ẩm; đặt chỗ sớm vì mùa và số suất rất hạn chế.",
    },
    [
        {"title": "Wikipedia (RU) — Шантарские острова", "url": "https://ru.wikipedia.org/wiki/Шантарские_острова"},
        {"title": "Wikipedia (RU) — Национальный парк «Шантарские острова»", "url": "https://ru.wikipedia.org/wiki/Шантарские_острова_(национальный_парк)"},
    ],
    ["national-park", "whales", "okhotsk-sea", "wilderness", "islands", "khabarovsk"],
    maps_text("Шантарские острова", "Хабаровский край", "Shantar Islands", "Khabarovsk Krai", 55.0, 137.5),
))

# 21) Комсомольский заповедник ------------------------------------------------------
RECORDS.append(rec(
    "komsomolsky-reserve",
    "Khu bảo tồn thiên nhiên Komsomolsky",
    "Комсомольский заповедник",
    "Komsomolsky Nature Reserve",
    ["park_garden"],
    50.809996, 137.719214,
    "Cửa sông Gorin đổ vào Amur, gần Komsomolsk-on-Amur, Vùng Khabarovsk, Nga.",
    "Khu bảo tồn thiên nhiên Komsomolsky bảo vệ vùng rừng taiga và đầm lầy hạ lưu sông Gorin nơi đổ vào Amur, gần Komsomolsk-on-Amur. Nơi trú ngụ của hổ Amur, gấu, cá hồi di cư và nhiều loài chim quý.",
    "Khu bảo tồn thiên nhiên Komsomolsky (zapovednik) được thành lập năm 1963 nhằm bảo vệ những hệ sinh thái đặc trưng của vùng hạ lưu Amur, trải dọc vùng cửa sông Gorin - một phụ lưu lớn - nơi đổ vào dòng Amur, không xa thành phố Komsomolsk-on-Amur. Khu bảo tồn ôm trọn một khảm sinh cảnh phong phú: rừng taiga lá kim và rừng hỗn giao, các bãi bồi, đầm lầy, hồ và mạng lưới lạch nước ven sông. Đây là địa bàn sinh sống của nhiều loài thú lớn tiêu biểu vùng Viễn Đông như hổ Amur, gấu nâu và gấu ngựa, nai, lợn rừng, cùng hệ chim nước và chim rừng đa dạng. Một giá trị đặc biệt của khu bảo tồn là vai trò trong vòng đời của các loài cá hồi Viễn Đông (như cá hồi keta) di cư ngược sông Gorin để sinh sản, kéo theo cả một chuỗi sinh thái phụ thuộc. Với địa hình sông nước và rừng nguyên sinh, Komsomolsky là điểm nghiên cứu, du lịch sinh thái có kiểm soát, dành cho những ai muốn tìm hiểu và chiêm ngưỡng thiên nhiên hoang dã đặc trưng của lưu vực Amur.",
    [
        "Bảo vệ rừng taiga và đầm lầy vùng cửa sông Gorin đổ vào Amur.",
        "Nơi sống của hổ Amur, gấu, nai và hệ chim nước phong phú.",
        "Quan trọng cho vòng đời cá hồi Viễn Đông di cư sinh sản.",
    ],
    {
        "hours_vi": "Khu bảo tồn nghiêm ngặt; tham quan phải xin phép và đi theo tuyến du lịch sinh thái được duyệt.",
        "ticket_vi": "Cần đăng ký, xin phép trước với ban quản lý; có thể thu phí tuyến sinh thái.",
        "duration_vi": "Nửa ngày đến vài ngày tùy tuyến.",
        "best_time_vi": "Cuối hè - đầu thu, đặc biệt mùa cá hồi di cư; tránh mùa lũ.",
        "tips_vi": "Liên hệ ban quản lý ở Komsomolsk-on-Amur trước; đi cùng kiểm lâm/hướng dẫn, chuẩn bị chống muỗi và đồ đi rừng.",
    },
    [
        {"title": "Wikipedia (RU) — Комсомольский заповедник", "url": "https://ru.wikipedia.org/wiki/Комсомольский_заповедник"},
    ],
    ["nature-reserve", "taiga", "amur-tiger", "salmon", "gorin", "khabarovsk"],
    maps_text("Комсомольский заповедник", "Комсомольск-на-Амуре", "Komsomolsky Nature Reserve", "Komsomolsk-on-Amur", 50.809996, 137.719214),
))

# 22) Анненские минеральные воды ----------------------------------------------------
RECORDS.append(rec(
    "anninskie-mineral-waters",
    "Suối khoáng nóng Anninskie (Anninskie Vody)",
    "Анненские (Аннинские) минеральные воды",
    "Anninskie Mineral Waters (thermal springs)",
    ["other"],
    52.766599, 140.170701,
    "Làng Anninskiye Vody, huyện Ulchsky, Vùng Khabarovsk, Nga.",
    "Anninskie Vody là khu suối khoáng nóng và nghỉ dưỡng lâu đời ở huyện Ulchsky, hạ lưu Amur. Nguồn nước khoáng nóng silic - nitơ được dùng chữa bệnh, tắm trị liệu giữa khung cảnh rừng taiga.",
    "Anninskie (còn viết Annenskie) Vody là một trong những khu suối khoáng nóng và điều dưỡng lâu đời nhất vùng Viễn Đông, nằm ở huyện Ulchsky thuộc vùng hạ lưu sông Amur của Vùng Khabarovsk. Nguồn nước khoáng nóng ở đây thuộc loại nước nóng silic - nitơ với nhiệt độ tự nhiên cao, được phát hiện và khai thác cho mục đích chữa bệnh từ hơn một thế kỷ trước; quanh nguồn nước đã hình thành một khu an dưỡng (sanatorium) với các bể tắm, phòng trị liệu và nhà nghỉ. Nước khoáng nóng tại Anninskie Vody được sử dụng để tắm ngâm và điều trị hỗ trợ nhiều chứng bệnh về xương khớp, thần kinh, da liễu và tuần hoàn, theo phương pháp điều dưỡng đặc trưng của Nga. Điểm hấp dẫn của nơi đây là sự kết hợp giữa liệu pháp suối nóng và khung cảnh thiên nhiên taiga yên tĩnh, xa rời phố thị, mang lại trải nghiệm nghỉ dưỡng - phục hồi sức khỏe độc đáo giữa vùng Viễn Đông xa xôi. Đây là điểm đến cho những ai quan tâm tới du lịch nghỉ dưỡng, chữa lành và trải nghiệm văn hóa an dưỡng kiểu Nga.",
    [
        "Suối khoáng nóng silic - nitơ với khu an dưỡng lâu đời hơn một thế kỷ.",
        "Tắm ngâm, trị liệu hỗ trợ xương khớp, thần kinh, da liễu.",
        "Nghỉ dưỡng giữa khung cảnh rừng taiga yên tĩnh vùng hạ lưu Amur.",
    ],
    {
        "hours_vi": "Hoạt động theo lịch của khu an dưỡng; liên hệ trước khi tới.",
        "ticket_vi": "Theo gói dịch vụ tắm/điều dưỡng của sanatorium.",
        "duration_vi": "Từ nửa ngày đến lưu trú nhiều ngày theo liệu trình.",
        "best_time_vi": "Quanh năm; mùa đông tắm suối nóng giữa tuyết là trải nghiệm đặc biệt.",
        "tips_vi": "Ở xa và khó tiếp cận, nên sắp xếp phương tiện và đặt chỗ trước; tham khảo ý kiến y tế nếu có bệnh nền.",
    },
    [
        {"title": "Wikipedia (RU) — Аннинские Минеральные Воды", "url": "https://ru.wikipedia.org/wiki/Аннинские_Минеральные_Воды"},
    ],
    ["thermal-springs", "spa", "sanatorium", "wellness", "ulchsky", "khabarovsk"],
    maps_text("Анненские минеральные воды", "Хабаровский край", "Anninskie Mineral Waters", "Khabarovsk Krai", 52.766599, 140.170701),
))

# 23) Комсомольский-на-Амуре краеведческий музей ------------------------------------
RECORDS.append(rec(
    "komsomolsk-local-lore-museum",
    "Bảo tàng địa phương Komsomolsk-on-Amur",
    "Комсомольский-на-Амуре краеведческий музей",
    "Komsomolsk-on-Amur Museum of Local Lore",
    ["museum"],
    50.543852, 137.029816,
    "Trung tâm Komsomolsk-on-Amur, Vùng Khabarovsk, Nga.",
    "Bảo tàng địa phương Komsomolsk-on-Amur kể câu chuyện thành phố công nghiệp trẻ được dựng lên từ rừng taiga hoang vu năm 1932 bởi các đoàn thanh niên Komsomol. Trưng bày thiên nhiên, dân tộc bản địa Nanai và lịch sử xây dựng thành phố.",
    "Bảo tàng địa phương (kraevedcheskiy) thành phố Komsomolsk-on-Amur là điểm đến chủ chốt để hiểu về một trong những thành phố công nghiệp mang tính biểu tượng nhất thời Xô Viết. Được khai sinh năm 1932, khi những đoàn thanh niên Komsomol tới dựng thành phố và các nhà máy khổng lồ giữa vùng rừng taiga hoang vu bên bờ sông Amur, Komsomolsk-on-Amur mang một huyền thoại 'thành phố tuổi trẻ' đặc biệt. Bảo tàng tái hiện toàn cảnh câu chuyện đó qua các gian trưng bày: thiên nhiên và địa lý vùng hạ Amur; văn hóa của các dân tộc bản địa như người Nanai với nghề cá, trang phục thêu và tín ngưỡng; và đặc biệt là lịch sử hào hùng cùng gian khổ của công cuộc xây dựng thành phố - những lán trại đầu tiên, dụng cụ lao động, ảnh tư liệu, và câu chuyện của các nhà máy đóng tàu, chế tạo máy bay. Các gian về thời Thế chiến II và giai đoạn phát triển sau chiến tranh cho thấy vai trò công nghiệp - quốc phòng quan trọng của thành phố. Đây là nơi lý tưởng để du khách hiểu vì sao Komsomolsk-on-Amur được gọi là 'thành phố do tuổi trẻ dựng nên' và cảm nhận tinh thần của cả một thời đại.",
    [
        "Kể câu chuyện thành phố 'do tuổi trẻ Komsomol dựng nên' từ năm 1932.",
        "Trưng bày văn hóa dân tộc bản địa Nanai vùng hạ lưu Amur.",
        "Lịch sử xây dựng, công nghiệp đóng tàu - chế tạo máy bay của thành phố.",
    ],
    {
        "hours_vi": "Thường mở 10:00–18:00, nghỉ đầu tuần (kiểm tra lịch).",
        "ticket_vi": "Vé phổ thông giá thấp; ưu đãi học sinh, sinh viên.",
        "duration_vi": "1–1,5 giờ.",
        "best_time_vi": "Quanh năm; phù hợp mọi mùa.",
        "tips_vi": "Kết hợp Bảo tàng Mỹ thuật và bờ kè Komsomolsk; hỏi thuyết minh phần lịch sử xây dựng thành phố.",
    },
    [
        {"title": "Wikipedia (RU) — Комсомольск-на-Амуре", "url": "https://ru.wikipedia.org/wiki/Комсомольск-на-Амуре"},
    ],
    ["museum", "local-lore", "komsomolsk", "nanai", "history", "far-east"],
    maps_text("Комсомольский-на-Амуре краеведческий музей", "Комсомольск-на-Амуре", "Komsomolsk Museum of Local Lore", "Komsomolsk-on-Amur", 50.543852, 137.029816),
))

# 24) Музей изобразительных искусств Комсомольска -----------------------------------
RECORDS.append(rec(
    "komsomolsk-fine-arts-museum",
    "Bảo tàng Mỹ thuật Komsomolsk-on-Amur",
    "Музей изобразительных искусств Комсомольска-на-Амуре",
    "Komsomolsk-on-Amur Museum of Fine Arts",
    ["museum"],
    50.538643, 137.025238,
    "Đại lộ Mira 16, Komsomolsk-on-Amur, Vùng Khabarovsk, Nga.",
    "Bảo tàng Mỹ thuật Komsomolsk-on-Amur là bảo tàng nghệ thuật hàng đầu của thành phố, nổi bật với bộ sưu tập nghệ thuật dân gian và ứng dụng của các dân tộc bản địa vùng hạ Amur như người Nanai, Ulchi, Nivkh.",
    "Bảo tàng Mỹ thuật thành phố Komsomolsk-on-Amur là một trong những bảo tàng nghệ thuật quan trọng của Vùng Khabarovsk, được thành lập vào nửa sau thế kỷ 20 và nằm trên đại lộ trung tâm Mira. Bộ sưu tập của bảo tàng khá đa dạng, gồm hội họa, đồ họa, điêu khắc và nghệ thuật trang trí - ứng dụng của các nghệ sĩ Nga và vùng Viễn Đông. Tuy nhiên, điều làm nên bản sắc riêng của bảo tàng chính là bộ sưu tập nghệ thuật dân gian và ứng dụng của các dân tộc bản địa vùng hạ lưu Amur - Sakhalin: các tác phẩm thêu, khảm da cá, chạm khắc gỗ và xương, trang phục truyền thống với hoa văn xoáy đặc trưng của người Nanai, Ulchi, Nivkh, Udege. Những hiện vật này thể hiện tài hoa và thế giới quan độc đáo của các cư dân sông nước Amur, giúp bảo tàng trở thành một trung tâm lưu giữ và tôn vinh di sản văn hóa nghệ thuật bản địa. Bảo tàng cũng tổ chức các triển lãm chuyên đề, hoạt động giáo dục và là điểm đến văn hóa hấp dẫn cho du khách khi ghé thăm thành phố tuổi trẻ bên sông Amur.",
    [
        "Bảo tàng nghệ thuật hàng đầu của Komsomolsk-on-Amur.",
        "Đặc sắc: nghệ thuật dân gian, khảm da cá, chạm khắc của người Nanai, Ulchi, Nivkh.",
        "Kết hợp hội họa, đồ họa, điêu khắc Nga và di sản bản địa Amur.",
    ],
    {
        "hours_vi": "Thường mở 10:00–18:00, nghỉ đầu tuần (kiểm tra lịch).",
        "ticket_vi": "Vé phổ thông giá thấp; ưu đãi học sinh, sinh viên.",
        "duration_vi": "1–1,5 giờ.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Ưu tiên xem khu nghệ thuật bản địa Amur; kết hợp Bảo tàng địa phương và bờ kè gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Музей изобразительных искусств Комсомольска-на-Амуре", "url": "https://ru.wikipedia.org/wiki/Музей_изобразительных_искусств_(Комсомольск-на-Амуре)"},
    ],
    ["museum", "fine-arts", "komsomolsk", "nanai", "folk-art", "far-east"],
    maps_text("Музей изобразительных искусств Комсомольска-на-Амуре", "Комсомольск-на-Амуре", "Komsomolsk Museum of Fine Arts", "Komsomolsk-on-Amur", 50.538643, 137.025238),
))

# 25) Набережная Комсомольска-на-Амуре ----------------------------------------------
RECORDS.append(rec(
    "komsomolsk-embankment",
    "Bờ kè sông Amur ở Komsomolsk-on-Amur",
    "Набережная Комсомольска-на-Амуре",
    "Komsomolsk-on-Amur Amur River Embankment",
    ["square_street", "park_garden"],
    50.530601, 137.026273,
    "Bờ sông Amur, gần bến tàu sông, Komsomolsk-on-Amur, Vùng Khabarovsk, Nga.",
    "Bờ kè Komsomolsk-on-Amur là trục dạo chơi ven sông Amur của thành phố, với đài tưởng niệm những người dựng thành, nhà ga sông và tầm nhìn thoáng ra dòng sông rộng. Là điểm hẹn và nghỉ ngơi được người dân yêu thích.",
    "Bờ kè sông Amur là không gian công cộng ven sông tiêu biểu của Komsomolsk-on-Amur, trải dài dọc dòng Amur hùng vĩ ngay cạnh trung tâm thành phố. Đây là nơi người dân và du khách tìm đến để tản bộ, hóng gió và ngắm khung cảnh mênh mông của con sông vốn là cội nguồn ra đời của thành phố. Điểm nhấn nổi bật trên bờ kè là đài tưởng niệm những người dựng thành đầu tiên (những đoàn thanh niên Komsomol đổ bộ lên bờ Amur năm 1932 để khai sinh thành phố) - một khối tượng đài mang tính biểu tượng nhìn ra sông. Dọc bờ kè là các lối đi lát đá, bậc thang xuống nước, luống hoa, ghế nghỉ, nhà ga sông (rechnoy vokzal) và các bến tàu, cùng tầm nhìn rộng mở về phía dòng Amur và bờ đối diện. Vào mùa hè, khu vực này sống động với người dạo chơi, các chuyến tàu sông và những buổi hoàng hôn tuyệt đẹp; mùa đông, mặt sông đóng băng tạo nên khung cảnh khác lạ. Bờ kè là nơi lý tưởng để cảm nhận nhịp sống và tinh thần 'thành phố tuổi trẻ' của Komsomolsk-on-Amur.",
    [
        "Trục dạo chơi ven sông Amur trung tâm của Komsomolsk-on-Amur.",
        "Đài tưởng niệm những người dựng thành đầu tiên năm 1932.",
        "Nhà ga sông, bến tàu và tầm nhìn thoáng ra dòng Amur.",
    ],
    {
        "hours_vi": "Không gian ngoài trời, mở tự do 24/24.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "45 phút–1,5 giờ.",
        "best_time_vi": "Chiều tối mùa hè (tháng 6–9) để ngắm hoàng hôn trên sông Amur.",
        "tips_vi": "Kết hợp đài tưởng niệm những người dựng thành và các bảo tàng trung tâm; mang áo khoác vì gió sông.",
    },
    [
        {"title": "Wikipedia (RU) — Комсомольск-на-Амуре", "url": "https://ru.wikipedia.org/wiki/Комсомольск-на-Амуре"},
    ],
    ["embankment", "promenade", "amur", "komsomolsk", "river", "viewpoint"],
    maps_text("Набережная Комсомольска-на-Амуре", "Комсомольск-на-Амуре", "Komsomolsk Amur Embankment", "Komsomolsk-on-Amur", 50.530601, 137.026273),
))

# 26) Озеро Амут --------------------------------------------------------------------
RECORDS.append(rec(
    "lake-amut",
    "Hồ Amut",
    "Озеро Амут",
    "Lake Amut",
    ["park_garden"],
    50.808889, 136.397222,
    "Dãy Myao-Chan, huyện Solnechny, gần khu Gorny Vozdukh, Vùng Khabarovsk, Nga.",
    "Hồ Amut là hồ núi trong vắt nằm giữa dãy Myao-Chan ở huyện Solnechny, được ví như 'viên ngọc' của vùng. Bao quanh bởi rừng taiga và núi non, đây là điểm du lịch sinh thái, trượt tuyết và nghỉ dưỡng nổi tiếng.",
    "Hồ Amut là một hồ núi tuyệt đẹp nằm ở độ cao khoảng 760 m giữa dãy Myao-Chan thuộc huyện Solnechny, không xa Komsomolsk-on-Amur. Hồ được hình thành do một khối trượt đất đá cổ chặn dòng suối, tạo nên một mặt nước trong vắt màu xanh ngọc lọt thỏm giữa những sườn núi phủ rừng taiga rậm rạp. Vẻ đẹp nguyên sơ và bầu không khí trong lành khiến Amut được người dân địa phương yêu quý gọi là 'viên ngọc' của vùng Priamurye. Quanh hồ là hệ động thực vật phong phú của rừng núi Viễn Đông; nước hồ lạnh và sâu, phản chiếu mây trời và núi non tạo nên khung cảnh nên thơ đặc biệt vào bình minh và hoàng hôn. Gần đó là khu nghỉ dưỡng - thể thao mùa đông 'Gorny Vozdukh' (Không khí núi) với các đường trượt tuyết, biến khu vực này thành điểm đến bốn mùa: mùa hè cho trekking, cắm trại, chèo thuyền và ngắm cảnh; mùa đông cho trượt tuyết và nghỉ dưỡng giữa rừng tuyết. Đây là một trong những viên ngọc thiên nhiên được yêu thích nhất của du lịch nội địa vùng Khabarovsk.",
    [
        "Hồ núi nước xanh ngọc trong vắt giữa dãy Myao-Chan, được ví như 'viên ngọc' của vùng.",
        "Hình thành do khối trượt đất đá cổ chặn dòng suối, độ cao khoảng 760 m.",
        "Điểm đến bốn mùa: trekking, cắm trại mùa hè; trượt tuyết mùa đông gần Gorny Vozdukh.",
    ],
    {
        "hours_vi": "Khu thiên nhiên ngoài trời, không giờ cố định.",
        "ticket_vi": "Không thu vé cố định; chi phí chủ yếu là di chuyển, tour hoặc dịch vụ khu nghỉ.",
        "duration_vi": "Nửa ngày đến vài ngày (kết hợp lưu trú).",
        "best_time_vi": "Mùa hè (tháng 7–9) cho trekking và cảnh hồ; mùa đông cho trượt tuyết.",
        "tips_vi": "Đường tới hồ gồ ghề, nên đi xe gầm cao hoặc tour; chuẩn bị đồ ấm, chống muỗi mùa hè; giữ gìn vệ sinh khu bảo tồn.",
    },
    [
        {"title": "Wikipedia (RU) — Амут (озеро)", "url": "https://ru.wikipedia.org/wiki/Амут_(озеро)"},
    ],
    ["lake", "mountain", "nature", "solnechny", "myao-chan", "khabarovsk"],
    maps_text("Озеро Амут", "Солнечный район", "Lake Amut", "Solnechny", 50.808889, 136.397222),
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
