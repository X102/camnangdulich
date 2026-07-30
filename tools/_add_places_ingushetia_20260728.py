# -*- coding: utf-8 -*-
"""_add_places_ingushetia_20260728.py — VÙNG: Cộng hòa Ingushetia (Республика Ингушетия)
(lần chạy tự động 2026-07-28).

Bối cảnh: ingushetia.json hiện có 7 địa điểm. Bổ sung 19 địa điểm THẬT SỰ nổi tiếng/đặc
sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 26.

GHI CHÚ QUAN TRỌNG (số lượng < 30): Ingushetia có RẤT nhiều danh lam (hàng chục quần thể
tháp, đền, thác...). Tuy nhiên ngân sách WebSearch của phiên đã cạn giữa chừng và phần lớn
trang ru.wikipedia/openkavkaz trả về RỖNG qua web_fetch, nên chỉ xác minh được TOẠ ĐỘ TIN
CẬY cho 19 địa điểm mới. Theo nguyên tắc "KHÔNG bịa toạ độ", các địa điểm nổi tiếng khác mà
KHÔNG xác minh được toạ độ trong phiên này đã được BỎ QUA (không nhồi số bịa), gồm: Мавзолей
Борга-Каш (mộ cổ Hồi giáo, di tích cấp liên bang), Фуртоуг + thác Фуртоугский, Морч (+ đền
Морч-Сели), Дошхакле, Някист, Фалхан, Замок Дударова, Маго-Ерды, Альби-Ерды, Сеска-Солса-
Ерды, núi Цей-Лоам, núi Черехкорт (+ Коки), Ингушский музей ИЗО, Джейрах (làng thủ phủ quận).

Phân bố loại hình (19 bản ghi mới):
- fortress (11): Таргим, Хамхи, Ний, Пялинг, Цори, Салги, Хяни, Ляжги (làng tháp),
  Крепость Назрань, + (Мемориал «Девять башен» dùng monument).
- park_garden (4): Ляжгинский водопад, Столовая гора, Ассинское ущелье, Заповедник «Эрзи».
- church (2): Мят-Сели (thánh địa trên Столовая), Джума-мечеть Назрани (nhà thờ Hồi giáo).
- monument (2): Мемориал памяти и славы «Девять башен» (+museum), Аланские Ворота (Магас).
- museum (1): Ингушский музей краеведения им. Т. Мальсагова.
- square_street (1): Магас — проспект Идриса Зязикова / trung tâm thủ phủ.
(nhiều tháp dùng đồng thời fortress+monument)

TOẠ ĐỘ — xác minh chéo (ru.wikipedia infobox/geohack, openkavkaz.com toạ độ text, tripplanet
GPS, autotravel.ru DMS cho đối tượng đô thị Назрань, 2026-07-28). Phạm vi Ingushetia: lat
~42,7–43,6; lon ~44,6–45,3 — tất cả toạ độ nằm trong phạm vi, KHÔNG đảo lat/lon:
  Таргим 42.835125,44.942354 (ru.wiki 42°50′06″N 44°56′33″E); Хамхи 42.822222,44.926389
  (ru.wiki 42°49′20″N 44°55′35″E); Ний 42.830961,45.002156; Пялинг 42.822778,44.986389
  (ru.wiki 42°49′22″N 44°59′11″E); Цори 42.8077,45.0949; Салги 42.7979,44.8200; Хяни
  42.8038,44.8312 (openkavkaz); Ляжги 42.8073,44.7329; Ляжгинский водопад 42.7985,44.7195;
  Столовая гора/Мят-Лоам 42.8550,44.7192; Ассинское ущелье 42.807141,44.933356 (tripplanet
  GPS); Заповедник «Эрзи» 42.8024,44.7540 (điểm đại diện trong khu bảo tồn); Мят-Сели
  42.8533,44.7169 (đỉnh Столовая); Джума-мечеть Назрани 43.2311,44.7711 (autotravel N043
  13.865 E044 46.263); Крепость Назрань 43.2472,44.8102 (autotravel N043 14.834 E044 48.612);
  Мемориал «Девять башен» 43.196869,44.771359; Музей Мальсагова 43.2316,44.7682 (autotravel
  N043 13.894 E044 46.092, ул. Осканова 29); Аланские Ворота Магас 43.1802,44.7988; Магас
  центр 43.1667,44.8042 (проспект И. Зязикова).

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_ingushetia_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "ingushetia"
REGION_NAME_VI = "Cộng hòa Ingushetia"
FD = "Vùng Bắc Kavkaz"

# Ghi chú giấy phép vùng biên giới (dùng lại cho các điểm núi Dzheyrakh-Assa)
BORDER = ("Toàn vùng núi Dzheyrakh thuộc vùng biên giới giáp Gruzia: du khách (đặc biệt "
          "người nước ngoài) cần xin giấy phép vào vùng biên giới trước nhiều ngày.")


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


def mountain_practical(duration, extra_tip=""):
    tip = ("Đi xe gầm cao hoặc tour có hướng dẫn địa phương; mang giày leo núi, nước và đồ ấm; "
           "chuẩn bị giấy tờ tùy thân và giấy phép vùng biên giới. " + extra_tip).strip()
    return {
        "hours_vi": "Di tích/thiên nhiên ngoài trời, tham quan ban ngày quanh năm; không có giờ cố định.",
        "ticket_vi": "Không thu vé cố định cho khu ngoài trời. " + BORDER,
        "duration_vi": duration,
        "best_time_vi": "Cuối xuân đến đầu thu (tháng 5–9) khi đường núi khô ráo, tầm nhìn tốt.",
        "tips_vi": tip,
    }


RECORDS = []

# 1) Таргим ------------------------------------------------------------------------
RECORDS.append(rec(
    "targim-tower-complex",
    "Quần thể tháp cổ Targim (Tạc-ghim)",
    "Таргим",
    "Targim Tower Complex",
    ["fortress", "monument"],
    42.835125, 44.942354,
    "Hữu ngạn sông Assa, lòng chảo Targim (độ cao ~1.080 m), quận Dzheyrakh, Cộng hòa Ingushetia, Nga.",
    "Targim là một trong ba 'thành phố tháp' - pháo đài lớn nhất của vùng núi Ingushetia (cùng Egikal và Khamkhi), nằm bên hữu ngạn sông Assa. Quần thể gồm nhiều tháp chiến, tháp ở, đền miếu và khu mộ cổ, có dấu tích cư trú từ thiên niên kỷ II–I trước Công nguyên.",
    "Trải trên hữu ngạn sông Assa trong lòng chảo Targim ở độ cao khoảng 1.080 m, Targim là một trong ba quần thể làng - pháo đài hùng vĩ nhất của vùng 'Galgai' cổ (cùng với Egikal và Khamkhi). Theo truyền thuyết, ba pháo đài này do ba anh em - con của tổ phụ huyền thoại Alby-Yerda - dựng nên; người em út Targim vượt sông Assa lập làng ở bờ bên kia. Quần thể tập hợp một tập hợp di tích dày đặc: những ngôi nhà đá kiểu 'cyclopean' (xếp khối đá lớn) có niên đại thiên niên kỷ II–I trước Công nguyên, 4 tháp chiến, 4 tháp bán chiến, 16 tháp ở, cùng 19 khu mộ - nhà mồ, 2 lăng mộ và 5 đền - thánh địa. Những tháp chiến hình chóp cụt vươn cao khoảng 30 m, thu nhỏ dần về đỉnh, là kiệt tác kiến trúc đá của người Ingush. Không xa Targim còn có phế tích một nhà thờ Kitô giáo cổ, cho thấy vùng đất đã có người sinh sống từ rất lâu trước khi các tháp - pháo đài mọc lên. Targim là quê tổ của hàng chục dòng họ (taip) Ingush và ngày nay nằm trong Khu bảo tồn lịch sử - kiến trúc và tự nhiên Dzheyrakh-Assa, được nhà nước bảo vệ.",
    [
        "Một trong ba quần thể tháp - pháo đài lớn nhất vùng núi Ingushetia, bên hữu ngạn sông Assa.",
        "Gồm nhà đá cyclopean niên đại thiên niên kỷ II–I TCN, 4 tháp chiến, 16 tháp ở, lăng mộ và đền miếu.",
        "Gắn với truyền thuyết ba anh em con tổ phụ Alby-Yerda, quê tổ của nhiều dòng họ Ingush.",
    ],
    mountain_practical("Khoảng 1,5–2 giờ; trọn ngày nếu kết hợp Egikal, Khamkhi và nhà thờ Tkhaba-Yerdy.",
                       "Kết hợp thăm lòng chảo Targim và hẻm Assa lân cận."),
    [
        {"title": "Wikipedia (RU) — Таргим", "url": "https://ru.wikipedia.org/wiki/Таргим"},
        {"title": "TripPlanet — Достопримечательности Ингушетии", "url": "https://tripplanet.ru/dostoprimechatelnosti-ingushetii/"},
    ],
    ["towers", "medieval", "fortress", "cyclopean", "assa-gorge", "vainakh", "north-caucasus"],
    maps_text("Башенный комплекс Таргим", "Джейрахский район", "Targim Tower Complex", "Ingushetia", 42.835125, 44.942354),
))

# 2) Хамхи --------------------------------------------------------------------------
RECORDS.append(rec(
    "khamkhi-tower-complex",
    "Quần thể tháp cổ Khamkhi (Kham-khi)",
    "Хамхи",
    "Khamkhi Tower Complex",
    ["fortress", "monument"],
    42.822222, 44.926389,
    "Tả ngạn sông Assa, khu lịch sử 'Kkyakhale' (độ cao ~1.230 m), quận Dzheyrakh, Cộng hòa Ingushetia, Nga.",
    "Khamkhi là một trong ba làng - pháo đài lớn nhất của vùng núi Ingushetia, nằm bên tả ngạn sông Assa ở trung tâm lòng chảo Targim. Quần thể gồm nhà đá cyclopean cổ, tháp chiến, tháp ở và các khu nhà mồ, là quê tổ của nhiều dòng họ Ingush.",
    "Nằm bên tả ngạn sông Assa, đối diện Targim ở trung tâm lòng chảo, Khamkhi là một trong ba 'thành phố tháp' cổ lớn nhất của vùng lịch sử 'Kkyakhale' (tiếng Ingush nghĩa gần với 'Ba thành'). Ở độ cao khoảng 1.230 m, quần thể quy tụ những ngôi nhà đá kiểu megalith - cyclopean có niên đại thiên niên kỷ II–I trước Công nguyên, 4 tháp chiến, 4 tháp bán chiến, 16 tháp ở nhiều tầng cùng 10 khu mộ - nhà mồ cổ. Đây là quê tổ của hàng loạt dòng họ (taip) Ingush như Khamkhoev, Izmailov, Bekbuzarov, Martazanov... Một số học giả từng gắn địa danh này với tộc danh 'hamekiti' mà nhà địa lý cổ đại Strabon nhắc tới, dù giả thuyết còn tranh luận. Toàn bộ quần thể và khu định cư nằm trong Khu bảo tồn lịch sử - kiến trúc và tự nhiên Dzheyrakh-Assa, được nhà nước bảo vệ, và là một mắt xích quan trọng để hiểu về xã hội thị tộc và kiến trúc tháp Vainakh thời trung cổ.",
    [
        "Một trong ba làng - pháo đài lớn nhất vùng núi, ở trung tâm lòng chảo Targim bên tả ngạn Assa.",
        "Gồm nhà đá cyclopean, 4 tháp chiến, 16 tháp ở và 10 khu nhà mồ cổ.",
        "Quê tổ của nhiều dòng họ Ingush; nằm trong Khu bảo tồn Dzheyrakh-Assa.",
    ],
    mountain_practical("Khoảng 1–1,5 giờ; nên kết hợp Targim và Egikal.",
                       "Kết hợp thăm Targim đối diện và nhà thờ Tkhaba-Yerdy."),
    [
        {"title": "Wikipedia (RU) — Хамхи", "url": "https://ru.wikipedia.org/wiki/Хамхи"},
        {"title": "Wikipedia (RU) — Ингушские башни", "url": "https://ru.wikipedia.org/wiki/Ингушские_башни"},
    ],
    ["towers", "medieval", "fortress", "cyclopean", "assa-gorge", "vainakh"],
    maps_text("Башенный комплекс Хамхи", "Джейрахский район", "Khamkhi Tower Complex", "Ingushetia", 42.822222, 44.926389),
))

# 3) Ний ----------------------------------------------------------------------------
RECORDS.append(rec(
    "nyi-tower-complex",
    "Quần thể tháp cổ Nyi (Nì)",
    "Ний",
    "Nyi Tower Complex",
    ["fortress", "monument"],
    42.830961, 45.002156,
    "Vùng núi dưới rặng Tsorey-Loam (độ cao ~1.700 m), quận Dzheyrakh, Cộng hòa Ingushetia, Nga.",
    "Nyi là một trong những quần thể tháp trung cổ được bảo tồn tốt nhất của Ingushetia, nằm trên vùng núi cao dưới rặng Tsorey-Loam. Quần thể còn giữ được 4 tháp chiến, nhiều tháp ở, đền cột và các khu nhà mồ, giữa khung cảnh hoang sơ hùng vĩ.",
    "Nằm ở độ cao khoảng 1.700 m dưới rặng núi Tsorey-Loam thuộc quận Dzheyrakh, Nyi là một trong những làng tháp còn nguyên vẹn nhất của vùng núi Ingushetia. Dù nay đã hoang vắng, quần thể vẫn bảo tồn được 4 tháp chiến, 1 tháp bán chiến và 13 tháp ở (phần lớn hư hại một phần), cùng 2 đền - thánh địa dạng cột và 14 khu mộ - nhà mồ. Những tòa tháp chiến cao vút với mái chóp bậc thang tiêu biểu cho đỉnh cao kiến trúc phòng thủ của người Vainakh, mọc lên giữa một địa thế biệt lập, ít dấu chân người. Chính sự tách biệt và khung cảnh núi non nguyên sơ khiến Nyi trở thành điểm đến hấp dẫn với những ai muốn cảm nhận trọn vẹn không khí trầm mặc của 'xứ sở tháp cổ'. Quần thể thuộc Khu bảo tồn lịch sử - kiến trúc và tự nhiên Dzheyrakh-Assa và được nhà nước bảo vệ.",
    [
        "Một trong những quần thể tháp còn nguyên vẹn nhất Ingushetia, dưới rặng Tsorey-Loam.",
        "Còn 4 tháp chiến, 13 tháp ở, 2 đền cột và 14 khu nhà mồ cổ.",
        "Địa thế biệt lập, hoang sơ, cảnh núi non hùng vĩ, thuộc Khu bảo tồn Dzheyrakh-Assa.",
    ],
    mountain_practical("Khoảng 1–1,5 giờ; đường vào khá xa và hiểm trở.",
                       "Cần hướng dẫn viên rành đường; kết hợp Pyaling và Tsori lân cận."),
    [
        {"title": "Wikipedia (RU) — Ний", "url": "https://ru.wikipedia.org/wiki/Ний"},
        {"title": "TripPlanet — Достопримечательности Ингушетии", "url": "https://tripplanet.ru/dostoprimechatelnosti-ingushetii/"},
    ],
    ["towers", "medieval", "fortress", "mountain", "vainakh", "heritage"],
    maps_text("Башенный комплекс Ний", "Джейрахский район", "Nyi Tower Complex", "Ingushetia", 42.830961, 45.002156),
))

# 4) Пялинг -------------------------------------------------------------------------
RECORDS.append(rec(
    "pyaling-tower-complex",
    "Quần thể tháp cổ Pyaling (Pi-a-ling)",
    "Пялинг",
    "Pyaling Tower Complex",
    ["fortress", "monument"],
    42.822778, 44.986389,
    "Vùng núi dưới rặng Tsorey-Loam, quận Dzheyrakh, Cộng hòa Ingushetia, Nga.",
    "Pyaling là một thành phố - làng tháp trung cổ ở quận Dzheyrakh, quê tổ của dòng họ Polonkoy. Quần thể gồm 5 tháp chiến, hơn 20 tháp ở, cùng nhiều khu nhà mồ, lăng mộ và đền - thánh địa.",
    "Pyaling là một trong những làng tháp cổ đặc sắc của vùng núi Dzheyrakh, được xem là quê tổ của dòng họ (taip) Polonkoy - dòng họ gắn với nghệ nhân Murad Polonkoev, tác giả của memorial 'Chín Tháp' ở Nazran. Quần thể kiến trúc Pyaling khá đồ sộ với 5 tháp chiến và 21 tháp ở nhiều tầng, bao quanh là 13 khu mộ - nhà mồ, 1 lăng mộ và 1 đền - thánh địa. Các tòa tháp mọc trên sườn núi dưới rặng Tsorey-Loam thiêng, thường được du khách ghé thăm cùng cụm tháp Nyi lân cận trong một hành trình khám phá thung lũng phía đông của vùng núi Ingushetia. Cũng như các làng tháp khác, Pyaling nằm trong Khu bảo tồn lịch sử - kiến trúc và tự nhiên Dzheyrakh-Assa và được nhà nước bảo vệ như một di sản văn hóa - lịch sử.",
    [
        "Thành phố - làng tháp trung cổ, quê tổ của dòng họ Polonkoy.",
        "Gồm 5 tháp chiến, 21 tháp ở cùng nhiều khu nhà mồ, lăng mộ và đền - thánh địa.",
        "Nằm dưới rặng Tsorey-Loam thiêng, thường thăm cùng cụm tháp Nyi.",
    ],
    mountain_practical("Khoảng 1–1,5 giờ; thường kết hợp với Nyi.",
                       "Đường núi hiểm trở, nên đi cùng hướng dẫn viên."),
    [
        {"title": "Wikipedia (RU) — Пялинг", "url": "https://ru.wikipedia.org/wiki/Пялинг"},
        {"title": "Wikipedia (RU) — Ингушские башни", "url": "https://ru.wikipedia.org/wiki/Ингушские_башни"},
    ],
    ["towers", "medieval", "fortress", "mountain", "vainakh", "heritage"],
    maps_text("Башенный комплекс Пялинг", "Джейрахский район", "Pyaling Tower Complex", "Ingushetia", 42.822778, 44.986389),
))

# 5) Цори ---------------------------------------------------------------------------
RECORDS.append(rec(
    "tsori-tower-complex",
    "Quần thể tháp cổ Tsori (Xô-ri)",
    "Цори",
    "Tsori Tower Complex",
    ["fortress", "monument"],
    42.8077, 45.0949,
    "Thung lũng sông Gulojhi, quận Dzheyrakh, Cộng hòa Ingushetia, Nga.",
    "Tsori là một quần thể tháp lớn thời trung cổ (thế kỷ 12–17) từng là trung tâm quy tụ các cộng đồng thị tộc trong vùng. Điểm đặc sắc là các bức tường tháp khắc đầy petroglyph - hoa văn và biểu tượng mặt trời.",
    "Từng là hạt nhân chính trị quy tụ các cộng đồng - thị tộc (taip) rải rác quanh vùng, Tsori là một trong những quần thể tháp lớn và đặc sắc của Ingushetia, được cho là xây dựng vào khoảng thế kỷ 12–17. Quần thể gồm 3 tháp chiến và khoảng 20 tháp ở, cùng các khu mộ và công trình phụ trợ, xưa được bao quanh bởi tường thành có cổng mà nay chỉ còn phần móng. Nét độc đáo của Tsori nằm ở lớp trang trí: nhiều tòa tháp có kích thước và hình dáng tương tự nhau nhưng trên tường lại khắc các petroglyph - hình chạm đá thể hiện hoa văn và biểu tượng mặt trời (solar). Trên một ngọn đồi gần đó còn có thêm một cụm ba tháp nhỏ với tầm nhìn tuyệt đẹp, dù lối lên chưa có đường mòn du lịch. Tsori nằm ở phần phía đông của vùng núi, dọc thung lũng sông Gulojhi, và thuộc hệ thống di tích tháp cổ được bảo vệ của Ingushetia.",
    [
        "Quần thể tháp lớn (thế kỷ 12–17), từng là trung tâm quy tụ các thị tộc trong vùng.",
        "Gồm 3 tháp chiến và ~20 tháp ở, có tường thành và cổng (nay còn móng).",
        "Đặc sắc với các petroglyph khắc hoa văn và biểu tượng mặt trời trên tường tháp.",
    ],
    mountain_practical("Khoảng 1–1,5 giờ.",
                       "Đường xa; cụm ba tháp trên đồi gần đó chưa có đường mòn, cần thận trọng."),
    [
        {"title": "TripPlanet — Достопримечательности Ингушетии", "url": "https://tripplanet.ru/dostoprimechatelnosti-ingushetii/"},
        {"title": "Bolshaya Strana — Достопримечательности Ингушетии", "url": "https://bolshayastrana.com/blog/dostoprimechatelnosti-ingushetii-87"},
    ],
    ["towers", "medieval", "fortress", "petroglyphs", "mountain", "vainakh"],
    maps_text("Башенный комплекс Цори", "Джейрахский район", "Tsori Tower Complex", "Ingushetia", 42.8077, 45.0949),
))

# 6) Салги --------------------------------------------------------------------------
RECORDS.append(rec(
    "salgi-tower-complex",
    "Quần thể tháp cổ Salgi (Xan-ghi)",
    "Салги",
    "Salgi Tower Complex",
    ["fortress", "monument"],
    42.7979, 44.8200,
    "Bên bờ sông Chulkhi, hẻm núi Chulkhoi (Salgi), quận Dzheyrakh, Cộng hòa Ingushetia, Nga.",
    "Salgi là làng - pháo đài nổi tiếng nhất trong hẻm núi Chulkhoi (còn gọi hẻm Salgi), bên bờ sông Chulkhi. Quần thể gồm hai tháp chiến, khoảng chục tháp ở cùng khu nhà mồ, giữa một hẻm núi nhỏ nhưng dày đặc di tích.",
    "Hẻm núi Chulkhoi (còn gọi là hẻm Salgi) tuy nhỏ nhưng lại quy tụ nhiều cụm tháp - pháo đài, trong đó nổi tiếng nhất chính là làng tháp Salgi bên bờ sông Chulkhi. Quần thể gồm hai tháp chiến vươn cao, khoảng mười tháp ở cùng nhiều công trình phụ trợ và tường phòng thủ; phần lớn công trình nay đã hư hại, còn ở phía bắc làng vẫn giữ được một khu nhà mồ - nghĩa địa cổ. Nằm giữa khung cảnh núi non nguyên sơ, Salgi là điểm dừng lý tưởng cho những ai muốn khám phá một hẻm núi ít du khách nhưng đậm đặc dấu tích kiến trúc Vainakh. Quần thể thuộc hệ thống di tích tháp cổ của Ingushetia trong vùng Dzheyrakh-Assa và được nhà nước bảo vệ.",
    [
        "Làng - pháo đài nổi tiếng nhất hẻm núi Chulkhoi (Salgi), bên bờ sông Chulkhi.",
        "Gồm hai tháp chiến, khoảng chục tháp ở, tường phòng thủ và khu nhà mồ cổ ở phía bắc.",
        "Hẻm núi nhỏ nhưng dày đặc di tích, cảnh quan nguyên sơ, ít du khách.",
    ],
    mountain_practical("Khoảng 1 giờ.",
                       "Kết hợp thăm cụm tháp Hyani cùng hẻm Chulkhoi."),
    [
        {"title": "TripPlanet — Достопримечательности Ингушетии", "url": "https://tripplanet.ru/dostoprimechatelnosti-ingushetii/"},
        {"title": "Bolshaya Strana — Достопримечательности Ингушетии", "url": "https://bolshayastrana.com/blog/dostoprimechatelnosti-ingushetii-87"},
    ],
    ["towers", "medieval", "fortress", "chulkhoi-gorge", "mountain", "vainakh"],
    maps_text("Башенный комплекс Салги", "Джейрахский район", "Salgi Tower Complex", "Ingushetia", 42.7979, 44.8200),
))

# 7) Хяни ---------------------------------------------------------------------------
RECORDS.append(rec(
    "hyani-tower-complex",
    "Quần thể tháp cổ Hyani (Khi-a-ni)",
    "Хяни",
    "Hyani Tower Complex",
    ["fortress", "monument"],
    42.8038, 44.8312,
    "Hẻm núi Chulkhoi, quận Dzheyrakh, Cộng hòa Ingushetia, Nga.",
    "Hyani là quần thể tháp cổ trong hẻm núi Chulkhoi, quê hương của Khing Khaniev - một trong những thợ cả xây tháp lừng danh nhất thời trung cổ. Nơi đây còn giữ những tháp chiến mái chóp bậc thang giữa cảnh núi non tuyệt đẹp.",
    "Hyani (Khyani) là một làng tháp cổ trong hẻm núi Chulkhoi, nổi tiếng gắn với tên tuổi thợ cả Khing Khaniev - một trong những bậc thầy xây tháp (ингуш. тӏоговзанча) được kính trọng nhất của vùng núi Ingushetia thời trung cổ. Truyền thống ghi nhận những nghệ nhân như Yand làng Erzi, Khing làng Hyani hay Baki Barkhanoev là các 'kiến trúc sư' của kiệt tác tháp Vainakh - những công trình đá khan cao vút, mái chóp bậc thang, xây dựng đòi hỏi kỹ năng cha truyền con nối. Quần thể Hyani bảo tồn các tháp chiến và tháp ở tiêu biểu, nằm giữa khung cảnh núi non tráng lệ của hẻm Chulkhoi. Đây là điểm đến giàu chiều sâu cho những ai quan tâm tới nghệ thuật xây tháp và các dòng nghệ nhân - thợ cả của người Ingush. Di tích thuộc vùng bảo tồn Dzheyrakh-Assa.",
    [
        "Làng tháp cổ trong hẻm Chulkhoi, quê hương thợ cả xây tháp lừng danh Khing Khaniev.",
        "Gắn với truyền thống nghệ nhân - thợ cả xây tháp Vainakh (Yand, Khing, Baki Barkhanoev...).",
        "Tháp chiến mái chóp bậc thang giữa cảnh núi non tuyệt đẹp của hẻm Chulkhoi.",
    ],
    mountain_practical("Khoảng 1 giờ; thường thăm cùng Salgi.",
                       "Kết hợp khám phá cả hẻm Chulkhoi."),
    [
        {"title": "Wikipedia (RU) — Ингушские башни", "url": "https://ru.wikipedia.org/wiki/Ингушские_башни"},
        {"title": "OpenKavkaz — Хяни", "url": "https://openkavkaz.com/ing/hyani/"},
    ],
    ["towers", "medieval", "fortress", "master-builder", "chulkhoi-gorge", "vainakh"],
    maps_text("Башенный комплекс Хяни", "Джейрахский район", "Hyani Tower Complex", "Ingushetia", 42.8038, 44.8312),
))

# 8) Ляжги (làng tháp) --------------------------------------------------------------
RECORDS.append(rec(
    "lyazhgi-village-towers",
    "Làng tháp cổ Lyazhgi (Li-át-ghi)",
    "Ляжги",
    "Lyazhgi Village Towers",
    ["fortress"],
    42.8073, 44.7329,
    "Hữu ngạn sông Armkhi, hẻm núi Dzheyrakh, quận Dzheyrakh, Cộng hòa Ingushetia, Nga.",
    "Lyazhgi là làng tháp cổ bên hữu ngạn sông Armkhi, nổi tiếng với các tháp chiến do thợ cả Khano Khing xây dựng - được gia cố thêm vòm đá đặc biệt để tăng độ vững chắc. Làng cũng là cửa ngõ tới thác Lyazhgi.",
    "Lyazhgi là một làng tháp cổ nằm bên hữu ngạn sông Armkhi trong hẻm núi Dzheyrakh. Điểm đặc biệt của cụm tháp nơi đây là kỹ thuật xây dựng: theo ghi chép, tháp chiến Lyazhgi do thợ cả Khano Khing dựng, được gia cố thêm một vòm đá giữa tầng 4 và tầng 5 nhằm tăng độ bền vững và khả năng chịu lực - một giải pháp tinh xảo hiếm thấy. Ngoài giá trị kiến trúc, Lyazhgi còn là cửa ngõ dẫn tới thác Lyazhgi (Ляжгинский водопад), thác lớn nhất vùng núi Ingushetia, qua một tuyến đi bộ sinh thái xuyên rừng. Làng nằm trong Khu bảo tồn thiên nhiên Erzi và vùng lịch sử - kiến trúc Dzheyrakh-Assa, thuận tiện để kết hợp tham quan cùng khu nghỉ dưỡng Armkhi gần đó.",
    [
        "Làng tháp cổ bên hữu ngạn sông Armkhi trong hẻm núi Dzheyrakh.",
        "Tháp chiến do thợ cả Khano Khing xây, gia cố vòm đá đặc biệt giữa tầng 4 và 5.",
        "Cửa ngõ tới thác Lyazhgi - thác lớn nhất vùng núi Ingushetia.",
    ],
    mountain_practical("Khoảng 1 giờ tham quan làng; thêm 1–2 giờ nếu đi bộ tới thác.",
                       "Kết hợp trekking tới thác Lyazhgi và nghỉ tại Armkhi."),
    [
        {"title": "Wikipedia (RU) — Ингушские башни", "url": "https://ru.wikipedia.org/wiki/Ингушские_башни"},
        {"title": "TripPlanet — Достопримечательности Ингушетии", "url": "https://tripplanet.ru/dostoprimechatelnosti-ingushetii/"},
    ],
    ["towers", "medieval", "fortress", "armkhi", "dzheyrakh-gorge", "vainakh"],
    maps_text("Ляжги", "Джейрахский район", "Lyazhgi Village", "Ingushetia", 42.8073, 44.7329),
))

# 9) Ляжгинский водопад -------------------------------------------------------------
RECORDS.append(rec(
    "lyazhgi-waterfall",
    "Thác Lyazhgi (Ljiat-ghinsky)",
    "Ляжгинский водопад",
    "Lyazhgi Waterfall",
    ["park_garden"],
    42.7985, 44.7195,
    "Suối Lyazhgi (chi lưu tả ngạn sông Armkhi), hẻm núi Dzheyrakh (độ cao ~1.300 m), quận Dzheyrakh, Cộng hòa Ingushetia, Nga.",
    "Thác Lyazhgi được xem là thác nước lớn nhất và đẹp nhất vùng núi Ingushetia, cao khoảng 18–20 m và đổ qua nhiều bậc. Nằm trong Khu bảo tồn thiên nhiên Erzi, thác được nối bằng một tuyến đi bộ sinh thái xuyên rừng.",
    "Nằm ở độ cao khoảng 1.300 m trong hẻm núi Dzheyrakh, thác Lyazhgi được hình thành từ dòng suối Lyazhgi - một chi lưu tả ngạn của sông Armkhi, được nuôi dưỡng bởi băng tuyết trên núi. Với chiều cao khoảng 18–20 m và cấu trúc nhiều bậc thác, đây được coi là thác nước lớn nhất của vùng núi Ingushetia. Làn nước xanh trong, mát lạnh (có cả cá hồi suối) đổ giữa khung cảnh rừng thông, bách xù và thanh lương trà tạo nên một điểm dừng chân thơ mộng, đặc biệt vào cuối xuân - đầu hè khi thác nhiều nước và cây cối xanh tươi nhất. Từ chân hẻm, một tuyến đường mòn sinh thái có biển chỉ dẫn dẫn du khách tới thác, băng qua những cánh rừng đẹp của Khu bảo tồn thiên nhiên Erzi. Đây là một trong những điểm tham quan được yêu thích nhất của khu bảo tồn, phù hợp cho cả du khách lẫn người dân địa phương tới dã ngoại.",
    [
        "Thác nước lớn nhất vùng núi Ingushetia, cao khoảng 18–20 m, nhiều bậc thác.",
        "Nước xanh trong nuôi bởi băng tuyết, có cá hồi suối, giữa rừng thông - bách xù.",
        "Nằm trong Khu bảo tồn thiên nhiên Erzi, có đường mòn sinh thái với biển chỉ dẫn.",
    ],
    {
        "hours_vi": "Thiên nhiên ngoài trời, tham quan ban ngày quanh năm.",
        "ticket_vi": "Không thu vé riêng cho thác. " + BORDER,
        "duration_vi": "Khoảng 2–3 giờ cả đi bộ khứ hồi từ điểm gửi xe.",
        "best_time_vi": "Cuối xuân đến đầu hè (tháng 5–6) khi thác nhiều nước nhất; mùa hè cũng đẹp.",
        "tips_vi": "Đi giày chống trượt, mang nước; theo biển chỉ dẫn trên đường mòn; kết hợp làng tháp Lyazhgi và khu nghỉ Armkhi. " + BORDER,
    },
    [
        {"title": "TripPlanet — Достопримечательности Ингушетии", "url": "https://tripplanet.ru/dostoprimechatelnosti-ingushetii/"},
        {"title": "Bolshaya Strana — Достопримечательности Ингушетии", "url": "https://bolshayastrana.com/blog/dostoprimechatelnosti-ingushetii-87"},
    ],
    ["waterfall", "nature", "erzi-reserve", "dzheyrakh-gorge", "hiking", "north-caucasus"],
    maps_text("Ляжгинский водопад", "Джейрахский район", "Lyazhgi Waterfall", "Ingushetia", 42.7985, 44.7195),
))

# 10) Столовая гора -----------------------------------------------------------------
RECORDS.append(rec(
    "stolovaya-table-mountain",
    "Núi Bàn (Stolovaya - Myat-Loam)",
    "Столовая гора (Мят-Лоам)",
    "Table Mountain (Stolovaya)",
    ["park_garden", "monument"],
    42.8550, 44.7192,
    "Ranh giới quận Dzheyrakh (Ingushetia) và quận Prigorodny (Bắc Ossetia), đỉnh cao ~3.003 m, Nga.",
    "Núi Bàn (Stolovaya, tiếng Ingush là Myat-Loam) cao khoảng 3.003 m, là biểu tượng thiêng liêng của Ingushetia - hình núi xuất hiện trên quốc huy Cộng hòa Ingushetia và huy hiệu thành phố Vladikavkaz. Đỉnh phẳng như mặt bàn, có các đền - thánh địa cổ.",
    "Sừng sững ngay ranh giới giữa quận Dzheyrakh của Ingushetia và quận Prigorodny của Bắc Ossetia, núi Bàn - tiếng Nga là Stolovaya, tiếng Ingush là Myat-Loam ('núi mẹ') - cao khoảng 3.003 m và mang ý nghĩa biểu tượng đặc biệt. Với đỉnh gần như phẳng như mặt bàn, ngọn núi được đặt tên theo chính hình dáng ấy và từ lâu được người dân tôn kính như một nơi thiêng, nơi trú ngụ của các vị thần theo tín ngưỡng cổ. Hình núi Bàn hiện diện trên quốc huy Cộng hòa Ingushetia và cả huy hiệu thành phố Vladikavkaz. Trên và quanh đỉnh còn lưu giữ các đền - thánh địa cổ thuộc nhiều thời kỳ khác nhau, trong đó nổi bật là thánh địa Myat-Seli. Đây cũng là điểm leo núi được yêu thích: lối lên từ phía Ingushetia tương đối dễ, mất vài giờ đi bộ, mở ra tầm nhìn ngoạn mục xuống thung lũng Armkhi và các dãy Kavkaz; một số vách đá còn được dân chơi nhảy dù (base jumping) ưa chuộng.",
    [
        "Đỉnh núi ~3.003 m, biểu tượng của Ingushetia, có trên quốc huy nước cộng hòa và huy hiệu Vladikavkaz.",
        "Đỉnh phẳng như mặt bàn; nơi thiêng với các đền - thánh địa cổ (có thánh địa Myat-Seli).",
        "Điểm leo núi được ưa thích, lối lên từ phía Ingushetia tương đối dễ, tầm nhìn hùng vĩ.",
    ],
    mountain_practical("Trọn ngày cho hành trình leo lên đỉnh và xuống núi.",
                       "Cần thể lực tốt, khởi hành sớm, theo dõi thời tiết; nên có hướng dẫn viên."),
    [
        {"title": "Wikipedia (RU) — Столовая (гора, Кавказ)", "url": "https://ru.wikipedia.org/wiki/Столовая_(гора,_Кавказ)"},
        {"title": "TripPlanet — Достопримечательности Ингушетии", "url": "https://tripplanet.ru/dostoprimechatelnosti-ingushetii/"},
    ],
    ["mountain", "nature", "sacred", "hiking", "symbol", "north-caucasus"],
    maps_text("Столовая гора Мят-Лоам", "Джейрахский район", "Table Mountain Stolovaya", "Ingushetia", 42.8550, 44.7192),
))

# 11) Ассинское ущелье --------------------------------------------------------------
RECORDS.append(rec(
    "assa-gorge",
    "Hẻm núi Assa (Át-xa)",
    "Ассинское ущелье",
    "Assa Gorge",
    ["park_garden"],
    42.807141, 44.933356,
    "Thung lũng sông Assa quanh lòng chảo Targim, quận Dzheyrakh, Cộng hòa Ingushetia, Nga.",
    "Hẻm núi Assa là một khe núi hẹp với vách đá dựng đứng, nơi dòng sông Assa xuyên qua rặng Skalisty. Thung lũng tập trung nhiều di tích nổi tiếng như nhà thờ Tkhaba-Yerdy và các làng tháp Targim, Egikal, Khamkhi.",
    "Hẻm núi Assa là một trong những khe núi đẹp và giàu di tích bậc nhất của vùng núi Ingushetia, nơi dòng sông Assa (dài khoảng 133 km, chảy qua cả Ingushetia, Gruzia và Chechnya) cắt xuyên rặng núi Skalisty tạo thành những vách đá dựng đứng phủ cây rừng. Con đường chạy dọc hẻm khi thì men hữu ngạn, khi thì tả ngạn sông, mở ra một hành trình ngoạn mục dài không dưới 7 km. Chính trong thung lũng này và lòng chảo Targim mà tập trung dày đặc các di tích trứ danh: nhà thờ Kitô giáo cổ Tkhaba-Yerdy, các làng - pháo đài Targim, Egikal, Khamkhi cùng nhiều đền miếu, khu nhà mồ. Toàn bộ khu vực nằm trong Khu bảo tồn lịch sử - kiến trúc và tự nhiên Dzheyrakh-Assa, nơi bảo tồn cảnh quan thiên nhiên và di sản văn hóa, đồng thời phát triển du lịch sinh thái. Hẻm Assa vì thế vừa là một tuyến cảnh quan tuyệt đẹp, vừa là 'trục di sản' của xứ sở tháp cổ Ingushetia.",
    [
        "Khe núi hẹp với vách đá dựng đứng, nơi sông Assa xuyên qua rặng Skalisty.",
        "Tuyến cảnh quan dài hơn 7 km, đường chạy men hai bờ sông.",
        "Trục di sản: nhà thờ Tkhaba-Yerdy, làng tháp Targim, Egikal, Khamkhi.",
    ],
    mountain_practical("Nửa ngày đến trọn ngày tùy số điểm ghé thăm dọc hẻm.",
                       "Kết hợp thăm Tkhaba-Yerdy, Targim và Egikal; xe gầm cao cho đoạn đường mòn."),
    [
        {"title": "TripPlanet — Достопримечательности Ингушетии (GPS 42.807141, 44.933356)", "url": "https://tripplanet.ru/dostoprimechatelnosti-ingushetii/"},
        {"title": "Bolshaya Strana — Заповедник Эрзи", "url": "https://bolshayastrana.com/dostoprimechatelnosti/ingushetiya/zapovednik-ehrzi-225"},
    ],
    ["gorge", "nature", "assa-river", "landscape", "heritage", "dzheyrakh-assa"],
    maps_text("Ассинское ущелье", "Джейрахский район", "Assa Gorge", "Ingushetia", 42.807141, 44.933356),
))

# 12) Заповедник «Эрзи» -------------------------------------------------------------
RECORDS.append(rec(
    "erzi-nature-reserve",
    "Khu bảo tồn thiên nhiên Erzi (Ơ-di)",
    "Государственный природный заповедник «Эрзи»",
    "Erzi Nature Reserve",
    ["park_garden"],
    42.8024, 44.7540,
    "Vùng núi các quận Dzheyrakh và Sunzha (~35.300 ha), Cộng hòa Ingushetia, Nga.",
    "Khu bảo tồn thiên nhiên quốc gia Erzi (thành lập năm 2000, rộng ~35.300 ha) là khu bảo tồn liên bang thứ 100 của nước Nga. Nơi đây gìn giữ hệ sinh thái núi Kavkaz cùng hơn 50 quần thể tháp trung cổ và thác Lyazhgi trứ danh.",
    "Được thành lập tháng 12 năm 2000 với tư cách khu bảo tồn (zapovednik) thứ 100 của nước Nga, Erzi (tiếng Ingush nghĩa là 'đại bàng') trải rộng khoảng 35.300 ha trên vùng núi hai quận Dzheyrakh và Sunzha. Ranh giới khu bảo tồn phía bắc - tây giáp Bắc Ossetia, phía đông giáp Chechnya, phía nam vươn tới rặng Tsorey-Loam; khoảng một phần ba diện tích là rừng sồi, dẻ gai xen phong, chuyển dần lên các đồng cỏ núi cao và cả những khối băng trên đỉnh vượt 3.500–4.000 m. Erzi là nơi trú ngụ của nhiều loài quý hiếm - dê núi tur, sơn dương, đại bàng vàng, và gần đây ghi nhận cả báo Kavkaz (báo tiền Á) được tái thả; có tới khoảng 180 loài thực vật quý. Đặc biệt, khu bảo tồn còn là 'bảo tàng ngoài trời': trong ranh giới của nó có hơn 50 tháp và pháo đài trung cổ, các đền - thánh địa cổ, cùng những điểm thiên nhiên nổi tiếng như thác Lyazhgi, thác Furtoug và thung lũng sông Gulojhi. Chính tại một tòa tháp trong vùng, người ta đã tìm thấy tượng đồng 'Đại bàng Suleiman' (thế kỷ 8) - biểu tượng của Ingushetia, nay lưu giữ tại Bảo tàng Hermitage.",
    [
        "Khu bảo tồn liên bang thứ 100 của Nga (thành lập 2000), rộng ~35.300 ha.",
        "Hệ sinh thái núi Kavkaz đa dạng: ~180 loài thực vật quý, dê tur, sơn dương, đại bàng, báo Kavkaz.",
        "Chứa hơn 50 quần thể tháp trung cổ, thác Lyazhgi, thác Furtoug; nơi tìm thấy 'Đại bàng Suleiman'.",
    ],
    mountain_practical("Từ nửa ngày (một điểm) đến nhiều ngày nếu đi các tuyến khác nhau.",
                       "Có khoảng 11 tuyến du lịch; nên đi tour có hướng dẫn và xin phép trước."),
    [
        {"title": "Bolshaya Strana — Заповедник Эрзи", "url": "https://bolshayastrana.com/dostoprimechatelnosti/ingushetiya/zapovednik-ehrzi-225"},
        {"title": "TripPlanet — Достопримечательности Ингушетии", "url": "https://tripplanet.ru/dostoprimechatelnosti-ingushetii/"},
    ],
    ["nature-reserve", "nature", "wildlife", "erzi", "mountain", "north-caucasus"],
    maps_text("Заповедник Эрзи", "Джейрахский район", "Erzi Nature Reserve", "Ingushetia", 42.8024, 44.7540),
))

# 13) Мят-Сели ----------------------------------------------------------------------
RECORDS.append(rec(
    "myat-seli-sanctuary",
    "Thánh địa Myat-Seli (Mjat-Xê-li)",
    "Мят-Сели",
    "Myat-Seli Sanctuary",
    ["church", "monument"],
    42.8533, 44.7169,
    "Trên đỉnh núi Bàn (Stolovaya - Myat-Loam), ranh giới quận Dzheyrakh, Cộng hòa Ingushetia, Nga.",
    "Myat-Seli là đền - thánh địa cổ của người Ingush nằm ngay trên đỉnh núi Bàn (Myat-Loam) thiêng. Đây là một trong những di tích tín ngưỡng được tôn kính nhất, nơi diễn ra các nghi lễ cầu mùa từ thời xa xưa.",
    "Trên đỉnh núi Bàn (Myat-Loam) - ngọn núi thiêng bậc nhất của Ingushetia - còn lưu giữ đến ngày nay một di tích tín ngưỡng cổ: đền - thánh địa Myat-Seli. Đây là một trong những nơi thờ tự quan trọng nhất trong hệ thống tín ngưỡng tiền Hồi giáo của người Ingush, gắn với việc thờ các vị thần thiên nhiên và cầu cho mùa màng, mưa thuận gió hòa. Vào những dịp lễ theo lịch mặt trời, các bô lão và pháp sư (thầy tế) leo lên đỉnh núi để hành lễ và dâng vật hiến tế. Ngôi đền đá khiêm nhường nhưng mang ý nghĩa tâm linh sâu sắc, là chứng tích cho lớp tín ngưỡng bản địa lâu đời trước khi Hồi giáo lan tới vùng núi. Nằm ở độ cao gần 3.000 m, Myat-Seli vừa là điểm đến hành hương - lịch sử, vừa là phần thưởng cho những ai chinh phục đỉnh núi Bàn, với tầm nhìn bao la xuống các thung lũng và dãy Kavkaz.",
    [
        "Đền - thánh địa cổ của người Ingush ngay trên đỉnh núi Bàn (Myat-Loam) thiêng.",
        "Nơi hành lễ cầu mùa và dâng hiến tế theo lịch mặt trời từ thời tiền Hồi giáo.",
        "Chứng tích tín ngưỡng bản địa lâu đời, ở độ cao gần 3.000 m với tầm nhìn hùng vĩ.",
    ],
    mountain_practical("Kết hợp trong hành trình leo núi Bàn (trọn ngày).",
                       "Tôn trọng không gian thiêng; cần thể lực tốt và hướng dẫn viên."),
    [
        {"title": "TripPlanet — Достопримечательности Ингушетии", "url": "https://tripplanet.ru/dostoprimechatelnosti-ingushetii/"},
        {"title": "Wikipedia (RU) — Столовая (гора, Кавказ)", "url": "https://ru.wikipedia.org/wiki/Столовая_(гора,_Кавказ)"},
    ],
    ["sanctuary", "pagan", "sacred", "mountain", "heritage", "vainakh"],
    maps_text("Мят-Сели", "гора Столовая, Джейрахский район", "Myat-Seli Sanctuary", "Ingushetia", 42.8533, 44.7169),
))

# 14) Джума-мечеть Назрани ----------------------------------------------------------
RECORDS.append(rec(
    "nazran-dzhuma-mosque",
    "Nhà thờ Hồi giáo trung tâm (Djuma) Nazran",
    "Центральная (Джума) мечеть Назрани",
    "Nazran Central (Dzhuma) Mosque",
    ["church"],
    43.2311, 44.7711,
    "Thành phố Nazran, Cộng hòa Ingushetia, Bắc Kavkaz, Nga.",
    "Nhà thờ Hồi giáo trung tâm (Djuma) của Nazran là một trong những thánh đường Hồi giáo lớn của Ingushetia - nơi cầu nguyện tập thể ngày thứ Sáu của cộng đồng Hồi giáo Sunni ở thành phố lớn nhất nước cộng hòa.",
    "Là nước cộng hòa mà đa số dân theo Hồi giáo Sunni, Ingushetia có nhiều thánh đường, và nhà thờ Hồi giáo trung tâm (Djuma) ở Nazran là một trong những công trình tôn giáo tiêu biểu. 'Djuma' (Jumu'ah) chỉ buổi lễ cầu nguyện tập thể trọng thể vào trưa thứ Sáu, nên nhà thờ Djuma là trung tâm sinh hoạt tôn giáo của cộng đồng tại thành phố đông dân nhất nước cộng hòa. Với những mái vòm và tháp bút (minaret) vươn cao, thánh đường mang phong cách kiến trúc Hồi giáo hiện đại, là nơi diễn ra các buổi lễ, sự kiện tôn giáo và cũng là điểm để du khách tìm hiểu đời sống tinh thần của người Ingush. Khi tới thăm, du khách nên ăn mặc kín đáo và giữ thái độ tôn trọng theo quy tắc của nơi thờ tự.",
    [
        "Thánh đường Hồi giáo trung tâm (Djuma) của Nazran - thành phố lớn nhất Ingushetia.",
        "Trung tâm lễ cầu nguyện tập thể thứ Sáu của cộng đồng Hồi giáo Sunni.",
        "Kiến trúc Hồi giáo với mái vòm và tháp bút; điểm tìm hiểu đời sống tâm linh Ingush.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ lễ trong ngày; ngoài giờ cầu nguyện có thể tham quan bên ngoài.",
        "ticket_vi": "Vào cửa tự do (không thu vé).",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Quanh năm; tránh giờ cầu nguyện đông người nếu chỉ tham quan.",
        "tips_vi": "Ăn mặc kín đáo, cởi giày khi vào; phụ nữ nên trùm khăn; giữ trật tự, tôn trọng người hành lễ.",
    },
    [
        {"title": "AutoTravel — Назрань, что посмотреть", "url": "https://autotravel.ru/excite.php/4241/1"},
    ],
    ["mosque", "islam", "religion", "nazran", "architecture"],
    maps_text("Центральная мечеть", "Назрань", "Nazran Central Mosque", "Nazran", 43.2311, 44.7711),
))

# 15) Крепость Назрань --------------------------------------------------------------
RECORDS.append(rec(
    "nazran-fortress",
    "Pháo đài Nazran (Nạ-dran)",
    "Назрановская крепость",
    "Nazran Fortress",
    ["fortress", "monument"],
    43.2472, 44.8102,
    "Thành phố Nazran, Cộng hòa Ingushetia, Bắc Kavkaz, Nga.",
    "Pháo đài Nazran là công trình quân sự của quân đội đế quốc Nga đầu thế kỷ 19, một trong số ít di tích kiến trúc phòng thủ thời kỳ đó còn sót lại và là một trong những điểm tham quan chính ở vùng đồng bằng Ingushetia.",
    "Pháo đài Nazran là một mẫu mực hiếm hoi của kiến trúc quân sự - phòng thủ Nga đầu thế kỷ 19 còn tồn tại trên vùng đồng bằng Ingushetia. Được quân đội đế quốc Nga xây dựng trong quá trình mở rộng kiểm soát vùng Bắc Kavkaz, pháo đài từng giữ vai trò trọng yếu về quân sự và hành chính, kiểm soát các tuyến đường trên vùng chân núi. Trải qua hai thế kỷ, công trình vẫn giữ được nét đặc trưng của một pháo đài cổ với tường thành và bố cục phòng thủ, trở thành một trong những di tích lịch sử - văn hóa quan trọng và là điểm tham quan chính ở khu vực đồng bằng của nước cộng hòa. Đây là nơi giúp du khách hình dung một trang lịch sử phức tạp của quan hệ giữa vùng Kavkaz và nước Nga, đồng thời là điểm dừng thuận tiện ngay trong thành phố Nazran.",
    [
        "Pháo đài quân sự Nga đầu thế kỷ 19, hiếm hoi còn sót lại ở Bắc Kavkaz.",
        "Giữ nét đặc trưng của pháo đài cổ với tường thành và bố cục phòng thủ.",
        "Một trong những điểm tham quan lịch sử chính ở vùng đồng bằng Ingushetia.",
    ],
    {
        "hours_vi": "Di tích ngoài trời; tham quan ban ngày. Nên hỏi trước về khả năng vào bên trong.",
        "ticket_vi": "Thường không thu vé hoặc phí thấp; kiểm tra tại chỗ.",
        "duration_vi": "Khoảng 30–60 phút.",
        "best_time_vi": "Quanh năm; đẹp nhất vào ngày trời quang.",
        "tips_vi": "Nằm trong thành phố Nazran, dễ kết hợp với Memorial 'Chín Tháp' và bảo tàng Malsagov.",
    },
    [
        {"title": "Wikipedia (RU) — Крепость Назрань", "url": "https://ru.wikipedia.org/wiki/Крепость_Назрань"},
        {"title": "AutoTravel — Назрань (N043 14.834 E044 48.612)", "url": "https://autotravel.ru/excite.php/4241/1"},
    ],
    ["fortress", "military", "19th-century", "nazran", "russian-empire", "heritage"],
    maps_text("Назрановская крепость", "Назрань", "Nazran Fortress", "Nazran", 43.2472, 44.8102),
))

# 16) Мемориал «Девять башен» -------------------------------------------------------
RECORDS.append(rec(
    "nine-towers-memorial",
    "Đài tưởng niệm 'Chín Tháp' (Tưởng niệm & Vinh quang)",
    "Мемориал памяти и славы «Девять башен»",
    "Nine Towers Memorial (Memorial of Memory and Glory)",
    ["monument", "museum"],
    43.196869, 44.771359,
    "Khu Nasyr-Kort, thành phố Nazran, Cộng hòa Ingushetia, Bắc Kavkaz, Nga.",
    "Đài tưởng niệm 'Chín Tháp' là biểu tượng và 'tấm danh thiếp' của Ingushetia. Chín tòa tháp áp sát nhau, quấn dây thép gai, tưởng niệm các dân tộc bị trục xuất năm 1944; bên trong là bảo tàng về thảm kịch lịch sử.",
    "Nằm ở khu Nasyr-Kort của thành phố Nazran, Memorial 'Tưởng niệm và Vinh quang' (mà trung tâm là đài 'Chín Tháp' - Девять башен) là một trong những công trình tưởng niệm quan trọng và xúc động nhất của Ingushetia. Đài 'Chín Tháp' được khánh thành năm 1997, đúng dịp tưởng niệm cuộc trục xuất người Ingush và Chechen sang Kazakhstan và Trung Á năm 1944; cả quần thể được hoàn thiện quy mô vào năm 2012. Công trình cao khoảng 25 m gồm chín tòa tháp kiểu Vainakh áp sát nhau - mỗi tháp tượng trưng cho một dân tộc từng chịu cảnh lưu đày - và được quấn dây thép gai như một hình ảnh ám ảnh về nỗi đau chung. Bên trong có bảo tàng trưng bày tư liệu, hiện vật về thảm kịch 1944 cũng như cuộc xung đột năm 1992. Quần thể còn có hàng cột (colonnade), tượng đài trung đoàn kỵ binh, một đoàn tàu gợi nhắc chuyến lưu đày và nhiều tác phẩm điêu khắc khác. Do kiến trúc sư - nghệ sĩ công huân Murad Polonkoev thiết kế (từng nhận huy chương vàng của Viện Hàn lâm Nghệ thuật Nga), đây là nơi để tưởng nhớ, suy ngẫm và hiểu sâu hơn về lịch sử của người Ingush.",
    [
        "Đài 'Chín Tháp' cao ~25 m: chín tháp Vainakh áp sát, quấn dây thép gai, mỗi tháp một dân tộc bị lưu đày.",
        "Tưởng niệm cuộc trục xuất 1944; có bảo tàng về thảm kịch 1944 và xung đột 1992 bên trong.",
        "Biểu tượng của Ingushetia, do nghệ sĩ Murad Polonkoev thiết kế; có hàng cột, tượng đài, đoàn tàu lưu đày.",
    ],
    {
        "hours_vi": "Khu tưởng niệm ngoài trời; bảo tàng bên trong mở ban ngày, có tour hằng ngày.",
        "ticket_vi": "Vào khu tưởng niệm thường tự do; tham quan bảo tàng/tour có thể tính phí - hỏi tại chỗ.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Giữ thái độ trang nghiêm tại nơi tưởng niệm; nên đi cùng hướng dẫn để hiểu bối cảnh lịch sử.",
    },
    [
        {"title": "Wikipedia (RU) — Мемориал памяти и славы (Назрань)", "url": "https://ru.wikipedia.org/wiki/Мемориал_памяти_и_славы_(Назрань)"},
        {"title": "TripPlanet — Достопримечательности Ингушетии", "url": "https://tripplanet.ru/dostoprimechatelnosti-ingushetii/"},
    ],
    ["memorial", "deportation-1944", "nine-towers", "museum", "nazran", "history"],
    maps_text("Мемориал памяти и славы Девять башен", "Назрань", "Nine Towers Memorial", "Nazran", 43.196869, 44.771359),
))

# 17) Ингушский музей краеведения им. Т. Мальсагова --------------------------------
RECORDS.append(rec(
    "ingush-museum-malsagov",
    "Bảo tàng địa phương Ingushetia mang tên T. Malsagov",
    "Ингушский государственный музей краеведения имени Т. Мальсагова",
    "Ingush State Museum of Local Lore named after T. Malsagov",
    ["museum"],
    43.2316, 44.7682,
    "Ул. Осканова (Oskanov), số 29, thành phố Nazran, Cộng hòa Ingushetia, Nga.",
    "Bảo tàng địa phương quốc gia Ingushetia mang tên nhà nghiên cứu Tugan Malsagov là bảo tàng lịch sử - văn hóa chính của nước cộng hòa. Bộ sưu tập trải rộng từ thiên nhiên, khảo cổ tới dân tộc học và lịch sử người Ingush.",
    "Nằm trên phố Oskanov ở trung tâm Nazran, Bảo tàng địa phương quốc gia Ingushetia mang tên Tugan Malsagov là điểm khởi đầu lý tưởng để hiểu về vùng đất và con người Ingush. Các gian trưng bày dẫn khách đi qua thế giới tự nhiên của núi rừng Kavkaz, những phát hiện khảo cổ của nền văn hóa Koban và thời tháp cổ, đời sống - phong tục - trang phục - vũ khí của người Ingush, cho tới những trang sử cận - hiện đại đầy biến động của nước cộng hòa. Một trong những hiện vật được chú ý là bản sao tượng đồng 'Đại bàng Suleiman' (thế kỷ 8) - biểu tượng của Ingushetia mà bản gốc hiện lưu giữ tại Bảo tàng Hermitage. Là bảo tàng đầu ngành của vùng, nơi đây thường xuyên tổ chức các triển lãm chuyên đề và hoạt động giáo dục, giúp du khách nắm bắt bức tranh tổng thể về di sản văn hóa - lịch sử Ingushetia trước khi lên đường khám phá 'xứ sở tháp cổ'.",
    [
        "Bảo tàng lịch sử - văn hóa đầu ngành của Ingushetia, mang tên T. Malsagov.",
        "Trưng bày thiên nhiên, khảo cổ Koban, dân tộc học và lịch sử người Ingush.",
        "Có bản sao tượng đồng 'Đại bàng Suleiman' - biểu tượng vùng (bản gốc ở Hermitage).",
    ],
    {
        "hours_vi": "Mở cửa ban ngày (thường khoảng 9:00–18:00); nên kiểm tra lịch theo mùa/ngày nghỉ.",
        "ticket_vi": "Vé vào cửa giá bình dân; có thêm phí cho tour hướng dẫn và triển lãm chuyên đề.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Nằm ở trung tâm Nazran, tiện kết hợp với Memorial 'Chín Tháp' và pháo đài Nazran.",
    },
    [
        {"title": "Culture.ru — Ингушский музей краеведения им. Т. Х. Мальсагова", "url": "https://www.culture.ru/institutes/9986/ingushskii-gosudarstvennyi-muzei-kraevedeniya-im-t-kh-malsagova"},
        {"title": "AutoTravel — Назрань (N043 13.894 E044 46.092, ул. Осканова 29)", "url": "https://autotravel.ru/excite.php/4241/1"},
    ],
    ["museum", "local-history", "ethnography", "archaeology", "nazran"],
    maps_text("Ингушский музей краеведения имени Мальсагова", "Назрань", "Ingush Museum of Local Lore", "Nazran", 43.2316, 44.7682),
))

# 18) Аланские Ворота (Магас) -------------------------------------------------------
RECORDS.append(rec(
    "alan-gate-magas",
    "Cổng Alan (Alanskiye Vorota, Magas)",
    "Аланские Ворота",
    "Alan Gate (Magas)",
    ["monument"],
    43.1802, 44.7988,
    "Cửa ngõ vào thành phố Magas, thủ phủ Cộng hòa Ingushetia, Nga.",
    "Cổng Alan (Alanskiye Vorota) là một công trình - biểu tượng ở cửa ngõ thủ phủ Magas, gợi nhắc di sản Alan cổ và mở ra 'gương mặt' của thành phố thủ phủ trẻ nhất nước Nga.",
    "Cổng Alan (Alanskiye Vorota) là một trong những công trình - biểu tượng đón chào du khách ở cửa ngõ thành phố Magas. Tên gọi gợi nhắc tới người Alan - cư dân cổ của vùng và tới chính địa danh Magas, vốn được cho là kinh đô cổ của nhà nước Alania thời trung cổ. Được dựng lên khi Magas hình thành như thủ phủ mới của Cộng hòa Ingushetia, cổng Alan đóng vai trò như một 'khải hoàn môn' hiện đại, kết nối niềm tự hào lịch sử với diện mạo quy hoạch mới mẻ của thành phố. Với hình khối bề thế và vị trí ngay lối vào, đây là điểm chụp ảnh lưu niệm quen thuộc và là khởi đầu tự nhiên cho hành trình tham quan Magas - từ Tháp Đồng thuận tới các đại lộ và quảng trường trung tâm.",
    [
        "Công trình - biểu tượng ở cửa ngõ thủ phủ Magas.",
        "Gợi nhắc di sản Alan cổ và tên gọi Magas - kinh đô cổ của Alania.",
        "'Khải hoàn môn' hiện đại, điểm chụp ảnh và khởi đầu tham quan thành phố.",
    ],
    {
        "hours_vi": "Công trình ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–20 phút.",
        "best_time_vi": "Quanh năm; đẹp khi lên đèn buổi tối.",
        "tips_vi": "Kết hợp tham quan trung tâm Magas: Tháp Đồng thuận, đại lộ Idris Zyazikov.",
    },
    [
        {"title": "Tur-Ray — Достопримечательности Магаса (43.180178, 44.798844)", "url": "https://tur-ray.ru/magas-attractions.html"},
    ],
    ["landmark", "gate", "magas", "alania", "modern"],
    maps_text("Аланские Ворота", "Магас", "Alan Gate", "Magas", 43.1802, 44.7988),
))

# 19) Магас — центр / проспект Идриса Зязикова -------------------------------------
RECORDS.append(rec(
    "magas-center-zyazikov-avenue",
    "Trung tâm Magas - Đại lộ Idris Zyazikov",
    "Магас — проспект Идриса Зязикова",
    "Magas Center — Idris Zyazikov Avenue",
    ["square_street"],
    43.1667, 44.8042,
    "Trung tâm thành phố Magas, thủ phủ Cộng hòa Ingushetia, Nga.",
    "Magas là thủ phủ trẻ nhất nước Nga - một thành phố quy hoạch mới xây từ thập niên 1990. Đại lộ trung tâm Idris Zyazikov với các tòa nhà chính quyền, Quốc hội và không gian hiện đại là trái tim hành chính của nước cộng hòa.",
    "Magas là một trong những thành phố độc đáo nhất nước Nga: được khởi công xây dựng từ giữa thập niên 1990 trên vùng đất trống và trở thành thủ phủ của Cộng hòa Ingushetia từ năm 2000, đây là một trong những thủ phủ trẻ và nhỏ nhất cả nước. Tên thành phố lấy từ 'Magas' - kinh đô cổ được cho là của nhà nước Alania thời trung cổ, thể hiện khát vọng nối tiếp di sản lịch sử. Là một thành phố quy hoạch từ đầu, Magas gây ấn tượng với bố cục thoáng đãng, các đại lộ rộng và những công trình hành chính hiện đại. Trục trung tâm - đại lộ Idris Zyazikov - là nơi tập trung các cơ quan đầu não như trụ sở Chính phủ và Quốc hội (Народное Собрание) nước cộng hòa, cùng các quảng trường và không gian công cộng. Dạo bộ dọc trục này, du khách có thể cảm nhận diện mạo của một thủ phủ mới đang vươn lên, và từ đây dễ dàng ghé Tháp Đồng thuận hay cổng Alan gần kề.",
    [
        "Thủ phủ trẻ nhất nước Nga: xây mới từ thập niên 1990, thành thủ phủ Ingushetia năm 2000.",
        "Đại lộ trung tâm Idris Zyazikov quy tụ trụ sở Chính phủ, Quốc hội và các quảng trường.",
        "Thành phố quy hoạch hiện đại, tên lấy từ kinh đô cổ Magas của Alania.",
    ],
    {
        "hours_vi": "Không gian đô thị mở, dạo bộ tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 1–2 giờ dạo trung tâm.",
        "best_time_vi": "Quanh năm; buổi chiều tối mát mẻ, lên đèn đẹp.",
        "tips_vi": "Kết hợp Tháp Đồng thuận và cổng Alan; lưu ý đây là khu hành chính, tôn trọng quy định chụp ảnh gần trụ sở.",
    },
    [
        {"title": "Wikipedia (RU) — Магас", "url": "https://ru.wikipedia.org/wiki/Магас"},
        {"title": "TripPlanet — Достопримечательности Ингушетии", "url": "https://tripplanet.ru/dostoprimechatelnosti-ingushetii/"},
    ],
    ["capital", "magas", "avenue", "modern-city", "square"],
    maps_text("Проспект Идриса Зязикова", "Магас", "Idris Zyazikov Avenue", "Magas", 43.1667, 44.8042),
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
