# -*- coding: utf-8 -*-
"""_add_three_places_q.py — Bổ sung 3 địa điểm nổi tiếng còn thiếu (Moscow x1, SPB x2).
Nội dung tiếng Việt nguyên gốc, tọa độ thật, ghi nguồn. Chạy: python3 tools/_add_three_places_q.py"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-26"

NEW = [
    {
        "id": "moscow-bakhrushin-theatre-museum",
        "slug": "bakhrushin-theatre-museum",
        "region": "moscow",
        "region_name_vi": "Moskva",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Bảo tàng Sân khấu Trung ương mang tên A.A. Bakhrushin (Ba-khơ-ru-sin)",
        "name_ru": "Государственный центральный театральный музей имени А. А. Бахрушина",
        "name_en": "A.A. Bakhrushin State Central Theatre Museum",
        "categories": ["museum"],
        "coordinates": {"lat": 55.73167, "lon": 37.63778},
        "address_vi": "Phố Bakhrushina, số 31/12 (ulitsa Bakhrushina, 31/12), quận Zamoskvorechye, Moskva; gần ga tàu điện ngầm Paveletskaya.",
        "rating": None,
        "review_summary_vi": "Khách yêu sân khấu đánh giá đây là 'thánh địa' của nghệ thuật biểu diễn Nga: kho hiện vật đồ sộ từ trang phục, đạo cụ tới phác thảo phông cảnh và di vật của các nghệ sĩ opera, ballet, kịch nói lừng danh, đặt trong một dinh thự cổ rất có không khí. Điểm nên lưu ý: dinh thự lịch sử vừa trải qua đợt trùng tu – mở rộng lớn, nên nội dung trưng bày và cơ sở mở cửa có thể thay đổi; hãy xem lịch trên trang chính thức trước khi đến.",
        "presentation_short_vi": "Bảo tàng sân khấu đầu tiên của nước Nga và được đánh giá là bảo tàng sân khấu lớn nhất thế giới, do nhà buôn – nhà sưu tầm Alexey Bakhrushin sáng lập năm 1894. Bảo tàng đặt trong dinh thự phong cách Tân Gothic của chính người sáng lập, lưu giữ hơn 1,5 triệu hiện vật kể lại lịch sử nghệ thuật sân khấu Nga.",
        "presentation_long_vi": "Năm 1894, nhà buôn giàu có và say mê nghệ thuật Alexey Alexandrovich Bakhrushin bắt đầu sưu tầm những kỷ vật gắn với sân khấu Nga; ngày 29 tháng 10 năm ấy, khi lần đầu bày bộ sưu tập cho công chúng xem, được coi là ngày khai sinh bảo tàng. Đây là bảo tàng sân khấu đầu tiên ở Nga và là một trong những bảo tàng sân khấu ra đời sớm nhất thế giới; về sau bộ sưu tập lớn tới mức được xem là bảo tàng sân khấu lớn nhất thế giới. Từ năm 1896, bộ sưu tập được đặt trong dinh thự riêng của gia đình Bakhrushin trên con phố nay mang chính tên ông — một công trình duyên dáng theo phong cách Tân Gothic (Anh) do kiến trúc sư Karl Gippius thiết kế. Hơn 1,5 triệu hiện vật ở đây trải khắp các loại hình: trang phục và đạo cụ biểu diễn, phác thảo phông cảnh và phục trang, áp phích, chương trình diễn, thư từ, ảnh chụp, chân dung và di vật cá nhân của các nghệ sĩ opera, ballet, kịch nói. Ngày nay Bảo tàng Bakhrushin còn là 'đầu tàu' của cả một mạng lưới bảo tàng – nhà lưu niệm sân khấu ở Moskva. Dinh thự lịch sử vừa trải qua đợt trùng tu – mở rộng quy mô lớn thành một 'Khu phố Sân khấu', vì vậy du khách nên kiểm tra trước lịch mở cửa và các cơ sở đang hoạt động. Bảo tàng nằm chỉ vài phút đi bộ từ ga tàu điện ngầm Paveletskaya.",
        "highlights_vi": [
            "Bảo tàng sân khấu đầu tiên của nước Nga, khai sinh ngày 29/10/1894 từ bộ sưu tập của nhà buôn Alexey Bakhrushin; được đánh giá là bảo tàng sân khấu lớn nhất thế giới.",
            "Trụ sở là dinh thự Tân Gothic do kiến trúc sư Karl Gippius xây năm 1896 cho gia đình Bakhrushin, nay là di tích kiến trúc trên phố Bakhrushina gần ga Paveletskaya.",
            "Hơn 1,5 triệu hiện vật: trang phục, đạo cụ, phác thảo phông cảnh – phục trang, áp phích, ảnh và di vật của các nghệ sĩ opera, ballet, kịch nói."
        ],
        "practical": {
            "hours_vi": "Thường mở cửa gần như cả tuần, nghỉ một ngày đầu tuần; do dinh thự lịch sử vừa trải qua trùng tu lớn, nên kiểm tra giờ mở và cơ sở đang hoạt động trên trang chính thức trước khi đến.",
            "ticket_vi": "Có bán vé vào cửa và vé triển lãm chuyên đề; ưu đãi cho học sinh, sinh viên, người cao tuổi. Giá thay đổi theo chương trình.",
            "duration_vi": "Khoảng 1,5–2 giờ.",
            "best_time_vi": "Ngày thường buổi sáng ít đông.",
            "tips_vi": "Đi bộ ít phút từ ga metro Paveletskaya; dễ kết hợp dạo khu Zamoskvorechye và ghé Phòng tranh Tretyakov gần đó."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=37.63778,55.73167&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=55.73167,37.63778"
        },
        "official_site": "https://bakhrushinmuseum.ru",
        "sources": [
            {"title": "Bakhrushin Museum — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Bakhrushin_Museum"},
            {"title": "Trang chính thức Bảo tàng Bakhrushin", "url": "https://www.bakhrushinmuseum.ru/en/museum-en/"}
        ],
        "tags": ["museum", "theatre", "history", "indoor", "culture"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-narva-triumphal-gate",
        "slug": "narva-triumphal-gate",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Khải Hoàn Môn Narva (Narvskiye Triumfalnye Vorota)",
        "name_ru": "Нарвские триумфальные ворота",
        "name_en": "Narva Triumphal Gate",
        "categories": ["monument"],
        "coordinates": {"lat": 59.90084, "lon": 30.27382},
        "address_vi": "Quảng trường Stachek (Ploshchad Stachek), quận Kirovsky, Saint Petersburg; ngay cạnh ga tàu điện ngầm Narvskaya.",
        "rating": None,
        "review_summary_vi": "Du khách ấn tượng với quy mô bề thế của cổng khải hoàn và cỗ chiến xa sáu ngựa bằng đồng trên đỉnh, xem đây là một trong những tượng đài chiến thắng đáng nhớ nhất thành phố. Nhiều người thấy tiện vì cổng nằm ngay cửa ga metro Narvskaya. Điểm lưu ý: công trình đứng giữa quảng trường nhiều xe cộ, cần chú ý an toàn khi băng đường để tới gần và chụp ảnh.",
        "presentation_short_vi": "Cổng khải hoàn hoành tráng dựng để đón đoàn Cận vệ Nga chiến thắng trở về sau khi đánh bại Napoleon. Bản gỗ ban đầu (1814) của Giacomo Quarenghi được kiến trúc sư Vasily Stasov xây lại bằng gạch bọc đồng, khánh thành năm 1834; trên đỉnh là cỗ chiến xa sáu ngựa của Nữ thần Vinh Quang.",
        "presentation_long_vi": "Sau khi quân đội Nga đánh bại Napoleon và tiến vào Paris năm 1814, Saint Petersburg dựng vội một cổng khải hoàn bằng gỗ và vữa alabaster ở cửa ngõ tây nam thành phố — trên con đường đi Narva — để nghênh đón các trung đoàn Cận vệ khải hoàn. Thiết kế đầu tiên này thuộc về kiến trúc sư người Ý Giacomo Quarenghi. Theo thời gian, công trình gỗ xuống cấp, nên cuối thập niên 1820 kiến trúc sư Vasily Stasov được giao dựng lại một cổng mới bền vững hơn ở vị trí gần đó: khung gạch ốp những tấm đồng dập, vẫn giữ nguyên tinh thần bố cục của Quarenghi. Cổng mới được khánh thành ngày 17 (tức 30 theo lịch mới) tháng 8 năm 1834. Trên đỉnh vòm cao khoảng 30 mét là cỗ chiến xa của Nữ thần Vinh Quang do sáu con tuấn mã kéo, cùng những pho tượng chiến binh và thiên thần — tác phẩm của các nhà điêu khắc Pyotr Klodt, Vasily Demut-Malinovsky và Stepan Pimenov, tất cả đều gò từ đồng tấm. Cổng đứng sừng sững giữa Quảng trường Stachek (xưa gọi là Quảng trường Narva). Từ cuối thập niên 1980, tầng trên của cổng mở một bảo tàng nhỏ — nay là chi nhánh của Bảo tàng Điêu khắc Đô thị Nhà nước, kể lại lịch sử công trình và cuộc Chiến tranh Vệ quốc năm 1812. Cổng nằm ngay cạnh ga tàu điện ngầm Narvskaya, rất dễ ghé thăm.",
        "highlights_vi": [
            "Dựng để đón đoàn Cận vệ Nga chiến thắng trở về sau khi đánh bại Napoleon; bản gỗ đầu tiên (1814) do Giacomo Quarenghi thiết kế.",
            "Kiến trúc sư Vasily Stasov xây lại bằng gạch bọc đồng tấm, khánh thành năm 1834; trên đỉnh là cỗ chiến xa sáu ngựa của Nữ thần Vinh Quang (điêu khắc Pyotr Klodt cùng cộng sự).",
            "Cao khoảng 30 m, đứng giữa Quảng trường Stachek cạnh ga metro Narvskaya; tầng trên có bảo tàng nhỏ thuộc Bảo tàng Điêu khắc Đô thị."
        ],
        "practical": {
            "hours_vi": "Có thể ngắm cổng tự do ngoài trời mọi lúc. Bảo tàng nhỏ ở tầng trên có giờ mở riêng và thường nghỉ vài ngày trong tuần — nên xem lịch trước.",
            "ticket_vi": "Ngắm và chụp ảnh bên ngoài miễn phí; vào bảo tàng trên cổng thu phí nhỏ.",
            "duration_vi": "Khoảng 15–30 phút (thêm thời gian nếu vào bảo tàng).",
            "best_time_vi": "Ban ngày để thấy rõ chi tiết tượng đồng; lúc hoàng hôn cổng lên hình rất đẹp.",
            "tips_vi": "Xuống ga metro Narvskaya là tới ngay; cổng nằm giữa quảng trường có xe cộ đông, chú ý an toàn khi băng đường để chụp ảnh."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.27382,59.90084&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.90084,30.27382"
        },
        "official_site": None,
        "sources": [
            {"title": "Narva Triumphal Arch — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Narva_Triumphal_Arch"},
            {"title": "The Narva Gate — Saint-Petersburg.com", "url": "http://www.saint-petersburg.com/monuments/narva-gate.asp"}
        ],
        "tags": ["monument", "arch", "history", "1812", "outdoor", "free"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-lion-bridge",
        "slug": "lion-bridge",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Cầu Sư Tử (Lviny most — 'Cầu Bốn Sư Tử')",
        "name_ru": "Львиный мост",
        "name_en": "Lion Bridge (Bridge of Four Lions)",
        "categories": ["bridge"],
        "coordinates": {"lat": 59.92694, "lon": 30.30139},
        "address_vi": "Bắc qua kênh Griboedov, nối ngõ Lviny với phố Malaya Podyacheskaya, quận Admiralteysky, Saint Petersburg.",
        "rating": None,
        "review_summary_vi": "Du khách thích thú với bốn con sư tử trắng canh giữ cây cầu treo nhỏ xinh bên kênh Griboedov, xem đây là điểm chụp ảnh lãng mạn và thường ghé cùng cầu Ngân Hàng gần đó. Điểm lưu ý: cầu khá hẹp nên hay đông khách vào giờ cao điểm, cần nhường lối cho người qua lại.",
        "presentation_short_vi": "Cầu treo dành cho người đi bộ bắc qua kênh Griboedov, khánh thành năm 1826, nổi bật với bốn tượng sư tử gang sơn trắng. Hệ cáp treo đỡ mặt cầu được giấu khéo trong thân bốn con sư tử — cùng kỹ sư và nhà điêu khắc với cầu Ngân Hàng nổi tiếng gần đó.",
        "presentation_long_vi": "Nếu cầu Ngân Hàng nổi danh với bầy griffin mạ vàng thì 'người anh em' song sinh của nó — cầu Sư Tử (Lviny most) — lại được canh giữ bởi bốn con sư tử gang sơn trắng muốt như cẩm thạch. Đây là cây cầu treo cho người đi bộ dài khoảng 28 mét bắc qua kênh đào Griboedov, nối ngõ Lviny với phố Malaya Podyacheskaya. Cầu do kỹ sư Wilhelm von Traitteur thiết kế và được khánh thành ngày 1 tháng 7 năm 1826 — cùng thời và cùng ý tưởng với cầu Ngân Hàng: toàn bộ hệ dây cáp treo đỡ mặt cầu được giấu kín trong thân những pho tượng thú ở hai đầu, để dây xích 'chui ra' từ miệng sư tử. Bốn con sư tử là tác phẩm của nhà điêu khắc Pavel Sokolov — chính người đã tạc bầy griffin cho cầu Ngân Hàng — và được sơn màu trắng mờ để trông như tạc từ đá cẩm thạch. Cầu Sư Tử là một trong ba cây cầu treo dây xích dành cho người đi bộ còn sót lại của Saint Petersburg (cùng cầu Ngân Hàng và cầu Pochtamtsky). Danh tiếng của nó vượt khỏi biên giới nước Nga: năm 1838, một phiên bản thu nhỏ đã được dựng trong công viên Tiergarten ở Berlin. Trải qua nhiều lần trùng tu (gần đây nhất là phần tượng năm 2018), cây cầu vẫn là điểm dừng chân nên thơ dọc dòng kênh Griboedov.",
        "highlights_vi": [
            "Cầu treo cho người đi bộ dài khoảng 28 m bắc qua kênh Griboedov, khánh thành 1/7/1826; hệ cáp treo giấu trong thân bốn con sư tử, dây xích thoát ra từ miệng.",
            "Do kỹ sư Wilhelm von Traitteur thiết kế và nhà điêu khắc Pavel Sokolov tạc tượng — cùng bộ đôi tác giả với cầu Ngân Hàng gần đó; sư tử sơn trắng mờ giả cẩm thạch.",
            "Một trong ba cầu treo dây xích cho người đi bộ còn lại ở Saint Petersburg; một bản sao thu nhỏ được dựng ở công viên Tiergarten (Berlin) năm 1838."
        ],
        "practical": {
            "hours_vi": "Cầu đi bộ công cộng, mở cửa tự do 24/7.",
            "ticket_vi": "Miễn phí.",
            "duration_vi": "Khoảng 10–20 phút.",
            "best_time_vi": "Sáng sớm cho không gian yên tĩnh chụp ảnh, hoặc buổi tối khi cầu lên đèn.",
            "tips_vi": "Kết hợp đi dọc kênh Griboedov để ngắm luôn cầu Ngân Hàng (bốn griffin) cùng phong cách; cầu hẹp nên nhường lối khi đông khách."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.30139,59.92694&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.92694,30.30139"
        },
        "official_site": None,
        "sources": [
            {"title": "Bridge of Four Lions — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Bridge_of_Four_Lions"},
            {"title": "Lions Bridge — Saint-Petersburg.com", "url": "http://www.saint-petersburg.com/bridges/lions-bridge/"},
            {"title": "Lion Bridge — Mostotrest (EN)", "url": "https://en.mostotrest-spb.ru/bridges/lvinyj"}
        ],
        "tags": ["bridge", "sculpture", "lion", "free", "outdoor", "romantic"],
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
