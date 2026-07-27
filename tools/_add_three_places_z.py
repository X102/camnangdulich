# -*- coding: utf-8 -*-
"""_add_three_places_z.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26, buổi chiều).

Ưu tiên VÙNG: các thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.

Thêm:
  1) Tỉnh Moskva (moscow-oblast)     : Thành Zaraysk Kremlin (fortress/church/museum)
  2) Tỉnh Moskva (moscow-oblast)     : Tu viện Vysotsky ở Serpukhov (church/fortress)
  3) Tỉnh Leningrad (leningrad-oblast): Tu viện Alexander-Svirsky (church/monument)

LƯU Ý: Cung điện Gatchina KHÔNG thêm vào đây vì đã có sẵn trong saint-petersburg.json
(slug 'gatchina-palace') — tránh trùng; thay bằng Tu viện Alexander-Svirsky (thật sự còn thiếu).

Nội dung tiếng Việt nguyên gốc, có ghi nguồn. Toạ độ thật (đã đối chiếu web 2026-07,
Wikipedia/Wikidata + nguồn Nga). Link bản đồ theo dạng TRỎ-ĐỊA-ĐIỂM (khớp convention của
tools/retrofit_map_links.py: Yandex tìm theo tên Nga + vùng, canh giữa bằng ll=lon,lat).

Chạy:  python3 tools/_add_three_places_z.py
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-26"


def maps_for(name_ru, name_en, region_ru, region_en, lat, lon):
    """Trỏ thẳng tới địa điểm (khớp tools/retrofit_map_links.py để idempotent)."""
    yq = urllib.parse.quote(f"{name_ru}, {region_ru}")
    parts = [name_en]
    if region_en.lower() not in name_en.lower():
        parts.append(region_en)
    parts.append("Russia")
    gq = urllib.parse.quote(", ".join(parts))
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


# ------------------------------------------------------------------ RECORDS
ZARAYSK_KREMLIN = {
    "id": "moscow-oblast-zaraysk-kremlin",
    "slug": "zaraysk-kremlin",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Thành Zaraysk Kremlin (Zaraysky kreml)",
    "name_ru": "Зарайский кремль",
    "name_en": "Zaraysk Kremlin",
    "categories": ["fortress", "church", "museum"],
    "coordinates": {"lat": 54.75667, "lon": 38.86917},
    "address_vi": "Trung tâm lịch sử thành phố Zaraysk, Tỉnh Moskva; nằm trên bờ cao sông Osyotr gần nơi hợp lưu với sông Oka, cách Moskva khoảng 145 km về phía đông nam.",
    "rating": None,
    "presentation_short_vi": (
        "Toà thành gạch - đá vôi hình chữ nhật nhỏ nhắn nhưng là kremlin còn nguyên vẹn nhất "
        "trong số các thành cổ ở Tỉnh Moskva. Được xây năm 1528–1531 dưới thời Đại công tước "
        "Vasili III để trấn giữ tuyến phòng thủ phía nam Moskva trước các cuộc đột kích của "
        "quân Tatar Crimea. Bên trong vòng tường thành vẫn còn Nhà thờ chính toà Thánh Nikolai "
        "(1681) năm vòm hành và Nhà thờ Thánh Gioan Tiền Hô kiểu tân cổ điển."
    ),
    "presentation_long_vi": (
        "Zaraysk khởi đầu là Novgorodok-na-Osyotre, một tiền đồn của công quốc Ryazan; khi Ryazan "
        "mất độc lập và sáp nhập Đại công quốc Moskva năm 1503, vùng đất này trở thành tuyến đầu "
        "phía nam của Moskva. Để thay cho hàng phòng thủ mà Ryazan từng đảm nhận trước quân Tatar, "
        "Đại công tước Vasili III cho dựng một toà thành bằng đá trong các năm 1528–1531. Đây là "
        "kiểu kremlin 'chính quy' tương tự thành Moskva xây vài thập niên trước đó, nhưng gọn hơn "
        "nhiều: mặt bằng chỉ khoảng 2,4 ha, tường cao chừng 9 m và dày tới 3 m, xây bằng gạch phối "
        "hợp khối đá vôi trắng, gia cố bằng bảy tháp canh - trong đó bốn tháp góc mười hai cạnh và "
        "ba tháp giữa tường có cổng ra vào; các lỗ châu mai được bố trí để pháo có thể bắn ra "
        "ngoài lẫn quét dọc chân tường. Thành là một mắt xích của 'Tuyến phòng thủ Lớn' (Zasechnaya "
        "cherta) chạy dọc sông Oka. Vừa hoàn thành, năm 1531 và tiếp đó 1541, 1570, 1573, 1591 "
        "thành liên tục hứng chịu các đợt tấn công của người Tatar Crimea nhưng đều đứng vững; "
        "trong Thời loạn (Smuta), năm 1608 thành từng rơi vào tay quân Ba Lan - Litva của Lisowski "
        "rồi được Dmitry Pozharsky - khi ấy làm voevoda (trấn thủ) Zaraysk - giành lại. Sang thế kỉ "
        "18, khi biên giới lùi xa về phía nam, Zaraysk mất dần vai trò quân sự và trở thành một "
        "thị trấn thương mại yên bình. Trong vòng tường có hai ngôi thánh đường dựng muộn hơn nhiều "
        "so với thành: Nhà thờ chính toà Thánh Nikolai (Nikolsky sobor) xây năm 1681 với năm vòm "
        "hành theo lối Nga truyền thống, và Nhà thờ Thánh Gioan Tiền Hô (Ioanna Predtechi) một vòm "
        "kiểu tân cổ điển, được xây lại vào các năm 1901–1904. Từ năm 1918 cả khu thành trở thành "
        "bảo tàng; đến năm 1998 hình thành 'Bảo tàng Kremlin Zaraysk'. Ngay bên ngoài chân tường "
        "còn có một di chỉ thời đồ đá cũ (văn hoá Gravette) nổi tiếng, nơi các nhà khảo cổ tìm thấy "
        "tượng bò rừng và hai bức tượng Venus tạc từ ngà voi ma mút có tuổi khoảng hơn hai vạn năm "
        "- nay được trưng bày trong bảo tàng, biến Zaraysk thành điểm đến hiếm có kết hợp thành cổ "
        "và tiền sử."
    ),
    "highlights_vi": [
        "Kremlin duy nhất ở Tỉnh Moskva còn nguyên vòng tường thành (xây 1528–1531): tường cao ~9 m, dày tới 3 m, bảy tháp canh.",
        "Bên trong có Nhà thờ chính toà Thánh Nikolai (1681) năm vòm hành và Nhà thờ Thánh Gioan Tiền Hô kiểu tân cổ điển.",
        "Bảo tàng Zaraysk trưng bày tượng Venus và tượng bò rừng bằng ngà voi ma mút hơn 20.000 năm tuổi - di chỉ đồ đá cũ quý hiếm.",
    ],
    "practical": {
        "hours_vi": "Khuôn viên trong thành thường mở tự do ban ngày; bảo tàng và các nhà thờ thường mở 10:00–18:00, nghỉ đầu tuần (xem lịch cụ thể).",
        "ticket_vi": "Dạo trong thành thường miễn phí; tham quan các gian bảo tàng và leo tháp có bán vé riêng, nhiều mức ưu đãi.",
        "duration_vi": "Khoảng 1,5–2 giờ cho khu Kremlin và bảo tàng.",
        "best_time_vi": "Mùa hè và đầu thu trời khô ráo; tiện dạo thêm phố cổ Zaraysk với tháp nước lịch sử.",
        "tips_vi": "Từ Moskva có xe khách từ bến Kotelniki đi Zaraysk (khoảng 2,5–3 giờ); có thể kết hợp trong hành trình về Kolomna cùng nằm ở đông nam Tỉnh Moskva.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Зарайский кремль", "Zaraysk Kremlin", "Московская область", "Moscow Oblast", 54.75667, 38.86917),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN) — Zaraysk Kremlin", "url": "https://en.wikipedia.org/wiki/Zaraysk_Kremlin"},
        {"title": "Museum.ru — Историко-архитектурный, художественный и археологический музей «Зарайский кремль»", "url": "http://www.museum.ru/M453"},
        {"title": "Wikipedia (EN) — Venus figurines of Zaraysk", "url": "https://en.wikipedia.org/wiki/Venus_figurines_of_Zaraysk"},
    ],
    "tags": ["fortress", "kremlin", "church", "museum", "zaraysk", "history", "day-trip"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


VYSOTSKY_MONASTERY = {
    "id": "moscow-oblast-vysotsky-monastery-serpukhov",
    "slug": "vysotsky-monastery-serpukhov",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Tu viện Vysotsky ở Serpukhov (Vysotsky monastyr)",
    "name_ru": "Высоцкий монастырь",
    "name_en": "Vysotsky Monastery",
    "categories": ["church", "fortress"],
    "coordinates": {"lat": 54.90166, "lon": 37.41925},
    "address_vi": "Phố Kaluzhskaya, thành phố Serpukhov, Tỉnh Moskva; trên bờ trái cao của sông Nara gần nơi đổ vào sông Oka, cách Moskva khoảng 99 km về phía nam.",
    "rating": None,
    "presentation_short_vi": (
        "Tu viện Chính thống giáo cổ kính bên bờ cao sông Nara, do công tước Vladimir Andreyevich "
        "'Dũng cảm' của Serpukhov lập năm 1374 với sự chúc phúc của Thánh Sergiy Radonezhsky - một "
        "trong những tu viện lâu đời nhất nước Nga. Nơi đây nổi tiếng khắp cả nước nhờ bản icon "
        "'Chén Không Vơi' (Neupivaemaya Chasha) được sùng kính, thu hút đông đảo người hành hương "
        "cầu nguyện cai nghiện rượu và ma tuý."
    ),
    "presentation_long_vi": (
        "Tu viện Vysotsky (nghĩa là 'trên Cao', theo tên gò đất nơi toạ lạc) ra đời năm 1374 theo "
        "nguyện vọng của công tước Vladimir Andreyevich 'Dũng cảm' xứ Serpukhov - người anh em họ "
        "và bạn chiến đấu của Đại công tước Dmitry Donskoy. Theo truyền thuyết, dù tuổi đã cao và "
        "giữa mùa đông, Thánh Sergiy Radonezhsky vẫn đi bộ từ tu viện của mình tới Serpukhov để "
        "chọn đất và chúc phúc cho nơi này, cùng người học trò thân tín Afanasy - vị viện phụ đầu "
        "tiên của tu viện. Chỉ ít năm sau, ngôi thánh đường chính Zachatievsky (kính Sự Thụ thai "
        "của Đức Trinh nữ Maria) được dựng để tạ ơn chiến thắng vang dội trên cánh đồng Kulikovo "
        "năm 1380; trong iconostas (bức tường ảnh thánh) của nhà thờ tương truyền có bảy bức icon "
        "do viện phụ Afanasy gửi về từ Constantinople (Tsargrad). Nằm ở khúc quanh phía nam của "
        "Đại công quốc Moskva, tu viện đồng thời là một pháo đài canh giữ tuyến sông Oka; phần lớn "
        "công trình từng bị tàn phá trong cuộc đột kích của quân Tatar Crimea năm 1571 rồi được "
        "xây lại kiên cố bằng đá. Trải các thế kỉ, quần thể dần hình thành diện mạo như ngày nay: "
        "nhà thờ Zachatievsky, nhà thờ kính Thánh Sergiy Radonezhsky, tháp chuông cao, dãy tường "
        "thành và tháp canh cùng khu mộ các công tước Serpukhov, tất cả nằm trên gò cao nhìn bao "
        "quát dòng Nara và sông Oka. Danh tiếng đặc biệt của Vysotsky gắn với icon 'Chén Không Vơi' "
        "- một ảnh thánh của vùng Serpukhov được tôn kính từ cuối thế kỉ 19, gắn với niềm tin chữa "
        "lành chứng nghiện rượu; sau khi bản gốc thất lạc thời Xô-viết, tu viện Vysotsky gìn giữ "
        "một bản icon 'Chén Không Vơi' được sùng kính, hằng năm đón hàng vạn tín đồ tới cầu nguyện "
        "cho người thân thoát cảnh nghiện ngập. Bị đóng cửa dưới thời Liên Xô, tu viện được trao "
        "trả cho Giáo hội và phục hồi đời sống tu trì từ năm 1991, nay là tu viện nam giới "
        "stavropegic; năm 2024 cộng đồng kỷ niệm tròn 650 năm ngày thành lập."
    ),
    "highlights_vi": [
        "Một trong những tu viện lâu đời nhất nước Nga, lập năm 1374 với sự chúc phúc của Thánh Sergiy Radonezhsky (kỷ niệm 650 năm vào 2024).",
        "Nhà thờ chính Zachatievsky dựng để tạ ơn chiến thắng Kulikovo (1380); quần thể pháo đài - tu viện trên gò cao nhìn ra sông Nara và Oka.",
        "Bản icon 'Chén Không Vơi' được sùng kính - điểm hành hương nổi tiếng cho người cầu nguyện cai nghiện rượu và ma tuý.",
    ],
    "practical": {
        "hours_vi": "Tu viện thường mở đón khách hành hương ban ngày (khoảng 8:00–19:00); giờ lễ và thời gian tham quan tháp chuông xem thông báo tại chỗ.",
        "ticket_vi": "Vào cửa tự do; hoan nghênh quyên góp. Một số hoạt động hướng dẫn hoặc lên tháp chuông có thể thu phí nhỏ.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm; đông người hành hương vào các dịp lễ lớn và ngày kính icon 'Chén Không Vơi' (18/5).",
        "tips_vi": "Nên ăn mặc kín đáo, nữ mang khăn trùm đầu. Từ Moskva đi tàu ngoại ô từ ga Kursky tới Serpukhov rồi bắt xe buýt/taxi; có thể kết hợp thăm Tu viện Vladychny gần đó.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Высоцкий монастырь", "Vysotsky Monastery", "Московская область", "Moscow Oblast", 54.90166, 37.41925),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN) — Vysotsky Monastery", "url": "https://en.wikipedia.org/wiki/Vysotsky_Monastery"},
        {"title": "Rusmania — Vysotsky Monastery (Serpukhov)", "url": "https://rusmania.com/central/moscow-region/serpukhov/sights/around-the-centre/vysotsky-monastery"},
        {"title": "OrthoChristian.com — 650th anniversary of Vysotsky Monastery", "url": "https://orthochristian.com/163549.html"},
    ],
    "tags": ["church", "monastery", "pilgrimage", "serpukhov", "history", "inexhaustible-chalice"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


ALEXANDER_SVIRSKY = {
    "id": "leningrad-oblast-alexander-svirsky-monastery",
    "slug": "alexander-svirsky-monastery",
    "region": "leningrad-oblast",
    "region_name_vi": "Tỉnh Leningrad",
    "federal_district": "Vùng Tây Bắc",
    "name_vi": "Tu viện Alexander-Svirsky (Aleksandro-Svirsky monastyr)",
    "name_ru": "Александро-Свирский монастырь",
    "name_en": "Alexander-Svirsky Monastery",
    "categories": ["church", "monument"],
    "coordinates": {"lat": 60.77928, "lon": 33.30928},
    "address_vi": "Làng Staraya Sloboda, huyện Lodeynopolsky, Tỉnh Leningrad; bên hồ Roshchinskoye giữa rừng, cách Saint Petersburg khoảng 260 km về phía đông và cách thị trấn Lodeynoye Pole khoảng 21 km.",
    "rating": None,
    "presentation_short_vi": (
        "Tu viện Chính thống giáo cổ kính nằm giữa rừng sâu vùng đông bắc Tỉnh Leningrad, do Thánh "
        "Aleksandr Svirsky - một tu sĩ đến từ Valaam - lập năm 1487 bên hồ Roshchinskoye. Gồm hai "
        "cụm 'Chúa Ba Ngôi' (Troitsky) và 'Hiển Dung' (Preobrazhensky), tu viện nổi tiếng với tháp "
        "chuông ba chóp lều hiếm hoi thế kỉ 17 và di hài được xem là bất hoại của vị thánh sáng "
        "lập - một trong những điểm hành hương quan trọng nhất vùng Tây Bắc nước Nga."
    ),
    "presentation_long_vi": (
        "Tu viện được lập năm 1487 khi tu sĩ Aleksandr - vốn tu ở Tu viện Valaam trên hồ Ladoga - "
        "lui về ẩn tu giữa vùng rừng hồ hoang vắng, khoảng 20 km về phía đông hồ Ladoga và cách "
        "sông Svir chừng 6 km, giữa hai hồ Roshchinskoye và Svyatoye (hồ Thánh). Theo truyền "
        "thống Chính thống giáo, tại đây ngài được ơn thị kiến Chúa Ba Ngôi hiện ra dưới hình ba "
        "thiên thần - một sự kiện hiếm thấy khiến ngài được kính nhớ đặc biệt; vâng lời thị kiến, "
        "ngài dựng hai nguyện đường gỗ sồi kính Chúa Ba Ngôi và sự Hiển Dung, từ đó hình thành hai "
        "cụm tu viện song sinh Troitsky (Chúa Ba Ngôi) và Preobrazhensky (Hiển Dung). Thánh "
        "Aleksandr qua đời năm 1533, được Giáo hội tuyên thánh sớm khác thường vào năm 1547 và trở "
        "thành một vị thánh được sùng kính khắp nước Nga - thậm chí một nguyện đường của Nhà thờ "
        "Thánh Vasily Phúc trên Quảng trường Đỏ cũng được dâng kính ngài. Thời hoàng kim của tu "
        "viện là thế kỉ 17: Nhà thờ Hiển Dung năm vòm hoàn thành năm 1644 (Sa hoàng Mikhail "
        "Feodorovich ban tặng một hòm vàng để lưu giữ di hài thánh nhân), tháp chuông ba tầng đội "
        "ba chóp lều dựng năm 1649 - một trong số rất ít tháp chuông kiểu này còn lại ở Nga - và "
        "Nhà thờ Chúa Ba Ngôi rộng rãi hoàn tất năm 1695. Trong Thời loạn, quân Thuỵ Điển nhiều "
        "lần cướp phá và thiêu rụi, nhưng tu viện vẫn hồi sinh và thịnh vượng nhờ hội chợ Svir "
        "sầm uất họp ngay dưới chân thành. Ruộng đất mênh mông của tu viện bị sung công trong cuộc "
        "cải cách nhà thờ của Ekaterina II năm 1764. Sau Cách mạng 1917, các tu sĩ bị bắt và xử "
        "bắn, di hài thánh nhân bị đưa đi trưng bày ở Leningrad, còn quần thể cổ kính bị biến thành "
        "một phần trại lao động khổ sai Svirlag rồi tiếp tục hư hại trong Thế chiến II. Việc trùng "
        "tu chỉ bắt đầu từ thập niên 1970; tu viện được trao trả cho Giáo hội năm 1997 và di hài "
        "được xem là bất hoại của Thánh Aleksandr Svirsky đưa trở về năm 1998, từ đó nơi đây trở "
        "lại là một trung tâm hành hương lớn, đón dòng người từ khắp nước Nga về kính viếng."
    ),
    "highlights_vi": [
        "Do Thánh Aleksandr Svirsky lập năm 1487; theo truyền thống, ngài được ơn thị kiến Chúa Ba Ngôi - điều hiếm thấy trong lịch sử các thánh.",
        "Quần thể kiến trúc thế kỉ 17 với Nhà thờ Hiển Dung năm vòm (1644) và tháp chuông ba chóp lều (1649) độc đáo bậc nhất nước Nga.",
        "Di hài được xem là bất hoại của Thánh Aleksandr được đưa trở về năm 1998 - điểm hành hương lớn của vùng Tây Bắc.",
    ],
    "practical": {
        "hours_vi": "Tu viện mở đón khách hành hương ban ngày (khoảng 8:00–20:00 tuỳ mùa); giờ lễ và giờ mở nhà thờ đặt di hài xem thông báo tại chỗ.",
        "ticket_vi": "Vào cửa tự do; hoan nghênh quyên góp.",
        "duration_vi": "Khoảng 1,5–2 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu; đông người hành hương vào các ngày kính Thánh Aleksandr Svirsky (30/8 và 17/4 theo lịch nhà thờ).",
        "tips_vi": "Nên ăn mặc kín đáo, nữ mang khăn trùm đầu. Đường khá xa - từ Saint Petersburg có thể đi tàu tới ga Lodeynoye Pole rồi bắt xe, hoặc theo tour hành hương; tiện kết hợp hành trình dọc sông Svir.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Александро-Свирский монастырь", "Alexander-Svirsky Monastery", "Ленинградская область", "Leningrad Oblast", 60.77928, 33.30928),
    "official_site": "http://svirskoe.org",
    "sources": [
        {"title": "Wikipedia (EN) — Alexander-Svirsky Monastery", "url": "https://en.wikipedia.org/wiki/Alexander-Svirsky_Monastery"},
        {"title": "Sobory.ru — Старая Слобода, Александро-Свирский монастырь", "url": "https://sobory.ru/article/?object=00119"},
        {"title": "Tu viện Alexander-Svirsky — Trang chính thức (svirskoe.org)", "url": "http://svirskoe.org"},
    ],
    "tags": ["church", "monastery", "pilgrimage", "alexander-svirsky", "relics", "leningrad-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow-oblast.json": [ZARAYSK_KREMLIN, VYSOTSKY_MONASTERY],
    "leningrad-oblast.json": [ALEXANDER_SVIRSKY],
}


def main():
    total_added = 0
    for fname, recs in PLAN.items():
        path = os.path.join(REGIONS, fname)
        arr = json.load(open(path, encoding="utf-8"))
        existing_slugs = {p.get("slug") for p in arr}
        existing_ids = {p.get("id") for p in arr}
        to_add = []
        for r in recs:
            if r["slug"] in existing_slugs or r["id"] in existing_ids:
                print(f"  = BỎ QUA (đã có): {fname} :: {r['slug']}")
                continue
            to_add.append(r)
        if not to_add:
            continue
        bak = path + f".bak_add_{TS}"
        with open(bak, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        arr.extend(to_add)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        total_added += len(to_add)
        print(f"  + {fname}: thêm {len(to_add)} địa điểm -> tổng {len(arr)} (backup: {os.path.basename(bak)})")
        for r in to_add:
            print(f"        - {r['name_vi']}  [{','.join(r['categories'])}]  ({r['coordinates']['lat']},{r['coordinates']['lon']})")

    print(f"\nTổng đã thêm lần này: {total_added} địa điểm.")


if __name__ == "__main__":
    main()
