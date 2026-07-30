# -*- coding: utf-8 -*-
"""_add_places_karachay-cherkessia_20260728_2.py
VÙNG: Cộng hoà Karachay-Cherkessia (Карачаево-Черкесская Республика), Vùng Bắc Kavkaz.
(lần chạy tự động 2026-07-28)

Bối cảnh: karachay-cherkessia.json hiện có 7 địa điểm. Bổ sung 24 địa điểm THẬT SỰ nổi
tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 31 (≥30).

Chống trùng slug/id đã có: dombay-resort, arkhyz-resort, teberda-nature-reserve,
lower-arkhyz-alan-churches, sofia-waterfalls, special-astrophysical-observatory-bta,
khurzuk-village.

Phân bố loại hình 24 bản ghi mới:
- church (3): Шоанинский храм, Сентинский храм, Никольский собор (Черкесск).
- fortress (2): Хумаринское городище, Рим-Гора (đều +monument).
- museum (1): Карачаево-Черкесский музей-заповедник (Черкесск).
- other (1): РАТАН-600 (đài thiên văn vô tuyến).
- monument (1): Лик Христа (Архыз).
- square_street (1): Учкулан (làng cổ Karachay).
- park_garden (15): Клухорский перевал, Клухорское озеро, Бадукские озёра, Софийские
  озёра, Медовые водопады, Перевал Гумбаши, Кара-Кёль (Теберда), Алибекский водопад,
  каньон Аманауз, Муруджинские озёра, Чучхурский водопад, Гоначхирское ущелье, пик
  Домбай-Ульген, Джемагатское ущелье, парк «Зелёный остров» (Черкесск).

TOẠ ĐỘ — xác minh chéo (ru.wikipedia coordinates API, en.wikipedia, sobory.ru, OSM,
2GIS, các trang du lịch Nga; 2026-07-28). Phạm vi Karachay-Cherkessia: lat ~43,2–44,5;
lon ~40,5–42,6 — tất cả toạ độ nằm trong phạm vi, ĐÃ kiểm tra KHÔNG đảo lat/lon. Cảnh báo
đã xử lý: bài ru.wiki cùng tên "Кара-Кёль" là hồ ở Kyrgyzstan → đã dùng toạ độ hồ Kara-Kel
tại Teberda từ nguồn du lịch Nga; toạ độ Аманауз dùng điểm caньon tại Домбай (không phải cửa
sông); РАТАН-600 lấy từ en.wikipedia (ru.wiki không có toạ độ).

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_karachay-cherkessia_20260728_2.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "karachay-cherkessia"
REGION_NAME_VI = "Cộng hoà Karachay-Cherkessia"
FD = "Vùng Bắc Kavkaz"

# Ghi chú vùng biên giới (dùng cho các điểm giáp Abkhazia/Gruzia: Клухор, Гоначхир...)
BORDER = ("Đây là khu vực sát biên giới (vùng Klukhor giáp Abkhazia): du khách, nhất là "
          "người nước ngoài, có thể cần giấy phép vào vùng biên giới, nên hỏi trước tour "
          "hoặc cơ quan biên phòng.")


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


def nat_practical(hours, ticket, duration, best, tips):
    return {
        "hours_vi": hours,
        "ticket_vi": ticket,
        "duration_vi": duration,
        "best_time_vi": best,
        "tips_vi": tips,
    }


RECORDS = []

# 1) Шоанинский храм ---------------------------------------------------------------
RECORDS.append(rec(
    "shoana-church",
    "Nhà thờ Alan Shoana (Sô-a-na)",
    "Шоанинский храм",
    "Shoana Church",
    ["church"],
    43.80444, 41.88944,
    "Trên mỏm núi Shoana gần làng Kosta Khetagurova, huyện Karachayevsky, cách Karachayevsk vài km về phía bắc, Cộng hoà Karachay-Cherkessia, Nga.",
    "Nhà thờ Shoana là một trong những nhà thờ Kitô giáo cổ nhất nước Nga, dựng từ khoảng thế kỷ 10 thời quốc gia Alania. Ngôi đền đá kiểu Byzantine đứng chênh vênh trên mỏm núi, nhìn xuống thung lũng sông Kuban.",
    "Cùng với các nhà thờ ở Hạ Arkhyz và nhà thờ Senty lân cận, Shoana thuộc nhóm những công trình Kitô giáo cổ nhất còn đứng vững trên lãnh thổ Liên bang Nga, có niên đại khoảng thế kỷ 10 - thời kỳ nhà nước Alania tiếp nhận Kitô giáo từ Byzantium. Nhà thờ được xây theo hình thánh giá với mái vòm, bằng đá phiến, mang đậm phong cách kiến trúc Byzantine của vùng Kavkaz. Vị trí của nó đặc biệt ấn tượng: công trình toạ lạc trên một mỏm núi đá nhô cao gần làng Kosta Khetagurova, từ đây tầm nhìn mở rộng ra thung lũng sông Kuban và những dãy núi xung quanh. Qua nhiều thế kỷ, ngôi đền từng gắn với một tu viện và vẫn là nơi hành hương của tín đồ. Với du khách, Shoana vừa là di tích khảo cổ - tôn giáo quý giá, vừa là điểm ngắm cảnh tuyệt đẹp, đặc biệt vào lúc bình minh hay hoàng hôn khi ánh nắng nhuộm vàng những bức tường đá cổ.",
    [
        "Một trong những nhà thờ Kitô giáo cổ nhất nước Nga (khoảng thế kỷ 10, thời Alania).",
        "Kiến trúc đá kiểu Byzantine dựng chênh vênh trên mỏm núi Shoana.",
        "Tầm nhìn tuyệt đẹp xuống thung lũng sông Kuban và dãy núi Kavkaz.",
    ],
    nat_practical(
        "Di tích ngoài trời, tham quan ban ngày quanh năm; không có giờ đóng mở cố định.",
        "Vào tự do, không thu vé cố định (có thể quyên góp cho việc trùng tu).",
        "Khoảng 1–2 giờ kể cả đường leo lên mỏm núi.",
        "Cuối xuân đến đầu thu (tháng 5–10); sáng sớm hoặc chiều muộn để chụp ảnh đẹp.",
        "Đường lên dốc và trơn khi mưa, nên đi giày bám tốt; kết hợp thăm nhà thờ Senty và thành phố Karachayevsk.",
    ),
    [
        {"title": "Wikipedia (RU) — Шоанинский храм", "url": "https://ru.wikipedia.org/wiki/Шоанинский_храм"},
        {"title": "Sobory.ru — Шоанинский храм", "url": "https://sobory.ru/geo/?ll=41.889,43.804"},
    ],
    ["alania", "byzantine", "medieval-church", "kuban", "pilgrimage", "caucasus"],
    maps_text("Шоанинский храм", "Карачаево-Черкесия", "Shoana Church", "Karachay-Cherkessia", 43.80444, 41.88944),
))

# 2) Сентинский храм ---------------------------------------------------------------
RECORDS.append(rec(
    "sentinsky-church",
    "Nhà thờ Alan Senty (Xen-ti)",
    "Сентинский храм",
    "Senty Church",
    ["church"],
    43.63694, 41.86583,
    "Trên sườn núi phía trên làng Nizhnyaya Teberda (Hạ Teberda), huyện Karachayevsky, Cộng hoà Karachay-Cherkessia, Nga.",
    "Nhà thờ Senty là một trong những nhà thờ Kitô giáo cổ nhất nước Nga, dựng khoảng năm 965 thời Alania. Ngôi đền đá đứng trên sườn núi cao phía trên làng Hạ Teberda, bên cạnh là phế tích một tu viện và các lăng mộ cổ.",
    "Nằm trên một sườn núi cao nhìn xuống thung lũng sông Teberda phía trên làng Nizhnyaya Teberda, nhà thờ Senty được xem là một trong những công trình Kitô giáo cổ nhất còn nguyên vẹn ở Nga, với niên đại xây dựng thường được ghi vào khoảng năm 965. Cùng nhóm với các nhà thờ Hạ Arkhyz và Shoana, Senty phản ánh giai đoạn Kitô giáo hoá của nhà nước Alania dưới ảnh hưởng Byzantine. Nhà thờ có mặt bằng hình thánh giá và mái vòm, bên trong từng lưu giữ những mảng bích hoạ cổ. Gần đó là dấu tích của một tu viện nữ được lập vào cuối thế kỷ 19, cùng những lăng mộ đá (mausoleum) và di chỉ khảo cổ, tạo thành một quần thể lịch sử - tôn giáo đặc sắc. Đường lên nhà thờ dốc nhưng phần thưởng là khung cảnh núi non hùng vĩ và cảm giác đứng giữa một di tích hơn nghìn năm tuổi.",
    [
        "Một trong những nhà thờ cổ nhất nước Nga (khoảng năm 965, thời Alania).",
        "Kiến trúc đá Byzantine với dấu tích bích hoạ, đứng trên sườn núi cao.",
        "Bên cạnh có phế tích tu viện thế kỷ 19 và các lăng mộ cổ.",
    ],
    nat_practical(
        "Di tích ngoài trời, tham quan ban ngày quanh năm; không có giờ cố định.",
        "Vào tự do, không thu vé cố định.",
        "Khoảng 1,5–2 giờ kể cả đường leo lên sườn núi.",
        "Cuối xuân đến đầu thu (tháng 5–10) khi đường khô ráo.",
        "Đường lên dốc, cần giày leo tốt và thể lực; kết hợp thăm nhà thờ Shoana và khu bảo tồn Teberda.",
    ),
    [
        {"title": "Wikipedia (RU) — Сентинский храм", "url": "https://ru.wikipedia.org/wiki/Сентинский_храм"},
        {"title": "Sobory.ru — Сентинский храм", "url": "https://sobory.ru/geo/?ll=41.866,43.637"},
    ],
    ["alania", "byzantine", "medieval-church", "teberda", "frescoes", "caucasus"],
    maps_text("Сентинский храм", "Нижняя Теберда", "Senty Church", "Karachay-Cherkessia", 43.63694, 41.86583),
))

# 3) Никольский собор (Черкесск) ---------------------------------------------------
RECORDS.append(rec(
    "nikolsky-cathedral-cherkessk",
    "Nhà thờ chính toà Thánh Nikolai (Chéc-két)",
    "Свято-Никольский собор",
    "St Nicholas Cathedral (Cherkessk)",
    ["church"],
    44.22760, 42.05400,
    "Quảng trường Kirov, trung tâm thành phố Cherkessk, thủ phủ Cộng hoà Karachay-Cherkessia, Nga.",
    "Nhà thờ chính toà Thánh Nikolai là nhà thờ Chính thống giáo lớn và nổi bật nhất ở Cherkessk. Công trình mái vòm vàng bên quảng trường Kirov là trung tâm đời sống tôn giáo của thủ phủ nước cộng hoà.",
    "Toạ lạc ngay quảng trường Kirov ở trung tâm Cherkessk, nhà thờ chính toà Thánh Nikolai (Svyato-Nikolsky) là ngôi thánh đường Chính thống giáo chính của thủ phủ Karachay-Cherkessia. Nhà thờ nguyên thuỷ bằng gỗ từng bị phá huỷ trong thời kỳ Xô Viết; công trình khang trang hiện nay được xây lại bằng gạch với những mái vòm mạ vàng vươn cao, trở thành một trong những điểm nhấn kiến trúc của thành phố. Bên trong là không gian trang nghiêm với các bức icon và tranh tường theo truyền thống Chính thống giáo Nga. Đây không chỉ là nơi hành lễ của cộng đồng Cơ Đốc mà còn là điểm dừng chân quen thuộc của du khách khi khám phá trung tâm Cherkessk, nằm gần quảng trường trung tâm và các công viên của thành phố. Tiếng chuông và những mái vòm vàng lấp lánh dưới nắng khiến nhà thờ trở thành biểu tượng thân thuộc của đô thị vùng Bắc Kavkaz này.",
    [
        "Nhà thờ Chính thống giáo lớn nhất và nổi bật nhất của thủ phủ Cherkessk.",
        "Kiến trúc gạch với các mái vòm mạ vàng bên quảng trường Kirov.",
        "Nội thất trang nghiêm với icon và tranh tường Chính thống giáo Nga.",
    ],
    nat_practical(
        "Mở cửa hằng ngày theo giờ lễ, thường khoảng 7:00–19:00 (thay đổi theo lịch phụng vụ).",
        "Vào tự do, miễn phí.",
        "Khoảng 30–45 phút.",
        "Quanh năm; ghé vào giờ lễ để cảm nhận không khí phụng vụ.",
        "Ăn mặc kín đáo khi vào nhà thờ; nữ nên mang khăn trùm đầu; kết hợp dạo quảng trường trung tâm và công viên Zelyony Ostrov gần đó.",
    ),
    [
        {"title": "Sobory.ru — Свято-Никольский собор (Черкесск)", "url": "https://sobory.ru/geo/?ll=42.054,44.228"},
        {"title": "Wikipedia (RU) — Черкесск", "url": "https://ru.wikipedia.org/wiki/Черкесск"},
    ],
    ["orthodox", "cathedral", "cherkessk", "golden-domes", "city-landmark"],
    maps_text("Свято-Никольский собор", "Черкесск", "St Nicholas Cathedral", "Cherkessk", 44.22760, 42.05400),
))

# 4) Хумаринское городище ----------------------------------------------------------
RECORDS.append(rec(
    "khumara-fortress",
    "Thành cổ Khumara (Khu-ma-ra)",
    "Хумаринское городище",
    "Khumara Fortress",
    ["fortress", "monument"],
    43.87086, 41.92752,
    "Trên đỉnh cao nguyên đá hữu ngạn sông Kuban gần làng Khumara, huyện Karachayevsky, Cộng hoà Karachay-Cherkessia, Nga.",
    "Khumara là một thành luỹ đá cổ đồ sộ thời Trung cổ, gắn với nhà nước Khazar và Alania. Những đoạn tường đá khổng lồ trên cao nguyên hữu ngạn sông Kuban là chứng tích của một trung tâm phòng thủ - thương mại lớn trên tuyến Con đường Tơ lụa.",
    "Nằm trên một cao nguyên đá dựng đứng bên hữu ngạn sông Kuban, thành cổ Khumara là một trong những di chỉ khảo cổ ấn tượng nhất Karachay-Cherkessia. Toà thành có từ khoảng thế kỷ 8–10, thường được gắn với đế quốc Khazar và vùng ảnh hưởng Alania, từng là một pháo đài - đô thị án ngữ tuyến giao thương bắc qua Kavkaz. Điểm gây choáng ngợp nhất là hệ thống tường thành xây bằng những khối đá vôi lớn, có đoạn dài hàng trăm mét, cùng dấu tích các công trình, hầm mộ và bia đá khắc chữ (rune, Ả Rập, Hy Lạp) cho thấy sự giao thoa nhiều nền văn hoá. Vị trí trên cao khiến Khumara vừa hiểm yếu về quân sự vừa mở ra tầm nhìn bao quát thung lũng Kuban. Ngày nay dù chỉ còn là phế tích, quy mô của các bức tường đá vẫn đủ để gợi lên hình dung về một trung tâm quyền lực từng tồn tại hơn một nghìn năm trước.",
    [
        "Thành luỹ đá cổ (thế kỷ 8–10) gắn với đế quốc Khazar và vùng Alania.",
        "Tường thành bằng khối đá vôi lớn trên cao nguyên hữu ngạn sông Kuban.",
        "Dấu tích bia khắc nhiều loại chữ, minh chứng giao thoa văn hoá trên đường tơ lụa.",
    ],
    nat_practical(
        "Di chỉ khảo cổ ngoài trời, tham quan ban ngày quanh năm; không có giờ cố định.",
        "Vào tự do, không thu vé cố định.",
        "Khoảng 1,5–2 giờ; cần đi bộ lên cao nguyên.",
        "Cuối xuân đến đầu thu (tháng 5–10) khi trời khô ráo.",
        "Đường lên đồi không có bóng mát, mang nước và mũ; đi xe gầm cao hoặc tour để tới chân di tích.",
    ),
    [
        {"title": "Wikipedia (RU) — Хумаринское городище", "url": "https://ru.wikipedia.org/wiki/Хумаринское_городище"},
    ],
    ["khazar", "alania", "archaeology", "fortress", "silk-road", "kuban"],
    maps_text("Хумаринское городище", "Карачаево-Черкесия", "Khumara Fortress", "Karachay-Cherkessia", 43.87086, 41.92752),
))

# 5) Рим-Гора ----------------------------------------------------------------------
RECORDS.append(rec(
    "rim-gora",
    "Rim-Gora - Núi thành cổ (Rim Ga-ra)",
    "Рим-Гора",
    "Rim-Gora",
    ["fortress", "monument"],
    43.94260, 42.53830,
    "Bên sông Podkumok gần làng Bekeshevskaya/Uchkeken, huyện Malokarachaevsky, Cộng hoà Karachay-Cherkessia, Nga (gần Kislovodsk).",
    "Rim-Gora là một khối núi đá bằng phẳng từng là thành cổ tự nhiên của người Alania thời Trung cổ. Trên đỉnh còn dấu tích thành luỹ, bậc thang đục đá và mộ cổ, giữa khung cảnh thảo nguyên núi ngoạn mục.",
    "Rim-Gora (nghĩa dân gian là 'Núi La Mã') là một ngọn núi đá sa thạch có đỉnh bằng phẳng nhô lên giữa vùng thảo nguyên - núi ở huyện Malokarachaevsky, không xa Kislovodsk. Nhờ vách đá dựng đứng bao quanh, nơi đây từng là một pháo đài - đô thị tự nhiên lý tưởng của người Alania trong khoảng thế kỷ 10–12, án ngữ tuyến đường thương mại quan trọng. Trên và quanh đỉnh núi vẫn còn dấu tích của tường thành, những bậc thang và lối đi đục thẳng vào đá, các hố chứa, cùng nhiều ngôi mộ cổ đã được khảo cổ khai quật. Leo lên đỉnh Rim-Gora, du khách được tưởng thưởng tầm nhìn rộng lớn ra thung lũng sông Podkumok và dãy núi phía nam, trong đó có thể thấy đỉnh Elbrus vào ngày quang mây. Sự kết hợp giữa giá trị khảo cổ và cảnh quan khiến Rim-Gora là điểm dã ngoại - khám phá hấp dẫn cho những ai ưa lịch sử và thiên nhiên.",
    [
        "Núi đá đỉnh bằng từng là thành luỹ tự nhiên của người Alania (thế kỷ 10–12).",
        "Còn dấu tích tường thành, bậc thang đục đá, hố chứa và mộ cổ.",
        "Tầm nhìn rộng ra thung lũng Podkumok, có thể thấy Elbrus khi trời quang.",
    ],
    nat_practical(
        "Di tích ngoài trời, tham quan ban ngày quanh năm; không có giờ cố định.",
        "Vào tự do, không thu vé cố định.",
        "Khoảng 2–3 giờ kể cả leo lên và xuống.",
        "Cuối xuân đến đầu thu (tháng 5–10); tránh khi mưa vì đá trơn.",
        "Đường lên khá dốc và trơn, cần giày bám tốt và cẩn trọng ở mép vách đá; mang đủ nước.",
    ),
    [
        {"title": "Wikipedia (RU) — Рим-Гора", "url": "https://ru.wikipedia.org/wiki/Рим-Гора"},
    ],
    ["alania", "archaeology", "fortress", "table-mountain", "podkumok", "viewpoint"],
    maps_text("Рим-Гора", "Карачаево-Черкесия", "Rim-Gora", "Karachay-Cherkessia", 43.94260, 42.53830),
))

# 6) Карачаево-Черкесский музей-заповедник -----------------------------------------
RECORDS.append(rec(
    "karachay-cherkess-museum",
    "Bảo tàng - khu bảo tồn Karachay-Cherkessia (Chéc-két)",
    "Карачаево-Черкесский музей-заповедник",
    "Karachay-Cherkess Museum-Reserve",
    ["museum"],
    44.23177, 42.04708,
    "Trung tâm thành phố Cherkessk, thủ phủ Cộng hoà Karachay-Cherkessia, Nga.",
    "Đây là bảo tàng lịch sử - văn hoá - thiên nhiên trung tâm của nước cộng hoà, đặt tại Cherkessk. Bộ sưu tập phong phú giới thiệu khảo cổ Alania, dân tộc học các dân tộc Kavkaz và thiên nhiên vùng núi.",
    "Bảo tàng - khu bảo tồn quốc gia Karachay-Cherkessia là thiết chế bảo tàng lớn nhất và lâu đời nhất của nước cộng hoà, đặt tại trung tâm thủ phủ Cherkessk. Với hàng chục nghìn hiện vật, bảo tàng đưa người xem đi qua toàn bộ chiều dài lịch sử vùng đất: từ khảo cổ thời tiền sử và nhà nước Alania thời Trung cổ (đồ trang sức, vũ khí, bia đá), đến dân tộc học của các dân tộc cùng chung sống nơi đây như người Karachay, Cherkess (Circassian), Abazin, Nogai và Nga. Các gian trưng bày tái hiện trang phục truyền thống, đồ thủ công, nhạc cụ, cảnh sinh hoạt du mục và nông nghiệp vùng cao, bên cạnh phần giới thiệu thiên nhiên - địa chất - động thực vật của dãy Kavkaz. Đây là điểm đến lý tưởng để hiểu bức tranh đa sắc tộc và bề dày lịch sử của Karachay-Cherkessia trước khi lên đường khám phá các thung lũng núi. Bảo tàng cũng thường tổ chức triển lãm chuyên đề và hoạt động giáo dục.",
    [
        "Bảo tàng trung tâm về lịch sử, văn hoá và thiên nhiên của nước cộng hoà.",
        "Sưu tập khảo cổ Alania cùng dân tộc học Karachay, Cherkess, Abazin, Nogai.",
        "Giới thiệu thiên nhiên - địa chất - sinh vật dãy Kavkaz, kèm triển lãm chuyên đề.",
    ],
    nat_practical(
        "Thường mở cửa 9:00–18:00, nghỉ thứ Hai (nên kiểm tra lịch trước khi đến).",
        "Vé vào cửa mức thấp; có giá riêng cho các gian đặc biệt và đoàn.",
        "Khoảng 1–2 giờ.",
        "Quanh năm; thích hợp cho ngày thời tiết xấu không lên núi được.",
        "Có thể thuê thuyết minh để hiểu sâu hơn; kết hợp tham quan trung tâm Cherkessk và nhà thờ Thánh Nikolai.",
    ),
    [
        {"title": "Wikipedia (RU) — Черкесск", "url": "https://ru.wikipedia.org/wiki/Черкесск"},
    ],
    ["museum", "history", "ethnography", "alania", "cherkessk", "caucasus-peoples"],
    maps_text("Карачаево-Черкесский музей-заповедник", "Черкесск", "Karachay-Cherkess Museum", "Cherkessk", 44.23177, 42.04708),
))

# 7) РАТАН-600 ---------------------------------------------------------------------
RECORDS.append(rec(
    "ratan-600-radio-telescope",
    "Kính viễn vọng vô tuyến RATAN-600 (Ra-tan)",
    "РАТАН-600",
    "RATAN-600 Radio Telescope",
    ["other"],
    43.82580, 41.58640,
    "Gần làng Zelenchukskaya, huyện Zelenchuksky, Cộng hoà Karachay-Cherkessia, Nga.",
    "RATAN-600 là một trong những kính viễn vọng vô tuyến lớn nhất thế giới, với vòng phản xạ đường kính khoảng 600 m. Đây là cơ sở nghiên cứu thiên văn vô tuyến hàng đầu của Nga, nằm gần làng Zelenchukskaya.",
    "RATAN-600 (viết tắt của 'Kính viễn vọng vô tuyến của Viện Hàn lâm Khoa học') là một công trình khoa học độc đáo thuộc Đài quan sát Vật lý thiên văn Đặc biệt (SAO) của Viện Hàn lâm Khoa học Nga. Điểm đặc biệt của nó là ăng-ten phản xạ hình vòng khép kín gồm hàng trăm tấm gương kim loại xếp thành một vòng tròn đường kính khoảng 600 m - lớn nhất thế giới xét về đường kính vòng phản xạ. Cấu hình này cho phép các nhà khoa học nghiên cứu bức xạ vô tuyến từ Mặt Trời, các thiên hà, chuẩn tinh và nhiều đối tượng vũ trụ khác. Nằm gần làng Zelenchukskaya và cách không xa kính quang học khổng lồ BTA trên núi, RATAN-600 tạo nên cụm cơ sở thiên văn tầm cỡ quốc tế của vùng. Du khách quan tâm khoa học có thể tới tham quan (thường theo tour hoặc đăng ký trước) để tận mắt thấy quy mô ấn tượng của công trình và tìm hiểu cách con người 'lắng nghe' vũ trụ.",
    [
        "Ăng-ten vòng phản xạ đường kính ~600 m - lớn nhất thế giới về loại này.",
        "Cơ sở thiên văn vô tuyến hàng đầu của Nga, thuộc Đài quan sát SAO.",
        "Nghiên cứu bức xạ vô tuyến từ Mặt Trời, thiên hà và chuẩn tinh.",
    ],
    nat_practical(
        "Tham quan theo tour hoặc đăng ký trước; không mở tự do như điểm du lịch thông thường.",
        "Phí tham quan tuỳ chương trình; nên liên hệ đài quan sát trước.",
        "Khoảng 1–1,5 giờ.",
        "Cuối xuân đến đầu thu; kết hợp lịch tham quan kính BTA trên núi.",
        "Đăng ký trước qua tour hoặc đài quan sát; đây là cơ sở khoa học, cần tuân thủ hướng dẫn khi vào.",
    ),
    [
        {"title": "Wikipedia (EN) — RATAN-600", "url": "https://en.wikipedia.org/wiki/RATAN-600"},
        {"title": "Wikipedia (RU) — РАТАН-600", "url": "https://ru.wikipedia.org/wiki/РАТАН-600"},
    ],
    ["astronomy", "radio-telescope", "science", "sao", "zelenchukskaya"],
    maps_text("РАТАН-600", "Зеленчукская", "RATAN-600", "Karachay-Cherkessia", 43.82580, 41.58640),
))

# 8) Лик Христа (Архыз) ------------------------------------------------------------
RECORDS.append(rec(
    "lik-khrista-arkhyz",
    "Ảnh Chúa Kitô trên đá Arkhyz (Lích Khờ-rít-ta)",
    "Лик Христа",
    "Face of Christ (Arkhyz)",
    ["monument"],
    43.68783, 41.47166,
    "Trên sườn núi Mytseshta đối diện khu di tích Hạ Arkhyz (Nizhny Arkhyz), huyện Zelenchuksky, Cộng hoà Karachay-Cherkessia, Nga.",
    "Lik Khrista là hình vẽ khuôn mặt Chúa Kitô trên vách đá gần Hạ Arkhyz, được phát hiện năm 1999. Bức icon bí ẩn thu hút đông đảo khách hành hương leo hàng trăm bậc thang lên chiêm bái.",
    "Trên một vách đá của núi Mytseshta, đối diện quần thể di tích Alania ở Hạ Arkhyz, có một hình vẽ khuôn mặt Chúa Kitô mà người dân địa phương gọi là 'Lik Khrista' (Ảnh/Diện Chúa). Bức icon trên đá này chỉ được công chúng biết đến rộng rãi sau khi được phát hiện lại vào năm 1999, và nhanh chóng trở thành một trong những điểm hành hương nổi tiếng của vùng. Hình ảnh được vẽ bằng chất liệu màu trên bề mặt đá, phong cách gợi nhớ các icon Byzantine, và cho đến nay niên đại cũng như tác giả vẫn còn là đề tài tranh luận - có giả thuyết gắn nó với thời Alania Kitô giáo. Để lên tới nơi, du khách phải leo một cầu thang dài khoảng vài trăm bậc men theo sườn núi; đổi lại, ngoài việc chiêm bái bức ảnh, họ còn được ngắm toàn cảnh thung lũng sông Bolshoy Zelenchuk và khu di tích cổ bên dưới. Sự huyền bí của bức icon cùng khung cảnh núi non khiến đây là điểm đến được nhiều người tìm tới khi ghé Arkhyz.",
    [
        "Hình khuôn mặt Chúa Kitô vẽ trên vách đá, phát hiện lại năm 1999.",
        "Điểm hành hương nổi tiếng, phong cách gợi nhớ icon Byzantine, niên đại còn tranh luận.",
        "Leo cầu thang vài trăm bậc, ngắm toàn cảnh thung lũng và di tích Hạ Arkhyz.",
    ],
    nat_practical(
        "Ngoài trời, tham quan ban ngày quanh năm; không có giờ cố định.",
        "Vào tự do, không thu vé cố định.",
        "Khoảng 1–1,5 giờ kể cả leo bậc thang lên và xuống.",
        "Cuối xuân đến đầu thu (tháng 5–10); sáng sớm để tránh nắng gắt khi leo.",
        "Cầu thang dài và dốc, cần thể lực và giày phù hợp; kết hợp thăm khu di tích và các nhà thờ Alan Hạ Arkhyz.",
    ),
    [
        {"title": "Tourister.ru — Лик Христа (Архыз)", "url": "https://www.tourister.ru/world/europe/russia/city/arhyz/placeofinterest"},
    ],
    ["pilgrimage", "icon", "arkhyz", "alania", "rock-image", "mystery"],
    maps_text("Лик Христа", "Архыз", "Face of Christ", "Arkhyz", 43.68783, 41.47166),
))

# 9) Учкулан -----------------------------------------------------------------------
RECORDS.append(rec(
    "uchkulan-village",
    "Làng cổ Uchkulan (Úc-cu-lan)",
    "Учкулан",
    "Uchkulan",
    ["square_street"],
    43.45400, 42.09620,
    "Nơi hợp lưu hai nhánh sông tạo thành sông Kuban, huyện Karachayevsky, Cộng hoà Karachay-Cherkessia, Nga.",
    "Uchkulan là một trong những làng Karachay cổ nhất, được xem là cái nôi lịch sử của dân tộc Karachay. Ngôi làng nằm ở nơi hai dòng suối hợp thành sông Kuban, còn giữ nhiều nhà gỗ truyền thống và nhà thờ Hồi giáo cổ.",
    "Nằm ở điểm hợp lưu của hai nhánh Uchkulan và Ullu-Kam tạo thành thượng nguồn sông Kuban, Uchkulan cùng với Khurzuk và Kart-Dzhurt được coi là ba ngôi làng gốc, cái nôi lịch sử của dân tộc Karachay. Đây từng là một trong những trung tâm dân cư và văn hoá quan trọng nhất của người Karachay, nơi lưu giữ nếp sống vùng cao truyền thống. Dạo qua làng, du khách bắt gặp những ngôi nhà gỗ và đá cổ nhiều thế hệ, nhà thờ Hồi giáo lâu đời, cùng một trong những trường học đầu tiên của vùng. Khung cảnh làng quê nép mình giữa các sườn núi xanh, bên dòng sông trong vắt, mang lại cảm giác yên bình và đậm bản sắc. Uchkulan là điểm dừng lý tưởng để tìm hiểu văn hoá, kiến trúc dân gian và lịch sử của người Karachay, đồng thời là cửa ngõ hướng về vùng thượng Kuban và chân núi Elbrus.",
    [
        "Một trong ba làng gốc, cái nôi lịch sử của dân tộc Karachay.",
        "Nằm ở nơi hợp lưu hai nhánh sông tạo thành thượng nguồn sông Kuban.",
        "Còn nhiều nhà gỗ - đá cổ, nhà thờ Hồi giáo lâu đời và trường học xưa.",
    ],
    nat_practical(
        "Làng dân cư, tham quan tự do ban ngày quanh năm.",
        "Không thu vé; tôn trọng đời sống và tài sản của người dân.",
        "Khoảng 1–2 giờ dạo làng.",
        "Cuối xuân đến đầu thu (tháng 5–10) khi đường núi thuận lợi.",
        "Ăn mặc lịch sự, xin phép trước khi chụp ảnh người dân; kết hợp thăm làng Khurzuk và vùng thượng Kuban.",
    ),
    [
        {"title": "Wikipedia (RU) — Учкулан", "url": "https://ru.wikipedia.org/wiki/Учкулан"},
    ],
    ["karachay", "traditional-village", "kuban", "ethnography", "mountain-village"],
    maps_text("Учкулан", "Карачаево-Черкесия", "Uchkulan", "Karachay-Cherkessia", 43.45400, 42.09620),
))

# 10) Клухорский перевал -----------------------------------------------------------
RECORDS.append(rec(
    "klukhor-pass",
    "Đèo Klukhor (Klu-kho)",
    "Клухорский перевал",
    "Klukhor Pass",
    ["park_garden"],
    43.24417, 41.86694,
    "Trên dải phân thuỷ chính của dãy Kavkaz, biên giới Karachay-Cherkessia (Nga) với Abkhazia, độ cao ~2.782 m.",
    "Đèo Klukhor là con đèo lịch sử vượt sống núi chính Kavkaz ở độ cao khoảng 2.782 m, nối vùng Teberda với Abkhazia. Đây từng là tuyến đường quân sự Sukhumi cổ và là nơi diễn ra giao tranh ác liệt trong Thế chiến II.",
    "Nằm trên đường phân thuỷ chính của dãy Đại Kavkaz ở độ cao khoảng 2.782 m, đèo Klukhor là một trong những con đèo nổi tiếng và giàu tính lịch sử nhất vùng. Từ xa xưa, đèo đã là mắt xích của Tuyến đường Quân sự Sukhumi (Sukhumi Military Road) nối thượng nguồn Teberda ở phía bắc với Abkhazia bên bờ Biển Đen ở phía nam. Trong Chiến tranh Vệ quốc Vĩ đại, khu vực Klukhor là chiến trường của những trận đánh khốc liệt giành giật các con đèo Kavkaz, và đến nay vẫn còn các đài tưởng niệm, dấu tích công sự nhắc nhớ giai đoạn bi tráng ấy. Cảnh quan quanh đèo là thế giới núi cao điển hình: những đỉnh đá, sông băng và hồ Klukhor xanh lam nằm ngay dưới đèo. Đây là điểm đến của dân trekking ưa thử thách; tuy nhiên do nằm sát biên giới, việc tiếp cận cần lưu ý các quy định về vùng biên.",
    [
        "Đèo lịch sử vượt sống núi chính Kavkaz ở độ cao ~2.782 m.",
        "Nằm trên Tuyến đường Quân sự Sukhumi cổ nối Teberda với Abkhazia.",
        "Chiến trường ác liệt Thế chiến II, còn đài tưởng niệm và hồ Klukhor gần kề.",
    ],
    nat_practical(
        "Điểm núi cao ngoài trời; chỉ tiếp cận được vào mùa hè khi hết tuyết (tháng 7–9).",
        "Không thu vé. " + BORDER,
        "Trekking nhiều ngày từ Teberda/Dombay; riêng đoạn đèo cần cả ngày.",
        "Giữa hè đến đầu thu (tháng 7–9) khi tuyết tan và đường mòn khô ráo.",
        "Địa hình núi cao khắc nghiệt, cần kinh nghiệm trekking, đồ ấm và hướng dẫn viên; chuẩn bị giấy tờ vùng biên giới.",
    ),
    [
        {"title": "Wikipedia (RU) — Клухорский перевал", "url": "https://ru.wikipedia.org/wiki/Клухорский_перевал"},
    ],
    ["mountain-pass", "caucasus", "trekking", "wwii-history", "border-zone", "teberda"],
    maps_text("Клухорский перевал", "Карачаево-Черкесия", "Klukhor Pass", "Karachay-Cherkessia", 43.24417, 41.86694),
))

# 11) Клухорское озеро -------------------------------------------------------------
RECORDS.append(rec(
    "klukhor-lake",
    "Hồ Klukhor (Klu-kho)",
    "Клухорское озеро",
    "Klukhor Lake",
    ["park_garden"],
    43.25230, 41.86310,
    "Ngay dưới đèo Klukhor, thượng nguồn sông Kluhor-Teberda, huyện Karachayevsky, Cộng hoà Karachay-Cherkessia, Nga; độ cao ~2.676 m.",
    "Hồ Klukhor là một hồ băng núi cao tuyệt đẹp nằm ngay dưới đèo cùng tên, ở độ cao khoảng 2.676 m. Mặt nước xanh lam lạnh giá thường có băng trôi ngay cả giữa hè, bao quanh là vách đá và sông băng.",
    "Nằm ngay dưới đèo Klukhor ở độ cao khoảng 2.676 m, hồ Klukhor là một hồ băng - kiến tạo điển hình của vùng núi cao Kavkaz, thuộc thượng nguồn hệ sông Teberda. Hồ được nuôi dưỡng bởi tuyết và sông băng tan chảy, nên nước lạnh buốt và có màu xanh lam đặc trưng; ngay cả giữa mùa hè, những tảng băng vẫn có thể trôi lững lờ trên mặt hồ. Bao quanh là những vách đá dốc đứng và các đỉnh núi phủ tuyết, tạo nên khung cảnh hoang sơ và tĩnh lặng đến choáng ngợp. Hồ nằm trên tuyến trekking cổ vượt đèo Klukhor về phía Abkhazia, nên thường là đích đến hoặc điểm dừng của những chuyến đi bộ đường dài xuất phát từ Teberda hay Dombay. Do độ cao lớn và vị trí sát biên giới, chỉ nên tới đây vào mùa hè và cần chuẩn bị kỹ về thể lực lẫn giấy tờ.",
    [
        "Hồ băng núi cao ở độ cao ~2.676 m, ngay dưới đèo Klukhor.",
        "Nước xanh lam lạnh giá, thường có băng trôi cả giữa mùa hè.",
        "Bao quanh bởi vách đá và sông băng, nằm trên tuyến trekking cổ vượt Kavkaz.",
    ],
    nat_practical(
        "Điểm núi cao ngoài trời; chỉ tới được vào mùa hè (tháng 7–9).",
        "Không thu vé. " + BORDER,
        "Trekking nhiều ngày; riêng chặng lên hồ tốn phần lớn một ngày.",
        "Giữa hè đến đầu thu (tháng 7–9).",
        "Cần kinh nghiệm và thể lực trekking núi cao, đồ ấm, hướng dẫn viên và giấy tờ vùng biên.",
    ),
    [
        {"title": "Wikipedia (RU) — Клухор (озеро)", "url": "https://ru.wikipedia.org/wiki/Клухор_(озеро)"},
    ],
    ["glacial-lake", "high-altitude", "caucasus", "trekking", "teberda", "border-zone"],
    maps_text("Клухорское озеро", "Карачаево-Черкесия", "Klukhor Lake", "Karachay-Cherkessia", 43.25230, 41.86310),
))

# 12) Бадукские озёра --------------------------------------------------------------
RECORDS.append(rec(
    "baduk-lakes",
    "Hồ Baduk (Ba-đúc)",
    "Бадукские озёра",
    "Baduk Lakes",
    ["park_garden"],
    43.37710, 41.65680,
    "Thung lũng sông Baduk, trong Khu bảo tồn thiên nhiên Teberda, huyện Karachayevsky, Cộng hoà Karachay-Cherkessia, Nga; độ cao ~1.930–2.000 m.",
    "Bộ ba hồ Baduk là chuỗi hồ núi màu ngọc lam nằm trong Khu bảo tồn Teberda, hình thành do đá lở chặn dòng suối. Đây là một trong những cung trekking một ngày được yêu thích nhất vùng Teberda - Dombay.",
    "Nằm trong Khu bảo tồn thiên nhiên Teberda ở độ cao khoảng 1.930–2.000 m, các hồ Baduk là một chuỗi ba hồ nhỏ tuyệt đẹp hình thành cách nay vài trăm năm khi những khối đá lở chặn dòng suối Baduk. Nước hồ trong veo, đổi màu từ xanh lam sang ngọc bích tuỳ ánh sáng và độ sâu, phản chiếu rừng thông và những sườn núi bao quanh. Đường mòn lên hồ đi men theo suối Baduk qua rừng lá kim rậm, băng qua cầu gỗ và những đoạn dốc đá, dài khoảng vài giờ đi bộ mỗi chiều - vừa sức cho người có thể lực trung bình khá. Chính sự kết hợp giữa quãng đường không quá dài và phần thưởng là những mặt hồ ngọc bích khiến Baduk trở thành một trong những chuyến trekking trong ngày nổi tiếng nhất khu vực Teberda - Dombay. Vì nằm trong khu bảo tồn, du khách cần mua vé và tuân thủ quy định bảo vệ thiên nhiên.",
    [
        "Chuỗi ba hồ núi màu ngọc lam trong Khu bảo tồn Teberda (độ cao ~1.930–2.000 m).",
        "Hình thành do đá lở chặn dòng suối Baduk, nước đổi màu theo ánh sáng.",
        "Cung trekking một ngày qua rừng lá kim, nổi tiếng và vừa sức.",
    ],
    nat_practical(
        "Đường mòn ngoài trời trong khu bảo tồn; đi ban ngày, mùa ấm (khoảng tháng 6–10).",
        "Có thu phí vào khu bảo tồn Teberda; kiểm tra tại trạm kiểm lâm/cổng.",
        "Khoảng 5–7 giờ cả đi và về (trekking trong ngày).",
        "Đầu hè đến đầu thu (tháng 6–10) khi đường mòn khô, hết tuyết.",
        "Mang giày trekking, nước và đồ ăn nhẹ; đăng ký/mua vé tại trạm kiểm lâm và không rời đường mòn.",
    ),
    [
        {"title": "Wikipedia (RU) — Бадукские озёра", "url": "https://ru.wikipedia.org/wiki/Бадукские_озёра"},
    ],
    ["mountain-lakes", "turquoise", "teberda-reserve", "trekking", "day-hike", "caucasus"],
    maps_text("Бадукские озёра", "Карачаево-Черкесия", "Baduk Lakes", "Karachay-Cherkessia", 43.37710, 41.65680),
))

# 13) Софийские озёра --------------------------------------------------------------
RECORDS.append(rec(
    "sofia-lakes",
    "Hồ Sofia (Xô-phi-a)",
    "Софийские озёра",
    "Sofia Lakes",
    ["park_garden"],
    43.45220, 41.22920,
    "Trên dãy Arkhyz gần núi Sofia, đầu nguồn thung lũng Kizgych/Sofia, huyện Zelenchuksky, Cộng hoà Karachay-Cherkessia, Nga; độ cao ~2.800 m.",
    "Hồ Sofia là cụm hồ băng núi cao nằm ở độ cao khoảng 2.800 m gần đỉnh Sofia trong vùng Arkhyz. Những mặt hồ xanh thẫm dưới chân sống núi đá là một trong những điểm trekking đẹp và nổi tiếng nhất Arkhyz.",
    "Nằm ở độ cao khoảng 2.800 m trên các bậc thềm đá của dãy Arkhyz, gần khối núi Sofia hùng vĩ, cụm hồ Sofia là một trong những điểm đến ngoạn mục nhất của vùng Arkhyz. Đây là những hồ băng - kiến tạo nằm trong các lòng chảo đá do sông băng cổ bào mòn, nước có màu từ xanh lam đến xanh thẫm và lạnh buốt quanh năm. Tuỳ mùa, một số hồ vẫn còn đóng băng hoặc có băng trôi đến tận đầu hè. Khung cảnh nơi đây là sự hoà quyện giữa mặt nước tĩnh lặng, những vách đá dựng và các đỉnh núi phủ tuyết soi bóng, tạo nên bức tranh núi cao gần như hoàn hảo. Đường lên hồ khá dài và dốc, thường mất trọn một ngày trekking hoặc kết hợp đi xe địa hình một phần chặng, nên phù hợp với người có thể lực tốt. Hồ Sofia thường được ghép cùng thác Sofia và thung lũng Sofia trong hành trình khám phá Arkhyz.",
    [
        "Cụm hồ băng núi cao ở độ cao ~2.800 m gần khối núi Sofia.",
        "Nước xanh thẫm, có nơi còn băng đến đầu hè, soi bóng các đỉnh tuyết.",
        "Một trong những cung trekking đẹp và nổi tiếng nhất vùng Arkhyz.",
    ],
    nat_practical(
        "Điểm núi cao ngoài trời; chỉ tới được vào mùa ấm (khoảng tháng 7–9).",
        "Không thu vé cố định; nhiều người thuê xe địa hình (UAZ) đi một phần chặng, có phí.",
        "Thường trọn một ngày (trekking dài hoặc kết hợp xe địa hình).",
        "Giữa hè đến đầu thu (tháng 7–9) khi tuyết tan.",
        "Đường dài và dốc, cần thể lực tốt, đồ ấm, nước; nên đi cùng nhóm/hướng dẫn viên và khởi hành sớm.",
    ),
    [
        {"title": "Tourister.ru — Софийские озёра (Архыз)", "url": "https://www.tourister.ru/world/europe/russia/city/arhyz/placeofinterest"},
    ],
    ["mountain-lakes", "high-altitude", "arkhyz", "sofia", "trekking", "caucasus"],
    maps_text("Софийские озёра", "Архыз", "Sofia Lakes", "Arkhyz", 43.45220, 41.22920),
))

# 14) Медовые водопады -------------------------------------------------------------
RECORDS.append(rec(
    "medovye-honey-waterfalls",
    "Thác Mật ong (Mê-đô-vưi)",
    "Медовые водопады",
    "Honey Waterfalls",
    ["park_garden"],
    43.88360, 42.58640,
    "Hẻm sông Alikonovka và Echki-Bash gần làng Medovka, huyện Malokarachaevsky, Cộng hoà Karachay-Cherkessia, Nga (gần Kislovodsk).",
    "Thác Mật ong là cụm năm thác nước trong một hẻm núi đẹp gần Kislovodsk, thuộc huyện Malokarachaevsky. Đây là điểm dã ngoại nổi tiếng với các thác cao tới hơn 18 m, cầu treo và khung cảnh hẻm đá ngoạn mục.",
    "Nằm trong hẻm của hai dòng sông nhỏ Alikonovka và Echki-Bash ở huyện Malokarachaevsky, sát ranh giới với vùng Kislovodsk, cụm Thác Mật ong (Medovye vodopady) là một trong những điểm tham quan thiên nhiên dễ tiếp cận và được yêu thích nhất phía bắc nước cộng hoà. Quần thể gồm khoảng năm thác nước lớn nhỏ mang những cái tên riêng, trong đó thác cao nhất - Bolshoy Medovy - đổ xuống từ độ cao khoảng 18 m. Theo truyền thuyết dân gian, tên gọi 'mật ong' bắt nguồn từ chuyện ong rừng làm tổ trên vách đá, mật chảy hoà vào dòng nước; một cách giải thích khác gắn với các cặp đôi từng tới đây hưởng 'tuần trăng mật'. Xung quanh thác có đường mòn, cầu treo bắc qua hẻm, các điểm ngắm cảnh và một khu phức hợp du lịch nhỏ với quán ăn, bảo tàng dân tộc học. Nhờ gần Kislovodsk, đây là điểm đến trong ngày lý tưởng, kết hợp ngắm thác, chụp ảnh và thưởng thức ẩm thực Kavkaz.",
    [
        "Cụm khoảng 5 thác trong hẻm núi, thác cao nhất tới ~18 m.",
        "Cầu treo, đường mòn và điểm ngắm cảnh, khu du lịch có bảo tàng dân tộc học.",
        "Gần Kislovodsk, điểm dã ngoại trong ngày dễ tiếp cận và nổi tiếng.",
    ],
    nat_practical(
        "Khu tham quan ngoài trời, mở cửa ban ngày quanh năm.",
        "Có thể thu phí vào khu du lịch/bãi xe (mức thấp).",
        "Khoảng 1,5–2,5 giờ.",
        "Cuối xuân đến đầu thu (tháng 5–10); mùa xuân nước thác mạnh nhất.",
        "Đường xuống hẻm có bậc và có thể trơn; đi giày bám tốt; dễ kết hợp trong tuyến tham quan từ Kislovodsk.",
    ),
    [
        {"title": "Wikipedia (RU) — Медовые водопады", "url": "https://ru.wikipedia.org/wiki/Медовые_водопады"},
    ],
    ["waterfalls", "canyon", "day-trip", "kislovodsk", "nature", "caucasus"],
    maps_text("Медовые водопады", "Карачаево-Черкесия", "Honey Waterfalls", "Karachay-Cherkessia", 43.88360, 42.58640),
))

# 15) Перевал Гумбаши --------------------------------------------------------------
RECORDS.append(rec(
    "gum-bashi-pass",
    "Đèo Gum-Bashi (Gum Ba-si)",
    "Перевал Гумбаши",
    "Gum-Bashi Pass",
    ["park_garden"],
    43.77500, 42.19917,
    "Trên đường nối Karachayevsk với Kislovodsk, huyện Malokarachaevsky, Cộng hoà Karachay-Cherkessia, Nga; độ cao ~2.044 m.",
    "Đèo Gum-Bashi ở độ cao khoảng 2.044 m là điểm ngắm Elbrus nổi tiếng trên đường từ Karachayevsk đi Kislovodsk. Từ đỉnh đèo, du khách được chiêm ngưỡng toàn cảnh dãy Kavkaz và hai đỉnh tuyết Elbrus khi trời quang.",
    "Nằm trên tuyến đường bộ nối Karachayevsk với Kislovodsk, đèo Gum-Bashi ở độ cao khoảng 2.044 m là một trong những điểm ngắm cảnh đẹp và dễ tiếp cận nhất của vùng. Điều làm nên danh tiếng của đèo chính là tầm nhìn: vào những ngày trời trong, từ đây có thể thấy trọn vẹn bức tường của dãy Đại Kavkaz với đỉnh Elbrus hai chóp tuyết sừng sững ở phía chân trời. Con đường lên đèo uốn lượn qua những sườn đồi cỏ xanh mướt mùa hè và phủ tuyết mùa đông, hai bên thường có các quầy bán mật ong, sữa chua (ayran), đồ len và trà thảo mộc của người dân địa phương. Vì có thể tới bằng ô tô, Gum-Bashi trở thành điểm dừng chân quen thuộc để nghỉ ngơi, chụp ảnh toàn cảnh núi non và thưởng thức đặc sản vùng cao. Cảnh mặt trời mọc hay hoàng hôn nhuộm hồng đỉnh Elbrus nhìn từ đèo được nhiều nhiếp ảnh gia săn đón.",
    [
        "Đèo ô tô ở độ cao ~2.044 m trên đường Karachayevsk - Kislovodsk.",
        "Điểm ngắm toàn cảnh dãy Kavkaz và đỉnh Elbrus hai chóp khi trời quang.",
        "Sườn cỏ xanh mùa hè, có quầy bán mật ong, ayran và đồ len địa phương.",
    ],
    nat_practical(
        "Điểm ngắm cảnh ngoài trời bên đường, qua lại tự do quanh năm (mùa đông có thể trơn tuyết).",
        "Không thu vé.",
        "Khoảng 30–60 phút dừng chân ngắm cảnh.",
        "Cuối xuân đến đầu thu để cỏ xanh; sáng sớm/chiều muộn ngắm Elbrus đẹp nhất.",
        "Trời có thể nhiều mây che Elbrus, nên canh ngày quang; mang áo ấm vì trên đèo gió lạnh.",
    ),
    [
        {"title": "Wikipedia (RU) — Гумбаши", "url": "https://ru.wikipedia.org/wiki/Гумбаши"},
    ],
    ["mountain-pass", "viewpoint", "elbrus-view", "scenic-drive", "caucasus"],
    maps_text("Перевал Гумбаши", "Карачаево-Черкесия", "Gum-Bashi Pass", "Karachay-Cherkessia", 43.77500, 42.19917),
))

# 16) Кара-Кёль (Теберда) ----------------------------------------------------------
RECORDS.append(rec(
    "kara-kel-lake-teberda",
    "Hồ Kara-Kel (Ka-ra Kiôl)",
    "Кара-Кёль",
    "Kara-Kel Lake",
    ["park_garden"],
    43.43690, 41.74330,
    "Trong thành phố nghỉ dưỡng Teberda, huyện Karachayevsky, Cộng hoà Karachay-Cherkessia, Nga.",
    "Kara-Kel là hồ tự nhiên nằm ngay trong thị trấn nghỉ dưỡng Teberda, được xem là một trong những hồ ấm và cổ nhất vùng. Mặt hồ tĩnh lặng phản chiếu rừng thông và núi, là nơi dạo chơi, đạp vịt và tắm mát mùa hè.",
    "Khác với các hồ băng lạnh giá trên cao, Kara-Kel (tiếng Karachay nghĩa là 'hồ đen') nằm ngay trong lòng thị trấn nghỉ dưỡng Teberda ở độ cao vừa phải, nên nước ấm hơn và dễ tiếp cận. Hồ có nguồn gốc băng hà cổ, được cho là một trong những hồ lâu đời của vùng Teberda; lớp bùn đáy sẫm màu tạo nên cái tên 'hồ đen'. Vào mùa hè, đây là nơi người dân và du khách tới dạo bộ quanh bờ, chèo thuyền hoặc đạp vịt, thậm chí tắm mát - điều hiếm thấy ở các hồ núi khác trong vùng. Xung quanh hồ là rừng thông, thảm cỏ và các lối đi bộ, với hậu cảnh là những dãy núi của Khu bảo tồn Teberda. Nhờ vị trí thuận tiện và khung cảnh yên bình, Kara-Kel là điểm thư giãn nhẹ nhàng, phù hợp cho gia đình có trẻ nhỏ và là điểm dừng chân dễ chịu trên đường tới Dombay.",
    [
        "Hồ tự nhiên ngay trong thị trấn nghỉ dưỡng Teberda, dễ tiếp cận.",
        "Nước ấm hơn hồ băng, mùa hè có thể chèo thuyền, đạp vịt, tắm mát.",
        "Bao quanh là rừng thông và lối đi bộ, hậu cảnh núi Teberda.",
    ],
    nat_practical(
        "Khu hồ - công viên ngoài trời, mở cửa ban ngày quanh năm.",
        "Vào tự do; dịch vụ thuê thuyền/đạp vịt có phí.",
        "Khoảng 1 giờ dạo quanh hồ.",
        "Mùa hè (tháng 6–9) cho hoạt động dưới nước; các mùa khác vẫn đẹp để dạo bộ.",
        "Điểm dừng nhẹ nhàng phù hợp gia đình; kết hợp thăm khu bảo tồn Teberda và trên đường đi Dombay.",
    ),
    [
        {"title": "EtoKavkaz — Озеро Кара-Кёль (Теберда)", "url": "https://etokavkaz.ru/mesta/ozero-kara-kyol"},
    ],
    ["lake", "teberda", "resort", "family-friendly", "glacial", "relax"],
    maps_text("Озеро Кара-Кёль", "Теберда", "Kara-Kel Lake", "Teberda", 43.43690, 41.74330),
))

# 17) Алибекский водопад -----------------------------------------------------------
RECORDS.append(rec(
    "alibek-waterfall",
    "Thác Alibek (A-li-béc)",
    "Алибекский водопад",
    "Alibek Waterfall",
    ["park_garden"],
    43.29880, 41.55570,
    "Thung lũng Alibek gần Dombay, dưới chân sông băng Alibek, huyện Karachayevsky, Cộng hoà Karachay-Cherkessia, Nga.",
    "Thác Alibek là thác nước hùng vĩ cao khoảng 25 m ở thung lũng Alibek gần Dombay, do dòng chảy từ sông băng Alibek tạo thành. Đây là một trong những cung đi bộ đẹp và phổ biến nhất khu vực Dombay.",
    "Nằm trong thung lũng Alibek gần khu nghỉ Dombay, thác Alibek là một trong những thác nước ấn tượng nhất vùng, được tạo thành từ dòng nước tan chảy của sông băng Alibek đổ qua một bậc đá cao khoảng 25 m. Vào cuối xuân đầu hè, khi băng tuyết tan mạnh, thác cuồn cuộn tung bọt trắng xoá, âm vang cả một góc thung lũng. Đường mòn tới thác đi qua rừng lá kim, đồng cỏ núi và ngang qua hồ băng Turye (Turye Ozero) cùng khu vực sông băng Alibek - một trong những sông băng dễ tiếp cận nhất Kavkaz. Cung đi bộ này dài vừa phải, cảnh quan thay đổi liên tục từ rừng sang thế giới băng đá, nên rất được lòng du khách khi tới Dombay. Vào mùa hè, quanh chân thác thường có hơi nước mát lạnh và cầu vồng nhỏ lấp lánh trong nắng. Đây là lựa chọn tuyệt vời cho một ngày trekking không quá nặng nhưng giàu trải nghiệm.",
    [
        "Thác cao ~25 m ở thung lũng Alibek, tạo bởi nước tan từ sông băng Alibek.",
        "Đường mòn qua rừng lá kim, đồng cỏ, hồ băng Turye và khu sông băng.",
        "Một trong những cung đi bộ trong ngày đẹp và phổ biến nhất Dombay.",
    ],
    nat_practical(
        "Đường mòn ngoài trời, đi ban ngày vào mùa ấm (khoảng tháng 6–10).",
        "Có thể thu phí vào khu bảo tồn/kiểm lâm khu vực Dombay.",
        "Khoảng 4–6 giờ cả đi và về từ Dombay.",
        "Đầu hè đến đầu thu (tháng 6–10); cuối xuân đầu hè thác mạnh nhất.",
        "Mang giày trekking, nước, đồ ấm; kết hợp thăm hồ Turye và sông băng Alibek trên cùng cung đường.",
    ),
    [
        {"title": "Wikipedia (RU) — Алибекский водопад", "url": "https://ru.wikipedia.org/wiki/Алибекский_водопад"},
    ],
    ["waterfall", "glacier", "dombay", "trekking", "day-hike", "caucasus"],
    maps_text("Алибекский водопад", "Домбай", "Alibek Waterfall", "Dombay", 43.29880, 41.55570),
))

# 18) Каньон Аманауз ---------------------------------------------------------------
RECORDS.append(rec(
    "amanauz-canyon",
    "Hẻm Amanauz (A-ma-na-uz)",
    "Каньон Аманауз",
    "Amanauz Canyon",
    ["park_garden"],
    43.27740, 41.61947,
    "Thung lũng sông Amanauz ngay phía trên khu nghỉ Dombay, huyện Karachayevsky, Cộng hoà Karachay-Cherkessia, Nga.",
    "Hẻm Amanauz là một hẻm núi sâu và hẹp ngay sát Dombay, nơi dòng sông Amanauz gầm réo qua các khe đá. Điểm nhấn là 'Cối xay của Quỷ' - đoạn nước xoáy dữ dội giữa vách đá, cùng các thác nhỏ.",
    "Chỉ cách trung tâm khu nghỉ Dombay một quãng đi bộ ngắn, hẻm Amanauz là điểm khám phá thiên nhiên hấp dẫn dành cho cả những du khách không muốn đi trekking quá xa. Con sông Amanauz - có tên nghĩa gần với 'miệng dữ' trong tiếng địa phương - đã bào xẻ vào lòng núi tạo thành một hẻm sâu, hẹp với vách đá dựng đứng. Đoạn nổi tiếng nhất là 'Chyortova Melnitsa' (Cối xay của Quỷ), nơi dòng nước bị nén lại giữa hai vách đá rồi xoáy cuộn, tung bọt trắng và gầm vang dữ dội. Dọc hẻm còn có các thác nhỏ, các điểm ngắm và những tảng đá khổng lồ. Đường mòn men theo bờ sông qua rừng thông, tương đối dễ đi ở đoạn đầu nhưng trở nên hiểm trở hơn khi tiến sâu vào hẻm. Với khoảng cách gần Dombay và khung cảnh vừa hùng vĩ vừa dữ dội, Amanauz là lựa chọn lý tưởng cho một buổi dạo bộ nửa ngày giàu ấn tượng.",
    [
        "Hẻm núi sâu, hẹp ngay sát Dombay, dễ tiếp cận bằng đi bộ.",
        "Điểm nhấn 'Cối xay của Quỷ' - nước xoáy dữ dội giữa vách đá.",
        "Đường mòn ven sông qua rừng thông, có nhiều thác nhỏ và điểm ngắm.",
    ],
    nat_practical(
        "Đường mòn ngoài trời, đi ban ngày vào mùa ấm (khoảng tháng 6–10).",
        "Vào tự do; có thể thu phí khu bảo tồn ở một số điểm.",
        "Khoảng 2–4 giờ tuỳ đi sâu vào hẻm.",
        "Đầu hè đến đầu thu (tháng 6–10) khi đường khô ráo.",
        "Đoạn sâu trong hẻm hiểm trở và trơn, cần thận trọng, giày bám tốt; không lại gần mép nước xoáy.",
    ),
    [
        {"title": "Tourister.ru — Каньон Аманауз (Домбай)", "url": "https://www.tourister.ru/world/europe/russia/city/dombaj/placeofinterest"},
    ],
    ["canyon", "river", "dombay", "waterfall", "day-hike", "caucasus"],
    maps_text("Каньон Аманауз", "Домбай", "Amanauz Canyon", "Dombay", 43.27740, 41.61947),
))

# 19) Муруджинские озёра -----------------------------------------------------------
RECORDS.append(rec(
    "muruzhu-lakes",
    "Hồ Muruzhu (Mu-ru-giu)",
    "Муруджинские озёра",
    "Muruzhu Lakes",
    ["park_garden"],
    43.32300, 41.77070,
    "Thượng nguồn sông Muruzhu (nhánh sông Uchkulan/Daut), huyện Karachayevsky, Cộng hoà Karachay-Cherkessia, Nga; độ cao ~2.800–3.000 m.",
    "Hồ Muruzhu là cặp hồ núi cao nổi tiếng với hai màu tương phản: một hồ Xanh lam và một hồ Đen. Nằm ở độ cao gần 3.000 m giữa vùng núi hoang sơ, đây là đích đến của những chuyến trekking dài đầy thử thách.",
    "Ẩn mình ở độ cao khoảng 2.800–3.000 m trong vùng núi hoang sơ phía đông Teberda - Dombay, cụm hồ Muruzhu nổi tiếng nhất với hai hồ có màu nước tương phản kỳ lạ: 'Hồ Xanh' (Goluboye) với nước xanh lam trong vắt và 'Hồ Đen' (Chornoye) sẫm màu bí ẩn nằm cách nhau không xa. Sự khác biệt màu sắc đến từ độ sâu, đáy hồ và cách ánh sáng phản chiếu, tạo nên một trong những cảnh quan hồ núi độc đáo nhất Kavkaz. Đây là những hồ băng - kiến tạo, nước lạnh giá và trong đến mức có thể nhìn thấu đáy ở vùng nông. Đường tới hồ dài, dốc và ít dấu chân người, đòi hỏi nhiều giờ, thậm chí nhiều ngày trekking qua các thung lũng và sườn núi, nên Muruzhu là phần thưởng dành cho những người ưa mạo hiểm và có kinh nghiệm đi núi. Khung cảnh tĩnh lặng, gần như nguyên sơ khiến nơi đây trở thành điểm đến trong mơ của dân trekking và nhiếp ảnh phong cảnh.",
    [
        "Cặp hồ núi cao nổi tiếng với 'Hồ Xanh' và 'Hồ Đen' màu tương phản.",
        "Nằm ở độ cao gần 3.000 m giữa vùng núi hoang sơ, nước băng trong vắt.",
        "Đích đến của các chuyến trekking dài, thử thách, ít dấu chân người.",
    ],
    nat_practical(
        "Điểm núi cao ngoài trời; chỉ tới được vào mùa hè (khoảng tháng 7–9).",
        "Không thu vé cố định; có thể qua khu vực thu phí kiểm lâm.",
        "Trekking dài, thường nhiều ngày hoặc trọn một ngày rất dài.",
        "Giữa hè đến đầu thu (tháng 7–9) khi tuyết tan.",
        "Cung khó, cần kinh nghiệm trekking, thể lực tốt, đồ cắm trại và hướng dẫn viên rành đường.",
    ),
    [
        {"title": "Tripplanet — Достопримечательности Карачаево-Черкесии", "url": "https://tripplanet.ru/dostoprimechatelnosti-karachaevo-cherkesii/"},
    ],
    ["mountain-lakes", "high-altitude", "blue-lake", "trekking", "wilderness", "caucasus"],
    maps_text("Муруджинские озёра", "Карачаево-Черкесия", "Muruzhu Lakes", "Karachay-Cherkessia", 43.32300, 41.77070),
))

# 20) Чучхурский водопад -----------------------------------------------------------
RECORDS.append(rec(
    "chuchkhur-waterfall",
    "Thác Chuchkhur (Chuc-khu)",
    "Чучхурский водопад",
    "Chuchkhur Waterfall",
    ["park_garden"],
    43.26530, 41.69140,
    "Thung lũng Dombay-Yolgen phía trên khu nghỉ Dombay, huyện Karachayevsky, Cộng hoà Karachay-Cherkessia, Nga.",
    "Thác Chuchkhur là thác nước nhiều bậc trên suối Chuchkhur ở thung lũng phía trên Dombay. Nước từ sông băng đổ qua các bậc đá cao tổng cộng vài chục mét, giữa khung cảnh đồng cỏ núi và các đỉnh tuyết.",
    "Nằm trong thung lũng Dombay-Yolgen phía trên khu nghỉ Dombay, thác Chuchkhur là một trong những đích đến trekking trong ngày quen thuộc của du khách. Dòng suối Chuchkhur, được nuôi bởi tuyết và băng tan từ các sườn núi cao, đổ xuống qua nhiều bậc đá tạo thành một thác nước cao tổng cộng vài chục mét, tung bọt trắng giữa nền đá xám và cỏ xanh. Đường mòn tới thác đi từ thung lũng Dombay qua những đồng cỏ núi rộng, băng qua suối và ngang các điểm ngắm nhìn ra đỉnh Belalakaya sọc trắng cùng nhiều đỉnh tuyết khác. Cung đường tương đối vừa sức, cảnh quan thoáng đãng, nên phù hợp cả với những nhóm gia đình có thể lực trung bình. Vào mùa hè, đồng cỏ nở đầy hoa dại, còn dòng thác mát lạnh là nơi nghỉ chân lý tưởng. Chuchkhur thường được kết hợp cùng các cung đi bộ khác quanh Dombay trong hành trình khám phá vùng núi.",
    [
        "Thác nhiều bậc cao tổng cộng vài chục mét trên suối Chuchkhur.",
        "Đường mòn qua đồng cỏ núi, ngắm đỉnh Belalakaya và các đỉnh tuyết.",
        "Cung trekking trong ngày vừa sức, phổ biến quanh Dombay.",
    ],
    nat_practical(
        "Đường mòn ngoài trời, đi ban ngày vào mùa ấm (khoảng tháng 6–10).",
        "Có thể thu phí vào khu bảo tồn khu vực Dombay.",
        "Khoảng 4–6 giờ cả đi và về từ Dombay.",
        "Đầu hè đến đầu thu (tháng 6–10); mùa hè đồng cỏ nhiều hoa.",
        "Mang giày trekking, nước, kem chống nắng; kết hợp các cung đi bộ khác quanh Dombay.",
    ),
    [
        {"title": "Tourister.ru — Чучхурский водопад (Домбай)", "url": "https://www.tourister.ru/world/europe/russia/city/dombaj/placeofinterest"},
    ],
    ["waterfall", "dombay", "alpine-meadow", "trekking", "day-hike", "caucasus"],
    maps_text("Чучхурский водопад", "Домбай", "Chuchkhur Waterfall", "Dombay", 43.26530, 41.69140),
))

# 21) Гоначхирское ущелье ----------------------------------------------------------
RECORDS.append(rec(
    "gonachkhir-gorge",
    "Hẻm Gonachkhir (Gô-nác-khia)",
    "Гоначхирское ущелье",
    "Gonachkhir Gorge",
    ["park_garden"],
    43.28520, 41.79290,
    "Thung lũng sông Gonachkhir trên đường từ Teberda tới đèo Klukhor, Khu bảo tồn Teberda, huyện Karachayevsky, Cộng hoà Karachay-Cherkessia, Nga.",
    "Hẻm Gonachkhir là một thung lũng núi tuyệt đẹp trên đường từ Teberda về phía đèo Klukhor, trong Khu bảo tồn Teberda. Điểm nhấn là hồ Tumanly-Kel (hồ Cá hồi) xanh biếc soi bóng rừng lá kim và núi tuyết.",
    "Con đường từ Teberda hướng về đèo Klukhor luồn qua hẻm Gonachkhir - một thung lũng hẹp, sâu nằm trong Khu bảo tồn thiên nhiên Teberda, hai bên là những sườn núi phủ rừng lá kim rậm rạp và các đỉnh đá dựng đứng. Dòng sông Gonachkhir trong vắt chảy dọc thung lũng, còn viên ngọc của khu vực là hồ Tumanly-Kel (còn gọi là hồ Forelnoye - 'hồ Cá hồi'), một hồ nhỏ nước xanh biếc soi bóng rừng thông và núi tuyết, đẹp như tranh vẽ. Vào mùa thu, cả thung lũng chuyển sang sắc vàng đỏ rực rỡ, biến Gonachkhir thành một trong những nơi ngắm lá vàng đẹp nhất vùng. Vì có đường xe chạy qua, du khách có thể dễ dàng dừng lại ngắm cảnh, chụp ảnh bên hồ mà không cần trekking vất vả. Tuy nhiên do nằm trong khu bảo tồn và hướng ra vùng biên giới, việc đi sâu về phía đèo Klukhor cần tuân thủ quy định và có thể cần giấy phép.",
    [
        "Thung lũng núi đẹp trên đường Teberda - đèo Klukhor, trong Khu bảo tồn Teberda.",
        "Điểm nhấn hồ Tumanly-Kel (hồ Cá hồi) xanh biếc soi bóng rừng và núi tuyết.",
        "Mùa thu lá vàng đỏ rực rỡ, dễ tiếp cận bằng đường ô tô.",
    ],
    nat_practical(
        "Thung lũng ngoài trời trong khu bảo tồn; tham quan ban ngày mùa ấm (tháng 6–10).",
        "Có thu phí vào khu bảo tồn Teberda. " + BORDER,
        "Khoảng 1–2 giờ dừng ngắm cảnh (không kể trekking sâu).",
        "Cuối hè đến giữa thu (tháng 8–10) cho mùa lá vàng; mùa hè cảnh xanh mát.",
        "Tuân thủ quy định khu bảo tồn, không xả rác; hỏi trước về giấy phép nếu đi sâu về phía đèo Klukhor.",
    ),
    [
        {"title": "Tourister.ru — Гоначхирское ущелье", "url": "https://www.tourister.ru/world/europe/russia/city/teberda/placeofinterest"},
    ],
    ["gorge", "lake", "teberda-reserve", "autumn-foliage", "scenic-drive", "caucasus"],
    maps_text("Гоначхирское ущелье", "Карачаево-Черкесия", "Gonachkhir Gorge", "Karachay-Cherkessia", 43.28520, 41.79290),
))

# 22) Пик Домбай-Ульген ------------------------------------------------------------
RECORDS.append(rec(
    "dombay-ulgen-peak",
    "Đỉnh Dombay-Ulgen (Đôm-bai Un-ghen)",
    "Домбай-Ульген",
    "Dombay-Ulgen Peak",
    ["park_garden"],
    43.24310, 41.72780,
    "Trên sống núi chính Kavkaz, biên giới Karachay-Cherkessia (Nga) với Abkhazia, huyện Karachayevsky, Nga; độ cao ~4.046 m.",
    "Dombay-Ulgen là đỉnh núi cao nhất của vùng Tây Kavkaz, khoảng 4.046 m. Khối núi tuyết hùng vĩ này là biểu tượng của Dombay và là mục tiêu mơ ước của giới leo núi chuyên nghiệp.",
    "Vươn lên độ cao khoảng 4.046 m, Dombay-Ulgen (theo truyền thuyết địa phương nghĩa gần với 'nơi con bò rừng chết') là đỉnh cao nhất của toàn bộ vùng Tây Kavkaz và là biểu tượng thiên nhiên của khu nghỉ Dombay. Khối núi khổng lồ với các sườn dốc đứng phủ băng tuyết vĩnh cửu, những sông băng treo và vách đá hiểm trở, nằm ngay trên đường phân thuỷ chính - biên giới giữa Nga và Abkhazia. Với du khách phổ thông, Dombay-Ulgen chủ yếu là đối tượng để chiêm ngưỡng và chụp ảnh từ xa: từ sườn núi Mussa-Achitara (nơi cáp treo Dombay đưa lên) hay từ các điểm ngắm trong thung lũng, đỉnh núi hiện ra sừng sững, thường được mây và tuyết bao phủ. Với giới leo núi, đây là một trong những mục tiêu danh giá nhưng đầy thách thức của Kavkaz, đòi hỏi kỹ thuật và kinh nghiệm cao. Chính sự hùng vĩ của Dombay-Ulgen đã góp phần làm nên danh tiếng của cả vùng Dombay.",
    [
        "Đỉnh cao nhất vùng Tây Kavkaz (~4.046 m), biểu tượng của Dombay.",
        "Khối núi băng tuyết vĩnh cửu với sông băng treo, trên biên giới Nga - Abkhazia.",
        "Ngắm đẹp từ sườn Mussa-Achitara; mục tiêu leo núi kỹ thuật cao.",
    ],
    nat_practical(
        "Đỉnh núi cao; ngắm cảnh quanh năm từ Dombay, leo núi chỉ dành cho dân chuyên nghiệp.",
        "Không thu vé để ngắm; leo núi cần tổ chức chuyên nghiệp. " + BORDER,
        "Ngắm cảnh vài chục phút; leo đỉnh là hành trình nhiều ngày cho người có kỹ thuật.",
        "Mùa hè cho leo núi; mùa đông và các mùa khác đều ngắm đẹp từ cáp treo Dombay.",
        "Không tự ý leo nếu thiếu kinh nghiệm; ngắm đỉnh đẹp nhất từ sườn Mussa-Achitara qua cáp treo.",
    ),
    [
        {"title": "Wikipedia (RU) — Домбай-Ульген", "url": "https://ru.wikipedia.org/wiki/Домбай-Ульген"},
    ],
    ["peak", "mountaineering", "dombay", "glacier", "highest-point", "caucasus"],
    maps_text("Домбай-Ульген", "Домбай", "Dombay-Ulgen Peak", "Karachay-Cherkessia", 43.24310, 41.72780),
))

# 23) Джемагатское ущелье ----------------------------------------------------------
RECORDS.append(rec(
    "dzhamagat-gorge",
    "Hẻm Dzhamagat và suối khoáng narzan (Gia-ma-gát)",
    "Джемагатское ущелье",
    "Dzhamagat Gorge",
    ["park_garden"],
    43.48410, 41.75210,
    "Thung lũng sông Dzhamagat gần thị trấn Teberda, huyện Karachayevsky, Cộng hoà Karachay-Cherkessia, Nga.",
    "Hẻm Dzhamagat gần Teberda nổi tiếng với các mạch suối khoáng narzan tự nhiên và phế tích một ngôi làng Karachay cổ. Thung lũng xanh mát này là điểm trekking và chữa lành quen thuộc của vùng.",
    "Mở ra ngay gần thị trấn Teberda, hẻm Dzhamagat là một thung lũng núi xanh mát gắn với cả thiên nhiên lẫn lịch sử của người Karachay. Trong thung lũng có những mạch suối khoáng narzan tự nhiên phun trào từ lòng đất - loại nước khoáng có ga giàu khoáng chất mà người dân tin là tốt cho sức khoẻ, khiến nơi đây từ lâu đã là điểm đến để 'uống nước và dưỡng bệnh'. Cũng tại thung lũng này còn có phế tích của một ngôi làng Karachay cổ (aul Dzhamagat/Jamagat) từng bị bỏ hoang sau dịch bệnh, được nhắc tới trong thi ca và truyền thuyết địa phương, phủ lên cảnh quan một màu sắc hoài niệm. Đường mòn men theo suối đi qua rừng và đồng cỏ, với hậu cảnh là những đỉnh núi của khu vực Teberda. Nhờ khoảng cách gần Teberda và địa hình vừa phải, Dzhamagat là lựa chọn tốt cho một chuyến đi bộ nhẹ nhàng kết hợp thưởng thức nước khoáng và tìm hiểu văn hoá vùng cao.",
    [
        "Nhiều mạch suối khoáng narzan tự nhiên, điểm 'dưỡng bệnh' truyền thống.",
        "Phế tích làng Karachay cổ gắn với truyền thuyết và thi ca địa phương.",
        "Thung lũng xanh mát gần Teberda, đường mòn vừa sức ven suối.",
    ],
    nat_practical(
        "Thung lũng ngoài trời, đi ban ngày vào mùa ấm (khoảng tháng 5–10).",
        "Vào tự do; có thể qua khu vực thu phí kiểm lâm.",
        "Khoảng 3–5 giờ cả đi và về.",
        "Cuối xuân đến đầu thu (tháng 5–10) khi đường khô ráo.",
        "Mang bình để nếm nước narzan; giày bám tốt; kết hợp thăm thị trấn Teberda và khu bảo tồn.",
    ),
    [
        {"title": "Wikipedia (RU) — Джемагат", "url": "https://ru.wikipedia.org/wiki/Джемагат"},
    ],
    ["gorge", "mineral-springs", "narzan", "teberda", "karachay-history", "trekking"],
    maps_text("Джемагатское ущелье", "Теберда", "Dzhamagat Gorge", "Teberda", 43.48410, 41.75210),
))

# 24) Парк «Зелёный остров» (Черкесск) ---------------------------------------------
RECORDS.append(rec(
    "green-island-park-cherkessk",
    "Công viên Đảo Xanh (Chéc-két)",
    "Парк «Зелёный остров»",
    "Green Island Park (Cherkessk)",
    ["park_garden"],
    44.23460, 42.03590,
    "Trên một cù lao sông Kuban, thành phố Cherkessk, thủ phủ Cộng hoà Karachay-Cherkessia, Nga.",
    "Đảo Xanh là công viên giải trí lớn nằm trên một cù lao sông Kuban ở Cherkessk. Nơi đây có hồ nước, khu vui chơi, các tiểu cảnh và là điểm dạo chơi, nghỉ ngơi được người dân thủ phủ yêu thích.",
    "Nằm trên một cù lao giữa dòng sông Kuban ngay trong lòng thành phố Cherkessk, công viên 'Zelyony Ostrov' (Đảo Xanh) là không gian nghỉ ngơi - giải trí lớn và được yêu thích bậc nhất của thủ phủ nước cộng hoà. Công viên trải rộng với nhiều mảng cây xanh, hồ nước, đài phun và các lối đi dạo bộ, xen kẽ là khu vui chơi có các trò cảm giác mạnh, sân chơi trẻ em, quán cà phê và những tiểu cảnh trang trí đầy màu sắc. Đây là nơi các gia đình, cặp đôi và du khách tìm đến để thư giãn, đạp xe, chèo thuyền trên hồ hay đơn giản là tản bộ dưới bóng cây, đặc biệt vào những buổi chiều mùa hè oi ả. Vào các dịp lễ hội, công viên thường tổ chức sự kiện, biểu diễn và trò chơi, trở thành trung tâm đời sống cộng đồng của Cherkessk. Với vị trí trung tâm và không khí trong lành bên sông, Đảo Xanh là điểm dừng dễ chịu để cân bằng lại nhịp sống trước hoặc sau những chuyến lên núi.",
    [
        "Công viên giải trí lớn trên cù lao sông Kuban giữa lòng Cherkessk.",
        "Có hồ nước, đài phun, khu vui chơi, quán cà phê và nhiều tiểu cảnh.",
        "Điểm dạo chơi, thư giãn quen thuộc của người dân và du khách thủ phủ.",
    ],
    nat_practical(
        "Công viên mở cửa hằng ngày, thường từ sáng tới tối muộn.",
        "Vào cửa tự do; các trò chơi và dịch vụ (thuyền, đu quay...) tính phí riêng.",
        "Khoảng 1–2 giờ.",
        "Quanh năm; đẹp và nhộn nhịp nhất vào chiều tối mùa hè và dịp lễ hội.",
        "Điểm nghỉ ngơi phù hợp gia đình; kết hợp dạo trung tâm Cherkessk, nhà thờ Thánh Nikolai và bảo tàng.",
    ),
    [
        {"title": "Wikipedia (RU) — Черкесск", "url": "https://ru.wikipedia.org/wiki/Черкесск"},
    ],
    ["city-park", "cherkessk", "kuban", "recreation", "family-friendly"],
    maps_text("Парк Зелёный остров", "Черкесск", "Green Island Park", "Cherkessk", 44.23460, 42.03590),
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
