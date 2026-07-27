# -*- coding: utf-8 -*-
"""_add_three_places_ad.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26, đêm).

Ưu tiên VÙNG: thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.

Thêm:
  1) Tỉnh Moskva (moscow-oblast)      : Bảo tàng «Pastila Kolomna» (Kolomna) — museum (hiện đại/tương tác)
  2) Tỉnh Moskva (moscow-oblast)      : Đài tưởng niệm «Anh hùng Panfilov» ở Dubosekovo — monument (WWII)
  3) Tỉnh Leningrad (leningrad-oblast): Bảo tàng Panorama «Proryv» ở Kirovsk — museum/monument (hiện đại, 2018)

LƯU Ý (đối chiếu tránh trùng, đã kiểm tra data/regions/*.json toàn bộ):
  - Kolomna trước nay chỉ có Kremlin Kolomna -> Bảo tàng «Pastila Kolomna» (Posadskaya 13a) là bảo tàng
    ẩm thực tương tác nổi tiếng, KHÁC loại hình và khác vị trí (khu Posad) -> bổ sung hợp lý.
  - Volokolamsk đã có Tu viện Iosifo-Volotsky; Dubosekovo là tượng đài WWII hoành tráng, loại hình khác,
    vị trí khác (gần ga Dubosekovo) -> bổ sung, cân bằng thêm 'monument'.
  - Leningrad: đã có Vyborg/Oreshek/Ivangorod/Tikhvin...; «Proryv» (Kirovsk) là bảo tàng-panorama HIỆN ĐẠI
    (2018) về Chiến dịch Iskra, chưa có trong CSDL -> bổ sung. (Gatchina/Priory Palace ĐÃ có trong
    saint-petersburg.json nên KHÔNG thêm.)

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, không sao chép nguyên văn), có ghi nguồn.
Toạ độ THẬT, đối chiếu web 2026-07 (nguồn đáng tin, dạng thập phân WGS84):
  - Kolomna Pastila : 55.10456, 38.76990  (2ГИС: center=38.7699,55.104558; Посадская ул., 13а)
  - Dubosekovo      : 55.97899, 36.04219  (Wikipedia RU: 55°58′44.35″N 36°02′31.90″E; gần ga Dubosekovo)
  - Proryv panorama : 59.90855, 30.99431  (memgid.ru/object/1377: 59.908545, 30.994313; chân cầu Ladoga)
Kiểm tra thứ tự lat/lon: lat 55–60 (∈41–70), lon 30–38 (∈19–180), KHÔNG đảo; đều nằm trong phạm vi vùng.

LINK BẢN ĐỒ dạng TRỎ-ĐỊA-ĐIỂM:
  - Kolomna Pastila & Dubosekovo: ưu tiên URL trang tổ chức Yandex (yandex.com/maps/org/.../<id>/) — chính xác nhất.
  - Proryv: dùng helper text+ll (khớp convention tools/retrofit_map_links.py) vì chưa tra được URL org sạch.
Toạ độ coordinates{lat,lon} vẫn LƯU chuẩn cho bản đồ nội bộ/GIS.

Chạy:  python3 tools/_add_three_places_ad.py
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
KOLOMNA_PASTILA = {
    "id": "moscow-oblast-kolomna-pastila-museum",
    "slug": "kolomna-pastila-museum",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Bảo tàng «Pastila Kolomna» (Muzey «Kolomenskaya pastila»)",
    "name_ru": "Музей «Коломенская пастила»",
    "name_en": "Kolomna Pastila Museum (Museum of the History of Pastila)",
    "categories": ["museum"],
    "coordinates": {"lat": 55.10456, "lon": 38.76990},
    "address_vi": "Phố Posadskaya số 13a, khu phố cổ Posad («Staraya Kolomna»), thành phố Kolomna, Tỉnh Moskva; ngay cạnh Kremlin Kolomna, gần nhà thờ Thánh Nikola trên Posad.",
    "rating": None,
    "presentation_short_vi": (
        "Bảo tàng «Pastila Kolomna» là bảo tàng đầu tiên ở Nga dành riêng cho pastila - món kẹo mứt táo "
        "truyền thống từng làm nên danh tiếng của thành phố Kolomna. Mở cửa năm 2009 trong một ngôi nhà cổ "
        "ở khu Posad ngay cạnh Kremlin Kolomna, nơi đây không chỉ trưng bày mà còn dựng cả một 'sân khấu "
        "vị giác': khách được hướng dẫn viên trong trang phục thế kỉ 19 mời trà, kể chuyện và nếm thử "
        "pastila làm theo công thức cổ đã được phục dựng."
    ),
    "presentation_long_vi": (
        "Pastila (пастила) là loại kẹo mứt xốp làm từ táo nghiền đánh bông rồi sấy khô - một đặc sản lâu "
        "đời của Kolomna, từng nổi tiếng khắp nước Nga thời đế chế. Đến đầu thế kỉ 20, nghề làm pastila "
        "thủ công gần như thất truyền. Năm 2009, trong khuôn khổ dự án hồi sinh khu phố cổ Posad, một nhóm "
        "người tâm huyết địa phương đã lập nên bảo tàng với tên gọi đầy đủ «Pastila Kolomna - Bảo tàng "
        "lịch sử có vị ngọt», dựa trên việc tìm lại và tái hiện các công thức pastila cổ trong văn khố và "
        "sách dạy nấu ăn xưa. Bảo tàng đặt trong một gian nhà thuộc điền trang thương gia cũ ở phố "
        "Posadskaya, cạnh nhà thờ Thánh Nikola trên Posad, và nhanh chóng thành một trong những bảo tàng "
        "tư nhân được yêu thích nhất vùng ngoại ô Moskva. Điểm đặc biệt là hình thức 'bảo tàng - sân khấu' "
        "mang tính tương tác: thay vì lặng lẽ ngắm tủ kính, khách tham quan theo suất, được các 'chủ nhà' "
        "và 'người hầu' hóa trang thời Sa hoàng dẫn qua từng căn phòng, nghe kể về thói quen uống trà và "
        "các loại pastila (táo trắng, pastila hạt phỉ, mận, thanh lương trà…), rồi cùng nếm thử bên tách "
        "trà nóng. Thành công của bảo tàng đầu tiên đã dẫn tới việc mở thêm 'Nhà máy - Bảo tàng Pastila' "
        "(2011) trong xưởng cũ của thương gia Chuprikov ở phố Polyanskaya - nơi khách xem tái hiện quy "
        "trình sản xuất thủ công - cùng bảo tàng bánh kalach (Kalachnaya) gần đó, tạo thành một cụm "
        "'thành phố - bảo tàng' sống động ở Posad Kolomna. Đây là ví dụ tiêu biểu cho làn sóng bảo tàng "
        "tương tác 'hiện đại' của Nga: biến di sản ẩm thực thành trải nghiệm du lịch hấp dẫn, đặc biệt hợp "
        "với gia đình và các chuyến đi trong ngày từ Moskva."
    ),
    "highlights_vi": [
        "Trải nghiệm 'bảo tàng - sân khấu': hướng dẫn viên hóa trang thời Sa hoàng dẫn khách qua các phòng, kể chuyện và mời nếm pastila bên tách trà.",
        "Nếm thử nhiều loại pastila làm theo công thức cổ đã phục dựng (táo trắng, pastila hạt phỉ, mận, thanh lương trà…) - hương vị khó tìm ở nơi khác.",
        "Vị trí ngay khu phố cổ Posad cạnh Kremlin Kolomna, kết nối cụm 'Nhà máy - Bảo tàng Pastila' và bảo tàng bánh kalach Kalachnaya.",
    ],
    "practical": {
        "hours_vi": "Thường mở cửa hằng ngày khoảng 10:00–20:00; tham quan tổ chức theo suất/nhóm có hướng dẫn nên tốt nhất là đặt trước, nhất là cuối tuần và ngày lễ.",
        "ticket_vi": "Vé có thu phí (thường đã gồm phần thuyết minh và nếm thử pastila cùng trà). Nên đặt suất trước qua trang chính thức; giá thay đổi theo chương trình - hãy kiểm tra trước khi đến.",
        "duration_vi": "Khoảng 1–1,5 giờ cho một suất tham quan có hướng dẫn.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà); dễ ghép cùng Kremlin Kolomna và khu phố cổ Posad trong một ngày.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô hoặc tàu tốc hành từ ga Kazansky đến Kolomna (khoảng 2 giờ) rồi bắt xe buýt/taxi vào khu Kremlin. Nên đặt suất trước; kết hợp thăm 'Nhà máy - Bảo tàng Pastila' (phố Polyanskaya) và bảo tàng bánh kalach gần đó để trọn trải nghiệm ẩm thực Kolomna.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_org("https://yandex.com/maps/org/muzey_kolomenskoy_pastily/1139584152/", "Kolomna Pastila Museum", "Moscow Oblast"),
    "official_site": "https://kolomnapastila.ru/",
    "sources": [
        {"title": "Trang chính thức — Музей «Коломенская пастила» (kolomnapastila.ru)", "url": "https://kolomnapastila.ru/"},
        {"title": "2ГИС — Коломенская пастила, музей истории со вкусом (Посадская, 13а)", "url": "https://2gis.ru/kolomna/firm/70000001023964852"},
        {"title": "Tourister.ru — Музей «Коломенская пастила»", "url": "https://www.tourister.ru/world/europe/russia/city/kolomna/museum/22968"},
    ],
    "tags": ["museum", "pastila", "gastronomy", "interactive-museum", "kolomna", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


DUBOSEKOVO = {
    "id": "moscow-oblast-dubosekovo-panfilov-memorial",
    "slug": "dubosekovo-panfilov-memorial",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Đài tưởng niệm «Anh hùng Panfilov» ở Dubosekovo («Podvigu 28»)",
    "name_ru": "Мемориал «Героям-панфиловцам» (Дубосеково)",
    "name_en": "Memorial to the Panfilov Heroes (Dubosekovo)",
    "categories": ["monument"],
    "coordinates": {"lat": 55.97899, "lon": 36.04219},
    "address_vi": "Gần ga xép Dubosekovo (cách làng Nelidovo khoảng 1,5 km), khu đô thị Volokolamsk, Tỉnh Moskva; cách thành phố Volokolamsk khoảng 7 km về phía đông nam.",
    "rating": None,
    "presentation_short_vi": (
        "Đài tưởng niệm «Anh hùng Panfilov» ở Dubosekovo là một trong những tượng đài chiến tranh lớn và "
        "giàu sức biểu cảm nhất Tỉnh Moskva. Khánh thành năm 1975, cụm tượng gồm sáu chiến sĩ tạc từ đá "
        "granit cao khoảng 10 mét, đứng quay lưng về Moskva và hướng mặt về phía tây - nơi quân Đức từng "
        "tiến đến. Công trình tưởng nhớ '28 chiến sĩ Panfilov' đã chặn xe tăng địch trong Trận chiến bảo "
        "vệ Moskva mùa đông 1941."
    ),
    "presentation_long_vi": (
        "Mùa thu - đông năm 1941, khi quân Đức mở chiến dịch 'Bão táp' (Taifun) nhằm chiếm Moskva, tuyến "
        "Volokolamsk trở thành một trong những hướng phòng thủ ác liệt nhất. Theo tường thuật kinh điển "
        "của báo chí Xô-viết, ngày 16 tháng 11 năm 1941 một nhóm chiến sĩ diệt tăng thuộc đại đội 4, trung "
        "đoàn bộ binh 1075, Sư đoàn bộ binh 316 do tướng Ivan Panfilov chỉ huy đã tử thủ tại ga xép "
        "Dubosekovo, chặn đứng nhiều đợt tấn công của xe tăng Đức chỉ với súng trường chống tăng, lựu đạn "
        "và chai cháy. Câu nói được gán cho chính trị viên Vasily Klochkov - «Nước Nga bao la, nhưng không "
        "còn đường lui - sau lưng là Moskva!» - đã trở thành biểu tượng cho tinh thần quyết tử bảo vệ thủ "
        "đô, và cả nhóm về sau được truy tặng danh hiệu Anh hùng Liên Xô. Cần nói thêm cho khách quan: từ "
        "thập niên 1990, giới sử học đã tranh luận nhiều về các chi tiết của câu chuyện (con số '28', diễn "
        "biến trận đánh và câu nói nổi tiếng), cho rằng bản tường thuật báo chí đã được lí tưởng hóa; dù "
        "vậy, đài tưởng niệm được dựng lên để tôn vinh sự hi sinh và lòng quả cảm chung của những người "
        "lính Hồng quân trên tuyến phòng thủ Moskva. Tượng đài «Podvigu 28» ('Chiến công của 28 người') "
        "được khánh thành ngày 6 tháng 5 năm 1975 nhân 30 năm Chiến thắng: sáu pho tượng đá granit khổng "
        "lồ, tượng trưng cho sáu dân tộc trong sư đoàn đa sắc tộc của Panfilov, dựng trên gò đất giữa cánh "
        "đồng trống nên tạo hiệu ứng thị giác rất mạnh. Gần đó, ở làng Nelidovo có ngôi mộ tập thể và một "
        "bảo tàng nhỏ về sự kiện. Ngày nay Dubosekovo là điểm đến tưởng niệm quan trọng, đặc biệt đông vào "
        "dịp 9/5 (Ngày Chiến thắng), và thường được ghép trong hành trình khám phá vùng Volokolamsk giàu "
        "di tích chiến tranh."
    ),
    "highlights_vi": [
        "Cụm sáu tượng chiến sĩ bằng đá granit cao khoảng 10 m, tượng trưng cho sáu dân tộc trong Sư đoàn Panfilov - một trong những tượng đài Chiến tranh Vệ quốc hoành tráng nhất ngoại ô Moskva.",
        "Gắn với câu nói biểu tượng gán cho chính trị viên Klochkov: «sau lưng là Moskva», và câu chuyện '28 anh hùng Panfilov' trong Trận chiến bảo vệ Moskva 1941.",
        "Khu ngoài trời với chiến hào phục dựng; gần làng Nelidovo có mộ tập thể và bảo tàng nhỏ; cách ga xép Dubosekovo chỉ vài trăm mét.",
    ],
    "practical": {
        "hours_vi": "Đài tưởng niệm ngoài trời, có thể tham quan tự do mọi lúc. Bảo tàng nhỏ ở Nelidovo và khu trưng bày mở theo giờ hành chính (nên kiểm tra trước).",
        "ticket_vi": "Vào khu tượng đài miễn phí. Bảo tàng ở Nelidovo có thể thu phí ở mức khiêm tốn.",
        "duration_vi": "Khoảng 30–60 phút cho khu tượng đài; thêm 30–45 phút nếu ghé bảo tàng Nelidovo.",
        "best_time_vi": "Dịp 9/5 (Ngày Chiến thắng) có lễ tưởng niệm trang trọng; mùa xuân - thu thuận tiện tham quan. Mùa đông cánh đồng phủ tuyết cũng tạo khung cảnh xúc động.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô hướng Rizhsky/Volokolamsk, xuống ngay ga xép Dubosekovo (đài tưởng niệm cách khoảng 300 m); hoặc tới Volokolamsk (~7 km) rồi bắt taxi. Có thể kết hợp thăm Kremlin Volokolamsk và Tu viện Iosifo-Volotsky trong cùng chuyến.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_org("https://yandex.com/maps/org/memorialny_kompleks_geroyam_panfilovtsam/144366155623/", "Panfilov Heroes Memorial Dubosekovo", "Moscow Oblast"),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Мемориал «Героям-панфиловцам»", "url": "https://ru.wikipedia.org/wiki/Мемориал_«Героям-панфиловцам»"},
        {"title": "GeoMerid — Мемориал Героям-Панфиловцам (Дубосеково)", "url": "https://geomerid.com/ru/place/memorial-geroyam-panfilovcam-dubosekovo/overview/"},
        {"title": "Yandex Maps — Мемориальный комплекс Героям-панфиловцам", "url": "https://yandex.com/maps/org/memorialny_kompleks_geroyam_panfilovtsam/144366155623/"},
    ],
    "tags": ["memorial", "wwii", "battle-of-moscow", "panfilov", "dubosekovo", "volokolamsk", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PRORYV_PANORAMA = {
    "id": "leningrad-oblast-proryv-panorama-museum",
    "slug": "proryv-panorama-museum",
    "region": "leningrad-oblast",
    "region_name_vi": "Tỉnh Leningrad",
    "federal_district": "Vùng Tây Bắc",
    "name_vi": "Bảo tàng Panorama «Proryv» (Chọc thủng vòng vây Leningrad)",
    "name_ru": "Музей-панорама «Прорыв»",
    "name_en": "Proryv Panorama Museum (Breakthrough of the Leningrad Siege)",
    "categories": ["museum", "monument"],
    "coordinates": {"lat": 59.90855, "lon": 30.99431},
    "address_vi": "Chân cầu Ladoga (bờ trái sông Neva), gần làng Maryino, thành phố Kirovsk, huyện Kirovsky, Tỉnh Leningrad; km 41 đường cao tốc Murmansk (R21 «Kola»), cách Saint Petersburg khoảng 40 km.",
    "rating": None,
    "presentation_short_vi": (
        "Bảo tàng Panorama «Proryv» là một trong những bảo tàng chiến tranh hiện đại và giàu cảm xúc nhất "
        "vùng Leningrad. Khánh thành ngày 18 tháng 1 năm 2018 nhân 75 năm ngày chọc thủng vòng vây "
        "Leningrad, panorama ba chiều tái hiện sống động một khoảnh khắc của trận đánh trên 'Mảnh đất Neva' "
        "(Nevsky Pyatachok) ngày 13/1/1943 - ngày thứ hai của Chiến dịch «Iskra». Người xem như bị đặt "
        "thẳng vào giữa trận địa."
    ),
    "presentation_long_vi": (
        "Tháng 1 năm 1943, Chiến dịch «Iskra» ('Tia lửa') của hai Phương diện quân Leningrad và Volkhov đã "
        "chọc thủng vòng vây phong tỏa Leningrad kéo dài gần 900 ngày, mở lại hành lang đường bộ nối thành "
        "phố với đất nước. Cụm bảo tàng - khu bảo tồn «Proryv blokady Leningrada» ở Kirovsk được lập nên "
        "để tưởng nhớ chiến dịch này, mà trung tâm ban đầu là bảo tàng - diorama nổi tiếng (khánh thành "
        "7/5/1985) gắn ngay trong khối bê tông của cầu Ladoga ở bờ trái sông Neva - đúng nơi bộ đội vượt "
        "sông năm 1943. Năm 2018, ngay cạnh diorama, khu này được bổ sung Bảo tàng Panorama «Proryv» - một "
        "panorama lịch sử - nghệ thuật ba chiều do họa sĩ Dmitry Poshtarenko và xưởng sáng tác «Nevsky "
        "Batalist» thực hiện. Khác với tranh panorama truyền thống, tác phẩm kết hợp hình nộm người kích "
        "thước thật, khí tài, âm thanh, ánh sáng và bố cục không gian để 'đóng băng' một khoảnh khắc chiến "
        "đấu cụ thể trên Nevsky Pyatachok - dải đầu cầu nhỏ bé mà đẫm máu bên tả ngạn Neva. Bước vào, "
        "khách như trở thành một người lính trong nhóm xung kích đang tấn công tuyến phòng ngự của địch, "
        "cảm nhận rõ 'hiệu ứng hiện diện'. Trong khuôn viên còn có trưng bày ngoài trời về xe tăng của "
        "chiến dịch (nhiều chiếc được trục vớt từ lòng sông Neva) cùng một số khí tài hiện đại. Nằm cùng "
        "cụm với diorama, đài Nevsky Pyatachok và cao điểm Sinyavino, «Proryv» là điểm đến đáng nhớ cho ai "
        "muốn hiểu về một trong những trang bi tráng nhất của Chiến tranh Vệ quốc, đồng thời là ví dụ tiêu "
        "biểu cho thế hệ bảo tàng nhập vai hiện đại của Nga."
    ),
    "highlights_vi": [
        "Panorama ba chiều nhập vai tái hiện trận đánh trên 'Mảnh đất Neva' ngày 13/1/1943, với hình nộm kích thước thật, khí tài, ánh sáng và âm thanh tạo 'hiệu ứng hiện diện'.",
        "Tác phẩm của họa sĩ Dmitry Poshtarenko và xưởng «Nevsky Batalist»; khánh thành năm 2018 nhân 75 năm chọc thủng vòng vây Leningrad.",
        "Nằm ngay chân cầu Ladoga cạnh bảo tàng - diorama (1985); có trưng bày ngoài trời nhiều xe tăng trục vớt từ sông Neva.",
    ],
    "practical": {
        "hours_vi": "Thường mở Thứ Ba–Thứ Năm và Chủ nhật 10:00–18:00; Thứ Sáu–Thứ Bảy 10:00–20:00; nghỉ Thứ Hai. Nên kiểm tra lịch trước khi đến.",
        "ticket_vi": "Vé thu phí theo suất (có ưu đãi cho học sinh, sinh viên, người cao tuổi; trẻ nhỏ thường miễn phí). Cuối tuần đông khách nên đặt trước hoặc đến sớm; có thể mua vé gộp cả panorama lẫn diorama.",
        "duration_vi": "Khoảng 1–1,5 giờ nếu xem cả panorama và diorama cùng khu trưng bày ngoài trời.",
        "best_time_vi": "Quanh năm (trưng bày trong nhà); dịp 18/1 và 27/1 (mốc phá vây và giải phóng hoàn toàn Leningrad) có nhiều hoạt động tưởng niệm.",
        "tips_vi": "Cách Saint Petersburg khoảng 40 km theo đường cao tốc Murmansk (R21). Có thể đi ô tô/taxi hoặc xe buýt tới Kirovsk/Maryino; nên ghép cùng pháo đài Oreshek (Shlisselburg) và đài Nevsky Pyatachok gần đó.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_text("Музей-панорама «Прорыв»", "Ленинградская область", "Proryv Panorama Museum Breakthrough of the Leningrad Siege", "Leningrad Oblast", 59.90855, 30.99431),
    "official_site": None,
    "sources": [
        {"title": "Культура.РФ — Музей-панорама «Прорыв»", "url": "https://www.culture.ru/institutes/97702/muzei-panorama-proryv"},
        {"title": "Музейное агентство ЛО — Музей-заповедник «Прорыв блокады Ленинграда»", "url": "https://www.lenoblmus.ru/museums/muzey-zapovednik-proryv-blokady-leningrada"},
        {"title": "Книга Памяти СЗФО (memgid.ru) — toạ độ GPS diorama/panorama «Прорыв»", "url": "https://memgid.ru/object/1377"},
    ],
    "tags": ["museum", "panorama", "wwii", "siege-of-leningrad", "operation-iskra", "nevsky-batalist", "kirovsk", "leningrad-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow-oblast.json": [KOLOMNA_PASTILA, DUBOSEKOVO],
    "leningrad-oblast.json": [PRORYV_PANORAMA],
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
