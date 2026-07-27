# -*- coding: utf-8 -*-
"""_add_three_places_ag.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26, đêm).

Ưu tiên VÙNG (a): thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.

Thêm:
  1) Tỉnh Moskva (moscow-oblast)      : Bảo tàng «Tân Jerusalem» (Muzey «Novy Ierusalim»), Istra — museum
        (bảo tàng lớn nhất Tỉnh Moskva; toà nhà «kiến trúc xanh» mới khánh thành 2014-2015)
  2) Tỉnh Moskva (moscow-oblast)      : Nhà thờ Đức Mẹ Vladimir ở Bykovo (Vladimirskaya tserkov) — church
        (kiệt tác Tân Gothic (giả Gothic) Nga cuối thế kỉ 18, gán cho kiến trúc sư V. I. Bazhenov)
  3) Tỉnh Leningrad (leningrad-oblast): Bảo tàng - Điền trang Priyutino ở Vsevolozhsk (Muzey-usadba Priyutino) — museum/park_garden
        (điền trang của A. N. Olenin; «tổ ấm của các thi nhân Nga» thời Pushkin, Krylov)

ĐỐI CHIẾU TRÁNH TRÙNG (đã quét slug/name toàn bộ 2 file vùng, non-bak):
  - moscow-oblast.json (26 bản ghi): có 'new-jerusalem-monastery-istra' (TU VIỆN) nhưng CHƯA có BẢO TÀNG
    «Novy Ierusalim» (toà nhà hiện đại riêng, bên kia sông) -> bổ sung hợp lệ, slug 'novy-ierusalim-museum'.
  - Bykovo / Vladimirskaya church: CHƯA có ở bất kì đâu.
  - leningrad-oblast.json (17 bản ghi): CHƯA có Priyutino. (Gatchina/Priory/Pavlovsk ĐÃ nằm ở saint-petersburg.json.)

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, không sao chép nguyên văn), có ghi nguồn.

TOẠ ĐỘ THẬT — đối chiếu web 2026-07 (thập phân WGS84, nhiều nguồn khớp nhau):
  - Muzey «Novy Ierusalim» (Истра, ул. Ново-Иерусалимская наб., 1): 55.926738, 36.844530
        (bên kia sông Истра, cách Tu viện Tân Jerusalem ~0,5 km về phía bắc; 2GIS/tonkosti/travel.riamo khớp)
  - Владимирская церковь (Быково, Раменский г.о.):                  55.610115, 38.058122
        (sobory.ru object=01404 và places.moscow đều nêu cùng toạ độ)
  - Музей-усадьба «Приютино» (Всеволожск, ул. Приютинская, 1):      60.012264, 30.580619
        (autotravel.ru meta geo.position 60.0123; 30.58117 — khớp; tây nam Vsevolozhsk, gần ga Бернгардовка)
Kiểm tra thứ tự lat/lon: lat 55–60 (∈41–70), lon 30–38 (∈19–180), KHÔNG đảo; đều nằm trong phạm vi vùng/thành phố.
LƯU Ý tên: 'Быково' (Раменский) — có nhiều 'Быково' khác; ghim theo tên nhà thờ + Раменский/toạ độ để tránh nhầm.

LINK BẢN ĐỒ dạng TRỎ-ĐỊA-ĐIỂM: dùng helper text+ll (khớp convention tools/retrofit_map_links.py) — mở đúng thẻ địa
điểm theo tên + thành phố và canh giữa theo toạ độ đã kiểm chứng. Toạ độ coordinates{lat,lon} vẫn LƯU chuẩn cho GIS.

Chạy:  python3 tools/_add_three_places_ag.py
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
NOVY_IERUSALIM_MUSEUM = {
    "id": "moscow-oblast-novy-ierusalim-museum",
    "slug": "novy-ierusalim-museum",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Bảo tàng «Tân Jerusalem» (Muzey «Novy Ierusalim»)",
    "name_ru": "Музейно-выставочный комплекс «Новый Иерусалим»",
    "name_en": "New Jerusalem Museum-Exhibition Complex",
    "categories": ["museum"],
    "coordinates": {"lat": 55.926738, "lon": 36.844530},
    "address_vi": "Đường Ново-Иерусалимская набережная, số 1, thành phố Istra, Tỉnh Moskva (mã bưu chính 143500); nằm bên hữu ngạn sông Istra, đối diện Tu viện Tân Jerusalem, cách trung tâm Moskva khoảng 50 km về phía tây theo cao tốc Volokolamsk/Riga.",
    "rating": None,
    "presentation_short_vi": (
        "Bảo tàng «Tân Jerusalem» là bảo tàng lớn nhất Tỉnh Moskva, với bộ sưu tập hơn 180.000 hiện vật về "
        "lịch sử, nghệ thuật và văn hoá vùng ngoại ô phía tây thủ đô. Cuối năm 2014 bảo tàng chuyển tới một "
        "toà nhà ba tầng hiện đại theo phong cách «kiến trúc xanh», nằm bên kia sông Istra đối diện Tu viện "
        "Tân Jerusalem - một trong những trung tâm trưng bày, triển lãm nổi bật nhất của nước Nga hiện nay."
    ),
    "presentation_long_vi": (
        "Bảo tàng «Tân Jerusalem» (Novy Ierusalim) ra đời năm 1920 ngay trong khuôn viên Tu viện Tân Jerusalem "
        "vừa bị đóng cửa sau Cách mạng, ban đầu là bảo tàng lịch sử - nghệ thuật kết hợp bảo tàng địa phương, "
        "rồi hợp nhất năm 1922. Suốt gần một thế kỉ, sưu tập của bảo tàng lớn dần nhờ hiện vật từ các điền trang "
        "quý tộc bị quốc hữu hoá ở phía tây Tỉnh Moskva, các nhà thờ tu viện và những cuộc khai quật khảo cổ; "
        "đến nay đã vượt hơn 180.000 đơn vị, gồm tranh Nga và châu Âu, tượng, icon cổ, đồ sứ, trang phục, tư "
        "liệu khảo cổ và dân tộc học - khiến nơi đây trở thành bảo tàng lớn nhất và giàu có bậc nhất của tỉnh. "
        "Trong Chiến tranh Vệ quốc, phần lớn quần thể tu viện bị quân Đức phá huỷ khi rút lui năm 1941, nhiều "
        "hiện vật bị mất; bảo tàng phải sơ tán rồi hồi phục dần từ cuối thập niên 1940. Để trả lại không gian "
        "tôn giáo cho tu viện đang được phục dựng, chính quyền Tỉnh Moskva quyết định xây cho bảo tàng một trụ "
        "sở riêng. Cuối năm 2014 - đầu năm 2015, bảo tàng chuyển sang toà nhà ba tầng hoàn toàn mới trên khu "
        "đất rộng 4,28 ha bên hữu ngạn sông Istra, do kiến trúc sư Valery Lukomsky thiết kế theo phong cách "
        "«kiến trúc xanh»: công trình như nép mình vào sườn đồi, mái phủ cỏ, để không lấn át hình bóng cổ kính "
        "của tu viện ở bờ đối diện. Với hơn 10.000 m² diện tích trưng bày, các kho lưu trữ hiện đại, trung tâm "
        "phục chế, phòng triển lãm và khán phòng hoà nhạc, «Novy Ierusalim» nay là một tổ hợp bảo tàng - triển "
        "lãm tầm cỡ, thường xuyên tổ chức những triển lãm nghệ thuật lớn của Nga và quốc tế, kết hợp lí tưởng "
        "với chuyến thăm Tu viện Tân Jerusalem kề bên trong một ngày trọn vẹn ở Istra."
    ),
    "highlights_vi": [
        "Bảo tàng lớn nhất Tỉnh Moskva với hơn 180.000 hiện vật: tranh, icon cổ, đồ sứ, khảo cổ và dân tộc học, phần lớn từ các điền trang quý tộc và nhà thờ vùng tây Moskva.",
        "Toà nhà «kiến trúc xanh» ba tầng khánh thành 2014-2015 (KTS Valery Lukomsky): nép vào sườn đồi, mái phủ cỏ, hơn 10.000 m² trưng bày, để giữ vai trò chủ đạo cho quần thể Tu viện Tân Jerusalem đối diện.",
        "Điểm đến kết hợp hoàn hảo với Tu viện Tân Jerusalem ở bờ sông bên kia; thường xuyên có các triển lãm nghệ thuật lớn tầm quốc gia và quốc tế.",
    ],
    "practical": {
        "hours_vi": "Mở cửa thứ Ba - Chủ nhật, thường 10:00-18:00 (mùa hè), 10:00-17:00 (mùa đông); đóng cửa thứ Hai và thường là thứ Sáu cuối cùng của tháng. Nên kiểm tra lịch trên trang chính thức trước khi đến.",
        "ticket_vi": "Có bán vé vào cửa và vé theo từng triển lãm (giá thay đổi theo chương trình); có ưu đãi cho học sinh, sinh viên, người hưu trí. Nên xem biểu giá và đặt vé trên website njerusalem.ru.",
        "duration_vi": "Khoảng 1,5-2,5 giờ cho các phòng trưng bày thường trực và triển lãm; nếu kết hợp thăm Tu viện Tân Jerusalem nên dành trọn nửa ngày đến một ngày.",
        "best_time_vi": "Tham quan quanh năm vì trưng bày trong nhà; kết hợp dạo bờ sông Istra và tu viện đẹp nhất vào cuối xuân đến đầu thu.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô từ ga Rizhsky hoặc bến xe «Tushinskaya» tới Istra, rồi bắt xe buýt (số 4, 40, 46, 48 - bến «Muzey», hoặc 32, 33 - bến «Teplitsa»). Đi ô tô theo cao tốc Novorizhskoye (M9) hoặc Volokolamskoye khoảng 50 km. Đừng nhầm BẢO TÀNG (toà nhà mới bên sông) với TU VIỆN Tân Jerusalem ở bờ đối diện.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text("Музей «Новый Иерусалим»", "Истра, Московская область", "New Jerusalem Museum", "Istra, Moscow Oblast", 55.926738, 36.844530),
    "official_site": "https://njerusalem.ru/",
    "sources": [
        {"title": "Wikipedia (RU) — Новый Иерусалим (музей)", "url": "https://ru.wikipedia.org/wiki/Новый_Иерусалим_(музей)"},
        {"title": "Trang chính thức — Музей «Новый Иерусалим» (njerusalem.ru)", "url": "https://njerusalem.ru/"},
        {"title": "Культура.РФ — Государственный историко-художественный музей «Новый Иерусалим»", "url": "https://www.culture.ru/institutes/12363/gosudarstvennyi-istoriko-khudozhestvennyi-muzei-novyi-ierusalim"},
    ],
    "tags": ["museum", "art", "history", "green-architecture", "istra", "new-jerusalem", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


BYKOVO_VLADIMIR_CHURCH = {
    "id": "moscow-oblast-bykovo-vladimir-church",
    "slug": "bykovo-vladimir-church",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Nhà thờ Đức Mẹ Vladimir ở Bykovo (Vladimirskaya tserkov)",
    "name_ru": "Церковь Владимирской иконы Божией Матери (Быково)",
    "name_en": "Church of the Vladimir Icon of the Mother of God (Bykovo)",
    "categories": ["church"],
    "coordinates": {"lat": 55.610115, "lon": 38.058122},
    "address_vi": "Làng Bykovo, khu đô thị Ramensky, Tỉnh Moskva (gần thành phố Zhukovsky và sân bay Bykovo); cách trung tâm Moskva khoảng 35 km về phía đông nam.",
    "rating": None,
    "presentation_short_vi": (
        "Nhà thờ Đức Mẹ Vladimir ở làng Bykovo là một trong những nhà thờ độc đáo nhất vùng phụ cận Moskva - "
        "một kiệt tác Tân Gothic (giả Gothic) Nga hiếm có, xây cuối thế kỉ 18 và thường được gán cho kiến trúc "
        "sư lừng danh Vasily Bazhenov. Ngôi thánh đường hai tầng bằng đá trắng với hai tháp nhọn vút cao trông "
        "tựa một lâu đài châu Âu giữa đồng quê Nga."
    ),
    "presentation_long_vi": (
        "Tại làng Bykovo thuộc khu đô thị Ramensky, cách Moskva chừng 35 km về phía đông nam, sừng sững một "
        "công trình khiến ai lần đầu trông thấy cũng ngỡ ngàng: Nhà thờ Đức Mẹ Vladimir - viên ngọc của phong "
        "cách Tân Gothic (người Nga quen gọi là «giả Gothic», псевдоготика) hiếm thấy trong kiến trúc tôn giáo "
        "Chính thống. Nhà thờ được dựng vào những năm 1780 (nhiều nguồn nêu 1783-1789) trên đất điền trang "
        "Bykovo (còn gọi Marino) khi ấy thuộc về Mikhail Izmailov, một quý tộc thân cận triều đình. Theo các "
        "đặc điểm phong cách, thiết kế được gán cho Vasily Bazhenov - bậc thầy kiến trúc Nga thế kỉ 18, người "
        "ưa lối kết hợp mô-típ Gothic phương Tây với truyền thống bản địa. Điểm đặc biệt nhất là nhà thờ có "
        "kết cấu hai tầng (hai nhà thờ chồng lên nhau): tầng dưới cung hiến Chúa Giáng Sinh (Rozhdestva "
        "Khristova), tầng trên dâng kính Icon Đức Mẹ Vladimir, nối với nhau bằng cầu thang vòng cung duyên "
        "dáng dẫn lên sân thượng phía trước. Mặt bằng hình bầu dục lạ mắt, tường ốp đá trắng chạm khắc tinh "
        "xảo, những cửa sổ nhọn kiểu Gothic và đặc biệt là hai tháp chuông cân xứng vươn lên như tháp nhà thờ "
        "châu Âu - tất cả tạo nên vẻ đẹp vừa uy nghi vừa lãng mạn, gần như «có một không hai» ở Nga. Đến năm "
        "1884, một tháp chuông riêng theo phong cách hoà hợp được xây thêm cạnh nhà thờ. Sau thời Xô-viết bị "
        "đóng cửa và xuống cấp, nhà thờ đã được trả lại cho Giáo hội, trùng tu và hoạt động trở lại; nay là "
        "điểm hành hương, chụp ảnh kiến trúc và tham quan trong ngày rất được yêu thích từ Moskva."
    ),
    "highlights_vi": [
        "Kiệt tác kiến trúc Tân Gothic (giả Gothic) Nga hiếm có, xây thập niên 1780, thường được gán cho kiến trúc sư Vasily Bazhenov.",
        "Nhà thờ hai tầng độc đáo: tầng dưới kính Chúa Giáng Sinh, tầng trên kính Icon Đức Mẹ Vladimir; mặt bằng bầu dục, đá trắng chạm khắc, cầu thang vòng cung phía trước.",
        "Hai tháp nhọn cân xứng như lâu đài châu Âu giữa làng quê Nga; tháp chuông riêng dựng thêm năm 1884 - tổng thể được coi là 'có một không hai' ở vùng Moskva.",
    ],
    "practical": {
        "hours_vi": "Là nhà thờ đang hoạt động, thường mở cửa cho khách vào ban ngày theo giờ lễ; bên trong tầng trên có thể chỉ mở vào dịp lễ hoặc theo hẹn. Nên kiểm tra lịch lễ của giáo xứ trước khi đến.",
        "ticket_vi": "Vào tham quan tự do (không bán vé); hoan nghênh đóng góp tuỳ tâm để duy trì và trùng tu.",
        "duration_vi": "Khoảng 30-60 phút để ngắm kiến trúc bên ngoài, cầu thang, hai tháp và (nếu mở) nội thất; có thể kết hợp dạo khu điền trang Bykovo và ao hồ lân cận.",
        "best_time_vi": "Đẹp quanh năm; ánh sáng cuối chiều làm nổi bật đá trắng và hai tháp nhọn - lí tưởng để chụp ảnh. Ngày lễ Chính thống giáo có đông tín đồ.",
        "tips_vi": "Ăn mặc kín đáo khi vào nhà thờ (nữ nên mang khăn trùm đầu). Từ Moskva đi tàu ngoại ô từ ga Kazansky tới ga Bykovo rồi đi bộ/taxi, hoặc đi ô tô theo hướng Zhukovsky/Ramenskoye. Lưu ý 'Bykovo' ở Ramensky khác với nhiều địa danh 'Bykovo' trùng tên - ghim theo tên nhà thờ hoặc toạ độ.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text("Владимирская церковь", "Быково, Раменский район, Московская область", "Vladimir Church Bykovo (pseudo-Gothic)", "Bykovo, Moscow Oblast", 55.610115, 38.058122),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Владимирская церковь (Быково)", "url": "https://ru.wikipedia.org/wiki/Владимирская_церковь_(Быково)"},
        {"title": "Соборы.Ру — Быково. Церковь Владимирской иконы Божией Матери (toạ độ)", "url": "https://sobory.ru/article/?object=01404"},
        {"title": "Places.Moscow — Владимирская церковь (địa chỉ, toạ độ)", "url": "https://places.moscow/trip/vladimirskaya-cerkov"},
    ],
    "tags": ["church", "gothic-revival", "pseudo-gothic", "bazhenov", "estate", "bykovo", "ramensky", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PRIYUTINO_ESTATE = {
    "id": "leningrad-oblast-priyutino-estate",
    "slug": "priyutino-estate",
    "region": "leningrad-oblast",
    "region_name_vi": "Tỉnh Leningrad",
    "federal_district": "Vùng Tây Bắc",
    "name_vi": "Bảo tàng - Điền trang Priyutino (Muzey-usadba Priyutino)",
    "name_ru": "Музей-усадьба «Приютино»",
    "name_en": "Priyutino Estate Museum",
    "categories": ["museum", "park_garden"],
    "address_vi": "Đường Priyutinskaya, số 1, thành phố Vsevolozhsk, Tỉnh Leningrad; gần ga Berngardovka (tuyến Irinovka), bên bờ sông Lubya, tại km số 6 của «Con đường Sự sống», cách trung tâm Saint Petersburg khoảng 25 km về phía đông bắc.",
    "coordinates": {"lat": 60.012264, "lon": 30.580619},
    "rating": None,
    "presentation_short_vi": (
        "Priyutino là điền trang của Aleksey Olenin - giám đốc đầu tiên của Thư viện Công cộng và chủ tịch Viện "
        "Hàn lâm Nghệ thuật - một trong số ít điền trang nửa đầu thế kỉ 19 còn giữ được gần Saint Petersburg. "
        "Từng là nơi tụ họp của giới tinh hoa văn hoá Nga thời hoàng kim (Pushkin, Krylov, Bryullov, Glinka...), "
        "nay Priyutino là bảo tàng văn học - nghệ thuật giữa một công viên cổ bên hồ."
    ),
    "presentation_long_vi": (
        "Bên bờ sông Lubya, tại km số 6 của «Con đường Sự sống» thuộc thành phố Vsevolozhsk, ẩn mình một điền "
        "trang bằng gạch đỏ không trát: Priyutino - «chốn nương náu», nơi từng được gọi trìu mến là «tổ ấm của "
        "các thi nhân Nga». Năm 1795, Aleksey Nikolaevich Olenin - nhà khảo cổ, hoạ sĩ, giám đốc đầu tiên của "
        "Thư viện Công cộng Hoàng gia và chủ tịch Viện Hàn lâm Nghệ thuật - mua mảnh đất này bằng của hồi môn "
        "của vợ và cho dựng dần một quần thể điền trang theo kế hoạch thống nhất suốt hai thập niên. Đến những "
        "năm 1820, nơi đây đã có hai toà nhà chính, nhà kính, hàng chục công trình phụ và một công viên cảnh "
        "quan tuyệt đẹp bao quanh hồ nước - tất cả xây bằng gạch đỏ để mộc, một nét hiếm thấy. Điều làm nên "
        "linh hồn của Priyutino là bầu không khí tự do, ấm áp mà gia đình Olenin tạo ra: «nhóm Olenin» quy tụ "
        "gần như toàn bộ tinh hoa văn hoá Nga đương thời. Thi hào Ivan Krylov gắn bó suốt gần ba mươi năm và "
        "viết nhiều truyện ngụ ngôn tại đây; Nikolai Gnedich hoàn thành phần lớn bản dịch «Iliad» của Homer; "
        "và chàng trai trẻ Aleksandr Pushkin nhiều lần lui tới, đem lòng yêu Anna - con gái út của chủ nhà - "
        "rồi viết tặng nàng những vần thơ tình bất hủ, trong đó có «Tôi yêu em». Batyushkov, Zhukovsky, "
        "Vyazemsky, Griboyedov, Mickiewicz, anh em hoạ sĩ Bryullov, Kiprensky, nhạc sĩ Glinka... đều từng là "
        "khách của Priyutino. Sau khi gia đình Olenin bán điền trang (1841), nơi này đổi chủ nhiều lần và dần "
        "sa sút. Năm 1960 Priyutino được công nhận di tích văn hoá; từ 1974 mở bảo tàng văn học - nghệ thuật "
        "trong toà nhà chính, tái hiện nội thất và cuộc sống điền trang đầu thế kỉ 19. Ngày nay du khách tới "
        "Priyutino để thăm bảo tàng, dạo công viên cổ bên hồ và cảm nhận không gian thơ mộng gắn với thời "
        "hoàng kim của văn học Nga."
    ),
    "highlights_vi": [
        "Điền trang của A. N. Olenin - giám đốc đầu tiên Thư viện Công cộng, chủ tịch Viện Hàn lâm Nghệ thuật; một trong số ít điền trang nửa đầu thế kỉ 19 còn giữ được gần Saint Petersburg, xây bằng gạch đỏ để mộc.",
        "«Tổ ấm của các thi nhân Nga»: nơi Krylov viết truyện ngụ ngôn, Gnedich dịch «Iliad», và Pushkin đem lòng yêu Anna Olenina; từng đón Zhukovsky, Griboyedov, Bryullov, Glinka...",
        "Bảo tàng văn học - nghệ thuật (mở từ 1974) trong toà nhà chính, giữa công viên cảnh quan cổ bên hồ - điểm dạo bộ và tìm hiểu văn hoá điền trang Nga.",
    ],
    "practical": {
        "hours_vi": "Bảo tàng thường mở thứ Tư - Chủ nhật, khoảng 10:00-17:00 (ngừng bán vé/vào cửa trước giờ đóng ~1 giờ); nghỉ thứ Hai, thứ Ba và thường là thứ Sáu cuối tháng. Công viên có thể dạo tự do. Nên gọi/kiểm tra trước khi đến.",
        "ticket_vi": "Vé vào bảo tàng ở mức phải chăng (thường khoảng 100 rúp; ưu đãi cho học sinh, sinh viên, người hưu trí). Tham quan có hướng dẫn giúp hiểu rõ hơn lịch sử «nhóm Olenin».",
        "duration_vi": "Khoảng 1-2 giờ cho bảo tàng và dạo công viên bên hồ.",
        "best_time_vi": "Đẹp nhất vào cuối xuân đến mùa thu khi công viên xanh mát hoặc lá vàng; mùa hè cuối tuần đôi khi có các chương trình, lễ hội âm nhạc ngoài trời.",
        "tips_vi": "Từ Saint Petersburg đi tàu ngoại ô từ ga Finlyandsky tới ga Berngardovka rồi đi bộ/taxi, hoặc đi ô tô theo «Con đường Sự sống» (Doroga Zhizni). Mang giày đi bộ để dạo công viên; chú ý một số công trình điền trang vẫn đang chờ trùng tu.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text("Музей-усадьба «Приютино»", "Всеволожск, Ленинградская область", "Priyutino Estate Museum", "Vsevolozhsk, Leningrad Oblast", 60.012264, 30.580619),
    "official_site": "https://www.lenoblmus.ru/museums/literaturno-khudozhestvennyy-muzey-usadba-priyutino",
    "sources": [
        {"title": "Wikipedia (RU) — Приютино (усадьба)", "url": "https://ru.wikipedia.org/wiki/Приютино_(усадьба)"},
        {"title": "Autotravel.ru — Музей-усадьба «Приютино» (toạ độ geo.position)", "url": "https://autotravel.ru/otklik.php/2046"},
        {"title": "ГБУК ЛО «Музейное агентство» — Литературно-художественный музей-усадьба «Приютино»", "url": "https://www.lenoblmus.ru/museums/literaturno-khudozhestvennyy-muzey-usadba-priyutino"},
    ],
    "tags": ["museum", "estate", "literary", "olenin", "pushkin", "krylov", "park", "vsevolozhsk", "day-trip", "leningrad-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow-oblast.json": [NOVY_IERUSALIM_MUSEUM, BYKOVO_VLADIMIR_CHURCH],
    "leningrad-oblast.json": [PRIYUTINO_ESTATE],
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
