# -*- coding: utf-8 -*-
"""_add_three_places_x.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26).

Thêm:
  1) Moscow          : Nhà thờ Kazan trên Quảng trường Đỏ (church) — ngôi đền bị phá 1936, phục dựng 1990–1993
  2) Saint Petersburg: Bảo tàng Anna Akhmatova tại Ngôi nhà Fontanka (museum) — bảo tàng văn học
  3) Moscow Oblast   : Nhà thờ Chính của Các Lực lượng Vũ trang Nga (church/monument) — công trình hiện đại 2020

Nội dung tiếng Việt nguyên gốc, có ghi nguồn. Toạ độ thật (đã đối chiếu web 2026-07).
Chạy:  python3 tools/_add_three_places_x.py
"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-26"


def maps_for(lat, lon):
    return {
        "yandex": f"https://yandex.com/maps/?pt={lon},{lat}&z=17&l=map",
        "google": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
    }


# ------------------------------------------------------------------ RECORDS
KAZAN_CATHEDRAL = {
    "id": "moscow-kazan-cathedral",
    "slug": "kazan-cathedral",
    "region": "moscow",
    "region_name_vi": "Moskva",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Nhà thờ Kazan trên Quảng trường Đỏ",
    "name_ru": "Казанский собор",
    "name_en": "Kazan Cathedral, Moscow",
    "categories": ["church"],
    "coordinates": {"lat": 55.755481, "lon": 37.619211},
    "address_vi": "Góc đông bắc Quảng trường Đỏ, nơi phố Nikolskaya đổ ra, Moskva 109012; đối diện Bảo tàng Lịch sử Quốc gia, gần ga metro Ploshchad Revolyutsii/Okhotny Ryad.",
    "rating": None,
    "presentation_short_vi": (
        "Thánh đường Chính thống giáo nhỏ nhắn mang sắc đỏ - trắng đứng ở góc đông bắc Quảng trường Đỏ, "
        "nơi phố đi bộ Nikolskaya mở ra. Nhà thờ đầu tiên dựng năm 1636 để tạ ơn biểu tượng Đức Mẹ Kazan "
        "sau khi Moskva được giải phóng năm 1612; bị phá huỷ năm 1936 rồi phục dựng gần như nguyên trạng "
        "vào các năm 1990–1993, trở thành ngôi đền đã mất đầu tiên trên quảng trường được hồi sinh."
    ),
    "presentation_long_vi": (
        "Nhà thờ Kazan gắn liền với một trong những trang sử bi tráng nhất của nước Nga: cuộc kháng chiến "
        "khép lại 'Thời Loạn Lạc' đầu thế kỉ 17. Tương truyền đội dân binh của công tước Dmitry Pozharsky "
        "đã mang theo bản sao biểu tượng Đức Mẹ Kazan khi tiến vào giải phóng Moskva khỏi quân Ba Lan - Litva "
        "năm 1612; sau chiến thắng, một nhà thờ (hoàn tất bằng gạch năm 1636) được dựng ngay cạnh Quảng "
        "trường Đỏ để tôn vinh biểu tượng ấy. Công trình mang dáng dấp nhà thờ 'posad' tiêu biểu của Moskva: "
        "khối gạch đỏ điểm chi tiết trắng, một vòm củ hành và những tầng mái nhọn kokoshnik xếp chồng thanh "
        "thoát. Năm 1936, giữa cao trào bài trừ tôn giáo, chính quyền Xô Viết cho san phẳng nhà thờ để lấy "
        "chỗ duyệt binh trên Quảng trường Đỏ - đây là một trong những ngôi đền đầu tiên bị xoá sổ. Nhưng "
        "trước khi phá dỡ, kiến trúc sư - nhà bảo tồn Pyotr Baranovsky đã kịp đo vẽ và ghi chép tỉ mỉ toàn "
        "bộ công trình. Nửa thế kỉ sau, chính những bản vẽ ấy giúp học trò của ông là Oleg Zhurin phục dựng "
        "nhà thờ gần như nguyên bản: viên đá đầu tiên được Thượng phụ Aleksi II đặt ngày 4 tháng 11 năm 1990, "
        "và ngày 4 tháng 11 năm 1993 thánh đường được thánh hiến trở lại. Nhờ vậy, Kazan trở thành ngôi đền "
        "đã mất đầu tiên trên Quảng trường Đỏ được tái sinh - một biểu tượng cho sự hồi sinh của di sản Nga. "
        "Ngày nay đây là nhà thờ đang hoạt động, mở cửa tự do cho khách viếng và lưu giữ bản biểu tượng Đức "
        "Mẹ Kazan được tôn kính."
    ),
    "highlights_vi": [
        "Ngôi đền đầu tiên bị phá trên Quảng trường Đỏ được phục dựng gần như nguyên trạng (1990–1993).",
        "Gắn với cuộc giải phóng Moskva năm 1612 và biểu tượng linh thiêng Đức Mẹ Kazan.",
        "Kiến trúc gạch đỏ - trắng với vòm củ hành và các tầng mái kokoshnik đặc trưng Moskva.",
    ],
    "practical": {
        "hours_vi": "Nhà thờ đang hoạt động, thường mở khoảng 8:00–19:00 hằng ngày theo lịch lễ.",
        "ticket_vi": "Vào cửa tự do (miễn phí).",
        "duration_vi": "Khoảng 15–20 phút.",
        "best_time_vi": "Sáng sớm yên tĩnh; nếu chỉ tham quan nên tránh giờ hành lễ.",
        "tips_vi": "Ăn mặc kín đáo, nữ nên có khăn trùm đầu, nam bỏ mũ; tiện kết hợp dạo Quảng trường Đỏ, trung tâm GUM và phố Nikolskaya ngay bên cạnh.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(55.755481, 37.619211),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN) — Kazan Cathedral, Moscow", "url": "https://en.wikipedia.org/wiki/Kazan_Cathedral,_Moscow"},
        {"title": "OrthodoxWiki — Kazan Cathedral (Moscow)", "url": "https://orthodoxwiki.org/Kazan_Cathedral_(Moscow)"},
        {"title": "Rusmania — Our Lady of Kazan Cathedral", "url": "https://rusmania.com/central/moscow-federal-city/moscow/central-moscow/around-red-square/our-lady-of-kazan-cathedral"},
    ],
    "tags": ["church", "orthodox", "red-square", "history", "reconstruction"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


AKHMATOVA_MUSEUM = {
    "id": "saint-petersburg-akhmatova-museum-fountain-house",
    "slug": "akhmatova-museum-fountain-house",
    "region": "saint-petersburg",
    "region_name_vi": "Saint Petersburg",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Bảo tàng Anna Akhmatova tại Ngôi nhà Fontanka",
    "name_ru": "Музей Анны Ахматовой в Фонтанном доме",
    "name_en": "Anna Akhmatova Museum at the Fountain House",
    "categories": ["museum"],
    "coordinates": {"lat": 59.9364, "lon": 30.3478},
    "address_vi": "Lối vào từ đại lộ Liteyny số 53 (qua cổng vòm) hoặc kè sông Fontanka số 34, Saint Petersburg 191014; trong cánh nam của Cung điện Sheremetev (Ngôi nhà Fontanka).",
    "rating": None,
    "presentation_short_vi": (
        "Bảo tàng văn học tưởng niệm nữ thi sĩ Anna Akhmatova, đặt trong cánh nhìn ra vườn của Cung điện "
        "Sheremetev - nơi bà sống gần ba thập kỉ. Khánh thành ngày 24 tháng 6 năm 1989 nhân 100 năm ngày "
        "sinh của bà, bảo tàng tái hiện căn hộ tưởng niệm và không khí văn chương Nga đầu - giữa thế kỉ 20."
    ),
    "presentation_long_vi": (
        "'Ngôi nhà Fontanka' (Fontanny Dom) là dinh thự cổ của dòng họ bá tước Sheremetev bên bờ sông "
        "Fontanka. Trong cánh nam nhìn ra khu vườn, nữ thi sĩ Anna Akhmatova - một trong những tiếng thơ "
        "lớn nhất của nước Nga thế kỉ 20 - đã sống từ năm 1926 đến 1952 theo lời mời của nhà nghiên cứu nghệ "
        "thuật Nikolai Punin. Chính tại đây, giữa những năm tháng ngặt nghèo của thời Đại Thanh trừng và "
        "cuộc phong toả Leningrad, bà đã viết nhiều phần của trường ca 'Khúc tưởng niệm' (Requiem) và 'Bài "
        "thơ không có nhân vật'. Bảo tàng mở cửa ngày 24 tháng 6 năm 1989, đúng dịp kỉ niệm 100 năm ngày "
        "sinh Akhmatova, ban đầu là chi nhánh của Bảo tàng Dostoevsky. Không gian trưng bày gồm hai phần: "
        "căn hộ tưởng niệm được phục dựng theo hồi ức của người thân và bạn văn, tái hiện phòng của Akhmatova "
        "cùng gia đình Punin; và phần trưng bày văn học - nghệ thuật giới thiệu cuộc đời, di cảo, thư từ, ảnh "
        "và đồ dùng cá nhân của bà. Bộ sưu tập của bảo tàng có tới khoảng 50 nghìn hiện vật. Khu vườn yên "
        "tĩnh phía sau, nơi thường có các buổi đọc thơ và hoà nhạc mùa hè, khiến đây trở thành một trong "
        "những địa chỉ văn hoá được giới trí thức Saint Petersburg yêu mến nhất. Với người yêu văn chương "
        "Nga, đến thăm Ngôi nhà Fontanka là dịp bước vào chính không gian đã chứng kiến và nuôi dưỡng những "
        "vần thơ bất hủ của Akhmatova."
    ),
    "highlights_vi": [
        "Căn hộ nơi Anna Akhmatova sống 1926–1952, được phục dựng thành không gian tưởng niệm.",
        "Khánh thành ngày 24/6/1989 nhân 100 năm ngày sinh nữ thi sĩ; sưu tập khoảng 50.000 hiện vật.",
        "Nằm trong Cung điện Sheremetev bên sông Fontanka, có khu vườn thường tổ chức đọc thơ - hoà nhạc.",
    ],
    "practical": {
        "hours_vi": "Thường mở 10:30–18:30 (thứ Ba mở muộn hơn, tới khoảng 20:00), nghỉ thứ Hai; giờ có thể thay đổi nên xem trang chính thức.",
        "ticket_vi": "Có bán vé vào cửa, nhiều mức ưu đãi cho học sinh - sinh viên - người cao tuổi (xem giá hiện hành trên trang chính thức).",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Ngày thường để tránh đông; mùa hè có thể kết hợp sự kiện ngoài vườn.",
        "tips_vi": "Lối vào chính từ đại lộ Liteyny 53 qua cổng vòm rồi băng qua sân; tiện kết hợp thăm Cung điện Sheremetev (Bảo tàng Âm nhạc) trong cùng khuôn viên.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(59.9364, 30.3478),
    "official_site": "https://www.akhmatova.spb.ru",
    "sources": [
        {"title": "Wikipedia (EN) — Anna Akhmatova Literary and Memorial Museum", "url": "https://en.wikipedia.org/wiki/Anna_Akhmatova_Literary_and_Memorial_Museum"},
        {"title": "Trang chính thức — The Anna Akhmatova Museum in the Fountain House", "url": "https://www.akhmatova.spb.ru/en"},
        {"title": "Rusmania — Anna Akhmatova Museum in the Fountain House", "url": "https://rusmania.com/north-western/st-petersburg-federal-city/st-petersburg/bezymyanny-island-and-the-south/around-liteyny-prospekt/anna-akhmatova-museum-in-the-fountain-house"},
    ],
    "tags": ["museum", "literature", "akhmatova", "poetry", "memorial", "fountain-house"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


ARMED_FORCES_CATHEDRAL = {
    "id": "moscow-oblast-armed-forces-cathedral",
    "slug": "armed-forces-cathedral",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Nhà thờ Chính của Các Lực lượng Vũ trang Nga (Công viên Patriot)",
    "name_ru": "Главный храм Вооружённых сил России",
    "name_en": "Main Cathedral of the Russian Armed Forces",
    "categories": ["church", "monument"],
    "coordinates": {"lat": 55.57917, "lon": 36.82194},
    "address_vi": "Công viên Patriot, Kubinka, huyện Odintsovo, Tỉnh Moskva; cách trung tâm Moskva khoảng 55 km về phía tây theo cao tốc Minsk (M1).",
    "rating": None,
    "presentation_short_vi": (
        "Thánh đường quân đội đồ sộ màu xanh ô-liu, thánh hiến năm 2020 nhân 75 năm Chiến thắng trong Chiến "
        "tranh Vệ quốc Vĩ đại. Nằm trong Công viên Patriot ở Kubinka, đây là một trong những nhà thờ Chính "
        "thống giáo cao nhất thế giới, với mỗi kích thước đều mã hoá một mốc lịch sử của cuộc chiến."
    ),
    "presentation_long_vi": (
        "Nhà thờ Chính của Các Lực lượng Vũ trang Nga - còn gọi là Nhà thờ Phục Sinh - là công trình tôn "
        "giáo kiêm đài tưởng niệm chiến tranh, xây trong Công viên quân sự - yêu nước Patriot ở Kubinka, phía "
        "tây Moskva. Được thánh hiến ngày 14 tháng 6 năm 2020 đúng dịp 75 năm chiến thắng phát xít, thánh "
        "đường gây ấn tượng mạnh bởi sắc xanh ô-liu (kaki) quân đội thay cho màu trắng - vàng truyền thống, "
        "cùng những vòm mái kim loại và phong cách Byzantine - Nga hoành tráng. Với chiều cao khoảng 95 m "
        "tính đến đỉnh thánh giá, đây là một trong những nhà thờ Chính thống giáo cao nhất thế giới. Toàn bộ "
        "kích thước công trình đều ẩn chứa con số biểu tượng: đường kính tang trống vòm chính 19,45 m ứng "
        "với năm 1945, tháp chuông cao 75 m gợi 75 năm Chiến thắng, các vòm nhỏ cao 14,18 m nhắc tới 1418 "
        "ngày đêm của cuộc chiến. Bên trong là những bức tranh khảm (mosaic) khổng lồ tái hiện các trận đánh; "
        "tương truyền bậc thềm được đúc từ kim loại nấu chảy của khí tài quân sự thu được. Bao quanh nhà thờ "
        "là quần thể bảo tàng - triển lãm 'Con đường Kí ức' (Doroga Pamyati) dài đúng 1.418 mét, dùng màn "
        "hình tương tác và nhiều triệu bức ảnh tư liệu để đưa khách đi qua từng ngày của cuộc chiến. Dù còn "
        "gây tranh luận về sự hoà trộn giữa tôn giáo và quân sự, đây vẫn là điểm đến gây choáng ngợp về quy "
        "mô và là công trình tiêu biểu cho dòng kiến trúc tưởng niệm hiện đại của nước Nga."
    ),
    "highlights_vi": [
        "Nhà thờ quân đội màu xanh ô-liu, thánh hiến năm 2020 nhân 75 năm Chiến thắng Vệ quốc.",
        "Cao khoảng 95 m - một trong những thánh đường Chính thống giáo cao nhất thế giới; kích thước mã hoá các mốc chiến tranh (1945, 75 năm, 1418 ngày).",
        "Quần thể bảo tàng 'Con đường Kí ức' dài 1.418 m bao quanh, cùng các bức tranh khảm hoành tráng.",
    ],
    "practical": {
        "hours_vi": "Khuôn viên và nhà thờ mở cửa hằng ngày (thường 9:00–20:00); bảo tàng 'Con đường Kí ức' có giờ riêng.",
        "ticket_vi": "Vào nhà thờ tự do; một số phần bảo tàng trong Công viên Patriot có thể bán vé riêng.",
        "duration_vi": "Khoảng 2–3 giờ nếu kết hợp tham quan bảo tàng và công viên.",
        "best_time_vi": "Ban ngày trời quang để thấy rõ sắc kim loại của mái vòm; dịp gần 9/5 (Ngày Chiến thắng) rất đông.",
        "tips_vi": "Cách Moskva ~55 km, tiện nhất là đi ô tô theo cao tốc M1; ăn mặc kín đáo khi vào nhà thờ; nên dành thời gian cho bảo tàng 'Con đường Kí ức'.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(55.57917, 36.82194),
    "official_site": "https://hram.mil.ru",
    "sources": [
        {"title": "Wikipedia (EN) — Main Cathedral of the Russian Armed Forces", "url": "https://en.wikipedia.org/wiki/Main_Cathedral_of_the_Russian_Armed_Forces"},
        {"title": "Atlas Obscura — Main Cathedral of the Russian Armed Forces", "url": "https://www.atlasobscura.com/places/main-cathedral-of-the-russian-armed-forces"},
        {"title": "Rusmania — Day tour to the Military Cathedral", "url": "https://rusmania.com/tours/day-tour-military-cathedral-moscow"},
    ],
    "tags": ["church", "memorial", "military", "modern", "mosaic", "patriot-park", "wwii"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow.json": [KAZAN_CATHEDRAL],
    "saint-petersburg.json": [AKHMATOVA_MUSEUM],
    "moscow-oblast.json": [ARMED_FORCES_CATHEDRAL],
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
