# -*- coding: utf-8 -*-
"""_add_three_places_ac.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26, tối).

Ưu tiên VÙNG: thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.

Thêm:
  1) Tỉnh Moskva (moscow-oblast)      : Tu viện Iosifo-Volotsky (Volokolamsk) — fortress/church
  2) Tỉnh Moskva (moscow-oblast)      : Bảo tàng Lịch sử - Nghệ thuật Serpukhov — museum
  3) Tỉnh Leningrad (leningrad-oblast): Thư viện Alvar Aalto ở Vyborg — monument (kiến trúc)

LƯU Ý (đối chiếu để tránh trùng, đã kiểm tra data/regions/*.json):
  - Volokolamsk trước nay CHƯA có bản ghi nào -> bổ sung Tu viện Iosifo-Volotsky (danh thắng lớn nhất huyện).
  - Serpukhov mới chỉ có Tu viện Vysotsky -> thêm Bảo tàng Lịch sử - Nghệ thuật ('Tretyakov thu nhỏ').
  - Vyborg đã có Lâu đài & công viên Monrepos; Thư viện Alvar Aalto là công trình kiến trúc hiện đại
    tầm cỡ thế giới, khác hẳn về loại hình -> bổ sung cho cân bằng vùng Leningrad + yếu tố 'hiện đại'.
  - Cung điện Gatchina/Priory Palace KHÔNG thêm (đã có trong saint-petersburg.json).

Nội dung tiếng Việt nguyên gốc (paraphrase, không sao chép nguyên văn), có ghi nguồn.
Toạ độ THẬT, đối chiếu web 2026-07 (Wikipedia EN/RU + nguồn du lịch/di sản):
  - Iosifo-Volotsky: 56.17238, 36.09980 (Wikipedia RU: 56°10′19″N 36°05′51″E, làng Teryayevo)
  - Serpukhov museum: 54.90333, 37.42611 (54°54′12″N 37°25′34″E, ул. Чехова 87)
  - Vyborg Aalto library: 60.70889, 28.74750 (60°42′32″N 28°44′51″E, пр. Суворова 4)
Kiểm tra thứ tự lat/lon: lat 54–61 (∈41–70), lon 28–37 (∈19–180), KHÔNG đảo; đều nằm trong phạm vi thành phố.
Link bản đồ dạng TRỎ-ĐỊA-ĐIỂM (khớp convention tools/retrofit_map_links.py để idempotent).

Chạy:  python3 tools/_add_three_places_ac.py
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
JOSEPH_VOLOKOLAMSK = {
    "id": "moscow-oblast-joseph-volokolamsk-monastery",
    "slug": "joseph-volokolamsk-monastery",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Tu viện Iosifo-Volotsky (Iosifo-Volokolamsky)",
    "name_ru": "Иосифо-Волоцкий монастырь",
    "name_en": "Joseph-Volokolamsk Monastery",
    "categories": ["fortress", "church"],
    "coordinates": {"lat": 56.17238, "lon": 36.09980},
    "address_vi": "Làng Teryayevo, khu đô thị Volokolamsk, Tỉnh Moskva; cách thành phố Volokolamsk khoảng 16 km về phía đông bắc, bên hồ Bratsky.",
    "rating": None,
    "presentation_short_vi": (
        "Tu viện Iosifo-Volotsky là một trong những tu viện - pháo đài uy nghi và nên thơ bậc nhất "
        "vùng ngoại ô Moskva, do Thánh Iosif Volotsky sáng lập năm 1479 và dâng kính lễ Đức Mẹ Yên "
        "Nghỉ (Uspenie). Từ thế kỉ 15-16, đây đã là một trong những tu viện giàu có và có ảnh hưởng "
        "nhất nước Nga, sánh ngang Tu viện Ba Ngôi ở Sergiev Posad. Quần thể gạch đỏ với vòng tường "
        "thành, các tòa tháp trang trí cầu kì và nhà thờ chính Uspensky lộng lẫy soi bóng xuống mặt "
        "hồ Bratsky - tạo nên khung cảnh tu viện đẹp vào loại nhất Trung Nga."
    ),
    "presentation_long_vi": (
        "Tu viện do Thánh Iosif Volotsky (còn gọi Iosif Volokolamsky) lập năm 1479 trên đất do công "
        "tước Boris Vasilyevich Volotsky ban tặng. Ngay từ đầu, Iosif đã xây dựng nơi đây thành trung "
        "tâm của khuynh hướng «sở hữu» (iosiflyane) trong Giáo hội Nga - chủ trương tu viện được quyền "
        "nắm giữ ruộng đất để làm việc thiện và giáo dục, đối lập với phái «không sở hữu» của Thánh "
        "Nil Sorsky; đây là một trong những cuộc tranh luận lớn nhất lịch sử Chính thống giáo Nga. "
        "Nhà thờ đá đầu tiên (1486) từng được danh họa Dionisy vẽ bích họa; bên cạnh là tháp chuông "
        "tám cạnh (1490) được xem như nguyên mẫu của tháp chuông Ivan Đại đế trong Kremlin Moskva. "
        "Phần lớn công trình còn lại hôm nay thuộc thế kỉ 16-17: nhà thờ chính Uspensky (Đức Mẹ Yên "
        "Nghỉ, 1688-1696) theo phong cách Baroque Moskva, trang trí bằng những mảng gạch men màu "
        "(izraztsy) do nghệ nhân Stepan Polubes thực hiện - cùng người từng làm ở Tu viện Tân "
        "Jerusalem; nhà ăn (trapeznaya) gắn nhà thờ Hiển Linh (1504); nhà thờ trên cổng thánh Phêrô "
        "và Phaolô (1679); cùng vòng tường thành và các tháp canh mang dáng dấp pháo đài. Trong lịch "
        "sử, tu viện vừa là nơi các Sa hoàng đến hành hương, vừa là chốn giam giữ những nhân vật bị "
        "coi là «kẻ thù của nhà nước» hay dị giáo - trong đó có học giả Maxim Grek (Maximus người Hy "
        "Lạp) và cả cựu Sa hoàng Vasily IV Shuisky, người bị phế truất năm 1610 và bị giam một thời "
        "gian trong tháp Germanova. Nơi đây cũng an nghỉ hài cốt Thánh Iosif và nhiều nhân vật lịch "
        "sử, trong đó có Malyuta Skuratov - thủ lĩnh khét tiếng của lực lượng oprichnik thời Ivan Hung "
        "đế - và bà N. I. Goncharova, mẹ vợ của đại thi hào Pushkin. Trong Thời kì Loạn lạc tu viện "
        "từng bị vây hãm; ngọn tháp chuông cổ (tầng dưới là nhà thờ Smolensk Odigitria, 1495) - từ đó "
        "ngày quang có thể nhìn thấy Moskva - đã bị Hồng quân cho nổ sập khi rút lui năm 1941 và đến "
        "nay vẫn chưa được phục dựng. Bị đóng cửa năm 1922, tu viện được trao trả Giáo hội Chính "
        "thống Nga năm 1989, mang quy chế stauropegic (trực thuộc Thượng phụ) từ 1999; hài cốt Thánh "
        "Iosif được tìm thấy và đặt trong nhà thờ Uspensky năm 2003. Ngày nay Iosifo-Volotsky là điểm "
        "hành hương và tham quan trong ngày nổi tiếng, quyến rũ nhờ kiến trúc tu viện - pháo đài cùng "
        "tấm gương nước phản chiếu tường thành."
    ),
    "highlights_vi": [
        "Nhà thờ chính Uspensky (1688-1696) phong cách Baroque Moskva, trang trí gạch men màu (izraztsy) của nghệ nhân Stepan Polubes.",
        "Vòng tường thành cùng các tòa tháp trang trí cầu kì mang dáng pháo đài, soi bóng xuống hồ Bratsky - hình ảnh biểu tượng của tu viện.",
        "Nơi lưu giữ hài cốt và xiềng khổ hạnh (verigi) của Thánh Iosif Volotsky, gắn với cuộc tranh luận «sở hữu» - «không sở hữu» trong Giáo hội Nga.",
    ],
    "practical": {
        "hours_vi": "Tu viện đang hoạt động, mở cửa cho khách hành hương và tham quan hằng ngày, thường khoảng 7:00-20:00; giờ lễ theo lịch phụng vụ. Trang phục kín đáo; nữ nên mang khăn trùm đầu và váy dài.",
        "ticket_vi": "Vào tham quan khuôn viên thường miễn phí (có thể quyên góp tùy tâm); một số khu vực/triển lãm nhỏ có thể thu phí hoặc tổ chức theo đoàn.",
        "duration_vi": "Khoảng 1,5-2 giờ để đi hết khuôn viên, nhà thờ chính và dạo quanh hồ.",
        "best_time_vi": "Cuối xuân đến đầu thu để chụp cảnh tường thành phản chiếu trên mặt hồ; các ngày lễ kính Thánh Iosif (dịp 22/9 và 3/3) thường đông khách hành hương.",
        "tips_vi": "Từ Moskva có thể đi tàu ngoại ô từ ga Rizhsky đến Volokolamsk rồi bắt xe buýt/taxi tới làng Teryayevo (khoảng 16 km). Có thể kết hợp thăm cụm di tích Volokolamsk Kremlin trong cùng chuyến.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Иосифо-Волоцкий монастырь", "Joseph-Volokolamsk Monastery", "Московская область", "Moscow Oblast", 56.17238, 36.09980),
    "official_site": "https://iosif-vm.ru/",
    "sources": [
        {"title": "Wikipedia (RU) — Иосифо-Волоцкий монастырь", "url": "https://ru.wikipedia.org/wiki/Иосифо-Волоцкий_монастырь"},
        {"title": "Trang chính thức tu viện — iosif-vm.ru", "url": "https://iosif-vm.ru/"},
        {"title": "Sobory.ru — Успенский Иосифо-Волоцкий монастырь", "url": "https://sobory.ru/article/?object=00394"},
    ],
    "tags": ["monastery", "fortress", "church", "pilgrimage", "joseph-volotsky", "volokolamsk", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


SERPUKHOV_MUSEUM = {
    "id": "moscow-oblast-serpukhov-history-art-museum",
    "slug": "serpukhov-history-art-museum",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Bảo tàng Lịch sử - Nghệ thuật Serpukhov",
    "name_ru": "Серпуховский историко-художественный музей",
    "name_en": "Serpukhov Historical and Art Museum",
    "categories": ["museum"],
    "coordinates": {"lat": 54.90333, "lon": 37.42611},
    "address_vi": "Phố Chekhova số 87, thành phố Serpukhov, Tỉnh Moskva; ở khu trung tâm lịch sử, gần Tu viện Vysotsky.",
    "rating": None,
    "presentation_short_vi": (
        "Được giới phê bình gọi là «phòng tranh Tretyakov thu nhỏ», Bảo tàng Lịch sử - Nghệ thuật "
        "Serpukhov sở hữu một trong những bộ sưu tập mĩ thuật giàu có nhất Tỉnh Moskva. Bảo tàng đặt "
        "trong tòa dinh thự cổ của nữ thương gia - nhà bảo trợ Anna Maraeva, trưng bày tranh của "
        "nhiều danh họa Nga thế kỉ 18-19 cùng một mảng hội họa Tây Âu quý hiếm."
    ),
    "presentation_long_vi": (
        "Nền tảng của bảo tàng là bộ sưu tập tư nhân của Anna Vasilyevna Maraeva - nữ chủ nhân một "
        "xưởng dệt lớn ở Serpukhov, theo phái Tín đồ Cũ (Old Believers) và là nhà bảo trợ nghệ thuật. "
        "Cuối thế kỉ 19, bà mua lại bộ sưu tập của nhà quý tộc Yuri Merlin gồm tranh Nga và Tây Âu, "
        "rồi cho cải tạo tòa dinh thự gia đình (theo nhiều nguồn là do kiến trúc sư Roman Klein - tác "
        "giả Bảo tàng Mĩ thuật Pushkin ở Moskva - thiết kế) để làm nơi lưu giữ. Sau Cách mạng 1917 bộ "
        "sưu tập được quốc hữu hóa và tới các năm 1918-1920 chính thức mở cửa thành bảo tàng công "
        "cộng ngay trong dinh thự Maraev. Ngày nay bộ sưu tập có hơn 40.000 hiện vật: hội họa, điêu "
        "khắc, đồ nội thất, đồ trang trí - ứng dụng và tranh in. Phần nghệ thuật Nga quy tụ tác phẩm "
        "của nhiều tên tuổi lớn như Ivan Shishkin, Isaac Levitan, Ivan Aivazovsky, Vasily Polenov, "
        "Konstantin Makovsky…; bên cạnh đó là mảng hội họa Tây Âu (Ý, Hà Lan, Flanders) thế kỉ 16-18 "
        "- điều hiếm thấy ở một bảo tàng cấp tỉnh, khiến Serpukhov được ví như «phòng tranh Tretyakov "
        "nhỏ». Bản thân tòa dinh thự với nội thất trang trí công phu cũng là một hiện vật, còn ngoài "
        "sân bảo tàng trưng bày một số bia mộ và hiện vật đá cổ. Nằm ngay trong khu trung tâm lịch sử "
        "và gần Tu viện Vysotsky, bảo tàng là điểm dừng chân lí tưởng cho chuyến khám phá thành phố "
        "cổ Serpukhov ở phía nam Moskva."
    ),
    "highlights_vi": [
        "Bộ sưu tập mĩ thuật lớn nhất Tỉnh Moskva với hơn 40.000 hiện vật, được ví như «phòng tranh Tretyakov thu nhỏ».",
        "Tranh của các danh họa Nga (Shishkin, Levitan, Aivazovsky, Polenov, Makovsky…) cùng mảng hội họa Tây Âu thế kỉ 16-18 hiếm có ở bảo tàng cấp tỉnh.",
        "Tòa dinh thự lịch sử của nữ thương gia Anna Maraeva với nội thất trang trí công phu - bản thân đã là một tác phẩm kiến trúc.",
    ],
    "practical": {
        "hours_vi": "Thường mở Thứ Ba–Chủ nhật khoảng 10:00-18:00 (một số tối trong tuần có thể muộn hơn); nghỉ Thứ Hai và ngày vệ sinh cuối tháng. Nên kiểm tra lịch trên trang chính thức trước khi đến.",
        "ticket_vi": "Có bán vé vào cửa và vé gộp cho các triển lãm; nhiều mức ưu đãi cho học sinh, sinh viên, người cao tuổi. Có thể thuê hướng dẫn hoặc máy thuyết minh (audioguide).",
        "duration_vi": "Khoảng 1,5-2 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà); thuận tiện nhất vào cuối tuần để ghép thêm Tu viện Vysotsky và trung tâm cổ Serpukhov.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô hoặc tàu tốc hành từ ga Kursky đến Serpukhov (khoảng 1,5-2 giờ), rồi bắt xe buýt/taxi tới phố Chekhova. Nên đi cùng Tu viện Vysotsky gần đó để trọn một ngày ở Serpukhov.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Серпуховский историко-художественный музей", "Serpukhov Historical and Art Museum", "Московская область", "Moscow Oblast", 54.90333, 37.42611),
    "official_site": None,
    "sources": [
        {"title": "Культура.РФ — Серпуховский историко-художественный музей", "url": "https://www.culture.ru/institutes/11944/serpukhovskii-istoriko-khudozhestvennyi-muzei"},
        {"title": "Rusmania — Serpukhov Historical and Art Museum", "url": "https://rusmania.com/central/moscow-region/serpukhov/sights/around-the-centre/serpukhov-historical-and-art-museum"},
        {"title": "Museum.ru — The Serpukhov History and Art Museum", "url": "http://www.museum.ru/museum/mscreg/e4_hist.htm"},
    ],
    "tags": ["museum", "art-gallery", "maraeva", "serpukhov", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


VYBORG_AALTO_LIBRARY = {
    "id": "leningrad-oblast-vyborg-alvar-aalto-library",
    "slug": "vyborg-alvar-aalto-library",
    "region": "leningrad-oblast",
    "region_name_vi": "Tỉnh Leningrad",
    "federal_district": "Vùng Tây Bắc",
    "name_vi": "Thư viện Alvar Aalto ở Vyborg",
    "name_ru": "Библиотека Алвара Аалто",
    "name_en": "Vyborg Library (Alvar Aalto Library)",
    "categories": ["monument"],
    "coordinates": {"lat": 60.70889, "lon": 28.74750},
    "address_vi": "Đại lộ Suvorova số 4, thành phố Vyborg, Tỉnh Leningrad; nằm trong công viên trung tâm thành phố.",
    "rating": None,
    "presentation_short_vi": (
        "Thư viện thành phố Vyborg do kiến trúc sư Phần Lan Alvar Aalto thiết kế (1927-1935) là một "
        "trong những công trình biểu tượng của kiến trúc hiện đại (chủ nghĩa công năng) thế kỉ 20 và "
        "là điểm «hành hương» của giới kiến trúc khắp thế giới. Công trình nổi tiếng với trần gỗ uốn "
        "lượn như sóng trong khán phòng và hệ giếng trời hình trụ đưa ánh sáng tự nhiên dịu đều xuống "
        "các phòng đọc."
    ),
    "presentation_long_vi": (
        "Alvar Aalto giành quyền thiết kế thư viện sau khi thắng cuộc thi kiến trúc năm 1927; công "
        "trình hoàn thành năm 1935, khi Vyborg (tên Phần Lan là Viipuri) còn thuộc Phần Lan. Từ "
        "phương án ban đầu mang hơi hướng cổ điển Bắc Âu, Aalto đã chuyển hẳn sang ngôn ngữ công năng "
        "(functionalism) thuần khiết, biến thư viện thành một trong những tuyên ngôn sớm của «chủ "
        "nghĩa hiện đại vùng miền». Nhiều giải pháp lần đầu thử nghiệm ở đây về sau trở thành «chữ "
        "kí» của Aalto: giếng đọc âm xuống nền (sunken reading well), hệ giếng trời hình trụ trên mái "
        "(khoảng 57 chiếc) lấy ánh sáng tự nhiên không tạo bóng đổ, và đặc biệt là trần gỗ uốn lượn "
        "của khán phòng - hình dạng mà Aalto lí giải dựa trên nghiên cứu về âm học. Aalto khác thế hệ "
        "kiến trúc sư hiện đại đầu tiên ở tình yêu với vật liệu tự nhiên: gỗ được đưa vào giữa bối "
        "cảnh bê tông, kính và thép. Sau Thế chiến II, Vyborg thuộc về Liên Xô; tòa nhà bị hư hại "
        "nặng, bỏ hoang gần một thập kỉ khiến trần khán phòng uốn sóng bị phá hủy, rồi được đổi tên "
        "thành Thư viện thành phố mang tên Nadezhda Krupskaya. Từ năm 1994 đến 2013, một dự án trùng "
        "tu Nga - Phần Lan kéo dài gần hai thập kỉ (do Viện hàn lâm Alvar Aalto dẫn dắt, với các kiến "
        "trúc sư Maija Kairamo và Tapani Mustonen) đã phục dựng công trình gần như nguyên trạng, tiêu "
        "tốn khoảng 9 triệu euro. Thành quả trùng tu được trao Giải Modernism của Quỹ Di tích Thế "
        "giới/Knoll (2014) và Giải Europa Nostra của châu Âu (2015). Ngày nay công trình vẫn là thư "
        "viện công cộng đang hoạt động (tên chính thức: Thư viện Trung tâm Thành phố mang tên A. "
        "Aalto), đồng thời mở các tour tham quan kiến trúc - một điểm đến độc đáo giữa Vyborg vốn nổi "
        "tiếng với lâu đài trung cổ."
    ),
    "highlights_vi": [
        "Trần gỗ uốn lượn như sóng trong khán phòng - thiết kế dựa trên nghiên cứu âm học, một biểu tượng của kiến trúc hiện đại.",
        "Hệ giếng trời hình trụ trên mái (khoảng 57 chiếc) và giếng đọc âm xuống nền - giải pháp lấy sáng tự nhiên đặc trưng của Aalto.",
        "Công trình chủ nghĩa công năng kinh điển (1935) của Alvar Aalto; dự án trùng tu đoạt giải World Monuments Fund/Knoll (2014) và Europa Nostra (2015).",
    ],
    "practical": {
        "hours_vi": "Là thư viện đang hoạt động, thường mở gần như cả tuần (nghỉ một ngày trong tuần và ngày lễ); khu vực tham quan kiến trúc mở theo giờ hành chính. Nên đặt trước tour có hướng dẫn để vào khán phòng và các khu nội bộ.",
        "ticket_vi": "Vào khu vực thư viện thường miễn phí; tour tham quan kiến trúc (nhất là khán phòng) thường có thu phí.",
        "duration_vi": "Khoảng 45 phút - 1 giờ cho tour kiến trúc.",
        "best_time_vi": "Quanh năm (công trình trong nhà). Có thể ghép trong ngày cùng Lâu đài Vyborg và công viên Monrepos.",
        "tips_vi": "Vyborg cách Saint Petersburg khoảng 130 km, đi tàu tốc hành «Lastochka» từ ga Finlyandsky khoảng 1-1,5 giờ. Thư viện nằm ngay công viên trung tâm, đi bộ gần từ ga và từ Lâu đài Vyborg. Kiểm tra lịch tour trên trang chính thức aalto.vbgcity.ru.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Библиотека Алвара Аалто", "Vyborg Library Alvar Aalto", "Ленинградская область", "Leningrad Oblast", 60.70889, 28.74750),
    "official_site": "http://www.aalto.vbgcity.ru/",
    "sources": [
        {"title": "Wikipedia (EN) — Vyborg Library", "url": "https://en.wikipedia.org/wiki/Vyborg_Library"},
        {"title": "Visit Alvar Aalto — Vyborg Library", "url": "https://visit.alvaraalto.fi/en/destinations/vyborg-library/"},
        {"title": "Trang chính thức thư viện — aalto.vbgcity.ru", "url": "http://www.aalto.vbgcity.ru/"},
    ],
    "tags": ["architecture", "modernism", "functionalism", "alvar-aalto", "library", "vyborg", "leningrad-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow-oblast.json": [JOSEPH_VOLOKOLAMSK, SERPUKHOV_MUSEUM],
    "leningrad-oblast.json": [VYBORG_AALTO_LIBRARY],
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
