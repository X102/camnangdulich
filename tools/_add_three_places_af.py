# -*- coding: utf-8 -*-
"""_add_three_places_af.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26, tối).

Ưu tiên VÙNG: thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.

Thêm:
  1) Tỉnh Moskva (moscow-oblast)      : Khu bảo tồn thiên nhiên Prioksko-Terrasny (vườn nuôi bò rừng zubr) — park_garden/other
  2) Tỉnh Moskva (moscow-oblast)      : Tu viện Nikolo-Ugreshsky ở Dzerzhinsky — church (Dmitry Donskoy, 1380; tường Palestine độc đáo)
  3) Tỉnh Leningrad (leningrad-oblast): Rừng thông rụng lá Lindulovskaya (Roshchino) — park_garden/other (Di sản UNESCO, rừng trồng cổ nhất châu Âu)

LƯU Ý (đối chiếu tránh trùng — đã quét toàn bộ data/regions/*.json, non-bak):
  - Prioksko-Terrasny / zubr питомник: CHƯA có bản ghi (các match "bison/zubr" khác nằm ở oryol.json = Orlovskoye
    Polesie và sakha.json = bảo tàng voi ma mút) -> bổ sung hợp lý, bổ sung loại hình 'khu bảo tồn thiên nhiên'.
  - Nikolo-Ugreshsky: CHƯA có; "Vladychny" chỉ xuất hiện trong 1 câu tips ở moscow-oblast, không phải bản ghi.
  - Lindulovskaya: CHƯA có bất kì đâu.
  - Gatchina / Priory Palace ĐÃ có trong saint-petersburg.json (đã xác minh lại) nên KHÔNG thêm.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, không sao chép nguyên văn), có ghi nguồn.

TOẠ ĐỘ THẬT, đối chiếu web 2026-07 (nguồn đáng tin, thập phân WGS84):
  - Prioksko-Terrasny (văn phòng hướng dẫn/vào vườn zubr, Данки): 54.912120, 37.573350
        (nhiều nguồn du lịch RU nêu toạ độ экскурсионное бюро; Wikipedia EN nêu tâm khu bảo tồn 54.9036, 37.5467)
  - Nikolo-Ugreshsky (Дзержинский):                               55.622560, 37.838418
        (places.moscow điểm dựng lộ trình; Wikipedia RU infobox 55.62167, 37.84000 — lệch ~0,15 km, cùng quần thể)
  - Lindulovskaya roshcha (gần Рощино, h. Выборг):               60.239476, 29.535834
        (Wikipedia RU infobox; lối vào phía Рощино ~60.2379, 29.5396 — cùng cánh rừng)
Kiểm tra thứ tự lat/lon: lat 54–60 (∈41–70), lon 29–38 (∈19–180), KHÔNG đảo; đều nằm trong phạm vi vùng/thành phố.
CẢNH BÁO tên: dùng "Дзержинский" (Tỉnh Moskva), KHÔNG phải "Дзержинск" (Tỉnh Nizhny Novgorod) khi tra Yandex.

LINK BẢN ĐỒ dạng TRỎ-ĐỊA-ĐIỂM: dùng helper text+ll (khớp convention tools/retrofit_map_links.py) — mở đúng thẻ địa điểm
theo tên + thành phố và canh giữa theo toạ độ đã kiểm chứng. Toạ độ coordinates{lat,lon} vẫn LƯU chuẩn cho GIS.

Chạy:  python3 tools/_add_three_places_af.py
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-26"


def _google(name_en, region_en):
    parts = [name_en]
    if region_en.lower() not in name_en.lower():
        parts.append(region_en)
    parts.append("Russia")
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(", ".join(parts))


def maps_text(name_ru, region_ru, name_en, region_en, lat, lon):
    """Trỏ thẳng tới địa điểm bằng tên + canh giữa theo toạ độ (khớp retrofit_map_links.py)."""
    yq = urllib.parse.quote(f"{name_ru}, {region_ru}")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": _google(name_en, region_en),
    }


# ------------------------------------------------------------------ RECORDS
PRIOKSKO_TERRASNY = {
    "id": "moscow-oblast-prioksko-terrasny-reserve",
    "slug": "prioksko-terrasny-reserve",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Khu bảo tồn thiên nhiên Prioksko-Terrasny (vườn nuôi bò rừng zubr)",
    "name_ru": "Приокско-Террасный государственный природный биосферный заповедник",
    "name_en": "Prioksko-Terrasny Nature Reserve",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 54.912120, "lon": 37.573350},
    "address_vi": "Làng Danki (местечко Данки), khu đô thị Serpukhov, Tỉnh Moskva (mã bưu chính 142200); tả ngạn sông Oka, cách trung tâm Moskva khoảng 80 km về phía nam theo cao tốc Simferopol (M2). Văn phòng hướng dẫn tham quan nằm ngay lối vào khu bảo tồn.",
    "rating": None,
    "presentation_short_vi": (
        "Khu bảo tồn thiên nhiên Prioksko-Terrasny là khu bảo tồn nghiêm ngặt (zapovednik) duy nhất của Tỉnh "
        "Moskva và là một trong những điểm dã ngoại thiên nhiên nổi tiếng nhất gần thủ đô. Thành lập năm 1945 "
        "bên tả ngạn sông Oka gần Serpukhov, nơi đây lừng danh nhờ Vườn nuôi bò rừng bison châu Âu (zubr) "
        "Trung ương lập năm 1948 - cơ sở đã góp phần cứu loài thú khổng lồ này khỏi bờ vực tuyệt chủng."
    ),
    "presentation_long_vi": (
        "Nằm cách Moskva khoảng 80 km về phía nam, trên vùng đồng bằng cát bên tả ngạn sông Oka thuộc huyện "
        "Serpukhov, Prioksko-Terrasny là khu bảo tồn thiên nhiên nghiêm ngặt (zapovednik) duy nhất còn lại của "
        "Tỉnh Moskva. Được thành lập năm 1945, khu bảo tồn rộng gần 5.000 ha nằm ngay ranh giới giữa vùng rừng "
        "taiga châu Âu và vùng rừng lá rộng, nên sở hữu hệ sinh thái chuyển tiếp đa dạng khác thường: khoảng "
        "900 loài thực vật bậc cao, gần 140 loài chim và 54 loài thú. Đặc biệt, dải 'thảo nguyên bên sông Oka' "
        "(Окская флора) với những loài cây thảo nguyên mọc lạc giữa rừng phương bắc từ lâu là một bí ẩn thú vị "
        "của giới thực vật học. Nhưng điều làm nên tên tuổi của Prioksko-Terrasny chính là Vườn nuôi bò rừng "
        "bison châu Âu (zubr) Trung ương, do nhà động vật học Mikhail Zablotsky lập năm 1948. Khi ấy loài zubr "
        "gần như tuyệt chủng ngoài tự nhiên; những cá thể đầu tiên được đưa về từ rừng nguyên sinh Belovezh "
        "(Ba Lan/Belarus) và vùng Tây Kavkaz để gây giống, nuôi lớn rồi thả về các khu rừng khắp nước Nga và "
        "châu Âu. Đến nay hàng trăm con zubr đã ra đời tại đây; vườn còn nuôi một đàn nhỏ bò rừng bison Bắc Mỹ. "
        "Du khách tham quan theo tuyến 'Đường tới đàn zubr' (Doroga k zubram) dài chừng 3 km, đi bộ theo lối mòn "
        "có hướng dẫn viên, leo đài quan sát để ngắm bò rừng trong những khu rừng rào rộng. Cạnh đó là Bảo tàng "
        "Thiên nhiên, các tuyến 'công viên trên cây' (đường dây và cầu treo giữa tán rừng) dành cho gia đình và "
        "trẻ em, cùng chương trình 'Nhận nuôi một con zubr' được nhiều người hưởng ứng. Không được tự ý cho zubr "
        "ăn, nhưng khách có thể mang cà rốt, táo bỏ vào 'Rương điều thiện' để nhân viên dùng trong giờ cho ăn. "
        "Là một trong những khu dự trữ sinh quyển được UNESCO công nhận từ cuối thập niên 1970, Prioksko-Terrasny "
        "là điểm đến trong ngày lí tưởng để kết hợp thiên nhiên, giáo dục môi trường và bảo tồn động vật hoang dã."
    ),
    "highlights_vi": [
        "Vườn nuôi bò rừng bison châu Âu (zubr) Trung ương lập năm 1948 - nơi gây giống và cứu loài zubr khỏi tuyệt chủng, đồng thời nuôi cả một đàn nhỏ bò rừng bison Bắc Mỹ.",
        "Tuyến tham quan 'Đường tới đàn zubr' dài khoảng 3 km với đài quan sát để ngắm bò rừng; có Bảo tàng Thiên nhiên và các tuyến 'công viên trên cây' cho gia đình.",
        "Khu bảo tồn (zapovednik) duy nhất của Tỉnh Moskva, khu dự trữ sinh quyển UNESCO, với hệ sinh thái chuyển tiếp taiga - rừng lá rộng và 'thảo nguyên bên sông Oka' độc đáo.",
    ],
    "practical": {
        "hours_vi": "Mở cửa cả tuần, quanh năm. Việc vào vườn zubr chỉ thực hiện theo suất tham quan có hướng dẫn 'Đường tới đàn zubr': ngày thường thường có các suất 11:00, 13:00 và 15:00; cuối tuần tổ chức theo giờ từ khoảng 9:00 đến 16:00. Nên tới sớm và kiểm tra lịch trên trang chính thức.",
        "ticket_vi": "Vé tuyến tham quan zubr khoảng 400 rúp/người lớn, 200 rúp/trẻ em 6-17 tuổi (giá có thể thay đổi). Không được tự cho zubr ăn; có thể mang cà rốt/táo bỏ vào 'Rương điều thiện'.",
        "duration_vi": "Khoảng 1,5 giờ cho tuyến 'Đường tới đàn zubr'; 2-3 giờ nếu thăm thêm Bảo tàng Thiên nhiên và các tuyến trên cây.",
        "best_time_vi": "Chuyên gia cho rằng ngắm zubr thú vị nhất vào sáng sớm mùa thu và mùa đông. Các tuyến 'công viên trên cây' thường hoạt động khoảng tháng 4-11.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô từ ga Kursky tới Serpukhov (khoảng 2 giờ), rồi bắt xe buýt số 41, 31 hoặc 25 tới bến 'Zapovednik'. Đi ô tô theo cao tốc Simferopol (M2) khoảng 80 km. Mặc đồ đi bộ, mang giày thoải mái; tôn trọng quy định giữ yên lặng và không cho thú ăn.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text("Приокско-Террасный заповедник", "Московская область", "Prioksko-Terrasny Nature Reserve", "Moscow Oblast", 54.912120, 37.573350),
    "official_site": "https://pt-zapovednik.ru/",
    "sources": [
        {"title": "Wikipedia (EN) — Prioksko-Terrasny Nature Reserve", "url": "https://en.wikipedia.org/wiki/Prioksko-Terrasny_Nature_Reserve"},
        {"title": "Trang chính thức — Приокско-Террасный заповедник (pt-zapovednik.ru)", "url": "https://pt-zapovednik.ru/"},
        {"title": "Клуб Приключений (vpoxod.ru) — Приокско-Террасный заповедник", "url": "https://www.vpoxod.ru/page/toponym/prioksko-terrasnyj-zapovednik_info"},
    ],
    "tags": ["nature", "reserve", "bison", "zubr", "wildlife", "biosphere-reserve", "serpukhov", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


NIKOLO_UGRESHSKY = {
    "id": "moscow-oblast-nikolo-ugreshsky-monastery",
    "slug": "nikolo-ugreshsky-monastery",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Tu viện Nikolo-Ugreshsky (Nikolo-Ugreshsky monastyr)",
    "name_ru": "Николо-Угрешский монастырь",
    "name_en": "Nikolo-Ugreshsky Monastery",
    "categories": ["church"],
    "coordinates": {"lat": 55.622560, "lon": 37.838418},
    "address_vi": "Quảng trường Thánh Nikolay (площадь Святителя Николая), số 1, thành phố Dzerzhinsky, Tỉnh Moskva (mã bưu chính 140090); cách trung tâm Moskva khoảng 20 km về phía đông nam, gần sông Moskva.",
    "rating": None,
    "presentation_short_vi": (
        "Tu viện Nikolo-Ugreshsky là một trong những tu viện cổ và nổi tiếng bậc nhất vùng phụ cận Moskva, do "
        "Đại công tước Dmitry Donskoy sáng lập năm 1380 để tạ ơn Thánh Nikolay trước trận Kulikovo. Nằm ở "
        "thành phố Dzerzhinsky phía đông nam Moskva, tu viện gây ấn tượng bởi Nhà thờ Chúa Biến Hình đồ sộ và "
        "bức 'tường Jerusalem' trang trí độc đáo."
    ),
    "presentation_long_vi": (
        "Tương truyền năm 1380, trên đường dẫn quân ra chiến trường Kulikovo, Đại công tước Dmitry Donskoy dừng "
        "chân nghỉ tại nơi này và một hình ảnh Thánh Nikolay Kì Diệu đã hiện ra, tiếp thêm niềm tin cho ông. "
        "Cảm động, ông thốt lên 'Сия вся угреша сердце мое' ('Tất cả những điều này đã sưởi ấm trái tim ta'), và "
        "từ đó vùng đất mang tên Ugresha, còn tu viện được gọi là Nikolo-Ugreshsky. Trải qua sáu thế kỉ, tu viện "
        "nhiều lần bị đốt phá rồi lại hồi sinh: năm 1521 bị quân Hãn Krym thiêu rụi, sang thế kỉ 17 hưng thịnh "
        "nhờ những chuyến 'hành hương Ugresha' của các Sa hoàng dòng Romanov, còn thời trẻ Pyotr I từng nhiều "
        "lần ghé thăm. Diện mạo tráng lệ hiện nay chủ yếu hình thành ở thế kỉ 19: Nhà thờ Chúa Biến Hình "
        "(Spaso-Preobrazhensky) khổng lồ do kiến trúc sư A. S. Kaminsky dựng trong các năm 1880-1894, trở thành "
        "công trình chủ đạo của cả quần thể. Một điểm độc đáo hiếm có là 'Bức tường Palestine' (còn gọi 'tường "
        "Jerusalem') xây giữa thế kỉ 19: mặt tường được trang trí mô phỏng hình bóng thành cổ Jerusalem, biến "
        "một đoạn tường rào thành tác phẩm nghệ thuật. Sau Cách mạng, tu viện bị đóng cửa năm 1925 và ngôi nhà "
        "thờ Thánh Nikolay cổ từ thế kỉ 16 bị phá năm 1940; thị trấn quanh tu viện mang tên Dzerzhinsky, còn "
        "khuôn viên từng bị biến thành trại lao động. Được trả lại cho Giáo hội năm 1991, tu viện được trùng tu "
        "công phu, xây mới nhiều nhà thờ (Nhà thờ Thánh Nikolay được dựng lại năm 2006), mở chủng viện, và nay "
        "là một trung tâm hành hương lớn với tháp chuông, ao thiên nga và vườn cây ăn trái trong khuôn viên rộng "
        "rãi. Hình ảnh tu viện được đưa lên huy hiệu thành phố Dzerzhinsky và từng được khắc trên đồng xu kỉ "
        "niệm của Ngân hàng Nga."
    ),
    "highlights_vi": [
        "Nhà thờ Chúa Biến Hình (Spaso-Preobrazhensky) đồ sộ do kiến trúc sư A. S. Kaminsky xây năm 1880-1894 - công trình chủ đạo của quần thể.",
        "'Bức tường Palestine' (tường Jerusalem) giữa thế kỉ 19, trang trí mô phỏng thành cổ Jerusalem - nét kiến trúc độc đáo hiếm thấy ở các tu viện Nga.",
        "Tu viện do Dmitry Donskoy lập năm 1380 gắn với trận Kulikovo; nay là trung tâm hành hương với tháp chuông, ao thiên nga và vườn cây, biểu tượng trên huy hiệu thành phố Dzerzhinsky.",
    ],
    "practical": {
        "hours_vi": "Khuôn viên tu viện thường mở cửa cho khách hằng ngày, khoảng 6:00-21:00 (có thể thay đổi theo lịch lễ); các nhà thờ mở theo giờ cầu nguyện. Nên kiểm tra lịch trước khi đến.",
        "ticket_vi": "Vào tham quan tự do (không bán vé). Một số bảo tàng/hoạt động trong tu viện hoặc đoàn có hướng dẫn viên có thể tính phí riêng.",
        "duration_vi": "Khoảng 1-2 giờ để dạo quanh khuôn viên, các nhà thờ và bức tường Palestine.",
        "best_time_vi": "Đẹp quanh năm; mùa xuân đến đầu thu thuận tiện dạo vườn và chụp ảnh. Các ngày lễ Chính thống giáo lớn rất đông tín đồ.",
        "tips_vi": "Ăn mặc kín đáo, nữ nên mang khăn trùm đầu khi vào nhà thờ. Từ Moskva có thể đi metro tới khu vực đông nam rồi bắt xe buýt tới bến 'Площадь Святителя Николая (монастырь)' ở Dzerzhinsky. Lưu ý phân biệt Dzerzhinsky (Tỉnh Moskva) với thành phố Dzerzhinsk ở Tỉnh Nizhny Novgorod.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text("Николо-Угрешский монастырь", "Дзержинский, Московская область", "Nikolo-Ugreshsky Monastery", "Dzerzhinsky, Moscow Oblast", 55.622560, 37.838418),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Николо-Угрешский монастырь", "url": "https://ru.wikipedia.org/wiki/Николо-Угрешский_монастырь"},
        {"title": "Places.Moscow — Николо-Угрешский монастырь (địa chỉ, toạ độ)", "url": "https://places.moscow/trip/nikolo-ugreshskiy-monastyr"},
        {"title": "KudaGo — Николо-Угрешский монастырь", "url": "https://kudago.com/msk/place/nikolo-ugreshskij-monastyr/"},
    ],
    "tags": ["monastery", "church", "orthodox", "dmitry-donskoy", "dzerzhinsky", "pilgrimage", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


LINDULOVSKAYA_GROVE = {
    "id": "leningrad-oblast-lindulovskaya-grove",
    "slug": "lindulovskaya-grove",
    "region": "leningrad-oblast",
    "region_name_vi": "Tỉnh Leningrad",
    "federal_district": "Vùng Tây Bắc",
    "name_vi": "Rừng thông rụng lá Lindulovskaya (Lindulovskaya roshcha)",
    "name_ru": "Линдуловская роща",
    "name_en": "Lindulovskaya Grove",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 60.239476, "lon": 29.535834},
    "address_vi": "Gần thị trấn Roshchino, huyện Vyborg, Tỉnh Leningrad; thung lũng sông Roshchinka (tên cũ Lintulovka), eo đất Karelia, cách Saint Petersburg khoảng 60 km về phía tây bắc.",
    "rating": None,
    "presentation_short_vi": (
        "Rừng thông rụng lá Lindulovskaya là khu rừng trồng nhân tạo lâu đời nhất nước Nga và cả châu Âu. Được "
        "gieo trồng từ năm 1738 theo sắc lệnh của Pyotr Đại đế để lấy gỗ đóng tàu cho hạm đội Baltic, rừng thông "
        "rụng lá Siberia bên sông Roshchinka nay là một khu bảo tồn thuộc Di sản Thế giới UNESCO, với những cây "
        "cao trên 40 m."
    ),
    "presentation_long_vi": (
        "Bên thung lũng sông Roshchinka (tên cũ Lintulovka) gần thị trấn Roshchino thuộc huyện Vyborg, cách "
        "Saint Petersburg khoảng 60 km về phía tây bắc trên eo đất Karelia, có một cánh rừng đặc biệt: "
        "Lindulovskaya - khu rừng trồng nhân tạo lâu đời nhất của Nga và cả châu Âu. Năm 1738, thực hiện một sắc "
        "lệnh trước đó của Pyotr Đại đế nhằm bảo đảm nguồn gỗ tốt để đóng tàu cho hải quân, nhà lâm học người "
        "Đức Ferdinand Fokel đã tổ chức gieo những hạt thông rụng lá (larch) Siberia đầu tiên trên nền đất canh "
        "tác cũ. Loài thông rụng lá vốn không mọc tự nhiên ở vùng này, nhưng cho thứ gỗ bền chắc và chịu nước - "
        "lí tưởng cho thân và ván tàu. Gần ba thế kỉ trôi qua, những hàng cây năm xưa đã vươn thành rừng cổ thụ "
        "uy nghi: nhiều cây cao trên 40 m, thân to cả người ôm, tuổi đời hơn hai trăm năm, tạo nên những 'đại "
        "lộ' thông rụng lá thẳng tắp hiếm nơi nào có. Rừng được lập thành khu bảo tồn (zakaznik) năm 1976 và từ "
        "đó trở thành điểm dạo bộ, dã ngoại và chụp ảnh được yêu thích của người dân Saint Petersburg, rực rỡ "
        "nhất vào mùa thu khi lá thông chuyển vàng óng rồi trút xuống thành thảm mềm. Nhờ giá trị lịch sử và "
        "khoa học đặc biệt, Lindulovskaya đã được đưa vào danh mục Di sản Thế giới của UNESCO như một hợp phần "
        "của quần thể 'Trung tâm lịch sử Saint Petersburg và các cụm di tích liên quan'. Tới đây, du khách có "
        "thể tản bộ dưới tán thông rụng lá cổ thụ, ngắm dòng Roshchinka và tận hưởng không khí trong lành - một "
        "'bảo tàng sống' của ngành lâm nghiệp Nga."
    ),
    "highlights_vi": [
        "Khu rừng trồng nhân tạo lâu đời nhất nước Nga và châu Âu, gieo trồng từ năm 1738 theo sắc lệnh của Pyotr Đại đế để lấy gỗ đóng tàu.",
        "Những 'đại lộ' thông rụng lá (larch) Siberia cổ thụ cao trên 40 m, tuổi đời hơn hai thế kỉ; đẹp nhất vào mùa thu lá vàng.",
        "Hợp phần của Di sản Thế giới UNESCO 'Trung tâm lịch sử Saint Petersburg và các cụm di tích liên quan'; được lập thành khu bảo tồn từ năm 1976.",
    ],
    "practical": {
        "hours_vi": "Khu bảo tồn ngoài trời, có thể dạo quanh năm vào ban ngày. Không có giờ đóng/mở cố định; nên đi ban ngày để an toàn và dễ tìm đường.",
        "ticket_vi": "Vào tham quan tự do (thường không thu phí). Là khu bảo tồn nên cần giữ gìn: không đốt lửa, không xả rác, không bẻ cây.",
        "duration_vi": "Khoảng 1,5-2,5 giờ để đi hết các lối mòn chính dưới tán rừng và ra bờ sông Roshchinka.",
        "best_time_vi": "Đẹp nhất vào mùa thu (cuối tháng 9 - tháng 10) khi lá thông rụng lá chuyển vàng; mùa hè xanh mát, mùa đông tuyết phủ yên tĩnh.",
        "tips_vi": "Từ Saint Petersburg đi tàu ngoại ô từ ga Finlyandsky về hướng Vyborg, xuống ga Roshchino rồi đi taxi/đi bộ tới rừng; hoặc đi ô tô theo cao tốc Skandinaviya (A181). Mang giày đi bộ, nước uống và thuốc chống côn trùng vào mùa hè.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text("Линдуловская роща", "Ленинградская область", "Lindulovskaya Grove larch reserve", "Leningrad Oblast", 60.239476, 29.535834),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Линдуловская роща", "url": "https://ru.wikipedia.org/wiki/Линдуловская_роща"},
        {"title": "Туристер.Ру — Линдуловская роща", "url": "https://www.tourister.ru/world/europe/russia/city/saint_petersburg/reserves/28526"},
        {"title": "World Heritage Site — Historic Centre of Saint Petersburg (hợp phần Lindulovskaya)", "url": "https://www.worldheritagesite.org/list/st-petersburg/"},
    ],
    "tags": ["nature", "reserve", "larch", "forest", "unesco", "karelian-isthmus", "vyborg", "day-trip", "leningrad-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow-oblast.json": [PRIOKSKO_TERRASNY, NIKOLO_UGRESHSKY],
    "leningrad-oblast.json": [LINDULOVSKAYA_GROVE],
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
