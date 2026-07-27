# -*- coding: utf-8 -*-
"""_add_three_places_r.py — Bổ sung 3 địa điểm nổi tiếng/hiện đại còn thiếu.
Nội dung tiếng Việt nguyên gốc (không sao chép/dịch nguyên văn), có ghi nguồn.
Chạy: python3 tools/_add_three_places_r.py  (rồi normalize_categories.py + build.py)
"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-26"

NEW = [
    {
        "id": "moscow-melnikov-house",
        "slug": "melnikov-house",
        "region": "moscow",
        "region_name_vi": "Moskva",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Nhà Melnikov (Dom Melnikova)",
        "name_ru": "Дом Мельникова",
        "name_en": "Melnikov House",
        "categories": ["museum", "monument"],
        "coordinates": {"lat": 55.748056, "lon": 37.589444},
        "address_vi": "Ngõ Krivoarbatsky, số 10, quận Arbat, Moskva",
        "rating": None,
        "presentation_short_vi": "Ngôi nhà hình hai trụ tròn lồng vào nhau với hàng chục ô cửa lục giác, do kiến trúc sư Konstantin Melnikov tự thiết kế cho gia đình mình cuối thập niên 1920. Đây là một trong những biểu tượng táo bạo nhất của kiến trúc tiên phong (avant-garde) Xô-viết, nay mở cửa làm bảo tàng theo tour đặt trước.",
        "presentation_long_vi": "Giữa những con ngõ yên tĩnh của khu Arbat cổ, một công trình kỳ lạ khiến người qua đường phải dừng bước: hai khối trụ tròn bằng gạch lồng vào nhau, thân nhà lấm tấm hơn sáu chục ô cửa hình lục giác như tổ ong. Đó là Nhà Melnikov, do kiến trúc sư Konstantin Melnikov dựng trong các năm 1927–1929 làm nơi ở kiêm xưởng sáng tác cho chính gia đình ông — một đặc ân hiếm có ở thời Liên Xô, khi nhà ở tư nhân gần như không còn. Melnikov khước từ mọi trường phái đương thời để theo đuổi lối kiến trúc của riêng mình: kết cấu tường tổ ong không cần cột chống, cho phép ông tùy ý bịt hay mở các ô cửa lục giác, tạo nên những căn phòng ngập ánh sáng mà không lãng phí vật liệu. Xưởng vẽ trên tầng cao với rừng cửa sổ là điểm nhấn được nhắc đến nhiều nhất. Sau nhiều thập niên xuống cấp và tranh chấp thừa kế, ngôi nhà trở thành bảo tàng tưởng niệm hai cha con Konstantin và Viktor Melnikov từ năm 2014, trực thuộc Bảo tàng Kiến trúc Shchusev. Vì không gian nhỏ và mong manh, khách chỉ vào thăm theo đoàn nhỏ đặt trước, giúp bảo tồn từng chi tiết gốc. Với giới yêu kiến trúc, đây là điểm hành hương gần như bắt buộc khi tới Moskva.",
        "highlights_vi": [
            "Xây năm 1927–1929, gồm hai trụ tròn lồng nhau với hơn 60 ô cửa lục giác; tường chịu lực kiểu 'tổ ong' không cần cột đỡ.",
            "Là căn nhà ở riêng hiếm hoi được phép xây thời Xô-viết, do KTS Konstantin Melnikov thiết kế cho chính gia đình mình.",
            "Từ năm 2014 là bảo tàng (chi nhánh Bảo tàng Kiến trúc Shchusev); chỉ đón khách theo tour nhỏ đặt trước để bảo tồn."
        ],
        "practical": {
            "hours_vi": "Chỉ tham quan theo tour có hướng dẫn, đặt trước: Thứ Ba–Thứ Bảy, thường 1 suất/ngày (khoảng 13:00), mỗi đoàn tối đa ~5 khách.",
            "ticket_vi": "Khoảng 1.500 RUB/khách; giảm còn ~1.000 RUB cho học sinh–sinh viên và người cao tuổi.",
            "duration_vi": "1,5–2 giờ.",
            "best_time_vi": "Đặt vé sớm nhiều tuần vì số chỗ mỗi suất rất ít.",
            "tips_vi": "Bắt buộc đặt tour trước qua Bảo tàng Kiến trúc Shchusev; không thể vào trong nếu tự đến. Ga metro gần nhất: Smolenskaya hoặc Arbatskaya."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=37.589444,55.748056&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=55.748056,37.589444"
        },
        "official_site": "https://muar.ru",
        "sources": [
            {"title": "Melnikov House — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Melnikov_House"},
            {"title": "For Visitors of the Melnikov House — Shchusev Museum of Architecture (MUAR)", "url": "http://muar.ru/en/for-visitors-of-the-melnikov-house"},
            {"title": "Melnikov House — Iconic Houses", "url": "https://www.iconichouses.org/houses/melnikov-house"}
        ],
        "tags": ["architecture", "avant-garde", "constructivism", "museum", "landmark", "top"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "moscow-narkomfin-building",
        "slug": "narkomfin-building",
        "region": "moscow",
        "region_name_vi": "Moskva",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Nhà Narkomfin (Dom Narkomfina)",
        "name_ru": "Дом Наркомфина",
        "name_en": "Narkomfin Building",
        "categories": ["monument", "museum"],
        "coordinates": {"lat": 55.7543, "lon": 37.5753},
        "address_vi": "Đại lộ Novinsky, số 25, quận Presnensky, Moskva",
        "rating": None,
        "presentation_short_vi": "Chung cư 'công xã' mang tính thử nghiệm do Moisei Ginzburg thiết kế đầu thập niên 1930 — biểu tượng của kiến trúc Kiến tạo (Constructivism) và ý tưởng sống tập thể kiểu Xô-viết. Sau đợt trùng tu công phu hoàn tất năm 2020, tòa nhà hồi sinh và mở khu trưng bày về chính lịch sử của mình.",
        "presentation_long_vi": "Nằm bên Vành đai Vườn, Nhà Narkomfin trông khiêm nhường nhưng lại là một trong những công trình có ảnh hưởng lớn nhất của kiến trúc hiện đại thế kỷ 20. Do kiến trúc sư Moisei Ginzburg cùng Ignaty Milinis thiết kế năm 1928 và hoàn thành năm 1932, tòa nhà được dựng cho cán bộ Bộ Tài chính Nhân dân (viết tắt là Narkomfin) như một 'cỗ máy để sống tập thể': khối căn hộ dài đặt trên hàng cột piloti, nối bằng hành lang trên cao sang khối dịch vụ chung gồm bếp tập thể, nhà trẻ, phòng đọc và khu thể chất. Ý tưởng là giải phóng con người — đặc biệt là phụ nữ — khỏi gánh nặng việc nhà, biến kiến trúc thành 'chất xúc tác xã hội'. Các căn hộ hai tầng thông minh (kiểu 'ô K' và 'ô F') về sau truyền cảm hứng trực tiếp cho Le Corbusier khi ông thiết kế khu Unité d'Habitation ở Marseille. Từng bị bỏ hoang và xuống cấp tới mức lọt vào danh sách di sản nguy cấp của thế giới, tòa nhà được cháu nội của Ginzburg là Alexei chủ trì trùng tu và mở cửa trở lại ngày 9/7/2020, khôi phục gần như nguyên trạng thiết kế gốc. Ngày nay phần lớn căn hộ là nhà ở tư nhân, nhưng khu sảnh có trưng bày nhỏ về lịch sử và quá trình phục dựng; du khách yêu kiến trúc có thể ngắm ngoại thất hoặc tham gia các tour chuyên đề.",
        "highlights_vi": [
            "Thiết kế bởi Moisei Ginzburg và Ignaty Milinis (1928), hoàn thành 1932 — kiệt tác nhà ở của phong trào Kiến tạo Xô-viết.",
            "Mô hình căn hộ hai tầng và ý tưởng 'nhà công xã' đã ảnh hưởng tới Le Corbusier (Unité d'Habitation) và nhiều KTS hiện đại.",
            "Từng nằm trong danh sách di sản nguy cấp; được trùng tu và mở cửa lại ngày 9/7/2020 dưới sự dẫn dắt của cháu nội KTS."
        ],
        "practical": {
            "hours_vi": "Phần lớn là căn hộ tư nhân — có thể ngắm ngoại thất tự do; khu trưng bày ở sảnh và các tour chuyên đề mở theo lịch, nên đặt trước.",
            "ticket_vi": "Ngắm bên ngoài miễn phí; tour có hướng dẫn thu phí tùy đơn vị tổ chức.",
            "duration_vi": "30–60 phút (ngắm ngoài); ~1,5 giờ nếu đi tour.",
            "best_time_vi": "Ban ngày để thấy rõ khối nhà trên cột piloti và dải cửa băng ngang đặc trưng.",
            "tips_vi": "Tôn trọng sự riêng tư của cư dân; không tự ý vào các tầng ở. Nằm cạnh Vành đai Vườn, gần khu Đại sứ quán Mỹ, dễ kết hợp dạo phố Novinsky."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=37.5753,55.7543&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=55.7543,37.5753"
        },
        "official_site": "https://narkomfin.ru",
        "sources": [
            {"title": "Narkomfin building — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Narkomfin_building"},
            {"title": "Restoration of Narkomfin Building — Moscow City official site (mos.ru)", "url": "https://www.mos.ru/en/news/item/109794073/"},
            {"title": "The Narkomfin Building — dự án phục dựng chính thức", "url": "https://narkomfin.ru/en/history"}
        ],
        "tags": ["architecture", "constructivism", "avant-garde", "modern", "landmark"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-stieglitz-museum",
        "slug": "stieglitz-museum",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Bảo tàng Nghệ thuật Ứng dụng Stieglitz",
        "name_ru": "Музей прикладного искусства Академии имени А. Л. Штиглица",
        "name_en": "Stieglitz Museum of Applied Arts",
        "categories": ["museum"],
        "coordinates": {"lat": 59.9437, "lon": 30.3389},
        "address_vi": "Ngõ Solyanoy, số 13–15, Saint Petersburg",
        "rating": None,
        "presentation_short_vi": "Bảo tàng nghệ thuật ứng dụng nằm trong Học viện Mỹ thuật Stieglitz, nổi tiếng nhờ dãy sảnh nội thất lộng lẫy mô phỏng cung điện Ý thời Phục Hưng và điện Terem Nga. Kho hiện vật hơn 30.000 món trải từ gốm sứ, đồ gỗ tới lò sưởi ốp gạch men — một 'viên ngọc giấu kín' của Saint Petersburg.",
        "presentation_long_vi": "Được nhà tài phiệt kiêm nhà từ thiện, Nam tước Alexander von Stieglitz, sáng lập năm 1876 để phục vụ trường dạy nghề mỹ thuật của ông, bảo tàng này là nơi bao thế hệ nghệ nhân Nga tới học hỏi tinh hoa nghề thủ công thế giới. Tòa nhà hiện nay do kiến trúc sư Maximilian Messmacher thiết kế, xây trong các năm 1885–1896 theo phong cách Tân Phục Hưng; nhưng điều khiến du khách sững sờ lại nằm ở bên trong: mỗi gian sảnh được tạo tác theo một phong cách và thời kỳ riêng để 'hòa nhịp' với hiện vật trưng bày. Trung tâm là đại sảnh phủ mái kính khổng lồ, viền quanh bởi hai tầng hành lang kiểu Ý; nổi bật nhất là căn phòng phỏng theo điện Terem của các Sa hoàng, rực rỡ như một hộp trang sức. Bộ sưu tập gồm hơn ba mươi nghìn hiện vật — sứ châu Âu, gốm phương Đông, đồ gỗ thế kỷ 16–19, lò sưởi ốp gạch men Nga thế kỷ 18, đồ kim khí và dệt may nghệ thuật. Sau Cách mạng 1917, nhiều báu vật được chuyển sang bảo tàng Hermitage và nội thất từng bị bỏ bê — thậm chí có sảnh bị biến thành phòng tập thể dục; công cuộc phục dựng bền bỉ chỉ bắt đầu sau khi Liên Xô tan rã. Ngày nay đây vẫn là bảo tàng của học viện, nơi sinh viên chép mẫu ngay giữa các kiệt tác.",
        "highlights_vi": [
            "Do Nam tước Alexander von Stieglitz sáng lập năm 1876; tòa nhà xây 1885–1896 do KTS Maximilian Messmacher thiết kế.",
            "Mỗi gian sảnh trang trí theo một phong cách riêng; đại sảnh mái kính và phòng kiểu điện Terem là điểm nhấn không thể bỏ lỡ.",
            "Kho hơn 30.000 hiện vật mỹ thuật ứng dụng; thuộc Học viện Mỹ thuật Stieglitz (thời Xô-viết từng mang tên Mukhina)."
        ],
        "practical": {
            "hours_vi": "Thường mở Thứ Ba–Thứ Bảy, khoảng 11:00–17:00; nên kiểm tra lịch vì khách vào theo suất/đoàn.",
            "ticket_vi": "Khoảng 300–400 RUB; thường tham quan kèm hướng dẫn.",
            "duration_vi": "1–1,5 giờ.",
            "best_time_vi": "Giữa tuần, ban ngày để tận dụng ánh sáng qua mái kính.",
            "tips_vi": "Vào qua cổng chính của Học viện (ngõ Solyanoy); nên đặt suất trước vì bảo tàng vẫn phục vụ việc dạy học. Gần Vườn Mùa Hè và sông Fontanka."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.3389,59.9437&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.9437,30.3389"
        },
        "official_site": "https://www.ghpa.ru",
        "sources": [
            {"title": "Stieglitz Museum of Applied Arts — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Stieglitz_Museum_of_Applied_Arts"},
            {"title": "Museum — Stieglitz State Academy of Art and Design (ghpa.ru)", "url": "https://www.ghpa.ru/en/museum"},
            {"title": "The Applied Art Museum in St. Petersburg — Saint-Petersburg.com", "url": "http://www.saint-petersburg.com/museums/applied-art-museum/"}
        ],
        "tags": ["museum", "applied-art", "interior", "architecture", "hidden-gem"],
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
