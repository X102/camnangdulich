# -*- coding: utf-8 -*-
"""_add_places_khakassia_20260728_2.py — VÙNG: Cộng hoà Khakassia (Республика Хакасия)
(lần chạy tự động 2026-07-28).

Bối cảnh: khakassia.json hiện có 7 địa điểm. Bổ sung 23 địa điểm THẬT SỰ nổi tiếng/đặc sắc
còn thiếu, đa dạng loại hình → đưa vùng lên 30.

Phân bố loại hình (23 bản ghi mới):
- park_garden (9): Заповедник «Хакасский», hồ Шира, Белё, Тус, Иткуль, Ханкуль,
  Парк «Сады мечты», Хакасский зоопарк, Парк культуры и отдыха (Абакан).
- monument (4) + kèm: Боярская писаница, Малая Сыя, Сулекская писаница, Сафроновский
  могильник; + Парк Победы (monument+park_garden); + Оглахты (fortress+monument);
  + Саяно-Шушенская ГЭС (other+monument).
- fortress (1, kèm Оглахты): thành/pháo đài khảo cổ trên núi Оглахты.
- other (3): Саяно-Шушенская ГЭС, ГЛК «Гладенькая», Бородинская пещера.
- museum (1): Хакасский нац. краеведческий музей им. Л.Р. Кызласова.
- theatre (2): Хакасский нац. драмтеатр им. А.М. Топанова, Русский драмтеатр им. Лермонтова.
- church (2): Никольский храм (Абакан), храм Св. Константина и Елены (Абакан).

TOẠ ĐỘ — xác minh chéo qua ru.wikipedia (geohack/infobox), Wikidata, 2GIS, Yandex Maps org,
khakassia.travel (cổng du lịch chính thức), gpx.su (2026-07-28). Phạm vi Khakassia: lat
~51,0–55,5; lon ~88,0–91,5 (Abakan ~53,72; 91,44) — tất cả toạ độ nằm trong phạm vi, KHÔNG
đảo lat/lon. Toạ độ cơ sở đô thị (bảo tàng, nhà hát, nhà thờ, công viên) lấy theo marker
tổ chức của 2GIS/Yandex; đối tượng tự nhiên/khảo cổ lấy điểm đại diện.

GHI CHÚ: Hai hồ Матарак và Сарат (Ширинский) KHÔNG xác minh được toạ độ số tin cậy nên đã
BỎ QUA (không nhồi toạ độ bịa). Vùng vẫn đạt mục tiêu 30 mà không cần chúng.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_khakassia_20260728_2.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "khakassia"
REGION_NAME_VI = "Cộng hoà Khakassia"
FD = "Vùng Siberia"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=15",
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


def outdoor_practical(hours, ticket, duration, best, tips):
    return {
        "hours_vi": hours,
        "ticket_vi": ticket,
        "duration_vi": duration,
        "best_time_vi": best,
        "tips_vi": tips,
    }


RECORDS = []

# 1) Заповедник «Хакасский» -------------------------------------------------------
RECORDS.append(rec(
    "khakassky-nature-reserve",
    "Khu bảo tồn thiên nhiên Khakassky (Kha-ka-xki Da-pô-viét-nhích)",
    "Государственный природный заповедник «Хакасский»",
    "Khakassky State Nature Reserve",
    ["park_garden"],
    53.695379, 91.418552,
    "Trụ sở quản lý tại đường Tsukanovoy 164, thành phố Abakan; các phân khu rải rác khắp Cộng hoà Khakassia, Nga.",
    "Khakassky là khu bảo tồn thiên nhiên quốc gia bảo vệ hai hệ sinh thái đặc trưng của Khakassia: thảo nguyên khô hạn với vô số hồ và gò mộ cổ, cùng vùng rừng taiga núi cao Tây Sayan. Khu gồm nhiều phân khu tách biệt, trong đó có Oglakhty và các hồ Itkul, Belyo.",
    "Được thành lập năm 1999 trên cơ sở gộp các khu bảo tồn có sẵn, «Khakassky» là khu bảo tồn thiên nhiên liên bang lớn nhất của Cộng hoà Khakassia, trải rộng qua nhiều phân khu (кластер) không liền nhau. Điểm độc đáo là nó ôm trọn hai thế giới hoàn toàn khác biệt: nhóm phân khu thảo nguyên phía bắc quanh vùng hồ Shirinsky với những đồng cỏ khô, hồ nước mặn - nước ngọt xen kẽ, gò mộ và bãi khắc đá của người cổ; và nhóm phân khu miền núi phía nam với rừng taiga, tuyết tùng, sông suối và đỉnh cao của dãy Tây Sayan. Hệ động vật phong phú gồm cừu núi argali, báo tuyết (ở phần núi), nhiều loài chim nước quý tụ về các hồ vào mùa di cư. Nhiều phân khu như Oglakhty còn là kho tàng khảo cổ ngoài trời với tranh khắc đá và mộ táng hàng nghìn năm tuổi. Khu bảo tồn có trung tâm quản lý và bộ phận giáo dục môi trường tại Abakan, tổ chức các tuyến sinh thái có kiểm soát; phần lớn diện tích lõi cần xin phép mới được vào.",
    [
        "Khu bảo tồn liên bang lớn nhất Khakassia, gồm nhiều phân khu thảo nguyên và núi taiga.",
        "Bảo vệ hệ hồ - thảo nguyên với gò mộ, khắc đá cổ và hệ chim nước di cư.",
        "Ôm trọn hai hệ sinh thái tương phản: thảo nguyên khô hạn và rừng núi Tây Sayan.",
    ],
    outdoor_practical(
        "Trung tâm quản lý tại Abakan làm việc giờ hành chính các ngày trong tuần; các tuyến sinh thái mở theo mùa.",
        "Vào các phân khu lõi phải xin phép và thường đi cùng hướng dẫn viên; một số tuyến sinh thái thu phí tượng trưng.",
        "Từ nửa ngày đến vài ngày tuỳ phân khu và tuyến tham quan.",
        "Tháng 5–9 cho phân khu thảo nguyên và hồ; mùa hè cho phần núi taiga.",
        "Liên hệ trước với ban quản lý để đăng ký tuyến và xin phép; tuân thủ nghiêm quy định bảo tồn, không rời tuyến, không mang theo thú nuôi.",
    ),
    [
        {"title": "Wikipedia (RU) — Хакасский заповедник", "url": "https://ru.wikipedia.org/wiki/Хакасский_заповедник"},
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
    ],
    ["nature-reserve", "steppe", "taiga", "lakes", "protected-area", "khakassia"],
    maps_text("Заповедник Хакасский", "Абакан", "Khakassky Nature Reserve", "Abakan", 53.695379, 91.418552),
    official_site="https://zapovednik-khakassky.ru",
))

# 2) Озеро Шира -------------------------------------------------------------------
RECORDS.append(rec(
    "lake-shira",
    "Hồ Shira (Ô-di-rô Si-ra)",
    "Озеро Шира",
    "Lake Shira",
    ["park_garden"],
    54.50675, 90.21048,
    "Huyện Shirinsky, gần thị trấn nghỉ dưỡng Zhemchuzhny, Cộng hoà Khakassia, Nga.",
    "Hồ Shira là hồ nước khoáng - mặn nổi tiếng bậc nhất Khakassia và là trung tâm nghỉ dưỡng lâu đời của vùng. Nước hồ giàu khoáng chất cùng lớp bùn đáy được dùng chữa bệnh, thu hút du khách về tắm và điều dưỡng suốt mùa hè.",
    "Nằm giữa vùng thảo nguyên hồ ở phía bắc Khakassia, Shira là một trong những hồ nổi tiếng và đông khách nhất nước cộng hoà. Đây là hồ không có dòng chảy ra, nước lợ - khoáng với độ mặn vừa phải, giàu sunfat và muối khoáng; kết hợp với lớp bùn đáy có tính chữa bệnh, hồ đã trở thành nơi điều dưỡng từ cuối thế kỷ 19 và được biết đến rộng rãi thời Xô Viết với khu an dưỡng «Shira». Bờ hồ thoải, đáy cát, nước ấm nhanh vào mùa hè nên rất thích hợp để tắm; nhiều người ngâm mình rồi đắp bùn theo lối trị liệu dân gian. Quanh hồ là chuỗi khu nghỉ, bãi cắm trại, nhà nghỉ và dịch vụ du lịch bình dân, đặc biệt nhộn nhịp vào tháng 7–8. Cảnh quan thảo nguyên thoáng đãng, hoàng hôn trải dài trên mặt nước và không khí khô mát khiến Shira được ví như «biển nhỏ» của Siberia. Từ đây, du khách dễ dàng kết hợp khám phá các hồ lân cận, gò mộ cổ và các phân khu của khu bảo tồn Khakassky.",
    [
        "Hồ khoáng - mặn nổi tiếng nhất Khakassia, trung tâm nghỉ dưỡng lâu đời của vùng.",
        "Nước và bùn đáy giàu khoáng, được dùng để tắm và điều dưỡng chữa bệnh.",
        "Bờ cát thoải, nước ấm nhanh, sôi động du khách vào mùa hè - «biển nhỏ» của thảo nguyên.",
    ],
    outdoor_practical(
        "Hồ mở tự do quanh năm; mùa tắm và dịch vụ nghỉ dưỡng chủ yếu từ tháng 6 đến cuối tháng 8.",
        "Tắm hồ nhìn chung miễn phí; các bãi tắm có dịch vụ, khu an dưỡng và chỗ ở thu phí riêng.",
        "Từ nửa ngày dạo chơi đến vài ngày nghỉ dưỡng.",
        "Tháng 7–8 khi nước ấm nhất; đầu thu vắng vẻ, thảo nguyên đẹp.",
        "Uống đủ nước và che nắng vì thảo nguyên nắng gắt; hỏi ý kiến bác sĩ trước khi trị liệu bằng bùn nếu có bệnh nền.",
    ),
    [
        {"title": "Wikipedia (RU) — Шира (озеро)", "url": "https://ru.wikipedia.org/wiki/Шира_(озеро)"},
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
    ],
    ["lake", "resort", "mineral-water", "steppe", "shirinsky", "khakassia"],
    maps_text("Озеро Шира", "Ширинский район", "Lake Shira", "Shirinsky District", 54.50675, 90.21048),
))

# 3) Озеро Белё -------------------------------------------------------------------
RECORDS.append(rec(
    "lake-belyo",
    "Hồ Belyo (Ô-di-rô Bê-lê)",
    "Озеро Белё",
    "Lake Belyo",
    ["park_garden"],
    54.653193, 90.120543,
    "Huyện Shirinsky, phía bắc Cộng hoà Khakassia, Nga.",
    "Belyo là hồ lớn nhất Khakassia, một hồ nước khoáng - mặn chia thành hai phần thông nhau. Với mặt nước rộng, bãi bờ đa dạng và nước ấm, đây là điểm cắm trại, tắm và nghỉ dưỡng hè được nhiều gia đình yêu thích.",
    "Belyo (còn viết Bele) là hồ có diện tích mặt nước lớn nhất Cộng hoà Khakassia, nằm giữa vùng thảo nguyên hồ phía bắc. Hồ gồm hai phần - Bolshoe Belyo và Maloe Belyo - nối với nhau qua một eo hẹp, có độ mặn và độ khoáng khác nhau, nước lợ giàu muối và vi khoáng. Nhờ diện rộng và độ sâu đáng kể, mặt hồ thường lộng gió, tạo sóng nên được dân chơi thuyền buồm, ván diều ưa chuộng; đồng thời nhiều vịnh kín gió lại có bãi thoải, nước ấm, lý tưởng cho gia đình tắm và cắm trại. Vào mùa hè, bờ hồ mọc lên các khu lều trại, nhà nghỉ và điểm dịch vụ, trở thành một trong những bãi nghỉ đông vui nhất vùng. Cảnh quan quanh hồ mang vẻ đẹp thảo nguyên khoáng đạt: đồi cỏ thấp, trời cao và đường chân trời trải dài. Cùng với Shira và Itkul, Belyo tạo thành cụm hồ du lịch trứ danh của huyện Shirinsky, thuận tiện kết hợp tham quan gò mộ, khắc đá và các phân khu bảo tồn lân cận.",
    [
        "Hồ có mặt nước lớn nhất Khakassia, gồm hai phần Lớn và Nhỏ thông nhau.",
        "Nước khoáng - mặn, nhiều vịnh bãi thoải thích hợp tắm và cắm trại gia đình.",
        "Mặt hồ lộng gió, được ưa chuộng cho thuyền buồm và các môn thể thao nước.",
    ],
    outdoor_practical(
        "Mở tự do quanh năm; mùa du lịch chính từ tháng 6 đến tháng 8.",
        "Tắm và cắm trại nhìn chung miễn phí ở bãi công cộng; bãi có dịch vụ và chỗ ở thu phí riêng.",
        "Từ nửa ngày đến vài ngày nghỉ dưỡng, cắm trại.",
        "Tháng 7–8 nước ấm nhất; chú ý gió lớn khi ra xa bờ.",
        "Chọn vịnh kín gió cho trẻ nhỏ; mang lều chắc vì thảo nguyên nhiều gió; dọn rác, giữ vệ sinh bờ hồ.",
    ),
    [
        {"title": "Wikipedia (RU) — Белё", "url": "https://ru.wikipedia.org/wiki/Белё"},
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
    ],
    ["lake", "largest-lake", "camping", "watersports", "shirinsky", "khakassia"],
    maps_text("Озеро Белё", "Ширинский район", "Lake Belyo", "Shirinsky District", 54.653193, 90.120543),
))

# 4) Озеро Тус --------------------------------------------------------------------
RECORDS.append(rec(
    "lake-tus",
    "Hồ Tus - Hồ muối hồng (Ô-di-rô Tút)",
    "Озеро Тус",
    "Lake Tus",
    ["park_garden"],
    54.736277, 89.960647,
    "Huyện Shirinsky, gần làng Solyonoozyornoye, Cộng hoà Khakassia, Nga.",
    "Tus là hồ nước mặn nổi tiếng với độ mặn rất cao, được ví như «Biển Chết của Siberia». Nước siêu mặn nâng bổng cơ thể người tắm, có lúc chuyển sắc hồng, cùng lớp bùn đen chữa bệnh khiến Tus thành điểm tắm khoáng độc đáo của Khakassia.",
    "Nằm ở phía bắc Khakassia, Tus là hồ không có dòng chảy ra, tích tụ muối qua thời gian nên có độ mặn rất cao - nồng độ muối nhiều thời điểm sánh với Biển Chết, đủ để người tắm nổi bồng bềnh mà không cần bơi. Vào những giai đoạn nắng nóng, khi tảo ưa mặn và vi khuẩn phát triển mạnh, mặt nước có thể ánh lên sắc hồng - tím đặc trưng, tạo nên khung cảnh siêu thực trên nền đồi thảo nguyên. Đáy hồ phủ lớp bùn khoáng màu sẫm được người dân dùng đắp lên da theo lối trị liệu dân gian, cùng muối kết tinh ven bờ. Chính những đặc điểm này biến Tus thành điểm tắm khoáng - «spa thiên nhiên» hút khách vào mùa hè, dù tiện nghi quanh hồ còn khá mộc mạc. Du khách thường kết hợp Tus với chuỗi hồ Shira, Belyo, Itkul trong hành trình khám phá vùng hồ Shirinsky. Cần lưu ý nước siêu mặn có thể xót mắt và vết thương hở, nên tắm chừng mực và tráng nước ngọt sau khi lên bờ.",
    [
        "Hồ siêu mặn được ví như «Biển Chết của Siberia» - nước nâng nổi cơ thể người tắm.",
        "Có lúc mặt nước chuyển sắc hồng - tím do tảo và vi khuẩn ưa mặn.",
        "Bùn khoáng đen dưới đáy được dùng đắp da theo lối trị liệu dân gian.",
    ],
    outdoor_practical(
        "Mở tự do quanh năm; mùa tắm khoáng từ tháng 6 đến tháng 8.",
        "Nhìn chung miễn phí; một số bãi có thu phí gửi xe hoặc dịch vụ.",
        "Khoảng 1–3 giờ tắm và đắp bùn.",
        "Giữa hè nắng nóng, khi nước ấm và sắc hồng dễ xuất hiện nhất.",
        "Không để nước vào mắt và vết thương hở; tắm nước ngọt tráng lại sau khi lên bờ; không dầm quá lâu.",
    ),
    [
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
        {"title": "Geocaching.su — Озеро Тус", "url": "https://www.geocaching.su/?pn=101"},
    ],
    ["lake", "salt-lake", "pink-lake", "mud-therapy", "shirinsky", "khakassia"],
    maps_text("Озеро Тус", "Ширинский район", "Lake Tus", "Shirinsky District", 54.736277, 89.960647),
))

# 5) Озеро Иткуль -----------------------------------------------------------------
RECORDS.append(rec(
    "lake-itkul",
    "Hồ Itkul (Ô-di-rô It-kun)",
    "Озеро Иткуль",
    "Lake Itkul",
    ["park_garden"],
    54.464152, 90.090926,
    "Huyện Shirinsky, Cộng hoà Khakassia, Nga; một phần bờ thuộc khu bảo tồn Khakassky.",
    "Itkul là hồ nước ngọt trong lành hiếm hoi giữa vùng hồ mặn Shirinsky, nguồn nước sạch quan trọng của khu vực. Nước trong, bờ đẹp và một phần hồ nằm trong khu bảo tồn khiến Itkul vừa là điểm nghỉ mát, vừa là nơi bảo vệ thiên nhiên.",
    "Giữa vùng thảo nguyên phía bắc Khakassia vốn nổi tiếng với các hồ mặn - khoáng, Itkul là một ngoại lệ quý giá: hồ nước ngọt trong vắt, độ khoáng thấp, được xem là một trong những nguồn nước sạch quan trọng của huyện Shirinsky. Hồ có bờ đa dạng với các mũi đất, vịnh nhỏ và bãi thoải; nước mát, trong nên thu hút du khách tới tắm, câu cá và cắm trại trong bầu không khí yên tĩnh hơn so với các hồ đông khách lân cận. Một phần bờ và vùng nước của Itkul nằm trong ranh giới khu bảo tồn thiên nhiên Khakassky, nơi có trạm bảo vệ và các quy định gìn giữ hệ sinh thái ven hồ - môi trường sống của nhiều loài chim nước. Cảnh quan quanh hồ là sự chuyển tiếp mềm mại giữa thảo nguyên và những dải rừng thấp, đặc biệt đẹp vào sáng sớm và hoàng hôn. Itkul thường được ghép cùng Shira, Belyo, Tus thành cung đường khám phá vùng hồ, nhưng mang đến trải nghiệm dịu dàng, gần gũi thiên nhiên hơn.",
    [
        "Hồ nước ngọt trong lành hiếm hoi giữa vùng hồ mặn Shirinsky.",
        "Nguồn nước sạch quan trọng của khu vực, một phần thuộc khu bảo tồn Khakassky.",
        "Không gian yên tĩnh, thích hợp tắm, câu cá và cắm trại gần thiên nhiên.",
    ],
    outdoor_practical(
        "Mở tự do quanh năm; mùa du lịch từ tháng 6 đến tháng 8.",
        "Bãi công cộng nhìn chung miễn phí; khu vực thuộc bảo tồn có thể hạn chế hoặc cần tuân thủ quy định riêng.",
        "Từ vài giờ đến vài ngày cắm trại, nghỉ ngơi.",
        "Tháng 6–8; sáng sớm và hoàng hôn cảnh đẹp, mặt hồ tĩnh lặng.",
        "Tôn trọng ranh giới khu bảo tồn, không xả rác, không gây ô nhiễm nguồn nước sạch của vùng.",
    ),
    [
        {"title": "Wikipedia (RU) — Иткуль (озеро, Хакасия)", "url": "https://ru.wikipedia.org/wiki/Иткуль_(озеро,_Хакасия)"},
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
    ],
    ["lake", "freshwater", "fishing", "nature-reserve", "shirinsky", "khakassia"],
    maps_text("Озеро Иткуль", "Ширинский район", "Lake Itkul", "Shirinsky District", 54.464152, 90.090926),
))

# 6) Озеро Ханкуль ----------------------------------------------------------------
RECORDS.append(rec(
    "lake-khankul",
    "Hồ Khankul (Ô-di-rô Khan-kun)",
    "Озеро Ханкуль",
    "Lake Khankul",
    ["park_garden"],
    53.37097, 90.83143,
    "Huyện Askizsky, gần ga Khankul, Cộng hoà Khakassia, Nga.",
    "Khankul là hồ nước khoáng - mặn nhỏ ở miền nam Khakassia, nổi tiếng với nước và bùn có tính chữa bệnh. Đây là điểm tắm khoáng, đắp bùn dân dã được người địa phương lui tới quanh năm.",
    "Nằm ở huyện Askizsky phía nam nước cộng hoà, gần tuyến đường sắt và ga cùng tên, Khankul là một hồ nhỏ nhưng được người dân Khakassia đặc biệt quý trọng nhờ đặc tính khoáng của nó. Nước hồ thuộc loại khoáng - mặn, giàu muối và các nguyên tố vi lượng; lớp bùn đáy màu sẫm được xem là có tác dụng trị liệu, thường được du khách lấy đắp lên da và khớp theo kinh nghiệm dân gian. Khankul không có hạ tầng nghỉ dưỡng bề thế như các hồ ở Shirinsky, mà mang dáng vẻ mộc mạc: bãi đất ven hồ, vài điểm dịch vụ đơn sơ và dòng người tự tìm đến tắm, ngâm bùn vào mùa ấm. Chính sự bình dị đó cùng công dụng khoáng đã tạo nên sức hút riêng, biến hồ thành điểm chăm sóc sức khoẻ quen thuộc cho cư dân Abakan và các vùng lân cận. Do gần đường sắt và quốc lộ, Khankul cũng thuận tiện ghé thăm trên hành trình về phía nam Khakassia.",
    [
        "Hồ nước khoáng - mặn nhỏ ở miền nam Khakassia, nổi tiếng tính chữa bệnh.",
        "Bùn đáy sẫm màu được dùng đắp da, khớp theo kinh nghiệm dân gian.",
        "Điểm tắm khoáng dân dã, gần ga Khankul, thuận tiện ghé thăm.",
    ],
    outdoor_practical(
        "Mở tự do quanh năm; đông khách vào mùa hè.",
        "Nhìn chung miễn phí; có thể phát sinh phí gửi xe hoặc dịch vụ đơn sơ.",
        "Khoảng 1–2 giờ tắm và đắp bùn.",
        "Mùa hè (tháng 6–8) khi nước ấm.",
        "Hồ nhỏ, tiện nghi mộc mạc - nên tự chuẩn bị nước ngọt tráng người; hỏi ý kiến bác sĩ nếu trị liệu khi có bệnh nền.",
    ),
    [
        {"title": "Wikipedia (RU) — Ханкуль (озеро)", "url": "https://ru.wikipedia.org/wiki/Ханкуль_(озеро)"},
        {"title": "gpx.su — Озеро Ханкуль", "url": "https://gpx.su/place/39"},
    ],
    ["lake", "mineral-lake", "mud-therapy", "askizsky", "khakassia"],
    maps_text("Озеро Ханкуль", "Аскизский район", "Lake Khankul", "Askizsky District", 53.37097, 90.83143),
))

# 7) Боярская писаница ------------------------------------------------------------
RECORDS.append(rec(
    "boyarskaya-pisanitsa",
    "Bãi khắc đá Boyarskaya (Bô-i-a-rơ-xka-i-a Pi-xa-nhi-txa)",
    "Боярская писаница",
    "Boyarskaya Pisanitsa",
    ["monument"],
    54.29215, 91.188417,
    "Sườn dãy Boyarsky, gần làng Troitskoye, huyện Bogradsky, Cộng hoà Khakassia, Nga.",
    "Boyarskaya Pisanitsa là bãi tranh khắc đá cổ nổi tiếng, khắc họa cả một «ngôi làng» thời đồ sắt với nhà cửa, người và gia súc. Đây là tư liệu hình ảnh quý về đời sống người Tagar - Tashtyk trên thảo nguyên Khakassia.",
    "Trên sườn đá của dãy Boyarsky nhìn ra thung lũng sông Yenisei, các nhà khảo cổ đã ghi nhận một trong những bãi khắc đá đặc sắc nhất Nam Siberia - Boyarskaya Pisanitsa. Gồm hai cụm Lớn và Nhỏ, di tích có niên đại vào khoảng thế kỷ 3 trước Công nguyên đến thế kỷ 1 sau Công nguyên, thuộc thời kỳ văn hoá Tagar muộn và Tashtyk. Điều khiến bãi khắc này nổi tiếng là nội dung mang tính «tường thuật»: thay vì chỉ những con thú riêng lẻ, người xưa đã khắc cả một quang cảnh sinh hoạt - những ngôi nhà gỗ và lều hình vòm (yurt), vạc nấu, người đứng, cùng đàn bò, cừu, dê, ngựa. Nhờ đó, Boyarskaya trở thành nguồn tư liệu hình ảnh hiếm hoi cho biết diện mạo làng mạc, kiểu nhà ở và đời sống chăn nuôi của cư dân thảo nguyên Minusinsk cách nay hơn hai nghìn năm. Di tích nằm ngoài trời trên vách đá, phải đi bộ leo dốc mới tới, và cần được bảo vệ khỏi tác động thời tiết lẫn con người. Với giới yêu khảo cổ, đây là một điểm nhấn không thể bỏ qua khi khám phá «vùng đất của các bãi khắc đá» Khakassia.",
    [
        "Bãi khắc đá thời đồ sắt khắc họa cả một «ngôi làng»: nhà cửa, người và gia súc.",
        "Niên đại khoảng thế kỷ 3 TCN – thế kỷ 1 SCN, văn hoá Tagar muộn - Tashtyk.",
        "Tư liệu hình ảnh hiếm về nhà ở và đời sống chăn nuôi trên thảo nguyên cổ.",
    ],
    outdoor_practical(
        "Di tích ngoài trời trên vách đá, tham quan ban ngày; không có giờ cố định.",
        "Không thu vé; nên đi cùng hướng dẫn viên hoặc tour để tìm và hiểu đúng các hình khắc.",
        "Khoảng 1–2 giờ kể cả đường leo dốc.",
        "Cuối xuân đến đầu thu (tháng 5–9) khi đường khô ráo, ánh sáng nghiêng làm nổi nét khắc.",
        "Mang giày leo, nước uống; tuyệt đối không chạm, tô vẽ hay làm hư hại hình khắc; ánh sáng buổi sáng/chiều giúp nhìn rõ nét hơn.",
    ),
    [
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
        {"title": "Wikipedia (RU) — Боярская писаница", "url": "https://ru.wikipedia.org/wiki/Боярская_писаница"},
    ],
    ["petroglyphs", "rock-art", "archaeology", "tagar", "tashtyk", "bogradsky"],
    maps_org("https://yandex.ru/maps/org/boyarskaya_pisanitsa/81784749763/", "Boyarskaya Pisanitsa", "Bogradsky District"),
))

# 8) Оглахты ----------------------------------------------------------------------
RECORDS.append(rec(
    "oglakhty",
    "Khu núi Oglakhty (Ô-glắc-tư)",
    "Оглахты",
    "Oglakhty",
    ["fortress", "monument"],
    54.012812, 91.494083,
    "Bờ trái hồ chứa Krasnoyarsk trên sông Yenisei, huyện Ust-Abakansky; là một phân khu của khu bảo tồn Khakassky, Nga.",
    "Oglakhty là quần thể khảo cổ - cảnh quan trứ danh của Khakassia: dãy núi bên sông Yenisei với hàng nghìn hình khắc đá, tàn tích tường thành cổ trên đỉnh và các mộ táng Tashtyk nổi tiếng với mặt nạ thạch cao. Nay là phân khu bảo tồn có tuyến tham quan sinh thái.",
    "Bên bờ hồ chứa Krasnoyarsk (đoạn sông Yenisei), dãy núi Oglakhty vươn lên tạo thành một trong những cụm di sản khảo cổ giàu có nhất Khakassia. Trên các vách đá sa thạch đỏ ở đây lưu giữ hàng nghìn hình khắc và vẽ (pisanitsa) trải dài nhiều thời kỳ, từ thời đồ đá mới qua các nền văn hoá Okunev, Tagar đến Tashtyk. Trên các đỉnh núi còn dấu vết của một hệ thống tường - lũy đá cổ chạy dọc sống núi, cho thấy vị trí này từng có ý nghĩa chiến lược. Oglakhty đặc biệt nổi tiếng trong giới khảo cổ nhờ các ngôi mộ văn hoá Tashtyk (khoảng thế kỷ 1–5 SCN), nơi tìm thấy những mặt nạ tang lễ bằng thạch cao, tượng nhồi và di vật được bảo quản tốt, hé lộ nghi thức mai táng độc đáo của cư dân cổ. Ngày nay Oglakhty là một phân khu của khu bảo tồn Khakassky, có trạm kiểm lâm, tuyến đi bộ sinh thái với cầu thang gỗ và điểm ngắm cảnh sông núi hùng vĩ - kết hợp hài hoà giữa khám phá khảo cổ và thiên nhiên.",
    [
        "Hàng nghìn hình khắc - vẽ trên vách đá đỏ, trải nhiều thời kỳ từ đồ đá mới đến Tashtyk.",
        "Tàn tích tường thành đá cổ trên sống núi và các mộ Tashtyk với mặt nạ thạch cao trứ danh.",
        "Phân khu bảo tồn có tuyến sinh thái, ngắm cảnh sông Yenisei hùng vĩ.",
    ],
    outdoor_practical(
        "Tuyến tham quan mở theo mùa (chủ yếu mùa ấm); nên liên hệ khu bảo tồn Khakassky trước.",
        "Vào khu có thu phí tuyến sinh thái/hướng dẫn; đăng ký trước với ban quản lý.",
        "Khoảng nửa ngày (2–4 giờ) cho tuyến đi bộ và điểm ngắm cảnh.",
        "Tháng 5–9 khi đường khô ráo; tránh mùa lạnh và mưa trơn trượt.",
        "Mang giày leo và nước; đi theo tuyến quy định, không tự ý trèo vách hay chạm hình khắc; tuân thủ hướng dẫn kiểm lâm.",
    ),
    [
        {"title": "Wikipedia (RU) — Оглахты", "url": "https://ru.wikipedia.org/wiki/Оглахты"},
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
    ],
    ["petroglyphs", "fortress", "tashtyk", "archaeology", "yenisei", "nature-reserve"],
    maps_text("Оглахты", "Усть-Абаканский район", "Oglakhty", "Ust-Abakansky District", 54.012812, 91.494083),
))

# 9) Малая Сыя --------------------------------------------------------------------
RECORDS.append(rec(
    "malaya-syya",
    "Di chỉ Malaya Syya (Ma-la-i-a Xư-a)",
    "Малая Сыя",
    "Malaya Syya",
    ["monument"],
    54.4000, 89.4333,
    "Gần làng Malaya Syya, thung lũng sông Bely Iyus, huyện Shirinsky, Cộng hoà Khakassia, Nga.",
    "Malaya Syya là một trong những di chỉ cư trú thời đồ đá cũ (Paleolithic) quan trọng nhất Siberia. Các cuộc khai quật tìm thấy công cụ đá, xương thú và dấu vết đời sống của người cổ cách nay hàng chục nghìn năm.",
    "Bên thung lũng sông Bely Iyus ở phía tây bắc Khakassia, gần ngôi làng nhỏ cùng tên, các nhà khảo cổ đã phát hiện di chỉ cư trú Malaya Syya - một điểm mốc quan trọng trong nghiên cứu thời đồ đá cũ ở Nam Siberia. Được khảo sát và khai quật từ nửa sau thế kỷ 20, tầng văn hoá tại đây chứa nhiều công cụ đá đẽo, mảnh tước, di cốt động vật thời băng hà cùng dấu vết bếp lửa và nơi cư trú, phản ánh đời sống săn bắt - hái lượm của người cổ cách nay hàng chục nghìn năm. Niên đại của di chỉ từng gây nhiều tranh luận trong giới khoa học, với những ước tính đưa Malaya Syya vào hàng các điểm cư trú cổ xưa bậc nhất khu vực; dù con số cụ thể còn được bàn thảo, giá trị của nó như một cửa sổ nhìn về buổi bình minh của con người ở Siberia là điều được thừa nhận rộng rãi. Ngày nay hiện trường không có công trình trưng bày lớn tại chỗ - phần lớn hiện vật được lưu giữ và nghiên cứu ở các bảo tàng - nên điểm đến này phù hợp nhất với du khách yêu khảo cổ, thường kết hợp cùng hành trình khám phá vùng hồ và hang động phía bắc.",
    [
        "Một trong những di chỉ cư trú thời đồ đá cũ quan trọng nhất Nam Siberia.",
        "Phát hiện công cụ đá, di cốt thú băng hà và dấu vết bếp lửa của người cổ.",
        "Cửa sổ nhìn về buổi bình minh của con người ở Siberia, có giá trị khoa học cao.",
    ],
    outdoor_practical(
        "Di chỉ ngoài trời, không có giờ mở cố định; nên đi cùng hướng dẫn am hiểu.",
        "Không thu vé; hiện trường không có khu trưng bày lớn tại chỗ.",
        "Khoảng 1 giờ tại hiện trường (nên kết hợp điểm khác trong vùng).",
        "Mùa khô ấm (tháng 5–9) thuận tiện đi lại.",
        "Đây là địa điểm khoa học, không đào bới hay lấy đi hiện vật; tìm hiểu trước để hiểu ý nghĩa di chỉ.",
    ),
    [
        {"title": "Wikipedia (RU) — Малая Сыя (стоянка)", "url": "https://ru.wikipedia.org/wiki/Малая_Сыя_(стоянка)"},
        {"title": "komandirovka.ru — Малая Сыя", "url": "https://www.komandirovka.ru/sights/malaya-syya/"},
    ],
    ["archaeology", "paleolithic", "prehistoric", "shirinsky", "khakassia"],
    maps_text("Малая Сыя", "Ширинский район", "Malaya Syya", "Shirinsky District", 54.4000, 89.4333),
))

# 10) Сулекская писаница ----------------------------------------------------------
RECORDS.append(rec(
    "sulek-pisanitsa",
    "Bãi khắc đá Sulek (Xu-lếch-xka-i-a Pi-xa-nhi-txa)",
    "Сулекская писаница",
    "Sulek Pisanitsa",
    ["monument"],
    54.968232, 89.582716,
    "Núi Pisanaya gần làng Kopyovo, huyện Ordzhonikidzevsky, Cộng hoà Khakassia, Nga.",
    "Sulek Pisanitsa là một trong những bãi tranh khắc đá phong phú nhất Khakassia, nổi bật với các hình kỵ sĩ, chiến binh và thú vật thời trung cổ. Di tích phản ánh nghệ thuật và đời sống của người Yenisei - Kyrgyz cổ.",
    "Ở phía bắc Khakassia, trên vách núi Pisanaya gần làng Kopyovo, bãi khắc đá Sulek tập hợp một số lượng lớn hình khắc trải dài nhiều thời đại, từ thời đồ đồng - đồ sắt cho tới thời trung cổ. Nổi tiếng nhất là nhóm hình thuộc thời kỳ người Yenisei - Kyrgyz cổ (khoảng thế kỷ 8–10): những kỵ sĩ mặc giáp, cung thủ, chiến binh cầm cờ hiệu, cảnh săn bắn và các con thú được thể hiện sống động, tỉ mỉ đến từng chi tiết trang phục và vũ khí. Chính vì độ phong phú và giá trị nghệ thuật đó, Sulek được giới nghiên cứu xem như một «kho tranh» quý để tìm hiểu văn hoá, quân sự và tín ngưỡng của các cư dân thảo nguyên trung cổ ở lưu vực Yenisei. Di tích nằm ngoài trời trên vách đá cao, một số hình đã mờ do phong hoá và cần được bảo vệ khỏi tác động của con người. Với người yêu lịch sử, Sulek là điểm đến hấp dẫn tuy đòi hỏi phải di chuyển xa và leo dốc; ánh sáng xiên buổi sáng hoặc chiều muộn giúp các nét khắc hiện lên rõ nhất.",
    [
        "Bãi khắc đá phong phú bậc nhất Khakassia, trải từ đồ đồng đến thời trung cổ.",
        "Nổi bật các hình kỵ sĩ mặc giáp, chiến binh, cung thủ thời Yenisei - Kyrgyz cổ.",
        "Tư liệu quý về nghệ thuật, quân sự và tín ngưỡng của cư dân thảo nguyên trung cổ.",
    ],
    outdoor_practical(
        "Di tích ngoài trời, tham quan ban ngày; không có giờ cố định.",
        "Không thu vé; nên đi cùng hướng dẫn viên để định vị và hiểu các hình khắc.",
        "Khoảng 1–2 giờ kể cả đường leo.",
        "Tháng 5–9, ưu tiên sáng sớm hoặc chiều muộn khi ánh sáng xiên làm nổi nét khắc.",
        "Mang giày leo và nước; không chạm hay tô vẽ lên hình khắc; nhiều nét đã mờ, cần quan sát kỹ.",
    ),
    [
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
        {"title": "Wikipedia (RU) — Сулекская писаница", "url": "https://ru.wikipedia.org/wiki/Сулекская_писаница"},
    ],
    ["petroglyphs", "rock-art", "medieval", "yenisei-kyrgyz", "ordzhonikidzevsky"],
    maps_text("Сулекская писаница", "Орджоникидзевский район", "Sulek Pisanitsa", "Ordzhonikidzevsky District", 54.968232, 89.582716),
))

# 11) Сафроновский курганный могильник --------------------------------------------
RECORDS.append(rec(
    "safronov-kurgan-cemetery",
    "Nghĩa địa gò mộ Safronov (Xa-phrô-nốp-xki Mô-ghin-nhích)",
    "Сафроновский курганный могильник",
    "Safronovsky Kurgan Cemetery",
    ["monument"],
    53.05361, 90.06000,
    "Gần làng Kazanovka, huyện Askizsky, Cộng hoà Khakassia, Nga.",
    "Safronovsky là một trong những nghĩa địa gò mộ (kurgan) lớn và ấn tượng của văn hoá Tagar, với những phiến đá dựng khổng lồ quây quanh các gò. Đây là điểm nhấn của cảnh quan «thảo nguyên các gò mộ» ở miền nam Khakassia.",
    "Trên vùng thảo nguyên huyện Askizsky, gần khu bảo tồn Kazanovka, nghĩa địa gò mộ Safronovsky trải ra như một «thành phố của người chết» thời cổ. Thuộc văn hoá Tagar (khoảng thiên niên kỷ 1 trước Công nguyên), quần thể gồm nhiều gò mộ lớn nhỏ, mà đặc trưng nổi bật là những phiến đá sa thạch cao dựng đứng ở bốn góc và dọc chu vi mỗi gò - có phiến vươn cao vài mét, tạo nên khung cảnh trang nghiêm, kỳ vĩ giữa đồng cỏ. Những hàng đá dựng này không chỉ đánh dấu ranh giới mộ mà còn mang ý nghĩa nghi lễ, thể hiện quan niệm về thế giới bên kia và địa vị của người được chôn cất. Đứng giữa Safronovsky, du khách dễ hình dung vì sao vùng Minusinsk - Khakassia được mệnh danh là «thung lũng của các vị vua» phương Đông: mật độ gò mộ dày đặc, quy mô đồ sộ và tuổi đời hàng nghìn năm. Di tích nằm ngoài trời, gần đường nên tương đối dễ tiếp cận, và thường được kết hợp tham quan cùng khu bảo tồn Kazanovka cũng như Đại gò mộ Salbyk để có bức tranh trọn vẹn về văn hoá Tagar.",
    [
        "Nghĩa địa gò mộ Tagar lớn với những phiến đá dựng cao vài mét quanh mỗi gò.",
        "Khung cảnh trang nghiêm, kỳ vĩ - biểu tượng của «thảo nguyên các gò mộ» Khakassia.",
        "Dễ kết hợp với khu bảo tồn Kazanovka và Đại gò mộ Salbyk gần đó.",
    ],
    outdoor_practical(
        "Di tích ngoài trời, tham quan ban ngày quanh năm; không có giờ cố định.",
        "Không thu vé; có thể kết hợp tour khảo cổ vùng Askiz - Kazanovka.",
        "Khoảng 30–60 phút.",
        "Cuối xuân đến đầu thu (tháng 5–9); ánh sáng sớm/chiều làm nổi khối đá dựng.",
        "Không trèo lên hay xê dịch các phiến đá; kết hợp Kazanovka và Salbyk để hiểu trọn văn hoá Tagar.",
    ),
    [
        {"title": "Wikipedia (RU) — Сафроновский могильник", "url": "https://ru.wikipedia.org/wiki/Сафроновский_могильник"},
        {"title": "gpx.su — Сафроновский могильник", "url": "https://gpx.su/place/64"},
    ],
    ["kurgan", "tagar", "archaeology", "steppe", "askizsky", "menhir"],
    maps_text("Сафроновский курганный могильник", "Аскизский район", "Safronovsky Kurgan Cemetery", "Askizsky District", 53.05361, 90.06000),
))

# 12) Саяно-Шушенская ГЭС ---------------------------------------------------------
RECORDS.append(rec(
    "sayano-shushenskaya-dam",
    "Đập thủy điện Sayano-Shushenskaya (Xa-i-a-nô Su-sen-xka-i-a GES)",
    "Саяно-Шушенская ГЭС",
    "Sayano-Shushenskaya Dam",
    ["other", "monument"],
    52.82551, 91.37063,
    "Trên sông Yenisei gần thị trấn Cheryomushki, thành phố Sayanogorsk, Cộng hoà Khakassia, Nga.",
    "Sayano-Shushenskaya là nhà máy thủy điện lớn nhất nước Nga, với con đập vòm - trọng lực khổng lồ cao gần 250 m chắn ngang sông Yenisei nơi cửa hẻm núi Sayan. Đây là công trình kỹ thuật hùng vĩ và biểu tượng công nghiệp của vùng.",
    "Ở nơi sông Yenisei phá qua dãy Tây Sayan để đổ vào thảo nguyên Khakassia - Minusinsk, con người đã dựng lên một trong những công trình thủy điện vĩ đại nhất thế giới: nhà máy thủy điện Sayano-Shushenskaya. Đập chính là loại đập vòm - trọng lực bằng bê tông, cao khoảng 245 m, dài hơn một cây số ở đỉnh, uốn cong tựa vào hai vách hẻm núi để chống lại áp lực khổng lồ của hồ chứa phía sau. Với công suất lắp đặt 6.400 MW, đây là nhà máy điện lớn nhất nước Nga và là một trong những công trình thủy điện lớn nhất hành tinh. Khởi công từ cuối thập niên 1960 và hoàn thành qua nhiều thập kỷ, công trình gắn liền với lịch sử công nghiệp hoá Siberia; thảm hoạ vỡ tổ máy năm 2009 và công cuộc tái thiết sau đó cũng khiến nó được cả thế giới biết đến. Ngày nay, đứng từ các điểm ngắm cảnh bên bờ, du khách choáng ngợp trước bức tường bê tông dựng đứng, làn nước xả trắng xoá và khung cảnh núi non hùng vĩ bao quanh. Đập nằm ở phần phía nam Khakassia, gần thị trấn thủy điện Cheryomushki và thành phố Sayanogorsk; khu vực sản xuất được bảo vệ nghiêm ngặt nên tham quan chủ yếu từ bên ngoài.",
    [
        "Nhà máy thủy điện lớn nhất nước Nga, công suất 6.400 MW.",
        "Đập vòm - trọng lực cao khoảng 245 m, dài hơn 1 km, chắn ngang sông Yenisei.",
        "Công trình kỹ thuật hùng vĩ giữa hẻm núi Tây Sayan - biểu tượng công nghiệp Siberia.",
    ],
    outdoor_practical(
        "Ngắm từ các điểm bên ngoài quanh năm; khu vực nhà máy là công trình an ninh, không tự do vào trong.",
        "Ngắm cảnh bên ngoài miễn phí; tham quan có tổ chức (nếu có) theo chương trình riêng của nhà máy.",
        "Khoảng 30–60 phút tại các điểm ngắm cảnh.",
        "Mùa hè khi có xả nước, thác nước xả tạo cảnh tượng ấn tượng.",
        "Đây là công trình trọng yếu - tuân thủ biển cấm và khu vực an ninh; ngắm và chụp ảnh từ điểm cho phép.",
    ),
    [
        {"title": "Wikipedia (RU) — Саяно-Шушенская ГЭС", "url": "https://ru.wikipedia.org/wiki/Саяно-Шушенская_ГЭС"},
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
    ],
    ["dam", "hydropower", "yenisei", "engineering", "sayanogorsk", "landmark"],
    maps_text("Саяно-Шушенская ГЭС", "Черёмушки", "Sayano-Shushenskaya Dam", "Cheryomushki", 52.82551, 91.37063),
))

# 13) ГЛК «Гладенькая» ------------------------------------------------------------
RECORDS.append(rec(
    "gladenkaya-ski-resort",
    "Khu trượt tuyết Gladenkaya (Gla-đen-ka-i-a)",
    "Горнолыжный комплекс «Гладенькая»",
    "Gladenkaya Ski Resort",
    ["other"],
    52.945120, 91.359449,
    "Sườn núi Gladenkaya gần thành phố Sayanogorsk, Cộng hoà Khakassia, Nga.",
    "Gladenkaya là khu trượt tuyết núi cao nổi tiếng nhất Khakassia, với đường trượt dài, chênh cao lớn và cáp treo hiện đại. Nằm gần Sayanogorsk và đập thủy điện, đây là điểm đến thể thao mùa đông chủ lực của vùng.",
    "Trên sườn núi Gladenkaya thuộc dãy Tây Sayan, gần thành phố Sayanogorsk ở phía nam Khakassia, khu liên hợp thể thao mùa đông cùng tên đã trở thành «thánh địa» trượt tuyết của cả vùng và thu hút cả vận động viên chuyên nghiệp. Điểm mạnh của Gladenkaya là địa hình núi thật sự: độ chênh cao lớn (hàng trăm mét), các đường trượt dài với nhiều cấp độ khó, tuyết dày và mùa trượt kéo dài. Khu được trang bị cáp treo ghế ngồi đưa khách lên đỉnh, cùng hệ thống đường xanh - đỏ - đen phục vụ từ người mới học đến dân trượt lão luyện; nơi đây từng tổ chức các giải đấu và là điểm tập huấn của các đội tuyển. Bên cạnh trượt tuyết và trượt ván, du khách còn được thưởng ngoạn khung cảnh núi non hùng vĩ, rừng taiga phủ tuyết trắng và bầu không khí trong lành. Hạ tầng dịch vụ gồm nhà nghỉ, quán ăn, cho thuê thiết bị và trường dạy trượt. Vị trí gần Sayanogorsk và đập Sayano-Shushenskaya giúp Gladenkaya dễ kết hợp trong một hành trình khám phá miền nam Khakassia mùa đông.",
    [
        "Khu trượt tuyết núi cao lớn nhất Khakassia, chênh cao và đường trượt đa cấp độ.",
        "Cáp treo hiện đại, mùa tuyết dài, từng tổ chức thi đấu và tập huấn đội tuyển.",
        "Cảnh núi Tây Sayan phủ tuyết, gần Sayanogorsk và đập thủy điện.",
    ],
    outdoor_practical(
        "Hoạt động chủ yếu mùa đông - xuân (khoảng tháng 11–4); giờ mở cửa theo lịch khu trượt.",
        "Thu phí vé cáp/vé trượt theo ngày hoặc theo lượt; có gói thuê thiết bị và học phí.",
        "Từ nửa ngày đến nhiều ngày nghỉ dưỡng - thể thao.",
        "Giữa mùa đông đến đầu xuân khi tuyết dày và ổn định nhất.",
        "Đặt chỗ ở và thiết bị trước vào cao điểm; mặc đủ ấm, kiểm tra cấp độ đường trượt phù hợp trình độ.",
    ),
    [
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
        {"title": "zoon.ru — ГЛК Гладенькая", "url": "https://sayanogorsk.zoon.ru/"},
    ],
    ["ski-resort", "winter-sports", "mountain", "sayanogorsk", "sayan"],
    maps_text("Горнолыжный комплекс Гладенькая", "Саяногорск", "Gladenkaya Ski Resort", "Sayanogorsk", 52.945120, 91.359449),
))

# 14) Бородинская пещера ----------------------------------------------------------
RECORDS.append(rec(
    "borodinskaya-cave",
    "Hang Borodinskaya (Bô-rô-đin-xka-i-a Pê-sê-ra)",
    "Бородинская пещера",
    "Borodinskaya Cave",
    ["other"],
    54.110721, 91.096100,
    "Gần làng Tolchea, huyện Bogradsky, Cộng hoà Khakassia, Nga.",
    "Borodinskaya là hang động đá vôi lớn và đẹp bậc nhất Khakassia, nổi tiếng với những sảnh rộng cùng nhũ đá, măng đá và các khối canxit muôn hình. Đây là điểm thám hiểm hang động (caving) hấp dẫn của vùng.",
    "Trong lòng dãy núi đá vôi ở huyện Bogradsky, hang Borodinskaya được xem là một trong những hang động đẹp và đáng khám phá nhất Khakassia. Hệ thống hang gồm nhiều sảnh lớn nối nhau bằng các hành lang và lối hẹp, với tổng chiều dài đường hang đáng kể; bên trong là cả một thế giới ngầm của nhũ đá, măng đá, cột đá và các lớp trầm tích canxit hình thành qua hàng nghìn năm nước thấm qua đá. Một số sảnh đủ rộng và cao để tạo cảm giác choáng ngợp, được đặt những cái tên gợi hình theo dáng vẻ của các khối thạch nhũ. Hang thu hút giới thám hiểm hang động và du khách ưa mạo hiểm; tuy nhiên do địa hình trơn, tối và có đoạn khó nên việc tham quan cần đèn chiếu sáng, trang bị phù hợp và tốt nhất là đi cùng người dẫn đường am hiểu. Là di sản thiên nhiên nhạy cảm, các thành tạo trong hang rất dễ tổn hại nếu bị chạm hay bẻ, vì vậy nguyên tắc «không lấy đi gì ngoài những bức ảnh, không để lại gì ngoài dấu chân» luôn được nhấn mạnh. Borodinskaya thường nằm trong các tour khám phá thiên nhiên - hang động ở trung bắc Khakassia.",
    [
        "Một trong những hang đá vôi lớn và đẹp nhất Khakassia, nhiều sảnh rộng.",
        "Phong phú nhũ đá, măng đá, cột đá và trầm tích canxit hình thành qua hàng nghìn năm.",
        "Điểm thám hiểm hang động (caving) hấp dẫn, nên đi cùng người dẫn đường.",
    ],
    outdoor_practical(
        "Không có giờ mở cố định; tham quan theo tour hoặc nhóm có trang bị.",
        "Không thu vé cố định; đi tour caving có hướng dẫn thì trả phí dịch vụ.",
        "Khoảng 2–4 giờ khám phá tùy tuyến trong hang.",
        "Có thể vào quanh năm; mùa khô ấm thuận tiện đi lại tới cửa hang.",
        "Bắt buộc mang đèn, mũ bảo hiểm, giày bám tốt; đi cùng người dẫn đường; tuyệt đối không bẻ hay chạm nhũ đá.",
    ),
    [
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
        {"title": "Wikipedia (RU) — Бородинская пещера", "url": "https://ru.wikipedia.org/wiki/Бородинская_пещера"},
    ],
    ["cave", "caving", "karst", "speleology", "bogradsky", "nature"],
    maps_text("Бородинская пещера", "Боградский район", "Borodinskaya Cave", "Bogradsky District", 54.110721, 91.096100),
))

# 15) Хакасский национальный краеведческий музей им. Л.Р. Кызласова ---------------
RECORDS.append(rec(
    "khakassian-national-museum",
    "Bảo tàng Quốc gia Khakassia mang tên L.R. Kyzlasov (Kha-ka-xki Mu-dây)",
    "Хакасский национальный краеведческий музей им. Л.Р. Кызласова",
    "Khakassian National Museum named after L.R. Kyzlasov",
    ["museum"],
    53.720448, 91.474484,
    "Đường Pushkina 28A, thành phố Abakan, Cộng hoà Khakassia, Nga.",
    "Đây là bảo tàng lớn và quan trọng nhất Khakassia, lưu giữ bộ sưu tập khảo cổ tầm cỡ, nổi bật là các tấm bia đá (stela) khắc mặt người thời văn hoá Okunev. Bảo tàng là nơi tốt nhất để hiểu lịch sử và văn hoá của vùng đất gò mộ.",
    "Toạ lạc trong một toà nhà hiện đại ở trung tâm Abakan, Bảo tàng Quốc gia Khakassia mang tên nhà khảo cổ L.R. Kyzlasov là cơ sở bảo tàng đầu ngành của nước cộng hoà, có nguồn gốc từ bảo tàng địa phương thành lập đầu thế kỷ 20. Kho báu quý giá nhất của bảo tàng là bộ sưu tập khảo cổ phản ánh nhiều nghìn năm cư trú trên thảo nguyên Minusinsk - Khakassia: công cụ, đồ đồng, gốm và đặc biệt là các tấm bia đá và tượng đá cổ. Nổi bật hơn cả là những stela thời văn hoá Okunev (thiên niên kỷ 3–2 trước Công nguyên) chạm khắc mặt người bí ẩn, các biểu tượng và hoa văn - được xem như những kiệt tác nghệ thuật nguyên thuỷ độc nhất vô nhị, khiến bảo tàng trở thành «bảo tàng đá» danh tiếng. Bên cạnh khảo cổ, các gian trưng bày còn giới thiệu văn hoá dân tộc Khakas, đời sống du mục - chăn nuôi, trang phục, đồ thủ công, tín ngưỡng shaman, cùng thiên nhiên và lịch sử cận - hiện đại của vùng. Không gian trưng bày hiện đại, có gian sáng - tối phù hợp cho hiện vật đá, đưa Bảo tàng Quốc gia Khakassia thành điểm khởi đầu lý tưởng để hiểu về «thung lũng các vị vua» và bản sắc Khakassia.",
    [
        "Bảo tàng đầu ngành của Khakassia, bộ sưu tập khảo cổ tầm cỡ.",
        "Nổi tiếng với các bia đá khắc mặt người thời văn hoá Okunev - «bảo tàng đá».",
        "Trưng bày văn hoá dân tộc Khakas, đời sống du mục và tín ngưỡng shaman.",
    ],
    outdoor_practical(
        "Mở cửa các ngày trong tuần theo giờ hành chính (thường nghỉ Thứ Hai); nên kiểm tra lịch trước khi đến.",
        "Có bán vé tham quan; thường có ưu đãi cho học sinh, sinh viên và người cao tuổi.",
        "Khoảng 1,5–2,5 giờ.",
        "Quanh năm; là điểm đến lý tưởng khi thời tiết ngoài trời không thuận lợi.",
        "Nên tham quan bảo tàng trước khi ra thực địa gò mộ, khắc đá để hiểu bối cảnh; hỏi về tour có thuyết minh.",
    ),
    [
        {"title": "Wikipedia (RU) — Хакасский национальный краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Хакасский_национальный_краеведческий_музей_имени_Л._Р._Кызласова"},
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
    ],
    ["museum", "archaeology", "okunev", "stela", "khakas-culture", "abakan"],
    maps_text("Хакасский национальный краеведческий музей", "Абакан", "Khakassian National Museum", "Abakan", 53.720448, 91.474484),
    official_site="https://nhkm.ru",
))

# 16) Хакасский национальный драматический театр им. А.М. Топанова -----------------
RECORDS.append(rec(
    "khakas-national-drama-theatre",
    "Nhà hát Kịch Quốc gia Khakas mang tên A.M. Topanov (Tô-pa-nốp)",
    "Хакасский национальный драматический театр им. А.М. Топанова",
    "Khakas National Drama Theatre named after A.M. Topanov",
    ["theatre"],
    53.720994, 91.444841,
    "Đường Shchetinkina 12, thành phố Abakan, Cộng hoà Khakassia, Nga.",
    "Đây là nhà hát kịch dân tộc Khakas - sân khấu diễn bằng tiếng Khakas đầu tiên và tiêu biểu nhất, giữ vai trò trung tâm gìn giữ ngôn ngữ, văn hoá và nghệ thuật của dân tộc bản địa. Nhà hát mang tên nhà viết kịch, đạo diễn A.M. Topanov.",
    "Ra đời từ thập niên 1930 trên nền phong trào sân khấu dân tộc, Nhà hát Kịch Quốc gia Khakas là sân khấu chuyên nghiệp diễn bằng tiếng Khakas - một trong những trụ cột của đời sống văn hoá bản địa ở nước cộng hoà. Nhà hát mang tên Alexander Mikhailovich Topanov, người tiên phong đặt nền móng cho kịch nghệ Khakas. Trên sân khấu của mình, nhà hát dàn dựng cả kịch kinh điển thế giới lẫn Nga và đặc biệt là các vở lấy từ sử thi, truyền thuyết, phong tục và đời sống của người Khakas, qua đó gìn giữ và làm sống dậy ngôn ngữ mẹ đẻ, âm nhạc, trang phục và nghệ thuật kể chuyện truyền thống. Đoàn hát quy tụ nhiều nghệ sĩ dân tộc, thường lưu diễn về các vùng nông thôn và tham gia các liên hoan sân khấu. Nhà hát chia sẻ toà nhà biểu diễn ở trung tâm Abakan (trên đường Shchetinkina) cùng nhà hát kịch Nga, tạo thành một cụm sân khấu của thành phố. Với du khách, một buổi diễn ở đây - dù có thể cần theo dõi qua bản dịch - là cơ hội quý để cảm nhận tâm hồn và bản sắc của dân tộc Khakas.",
    [
        "Sân khấu kịch chuyên nghiệp diễn bằng tiếng Khakas, trụ cột văn hoá bản địa.",
        "Dàn dựng các vở từ sử thi, truyền thuyết và đời sống người Khakas.",
        "Mang tên A.M. Topanov, người đặt nền móng cho kịch nghệ Khakas.",
    ],
    outdoor_practical(
        "Biểu diễn theo lịch mùa diễn (thường thu - xuân); phòng vé mở theo giờ công bố.",
        "Mua vé theo suất diễn; giá phải chăng, có ưu đãi cho một số đối tượng.",
        "Mỗi buổi diễn khoảng 2–3 giờ.",
        "Mùa diễn thu - đông - xuân; nên xem lịch để chọn vở có phụ đề hoặc dễ theo dõi.",
        "Nhiều vở diễn bằng tiếng Khakas - hỏi trước về bản dịch/phụ đề; đặt vé sớm cho các suất đặc biệt.",
    ),
    [
        {"title": "Wikipedia (RU) — Хакасский национальный драматический театр", "url": "https://ru.wikipedia.org/wiki/Хакасский_национальный_драматический_театр_имени_А._М._Топанова"},
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
    ],
    ["theatre", "khakas-culture", "drama", "indigenous", "abakan"],
    maps_text("Хакасский национальный драматический театр Топанова", "Абакан", "Khakas National Drama Theatre", "Abakan", 53.720994, 91.444841),
))

# 17) Русский республиканский драматический театр им. М.Ю. Лермонтова --------------
RECORDS.append(rec(
    "russian-drama-theatre-lermontov",
    "Nhà hát Kịch Nga Cộng hoà mang tên M.Yu. Lermontov (Léc-môn-tốp)",
    "Русский республиканский драматический театр им. М.Ю. Лермонтова",
    "Russian Republican Drama Theatre named after M.Yu. Lermontov",
    ["theatre"],
    53.720969, 91.444543,
    "Đường Shchetinkina 12, thành phố Abakan, Cộng hoà Khakassia, Nga.",
    "Nhà hát Kịch Nga mang tên đại thi hào Lermontov là sân khấu kịch nói tiếng Nga chủ chốt của Khakassia, có lịch sử lâu đời và tiết mục phong phú từ kinh điển đến hiện đại. Đây là một trung tâm đời sống văn hoá của Abakan.",
    "Là một trong những nhà hát chuyên nghiệp lâu đời của nước cộng hoà, Nhà hát Kịch Nga Cộng hoà mang tên M.Yu. Lermontov giữ vai trò sân khấu kịch nói tiếng Nga trung tâm ở Khakassia, phục vụ khán giả Abakan và toàn vùng suốt nhiều thập kỷ. Trên sân khấu, nhà hát dàn dựng đa dạng thể loại: từ các kiệt tác kịch cổ điển Nga và thế giới, kịch tâm lý - xã hội, hài kịch cho tới các vở dành cho thiếu nhi và những dự án đương đại. Đội ngũ nghệ sĩ giàu kinh nghiệm cùng chương trình biểu diễn đều đặn khiến nơi đây trở thành điểm hẹn văn hoá quen thuộc của người dân thành phố, đặc biệt vào các buổi tối cuối tuần và dịp lễ hội sân khấu. Nhà hát chia sẻ toà nhà biểu diễn ở trung tâm Abakan cùng Nhà hát Kịch Quốc gia Khakas, tạo nên một tổ hợp sân khấu sinh động ngay trái tim thành phố. Với du khách, đây là lựa chọn thuận tiện để thưởng thức một buổi kịch tiếng Nga chất lượng và hoà mình vào nhịp sống văn hoá bản địa của thủ phủ Khakassia.",
    [
        "Sân khấu kịch nói tiếng Nga trung tâm và lâu đời của Khakassia.",
        "Tiết mục phong phú: kinh điển Nga - thế giới, kịch hiện đại và kịch thiếu nhi.",
        "Điểm hẹn văn hoá quen thuộc ngay trung tâm Abakan.",
    ],
    outdoor_practical(
        "Biểu diễn theo mùa diễn (thường thu - xuân); phòng vé mở theo giờ công bố.",
        "Mua vé theo suất; giá phải chăng, có ưu đãi cho một số đối tượng.",
        "Mỗi buổi diễn khoảng 2–3 giờ.",
        "Mùa diễn thu - đông - xuân; cuối tuần và dịp lễ thường có suất hấp dẫn.",
        "Đặt vé trước cho suất ăn khách; đến sớm để nhận chỗ; xem lịch để chọn vở phù hợp (người lớn/thiếu nhi).",
    ),
    [
        {"title": "Wikipedia (RU) — Русский республиканский драматический театр имени М. Ю. Лермонтова", "url": "https://ru.wikipedia.org/wiki/Русский_республиканский_драматический_театр_имени_М._Ю._Лермонтова"},
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
    ],
    ["theatre", "russian-drama", "culture", "abakan"],
    maps_text("Русский драматический театр имени Лермонтова", "Абакан", "Russian Drama Theatre Lermontov", "Abakan", 53.720969, 91.444543),
))

# 18) Никольский храм (Абакан) ----------------------------------------------------
RECORDS.append(rec(
    "abakan-nikolsky-church",
    "Nhà thờ Thánh Nikolai Abakan (Nhi-côn-xki Khram)",
    "Никольский храм (Абакан)",
    "St. Nicholas Church (Abakan)",
    ["church"],
    53.710042, 91.479255,
    "Ngõ Pionersky 1, thành phố Abakan, Cộng hoà Khakassia, Nga.",
    "Nhà thờ Thánh Nikolai là ngôi nhà thờ Chính thống giáo cổ nhất còn lại ở Abakan, có từ thời làng Ust-Abakanskoye. Ngôi thánh đường nhỏ này là chứng nhân lịch sử tôn giáo lâu đời của thành phố trước khi có Nhà thờ Chính tòa mới.",
    "Trong khi Nhà thờ Chính tòa Chúa Hiển Dung bề thế là công trình mới của thời hiện đại, thì Nhà thờ Thánh Nikolai (Nikolsky) lại nắm giữ vị thế đặc biệt: đây là ngôi nhà thờ Chính thống giáo cổ nhất còn tồn tại của Abakan, gắn với thời kỳ nơi đây còn là làng Ust-Abakanskoye khiêm nhường bên sông. Ngôi thánh đường có quy mô nhỏ, kiến trúc mộc mạc theo lối nhà thờ Nga truyền thống với mái vòm và tháp chuông, mang đậm không khí trầm mặc, ấm cúng khác hẳn sự tráng lệ của nhà thờ chính tòa. Trải qua những biến động của thế kỷ 20 - thời kỳ nhiều nhà thờ bị đóng cửa hay phá bỏ - việc Nikolsky tồn tại và tiếp tục hoạt động khiến nó trở thành một mảnh ký ức quý giá về đời sống tâm linh lâu đời của cư dân địa phương. Ngày nay nhà thờ vẫn duy trì các buổi lễ, là nơi lui tới của giáo dân và điểm dừng chân ý nghĩa cho những ai muốn tìm hiểu bề dày lịch sử tôn giáo của Abakan bên cạnh các công trình mới.",
    [
        "Nhà thờ Chính thống giáo cổ nhất còn lại ở Abakan, từ thời làng Ust-Abakanskoye.",
        "Kiến trúc nhỏ, mộc mạc, trầm mặc - tương phản với nhà thờ chính tòa mới.",
        "Chứng nhân quý về đời sống tâm linh lâu đời của cư dân địa phương.",
    ],
    outdoor_practical(
        "Mở cửa hằng ngày theo giờ lễ (thường sáng và chiều); có thể thay đổi theo lịch phụng vụ.",
        "Miễn phí vào tham quan và dự lễ; có thể tuỳ tâm công đức.",
        "Khoảng 20–30 phút.",
        "Quanh năm; đặc biệt vào các ngày lễ Chính thống giáo.",
        "Ăn mặc kín đáo, phụ nữ nên trùm khăn; giữ yên lặng và xin phép trước khi chụp ảnh bên trong.",
    ),
    [
        {"title": "sobory.ru — Никольский храм, Абакан", "url": "https://sobory.ru/geo/city/Abakan"},
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
    ],
    ["church", "orthodox", "historic", "oldest", "abakan"],
    maps_text("Никольский храм", "Абакан", "St Nicholas Church", "Abakan", 53.710042, 91.479255),
))

# 19) Церковь Святых Константина и Елены (Абакан) ----------------------------------
RECORDS.append(rec(
    "abakan-constantine-helen-church",
    "Nhà thờ Thánh Constantine và Helena Abakan (Kôn-xtan-tin va E-lê-na)",
    "Церковь Святых Константина и Елены (Абакан)",
    "Church of Saints Constantine and Helen (Abakan)",
    ["church"],
    53.718493, 91.463551,
    "Đường Pushkina 63, thành phố Abakan, Cộng hoà Khakassia, Nga.",
    "Nhà thờ Thánh Constantine và Helena là một thánh đường Chính thống giáo duyên dáng ở trung tâm Abakan, với dáng vẻ đền thờ Nga truyền thống và mái vòm ánh vàng. Đây là một trong những điểm hành hương và sinh hoạt giáo xứ quen thuộc của thành phố.",
    "Mang tên hai vị thánh Constantine Đại đế và mẹ ngài - hoàng hậu Helena, những người gắn với sự truyền bá Kitô giáo thời cổ, nhà thờ này là một trong những ngôi thánh đường Chính thống giáo đáng chú ý của Abakan. Công trình được xây theo phong cách đền thờ Nga truyền thống: khối nhà thờ cân đối, tường sáng màu, điểm xuyết những mái vòm củ hành và thánh giá vươn lên nền trời, tạo nên vẻ thanh thoát, ấm áp. Bên trong, không gian được trang hoàng với các ảnh thánh (icon), đèn nến và bàn thờ theo đúng truyền thống phụng vụ, là nơi cử hành các buổi lễ, rửa tội, hôn phối và các nghi thức tôn giáo cho cộng đồng giáo dân quanh vùng. Nằm trên trục đường Pushkina ở khu trung tâm, nhà thờ dễ tiếp cận và thường được du khách ghé thăm cùng với Nhà thờ Chính tòa Chúa Hiển Dung và các di tích khác của thành phố, góp phần khắc họa đời sống tôn giáo Chính thống đang hồi sinh mạnh mẽ ở Khakassia đương đại.",
    [
        "Thánh đường Chính thống giáo duyên dáng theo phong cách đền thờ Nga truyền thống.",
        "Mái vòm củ hành, nội thất icon - nến ấm cúng, phục vụ cộng đồng giáo dân.",
        "Vị trí trung tâm, dễ kết hợp tham quan cùng Nhà thờ Chính tòa Abakan.",
    ],
    outdoor_practical(
        "Mở cửa hằng ngày theo giờ lễ (thường sáng và chiều); có thể thay đổi theo lịch phụng vụ.",
        "Miễn phí vào tham quan và dự lễ; có thể tuỳ tâm công đức.",
        "Khoảng 20–30 phút.",
        "Quanh năm; sinh động nhất vào các ngày lễ Chính thống giáo.",
        "Ăn mặc kín đáo, phụ nữ nên trùm khăn; giữ yên lặng và xin phép trước khi chụp ảnh bên trong.",
    ),
    [
        {"title": "sobory.ru — храмы Абакана", "url": "https://sobory.ru/geo/city/Abakan"},
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
    ],
    ["church", "orthodox", "abakan", "religious"],
    maps_text("Церковь Константина и Елены", "Абакан", "Church of Constantine and Helen", "Abakan", 53.718493, 91.463551),
))

# 20) Парк «Сады мечты» -----------------------------------------------------------
RECORDS.append(rec(
    "sady-mechty-park",
    "Công viên «Vườn Mơ Ước» (Xa-đư Métr-tư)",
    "Парк «Сады мечты»",
    "Sady Mechty (Gardens of Dreams) Park",
    ["park_garden"],
    53.741267, 91.433405,
    "Đường Kati Perekreshchenko 11, khu công viên Preobrazhensky, thành phố Abakan, Cộng hoà Khakassia, Nga.",
    "«Vườn Mơ Ước» là công viên cây xanh - vườn cảnh nổi tiếng của Abakan, gây ấn tượng với nghệ thuật cắt tỉa cây (topiary) tạo hình muông thú, nhân vật cổ tích và các tiểu cảnh sinh động. Đây là điểm dạo chơi, chụp ảnh yêu thích của người dân và du khách.",
    "Nằm trong khu công viên Preobrazhensky ở trung tâm Abakan, «Sady Mechty» - «Vườn Mơ Ước» là một trong những không gian xanh được yêu thích nhất thành phố và là niềm tự hào về cảnh quan đô thị của Khakassia. Điểm làm nên tên tuổi của công viên là nghệ thuật cắt tỉa cây bụi và trồng hoa công phu: những khối cây xanh được tạo hình thành muông thú, chim chóc, nhân vật cổ tích và các biểu tượng ngộ nghĩnh, xen giữa là luống hoa nhiều màu, lối đi lát gạch, đài phun nước và các tiểu cảnh trang trí. Vào mùa ấm, công viên rực rỡ sắc hoa và cây lá, trở thành phông nền lý tưởng cho các bức ảnh gia đình, đám cưới và là nơi trẻ em vui chơi, người lớn dạo bộ, nghỉ ngơi. Không gian được chăm chút, sạch đẹp, kết hợp mảng xanh với các khu vực giải trí, quán giải khát tạo cảm giác thư thái ngay giữa lòng thủ phủ. «Vườn Mơ Ước» cùng cụm công viên Preobrazhensky đã biến khu vực này thành điểm đến giải trí - thư giãn nhẹ nhàng, thích hợp cho mọi lứa tuổi và dễ kết hợp trong hành trình khám phá Abakan.",
    [
        "Công viên vườn cảnh trứ danh của Abakan với nghệ thuật cắt tỉa cây (topiary).",
        "Cây tạo hình muông thú, nhân vật cổ tích, xen luống hoa và đài phun nước.",
        "Điểm dạo chơi, chụp ảnh và thư giãn yêu thích cho mọi lứa tuổi.",
    ],
    outdoor_practical(
        "Công viên ngoài trời, dạo chơi tự do; đẹp và đầy đủ dịch vụ nhất vào mùa ấm.",
        "Vào cửa nhìn chung miễn phí; một số trò chơi/dịch vụ trong khu thu phí riêng.",
        "Khoảng 1–1,5 giờ.",
        "Cuối xuân đến đầu thu (tháng 5–9) khi cây lá xanh tốt, hoa nở rộ.",
        "Lý tưởng cho gia đình có trẻ nhỏ; mang máy ảnh; buổi chiều mát mẻ dễ chịu để dạo bộ.",
    ),
    [
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
        {"title": "2GIS — Сады мечты, Абакан", "url": "https://2gis.ru/abakan"},
    ],
    ["park", "garden", "topiary", "family", "abakan"],
    maps_text("Парк Сады мечты", "Абакан", "Sady Mechty Park", "Abakan", 53.741267, 91.433405),
))

# 21) Парк Победы (Абакан) --------------------------------------------------------
RECORDS.append(rec(
    "abakan-victory-park",
    "Công viên Chiến Thắng Abakan (Pác Pa-bê-đư)",
    "Парк Победы (Абакан)",
    "Victory Park (Abakan)",
    ["monument", "park_garden"],
    53.721886, 91.431872,
    "Trung tâm thành phố Abakan, Cộng hoà Khakassia, Nga.",
    "Công viên Chiến Thắng là quần thể tưởng niệm trung tâm của Abakan, tôn vinh những người con Khakassia hy sinh trong Chiến tranh Vệ quốc Vĩ đại. Với đài tưởng niệm, ngọn lửa vĩnh cửu và khí tài trưng bày, đây là nơi diễn ra các nghi lễ trọng thể của thành phố.",
    "Công viên Chiến Thắng (Park Pobedy) là không gian tưởng niệm quan trọng bậc nhất của Abakan, được lập nên để tri ân những người dân Khakassia đã chiến đấu và hy sinh trong Chiến tranh Vệ quốc Vĩ đại (1941–1945). Trung tâm quần thể là đài tưởng niệm cùng ngọn lửa vĩnh cửu, các bia khắc tên và những biểu tượng vinh danh chiến công; xung quanh thường trưng bày khí tài quân sự như pháo, xe và trang bị thời chiến, giúp các thế hệ sau hình dung về một giai đoạn lịch sử bi tráng. Vào các ngày lễ trọng - đặc biệt là Ngày Chiến thắng 9 tháng 5 - nơi đây trở thành tâm điểm của thành phố với lễ đặt hoa, diễu hành và các hoạt động tưởng niệm thu hút đông đảo người dân. Ngày thường, công viên là không gian xanh yên tĩnh để dạo bộ, tưởng nhớ và giáo dục truyền thống cho học sinh. Kết hợp giữa ý nghĩa tưởng niệm sâu sắc và chức năng công viên đô thị, Park Pobedy là điểm dừng chân giàu cảm xúc và ý nghĩa lịch sử khi tham quan trung tâm Abakan.",
    [
        "Quần thể tưởng niệm trung tâm của Abakan tri ân người hy sinh trong Thế chiến II.",
        "Có đài tưởng niệm, ngọn lửa vĩnh cửu và khí tài quân sự trưng bày.",
        "Tâm điểm các nghi lễ trọng thể, đặc biệt Ngày Chiến thắng 9/5.",
    ],
    outdoor_practical(
        "Công viên ngoài trời, mở tự do quanh năm.",
        "Miễn phí.",
        "Khoảng 30–45 phút.",
        "Quanh năm; trang nghiêm và sống động nhất vào dịp 9/5.",
        "Giữ thái độ tôn nghiêm tại khu tưởng niệm; dịp lễ lớn khu vực rất đông, nên đi sớm.",
    ),
    [
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
        {"title": "2GIS — Парк Победы, Абакан", "url": "https://2gis.ru/abakan"},
    ],
    ["memorial", "victory-park", "wwii", "eternal-flame", "abakan"],
    maps_text("Парк Победы", "Абакан", "Victory Park", "Abakan", 53.721886, 91.431872),
))

# 22) Хакасский зоопарк (Абакан) --------------------------------------------------
RECORDS.append(rec(
    "khakassky-zoo",
    "Vườn thú Khakassia - Trung tâm Sinh vật Sống (Da-ô-pác)",
    "Хакасский зоопарк (Центр живой природы)",
    "Khakassky Zoo (Living Nature Centre)",
    ["park_garden"],
    53.680157, 91.427296,
    "Đường Pushkina 200, thành phố Abakan, Cộng hoà Khakassia, Nga.",
    "Vườn thú Khakassia ở Abakan là điểm tham quan gia đình được yêu thích, nơi trưng bày nhiều loài động vật bản địa Siberia lẫn ngoại lai. Đây vừa là nơi giải trí, vừa là trung tâm giáo dục và bảo tồn sinh vật của vùng.",
    "Nằm ở rìa nam thành phố Abakan, Vườn thú Khakassia - còn gọi là Trung tâm Sinh vật Sống - là một trong những điểm đến gia đình được ưa chuộng nhất của thủ phủ. Bộ sưu tập động vật ở đây khá đa dạng, gồm các loài đặc trưng của thiên nhiên Siberia và thảo nguyên Khakassia bên cạnh nhiều loài đến từ những vùng khí hậu khác: thú ăn thịt, hươu nai, chim muông, thú nhỏ và khu vực dành cho các loài quen thuộc với trẻ em. Vườn thú không chỉ phục vụ mục đích tham quan, giải trí mà còn đảm nhận vai trò giáo dục môi trường và bảo tồn - chăm sóc, nhân giống, cứu hộ động vật, đồng thời giúp du khách, nhất là các em nhỏ, hiểu và yêu thiên nhiên hơn. Khuôn viên có lối đi thoáng, khu vui chơi và dịch vụ phục vụ khách tham quan trong ngày. Với vị trí thuận tiện trong thành phố và bầu không khí thân thiện, Vườn thú Khakassia là lựa chọn lý tưởng để thư giãn cùng gia đình, đặc biệt phù hợp khi đi cùng trẻ em trong hành trình khám phá Abakan.",
    [
        "Điểm tham quan gia đình yêu thích ở Abakan, bộ sưu tập động vật đa dạng.",
        "Trưng bày loài bản địa Siberia bên cạnh nhiều loài ngoại lai.",
        "Kết hợp giải trí với giáo dục môi trường và bảo tồn động vật.",
    ],
    outdoor_practical(
        "Mở cửa hằng ngày theo giờ công bố (thường ban ngày, có thể rút ngắn vào mùa lạnh).",
        "Có bán vé vào cổng; thường có ưu đãi cho trẻ em và gia đình.",
        "Khoảng 1,5–2 giờ.",
        "Mùa ấm (tháng 5–9) khi động vật hoạt động nhiều và dạo chơi dễ chịu.",
        "Lý tưởng khi đi cùng trẻ nhỏ; không cho thú ăn ngoài quy định; kiểm tra giờ mở cửa mùa đông.",
    ),
    [
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
        {"title": "2GIS — Хакасский зоопарк, Абакан", "url": "https://2gis.ru/abakan"},
    ],
    ["zoo", "family", "wildlife", "education", "abakan"],
    maps_text("Хакасский зоопарк", "Абакан", "Khakassky Zoo", "Abakan", 53.680157, 91.427296),
))

# 23) Парк культуры и отдыха (Абакан) ---------------------------------------------
RECORDS.append(rec(
    "abakan-city-park",
    "Công viên Văn hoá và Nghỉ ngơi Abakan (Pác Kun-tu-rư)",
    "Парк культуры и отдыха (Абакан)",
    "Abakan City Park of Culture and Rest",
    ["park_garden"],
    53.725102, 91.476619,
    "Đường Katanova 10, thành phố Abakan, Cộng hoà Khakassia, Nga.",
    "Công viên Văn hoá và Nghỉ ngơi là công viên giải trí trung tâm lâu đời của Abakan, với cây xanh, khu trò chơi, vòng đu quay và các hoạt động cộng đồng. Đây là không gian thư giãn quen thuộc của nhiều thế hệ cư dân thành phố.",
    "Là công viên giải trí trung tâm có bề dày lịch sử của Abakan, Park kultury i otdykha (Công viên Văn hoá và Nghỉ ngơi) từ lâu đã là nơi vui chơi, gặp gỡ và nghỉ ngơi quen thuộc của người dân thủ phủ Khakassia. Trong khuôn viên rợp bóng cây là hệ thống trò chơi và thiết bị giải trí - từ vòng đu quay khổng lồ (chiếc «bánh xe ngắm cảnh») cho tầm nhìn bao quát thành phố, đến các trò chơi cho trẻ em, sân khấu ngoài trời và những lối đi dạo mát. Vào mùa hè, công viên nhộn nhịp với các buổi biểu diễn, lễ hội thành phố, hoạt động thiếu nhi và những buổi tối gia đình dạo chơi; mùa đông, một số khu vực chuyển thành sân băng và không gian đón lễ hội mùa lạnh. Không cầu kỳ như vườn cảnh chuyên đề, công viên này ghi điểm bằng sự gần gũi, sống động và vai trò như một «phòng khách ngoài trời» của cả cộng đồng. Nằm trong khu trung tâm, đây là điểm dừng chân thoải mái để cảm nhận nhịp sống thường nhật của Abakan giữa hành trình tham quan.",
    [
        "Công viên giải trí trung tâm lâu đời, «phòng khách ngoài trời» của Abakan.",
        "Có vòng đu quay ngắm cảnh, khu trò chơi trẻ em và sân khấu ngoài trời.",
        "Sôi động với lễ hội mùa hè; một số khu thành sân băng mùa đông.",
    ],
    outdoor_practical(
        "Công viên mở tự do; các trò chơi hoạt động theo giờ và theo mùa.",
        "Vào công viên miễn phí; từng trò chơi/thiết bị giải trí thu phí riêng.",
        "Khoảng 1–1,5 giờ.",
        "Mùa hè cho lễ hội và trò chơi; mùa đông có sân băng và không khí lễ hội.",
        "Mang tiền lẻ cho các trò chơi; phù hợp gia đình có trẻ nhỏ; kiểm tra lịch sự kiện thành phố.",
    ),
    [
        {"title": "Cổng du lịch Khakassia — khakassia.travel", "url": "https://khakassia.travel/"},
        {"title": "2GIS — Парк культуры и отдыха, Абакан", "url": "https://2gis.ru/abakan"},
    ],
    ["park", "amusement", "family", "recreation", "abakan"],
    maps_text("Парк культуры и отдыха", "Абакан", "Abakan City Park", "Abakan", 53.725102, 91.476619),
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
