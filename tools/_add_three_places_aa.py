# -*- coding: utf-8 -*-
"""_add_three_places_aa.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26, tối).

Ưu tiên VÙNG: các thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.

Thêm:
  1) Tỉnh Moskva (moscow-oblast)      : Nhà thờ Đức Mẹ Lên Trời trên Gorodok, Zvenigorod (church/monument)
  2) Tỉnh Moskva (moscow-oblast)      : Bảo tàng - Điền trang Gorki Leninskiye (museum/palace/park_garden)
  3) Tỉnh Leningrad (leningrad-oblast): Tu viện Konevets trên hồ Ladoga (church/monument)

LƯU Ý CHỐNG TRÙNG (đã kiểm tra 2026-07-26):
  - Cung điện Gatchina & Priory KHÔNG thêm: đã có sẵn trong saint-petersburg.json.
  - Toàn bộ vành đai cung điện hoàng gia quanh SPb (Peterhof, Pavlovsk, Tsarskoye Selo/Catherine,
    Alexander, Oranienbaum, Konstantinovsky, Gatchina, Priory) đã có đủ trong saint-petersburg.json.
  - 3 địa điểm dưới đây đối chiếu slug/id ở moscow-oblast.json & leningrad-oblast.json: còn THIẾU.

Nội dung tiếng Việt nguyên gốc (không dịch nguyên văn), có ghi nguồn. Toạ độ THẬT, đã đối chiếu
nhiều nguồn (Wikipedia RU/EN + nguồn Nga) tháng 7/2026:
  - Uspensky sobor na Gorodke (Zvenigorod): 55.733067, 36.840248  (Wikipedia RU + mosculture.ru)
  - Gorki Leninskiye (музей-заповедник)   : 55.50462, 37.76505    (Wikipedia + places.moscow, mgorki.ru)
  - Коневский монастырь (o. Коневец)       : 60.84778, 30.58556    (Wikipedia EN «geo» + konevets.ru)

Link bản đồ theo dạng TRỎ-ĐỊA-ĐIỂM (khớp convention tools/retrofit_map_links.py:
Yandex tìm theo tên Nga + vùng, canh giữa bằng ll=lon,lat).

Chạy:  python3 tools/_add_three_places_aa.py
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
DORMITION_GORODOK = {
    "id": "moscow-oblast-dormition-cathedral-gorodok-zvenigorod",
    "slug": "dormition-cathedral-gorodok-zvenigorod",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Nhà thờ chính toà Đức Mẹ Lên Trời trên Gorodok, Zvenigorod (Uspensky sobor na Gorodke)",
    "name_ru": "Успенский собор на Городке",
    "name_en": "Assumption Cathedral on Gorodok (Zvenigorod)",
    "categories": ["church", "monument"],
    "coordinates": {"lat": 55.733067, "lon": 36.840248},
    "address_vi": "Đồi Gorodok (phố Gorodok), thành phố Zvenigorod, Tỉnh Moskva; cách trung tâm Moskva khoảng 50 km về phía tây.",
    "rating": None,
    "presentation_short_vi": (
        "Toạ lạc trên đồi Gorodok - lõi thành cổ của Zvenigorod nay vẫn còn những lũy đất xưa - đây "
        "là một trong số rất ít nhà thờ đá trắng thời sơ kỳ Moskva còn tồn tại gần như nguyên vẹn. "
        "Ngôi thánh đường một vòm, bốn cột được Công tước Yury Dmitrievich (con trai Dmitry Donskoy) "
        "cho dựng vào khoảng năm 1399. Bên trong còn lưu giữ những mảng bích hoạ đầu thế kỷ 15 mà "
        "nhiều nhà nghiên cứu gắn với tên tuổi Andrei Rublev và Daniil Chyorny."
    ),
    "presentation_long_vi": (
        "Đồi Gorodok chính là hạt nhân đầu tiên của Zvenigorod: một toà thành nhỏ trên gò cao bên "
        "sông Moskva, quanh mình đắp luỹ đất mà đến nay du khách vẫn có thể men theo. Đầu thế kỷ 15, "
        "khi Zvenigorod trở thành kinh đô của một công quốc nhỏ dưới thời Công tước Yury Dmitrievich "
        "- con trai thứ của Đại công tước Dmitry Donskoy - vùng đất bước vào thời thịnh vượng ngắn "
        "ngủi nhưng rực rỡ về nghệ thuật. Vào khoảng năm 1399, trên đỉnh Gorodok mọc lên nhà thờ "
        "Đức Mẹ Lên Trời bằng đá vôi trắng, thuộc số ít công trình đá trắng thời sơ kỳ Moskva còn "
        "sót lại (cùng nhóm với nhà thờ ở Kolomna cũ, tu viện Trinity-Sergius và tu viện "
        "Savvino-Storozhevsky ngay gần đó). Đây là kiểu nhà thờ một vòm, bốn cột, khối vuông vức "
        "vươn lên gọn gàng, điểm nhấn là dải hoa văn chạm khắc chạy ngang thân tường và những vòm "
        "cửa hình lưỡi mác thanh thoát - ngôn ngữ tạo hình đặc trưng của kiến trúc Moskva buổi đầu. "
        "Bên trong còn giữ được những mảng bích hoạ đầu thế kỷ 15; giới nghiên cứu từ lâu gắn phần "
        "quý giá nhất trong số đó với xưởng vẽ của Andrei Rublev và Daniil Chyorny, và các đợt trùng "
        "tu gần đây tiếp tục phát lộ thêm nhiều diện tranh cổ. Zvenigorod cũng là nơi năm 1918 người "
        "ta tình cờ tìm thấy bộ ba icon trứ danh - Đấng Cứu Thế, Tổng lãnh thiên thần Mikhail và "
        "Tông đồ Phaolô - thường gọi là 'Chin Zvenigorod', được cho là tác phẩm của Rublev, nay là "
        "báu vật của Bảo tàng Tretyakov ở Moskva. Từ năm 1995, ngôi thánh đường trở thành podvorye "
        "(giáo sở phụ thuộc) của tu viện Savvino-Storozhevsky, vừa là nơi hành lễ vừa là một di tích "
        "kiến trúc - nghệ thuật hạng nhất mà bất cứ ai quan tâm tới nước Nga cổ đều nên ghé thăm."
    ),
    "highlights_vi": [
        "Một trong những nhà thờ đá trắng cổ nhất còn lại của vùng Moskva (khoảng năm 1399), tiêu biểu cho kiến trúc 'sơ kỳ Moskva'.",
        "Bích hoạ đầu thế kỷ 15 được nhiều nhà nghiên cứu gắn với Andrei Rublev và Daniil Chyorny; các đợt trùng tu gần đây phát lộ thêm nhiều mảng vẽ.",
        "Gắn với bộ ba icon 'Chin Zvenigorod' (Đấng Cứu Thế, Tổng lãnh Mikhail, Tông đồ Phaolô) tìm thấy năm 1918, nay ở Bảo tàng Tretyakov.",
    ],
    "practical": {
        "hours_vi": "Là nhà thờ đang hoạt động, thường mở ban ngày theo giờ lễ (khoảng 8:00–19:00); nên tránh làm phiền trong giờ hành lễ.",
        "ticket_vi": "Vào tự do; hoan nghênh quyên góp. Không thu vé tham quan như bảo tàng.",
        "duration_vi": "Khoảng 30–45 phút cho riêng nhà thờ và luỹ đất.",
        "best_time_vi": "Cuối xuân đến đầu thu, trời khô ráo; sáng sớm ánh sáng đẹp để ngắm mặt tường đá trắng.",
        "tips_vi": "Rất tiện kết hợp với tu viện Savvino-Storozhevsky cách đó chỉ vài km. Ăn mặc kín đáo, nữ nên mang khăn trùm đầu. Từ Moskva đi tàu ngoại ô tới ga Zvenigorod rồi bắt xe buýt/taxi lên Gorodok.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Успенский собор на Городке", "Assumption Cathedral on Gorodok", "Звенигород, Московская область", "Zvenigorod, Moscow Oblast", 55.733067, 36.840248),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Успенский собор на Городке (Звенигород)", "url": "https://ru.wikipedia.org/wiki/%D0%A3%D1%81%D0%BF%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BE%D0%B1%D0%BE%D1%80_%D0%BD%D0%B0_%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%BA%D0%B5"},
        {"title": "Wikipedia (EN) — Zvenigorod (Gorodok, Dormition Cathedral)", "url": "https://en.wikipedia.org/wiki/Zvenigorod"},
        {"title": "Культурные объекты Московской области — Успенский собор на Городке", "url": "https://mosculture.ru/object_mo/1-3-uspenskij-sobor-zvonnitsa-na-gorodke-i-zemlyanye-valy-1399-g/"},
    ],
    "tags": ["church", "cathedral", "medieval", "rublev", "zvenigorod", "white-stone", "day-trip"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


GORKI_LENINSKIYE = {
    "id": "moscow-oblast-gorki-leninskiye",
    "slug": "gorki-leninskiye",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Bảo tàng - Điền trang Gorki Leninskiye (Muzey-zapovednik «Gorki Leninskiye»)",
    "name_ru": "Музей-заповедник «Горки Ленинские»",
    "name_en": "Gorki Leninskiye State Historical Museum-Reserve",
    "categories": ["museum", "palace", "park_garden"],
    "coordinates": {"lat": 55.50462, "lon": 37.76505},
    "address_vi": "Thị trấn Gorki Leninskiye, Khu đô thị Leninsky, Tỉnh Moskva; cách vành đai MKAD của Moskva khoảng 10 km về phía nam (theo xa lộ Kashirskoye).",
    "rating": None,
    "presentation_short_vi": (
        "Điền trang quý tộc thế kỷ 18–19 bên sông Pakhra, nổi tiếng vì là nơi Vladimir Lenin sống "
        "những năm cuối đời và qua đời ngày 21/1/1924. Toà nhà chính mang diện mạo tân cổ điển do "
        "kiến trúc sư danh tiếng Fyodor Schechtel cải tạo cho nữ chủ nhân Zinaida Morozova những "
        "năm 1910–1914. Ngày nay cả quần thể là một bảo tàng - khu bảo tồn lịch sử rộng lớn với "
        "công viên cổ, nhà - bảo tàng Lenin và toà bảo tàng hiện đại khánh thành năm 1987."
    ),
    "presentation_long_vi": (
        "Lịch sử 'Gorki' bắt đầu từ thế kỷ 18 như một điền trang nhỏ ngoại ô Moskva, rồi qua tay "
        "nhiều chủ nhân. Từ năm 1824, nhà quý tộc kiêm cựu binh Chiến tranh Vệ quốc 1812 A. A. "
        "Pisarev cho xây toà nhà chính bằng đá hai tầng, dựng hai dãy nhà phụ (flügel) và định hình "
        "bố cục công viên còn giữ tới nay. Bước ngoặt đến năm 1909, khi Zinaida Morozova - quả phụ "
        "của ông trùm dệt Savva Morozov - mua lại điền trang và mời Fyodor Schechtel, kiến trúc sư "
        "thời thượng bậc nhất nước Nga, cải tạo toàn bộ: mặt tiền được điểm hàng cột Ionic và mái "
        "hiên bề thế, thêm vườn mùa đông, rồi lắp điện, nước máy, hệ thống sưởi hơi và cả điện thoại "
        "- những tiện nghi hiếm có ở nông thôn đương thời. Sau năm 1918, chính quyền Xô-viết quốc "
        "hữu hoá điền trang và dành cho Lenin làm nơi nghỉ dưỡng; ông về đây tĩnh dưỡng sau vụ mưu "
        "sát năm 1918, rồi từ tháng 5/1923 gần như sống hẳn tại đây cho đến khi qua đời ngày "
        "21/1/1924. Từ đó nơi này mang tên Gorki Leninskiye ('Gorki của Lenin') và toà nhà chính "
        "trở thành nhà - bảo tàng lưu giữ đồ dùng của ông. Năm 1987, ngay trong khuôn viên mọc lên "
        "toà 'Bảo tàng V. I. Lenin' đồ sộ do kiến trúc sư Leonid Pavlov thiết kế - một công trình "
        "tiêu biểu của kiến trúc Xô-viết muộn; đây cũng là nơi trưng bày văn phòng và căn hộ của "
        "Lenin trong Kremlin, được chuyển nguyên trạng về Gorki giữa thập niên 1990 khi toà nhà "
        "Thượng viện trong Kremlin trùng tu. Trong số hàng chục nghìn hiện vật, nổi bật nhất là "
        "chiếc Rolls-Royce Silver Ghost bán xích (bánh trước, xích sau để chạy trên tuyết) - cỗ xe "
        "độc nhất vô nhị từng phục vụ Lenin. Quần thể ngày nay còn có bảo tàng đời sống nông dân Nga, "
        "công viên cổ với tượng đài 'Cái chết của Lãnh tụ' (1958), và những năm gần đây khu vực còn "
        "được dùng làm phim trường - biến Gorki Leninskiye thành điểm tham quan kết hợp lịch sử, "
        "kiến trúc điền trang và ký ức thế kỷ 20."
    ),
    "highlights_vi": [
        "Nơi Lenin sống những năm cuối đời và qua đời (21/1/1924); toà nhà chính do Fyodor Schechtel cải tạo theo lối tân cổ điển với hàng cột Ionic.",
        "Toà 'Bảo tàng V. I. Lenin' (1987) của kiến trúc sư Leonid Pavlov - kiến trúc Xô-viết hoành tráng; bên trong tái dựng văn phòng và căn hộ Kremlin của Lenin.",
        "Chiếc Rolls-Royce Silver Ghost bán xích độc nhất vô nhị của Lenin cùng hơn 40.000 hiện vật; ngoài ra có bảo tàng đời sống nông dân và công viên cổ.",
    ],
    "practical": {
        "hours_vi": "Công viên mở hằng ngày; các khu trưng bày (nhà chính, Bảo tàng Lenin, bảo tàng nông dân) thường mở 10:00–18:00, nhiều khu nghỉ Thứ Hai - nên xem lịch trước.",
        "ticket_vi": "Vào công viên giá thấp hoặc miễn phí; mỗi khu trưng bày bán vé riêng, có vé gộp và nhiều mức ưu đãi.",
        "duration_vi": "Khoảng 2–3 giờ cho cả quần thể.",
        "best_time_vi": "Cuối xuân đến đầu thu để dạo công viên; mùa đông có tuyết phủ cũng đẹp nhưng nên xem giờ mở cửa.",
        "tips_vi": "Từ Moskva: đi metro tới ga Domodedovskaya rồi bắt xe buýt/marshrutka về Gorki Leninskiye, hoặc lái xe theo xa lộ Kashirskoye (~12 km từ MKAD). Khuôn viên rộng, nên đi giày thoải mái.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Музей-заповедник «Горки Ленинские»", "Gorki Leninskiye Museum-Reserve", "Московская область", "Moscow Oblast", 55.50462, 37.76505),
    "official_site": "https://mgorki.ru",
    "sources": [
        {"title": "Wikipedia (EN) — Gorki Leninskiye", "url": "https://en.wikipedia.org/wiki/Gorki_Leninskiye"},
        {"title": "Wikipedia (RU) — Горки (усадьба)", "url": "https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BA%D0%B8_(%D1%83%D1%81%D0%B0%D0%B4%D1%8C%D0%B1%D0%B0)"},
        {"title": "Государственный музей-заповедник «Горки Ленинские» — trang chính thức", "url": "https://mgorki.ru"},
    ],
    "tags": ["museum", "estate", "lenin", "schechtel", "history", "park", "day-trip"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


KONEVETS_MONASTERY = {
    "id": "leningrad-oblast-konevets-monastery",
    "slug": "konevets-monastery",
    "region": "leningrad-oblast",
    "region_name_vi": "Tỉnh Leningrad",
    "federal_district": "Vùng Tây Bắc",
    "name_vi": "Tu viện Konevets - Sinh Nhật Đức Mẹ (Kô-nhe-vét)",
    "name_ru": "Коневский Рождество-Богородичный монастырь",
    "name_en": "Konevsky Monastery",
    "categories": ["church", "monument"],
    "coordinates": {"lat": 60.84778, "lon": 30.58556},
    "address_vi": "Đảo Konevets, mặt tây hồ Ladoga, huyện Priozersk, Tỉnh Leningrad; lên đảo từ vịnh Vladimirskaya bằng tàu (khoảng 40–50 phút).",
    "rating": None,
    "presentation_short_vi": (
        "Tu viện Chính thống giáo cổ kính trên đảo Konevets giữa mặt tây hồ Ladoga, được xem là "
        "'người anh em song sinh' của tu viện Valaam. Do Thánh Arseny Konevsky lập khoảng năm 1393, "
        "nơi đây gìn giữ icon Đức Mẹ Konevskaya mang từ núi Athos về. Đảo mang tên tảng đá khổng lồ "
        "Kon-Kamen ('Đá Ngựa') nặng hơn 750 tấn từng được các bộ tộc Karelia ngoại giáo thờ phụng."
    ),
    "presentation_long_vi": (
        "Konevets là một hòn đảo dài chừng 5 km ở mặt tây hồ Ladoga, cách bờ khoảng một eo nước rộng "
        "5 km. Thời Trung cổ, các bộ tộc Phần Lan - Karelia coi đảo là đất thiêng và thờ một tảng đá "
        "hoa cương khổng lồ hình đầu ngựa nặng hơn 750 tấn, gọi là Kon-Kamen ('Đá Ngựa') - cũng "
        "chính là nguồn gốc tên đảo. Khoảng năm 1393, tu sĩ Arseny (sau là Thánh Arseny Konevsky) "
        "tìm đến đây lập tu viện với ước nguyện đưa dân Karelia ngoại giáo theo Kitô giáo; ngài mang "
        "về icon Đức Mẹ đặc biệt - hình Hài Nhi Giêsu cầm chim bồ câu non - từ núi Athos, về sau nổi "
        "danh là icon Đức Mẹ Konevskaya. Trên đỉnh Đá Ngựa, người ta dựng một nhà nguyện nhỏ đánh "
        "dấu sự lụi tàn của tín ngưỡng cổ. Cũng như Valaam ở phía bắc hồ, Konevets nổi tiếng về "
        "truyền giáo và trở thành một cặp tu viện đảo song sinh của Ladoga. Trải bao thăng trầm - bị "
        "quân Thuỵ Điển chiếm trong Chiến tranh Ingria khiến các tu sĩ phải lánh về Novgorod, rồi hồi "
        "sinh sau Đại chiến Bắc Âu - tu viện bước vào thời hoàng kim thế kỷ 19, khi cả những vị khách "
        "lừng danh như văn hào Alexandre Dumas hay thi sĩ Fyodor Tyutchev cũng tìm đến, còn nhà văn "
        "Nikolai Leskov viết hẳn một thiên bút ký (1873) về nơi này. Nhà thờ chính toà Sinh Nhật Đức "
        "Mẹ hiện nay - khối nhà hai tầng, tám trụ, đội năm vòm xanh - được dựng trong các năm "
        "1800–1809, cùng tháp chuông ba tầng cao 35 m (1810–1812). Sau năm 1917, đảo thuộc về Phần "
        "Lan độc lập; trong Chiến tranh Mùa đông và Chiến tranh Tiếp diễn, các tu sĩ phải sơ tán "
        "(năm 1940 mang theo icon quý), rồi sáp nhập vào tu viện Tân Valamo trên đất Phần Lan. Thời "
        "Xô-viết, đảo trở thành một căn cứ quân sự. Tu viện hồi sinh từ năm 1990–1991; tháng 11/1991 "
        "người ta tìm lại được hài cốt Thánh Arseny. Sau đợt trùng tu quy mô lớn hoàn tất vào cuối "
        "thập niên 2010 - đầu 2020, Konevets trở lại là một trung tâm hành hương và điểm du lịch "
        "đang lên của vùng Tây Bắc, đón dòng khách vượt hồ Ladoga ra đảo."
    ),
    "highlights_vi": [
        "Tu viện đảo do Thánh Arseny Konevsky lập khoảng năm 1393, được coi là 'song sinh' với Valaam trên hồ Ladoga.",
        "Nhà thờ chính toà Sinh Nhật Đức Mẹ (1800–1809) năm vòm xanh cùng tháp chuông cao 35 m (1810–1812).",
        "Tảng đá thiêng Kon-Kamen ('Đá Ngựa') nặng hơn 750 tấn với nhà nguyện nhỏ trên đỉnh - dấu tích tín ngưỡng cổ của người Karelia.",
    ],
    "practical": {
        "hours_vi": "Đón khách hành hương và du khách ban ngày; việc lưu trú hay tham quan sâu cần sắp xếp trước qua Ban Hành hương của tu viện.",
        "ticket_vi": "Vào tu viện tự do (hoan nghênh quyên góp); phí chủ yếu là vé tàu ra đảo hoặc tour trọn gói.",
        "duration_vi": "Thường là chuyến đi trong ngày, tính cả thời gian đi tàu (khoảng nửa ngày đến trọn ngày).",
        "best_time_vi": "Cuối xuân đến đầu thu, khi hồ Ladoga thuận cho tàu bè; mùa đông băng giá khó tiếp cận.",
        "tips_vi": "Từ Saint Petersburg đi theo xa lộ Priozerskoye tới vịnh Vladimirskaya rồi lên tàu ra đảo (~40–50 phút); nên liên hệ Ban Hành hương trước. Ăn mặc kín đáo, nữ mang khăn trùm đầu; mang áo ấm/chống gió vì thời tiết trên hồ đổi nhanh.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Коневский Рождество-Богородичный монастырь", "Konevsky Monastery", "Ленинградская область", "Leningrad Oblast", 60.84778, 30.58556),
    "official_site": "https://konevets.ru",
    "sources": [
        {"title": "Wikipedia (EN) — Konevsky Monastery", "url": "https://en.wikipedia.org/wiki/Konevsky_Monastery"},
        {"title": "Коневский Рождество-Богородичный мужской монастырь — trang chính thức", "url": "https://konevets.ru"},
        {"title": "Глобус Санкт-Петербургской митрополии — Коневский монастырь", "url": "https://globus.aquaviva.ru/konevskiy-rozhdestvo-bogorodichnyy-muzhskoy-monastyr"},
    ],
    "tags": ["church", "monastery", "island", "ladoga", "pilgrimage", "konevets", "arseny"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow-oblast.json": [DORMITION_GORODOK, GORKI_LENINSKIYE],
    "leningrad-oblast.json": [KONEVETS_MONASTERY],
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
    print(f"\nTONG CONG THEM: {total_added} dia diem.")


if __name__ == "__main__":
    main()
