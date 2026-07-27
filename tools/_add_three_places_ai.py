# -*- coding: utf-8 -*-
"""_add_three_places_ai.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-27).

Ưu tiên VÙNG (a): thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.
Cả 3 địa điểm lần này đều thuộc Tỉnh Moskva (moscow-oblast) — danh thắng nổi tiếng/hiện đại còn thiếu,
chọn cho đa dạng chủ đề (không gian – kỹ thuật hiện đại – tu viện cổ):

Thêm:
  1) Tỉnh Moskva (moscow-oblast): Trung tâm Đào tạo Phi hành gia Yu. A. Gagarin (Thành phố Sao / Zvyozdny Gorodok)
        (museum/other) — trung tâm huấn luyện vũ trụ nổi tiếng nhất nước Nga, nơi Gagarin và mọi thế hệ
        phi hành gia Xô Viết/Nga tập luyện; có Bảo tàng Du hành Vũ trụ, bể thuỷ lực, máy ly tâm khổng lồ.
  2) Tỉnh Moskva (moscow-oblast): Bảo tàng Kỹ thuật Vadim Zadorozhny (Arkhangelskoye, Krasnogorsk)
        (museum) — bảo tàng kỹ thuật tư nhân LỚN NHẤT nước Nga (một trong những bảo tàng lớn nhất châu Âu):
        hơn 1.000 hiện vật xe cổ, mô-tô, khí tài quân sự, máy bay; sát Điền trang Arkhangelskoye.
  3) Tỉnh Moskva (moscow-oblast): Tu viện Nikolo-Peshnoshsky (Lugovoy, huyện Dmitrov)
        (church/fortress/monument) — một trong những quần thể tu viện cổ và đẹp nhất Tỉnh Moskva, lập năm
        1361 bởi Thánh Mefodiy (môn đệ Thánh Sergiy Radonezhsky); hồi sinh sau nhiều thập niên bị đóng cửa.

ĐỐI CHIẾU TRÁNH TRÙNG (đã quét slug/name toàn bộ file vùng + toàn CSDL, non-bak):
  - moscow-oblast.json (31 bản ghi): CHƯA có Gagarin/Zvyozdny, Zadorozhny, hay Peshnoshsky.
  - Quét toàn CSDL: 'zadorozhny' -> 0, 'peshnosh' -> 0, 'zvyozdny/zvezdny/star city/подготовки космонавтов' -> 0.
    (moscow.json có 'cosmonautics-museum' = Bảo tàng Du hành Vũ trụ ở NỘI ĐÔ Moskva tại VDNKh — KHÁC hoàn
     toàn với Trung tâm huấn luyện ở Thành phố Sao; không trùng.)
  - Gatchina/Priory ĐÃ nằm ở saint-petersburg.json (cụm ngoại ô hoàng gia) -> KHÔNG đụng tới.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, không sao chép nguyên văn), có ghi nguồn.

TOẠ ĐỘ THẬT — đối chiếu chéo ≥2 nguồn (thập phân WGS84), 2026-07:
  - Центр подготовки космонавтов / Звёздный городок (г.о. Щёлково):  55.874968, 38.120628
        (ru.wikipedia + dữ liệu toạ độ Звёздный городок: N55°52.327′, E038°06.421′; đông bắc Moskva, cạnh Shchyolkovo)
  - Музей техники Вадима Задорожного (Ильинское ш., 4-й км, Архангельское, г.о. Красногорск): 55.796710, 37.298710
        (en.wikipedia Q4306477 55°47′48″N 37°17′56″E ~ 55.79667,37.29889; GPS 2GIS/культура.рф N55.79671 E37.29871)
  - Николо-Пешношский монастырь (пос. Луговой, Дмитровский р-н):    56.456894, 37.229650
        (2GIS/esosedi + Wikidata nhà thờ chính St. Nicholas 56°27′20.9″N 37°13′49.0″E; tây bắc Dmitrov, gần Rogachyovo)
Kiểm tra thứ tự lat/lon: lat 55-56 (∈41-70), lon 37-38 (∈19-180), KHÔNG đảo; đều nằm trong phạm vi Tỉnh Moskva.

LINK BẢN ĐỒ dạng TRỎ-ĐỊA-ĐIỂM:
  - Record 1 & 2: helper maps_text (text=tên+địa danh, ll=toạ độ đã kiểm chứng) — mở đúng thẻ địa điểm.
  - Record 3: dùng URL TRANG TỔ CHỨC Yandex (yandex.com/maps/org/nikolo_peshnoshsky_monastery/1381841909)
        vì tra được org-id chính xác (task ưu tiên org URL). coordinates{lat,lon} vẫn LƯU chuẩn cho GIS.

Chạy:  python3 tools/_add_three_places_ai.py
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-27"


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


# ============================================================ RECORD 1
GAGARIN_TRAINING_CENTER = {
    "id": "moscow-oblast-gagarin-cosmonaut-training-center",
    "slug": "gagarin-cosmonaut-training-center",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Trung tâm Đào tạo Phi hành gia Yu. A. Gagarin (Thành phố Sao – Zvyozdny Gorodok)",
    "name_ru": "Центр подготовки космонавтов имени Ю. А. Гагарина (Звёздный городок)",
    "name_en": "Yuri Gagarin Cosmonaut Training Center (Star City)",
    "categories": ["museum", "other"],
    "coordinates": {"lat": 55.874968, "lon": 38.120628},
    "address_vi": (
        "Posёlok Zvyozdny Gorodok (Thành phố Sao), thành phố (okrug) Shchyolkovo, Tỉnh Moskva; nằm ở phía "
        "đông bắc Moskva, cách trung tâm thủ đô khoảng 40-50 km, giữa rừng thông gần thành phố Shchyolkovo. "
        "Đây là một «thị trấn kín» (ZATO): vào tham quan Trung tâm và bảo tàng phải đăng ký trước theo tour "
        "và mang theo giấy tờ tuỳ thân."
    ),
    "rating": None,
    "presentation_short_vi": (
        "Đây là trung tâm huấn luyện vũ trụ nổi tiếng và quan trọng bậc nhất nước Nga - nơi Yuri Gagarin cùng "
        "mọi thế hệ phi hành gia Xô Viết và Nga (và nhiều phi hành gia quốc tế) đã rèn luyện trước khi bay vào "
        "không gian. Tọa lạc tại «Thành phố Sao» (Zvyozdny Gorodok) phía đông bắc Moskva, tổ hợp có Bảo tàng Du "
        "hành Vũ trụ mang tên Gagarin, bể thuỷ lực khổng lồ mô phỏng trạng thái không trọng lực, máy ly tâm và các "
        "mô hình trạm Mir, ISS kích thước thật. Tham quan theo tour đăng ký trước, mang lại trải nghiệm hiếm có "
        "về ngành du hành vũ trụ."
    ),
    "presentation_long_vi": (
        "Trung tâm Đào tạo Phi hành gia được thành lập ngày 11 tháng 1 năm 1960 và ngay trong năm đó chuyển về "
        "khu rừng thông phía đông bắc Moskva - nơi về sau hình thành «Thành phố Sao» (Zvyozdny Gorodok). Sau "
        "chuyến bay lịch sử của Yuri Gagarin năm 1961 và sự ra đi của ông năm 1968, Trung tâm được mang tên nhà "
        "du hành vũ trụ đầu tiên của nhân loại. Suốt hơn sáu thập niên, đây là «lò luyện» của toàn bộ phi hành "
        "gia Liên Xô rồi Liên bang Nga, cũng như nhiều phi hành gia nước ngoài trong các chương trình hợp tác "
        "quốc tế như Interkosmos và Trạm Vũ trụ Quốc tế (ISS). Tổ hợp huấn luyện quy tụ những thiết bị độc đáo: "
        "bể thuỷ lực (hydrolaboratory) đủ lớn để dìm cả mô-đun trạm vũ trụ nặng hàng chục tấn, giúp phi hành gia "
        "tập thao tác ngoài khoang trong môi trường mô phỏng không trọng lực; máy ly tâm cánh tay dài thuộc hàng "
        "lớn nhất thế giới để rèn sức chịu quá tải; các mô hình trạm Mir và ISS, tàu Soyuz kích thước thật cùng "
        "buồng tập kỹ năng và phòng mô phỏng. Trái tim tinh thần của nơi này là Bảo tàng Du hành Vũ trụ, ra đời "
        "năm 1967 theo chính đề xuất của Gagarin: tại đây lưu giữ phòng làm việc của ông được gìn giữ nguyên "
        "trạng, các kỷ vật cá nhân, bộ đồ du hành, khoang tàu và vô số hiện vật kể lại lịch sử chinh phục không "
        "gian của nước Nga. Vì Thành phố Sao là khu vực hành chính khép kín, du khách chỉ có thể vào theo tour có "
        "tổ chức, đăng ký trước và mang theo giấy tờ; với khách nước ngoài, thủ tục cần chuẩn bị sớm hơn. Dù vậy, "
        "được tận mắt bước vào nơi các phi hành gia luyện tập vẫn là một trong những trải nghiệm khoa học - công "
        "nghệ đáng nhớ nhất trong hành trình quanh Moskva. (Lưu ý: từ giữa năm 2025, một số tour tới Bảo tàng của "
        "Trung tâm tạm dừng do sửa chữa Nhà Phi hành gia - cần hỏi lại lịch trước khi đi.)"
    ),
    "highlights_vi": [
        "Tổ hợp huấn luyện độc đáo: bể thuỷ lực khổng lồ mô phỏng không trọng lực, máy ly tâm cánh tay dài hàng đầu thế giới, cùng mô hình trạm Mir, ISS và tàu Soyuz kích thước thật.",
        "Bảo tàng Du hành Vũ trụ (lập năm 1967 theo đề xuất của Gagarin) - lưu giữ phòng làm việc nguyên trạng, kỷ vật, bộ đồ du hành và khoang tàu của các phi hành gia.",
        "«Thành phố Sao» - thị trấn khép kín nơi Gagarin và mọi thế hệ phi hành gia Xô Viết/Nga sinh sống và luyện tập; tham quan theo tour đăng ký trước, mang lại trải nghiệm không gian hiếm có.",
    ],
    "practical": {
        "hours_vi": "Trung tâm làm việc các ngày trong tuần (khoảng 9:00-18:00). Tham quan bảo tàng và tổ hợp huấn luyện CHỈ theo tour đã đăng ký trước, không nhận khách vãng lai. Từ 16/6/2025, tour tới Bảo tàng của Trung tâm tạm dừng do sửa chữa Nhà Phi hành gia - nên hỏi lại lịch trước khi đến.",
        "ticket_vi": "Vé/tour có thu phí, thường đặt qua các đơn vị lữ hành được uỷ quyền; giá thay đổi theo chương trình (chỉ bảo tàng, hay có thêm bể thuỷ lực/máy ly tâm) và số lượng khách.",
        "duration_vi": "Khoảng 2-4 giờ tuỳ chương trình tour.",
        "best_time_vi": "Quanh năm (hoạt động trong nhà); nên chọn ngày thường và đặt trước vì cần thời gian làm thủ tục ra vào khu vực khép kín.",
        "tips_vi": "Bắt buộc đặt tour và cung cấp thông tin giấy tờ trước; khách nước ngoài nên đăng ký sớm hơn. Từ Moskva có thể đi tàu ngoại ô/xe buýt về hướng Shchyolkovo rồi theo hướng dẫn của đơn vị tổ chức. Luôn xác nhận lại tình trạng bảo tàng vì đang có hạng mục sửa chữa.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text(
        "Центр подготовки космонавтов имени Ю. А. Гагарина", "Звёздный городок, Московская область",
        "Gagarin Cosmonaut Training Center", "Star City, Moscow Oblast",
        55.874968, 38.120628,
    ),
    "official_site": "https://www.gctc.ru/",
    "sources": [
        {"title": "Wikipedia (RU) — Центр подготовки космонавтов имени Ю. А. Гагарина", "url": "https://ru.wikipedia.org/wiki/Центр_подготовки_космонавтов_имени_Ю._А._Гагарина"},
        {"title": "Trang chính thức — ЦПК им. Ю. А. Гагарина (gctc.ru)", "url": "https://www.gctc.ru/"},
        {"title": "Wikipedia (EN) — Yuri Gagarin Cosmonaut Training Center", "url": "https://en.wikipedia.org/wiki/Yuri_Gagarin_Cosmonaut_Training_Center"},
    ],
    "tags": ["space", "cosmonaut", "gagarin", "museum", "science", "excursion", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}

# ============================================================ RECORD 2
ZADOROZHNY_TECH_MUSEUM = {
    "id": "moscow-oblast-zadorozhny-technical-museum",
    "slug": "zadorozhny-technical-museum",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Bảo tàng Kỹ thuật Vadim Zadorozhny",
    "name_ru": "Музей техники Вадима Задорожного",
    "name_en": "Vadim Zadorozhny Museum of Technology",
    "categories": ["museum"],
    "coordinates": {"lat": 55.796710, "lon": 37.298710},
    "address_vi": (
        "Ильинское шоссе, 4-й километр, стр. 8, посёлок Архангельское, thành phố (okrug) Krasnogorsk, Tỉnh "
        "Moskva; cách Vành đai Moskva (MKAD) khoảng 5-6 km về phía tây, ngay cạnh Điền trang Arkhangelskoye "
        "và không xa cao tốc Novorizhskoye/Ilyinskoye."
    ),
    "rating": None,
    "presentation_short_vi": (
        "Đây là bảo tàng kỹ thuật tư nhân lớn nhất nước Nga và thuộc hàng lớn nhất châu Âu, với hơn một nghìn "
        "hiện vật: xe hơi cổ, mô-tô, khí tài quân sự, máy bay và vũ khí. Do nhà sưu tầm Vadim Zadorozhny gây "
        "dựng từ năm 2001, bảo tàng nổi bật với những chiếc limousine nhà nước ZIS/ZIL, xe đua và xe sang tiền "
        "chiến, cùng khu trưng bày ngoài trời đầy xe tăng, pháo và máy bay. Nằm sát Điền trang Arkhangelskoye, "
        "đây là điểm đến rất được các gia đình và người mê kỹ thuật yêu thích."
    ),
    "presentation_long_vi": (
        "Bảo tàng Kỹ thuật Vadim Zadorozhny khởi nguồn từ đam mê sưu tầm ô tô cổ của ông Vadim Zadorozhny - một "
        "cựu giáo viên lịch sử - bắt đầu từ năm 1999. Năm 2001, bộ sưu tập được định hình thành bảo tàng; đến "
        "năm 2004 chuyển về khu đất rộng cạnh Cung điện - Điền trang Arkhangelskoye, và toà nhà trưng bày chính "
        "sáu tầng khánh thành năm 2007. Từ đó, nơi đây phát triển thành bảo tàng kỹ thuật tư nhân lớn nhất nước "
        "Nga và là một trong những bảo tàng loại này lớn nhất châu Âu, với hơn một nghìn hiện vật. Trong các gian "
        "trưng bày trong nhà, khách có thể chiêm ngưỡng những chiếc ô tô cổ được phục chế tinh xảo: từ xe sang và "
        "xe đua tiền chiến của châu Âu, cho tới dàn limousine nghi lễ của lãnh đạo Liên Xô mang nhãn ZIS và ZIL - "
        "biểu tượng một thời của điện Kremlin. Bên cạnh ô tô còn có bộ sưu tập mô-tô, xe đạp, động cơ và cả vũ "
        "khí, quân phục. Khu vực ngoài trời trải rộng trưng bày khí tài quân sự đồ sộ: xe tăng, xe bọc thép, "
        "pháo, tên lửa phòng không và nhiều loại máy bay, trực thăng - trong đó có những phi cơ được đưa về từ "
        "sân bay Khodynka ở Moskva rồi phục dựng công phu. Bảo tàng còn có xưởng phục chế riêng, nơi hồi sinh "
        "những cỗ máy tưởng như đã thành phế liệu, và thường tổ chức các sự kiện, triển lãm xe cổ. Với không gian "
        "vừa trong nhà vừa ngoài trời, cách bài trí sinh động và vị trí liền kề Điền trang Arkhangelskoye, đây là "
        "điểm dừng chân lý tưởng cho một ngày dã ngoại kết hợp lịch sử - kỹ thuật gần Moskva, đặc biệt hợp với "
        "các gia đình có trẻ nhỏ và người yêu xe cộ."
    ),
    "highlights_vi": [
        "Bảo tàng kỹ thuật tư nhân lớn nhất nước Nga (thuộc hàng lớn nhất châu Âu) với hơn 1.000 hiện vật; toà trưng bày chính sáu tầng khánh thành năm 2007.",
        "Bộ sưu tập ô tô cổ phục chế tinh xảo, nổi bật là dàn limousine nghi lễ ZIS/ZIL của lãnh đạo Liên Xô, cùng xe sang và xe đua tiền chiến.",
        "Khu trưng bày ngoài trời đồ sộ về khí tài quân sự - xe tăng, pháo, tên lửa và máy bay; nằm ngay cạnh Điền trang Arkhangelskoye nên dễ kết hợp tham quan.",
    ],
    "practical": {
        "hours_vi": "Thường mở cửa hằng ngày: Thứ Hai-Thứ Sáu khoảng 10:00-20:00, Thứ Bảy-Chủ nhật 10:00-21:00 (quầy vé đóng sớm hơn giờ đóng cửa). Nên kiểm tra lịch trên trang chính thức trước khi đến.",
        "ticket_vi": "Có bán vé vào cửa, kèm nhiều mức ưu đãi cho trẻ em, học sinh, sinh viên và người cao tuổi; một số chương trình/hoạt động trải nghiệm có thể tính phí riêng.",
        "duration_vi": "Khoảng 2-3 giờ cho cả khu trong nhà và khu trưng bày ngoài trời.",
        "best_time_vi": "Quanh năm nhờ có khu trong nhà; khu ngoài trời đẹp và dễ tham quan nhất vào cuối xuân đến đầu thu.",
        "tips_vi": "Từ Moskva có thể đi tàu điện ngầm tới ga Tushinskaya rồi bắt xe buýt/marshrutka theo hướng Ilyinskoye/Arkhangelskoye, hoặc đi ô tô theo cao tốc Novorizhskoye/Ilyinskoye. Rất tiện kết hợp cùng chuyến thăm Điền trang Arkhangelskoye ở ngay gần.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text(
        "Музей техники Вадима Задорожного", "Архангельское, Московская область",
        "Vadim Zadorozhny Museum of Technology", "Krasnogorsk, Moscow Oblast",
        55.796710, 37.298710,
    ),
    "official_site": "https://tmuseum.ru/",
    "sources": [
        {"title": "Wikipedia (EN) — Technical Museum of Vadim Zadorozhny", "url": "https://en.wikipedia.org/wiki/Technical_Museum_of_Vadim_Zadorozhny"},
        {"title": "Культура.РФ — Музей техники Вадима Задорожного", "url": "https://www.culture.ru/institutes/12095/muzei-tekhniki-vadima-zadorozhnogo"},
        {"title": "Trang chính thức — Музей техники Вадима Задорожного (tmuseum.ru)", "url": "https://tmuseum.ru/"},
    ],
    "tags": ["museum", "technology", "retro-cars", "military", "aviation", "family", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}

# ============================================================ RECORD 3
NIKOLO_PESHNOSHSKY_MONASTERY = {
    "id": "moscow-oblast-nikolo-peshnoshsky-monastery",
    "slug": "nikolo-peshnoshsky-monastery",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Tu viện Nikolo-Peshnoshsky (Nikolo-Peshnoshsky monastyr)",
    "name_ru": "Николо-Пешношский монастырь",
    "name_en": "Nikolo-Peshnoshsky Monastery",
    "categories": ["church", "fortress", "monument"],
    "coordinates": {"lat": 56.456894, "lon": 37.229650},
    "address_vi": (
        "Posёlok Lugovoy (Lugovoy), huyện Dmitrov, Tỉnh Moskva; nằm ở phía tây bắc thành phố Dmitrov, gần thị "
        "trấn Rogachyovo, bên dòng sông Yakhroma nơi hợp lưu với suối Peshnosha, cách Moskva khoảng 80-90 km."
    ),
    "rating": None,
    "presentation_short_vi": (
        "Nikolo-Peshnoshsky là một trong những tu viện cổ và đẹp bậc nhất Tỉnh Moskva, được lập từ năm 1361 bởi "
        "Thánh Mefodiy - môn đệ của Thánh Sergiy Radonezhsky. Quần thể quy tụ Nhà thờ chính Thánh Nikolai từ thế "
        "kỷ 16, tháp chuông, các nhà thờ nhỏ, nhà ăn cùng tường thành và tháp canh kiểu pháo đài. Sau nhiều thập "
        "niên bị đóng cửa thời Xô Viết và dùng làm cơ sở y tế, tu viện đã được trùng tu và hồi sinh, nay là điểm "
        "hành hương - tham quan yên bình giữa vùng quê phía bắc Moskva."
    ),
    "presentation_long_vi": (
        "Tu viện Nikolo-Peshnoshsky được sáng lập năm 1361 bởi tu sĩ Mefodiy (Methodius) - một trong những môn đệ "
        "của Thánh Sergiy Radonezhsky, vị thánh được tôn kính nhất của Chính Thống giáo Nga. Tương truyền chính "
        "Thánh Sergiy đã khuyên Mefodiy chọn nơi ẩn tu heo hút này; vị tu sĩ tự tay khiêng gỗ bắc cầu qua con "
        "suối nhỏ, và cái tên «Peshnosha» (nghĩa gần như «đi bộ vác nặng») ra đời từ đó. Qua các thế kỷ 15-16, tu "
        "viện trở thành một trung tâm tôn giáo và kinh tế thịnh vượng ở phía bắc Moskva, được nhiều đời đại công "
        "và Sa hoàng ban tặng đất đai, và tích luỹ một quần thể kiến trúc phong phú. Trung tâm quần thể là Nhà "
        "thờ chính Thánh Nikolai (Nikolsky sobor) có từ đầu thế kỷ 16 - một trong những công trình cổ nhất còn "
        "lại; bên cạnh là tháp chuông cao với nhà nguyện Thánh Mefodiy, Nhà thờ Thánh Sergiy Radonezhsky, khu nhà "
        "ăn, cùng vòng tường thành và những tháp canh mang dáng dấp pháo đài của thế kỷ 16-17. Nhờ vẻ hài hoà và "
        "bề dày lịch sử, Nikolo-Peshnoshsky từ lâu được giới nghiên cứu ngợi ca như một trong những quần thể tu "
        "viện đẹp và nguyên vẹn nhất vùng Moskva. Năm 1928, tu viện bị chính quyền Xô Viết đóng cửa; suốt nhiều "
        "thập niên sau đó, phần lớn công trình được trưng dụng làm một cơ sở điều trị tâm thần, khiến nơi này gần "
        "như khép kín với bên ngoài và dần xuống cấp. Đời sống đan tu chỉ được khôi phục từ năm 2007 và tái lập "
        "đầy đủ vào năm 2014, đi cùng một đợt trùng tu quy mô lớn trả lại vẻ đẹp cho quần thể. Ngày nay, "
        "Nikolo-Peshnoshsky là một tu viện nam đang hoạt động và là di tích kiến trúc được xếp hạng, thu hút "
        "khách hành hương lẫn du khách muốn tìm một điểm đến tĩnh lặng, giàu lịch sử, có thể kết hợp trong hành "
        "trình khám phá vùng Dmitrov ở phía bắc Tỉnh Moskva."
    ),
    "highlights_vi": [
        "Quần thể tu viện cổ lập năm 1361 bởi Thánh Mefodiy - môn đệ của Thánh Sergiy Radonezhsky; một trong những tu viện lâu đời và đẹp nhất Tỉnh Moskva.",
        "Nhà thờ chính Thánh Nikolai đầu thế kỷ 16 cùng tháp chuông, các nhà thờ nhỏ, nhà ăn và vòng tường thành - tháp canh kiểu pháo đài thế kỷ 16-17.",
        "Câu chuyện hồi sinh: bị đóng cửa năm 1928 và dùng làm cơ sở y tế suốt nhiều thập niên, tu viện được trùng tu và khôi phục đời sống đan tu từ 2007-2014.",
    ],
    "practical": {
        "hours_vi": "Là tu viện đang hoạt động, thường mở cửa hằng ngày cho khách hành hương vào ban ngày, quanh các giờ lễ. Nên tránh làm ồn và hỏi trước nếu muốn chụp ảnh bên trong nhà thờ.",
        "ticket_vi": "Vào cửa tự do (khuyến khích công đức tuỳ tâm); một số chương trình tham quan có hướng dẫn có thể liên hệ trước với tu viện.",
        "duration_vi": "Khoảng 1-1,5 giờ để dạo quanh quần thể nhà thờ, tháp chuông và tường thành.",
        "best_time_vi": "Cuối xuân đến đầu thu khi thời tiết dễ chịu; các dịp lễ Chính Thống giáo không khí đặc biệt trang nghiêm, đông khách hành hương.",
        "tips_vi": "Trang phục kín đáo; nữ nên mang khăn trùm đầu và váy/quần dài. Từ Moskva thuận tiện nhất là đi ô tô theo hướng Dmitrov rồi tới Rogachyovo/Luovoy; hoặc đi tàu tới Dmitrov rồi bắt xe buýt địa phương. Có thể kết hợp thăm thành Dmitrov Kremlin trên cùng cung đường.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": {
        # Task ƯU TIÊN URL trang tổ chức Yandex khi tra được org-id (chính xác nhất về vị trí thẻ địa điểm).
        "yandex": "https://yandex.com/maps/org/nikolo_peshnoshsky_monastery/1381841909/",
        "google": _google("Nikolo-Peshnoshsky Monastery", "Dmitrovsky District, Moscow Oblast"),
    },
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Николо-Пешношский монастырь", "url": "https://ru.wikipedia.org/wiki/Николо-Пешношский_монастырь"},
        {"title": "Соборы.ру — Луговой, Николо-Пешношский монастырь", "url": "https://sobory.ru/article/?object=00506"},
        {"title": "Монастырский вестник — Николо-Пешношский мужской монастырь", "url": "https://monasterium.ru/monastyri/monastery/nikolo-peshnoshskiy-muzhskoy-monastyr/"},
    ],
    "tags": ["monastery", "church", "orthodox", "fortress", "history", "medieval", "dmitrov", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


# ------------------------------------------------------------------ PLAN
PLAN = {
    "moscow-oblast.json": [GAGARIN_TRAINING_CENTER, ZADOROZHNY_TECH_MUSEUM, NIKOLO_PESHNOSHSKY_MONASTERY],
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
