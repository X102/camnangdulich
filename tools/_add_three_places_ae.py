# -*- coding: utf-8 -*-
"""_add_three_places_ae.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26, tối/khuya).

Ưu tiên VÙNG: thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.

Thêm:
  1) Tỉnh Moskva (moscow-oblast)      : Bảo tàng Trung tâm Không quân ở Monino — museum (hàng không, hoành tráng)
  2) Tỉnh Leningrad (leningrad-oblast): Nhà thờ Thánh Andrei trên sông Vuoksa (Vasilyevo, h. Priozersk) — church (kỉ lục Guinness, hiện đại 2000)
  3) Tỉnh Leningrad (leningrad-oblast): Di tích thiên nhiên Sablino (hang động & thác nước) — nature/other (day-trip nổi tiếng gần SPb)

LƯU Ý (đối chiếu tránh trùng — đã quét toàn bộ data/regions/*.json):
  - moscow-oblast trước nay chưa có bảo tàng hàng không; Monino là một trong những bảo tàng hàng không LỚN NHẤT
    châu Âu, loại hình 'museum' mới cho vùng -> bổ sung hợp lý.
  - Gatchina/Priory Palace ĐÃ có trong saint-petersburg.json (đã xác minh) nên KHÔNG thêm.
  - leningrad-oblast đang thiên về pháo đài/tu viện/đài tưởng niệm; bổ sung 1 nhà thờ gỗ độc đáo (Vuoksa) và
    1 di tích thiên nhiên (Sablino: hang + thác) để cân bằng loại hình; cả hai chưa có trong CSDL.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, không sao chép nguyên văn), có ghi nguồn.
Toạ độ THẬT, đối chiếu web 2026-07 (nguồn đáng tin, thập phân WGS84):
  - Monino (Музей ВВС) : 55.830481, 38.188139  (culture.ru / Wikipedia; ул. Музейная, 1, пгт Монино)
  - Vuoksa (храм)      : 60.877009, 29.824944  (nhiều nguồn du lịch + 2ГИС/Yandex org; đảo đá cạnh Васильево)
  - Sablino (пещера)   : 59.66694, 30.79639    (Левобережная пещера N59°40′01″ E30°47′47″; водопад Саблинка kề bên)
Kiểm tra thứ tự lat/lon: lat 55–61 (∈41–70), lon 29–38 (∈19–180), KHÔNG đảo; đều nằm trong phạm vi vùng.

LINK BẢN ĐỒ dạng TRỎ-ĐỊA-ĐIỂM:
  - Monino & Vuoksa: dùng URL trang tổ chức Yandex (yandex.com/maps/org/.../<id>/) — mở đúng THẺ ĐỊA ĐIỂM.
  - Sablino: dùng helper text+ll (khớp convention tools/retrofit_map_links.py) vì là quần thể tự nhiên, không có 1 org sạch.
Toạ độ coordinates{lat,lon} vẫn LƯU chuẩn cho bản đồ nội bộ/GIS.

Chạy:  python3 tools/_add_three_places_ae.py
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


def maps_org(org_url, name_en, region_en):
    """Ưu tiên URL trang tổ chức Yandex (mở đúng THẺ ĐỊA ĐIỂM)."""
    return {"yandex": org_url, "google": _google(name_en, region_en)}


# ------------------------------------------------------------------ RECORDS
MONINO_AIRFORCE = {
    "id": "moscow-oblast-central-air-force-museum-monino",
    "slug": "central-air-force-museum-monino",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Bảo tàng Trung tâm Không quân (Monino)",
    "name_ru": "Центральный музей Военно-воздушных сил",
    "name_en": "Central Air Force Museum (Monino)",
    "categories": ["museum"],
    "coordinates": {"lat": 55.830481, "lon": 38.188139},
    "address_vi": "Phố Muzeynaya số 1, làng đô thị Monino, khu đô thị Shchyolkovo, Tỉnh Moskva; cách trung tâm Moskva khoảng 38 km về phía đông, gần ga đường sắt Monino (tuyến Yaroslavsky).",
    "rating": None,
    "presentation_short_vi": (
        "Bảo tàng Trung tâm Không quân ở Monino là một trong những bảo tàng hàng không lớn nhất châu Âu, "
        "trưng bày gần như trọn vẹn lịch sử phát triển của ngành hàng không quân sự Nga. Được lập năm 1958 "
        "trên nền một sân bay quân sự cũ và mở cửa đón khách từ năm 1960, nơi đây quy tụ hàng trăm máy bay, "
        "trực thăng cùng nhiều nguyên mẫu thử nghiệm độc nhất vô nhị, phần lớn trưng bày ngoài trời trên "
        "đường băng cũ."
    ),
    "presentation_long_vi": (
        "Nằm ở làng Monino phía đông Moskva, Bảo tàng Trung tâm Không quân (thường gọi tắt là Bảo tàng ВВС "
        "Monino) ra đời năm 1958 và chính thức mở cửa ngày 23 tháng 2 năm 1960, tận dụng lại sân bay, nhà "
        "xưởng và các nhà chứa máy bay của một sư đoàn không quân từng đóng ở đây. Qua hơn sáu thập kỉ, bộ "
        "sưu tập phình to thành một trong những kho tàng hàng không đồ sộ nhất châu lục: khoảng gần 200 khí "
        "tài bay đủ loại - từ những chiếc máy bay thuở sơ khai đầu thế kỉ 20, tiêm kích, cường kích, ném "
        "bom, vận tải, tới các mẫu trực thăng và tên lửa hành trình - cùng hàng chục nghìn hiện vật về động "
        "cơ, vũ khí, trang bị và tài liệu lịch sử. Điều làm nên danh tiếng đặc biệt của Monino là những mẫu "
        "máy bay hiếm có, nhiều chiếc là nguyên mẫu thử nghiệm duy nhất còn tồn tại trên thế giới: có thể kể "
        "tới máy bay chở khách siêu thanh Tu-144, chiếc trực thăng khổng lồ Mi-12 (V-12) lớn nhất từng được "
        "chế tạo, hay các mẫu thử tốc độ cao táo bạo của thời Chiến tranh Lạnh. Phần lớn hiện vật đặt ngoài "
        "trời dọc đường băng cũ, xen kẽ ba nhà chứa (hangar) và hai gian trưng bày trong nhà, nên khách gần "
        "như được đi bộ giữa một 'bảo tàng sống' của ngành hàng không Xô-viết và Nga. Đây là điểm hành "
        "hương quen thuộc của người mê hàng không từ khắp nơi (bảo tàng từng đón khách từ hơn 80 quốc gia) "
        "và là một chuyến đi trong ngày lí tưởng từ Moskva cho các gia đình cùng người yêu kĩ thuật. Cần "
        "lưu ý: Monino nằm cạnh cơ sở quân sự nên du khách nên mang theo giấy tờ tuỳ thân và kiểm tra trước "
        "quy định chụp ảnh cũng như giờ mở cửa."
    ),
    "highlights_vi": [
        "Bộ sưu tập gần 200 máy bay, trực thăng và tên lửa - một trong những bảo tàng hàng không lớn nhất châu Âu, trải rộng ngoài trời trên nền sân bay quân sự cũ.",
        "Nhiều mẫu độc nhất và nguyên mẫu thử nghiệm hiếm gặp, như máy bay siêu thanh Tu-144 và trực thăng khổng lồ Mi-12 (V-12) lớn nhất thế giới.",
        "Ba nhà chứa và hai gian trưng bày trong nhà bổ sung phần động cơ, vũ khí, quân phục và tài liệu; lí tưởng cho chuyến đi trong ngày từ Moskva.",
    ],
    "practical": {
        "hours_vi": "Thường mở cửa Thứ Tư–Chủ nhật: các nhà chứa (trong nhà) khoảng 9:00–17:45, khu trưng bày ngoài trời khoảng 10:00–18:45; nghỉ Thứ Hai và Thứ Ba. Nên kiểm tra lịch trên trang chính thức trước khi đi.",
        "ticket_vi": "Vé vào cửa ở mức phải chăng (thường khoảng 200–400 rúp, có ưu đãi cho học sinh/sinh viên/người cao tuổi). Một số chương trình tham quan có hướng dẫn hoặc dịch vụ chụp ảnh có thể tính phí riêng.",
        "duration_vi": "Khoảng 2–3 giờ để đi hết khu ngoài trời và các nhà chứa; người mê hàng không có thể ở lâu hơn.",
        "best_time_vi": "Mùa xuân đến đầu thu (tháng 5–9) dễ chịu nhất cho phần trưng bày ngoài trời; ngày nắng ráo thuận tiện chụp ảnh máy bay.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô từ ga Yaroslavsky đến ga Monino (khoảng 1 giờ), rồi đi bộ/taxi tới bảo tàng. Nên mang giấy tờ tuỳ thân (khu vực gần cơ sở quân sự) và mặc đồ đi bộ thoải mái vì khuôn viên rất rộng.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_org("https://yandex.com/maps/org/tsentralny_muzey_voyenno_vozdushnykh_sil/1043220919/", "Central Air Force Museum Monino", "Moscow Oblast"),
    "official_site": "https://cmvvs.ru/",
    "sources": [
        {"title": "Wikipedia (RU) — Центральный музей Военно-воздушных сил", "url": "https://ru.wikipedia.org/wiki/Центральный_музей_Военно-воздушных_сил"},
        {"title": "Культура.РФ — Центральный музей Военно-воздушных сил (Монино)", "url": "https://www.culture.ru/institutes/56239/centralnyi-muzei-voenno-vozdushnykh-sil"},
        {"title": "Trang chính thức — ЦМ ВВС (cmvvs.ru)", "url": "https://cmvvs.ru/"},
    ],
    "tags": ["museum", "aviation", "air-force", "aircraft", "monino", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


VUOKSA_CHURCH = {
    "id": "leningrad-oblast-st-andrew-church-vuoksa",
    "slug": "st-andrew-church-vuoksa",
    "region": "leningrad-oblast",
    "region_name_vi": "Tỉnh Leningrad",
    "federal_district": "Vùng Tây Bắc",
    "name_vi": "Nhà thờ Thánh Andrei Được gọi Đầu tiên trên sông Vuoksa",
    "name_ru": "Церковь Андрея Первозванного на Вуоксе",
    "name_en": "Church of St. Andrew the First-Called on the Vuoksa",
    "categories": ["church"],
    "coordinates": {"lat": 60.877009, "lon": 29.824944},
    "address_vi": "Trên một đảo đá nhỏ giữa sông Vuoksa, cạnh làng Vasilyevo (nằm giữa Melnikovo và Losevo), huyện Priozersk, Tỉnh Leningrad; theo đường 41K-153 (Sapernoe–Melnikovo), có bãi đỗ xe đối diện làng.",
    "rating": None,
    "presentation_short_vi": (
        "Nhà thờ gỗ Thánh Andrei Được gọi Đầu tiên là một trong những hình ảnh biểu tượng của eo đất Karelia "
        "và Tỉnh Leningrad: ngôi nhà thờ nhỏ dựng trên một mỏm đá vươn lên giữa dòng Vuoksa. Hoàn thành năm "
        "2000, công trình được sách Kỉ lục Guinness ghi nhận là nhà thờ duy nhất trên thế giới xây trên một "
        "đảo đá tí hon mà nền móng chính là khối đá nguyên khối nhô khỏi mặt nước."
    ),
    "presentation_long_vi": (
        "Giữa dòng Vuoksa - con sông lớn nhất eo đất Karelia - có một đảo đá chỉ rộng chừng trăm mét vuông, "
        "và trên đó là nhà thờ gỗ Thánh Andrei Được gọi Đầu tiên, một trong những cảnh quan được chụp ảnh "
        "nhiều nhất vùng Tây Bắc nước Nga. Ý tưởng ban đầu chỉ là dựng một chỗ nghỉ chân cho dân chèo "
        "thuyền, nhưng rồi được nâng thành việc xây một nhà thờ; công trình do kiến trúc sư Andrey Rotinov "
        "thiết kế, lấy cảm hứng từ dáng vươn cao của Nhà thờ Chúa Thăng Thiên ở Kolomenskoye. Việc xây dựng "
        "được Đô thành Ioann (Snychev) của Saint Petersburg và Ladoga ban phép lành năm 1994, và nhà thờ "
        "được thánh hiến ngày 23 tháng 9 năm 2000, dâng kính Thánh tông đồ Andrei - người mà theo truyền "
        "thuyết từng tới vùng này và làm phép rửa cho dân bản địa; ngài được coi là bổn mạng của ngư dân và "
        "người đi biển, còn lá cờ Thánh Andrei (chữ thập xanh chéo trên nền trắng) là quân kì của Hải quân "
        "Nga. Nhà thờ mang kiểu 'bát giác' (vosmerik) truyền thống, đội mái lều nhọn (shatyor) với chỏm "
        "hành, hai bên là gian tiền đường và gian thánh, phía trên tiền đường có một tháp chuông nhỏ. Trước "
        "kia đảo chỉ nối với bờ bằng phà; về sau người ta bắc một cây cầu chắc chắn để đón lượng khách ngày "
        "một đông, dù nhiều người tiếc rằng cây cầu làm giảm phần nào vẻ tách biệt huyền hoặc vốn có. Nằm "
        "giữa thiên nhiên hồ - sông - rừng của eo đất Karelia, nhà thờ đẹp trong mọi mùa: phủ tuyết mùa "
        "đông, sương sớm mùa hè hay lá vàng mùa thu, và thường được ghép trong hành trình khám phá "
        "Priozersk, ghềnh Losevo và vùng sông Vuoksa."
    ),
    "highlights_vi": [
        "Nhà thờ gỗ dựng trên đảo đá tí hon giữa sông Vuoksa - được sách Kỉ lục Guinness ghi nhận là nhà thờ duy nhất thế giới có nền là khối đá nguyên khối giữa dòng nước.",
        "Kiến trúc gỗ kiểu bát giác với mái lều nhọn, lấy cảm hứng từ Nhà thờ Chúa Thăng Thiên ở Kolomenskoye; thánh hiến năm 2000, dâng kính Thánh tông đồ Andrei - bổn mạng của ngư dân và người đi biển.",
        "Một trong những khung cảnh được chụp ảnh nhiều nhất eo đất Karelia, đẹp cả bốn mùa; dễ ghép cùng Priozersk, ghềnh Losevo và hành trình sông Vuoksa.",
    ],
    "practical": {
        "hours_vi": "Nhà thờ nhỏ, thường mở cửa cho khách vào cuối tuần khoảng 12:00–17:00; lễ được cử hành theo lịch riêng, chủ yếu vào mùa hè. Khuôn viên ngoài trời và cây cầu có thể ngắm cảnh, chụp ảnh mọi lúc.",
        "ticket_vi": "Vào tham quan tự do (không bán vé). Nếu muốn dự lễ hoặc làm các bí tích (rửa tội, hôn phối) cần liên hệ trước với giáo xứ.",
        "duration_vi": "Khoảng 30–60 phút để tham quan, đi qua cầu ra đảo và chụp ảnh.",
        "best_time_vi": "Đẹp quanh năm; mùa hè và mùa thu lá vàng thuận tiện đi lại và chụp ảnh nhất, mùa đông tuyết phủ cho khung cảnh cổ tích nhưng đường trơn.",
        "tips_vi": "Từ Saint Petersburg đi theo hướng Priozersk rồi rẽ vào đường 41K-153 (Sapernoe–Melnikovo); lấy làng Vasilyevo làm mốc, gửi xe ở bãi đối diện rồi đi bộ theo lối mòn ra bờ Vuoksa. Nên đi bằng ô tô vì giao thông công cộng tới tận nơi hạn chế; có thể kết hợp thăm ghềnh Losevo và thị trấn Priozersk (pháo đài Korela) trong cùng chuyến.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_org("https://yandex.com/maps/org/tserkov_andreya_pervozvannogo_na_vuokse/1000401335/", "Church of St Andrew the First-Called on the Vuoksa", "Leningrad Oblast"),
    "official_site": "https://melnikovo.cerkov.ru/pervozvanny/",
    "sources": [
        {"title": "Глобус Санкт-Петербургской митрополии — Храм св. ап. Андрея Первозванного на Вуоксе", "url": "https://globus.aquaviva.ru/khram-sv-ap-andreya-pervozvannogo-na-vuokse"},
        {"title": "Приход — melnikovo.cerkov.ru (Андрей Первозванный на Вуоксе)", "url": "https://melnikovo.cerkov.ru/pervozvanny/"},
        {"title": "Дорогами Срединного Пути (anashina.com) — Храм апостола Андрея Первозванного на Вуоксе", "url": "https://anashina.com/xram-apostola-andreya-pervozvannogo-na-vuokse/"},
    ],
    "tags": ["church", "wooden-architecture", "vuoksa", "karelian-isthmus", "priozersk", "guinness-record", "leningrad-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


SABLINO = {
    "id": "leningrad-oblast-sablino-natural-monument",
    "slug": "sablino-natural-monument",
    "region": "leningrad-oblast",
    "region_name_vi": "Tỉnh Leningrad",
    "federal_district": "Vùng Tây Bắc",
    "name_vi": "Di tích thiên nhiên Sablino (hang động và thác nước Sablinsky)",
    "name_ru": "Саблинский памятник природы",
    "name_en": "Sablino Natural Monument (Sablinsky)",
    "categories": ["park_garden", "other"],
    "coordinates": {"lat": 59.66694, "lon": 30.79639},
    "address_vi": "Gần làng đô thị Ulyanovka (tên cũ Sablino), huyện Tosno, Tỉnh Leningrad; hai bên thung lũng sông Sablinka và Tosna, cách Saint Petersburg khoảng 40 km về phía đông nam.",
    "rating": None,
    "presentation_short_vi": (
        "Di tích thiên nhiên Sablino là một trong những điểm dã ngoại trong ngày được yêu thích nhất quanh "
        "Saint Petersburg: một quần thể hang động nhân tạo, thác nước và hẻm sông để lộ các tầng đá cổ hàng "
        "trăm triệu năm. Được công nhận là di tích thiên nhiên từ năm 1976, nơi đây hấp dẫn du khách bằng "
        "những chuyến chui hang có hướng dẫn, hai thác nước trên sông Sablinka và Tosna, cùng nhiều dấu tích "
        "lịch sử."
    ),
    "presentation_long_vi": (
        "Cách Saint Petersburg chừng 40 km về phía đông nam, quanh làng Ulyanovka (tên cũ là Sablino) thuộc "
        "huyện Tosno, thiên nhiên đã bào mòn hai con sông nhỏ Sablinka và Tosna thành những hẻm vực, để lộ "
        "các lớp đá trầm tích kỉ Cambri và Ordovic có tuổi tới khoảng nửa tỉ năm - một 'trang giáo khoa địa "
        "chất' lộ thiên hiếm có ở gần đô thị. Đan xen giữa cảnh quan ấy là hệ thống hang động: khác với hang "
        "tự nhiên, đây là các đường hầm do con người đào từ thế kỉ 19 đến đầu thế kỉ 20 để khai thác cát "
        "thạch anh cung cấp cho các nhà máy thuỷ tinh khắp nước Nga; khi việc khai thác dừng lại, những hầm "
        "cát bỏ hoang biến thành mê cung ngầm mát lạnh, nay là nơi trú đông của loài dơi. Hang lớn nhất mở "
        "cho khách tham quan là Levoberezhnaya ('Tả Ngạn'), nơi có các tour chui hang đội mũ bảo hộ, nghe "
        "kể về địa chất và truyền thuyết địa phương. Bên cạnh giá trị tự nhiên, Sablino còn giàu dấu ấn "
        "lịch sử: gần đây là những gò mộ cổ, địa điểm được cho là nơi công tước Aleksandr Nevsky hạ trại "
        "trước trận đánh với quân Thuỵ Điển bên sông Neva năm 1240, và điền trang 'Pustynka' của thi hào "
        "Aleksey Konstantinovich Tolstoy. Với thác nước, hẻm sông, hang động và lịch sử hoà quyện, Sablino "
        "là lựa chọn quen thuộc cho các chuyến đi trong ngày, dã ngoại và du lịch địa chất - sinh thái từ "
        "Saint Petersburg; du khách nên đi cùng tour có hướng dẫn khi vào hang và mang giày chống trơn."
    ),
    "highlights_vi": [
        "Chui hang có hướng dẫn trong hang nhân tạo Levoberezhnaya - đường hầm khai thác cát thạch anh xưa, nay là mê cung ngầm và nơi dơi trú đông.",
        "Hai thác nước trên sông Sablinka và Tosna cùng hẻm vực để lộ các tầng đá kỉ Cambri - Ordovic khoảng nửa tỉ năm tuổi.",
        "Dấu tích lịch sử: gò mộ cổ, nơi tương truyền Aleksandr Nevsky hạ trại năm 1240 và điền trang 'Pustynka' của thi hào A. K. Tolstoy.",
    ],
    "practical": {
        "hours_vi": "Khu di tích ngoài trời (thác, hẻm sông) có thể dạo quanh năm. Tham quan hang động phải đi theo tour có hướng dẫn của đơn vị khai thác, tổ chức theo suất trong ngày - nên đặt trước, nhất là cuối tuần.",
        "ticket_vi": "Đi dạo khu thác và hẻm sông cơ bản không thu phí; tour chui hang Levoberezhnaya bán vé theo suất (thường đã gồm mũ bảo hộ và hướng dẫn viên). Giá thay đổi theo chương trình, nên kiểm tra trước.",
        "duration_vi": "Khoảng 1 giờ cho một tour hang; 2–3 giờ nếu đi thêm cả hai thác và dạo hẻm sông.",
        "best_time_vi": "Thác đẹp nhất vào mùa xuân khi tuyết tan (tháng 4–5) và sau mưa; hang mát ổn định quanh năm (khoảng 8°C) nên mang áo ấm khi vào hang kể cả mùa hè. Mùa đông đường trơn, cần cẩn trọng.",
        "tips_vi": "Từ Saint Petersburg đi tàu ngoại ô hướng Tosno/Moskva, xuống ga Sablino (Ulyanovka) rồi đi bộ/taxi tới khu thác - hang; hoặc đi ô tô theo cao tốc M10. Bắt buộc đi tour có hướng dẫn khi vào hang (không tự ý vào vì dễ lạc); mang giày chống trơn và đèn pin.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text("Саблинский памятник природы", "Ленинградская область", "Sablino Natural Monument caves and waterfalls", "Leningrad Oblast", 59.66694, 30.79639),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Саблинский памятник природы", "url": "https://ru.wikipedia.org/wiki/Саблинский_памятник_природы"},
        {"title": "vpoxod.ru — Саблинские пещеры: история, как добраться", "url": "https://www.vpoxod.ru/page/toponym/sablino_info"},
        {"title": "Туристер.Ру — Саблинский водопад (координаты, как добраться)", "url": "https://www.tourister.ru/world/europe/russia/city/ulyanovka/waterfall/28772"},
    ],
    "tags": ["nature", "caves", "waterfall", "geology", "sablino", "tosno", "day-trip", "leningrad-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow-oblast.json": [MONINO_AIRFORCE],
    "leningrad-oblast.json": [VUOKSA_CHURCH, SABLINO],
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
