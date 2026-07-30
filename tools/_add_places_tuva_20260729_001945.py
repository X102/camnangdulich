# -*- coding: utf-8 -*-
"""_add_places_tuva_20260729_001945.py — VÙNG: Cộng hoà Tuva (Республика Тыва)
(lần chạy tự động 2026-07-29).

Bối cảnh: tuva.json hiện có 7 địa điểm (obelisk «Центр Азии», Национальный музей им.
Алдан-Маадыр / Scythian gold, гора Догээ, Убсунурская котловина, Устуу-Хурээ, пески
Цугээр-Элс, этно-курорт Алдын-Булак). Bổ sung 23 địa điểm THẬT SỰ đáng kể còn thiếu →
đưa vùng lên 30. Tuva là vùng thưa dân, hoang sơ nên khai thác mạnh THIÊN NHIÊN, DI SẢN
PHẬT GIÁO và KHẢO CỔ; danh lam nhân tạo tập trung ở thủ phủ Kyzyl.

TRÁNH trùng 7 điểm đã có. KHÔNG thêm lại obelisk «Центр Азии» và Национальный музей.
Lưu ý: «Царская охота» (Tsar's Hunt) nằm trong quần thể Центр Азии nhưng là cụm điêu khắc
RIÊNG (Dashi Namdakov), toạ độ khác obelisk ~90 m → thêm như bản ghi độc lập.

Phân bố loại hình (23 bản ghi mới):
- church (3): Хурээ Цеченлинг (buddhist), Тубтен Шедруб Линг (buddhist, монастырь), Воскресенский собор (православный).
- theatre (3): муз-драм театр им. Кок-оола, Тувгосфилармония им. Халилова, Театр кукол.
- other (4): Центр тувинской традиционной культуры им. Ондара (хоомей), гора Хайыракан (священная),
  массив Монгун-Тайга (высшая точка), курорт-аржаан Уш-Белдир (горячие источники).
- park_garden (8): парк им. Гастелло (город) + 7 озёр (Дус-Холь, Хадын, Чагытай, Сут-Холь, Азас/Тоджа,
  Торе-Холь, Хиндиктиг-Холь).
- monument (3): «Царская охота», Долина царей / курганы Аржаан, петроглифы Мугур-Саргол.
- fortress (1): Пор-Бажын (древнеуйгурская крепость).
- square_street (1): площадь Арата (центральная площадь Кызыла).

TOẠ ĐỘ — xác minh chéo, tất cả trong phạm vi Tuva (lat 49.5–53.8, lon 88.8–99.2), KHÔNG đảo lat/lon:
  Цеченлинг 51.723753,94.450489 (2gis og center); Тубтен Шедруб Линг 51.69133,94.40493 (2gis og);
  Воскресенский собор 51.703611,94.408056 (ru.wikipedia 51°42′13″N 94°24′29″E); театр Кок-оола
  51.719896,94.439133 (2gis og, пл. Арата/Ленина 33); Тувгосфилармония 51.722006,94.433917 (2gis og);
  Театр кукол 51.717931,94.436624 (2gis og); Центр Ондара 51.721516,94.448593 (2gis og, Ленина 7);
  парк Гастелло 51.72209,94.461418 (2gis og); «Царская охота» 51.7249,94.4451 (cyclowiki, набережная);
  площадь Арата 51.719896,94.439133 (2gis, площадь с театром и Домом Правительства); Пор-Бажын
  50.615,97.3861 (ru.wikipedia 50°36′54″N 97°23′10″E); Дус-Холь 51.3625,94.4389 (visittuva/2gis
  51°21′45″N 94°26′20″E); Хадын 51.33528,94.52417 (sib-guide 51°20′07″N 94°31′27″E); Чагытай
  51.0,94.71667 (ru.wikipedia 51°00′N 94°43′E); Сут-Холь 51.51667,91.16528 (sib-guide 51°30′60″N
  91°09′55″E); Азас/Тоджа 52.39417,96.52444 (sib-guide 52°23′39″N 96°31′28″E); Торе-Холь 50.03333,
  95.06667 (ru.wikipedia 50°02′N 95°04′E, Эрзинский кожуун); Хиндиктиг-Холь 50.35472,89.82889
  (ru.wikipedia 50°21′17″N 89°49′44″E); Долина царей / Аржаан 52.084185,93.665095 (2gis geo; курган
  Аржаан-2 52.0555,93.6021); Мугур-Саргол 51.70194,92.28944 (sib-guide 51°42′07″N 92°17′22″E);
  Хайыракан 51.569837,93.000953 (tonkosti GPS, Улуг-Хемский кожуун); Монгун-Тайга 50.27944,90.12
  (ru.wikipedia 50°16′46″N 90°07′12″E, 3976 м); Уш-Белдир 51.46972,98.05472 (ru.wikipedia
  51°28′11″N 98°03′17″E).

GHI CHÚ: đã BỎ QUA vì không xác minh được toạ độ đáng tin: bảo tàng Сафьяновых ở Туран, памятник
Буян-Бадыргы, аржаан Тарыс, Дургенский водопад (không có toạ độ tra cứu chắc chắn — KHÔNG đoán).
Voskresensky собор + 3 chùa xếp category "church" theo quy ước dự án (chùa Phật giáo kèm tag
"buddhist"/"temple"; di chỉ khảo cổ dùng "monument"; hồ/núi/suối khoáng dùng "park_garden"/"other").

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_tuva_20260729_001945.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "tuva"
REGION_NAME_VI = "Cộng hoà Tuva"
FD = "Vùng Siberia"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=15",
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


def p(hours, ticket, duration, best, tips):
    return {"hours_vi": hours, "ticket_vi": ticket, "duration_vi": duration,
            "best_time_vi": best, "tips_vi": tips}


RECORDS = []

# ============================ PHẬT GIÁO & TÔN GIÁO (church) ============================

# 1) Хурээ Цеченлинг -------------------------------------------------------------------
RECORDS.append(rec(
    "tsechenling-buddhist-temple-kyzyl",
    "Chùa Phật giáo Tsechenling (Khuree Tsechenling)",
    "Хурээ Цеченлинг",
    "Tsechenling Buddhist Temple",
    ["church"],
    51.723753, 94.450489,
    "Phố Shchetinkina-Kravchenko 2, trung tâm thành phố Kyzyl, Cộng hoà Tuva, Nga",
    "Ngôi chùa Phật giáo trung tâm của Kyzyl, khánh thành năm 1999, tên tiếng Tây Tạng nghĩa là 'Chốn từ bi vô lượng'. Tường trắng, mái cong kiểu phương Đông và tám bảo tháp trong khuôn viên khiến đây là điểm hành hương và tham quan quen thuộc giữa lòng thủ phủ.",
    "Sau khi gần như toàn bộ chùa chiền ở Tuva bị phá huỷ vào cuối thập niên 1930, Tsechenling là một trong những ngôi chùa Phật giáo được phục dựng đầu tiên và trở thành trung tâm sinh hoạt Phật giáo của cả nước cộng hoà. Chùa được dựng chỉ trong khoảng một năm rưỡi bằng tiền quyên góp của người dân và các tổ chức, viên đá đầu tiên được đặt năm 1998 và chùa khánh thành năm 1999. Kiến trúc mang dáng dấp Tây Tạng - Mông Cổ với tường trắng, mái ngói cong vút ở các góc, cầu thang chính rộng và mặt tiền trang trí giản dị. Trong khuôn viên có tám bảo tháp (suburgan), mỗi tháp gắn với một sự kiện trong cuộc đời Đức Phật. Bên trong, các lạt-ma tiếp nhận khách thập phương, còn tầng dưới từng có lớp học thiền, tiếng Tây Tạng và yoga cùng một quán ăn phục vụ món Tuva. Với du khách, Tsechenling là nơi cảm nhận rõ nhất đời sống Phật giáo Kim Cương thừa đang hồi sinh ở vùng thảo nguyên Trung Á này.",
    [
        "Ngôi chùa Phật giáo trung tâm của Kyzyl, phục dựng năm 1999 sau thời kỳ vô thần.",
        "Tám bảo tháp (suburgan) trong khuôn viên, mỗi tháp ứng với một sự kiện đời Đức Phật.",
        "Nơi trải nghiệm Phật giáo Kim Cương thừa sống động của người Tuva ngay giữa thủ phủ.",
    ],
    p("Thường mở khoảng 09:00-18:00; giờ lễ và giờ tiếp khách có thể thay đổi.",
      "Vào cửa tự do; hoan nghênh quyên góp tuỳ tâm.",
      "Khoảng 30-45 phút.",
      "Quanh năm; dịp lễ Phật giáo (như Shagaa - Tết Tuva) rất sinh động.",
      "Cởi giày và ăn mặc kín đáo khi vào chính điện; đi vòng bảo tháp theo chiều kim đồng hồ; xin phép trước khi chụp ảnh bên trong."),
    [
        {"title": "Wikipedia (RU) — Тувинский буддизм / храмы Кызыла", "url": "https://ru.wikipedia.org/wiki/Буддизм_в_Туве"},
        {"title": "Livingheritage.ru — Буддийский храм «Цеченлинг»", "url": "https://livingheritage.ru/brand/respublika-tyva/buddijskij-hram-cechenling"},
    ],
    ["church", "buddhist", "temple", "kyzyl", "religion", "siberia"],
    maps_text("Хурээ Цеченлинг", "Кызыл", "Tsechenling Buddhist Temple", "Kyzyl", 51.723753, 94.450489),
))

# 2) Тубтен Шедруб Линг ----------------------------------------------------------------
RECORDS.append(rec(
    "tubten-shedrub-ling-monastery-kyzyl",
    "Tu viện Phật giáo Tubten Shedrub Ling",
    "Тубтен Шедруб Линг",
    "Tubten Shedrub Ling Monastery",
    ["church"],
    51.691330, 94.404930,
    "Phố Moskovskaya 72, thành phố Kyzyl, Cộng hoà Tuva, Nga",
    "Tu viện (datsan) Phật giáo lớn nhất nước Nga, khánh thành ngày 28/4/2023 tại Kyzyl. Toà chính điện nhiều tầng cao khoảng 56 m, có bệ thờ dành cho pho tượng Phật cao 10 m, nằm trong khuôn viên rộng gần mười hecta.",
    "Tubten Shedrub Ling - 'Chốn giảng giải và thực hành giáo pháp của Đức Phật Thích Ca' - là ngôi chùa/tu viện Phật giáo lớn nhất Liên bang Nga, được khánh thành ngày 28 tháng 4 năm 2023 và trở thành trung tâm Phật giáo Tuva mới. Công trình bề thế với toà chính điện nhiều tầng, cao khoảng 56 mét, bên trong bố trí bệ và cột để tôn trí pho tượng Phật cao chừng 10 mét, xung quanh là hệ thống hành lang, phòng cầu nguyện và không gian tu học. Toàn khu chiếm gần mười hecta, kết hợp mỹ thuật Phật giáo Tây Tạng với hoạ tiết truyền thống Tuva, tạo nên một quần thể vừa uy nghi vừa gần gũi. Việc xây dựng có sự ủng hộ của Đức Đạt Lai Lạt Ma thứ 14 (người đã đặt tên cho tu viện) và đông đảo phật tử, đánh dấu bước phát triển mạnh mẽ của Phật giáo tại Tuva sau nhiều thập niên gián đoạn. Đây là điểm đến tâm linh và kiến trúc nổi bật bậc nhất của Kyzyl hiện nay.",
    [
        "Tu viện Phật giáo LỚN NHẤT nước Nga, khánh thành 2023, biểu tượng mới của Kyzyl.",
        "Chính điện cao ~56 m, khuôn viên gần 10 hecta, có bệ thờ tượng Phật cao 10 m.",
        "Được Đức Đạt Lai Lạt Ma thứ 14 đặt tên; hoà quyện mỹ thuật Tây Tạng và Tuva.",
    ],
    p("Thường mở cửa ban ngày; nên kiểm tra lịch lễ và giờ mở trước khi đến.",
      "Vào cửa tự do; hoan nghênh cúng dường.",
      "Khoảng 45-60 phút.",
      "Quanh năm; đẹp nhất vào các đại lễ Phật giáo.",
      "Ăn mặc trang nghiêm, cởi giày khi vào điện; giữ yên lặng và tôn trọng nghi lễ đang diễn ra."),
    [
        {"title": "РИА Новости — Крупнейший буддийский монастырь России «Тубтен Шедруб Линг»", "url": "https://ria.ru/20230428/monastyr-1868427236.html"},
        {"title": "Официальный сайт — khuree.ru", "url": "http://khuree.ru/"},
    ],
    ["church", "buddhist", "temple", "monastery", "kyzyl", "siberia"],
    maps_text("Тубтен Шедруб Линг", "Кызыл", "Tubten Shedrub Ling Monastery", "Kyzyl", 51.691330, 94.404930),
    official_site="http://khuree.ru/",
))

# 3) Воскресенский собор ---------------------------------------------------------------
RECORDS.append(rec(
    "voskresensky-cathedral-kyzyl",
    "Nhà thờ chính toà Phục Sinh (Voskresensky)",
    "Воскресенский собор",
    "Resurrection Cathedral",
    ["church"],
    51.703611, 94.408056,
    "Phố Moskovskaya 7, thành phố Kyzyl, Cộng hoà Tuva, Nga",
    "Nhà thờ chính toà của giáo phận Kyzyl thuộc Chính thống giáo Nga, xây dựng 2002-2011. Toà nhà gạch một mái vòm với tháp chuông cao 42 m, sức chứa tới 2.000 người - trung tâm Chính thống giáo lớn nhất Tuva.",
    "Nhà thờ chính toà Phục Sinh là ngôi thánh đường Chính thống giáo trung tâm của Tuva và là nhà thờ mẹ của giáo phận Kyzyl. Lễ đặt viên đá đầu tiên diễn ra ngày 9 tháng 3 năm 2002; công trình từng bị đình lại năm 2005, khởi động lại năm 2009 và hoàn thành năm 2011, đến ngày 31 tháng 8 năm 2011 được Thượng phụ Kirill làm lễ tiểu cung hiến. Đây là một khối nhà gạch lớn kiểu 'chetverik' một mái vòm, có nhà thờ phụ, phòng ăn và tháp chuông, tổng diện tích khoảng 500 m² và chứa được tới 2.000 người. Tháp chuông cao 42 mét (đỉnh thánh giá gần 50 mét) treo 12 quả chuông, quả lớn nhất nặng 3,5 tấn; tường dày tới 1,5 mét. Trong khuôn viên còn có nhà nguyện kính Đức Mẹ Iveron và toà nhà giáo phận nối với nhà thờ bằng đường ngầm. Nhà thờ lưu giữ xá lợi của các thánh Kiev-Pechersk và từ năm 2019 bắt đầu có các buổi lễ bằng tiếng Tuva - nét độc đáo phản ánh sự giao thoa văn hoá nơi đây.",
    [
        "Nhà thờ chính toà Chính thống giáo lớn nhất Tuva, xây 2002-2011, chứa tới 2.000 người.",
        "Tháp chuông cao 42 m với 12 quả chuông, quả lớn nhất nặng 3,5 tấn.",
        "Lưu giữ xá lợi các thánh Kiev-Pechersk; có các buổi lễ bằng tiếng Tuva từ 2019.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm đến tối.",
      "Vào cửa tự do.",
      "Khoảng 20-40 phút.",
      "Quanh năm; dịp lễ Phục Sinh và Giáng Sinh Chính thống giáo đặc biệt trang trọng.",
      "Nữ nên trùm khăn đầu và mặc váy dài; tránh chụp ảnh trong giờ hành lễ."),
    [
        {"title": "Wikipedia (RU) — Воскресенский собор (Кызыл)", "url": "https://ru.wikipedia.org/wiki/Воскресенский_собор_(Кызыл)"},
        {"title": "Кызыльская епархия — sobortuva.cerkov.ru", "url": "http://sobortuva.cerkov.ru/"},
    ],
    ["church", "orthodox", "cathedral", "kyzyl", "religion", "siberia"],
    maps_text("Воскресенский собор", "Кызыл", "Resurrection Cathedral", "Kyzyl", 51.703611, 94.408056),
))

# ============================ NHÀ HÁT & BIỂU DIỄN (theatre) ============================

# 4) Тувинский музыкально-драматический театр им. В. Кок-оола --------------------------
RECORDS.append(rec(
    "kok-ool-music-drama-theatre-kyzyl",
    "Nhà hát Nhạc kịch Quốc gia Tuva mang tên V. Kok-ool",
    "Национальный музыкально-драматический театр им. В. Кок-оола",
    "Kok-ool National Music and Drama Theatre",
    ["theatre"],
    51.719896, 94.439133,
    "Quảng trường Arat, phố Lenina 33, trung tâm thành phố Kyzyl, Cộng hoà Tuva, Nga",
    "Nhà hát kịch chuyên nghiệp duy nhất của Tuva, thành lập năm 1936, mang tên nghệ sĩ - nhà viết kịch Viktor Kok-ool. Toà nhà bề thế ngay quảng trường Arat là trung tâm nghệ thuật sân khấu hàng đầu của nước cộng hoà.",
    "Nhà hát Nhạc kịch Quốc gia Tuva khởi nguồn từ một xưởng kịch dân tộc lập ở Kyzyl năm 1935-1936 và ngày nay là nhà hát kịch chuyên nghiệp duy nhất của cả nước cộng hoà, mang tên Viktor Shogzhapovich Kok-ool - diễn viên, nhà viết kịch Tuva được phong Nghệ sĩ công huân RSFSR. Suốt hơn tám thập niên, đây là trung tâm dẫn dắt nghệ thuật sân khấu Tuva, dàn dựng cả kịch nói, nhạc kịch lẫn các vở lấy cảm hứng từ sử thi, truyền thuyết và đời sống du mục bản địa. Toà nhà nằm ngay quảng trường Arat - trái tim hành chính và văn hoá của Kyzyl - với kiến trúc bề thế, sân khấu lớn, sân khấu nhỏ và cả không gian 'lều yurt' để biểu diễn thể nghiệm. Nhà hát thường xuyên lưu diễn khắp các huyện và mang chương trình dành cho thiếu nhi đến trường học. Với du khách, một buổi diễn ở đây - dù không hiểu hết lời thoại - vẫn là cách sinh động để tiếp cận âm nhạc, trang phục và tinh thần sân khấu Tuva.",
    [
        "Nhà hát kịch chuyên nghiệp DUY NHẤT của Tuva, thành lập 1936.",
        "Mang tên Viktor Kok-ool, biểu tượng của nghệ thuật sân khấu dân tộc Tuva.",
        "Toạ lạc ngay quảng trường Arat, trung tâm văn hoá - hành chính của Kyzyl.",
    ],
    p("Theo lịch diễn, thường buổi tối; phòng vé mở ban ngày.",
      "Giá vé phải chăng, tuỳ chương trình và vị trí ghế.",
      "Một buổi diễn khoảng 1,5-3 giờ.",
      "Quanh năm; mùa diễn chính từ thu đến xuân.",
      "Xem lịch và đặt vé trước trên trang nhà hát; phần lớn vở diễn bằng tiếng Tuva/Nga."),
    [
        {"title": "Culture.ru — Национальный музыкально-драматический театр Республики Тыва им. В. Кок-оола", "url": "https://www.culture.ru/institutes/10824/nacionalnyi-muzykalno-dramaticheskii-teatr-respubliki-tyva-im-v-kok-oola"},
        {"title": "Официальный сайт — theatre-tuva.ru", "url": "http://theatre-tuva.ru/"},
    ],
    ["theatre", "drama", "music", "kyzyl", "culture", "siberia"],
    maps_text("Театр им. Кок-оола", "Кызыл", "Kok-ool National Music and Drama Theatre", "Kyzyl", 51.719896, 94.439133),
    official_site="http://theatre-tuva.ru/",
))

# 5) Тувгосфилармония им. В.М. Халилова ------------------------------------------------
RECORDS.append(rec(
    "tuva-state-philharmonic-kyzyl",
    "Nhà hát Giao hưởng Quốc gia Tuva mang tên V. Khalilov",
    "Тувинская государственная филармония им. В.М. Халилова",
    "Tuva State Philharmonic named after V. Khalilov",
    ["theatre"],
    51.722006, 94.433917,
    "Phố Shchetinkina-Kravchenko 58, trung tâm thành phố Kyzyl, Cộng hoà Tuva, Nga",
    "Trung tâm hoà nhạc chính của Tuva, mang tên nhạc trưởng quân đội Valery Khalilov. Đây là sân khấu chủ lực cho nhạc dân tộc, hát đồng song thanh khoomei và các tập thể nghệ thuật danh tiếng của nước cộng hoà.",
    "Nhà hát Giao hưởng Quốc gia Tuva là nơi quy tụ và trình diễn âm nhạc chuyên nghiệp của nước cộng hoà, mang tên Valery Mikhailovich Khalilov - nhạc trưởng, nhà soạn nhạc quân đội Nga. Trên sân khấu này, du khách có thể nghe những gì tinh tuý nhất của âm nhạc Tuva: nghệ thuật hát đồng song thanh khoomei (throat singing) đặc trưng vùng thảo nguyên, các nhạc cụ dân tộc như igil, doshpuluur, byzaanchy, cùng những chương trình hoà nhạc hàn lâm và dân gian. Nhiều tập thể nổi tiếng thế giới gắn bó với đời sống biểu diễn nơi đây, đưa tiếng hát 'từ cổ họng' của Tuva ra khắp năm châu. Toà nhà nằm ở khu trung tâm Kyzyl, gần quảng trường Arat và cụm công trình văn hoá, thuận tiện kết hợp tham quan. Một buổi khoomei sống động tại nhà hát thường là trải nghiệm âm nhạc khó quên nhất trong hành trình đến Tuva.",
    [
        "Trung tâm hoà nhạc chính của Tuva, nơi nghe hát đồng song thanh khoomei chuẩn mực.",
        "Mang tên nhạc trưởng Valery Khalilov; sân khấu của nhiều tập thể nghệ thuật danh tiếng.",
        "Vị trí trung tâm Kyzyl, gần quảng trường Arat và cụm công trình văn hoá.",
    ],
    p("Theo lịch biểu diễn, thường buổi tối; phòng vé mở ban ngày.",
      "Giá vé phải chăng, tuỳ chương trình.",
      "Một buổi diễn khoảng 1-2 giờ.",
      "Quanh năm; nhiều sự kiện vào dịp lễ hội dân tộc.",
      "Ưu tiên các chương trình có khoomei; đặt vé trước qua trang tuvafil.ru."),
    [
        {"title": "Официальный сайт — tuvafil.ru", "url": "http://tuvafil.ru/"},
        {"title": "Министерство культуры Республики Тыва — Тувинская филармония", "url": "http://culture.rtyva.ru/"},
    ],
    ["theatre", "philharmonic", "khoomei", "throat-singing", "kyzyl", "music"],
    maps_text("Тувгосфилармония им. Халилова", "Кызыл", "Tuva State Philharmonic", "Kyzyl", 51.722006, 94.433917),
    official_site="http://tuvafil.ru/",
))

# 6) Театр кукол ----------------------------------------------------------------------
RECORDS.append(rec(
    "tuva-puppet-theatre-kyzyl",
    "Nhà hát Múa rối Tuva",
    "Тувинский театр кукол",
    "Tuva Puppet Theatre",
    ["theatre"],
    51.717931, 94.436624,
    "Phố Druzhby 170, trung tâm thành phố Kyzyl, Cộng hoà Tuva, Nga",
    "Nhà hát múa rối của Kyzyl, điểm đến gia đình dàn dựng các vở dựa trên truyện cổ, sử thi và thần thoại Tuva. Một cách nhẹ nhàng, giàu màu sắc để trẻ em và du khách làm quen với văn hoá dân gian bản địa.",
    "Nhà hát Múa rối Tuva là sân khấu dành cho thiếu nhi và gia đình ở trung tâm Kyzyl, chuyên dàn dựng những vở diễn lấy cảm hứng từ truyện cổ tích, sử thi anh hùng và thần thoại của người Tuva cũng như kho tàng cổ tích thế giới. Bằng ngôn ngữ con rối sinh động, âm nhạc dân tộc và tạo hình rực rỡ, nhà hát biến các truyền thuyết thảo nguyên thành những câu chuyện dễ tiếp cận, gần gũi với trẻ nhỏ. Đây cũng là nơi ươm mầm tình yêu sân khấu và bản sắc dân tộc cho thế hệ trẻ, đồng thời tổ chức nhiều chương trình lưu động, liên hoan. Với khách du lịch đi cùng con nhỏ, một buổi diễn ở đây là điểm dừng thư giãn, đầy màu sắc và mang đậm hồn văn hoá Tuva - không cần hiểu hết lời thoại vẫn cảm nhận được.",
    [
        "Sân khấu múa rối gia đình dựa trên truyện cổ, sử thi và thần thoại Tuva.",
        "Tạo hình rực rỡ, âm nhạc dân tộc - phù hợp du khách đi cùng trẻ nhỏ.",
        "Nơi nuôi dưỡng tình yêu sân khấu và bản sắc cho thế hệ trẻ Tuva.",
    ],
    p("Theo lịch diễn, thường vào cuối tuần và các buổi dành cho thiếu nhi.",
      "Vé rẻ, phù hợp gia đình.",
      "Một buổi diễn khoảng 45-60 phút.",
      "Quanh năm; nhiều suất vào dịp nghỉ học và lễ hội.",
      "Xem lịch trước; các vở chủ yếu bằng tiếng Tuva/Nga nhưng hình ảnh rất dễ theo dõi."),
    [
        {"title": "2ГИС — Театр кукол, Кызыл", "url": "https://2gis.ru/kyzyl/firm/70000001027042811"},
        {"title": "Quicktickets — Тувинский театр кукол", "url": "https://quicktickets.ru/kyzyl-teatr-kukol"},
    ],
    ["theatre", "puppet", "family", "kyzyl", "culture", "siberia"],
    maps_text("Театр кукол", "Кызыл", "Tuva Puppet Theatre", "Kyzyl", 51.717931, 94.436624),
))

# ============================ VĂN HOÁ, NÚI THIÊNG & SUỐI KHOÁNG (other) ================

# 7) Центр развития тувинской традиционной культуры и ремёсел им. К.Б. Ондара ----------
RECORDS.append(rec(
    "ondar-tuvan-culture-center-kyzyl",
    "Trung tâm Văn hoá và Thủ công truyền thống Tuva (mang tên K. Ondar)",
    "Центр развития тувинской традиционной культуры и ремёсел им. К.Б. Ондара",
    "Centre for the Development of Tuvan Traditional Culture and Crafts",
    ["other"],
    51.721516, 94.448593,
    "Phố Lenina 7, trung tâm thành phố Kyzyl, Cộng hoà Tuva, Nga",
    "Trung tâm gìn giữ và lan toả văn hoá Tuva, do bậc thầy khoomei Kongar-ool Ondar sáng lập năm 2008. Nơi đặt Dàn nhạc Dân tộc Tuva và trung tâm khoa học 'Khoomei', đồng thời trưng bày, dạy nghề thủ công và tổ chức biểu diễn hát đồng song thanh.",
    "Trung tâm Văn hoá truyền thống Tuva được thành lập năm 2008 theo sáng kiến của Kongar-ool Ondar - nghệ nhân hát đồng song thanh (khoomei) lừng danh - nhằm bảo tồn và phát triển di sản phong phú của dân tộc Tuva; năm 2012 trung tâm chuyển về toà nhà mới ở phố Lenina. Đây là 'ngôi nhà chung' của nhiều thành tố cốt lõi trong văn hoá Tuva: Dàn nhạc Dân tộc Tuva, trung tâm nghiên cứu khoa học 'Khoomei' chuyên về nghệ thuật hát cổ họng, các xưởng chế tác trang phục và nhạc cụ dân tộc, cùng những nhóm nghệ thuật dân gian nổi tiếng. Khách đến đây có thể tìm hiểu kỹ thuật khoomei, ngắm nhạc cụ truyền thống như igil hay doshpuluur, xem thợ thủ công làm việc và đôi khi bắt gặp các buổi tập, buổi diễn. Trung tâm nằm ngay khu trung tâm Kyzyl, gần bảo tàng quốc gia và các chùa, thuận tiện kết hợp trong hành trình khám phá bản sắc Tuva. Đây là một trong những nơi tốt nhất để 'chạm' vào linh hồn âm nhạc và thủ công của vùng đất này.",
    [
        "Do bậc thầy khoomei Kongar-ool Ondar sáng lập (2008) để giữ gìn văn hoá Tuva.",
        "Nơi đặt Dàn nhạc Dân tộc Tuva và trung tâm khoa học 'Khoomei' về hát đồng song thanh.",
        "Xưởng chế tác nhạc cụ, trang phục dân tộc và điểm tìm hiểu nghệ thuật cổ họng.",
    ],
    p("Thường mở khoảng 08:30-17:30, nghỉ trưa; nên gọi/hỏi trước về sự kiện.",
      "Tham quan thường miễn phí hoặc phí nhỏ; workshop/biểu diễn có thể thu phí.",
      "Khoảng 45-60 phút.",
      "Quanh năm; dịp lễ hội dân tộc và liên hoan khoomei rất đáng xem.",
      "Hỏi trước lịch biểu diễn/lớp học khoomei để canh giờ; nằm gần bảo tàng quốc gia."),
    [
        {"title": "Официальный сайт — tuvancenter.ru", "url": "https://tuvancenter.ru/istoriya-czentra/"},
        {"title": "Ituva.ru — Центр развития тувинской традиционной культуры и ремёсел", "url": "https://www.ituva.ru/tourism/9/"},
    ],
    ["other", "culture", "khoomei", "throat-singing", "crafts", "kyzyl"],
    maps_text("Центр тувинской культуры им. Ондара", "Кызыл", "Centre for Tuvan Traditional Culture and Crafts", "Kyzyl", 51.721516, 94.448593),
    official_site="https://tuvancenter.ru/",
))

# 8) Национальный парк культуры и отдыха им. Н. Гастелло ------------------------------
RECORDS.append(rec(
    "gastello-city-park-kyzyl",
    "Công viên Văn hoá và Nghỉ ngơi Quốc gia mang tên N. Gastello",
    "Национальный парк культуры и отдыха им. Н. Гастелло",
    "Gastello National Park of Culture and Leisure",
    ["park_garden"],
    51.722090, 94.461418,
    "Phố Kochetova 1а, thành phố Kyzyl, Cộng hoà Tuva, Nga",
    "Công viên giải trí trung tâm của Kyzyl, mang tên phi công anh hùng Nikolai Gastello. Không gian xanh với các trò chơi, khu đi dạo và sự kiện lễ hội - điểm thư giãn quen thuộc của người dân thủ phủ.",
    "Công viên Văn hoá và Nghỉ ngơi mang tên Nikolai Gastello là công viên giải trí chính của Kyzyl, nơi người dân thành phố tìm đến để đi dạo, vui chơi và nghỉ ngơi giữa những hàng cây. Trong công viên có các trò chơi, vòng đu quay, khu vui chơi thiếu nhi cùng những lối đi bộ râm mát, và vào các dịp lễ hội nơi đây trở thành sân khấu ngoài trời cho những sự kiện văn hoá, âm nhạc của nước cộng hoà. Đối với một thành phố nằm giữa vùng thảo nguyên - núi non khắc nghiệt, mảng xanh và không gian sinh hoạt cộng đồng như thế này có ý nghĩa quan trọng. Với du khách, công viên là nơi cảm nhận nhịp sống thường nhật, đời thường của người Kyzyl, thích hợp để thư giãn sau khi tham quan các bảo tàng và chùa chiền lân cận. Vào mùa hè, đây là điểm dạo chơi dễ chịu; mùa đông, không khí lễ hội cũng thường tụ về đây.",
    [
        "Công viên giải trí trung tâm của Kyzyl, mang tên phi công anh hùng N. Gastello.",
        "Trò chơi, đu quay, khu thiếu nhi và lối đi bộ xanh mát giữa lòng thành phố.",
        "Sân khấu ngoài trời cho nhiều sự kiện, lễ hội văn hoá của nước cộng hoà.",
    ],
    p("Không gian ngoài trời, thường mở cả ngày; các trò chơi hoạt động theo mùa.",
      "Vào cửa tự do; từng trò chơi thu phí riêng.",
      "Khoảng 45-90 phút.",
      "Đẹp nhất mùa hè (tháng 6-9); dịp lễ có nhiều hoạt động.",
      "Kết hợp dạo chơi khi tham quan trung tâm Kyzyl; mang tiền lẻ cho các trò chơi."),
    [
        {"title": "2ГИС — Национальный парк культуры и отдыха им. Н. Гастелло", "url": "https://2gis.ru/kyzyl/firm/70000001027139215"},
        {"title": "kntuva.ru — парк им. Гастелло", "url": "https://kntuva.ru/org/6/"},
    ],
    ["park_garden", "park", "city-park", "kyzyl", "leisure", "siberia"],
    maps_text("Парк им. Гастелло", "Кызыл", "Gastello Park of Culture and Leisure", "Kyzyl", 51.722090, 94.461418),
))

# ============================ ĐIÊU KHẮC & KHẢO CỔ (monument) ===========================

# 9) Скульптурная композиция «Царская охота» -----------------------------------------
RECORDS.append(rec(
    "tsars-hunt-sculpture-kyzyl",
    "Cụm điêu khắc 'Cuộc săn của Nhà vua' (Tsarskaya Okhota)",
    "Скульптурная композиция «Царская охота»",
    "The Royal Hunt sculpture",
    ["monument"],
    51.724900, 94.445100,
    "Bờ kè sông Yenisei, quần thể 'Trung tâm châu Á', trung tâm thành phố Kyzyl, Cộng hoà Tuva, Nga",
    "Cụm tượng đồng của nghệ sĩ Dashi Namdakov trên bờ kè Yenisei, tái hiện cảnh săn chim ưng của một vị vua và hoàng hậu Scythia. Tác phẩm từng được trưng bày ở Ý và mang về Kyzyl năm 2014, nằm cạnh đài Trung tâm châu Á.",
    "'Cuộc săn của Nhà vua' là cụm điêu khắc đồng do nghệ sĩ người Buryat Dashi Namdakov sáng tác, tái hiện một khoảnh khắc săn chim ưng - nghi lễ thiêng liêng của giới quý tộc du mục Trung Á cổ đại. Trên bệ đá hai tầng, hình tượng đôi kỵ sĩ nam - nữ (nhà vua và hoàng hậu - nữ chiến binh Amazon) phi ngựa, tay nâng chim ưng, phía trước là con báo lao về phía con mồi, gợi lại thế giới thần thoại của các bộ tộc Scythia từng chôn cất vua chúa ngay tại 'Thung lũng các vị vua' của Tuva. Tác phẩm được đúc tại các xưởng nghệ thuật danh tiếng ở Pietrasanta (Ý), từng trưng bày tại quảng trường Piazza del Duomo và mang về Kyzyl vào tháng 1 năm 2014, đặt trên bờ kè Yenisei trong quần thể 'Trung tâm châu Á'. Cùng với đài Trung tâm châu Á kề bên (cũng do Namdakov thiết kế lại), cụm tượng tạo nên một điểm nhấn nghệ thuật lộng lẫy bên dòng sông, đặc biệt đẹp lúc hoàng hôn.",
    [
        "Cụm tượng đồng của Dashi Namdakov, tái hiện cảnh săn chim ưng của vua - hoàng hậu Scythia.",
        "Từng trưng bày ở Pietrasanta (Ý), mang về Kyzyl năm 2014, đặt bên bờ Yenisei.",
        "Điểm nhấn nghệ thuật của quần thể 'Trung tâm châu Á', đẹp nhất lúc hoàng hôn.",
    ],
    p("Ngoài trời, tham quan tự do 24/7.",
      "Miễn phí.",
      "Khoảng 15-30 phút.",
      "Cuối chiều đến hoàng hôn mùa hè (tháng 6-9).",
      "Kết hợp với đài Trung tâm châu Á và dạo bờ kè Yenisei ngay cạnh; mùa đông rất lạnh, mặc ấm."),
    [
        {"title": "Циклопедия — Царская охота (Кызыл)", "url": "https://cyclowiki.org/wiki/Царская_охота_(Кызыл)"},
        {"title": "Ituva.ru — Скульптурная композиция «Царская охота»", "url": "https://ituva.ru/tourism/1/"},
    ],
    ["monument", "sculpture", "scythian", "yenisei", "kyzyl", "art"],
    maps_text("Царская охота", "Кызыл", "The Royal Hunt sculpture", "Kyzyl", 51.724900, 94.445100),
))

# 10) Долина царей / курганы Аржаан ---------------------------------------------------
RECORDS.append(rec(
    "valley-of-kings-arzhaan-kurgans",
    "Thung lũng các vị vua - cụm gò mộ Scythia Arzhaan",
    "Долина царей (курганы Аржаан)",
    "Valley of the Kings (Arzhaan Scythian kurgans)",
    ["monument"],
    52.084185, 93.665095,
    "Gần làng Arzhaan, thung lũng Turan-Uyuk, huyện Piy-Khem, Cộng hoà Tuva, Nga",
    "Quần thể gò mộ (kurgan) hoàng gia Scythia thế kỷ IX-VII trước Công nguyên ở thung lũng Uyuk - được mệnh danh 'Thung lũng các vị vua' của Tuva. Nơi phát lộ kho vàng Scythia lừng danh trong kurgan Arzhaan-2.",
    "Trải dài trong thung lũng Turan-Uyuk phía bắc Kyzyl là 'Thung lũng các vị vua' của Tuva - một trong những cụm di chỉ khảo cổ quan trọng bậc nhất về văn hoá Scythia sơ kỳ. Ở đây tập trung nhiều gò mộ hoàng gia khổng lồ (kurgan) có niên đại thế kỷ IX-VII trước Công nguyên, đường kính lên tới 80-120 mét, được đắp bằng gỗ, đất và đá với cấu trúc bên trong phức tạp. Kurgan Arzhaan-1 từng gây chấn động giới khảo cổ, nhưng nổi tiếng nhất là Arzhaan-2: cuộc khai quật năm 2001 phát lộ mộ 'vua' và 'hoàng hậu' cùng hơn 20 kg đồ trang sức vàng tinh xảo theo phong cách 'thú vật' Scythia-Siberia - phần lớn hiện được trưng bày tại Bảo tàng Quốc gia Tuva ở Kyzyl. Các đoàn khảo cổ quốc tế vẫn tiếp tục nghiên cứu tại đây (như kurgan Tunnug-1). Với du khách, khung cảnh là những gò đất và thảo nguyên mênh mông - vẻ đẹp nằm ở bề dày lịch sử và câu chuyện về nền văn minh du mục Á-Âu hơn là ở công trình phô trương.",
    [
        "Cụm gò mộ hoàng gia Scythia thế kỷ IX-VII TCN - 'Thung lũng các vị vua' của Tuva.",
        "Kurgan Arzhaan-2 phát lộ hơn 20 kg vàng Scythia theo phong cách 'thú vật' (2001).",
        "Di sản khảo cổ tầm cỡ thế giới; hiện vật trưng bày tại Bảo tàng Quốc gia Tuva.",
    ],
    p("Di chỉ ngoài trời trong thảo nguyên, tham quan tự do; nên đi cùng hướng dẫn.",
      "Miễn phí; kho vàng xem tại Bảo tàng Quốc gia ở Kyzyl (có vé).",
      "Khoảng 1-2 giờ nếu kết hợp di chuyển.",
      "Mùa hè (tháng 6-9) khi thảo nguyên khô ráo, dễ đi.",
      "Cần xe khá gầm cao và nên có người bản địa dẫn đường; hiện trường chủ yếu là gò đất, nên tìm hiểu trước để cảm nhận giá trị."),
    [
        {"title": "Российская газета — Загадки тувинской Долины царей", "url": "https://rg.ru/2024/09/20/reg-sibfo/zagadki-tuvinskoj-doliny-carej.html"},
        {"title": "Wikipedia (RU) — Аржан (курган)", "url": "https://ru.wikipedia.org/wiki/Аржан"},
    ],
    ["monument", "archaeology", "scythian", "kurgan", "piy-khem", "history"],
    maps_text("Долина царей Аржаан", "Тыва", "Valley of the Kings Arzhaan", "Tuva", 52.084185, 93.665095),
))

# 11) Петроглифы Мугур-Саргол ---------------------------------------------------------
RECORDS.append(rec(
    "mugur-sargol-petroglyphs",
    "Bãi khắc đá cổ Mugur-Sargol",
    "Петроглифы Мугур-Саргол",
    "Mugur-Sargol petroglyphs",
    ["monument"],
    51.701940, 92.289440,
    "Tả ngạn sông Yenisei (Ulug-Khem), gần cửa suối Mugur-Sargol, huyện Ulug-Khemsky, Cộng hoà Tuva, Nga",
    "Một trong những bảo tàng đá ngoài trời quan trọng nhất Trung Á, với hàng nghìn hình khắc đá (petroglyph) khắc trên các phiến đá bên sông Yenisei. Kho tư liệu quý về nghệ thuật và tín ngưỡng của các cư dân cổ vùng thảo nguyên.",
    "Mugur-Sargol là một trong những quần thể tranh khắc đá (petroglyph) nổi tiếng và phong phú nhất của Tuva và cả Trung Á, nằm bên tả ngạn dòng Yenisei thượng nguồn (Ulug-Khem). Trên các phiến đá và vách đá ở đây lưu giữ hàng nghìn hình khắc trải nhiều thời kỳ: hình thú (dê núi, hươu, bò tót), cảnh săn bắn, người, mặt nạ - thần linh và những biểu tượng nghi lễ, phản ánh đời sống tinh thần của cư dân du mục cổ. Đây được xem như một 'bảo tàng đá ngoài trời', nguồn tư liệu vô giá để nghiên cứu nghệ thuật, tín ngưỡng và lịch sử vùng Sayan-Altai. Một phần di chỉ nằm trong khu vực chịu ảnh hưởng của hồ chứa Sayano-Shushenskoye, khiến việc bảo tồn càng cấp thiết. Với du khách yêu khảo cổ, Mugur-Sargol mang lại cảm giác đối thoại trực tiếp với những nghệ nhân vô danh của hàng nghìn năm trước, giữa khung cảnh sông núi hoang sơ.",
    [
        "Hàng nghìn hình khắc đá (petroglyph) nhiều thời kỳ bên sông Yenisei.",
        "Hình thú, cảnh săn, mặt nạ - thần linh: 'bảo tàng đá ngoài trời' của Trung Á.",
        "Tư liệu quý về nghệ thuật và tín ngưỡng của cư dân du mục cổ vùng Sayan-Altai.",
    ],
    p("Di chỉ ngoài trời, hẻo lánh; tham quan nên có hướng dẫn và phương tiện phù hợp.",
      "Miễn phí; chi phí chủ yếu là di chuyển/hướng dẫn.",
      "Khoảng 1-2 giờ tại chỗ.",
      "Mùa hè khi mực nước thấp và đường khô ráo.",
      "Đường khó tiếp cận, nên đi tour chuyên đề; tuyệt đối không chạm/khắc lên hình đá cổ."),
    [
        {"title": "Sib-guide.ru — Петроглифы Мугур-Саргол", "url": "https://sib-guide.ru/siberia/di/156"},
        {"title": "Wikipedia (RU) — Петроглифы Тувы", "url": "https://ru.wikipedia.org/wiki/Мугур-Саргол"},
    ],
    ["monument", "petroglyphs", "archaeology", "rock-art", "yenisei", "history"],
    maps_text("Петроглифы Мугур-Саргол", "Тыва", "Mugur-Sargol petroglyphs", "Tuva", 51.701940, 92.289440),
))

# ============================ THÀNH LUỸ (fortress) ===================================

# 12) Крепость Пор-Бажын --------------------------------------------------------------
RECORDS.append(rec(
    "por-bazhyn-fortress-tere-khol",
    "Pháo đài cổ Por-Bazhyn trên hồ Tere-Khol",
    "Крепость Пор-Бажын",
    "Por-Bazhyn Fortress",
    ["fortress"],
    50.615000, 97.386100,
    "Đảo giữa hồ Tere-Khol, huyện Tere-Kholsky, Cộng hoà Tuva, Nga",
    "Di tích pháo đài - cung điện của Hãn quốc Uyghur, xây khoảng năm 777 sau Công nguyên, nằm trên một hòn đảo giữa hồ Tere-Khol hẻo lánh. Di sản văn hoá cấp liên bang, một trong những công trình đất cổ ấn tượng nhất Siberia.",
    "Por-Bazhyn (tiếng Tuva nghĩa là 'nhà đất sét') là tàn tích một pháo đài - cung điện được khởi công vào mùa hè năm 777 dưới thời Hãn quốc Uyghur thứ ba, đời Bögü Qaghan. Công trình hình chữ nhật gần như vuông vắn, trải dài khoảng 211 m theo hướng đông - tây và 158 m bắc - nam, với hệ thống tường thành, cổng có tháp gác và mạng lưới sân trong phức tạp; tường ngoài dày hơn 10 m, có chỗ còn cao tới hơn 9 m, được xây bằng gạch mộc. Điều kỳ lạ và cuốn hút nhất là toàn bộ pháo đài toạ lạc trên một hòn đảo giữa hồ Tere-Khol, ở độ cao khoảng 1.300 m giữa vùng núi non hiểm trở - muốn đến chỉ có thể đi bằng đường không hoặc xe địa hình vào mùa khô. Di chỉ được phát hiện năm 1891, khai quật quy mô lớn thập niên 1950-1960 rồi lại tiếp tục năm 2007 (chuyến thăm của Tổng thống Nga và Hoàng thân Monaco cùng năm khiến nơi này nổi tiếng cả nước). Năm 1995, Por-Bazhyn được công nhận là di tích cấp liên bang. Chính sự cô lập đã giúp nó bảo tồn tốt và trở thành một trong những bí ẩn khảo cổ hấp dẫn nhất Siberia.",
    [
        "Pháo đài - cung điện Uyghur xây khoảng năm 777, trên đảo giữa hồ Tere-Khol.",
        "Tường đất dày trên 10 m, quy mô 211x158 m; di sản văn hoá cấp liên bang.",
        "Vị trí cô lập ở độ cao ~1.300 m - bí ẩn khảo cổ nổi tiếng bậc nhất Siberia.",
    ],
    p("Di chỉ hoang sơ, không có hạ tầng du lịch thường trực; tiếp cận rất khó.",
      "Không thu phí tại chỗ; chi phí lớn nằm ở việc di chuyển (máy bay/trực thăng hoặc xe địa hình).",
      "Chuyến đi thường trọn ngày hoặc nhiều ngày.",
      "Chỉ khả thi vào mùa khô/ấm; mùa đông gần như không thể tiếp cận.",
      "Phải tổ chức qua tour chuyên biệt và người dẫn địa phương; chuẩn bị hậu cần kỹ, đây là vùng cực kỳ hẻo lánh gần biên giới Mông Cổ."),
    [
        {"title": "Wikipedia (RU) — Пор-Бажын", "url": "https://ru.wikipedia.org/wiki/Пор-Бажын"},
        {"title": "Livingheritage.ru — Крепость Пор-Бажын на озере Тере-Холь", "url": "https://livingheritage.ru/brand/respublika-tyva/krepost-por-bazhyn-na-ozere-tere-hol"},
    ],
    ["fortress", "archaeology", "uyghur", "tere-khol", "heritage", "siberia"],
    maps_text("Крепость Пор-Бажын", "Тыва", "Por-Bazhyn Fortress", "Tuva", 50.615000, 97.386100),
))

# ============================ HỒ & THIÊN NHIÊN (park_garden) ==========================

# 13) Озеро Дус-Холь (Сватиково) ------------------------------------------------------
RECORDS.append(rec(
    "dus-khol-salt-lake",
    "Hồ nước mặn Dus-Khol (Svatikovo)",
    "Озеро Дус-Холь (Сватиково)",
    "Dus-Khol (Svatikovo) salt lake",
    ["park_garden"],
    51.362500, 94.438900,
    "Bồn địa Tuva, huyện Tandinsky, cách Kyzyl khoảng 45 km về phía nam, Cộng hoà Tuva, Nga",
    "Hồ nước mặn nổi tiếng của Tuva, được ví như 'Biển Chết' nhờ nước mặn đến mức nâng người nổi và lớp bùn khoáng chữa bệnh. Điểm nghỉ dưỡng - trị liệu được ưa chuộng giữa vùng bán hoang mạc trung tâm.",
    "Dus-Khol - tiếng Tuva nghĩa là 'hồ muối' - còn gọi là Svatikovo, là hồ nước mặn khép kín nằm trong một bồn địa khô hạn ở trung tâm bồn địa Tuva, cách Kyzyl khoảng 45 km về phía nam. Độ mặn rất cao khiến nước có sức nâng lớn, du khách có thể nằm nổi thoải mái trên mặt hồ tương tự Biển Chết, còn lớp bùn đen đáy hồ giàu khoáng được cho là có tác dụng trị liệu cho da và khớp. Nhờ đó nơi đây từ lâu là điểm nghỉ dưỡng dân dã được người Tuva và du khách gần xa ưa chuộng vào mùa hè, với vài cơ sở nghỉ chân ven hồ. Cảnh quan xung quanh là thảo nguyên - bán hoang mạc bằng phẳng, bờ hồ thoai thoải, có chỗ cát trắng loang muối. Kết hợp với các hồ lân cận như Khadyn và Chagytai, khu vực này tạo thành một 'cụm hồ' đặc trưng của trung tâm Tuva - lý tưởng để tắm khoáng, thư giãn và trải nghiệm thiên nhiên thảo nguyên.",
    [
        "Hồ nước mặn kiểu 'Biển Chết' - nước nâng người nổi, không biết bơi vẫn thả mình được.",
        "Bùn khoáng đáy hồ nổi tiếng với công dụng trị liệu da và khớp.",
        "Điểm nghỉ dưỡng - tắm khoáng được ưa chuộng, cách Kyzyl ~45 km về phía nam.",
    ],
    p("Mùa tắm chính là mùa hè; các cơ sở nghỉ ven hồ hoạt động theo mùa.",
      "Có thể thu phí vào bãi/nghỉ tuỳ cơ sở; nhìn chung rẻ.",
      "Nửa ngày đến trọn ngày.",
      "Tháng 6-8 khi trời ấm.",
      "Mang nước ngọt để tráng người sau khi tắm mặn; tránh để nước mặn dính mắt/vết thương hở."),
    [
        {"title": "Туристический портал Республики Тыва — Дус-Холь (Сватиково)", "url": "https://visittuva.ru/arzhaany/dus-hol-svatikovo/"},
        {"title": "Wikipedia (RU) — Дус-Холь (озеро, Тандинский кожуун)", "url": "https://ru.wikipedia.org/wiki/Дус-Холь_(озеро,_Тандинский_кожуун)"},
    ],
    ["park_garden", "lake", "salt-lake", "balneology", "tandinsky", "nature"],
    maps_text("Озеро Дус-Холь Сватиково", "Тыва", "Dus-Khol Svatikovo salt lake", "Tuva", 51.362500, 94.438900),
))

# 14) Озеро Хадын ---------------------------------------------------------------------
RECORDS.append(rec(
    "khadyn-salt-lake",
    "Hồ nước mặn Khadyn",
    "Озеро Хадын",
    "Khadyn salt lake",
    ["park_garden"],
    51.335280, 94.524170,
    "Bồn địa Tuva, huyện Tandinsky, phía nam Kyzyl, gần hồ Dus-Khol, Cộng hoà Tuva, Nga",
    "Hồ nước mặn khép kín rộng hơn 23 km² ở phía nam Kyzyl, nằm cạnh Dus-Khol trong cụm hồ trung tâm Tuva. Bờ cát điểm những vệt muối trắng, là nơi tắm khoáng và nghỉ ngơi mùa hè.",
    "Khadyn là một hồ nước mặn không có dòng chảy ra, nằm ở phần đông của bồn địa Tuva, phía nam Kyzyl và chỉ cách hồ Dus-Khol vài ki-lô-mét về phía đông. Hồ rộng khoảng 23,6 km², nằm trong một vùng trũng khép kín được bao quanh bởi thảo nguyên gò đồi không cây cối; bờ đông và bắc là những dải cát ('bichevnik') phủ vệt muối trắng lấp lánh. Cùng với Dus-Khol và Chagytai, Khadyn tạo thành cụm hồ đặc trưng của trung tâm Tuva - nơi người dân và du khách tìm đến để tắm nước khoáng mặn, phơi nắng và cắm trại trong những tháng hè ngắn ngủi mà ấm áp. Khung cảnh mở rộng, tĩnh lặng, mang vẻ đẹp khắc khổ đặc trưng của bồn địa bán hoang mạc. Với người yêu thiên nhiên, Khadyn là điểm dừng dễ chịu để cảm nhận sự hào phóng bất ngờ của nước giữa vùng đất khô cằn.",
    [
        "Hồ nước mặn khép kín rộng ~23,6 km², bờ cát điểm vệt muối trắng.",
        "Thuộc cụm hồ trung tâm Tuva cùng Dus-Khol và Chagytai, ngay phía nam Kyzyl.",
        "Điểm tắm khoáng, phơi nắng và cắm trại mùa hè giữa thảo nguyên bán hoang mạc.",
    ],
    p("Không gian tự nhiên mở, tắm và cắm trại chủ yếu vào mùa hè.",
      "Miễn phí ở khu vực tự do; một số điểm nghỉ có thể thu phí.",
      "Nửa ngày.",
      "Tháng 6-8.",
      "Mang theo nước ngọt, ô/lều che nắng và đồ cắm trại vì hạ tầng ven hồ tối giản."),
    [
        {"title": "Sib-guide.ru — Озеро Хадын", "url": "https://sib-guide.ru/siberia/di/272"},
        {"title": "Wikipedia (RU) — Хадын", "url": "https://ru.wikipedia.org/wiki/Хадын"},
    ],
    ["park_garden", "lake", "salt-lake", "tandinsky", "steppe", "nature"],
    maps_text("Озеро Хадын", "Тыва", "Khadyn salt lake", "Tuva", 51.335280, 94.524170),
))

# 15) Озеро Чагытай -------------------------------------------------------------------
RECORDS.append(rec(
    "chagytai-lake",
    "Hồ Chagytai",
    "Озеро Чагытай",
    "Chagytai Lake",
    ["park_garden"],
    51.000000, 94.716670,
    "Chân sườn bắc dãy Đông Tannu-Ola, huyện Tandinsky, cách Kyzyl khoảng 70 km về phía nam, Cộng hoà Tuva, Nga",
    "Hồ nước ngọt sâu và lớn nhất của bồn địa Tuva, nằm dưới chân dãy Tannu-Ola. Bãi cát - cuội, nước trong, rừng lân cận và cá phong phú khiến đây là điểm nghỉ hè và câu cá được yêu thích.",
    "Chagytai là hồ nước ngọt lớn nhất và sâu nhất của bồn địa Tuva, nằm ở phần trung tâm huyện Tandinsky, dưới chân sườn bắc dãy Đông Tannu-Ola, ở độ cao khoảng 1.005 m và cách Kyzyl chừng 70 km về phía nam. Hồ rộng khoảng 28,6 km², đáy cát - cuội, bờ phần lớn thoải, có nơi đá, có nơi cát, phía đông nam là bờ đầm lầy thấp; từ hồ chảy ra con suối nhỏ Mazhalyk thuộc lưu vực sông Tiểu Yenisei. Nước trong, cảnh quan hồ - rừng - núi hài hoà và nguồn cá phong phú (được bổ sung cả các loài nuôi thả) khiến Chagytai trở thành điểm nghỉ hè, tắm mát và câu cá quen thuộc của người Tuva; quanh hồ có khu bảo tồn sinh - thuỷ văn Chagytai. Khác với các hồ mặn lân cận, Chagytai mang lại trải nghiệm nước ngọt mát lành, thích hợp cắm trại và thư giãn giữa thiên nhiên. Đây là một trong những hồ đẹp và dễ chịu nhất để dừng chân ở trung tâm Tuva.",
    [
        "Hồ nước ngọt LỚN và SÂU nhất bồn địa Tuva (~28,6 km²), dưới chân dãy Tannu-Ola.",
        "Nước trong, bãi cát - cuội, rừng bao quanh; nguồn cá phong phú để câu.",
        "Điểm nghỉ hè, tắm mát và cắm trại được yêu thích, cách Kyzyl ~70 km.",
    ],
    p("Không gian tự nhiên, nghỉ ngơi và câu cá chủ yếu vào mùa hè.",
      "Miễn phí ở khu tự do; điểm nghỉ/căn cứ nghỉ dưỡng thu phí riêng.",
      "Nửa ngày đến trọn ngày (hoặc cắm trại qua đêm).",
      "Tháng 6-8.",
      "Đường rẽ vào hồ nằm gần làng Balgazyn trên quốc lộ; đề phòng bão bụi thảo nguyên khi thời tiết xấu."),
    [
        {"title": "Wikipedia (RU) — Чагытай", "url": "https://ru.wikipedia.org/wiki/Чагытай"},
        {"title": "Ozera.info — Озеро Чагытай (Республика Тыва)", "url": "https://ozera.info/russia/so/tyva/chagytai"},
    ],
    ["park_garden", "lake", "freshwater", "fishing", "tandinsky", "nature"],
    maps_text("Озеро Чагытай", "Тыва", "Chagytai Lake", "Tuva", 51.000000, 94.716670),
))

# 16) Озеро Сут-Холь ------------------------------------------------------------------
RECORDS.append(rec(
    "sut-khol-sacred-lake",
    "Hồ thiêng Sut-Khol ('Hồ Sữa')",
    "Озеро Сут-Холь",
    "Sut-Khol Lake",
    ["park_garden"],
    51.516670, 91.165280,
    "Cao nguyên Alash, tây nam dãy Tây Sayan, huyện Sut-Kholsky, Cộng hoà Tuva, Nga",
    "Hồ núi đẹp và được coi là linh thiêng, tên tiếng Tuva nghĩa là 'hồ sữa'. Nằm ở độ cao hơn 1.800 m giữa dãy Tây Sayan, nước trong và sâu, gắn với tín ngưỡng của người Tuva.",
    "Sut-Khol - 'hồ sữa' theo tiếng Tuva - là một hồ núi tuyệt đẹp ở phần nam dãy Tây Sayan, thuộc phần đông nam cao nguyên Alash, nằm ở độ cao khoảng 1.815 m so với mực nước biển. Hồ dài chừng 8 km, rộng khoảng 3,5 km, độ sâu vượt quá 50 m, mặt nước trong vắt phản chiếu núi rừng bao quanh. Với người Tuva, Sut-Khol là hồ thiêng: sữa được xem là biểu tượng của sự tinh khiết, và quanh hồ có nhiều truyền thuyết, tập tục kiêng kỵ nhằm giữ gìn sự trong lành của nước. Cảnh quan núi cao, rừng taiga và không khí tĩnh mịch khiến nơi đây vừa hùng vĩ vừa mang chiều sâu tâm linh. Đường đến khá xa và khó, nên hồ vẫn giữ được vẻ hoang sơ, ít bị tác động. Đối với du khách ưa trekking và thiên nhiên nguyên bản, Sut-Khol là một trong những viên ngọc ẩn của Tuva - nơi vẻ đẹp thiên nhiên hoà cùng niềm tin của cư dân bản địa.",
    [
        "Hồ núi thiêng của người Tuva, tên nghĩa là 'hồ sữa' - biểu tượng của sự tinh khiết.",
        "Ở độ cao ~1.815 m giữa dãy Tây Sayan, nước trong, sâu trên 50 m.",
        "Hoang sơ, gắn với nhiều truyền thuyết và tập tục kiêng kỵ giữ gìn nguồn nước.",
    ],
    p("Vùng núi hẻo lánh, tiếp cận theo mùa; nên đi cùng người dẫn địa phương.",
      "Miễn phí; chi phí chủ yếu là di chuyển.",
      "Chuyến đi thường trọn ngày hoặc nhiều ngày.",
      "Mùa hè khi đường núi khô ráo, dễ đi.",
      "Tôn trọng tín ngưỡng bản địa: không xả rác, không làm ô uế nguồn nước; chuẩn bị hậu cần cho vùng xa."),
    [
        {"title": "Sib-guide.ru — Озеро Сут-Холь (молочное озеро)", "url": "https://sib-guide.ru/siberia/di/281"},
        {"title": "ООПТ России — Озеро Сут-Холь", "url": "http://oopt.aari.ru/oopt/Озеро-Сут-Холь"},
    ],
    ["park_garden", "lake", "sacred", "mountain", "sut-kholsky", "nature"],
    maps_text("Озеро Сут-Холь", "Тыва", "Sut-Khol Lake", "Tuva", 51.516670, 91.165280),
))

# 17) Озеро Азас (Тоджа) --------------------------------------------------------------
RECORDS.append(rec(
    "azas-todzha-lake",
    "Hồ Azas (Todzha) và khu bảo tồn Azas",
    "Озеро Азас (Тоджа)",
    "Azas (Todzha) Lake",
    ["park_garden"],
    52.394170, 96.524440,
    "Bồn địa Todzha, huyện Todzhinsky, đông bắc Tuva, gần làng Toora-Khem, Cộng hoà Tuva, Nga",
    "Hồ lớn giữa vùng taiga đông bắc Tuva, một phần thuộc khu bảo tồn thiên nhiên liên bang Azas - nơi bảo vệ loài hải ly Tuva quý hiếm. Cảnh quan hồ - rừng - núi nguyên sơ, giàu đa dạng sinh học.",
    "Azas (còn gọi là Todzha) là một hồ lớn nằm trong bồn địa Todzha ở vùng đông bắc Tuva, gần làng Toora-Khem; sông Azas đổ vào và sông Toora-Khem chảy ra để rồi hoà vào Đại Yenisei. Hồ rộng khoảng 50 km², trải dài, có nhiều đảo (đảo lớn nhất là Khaara dài chừng 1,5 km) và bị đóng băng hơn nửa năm. Phần đông bắc hồ thuộc Khu bảo tồn thiên nhiên nhà nước liên bang 'Azas' (thành lập năm 1985), được lập ra để bảo vệ hệ sinh thái taiga Todzha, đặc biệt là quần thể hải ly Tuva - một phân loài quý hiếm. Xung quanh là rừng taiga, núi non và hệ động thực vật phong phú, tạo nên một vùng thiên nhiên hoang sơ tiêu biểu cho 'Tuva rừng' khác hẳn với thảo nguyên khô ở trung tâm. Đây là điểm đến cho những ai tìm kiếm cảnh quan nguyên bản, câu cá, ngắm chim thú và trải nghiệm vùng taiga sâu - dù việc tiếp cận đòi hỏi tổ chức kỹ và tuân thủ quy định bảo tồn.",
    [
        "Hồ taiga lớn (~50 km²) ở đông bắc Tuva, nhiều đảo, đóng băng hơn nửa năm.",
        "Một phần thuộc khu bảo tồn liên bang Azas, bảo vệ hải ly Tuva quý hiếm.",
        "Cảnh quan rừng - hồ - núi nguyên sơ, tiêu biểu cho vùng 'Tuva rừng' Todzha.",
    ],
    p("Vùng taiga hẻo lánh; khu lõi bảo tồn hạn chế ra vào, cần xin phép.",
      "Miễn phí ở khu vực cho phép; chi phí chủ yếu là hậu cần/di chuyển.",
      "Nhiều ngày (vì đường xa).",
      "Mùa hè và đầu thu.",
      "Liên hệ ban quản lý khu bảo tồn về quy định; đây là vùng sâu, cần tour và trang bị đầy đủ."),
    [
        {"title": "Sib-guide.ru — Озеро Азас (Тоджа)", "url": "https://sib-guide.ru/siberia/di/288"},
        {"title": "Wikipedia (RU) — Азас (заповедник)", "url": "https://ru.wikipedia.org/wiki/Азас_(заповедник)"},
    ],
    ["park_garden", "lake", "nature-reserve", "taiga", "todzhinsky", "wildlife"],
    maps_text("Озеро Азас", "Тыва", "Azas Lake", "Tuva", 52.394170, 96.524440),
))

# 18) Озеро Торе-Холь -----------------------------------------------------------------
RECORDS.append(rec(
    "tore-khol-lake-erzin",
    "Hồ Tore-Khol (biên giới Mông Cổ)",
    "Озеро Торе-Холь",
    "Tore-Khol Lake",
    ["park_garden"],
    50.033330, 95.066670,
    "Bồn địa Ubsunur, huyện Erzinsky, cách làng Erzin khoảng 20 km về phía tây nam, biên giới Nga - Mông Cổ, Cộng hoà Tuva, Nga",
    "Hồ nước ngọt nằm vắt qua biên giới Nga - Mông Cổ, nổi bật với những cồn cát cao ven bờ. Bãi cát, nước ấm và cảnh quan bán hoang mạc khiến đây là một trong những hồ nghỉ dưỡng được yêu thích ở nam Tuva.",
    "Tore-Khol (đôi khi gọi nhầm là Tere-Khol) là hồ nước ngọt khép kín nằm ở phía nam Tuva, trong bồn địa Ubsunur, vắt qua biên giới với Mông Cổ - phần thuộc Nga rộng khoảng 35 km², phần Mông Cổ khoảng 7 km². Tên hồ theo tiếng Tuva liên quan đến 'bàn đạp yên ngựa', phản ánh hình dáng của nó. Đặc trưng nổi bật là những cồn cát cao tới 12 m bao quanh bờ, giáp với bãi cát Tsugeer-Els ở phía đông bắc - tạo nên khung cảnh 'sa mạc gặp hồ nước' độc đáo giữa vùng bán hoang mạc. Nước hồ ấm về mùa hè, bãi cát thoai thoải nên rất thích hợp để tắm và nghỉ dưỡng; ven bờ đã có nhà hàng và khu cắm trại gồm các bungalow, lều yurt phục vụ du khách. Trong hồ có cá chó, cá pelyad và cá osman. Với vị trí gần biên giới và cảnh quan lạ mắt, Tore-Khol là điểm dừng chân hấp dẫn khi khám phá vùng Erzin - Ubsunur đầy nắng gió ở cực nam Tuva.",
    [
        "Hồ nước ngọt vắt qua biên giới Nga - Mông Cổ, cồn cát cao tới 12 m ven bờ.",
        "Giáp bãi cát Tsugeer-Els: cảnh 'sa mạc gặp hồ' độc đáo ở nam Tuva.",
        "Nước ấm, bãi cát thoai thoải; có nhà hàng, bungalow và lều yurt nghỉ dưỡng.",
    ],
    p("Điểm nghỉ mùa hè; cơ sở lưu trú ven hồ hoạt động theo mùa.",
      "Có thể thu phí vào bãi/lưu trú; cần lưu ý đây là khu vực biên giới.",
      "Nửa ngày đến vài ngày.",
      "Tháng 6-8 khi trời nắng ấm.",
      "Mang theo giấy tờ tuỳ thân vì gần biên giới; kết hợp tham quan bãi cát Tsugeer-Els và vùng Erzin."),
    [
        {"title": "Wikipedia (RU) — Торе-Холь", "url": "https://ru.wikipedia.org/wiki/Торе-Холь"},
        {"title": "ООПТ России — Озеро Торе-Холь", "url": "http://oopt.aari.ru/oopt/Озеро-Торе-Холь"},
    ],
    ["park_garden", "lake", "freshwater", "sand-dunes", "erzinsky", "border"],
    maps_text("Озеро Торе-Холь", "Тыва", "Tore-Khol Lake", "Tuva", 50.033330, 95.066670),
))

# 19) Озеро Хиндиктиг-Холь ------------------------------------------------------------
RECORDS.append(rec(
    "khindiktig-khol-alpine-lake",
    "Hồ băng hà Khindiktig-Khol",
    "Озеро Хиндиктиг-Холь",
    "Khindiktig-Khol Lake",
    ["park_garden"],
    50.354720, 89.828890,
    "Dưới chân massif Mongun-Taiga, huyện Mongun-Tayginsky, tây nam Tuva, giáp Cộng hoà Altai, Nga",
    "Hồ băng hà lớn ở độ cao 2.305 m dưới chân đỉnh Mongun-Taiga, nước trong đến mức nhìn thấu tới 20 m. Tên tiếng Tuva nghĩa là 'hồ có rốn' vì hai hòn đảo đá nổi giữa lòng hồ.",
    "Khindiktig-Khol - 'hồ có rốn' theo tiếng Tuva - là một hồ băng hà lớn nằm ở rìa tây nam Tuva, trên địa phận huyện Mongun-Tayginsky sát biên giới Cộng hoà Altai, dưới chân massif Mongun-Taiga về phía đông và các nhánh của dãy Shapshal về phía tây - bắc. Hồ rộng khoảng 66 km², ở độ cao 2.305 m, nước lạnh trong vắt với độ trong đạt tới 20 m; giữa hồ nổi lên hai đảo đá (đỉnh cao nhất tới 2.458 m) - chính chúng đã đặt tên cho hồ. Hồ có nguồn gốc băng - moren, được cấp nước chủ yếu từ băng tuyết, và từ đây chảy ra sông Mogen-Buren thuộc lưu vực bồn địa Đại Hồ (Great Lakes Basin) của Mông Cổ. Trên đảo có rái đá/macmot Altai và cỏ thuốc, trong hồ nhiều cá hồi trắng (khariut) cỡ lớn. Nằm trong khu vực cụm sinh quyển Ubsunur, Khindiktig-Khol là một trong những hồ cao nguyên hoang sơ và ngoạn mục nhất Tuva - điểm đến của những người ưa mạo hiểm, trekking và cảnh quan núi cao nguyên bản.",
    [
        "Hồ băng hà lớn (~66 km²) ở độ cao 2.305 m, nước trong nhìn thấu tới 20 m.",
        "Hai đảo đá giữa hồ - nguồn gốc cái tên 'hồ có rốn' theo tiếng Tuva.",
        "Dưới chân đỉnh Mongun-Taiga, trong khu vực sinh quyển Ubsunur hoang sơ.",
    ],
    p("Vùng núi cao hẻo lánh; chỉ tiếp cận được vào mùa ấm, cần tổ chức chuyến đi kỹ.",
      "Miễn phí; chi phí chủ yếu là hậu cần/hướng dẫn.",
      "Nhiều ngày (kết hợp trekking Mongun-Taiga).",
      "Cuối mùa hè khi tuyết tan và đường khả thi.",
      "Đòi hỏi thể lực, trang bị núi cao và người dẫn đường; thời tiết đổi nhanh, luôn gió mạnh và lạnh."),
    [
        {"title": "Wikipedia (RU) — Хиндиктиг-Холь", "url": "https://ru.wikipedia.org/wiki/Хиндиктиг-Холь"},
        {"title": "Заповедник «Убсунурская котловина»", "url": "http://ubsunur.ru/"},
    ],
    ["park_garden", "lake", "alpine", "glacial", "mongun-tayginsky", "nature"],
    maps_text("Озеро Хиндиктиг-Холь", "Тыва", "Khindiktig-Khol Lake", "Tuva", 50.354720, 89.828890),
))

# ============================ NÚI THIÊNG & SUỐI KHOÁNG (other) =========================

# 20) Гора Хайыракан ------------------------------------------------------------------
RECORDS.append(rec(
    "khairakan-sacred-mountain",
    "Núi thiêng Khairakan",
    "Гора Хайыракан",
    "Mount Khairakan",
    ["other"],
    51.569837, 93.000953,
    "Huyện Ulug-Khemsky, gần thị trấn Shagonar và làng Khairakan, Cộng hoà Tuva, Nga",
    "Ngọn núi được người Tuva tôn kính bậc nhất, gắn với tín ngưỡng Phật giáo và shaman giáo. Đức Đạt Lai Lạt Ma thứ 14 từng ban phước cho ngọn núi này, khiến nó trở thành nơi hành hương.",
    "Khairakan là một trong những ngọn núi thiêng được người Tuva tôn kính nhất, nằm ở huyện Ulug-Khemsky gần thị trấn Shagonar bên dòng Yenisei thượng nguồn. Cái tên 'Khairakan' mang sắc thái kính ngưỡng (một cách gọi tôn xưng dành cho gấu hoặc bậc đáng kính), phản ánh vị thế đặc biệt của núi trong tâm thức bản địa. Với người Tuva, đây là nơi cư ngụ của các linh hồn chủ đất (thần núi), gắn với cả tín ngưỡng shaman giáo lẫn Phật giáo; ngọn núi càng trở nên nổi tiếng sau khi Đức Đạt Lai Lạt Ma thứ 14 ghé thăm Tuva và ban phước, khiến Khairakan thành điểm hành hương và thiền định. Sườn núi và các điểm nhìn quanh đây mở ra khung cảnh thảo nguyên - sông núi rộng lớn, đặc biệt ấn tượng lúc bình minh và hoàng hôn. Đến Khairakan, du khách không chỉ ngắm cảnh mà còn cảm nhận mối liên hệ sâu sắc giữa người Tuva và thiên nhiên - nơi ngọn núi được xem như một thực thể linh thiêng cần được tôn trọng.",
    [
        "Một trong những ngọn núi thiêng được tôn kính nhất của người Tuva.",
        "Gắn với cả shaman giáo và Phật giáo; Đức Đạt Lai Lạt Ma thứ 14 từng ban phước.",
        "Điểm hành hương, thiền định với tầm nhìn thảo nguyên - sông núi rộng lớn.",
    ],
    p("Núi ngoài trời, tham quan tự do; nên tôn trọng các điểm thờ cúng (ovaa).",
      "Miễn phí.",
      "Khoảng 1-2 giờ tuỳ mức độ leo/ngắm cảnh.",
      "Mùa hè và đầu thu; bình minh và hoàng hôn đẹp nhất.",
      "Giữ gìn sự tôn nghiêm: không xả rác, đi vòng ovaa theo chiều kim đồng hồ; mang nước và giày phù hợp."),
    [
        {"title": "Tonkosti.ru — Гора Хайыракан", "url": "https://tonkosti.ru/Гора_Хайыракан"},
        {"title": "Туристический портал Республики Тыва — visittuva.ru", "url": "https://visittuva.ru/"},
    ],
    ["other", "mountain", "sacred", "buddhism", "shamanism", "ulug-khemsky"],
    maps_text("Гора Хайыракан", "Тыва", "Mount Khairakan", "Tuva", 51.569837, 93.000953),
))

# 21) Массив Монгун-Тайга -------------------------------------------------------------
RECORDS.append(rec(
    "mongun-taiga-massif",
    "Massif Mongun-Taiga - đỉnh cao nhất Đông Siberia",
    "Горный массив Монгун-Тайга",
    "Mongun-Taiga Massif",
    ["other"],
    50.279440, 90.120000,
    "Huyện Mongun-Tayginsky, cực tây nam Tuva, phần đông dãy Altai, Cộng hoà Tuva, Nga",
    "Massif núi cao 3.976 m - điểm cao nhất Tuva và cả Đông Siberia, đội trên đỉnh một vòm băng hà lấp lánh. Tên tiếng Tuva nghĩa là 'núi bạc'; là ngọn núi thiêng và đích đến của giới leo núi.",
    "Mongun-Taiga ('núi bạc' theo tiếng Tuva) là một massif núi hùng vĩ ở cực tây nam Tuva, thuộc phần đông của dãy Altai, với đỉnh cao 3.976 m - điểm cao nhất của Tuva và của toàn bộ Đông Siberia. Đỉnh núi được phủ một vòm băng hà, những ngày quang mây ánh lên sắc bạc lạnh đúng như tên gọi; quanh năm gió mạnh thổi qua vùng cao. Massif được cấu tạo từ đá phiến kết tinh và sa thạch, ở phần lõi có xâm nhập granite, trên cao là hệ thống sông băng rộng khoảng 44 km² cùng những dấu tích băng hà cổ. Sườn bắc là đồng cỏ núi và tundra, sườn nam là thảo nguyên cao và bãi đá; hoàn toàn không có đai rừng. Đây là ngọn núi thiêng - theo tín ngưỡng bản địa việc leo lên đỉnh từng bị kiêng kỵ - song từ năm 1946 nó đã thu hút các nhà leo núi với nhiều tuyến đường độ khó khác nhau. Dưới chân núi phía đông là hồ băng Khindiktig-Khol; khu vực nằm trong cụm bảo tồn của khu dự trữ sinh quyển Ubsunur, nơi sinh sống của cừu hoang Altai (argali) và báo tuyết (irbis). Với dân leo núi và người ưa mạo hiểm, chinh phục Mongun-Taiga là một trong những thử thách đáng nhớ nhất ở Nam Siberia.",
    [
        "Đỉnh cao 3.976 m - điểm cao NHẤT Tuva và toàn Đông Siberia, phủ vòm băng hà.",
        "Tên nghĩa là 'núi bạc'; ngọn núi thiêng, đích đến của giới leo núi từ 1946.",
        "Vùng sông băng ~44 km², nơi sống của cừu argali và báo tuyết (khu sinh quyển Ubsunur).",
    ],
    p("Vùng núi cao xa xôi; chỉ dành cho chuyến leo núi có tổ chức và chuẩn bị kỹ.",
      "Miễn phí tiếp cận; chi phí lớn ở hậu cần, hướng dẫn và trang bị.",
      "Nhiều ngày (leo núi/trekking).",
      "Cuối mùa hè (tháng 7-8) là cửa sổ thời tiết khả thi nhất.",
      "Cần kinh nghiệm leo núi tuyết, dẫn đường và giấy phép vùng biên; tôn trọng tính thiêng của núi với người bản địa."),
    [
        {"title": "Wikipedia (RU) — Монгун-Тайга", "url": "https://ru.wikipedia.org/wiki/Монгун-Тайга"},
        {"title": "Заповедник «Убсунурская котловина»", "url": "http://ubsunur.ru/"},
    ],
    ["other", "mountain", "peak", "glacier", "mongun-tayginsky", "mountaineering"],
    maps_text("Монгун-Тайга", "Тыва", "Mongun-Taiga Massif", "Tuva", 50.279440, 90.120000),
))

# 22) Курорт-аржаан Уш-Белдир ---------------------------------------------------------
RECORDS.append(rec(
    "ush-beldir-hot-springs",
    "Suối khoáng nóng Ush-Beldir",
    "Аржаан Уш-Белдир",
    "Ush-Beldir hot springs",
    ["other"],
    51.469720, 98.054720,
    "Thượng nguồn sông Kyzyl-Khem, đông bắc Tuva sát biên giới Mông Cổ, huyện Kyzylsky, Cộng hoà Tuva, Nga",
    "Suối khoáng nóng (arzhaan) và khu điều dưỡng hẻo lánh ở đông bắc Tuva, nổi tiếng nhờ nguồn nước phóng xạ - khoáng chữa bệnh. Một trong những 'arzhaan' chữa lành được người Tuva tôn quý nhất, nay thuộc công viên tự nhiên 'Tuva'.",
    "Ush-Beldir là một khu điều dưỡng suối khoáng nóng nằm sâu trong vùng núi taiga hiểm trở ở đông bắc Tuva, bên thượng nguồn sông Kyzyl-Khem, trong dải năm ki-lô-mét dọc biên giới với Mông Cổ. Từ xa xưa, dòng nước nóng tự nhiên (arzhaan) nơi đây đã là điểm chữa bệnh được người Tuva tìm đến; năm 1933 nó chính thức trở thành khu điều dưỡng khoáng - nước (balneological) với nguồn nước giàu khoáng và tính phóng xạ nhẹ (radon), được cho là tốt cho các bệnh về khớp, thần kinh và ngoài da. Năm 2016, khu vực Ush-Beldir (rộng 442,8 nghìn hecta) trở thành một cụm của công viên tự nhiên 'Tuva', trải dọc biên giới trong lưu vực các sông Bilin và Busin-Gol. Do quá xa xôi, nơi đây chủ yếu tiếp cận bằng đường hàng không, giữ được sự cô lập gần như nguyên vẹn cùng cảnh quan núi rừng nguyên sơ. Với người tìm kiếm sự chữa lành và trải nghiệm thiên nhiên tận cùng hoang dã, Ush-Beldir là một 'arzhaan' huyền thoại của Tuva.",
    [
        "Suối khoáng nóng phóng xạ (radon) chữa bệnh - 'arzhaan' được tôn quý của người Tuva.",
        "Khu điều dưỡng từ 1933, nay thuộc cụm bảo tồn của công viên tự nhiên 'Tuva'.",
        "Cực kỳ hẻo lánh sát biên giới Mông Cổ, chủ yếu tiếp cận bằng đường hàng không.",
    ],
    p("Khu điều dưỡng xa xôi; tổ chức chuyến đi và lưu trú cần liên hệ trước.",
      "Có phí điều dưỡng/lưu trú; chi phí di chuyển (bay) đáng kể.",
      "Nhiều ngày.",
      "Mùa hè.",
      "Cần giấy tờ vì gần biên giới; sắp xếp qua cơ sở điều dưỡng và phương tiện bay, chuẩn bị hậu cần cho vùng cách trở."),
    [
        {"title": "Wikipedia (RU) — Уш-Белдир", "url": "https://ru.wikipedia.org/wiki/Уш-Белдир"},
        {"title": "Тувинская правда — «Волшебный Уш-Белдир»", "url": "https://ru.wikipedia.org/wiki/Уш-Белдир"},
    ],
    ["other", "hot-spring", "arzhaan", "balneology", "kyzylsky", "nature"],
    maps_text("Аржаан Уш-Белдир", "Тыва", "Ush-Beldir hot springs", "Tuva", 51.469720, 98.054720),
))

# ============================ QUẢNG TRƯỜNG (square_street) ============================

# 23) Площадь Арата -------------------------------------------------------------------
RECORDS.append(rec(
    "arat-square-kyzyl",
    "Quảng trường Arat",
    "Площадь Арата",
    "Arat Square",
    ["square_street"],
    51.719896, 94.439133,
    "Trung tâm thành phố Kyzyl, giữa phố Lenina và Dom Pravitelstva, Cộng hoà Tuva, Nga",
    "Quảng trường trung tâm và lớn nhất của Kyzyl, nơi đặt Nhà Chính phủ, Nhà hát Nhạc kịch và đài phun nước. Không gian diễn ra các sự kiện, lễ hội lớn của nước cộng hoà và là điểm dạo chơi quen thuộc.",
    "Quảng trường Arat (площадь Арата - 'quảng trường của người chăn nuôi/dân du mục') là trái tim hành chính và công cộng của Kyzyl. Bao quanh quảng trường là những công trình quan trọng nhất của nước cộng hoà: Nhà Chính phủ (Dom Pravitelstva), Nhà hát Nhạc kịch Quốc gia mang tên Kok-ool cùng cụm công trình văn hoá; ở giữa là đài phun nước và không gian mở rộng rãi. Đây là nơi tổ chức các sự kiện trọng đại - mít tinh, lễ hội dân tộc, hoà nhạc ngoài trời, đón năm mới Shagaa - và cũng là chốn người dân thong dong dạo bộ, gặp gỡ mỗi ngày. Vào buổi tối, đài phun nước và ánh đèn khiến quảng trường trở nên sống động; mùa đông, nơi đây thường dựng các công trình băng - tuyết dịp lễ. Với du khách, Arat là điểm khởi đầu tiện lợi để cảm nhận nhịp sống đô thị Tuva và từ đây tản bộ tới bờ kè Yenisei, đài Trung tâm châu Á cùng các bảo tàng, chùa lân cận.",
    [
        "Quảng trường trung tâm lớn nhất Kyzyl, nơi đặt Nhà Chính phủ và Nhà hát Kok-ool.",
        "Sân khấu của các sự kiện, lễ hội dân tộc và đón Tết Shagaa của nước cộng hoà.",
        "Có đài phun nước, không gian dạo bộ; điểm khởi đầu khám phá trung tâm Kyzyl.",
    ],
    p("Không gian công cộng ngoài trời, tự do 24/7.",
      "Miễn phí.",
      "Khoảng 20-40 phút.",
      "Buổi tối mùa hè khi đài phun nước hoạt động; dịp lễ hội rất sôi động.",
      "Dễ kết hợp đi bộ tới bờ kè Yenisei và đài Trung tâm châu Á; mùa đông rất lạnh, mặc thật ấm."),
    [
        {"title": "Российская газета — что посмотреть в Кызыле", "url": "https://rg.ru/2024/10/02/chto-posmotret-za-odin-den-okazavshis-v-kyzyle.html"},
        {"title": "Vpoxod.ru — Кызыл: достопримечательности", "url": "https://www.vpoxod.ru/page/toponym/kyzyl_info"},
    ],
    ["square_street", "square", "kyzyl", "city-center", "culture", "siberia"],
    maps_text("Площадь Арата", "Кызыл", "Arat Square", "Kyzyl", 51.719896, 94.439133),
))


# ============================ GHI FILE (backup + dedup) ==============================

def main():
    path = os.path.join(REGIONS, f"{REGION}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, list), "Định dạng file vùng phải là list"

    existing_slugs = {r.get("slug") for r in data}
    existing_ids = {r.get("id") for r in data}

    # Backup .bak (kèm timestamp) trước khi ghi
    bak = f"{path}.{TS}.bak"
    shutil.copy2(path, bak)

    added, skipped = [], []
    for r in RECORDS:
        if r["slug"] in existing_slugs or r["id"] in existing_ids:
            skipped.append(r["slug"])
            continue
        # kiểm tra toạ độ trong phạm vi Tuva, chống đảo lat/lon
        lat, lon = r["coordinates"]["lat"], r["coordinates"]["lon"]
        assert 49.0 <= lat <= 54.0, f"lat ngoài phạm vi Tuva: {r['slug']} -> {lat}"
        assert 88.0 <= lon <= 99.5, f"lon ngoài phạm vi Tuva: {r['slug']} -> {lon}"
        data.append(r)
        existing_slugs.add(r["slug"])
        existing_ids.add(r["id"])
        added.append(r["slug"])

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Backup: {bak}")
    print(f"Đã thêm {len(added)} địa điểm; bỏ qua {len(skipped)} (trùng).")
    print(f"Tổng số địa điểm tuva sau khi ghi: {len(data)}")
    if added:
        print("Slug đã thêm:")
        for s in added:
            print("  +", s)
    if skipped:
        print("Bỏ qua (trùng):", skipped)


if __name__ == "__main__":
    main()
