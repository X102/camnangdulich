# -*- coding: utf-8 -*-
"""_add_three_places_t.py — Bổ sung 3 địa điểm nổi tiếng còn thiếu.
Moscow: Khách sạn Metropol; Ga xe lửa Kievsky.
Saint Petersburg: Tàu phá băng - bảo tàng Krasin.
Nội dung tiếng Việt nguyên gốc; toạ độ & dữ kiện đã kiểm chứng qua nguồn ghi trong 'sources'.
Chạy: python3 tools/_add_three_places_t.py
"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TODAY = "2026-07-26"
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

NEW = [
    {
        "id": "moscow-metropol-hotel",
        "slug": "metropol-hotel",
        "region": "moscow",
        "region_name_vi": "Moskva",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Khách sạn Metropol",
        "name_ru": "Гостиница «Метрополь»",
        "name_en": "Hotel Metropol",
        "categories": ["other"],
        "coordinates": {"lat": 55.7586, "lon": 37.6214},
        "address_vi": "Teatralny Proezd 2, Moskva 109012 (đối diện Nhà hát Bolshoi; ga metro Teatralnaya / Ploshchad Revolyutsii)",
        "rating": None,
        "review_summary_vi": """Du khách trầm trồ trước mặt tiền Art Nouveau và bức tranh gốm 'Công chúa trong mộng' của Vrubel, xem đây là một trong những tòa nhà đẹp nhất trung tâm Moskva. Nhiều người khen đại sảnh nhà hàng mái kính sang trọng. Lưu ý: đây là khách sạn 5 sao nên phần lớn không gian bên trong dành cho khách lưu trú và thực khách; người tham quan thường chỉ ngắm và chụp ảnh mặt tiền từ bên ngoài.""",
        "presentation_short_vi": """Khách sạn hạng sang mang tính biểu tượng của Moskva, dựng năm 1899–1905 ngay đối diện Nhà hát Bolshoi. Đây là một trong những công trình đẹp nhất của phong cách Modern (Art Nouveau) Nga, nổi bật với bức tranh gốm majolica khổ lớn 'Công chúa trong mộng' của danh họa Mikhail Vrubel trên mặt tiền.""",
        "presentation_long_vi": """Metropol ra đời từ giấc mơ của nhà bảo trợ nghệ thuật Savva Mamontov: một tổ hợp văn hóa - khách sạn hoành tráng ở ngay trung tâm Moskva, nơi hội tụ hội họa, âm nhạc và kiến trúc mới. Công trình được khởi công năm 1899 và hoàn thành năm 1905, sau khi một trận hỏa hoạn lớn năm 1901 thiêu rụi phần đang xây và buộc phải làm lại. Phần mặt tiền theo phong cách Modern (Art Nouveau) do kiến trúc sư người Anh William Walcot phác thảo, còn kiến trúc sư Nga Lev Kekushev giám sát thi công. Điều khiến Metropol trở thành một 'bảo tàng ngoài trời' chính là những bức tranh gốm majolica ốp trên mặt tiền, do các nghệ sĩ của xưởng gốm Abramtsevo chế tác. Nổi tiếng nhất là bức 'Công chúa trong mộng' (Printsessa Gryoza) khổ lớn của Mikhail Vrubel nhìn ra phố Teatralny Proezd, lấy cảm hứng từ vở kịch của nhà thơ Pháp Edmond Rostand; nhiều bức nhỏ hơn do Alexander Golovin thực hiện. Sau Cách mạng, Metropol có một thời gian được dùng làm 'Ngôi nhà Xô-viết thứ hai' - nơi họp của các cơ quan chính quyền mới và Lenin từng phát biểu tại đây - trước khi trở lại công năng khách sạn. Trải qua hơn một thế kỷ, nơi đây từng đón vô số nhân vật nổi tiếng và đến nay vẫn vừa là chỗ lưu trú, vừa là điểm để chiêm ngưỡng kiến trúc. Bên trong, đại sảnh nhà hàng lợp mái kính khổng lồ cùng đài phun nước là không gian được nhắc đến nhiều.""",
        "highlights_vi": [
            "Kiệt tác kiến trúc Modern (Art Nouveau) Nga, xây 1899–1905 theo ý tưởng của nhà bảo trợ Savva Mamontov; mặt tiền do kiến trúc sư Anh William Walcot thiết kế.",
            "Bức tranh gốm majolica 'Công chúa trong mộng' của Mikhail Vrubel trên mặt tiền - một biểu tượng của mỹ thuật Nga đầu thế kỷ 20, chế tác tại xưởng Abramtsevo.",
            "Vị trí đắc địa đối diện Nhà hát Bolshoi và gần Quảng trường Đỏ; thời Xô-viết từng là trụ sở cơ quan chính quyền ('Ngôi nhà Xô-viết thứ hai') nơi Lenin phát biểu."
        ],
        "practical": {
            "hours_vi": "Là khách sạn đang hoạt động nên có thể ngắm mặt tiền và tranh gốm bất cứ lúc nào từ bên ngoài; nhà hàng và các không gian bên trong mở theo giờ phục vụ khách.",
            "ticket_vi": "Ngắm và chụp mặt tiền miễn phí. Vào bên trong (nhà hàng, quầy bar, lưu trú) theo mức giá dịch vụ của khách sạn.",
            "duration_vi": "Khoảng 15–30 phút nếu chỉ ngắm mặt tiền và tranh gốm.",
            "best_time_vi": "Ban ngày để thấy rõ màu sắc bức majolica; buổi tối mặt tiền được chiếu sáng đẹp.",
            "tips_vi": "Đi bộ từ Quảng trường Đỏ hoặc ga metro Teatralnaya / Ploshchad Revolyutsii. Kết hợp tham quan Nhà hát Bolshoi, Quảng trường Nhà hát và phố Nikolskaya ngay gần đó."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=37.6214,55.7586&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=55.7586,37.6214"
        },
        "official_site": "https://metropol-moscow.ru/",
        "sources": [
            {"title": "Hotel Metropol Moscow — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Hotel_Metropol_Moscow"},
            {"title": "Metropol Hotel façades to be restored — Moscow City (mos.ru)", "url": "https://www.mos.ru/en/news/item/31480073/"},
            {"title": "History — Metropol Hotel Moscow", "url": "https://metropol-moscow.ru/en/history/"}
        ],
        "tags": ["architecture", "art-nouveau", "modern-style", "historic-hotel", "landmark", "early-20th-century"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "moscow-kievsky-railway-station",
        "slug": "kievsky-railway-station",
        "region": "moscow",
        "region_name_vi": "Moskva",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Ga xe lửa Kievsky (Kievsky Vokzal)",
        "name_ru": "Киевский вокзал",
        "name_en": "Kievsky Railway Station",
        "categories": ["other"],
        "coordinates": {"lat": 55.7431, "lon": 37.5672},
        "address_vi": "Quảng trường Ga Kievsky (Ploshchad Kievskogo Vokzala) 1, bên Quảng trường Châu Âu (Ploshchad Evropy), Moskva; ga metro Kievskaya",
        "rating": None,
        "review_summary_vi": """Du khách đánh giá cao vẻ bề thế của mặt tiền và tháp đồng hồ, đặc biệt ấn tượng với mái vòm kính Shukhov phủ trên sân ga - một 'bảo tàng kỹ thuật' sống động. Nhiều người kết hợp ghé Quảng trường Châu Âu bên sông Moskva. Lưu ý: đây là nhà ga bận rộn nên khu vực sân ga khá đông, cần chú ý an ninh và giữ gìn hành lý.""",
        "presentation_short_vi": """Một trong những nhà ga đẹp và nổi tiếng nhất Moskva, khánh thành năm 1918 ở cửa ngõ phía tây nam thành phố. Ga gây ấn tượng với tháp đồng hồ cao 51 m và mái vòm kính khổng lồ hình parabol do kỹ sư thiên tài Vladimir Shukhov thiết kế phủ trên các sân ke tàu.""",
        "presentation_long_vi": """Ban đầu mang tên ga Bryansky, nhà ga được xây trong các năm 1914–1918 để phục vụ tuyến đường sắt đi về hướng tây nam. Phần kiến trúc theo phong cách Tân cổ điển (Empire) do kiến trúc sư Ivan Rerberg đảm nhiệm, với điểm nhấn là tháp đồng hồ cao 51 m gợi dáng một tháp chuông kiểu Ý. Chiếc đồng hồ cơ trên tháp đến nay vẫn chạy và là một trong hai đồng hồ tháp cơ khí còn hoạt động ở Moskva, cùng với đồng hồ trên tháp Spasskaya của Kremlin. Nhưng công trình được giới kỹ thuật ngưỡng mộ nhất chính là mái che sân ga: một vòm kính khổng lồ hình parabol bằng khung thép do kỹ sư Vladimir Shukhov - bậc thầy về kết cấu của nước Nga - thiết kế, dài khoảng 321 m, rộng gần 48 m, cao khoảng 30 m và nặng hơn một nghìn tấn. Năm 1934, ga được đổi tên thành Kievsky theo điểm đến chính của tuyến là thành phố Kiev. Ngày nay ga nằm bên Quảng trường Châu Âu (Ploshchad Evropy) ven sông Moskva, cạnh trung tâm thương mại và đầu mối metro Kievskaya sầm uất; các sảnh bên trong còn được trang trí bằng tranh tường. Đây vừa là đầu mối giao thông, vừa là một di tích kiến trúc mà du khách nên ghé ngắm.""",
        "highlights_vi": [
            "Nhà ga (nguyên là ga Bryansky) xây 1914–1918, kiến trúc Tân cổ điển của Ivan Rerberg, đổi tên thành Kievsky năm 1934.",
            "Mái che sân ga bằng kính hình parabol của kỹ sư Vladimir Shukhov - dài khoảng 321 m, rộng gần 48 m: một kỳ công kết cấu thép đầu thế kỷ 20.",
            "Tháp đồng hồ cao 51 m với đồng hồ cơ vẫn chạy - một trong hai đồng hồ tháp cơ khí còn hoạt động ở Moskva (cùng tháp Spasskaya của Kremlin)."
        ],
        "practical": {
            "hours_vi": "Là nhà ga đang hoạt động, khu vực công cộng mở gần như cả ngày; ra vào sảnh và sân ga theo quy định an ninh đường sắt.",
            "ticket_vi": "Tham quan bên ngoài và các sảnh công cộng miễn phí.",
            "duration_vi": "Khoảng 20–40 phút để ngắm mặt tiền, tháp đồng hồ và mái kính Shukhov.",
            "best_time_vi": "Ban ngày để thấy rõ vòm kính; kết hợp ngắm Quảng trường Châu Âu và sông Moskva.",
            "tips_vi": "Đến bằng metro tới ga Kievskaya (ba tuyến gặp nhau, các ga trang trí đẹp). Đây cũng là điểm khởi hành của nhiều tuyến tàu ngoại ô về hướng tây nam; chú ý an ninh và giữ vé/hành lý."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=37.5672,55.7431&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=55.7431,37.5672"
        },
        "official_site": None,
        "sources": [
            {"title": "Moscow Kiyevsky railway station — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Moscow_Kiyevsky_railway_station"},
            {"title": "The evolution of the Kievsky Railway Station — Moscow City (mos.ru)", "url": "https://www.mos.ru/en/news/item/18838073/"},
            {"title": "Kiev Station (Moscow, 1917) — Structurae", "url": "https://structurae.net/en/structures/kiev-station"}
        ],
        "tags": ["architecture", "railway-station", "shukhov", "neoclassical", "landmark", "early-20th-century"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-krasin-icebreaker",
        "slug": "krasin-icebreaker",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Tàu phá băng - bảo tàng Krasin",
        "name_ru": "Ледокол-музей «Красин»",
        "name_en": "Icebreaker Krasin (museum ship)",
        "categories": ["museum"],
        "coordinates": {"lat": 59.9278, "lon": 30.2689},
        "address_vi": "Kè Trung uý Schmidt (Naberezhnaya Leytenanta Shmidta), gần Đường số 23 (23-ya liniya), đảo Vasilievsky, Saint Petersburg",
        "rating": None,
        "review_summary_vi": """Du khách thích thú khi được lên một tàu phá băng thật, khám phá buồng lái, phòng máy và nghe câu chuyện cứu hộ Bắc Cực năm 1928 đầy kịch tính. Nhiều gia đình có trẻ nhỏ đánh giá đây là điểm tham quan hấp dẫn, khác lạ. Lưu ý: chủ yếu vào bên trong theo tour có hướng dẫn, một số suất bằng tiếng Nga; giờ mở cửa hạn chế trong tuần nên cần tra lịch trước.""",
        "presentation_short_vi": """Tàu phá băng huyền thoại nay là bảo tàng nổi trên đảo Vasilievsky, neo tại Kè Trung uý Schmidt. Đóng tại Anh trong các năm 1916–1917, con tàu nổi danh thế giới năm 1928 khi vượt băng Bắc Cực cứu những người sống sót của đoàn thám hiểm khinh khí cầu Italia.""",
        "presentation_long_vi": """Krasin là một trong những tàu phá băng nổi tiếng nhất lịch sử hàng hải Nga. Con tàu được đóng tại xưởng Armstrong Whitworth ở Newcastle (Anh) trong các năm 1916–1917 theo mẫu tàu phá băng Yermak trứ danh mà đô đốc Stepan Makarov khởi xướng, ban đầu mang tên 'Svyatogor'. Năm 1927, tàu được đổi tên thành 'Krasin' để tưởng nhớ nhà ngoại giao kiêm kỹ sư Xô-viết Leonid Krasin. Tên tuổi con tàu vang khắp thế giới vào năm 1928: khi khinh khí cầu Italia của tướng người Ý Umberto Nobile gặp nạn trên Bắc Băng Dương lúc trở về từ Bắc Cực, chính Krasin đã phá băng tiến tới và cứu được nhóm người sống sót; trên đường về, tàu còn hỗ trợ một tàu khách của Đức bị hư hại vì va vào băng. Trong nhiều thập niên sau đó, Krasin tiếp tục phục vụ ở Bắc Cực - dẫn dắt các đoàn tàu vận tải trên Tuyến đường biển phương Bắc và tham gia cả những nhiệm vụ thời Thế chiến II. Đến năm 1995, khu trưng bày bảo tàng đầu tiên được mở trên tàu; từ năm 2004, Krasin trở thành chi nhánh của Bảo tàng Đại dương Thế giới. Ngày nay du khách có thể lên tàu tham quan buồng lái, phòng máy, các khoang sinh hoạt của thủy thủ và tìm hiểu lịch sử chinh phục Bắc Cực của nước Nga - một trải nghiệm thú vị, thường đi kèm hướng dẫn viên.""",
        "highlights_vi": [
            "Tàu phá băng đóng tại Anh năm 1916–1917 (nguyên tên 'Svyatogor'), đổi tên thành 'Krasin' năm 1927 - biểu tượng của công cuộc chinh phục Bắc Cực.",
            "Năm 1928 nổi danh toàn cầu nhờ chiến dịch vượt băng cứu những người sống sót của đoàn thám hiểm khinh khí cầu Italia (tướng Umberto Nobile).",
            "Từ năm 2004 là tàu bảo tàng - chi nhánh của Bảo tàng Đại dương Thế giới, neo tại Kè Trung uý Schmidt trên đảo Vasilievsky."
        ],
        "practical": {
            "hours_vi": "Thường mở cửa tham quan từ Thứ Tư đến Chủ nhật, khoảng 11:00–18:00; đóng cửa Thứ Hai, Thứ Ba và ngày Thứ Tư cuối tháng. Nên kiểm tra lịch trước khi đến.",
            "ticket_vi": "Có vé vào tham quan với mức phí phải chăng; tham quan các khoang bên trong thường theo tour có hướng dẫn (có thể cần đăng ký trước, một số suất bằng tiếng Nga).",
            "duration_vi": "Khoảng 1–1,5 giờ.",
            "best_time_vi": "Ban ngày; mùa hè thời tiết thuận lợi cho việc đi bộ dọc kè và lên tàu.",
            "tips_vi": "Tàu neo ở khu vực Đường số 23, đảo Vasilievsky - đi bộ từ khu trung tâm đảo hoặc bắt xe tới Kè Trung uý Schmidt. Trẻ em thường rất thích buồng lái và phòng máy; nên mặc ấm vì trên tàu và ven sông khá lộng gió."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.2689,59.9278&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.9278,30.2689"
        },
        "official_site": "https://world-ocean.ru/",
        "sources": [
            {"title": "Krassin (1916 icebreaker) — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Krassin_(1916_icebreaker)"},
            {"title": "The Icebreaker Krasin Museum — Saint-Petersburg.com", "url": "http://www.saint-petersburg.com/museums/icebreaker-krasin/"},
            {"title": "Ledokol Krasin — Museum of the World Ocean", "url": "https://world-ocean.ru/"}
        ],
        "tags": ["museum", "ship", "icebreaker", "arctic", "history", "20th-century"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    }
]


def main():
    added, skipped = [], []
    by_region = {}
    for r in NEW:
        by_region.setdefault(r["region"], []).append(r)

    for region, recs in by_region.items():
        path = os.path.join(REGIONS, f"{region}.json")
        data = json.load(open(path, encoding="utf-8"))
        have = {p.get("slug") for p in data}
        bak = f"{path}.bak_add_{STAMP}"
        with open(bak, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        changed = False
        for r in recs:
            if r["slug"] in have:
                skipped.append(f"{region}/{r['slug']}")
                continue
            data.append(r)
            added.append(f"{region}/{r['slug']}")
            changed = True
        if changed:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"[OK] {region}.json -> {len(data)} ban ghi (backup: {os.path.basename(bak)})")
        else:
            os.remove(bak)

    print("DA THEM:", added or "(khong co)")
    print("BO QUA (da ton tai):", skipped or "(khong)")


if __name__ == "__main__":
    main()
