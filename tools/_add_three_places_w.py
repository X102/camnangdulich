# -*- coding: utf-8 -*-
"""_add_three_places_w.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26).

Thêm:
  1) Moscow          : Ga xe lửa Yaroslavsky (Yaroslavsky Vokzal) — điểm khởi đầu tuyến xuyên Siberia
  2) Saint Petersburg: Ga Phần Lan (Finlyandsky Vokzal) & Tượng đài Lenin
  3) Moscow          : Bảo tàng Quốc gia A.S. Pushkin trên phố Prechistenka (bảo tàng văn học)

Nội dung tiếng Việt nguyên gốc, có ghi nguồn. Toạ độ thật.
Chạy:  python3 tools/_add_three_places_w.py
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
YAROSLAVSKY_STATION = {
    "id": "moscow-yaroslavsky-railway-station",
    "slug": "yaroslavsky-railway-station",
    "region": "moscow",
    "region_name_vi": "Moskva",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Ga xe lửa Yaroslavsky (Yaroslavsky Vokzal)",
    "name_ru": "Ярославский вокзал",
    "name_en": "Moscow Yaroslavsky Railway Station",
    "categories": ["monument", "other"],
    "coordinates": {"lat": 55.776667, "lon": 37.656944},
    "address_vi": "Komsomolskaya ploshchad, 5, Moskva 107140 (Quảng trường Komsomolskaya — 'Quảng trường Ba Nhà Ga', quận Krasnoselsky; ngay cạnh ga metro vòng Komsomolskaya).",
    "rating": None,
    "presentation_short_vi": (
        "Nhà ga nhộn nhịp bậc nhất Moskva và là điểm khởi đầu của Đường sắt xuyên Siberia — tuyến "
        "đường sắt dài nhất thế giới. Toà nhà hiện nay (1902–1904) do kiến trúc sư Fyodor Shekhtel "
        "thiết kế theo phong cách Tân Nga pha Art Nouveau, với tháp cổng cao, mái lều và gạch men "
        "majolica gợi hình ảnh phương Bắc nước Nga."
    ),
    "presentation_long_vi": (
        "Nằm trên Quảng trường Komsomolskaya — quen gọi là «Quảng trường Ba Nhà Ga» vì quy tụ ba đầu "
        "mối đường sắt cạnh nhau (Yaroslavsky, Leningradsky và Kazansky) — ga Yaroslavsky là gương mặt "
        "được yêu thích nhất trong số đó. Nhà ga đầu tiên dựng thập niên 1860 để nối Moskva với vùng "
        "Sergiev Posad và Yaroslavl; đến các năm 1902–1904, kiến trúc sư bậc thầy của trường phái Tân "
        "nghệ thuật Nga Fyodor Shekhtel đã tái thiết mặt tiền thành một 'cổng dẫn về phương Bắc' đầy "
        "chất thơ. Ông dùng những mái lều dốc kiểu Nga cổ, tháp cổng vươn cao, cùng dải gạch men "
        "majolica nhiều màu điểm mô-típ thiên nhiên miền Bắc, khiến khối nhà bề thế mà vẫn duyên dáng "
        "như một cây chuyện cổ tích. Về vai trò, đây chính là ki-lô-mét số 0 của hành trình huyền "
        "thoại xuyên Siberia — con đường sắt dài khoảng 9.289 km chạy tới tận Vladivostok bên bờ Thái "
        "Bình Dương, và cũng là nơi tàu đi tuyến xuyên Mông Cổ, xuyên Mãn Châu khởi hành. Ngày nay ga "
        "vẫn tấp nập khách, là điểm dừng chân đáng ngắm cho du khách yêu kiến trúc: chỉ cần đứng trước "
        "quảng trường ngước nhìn mặt tiền, hoặc bước xuống ga metro vòng Komsomolskaya lộng lẫy ngay "
        "bên cạnh, là đã cảm nhận được nhịp lữ hành của nước Nga."
    ),
    "highlights_vi": [
        "Điểm xuất phát của Đường sắt xuyên Siberia — hành trình khoảng 9.289 km tới Vladivostok, dài nhất thế giới.",
        "Kiệt tác của kiến trúc sư Fyodor Shekhtel (1902–1904): tháp cổng, mái lều Nga cổ và gạch men majolica mang mô-típ phương Bắc.",
        "Toạ lạc trên Quảng trường Komsomolskaya — 'Quảng trường Ba Nhà Ga', kề bên ga Leningradsky và Kazansky.",
    ],
    "practical": {
        "hours_vi": "Ga hoạt động cả ngày; sảnh chờ mở phục vụ hành khách. Có thể ngắm mặt tiền và sảnh chính vào hầu hết thời gian trong ngày.",
        "ticket_vi": "Vào khu vực ga tự do; chỉ cần mua vé nếu đi tàu.",
        "duration_vi": "Khoảng 20–40 phút để ngắm kiến trúc bên ngoài và sảnh.",
        "best_time_vi": "Ban ngày để thấy rõ sắc men majolica; buổi tối tháp cổng được chiếu sáng đẹp.",
        "tips_vi": "Đi metro tới ga vòng Komsomolskaya (bản thân ga metro cũng là một kiệt tác) rồi tản bộ quanh Quảng trường Ba Nhà Ga; khu vực đông đúc nên chú ý giữ tư trang.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(55.776667, 37.656944),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN) — Moscow Yaroslavsky railway station", "url": "https://en.wikipedia.org/wiki/Moscow_Yaroslavsky_railway_station"},
        {"title": "Wikipedia (EN) — Fyodor Schechtel", "url": "https://en.wikipedia.org/wiki/Fyodor_Schechtel"},
        {"title": "Rusmania — Yaroslavsky Railway Station", "url": "https://rusmania.com/central/moscow-federal-city/moscow/krasnoselsky/beyond-the-garden-ring-around-komsomolskaya-ploschad/yaroslavsky-railway-station"},
    ],
    "tags": ["transport", "railway-station", "architecture", "art-nouveau", "shekhtel", "trans-siberian", "landmark"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


FINLAND_STATION = {
    "id": "saint-petersburg-finlyandsky-railway-station",
    "slug": "finlyandsky-railway-station",
    "region": "saint-petersburg",
    "region_name_vi": "Sankt-Peterburg",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Ga Phần Lan (Finlyandsky Vokzal) & Tượng đài Lenin",
    "name_ru": "Финляндский вокзал",
    "name_en": "Finlyandsky Railway Station (Finland Station) and Lenin Monument",
    "categories": ["monument", "other"],
    "coordinates": {"lat": 59.955556, "lon": 30.356111},
    "address_vi": "Ploshchad Lenina, 6, Sankt-Peterburg 194044 (Quảng trường Lenin, quận Kalininsky, bên tả ngạn sông Neva; trên ga metro Ploshchad Lenina).",
    "rating": None,
    "presentation_short_vi": (
        "Nhà ga đi vào lịch sử là nơi Lenin trở về Nga ngày 3/4/1917 và đọc diễn văn trên một chiếc "
        "xe bọc thép, châm ngòi cho chuỗi sự kiện Cách mạng. Trước ga, trên Quảng trường Lenin, sừng "
        "sững tượng đài Lenin dựng năm 1926 — một trong những tượng Lenin đầu tiên sau khi ông qua đời."
    ),
    "presentation_long_vi": (
        "Khánh thành năm 1870 và do Đường sắt Nhà nước Phần Lan xây dựng, Finlyandsky là nhà ga duy "
        "nhất ở Sankt-Peterburg từng nối thẳng ra nước ngoài — tới Helsinki và vùng Đại công quốc "
        "Phần Lan thuộc Nga khi xưa. Nhưng điều làm nên tên tuổi của ga lại là một buổi tối tháng Tư "
        "năm 1917: sau nhiều năm sống lưu vong ở Thuỵ Sĩ, Vladimir Lenin đáp «chuyến tàu niêm phong» "
        "băng qua Đức và Phần Lan để về đây, rồi trèo lên nóc một chiếc xe bọc thép đọc bài diễn văn "
        "nảy lửa trước đám đông công nhân, binh sĩ và thuỷ thủ — khoảnh khắc thường được xem là mở màn "
        "cho năm cách mạng. Năm 1926, trên quảng trường trước ga, người ta dựng tượng đài Lenin của "
        "nhà điêu khắc Sergey Yevseyev cùng hai kiến trúc sư Vladimir Shchuko và Vladimir Gelfreikh, "
        "tạc hình ông đang diễn thuyết trên bệ mô phỏng tháp pháo xe bọc thép. Trong sân ga còn lưu "
        "giữ đầu máy hơi nước số 293 — món quà của Phần Lan, gắn với hành trình bí mật của Lenin — "
        "được bảo quản trong một nhà kính. Ga cũng mang ký ức bi tráng của Thế chiến II: suốt những "
        "năm Leningrad bị vây hãm, đây là đầu mối đường sắt nối với «Con đường Sự sống» băng qua hồ "
        "Ladoga, tiếp tế cho thành phố. Toà nhà ga ngày nay được xây lại theo lối hiện đại thập niên "
        "1950–1960, giữ lại một mảng mặt tiền cũ như chứng tích thời gian."
    ),
    "highlights_vi": [
        "Nơi Lenin trở về từ nơi lưu vong (3/4/1917) và diễn thuyết trên xe bọc thép — thời khắc mở màn cho năm cách mạng 1917.",
        "Tượng đài Lenin trên Quảng trường Lenin (1926) của điêu khắc gia Sergey Yevseyev cùng kiến trúc sư Shchuko và Gelfreikh.",
        "Lưu giữ đầu máy hơi nước số 293; trong Thế chiến II, ga là đầu mối nối 'Con đường Sự sống' qua hồ Ladoga.",
    ],
    "practical": {
        "hours_vi": "Ga và quảng trường mở suốt ngày; tượng đài ngoài trời tham quan tự do. Đầu máy 293 trưng bày trong nhà kính ở khu sân ga (xem theo giờ hoạt động của ga).",
        "ticket_vi": "Tham quan quảng trường và tượng đài miễn phí.",
        "duration_vi": "Khoảng 30 phút.",
        "best_time_vi": "Ban ngày; nên kết hợp lịch trình đi metro.",
        "tips_vi": "Đi metro tuyến đỏ (số 1) tới ga Ploshchad Lenina, lên thẳng quảng trường trước nhà ga; từ bờ Neva gần đó có thể ngắm sang trung tâm lịch sử và tuần dương hạm Rạng Đông ở bờ đối diện.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(59.955556, 30.356111),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN) — Finland Station", "url": "https://en.wikipedia.org/wiki/Finland_Station"},
        {"title": "Saint-Petersburg.com — Monument to Lenin on Ploshchad Lenina", "url": "http://www.saint-petersburg.com/monuments/ploshchad-lenina/"},
        {"title": "Russian Trains — Finlyandsky Train Station in Saint Petersburg", "url": "https://www.russiantrains.com/en/station/finlyandsky-st-petersburg"},
    ],
    "tags": ["monument", "railway-station", "lenin", "history", "soviet", "1917", "road-of-life"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PUSHKIN_STATE_MUSEUM = {
    "id": "moscow-pushkin-state-museum",
    "slug": "pushkin-state-museum",
    "region": "moscow",
    "region_name_vi": "Moskva",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Bảo tàng Quốc gia A.S. Pushkin (Puskin) trên phố Prechistenka",
    "name_ru": "Государственный музей А. С. Пушкина",
    "name_en": "State Museum of A.S. Pushkin (Prechistenka)",
    "categories": ["museum"],
    "coordinates": {"lat": 55.744167, "lon": 37.597778},
    "address_vi": "Ulitsa Prechistenka, 12/2, Moskva 119034 (dinh thự Khrushchev–Seleznyov, gần ga metro Kropotkinskaya).",
    "rating": None,
    "presentation_short_vi": (
        "Một trong những bảo tàng văn học lớn nhất nước Nga, dành trọn cho đại thi hào Aleksandr "
        "Pushkin. Bảo tàng toạ lạc trong dinh thự quý tộc Khrushchev–Seleznyov đầu thế kỷ 19 theo "
        "phong cách Đế chế Nga trên con phố cổ Prechistenka."
    ),
    "presentation_long_vi": (
        "Đừng nhầm với Bảo tàng Mỹ thuật Pushkin (một bảo tàng nghệ thuật cùng mang tên nhà thơ): đây "
        "là bảo tàng văn học tưởng niệm chính về Aleksandr Sergeyevich Pushkin — người được xem là "
        "'Mặt trời của thi ca Nga'. Được thành lập năm 1957, bảo tàng chiếm trọn khu dinh thự "
        "Khrushchev–Seleznyov, một điền trang gỗ theo phong cách Đế chế (Empire) thanh nhã dựng lại "
        "sau trận đại hoả hoạn Moskva năm 1812 — chính là kiểu kiến trúc quý tộc mà Pushkin từng sống "
        "giữa lòng nó. Bên trong, du khách lần theo cuộc đời và sự nghiệp của thi hào qua các gian "
        "trưng bày cố định: bản thảo và thủ bút, những ấn bản đầu tiên, chân dung nhà thơ cùng bằng "
        "hữu, tranh minh hoạ cho «Yevgeny Onegin», «Con đầm bích», các truyện cổ tích thơ, và vô số "
        "kỷ vật tái hiện đời sống thượng lưu Nga đầu thế kỷ 19. Bảo tàng còn là một trung tâm nghiên "
        "cứu, giáo dục lớn, thường xuyên tổ chức triển lãm chuyên đề, buổi đọc thơ và hoà nhạc. Trong "
        "hệ thống của bảo tàng còn có chi nhánh Căn hộ-Bảo tàng Pushkin trên phố Arbat (số 53) — nơi "
        "nhà thơ sống những tháng đầu sau khi cưới Natalia Goncharova. Với người yêu văn chương, đây "
        "là nơi cảm nhận rõ nhất không khí 'Moskva của Pushkin'."
    ),
    "highlights_vi": [
        "Bảo tàng văn học hàng đầu về Pushkin: thủ bút, ấn bản đầu, chân dung và tranh minh hoạ cho các tác phẩm của ông.",
        "Đặt trong dinh thự Khrushchev–Seleznyov — công trình gỗ phong cách Đế chế Nga dựng lại sau đám cháy Moskva 1812.",
        "Khác với Bảo tàng Mỹ thuật Pushkin; hệ thống còn có chi nhánh Căn hộ-Bảo tàng Pushkin trên phố Arbat (số 53).",
    ],
    "practical": {
        "hours_vi": "Thường mở cửa Thứ Ba–Chủ Nhật 10:00–18:00, riêng Thứ Năm 13:00–21:00; đóng cửa Thứ Hai (và thường có một 'ngày vệ sinh' cuối tháng). Phòng vé đóng trước giờ mở cửa khoảng 30 phút — nên kiểm tra lịch mới nhất trên trang chính thức.",
        "ticket_vi": "Mua vé tại quầy hoặc trực tuyến trên pushkinmuseum.ru; có vé tổ hợp cho nhiều gian/triển lãm.",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Ngày thường để tham quan yên tĩnh.",
        "tips_vi": "Gần metro Kropotkinskaya; có thể kết hợp dạo phố Prechistenka nhiều dinh thự cổ và ghé Nhà thờ Chúa Cứu Thế gần đó.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(55.744167, 37.597778),
    "official_site": "https://www.pushkinmuseum.ru/",
    "sources": [
        {"title": "Express to Russia — State Museum of A.S. Pushkin, Moscow", "url": "https://www.expresstorussia.com/guide/state-museum-of-a-s-pushkin-moscow.html"},
        {"title": "Google Arts & Culture — The State A.S. Pushkin Museum", "url": "https://artsandculture.google.com/partner/state-pushkin-museum"},
        {"title": "Trang chính thức — Bảo tàng Quốc gia A.S. Pushkin", "url": "https://www.pushkinmuseum.ru/"},
    ],
    "tags": ["museum", "literature", "pushkin", "empire-style", "mansion", "prechistenka"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow.json": [YAROSLAVSKY_STATION, PUSHKIN_STATE_MUSEUM],
    "saint-petersburg.json": [FINLAND_STATION],
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
        # backup
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
