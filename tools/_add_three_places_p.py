# -*- coding: utf-8 -*-
"""_add_three_places_p.py — Bổ sung 3 địa điểm nổi tiếng/hiện đại còn thiếu (Moscow x1, SPB x2).
Nội dung tiếng Việt nguyên gốc, tọa độ thật, ghi nguồn. Chạy: python3 tools/_add_three_places_p.py"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-26"

NEW = [
    {
        "id": "moscow-losiny-ostrov",
        "slug": "losiny-ostrov",
        "region": "moscow",
        "region_name_vi": "Moskva",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Vườn Quốc gia Losiny Ostrov ('Đảo Nai Sừng Tấm')",
        "name_ru": "Национальный парк «Лосиный остров»",
        "name_en": "Losiny Ostrov National Park (Elk Island)",
        "categories": ["park_garden"],
        "coordinates": {"lat": 55.8636, "lon": 37.7775},
        "address_vi": "Rìa đông bắc Moskva, trải sang tỉnh Moskva; nhiều lối vào, trong đó có Trạm Sinh học Nai (Losinaya Biostantsiya) ở phía Mytishchi",
        "rating": {"value": None, "count": None, "source": "Tripadvisor", "as_of": "2026-07"},
        "review_summary_vi": "Du khách gọi đây là 'lá phổi xanh' khổng lồ ngay sát Moskva: không khí trong lành, rừng thông – bạch dương bạt ngàn, đường mòn đi bộ và đạp xe, cùng Trạm Sinh học Nai nơi có thể ngắm nai sừng tấm ở cự ly gần. Nhiều người khen cảm giác lạc vào rừng taiga dù chỉ cách trung tâm ít phút. Điểm lưu ý: công viên rất rộng và chia thành nhiều khu với các cổng vào tách biệt, một số khu khó tiếp cận, biển chỉ dẫn tiếng Anh hạn chế, và nhiều muỗi vào mùa hè.",
        "presentation_short_vi": "Mảng 'rừng taiga giữa lòng đô thị' — một trong những vườn quốc gia đầu tiên của nước Nga (1983) và là một trong các khu rừng lớn nhất nằm ngay trong ranh giới một siêu đô thị; nổi tiếng với Trạm Sinh học Nai cùng mạng lưới đường mòn, đồng cỏ và đầm lầy.",
        "presentation_long_vi": "Ngay sát nhịp sống hối hả của Moskva là một vùng rừng rộng lớn khiến người ta ngỡ đang ở sâu trong miền taiga phương Bắc — đó là Vườn Quốc gia Losiny Ostrov, dịch nôm na là 'Đảo Nai Sừng Tấm', đặt theo loài nai sừng tấm (còn gọi là hươu sừng tấm) vẫn sinh sống trong rừng. Vùng đất này từ xa xưa là khu săn bắn được canh giữ nghiêm ngặt của các đại công tước và Sa hoàng; được tuyên bố là khu vực bảo tồn từ năm 1799, có tổ chức quản lý rừng đầu tiên năm 1842, và ý tưởng lập vườn quốc gia đã được nêu từ năm 1909. Phải tới ngày 24 tháng 8 năm 1983, Losiny Ostrov mới chính thức trở thành vườn quốc gia — nằm trong nhóm những vườn quốc gia đầu tiên của nước Nga, cùng năm với Vườn Quốc gia Sochi. Với diện tích khoảng 116 km², trong đó chừng 83% là rừng, phần còn lại là đầm lầy, mặt nước và khu vui chơi nghỉ dưỡng, công viên trải rộng qua cả thành phố Moskva lẫn tỉnh Moskva, bị chia đôi bởi Đường vành đai Moskva (MKAD). Đây là ngôi nhà của khoảng 44 loài thú và chừng 170 loài chim; điểm hút khách nhất là Trạm Sinh học Nai (Losinaya Biostantsiya) hoạt động từ năm 1963, nơi du khách có thể quan sát nai sừng tấm, hươu và lợn rừng trong các khu bán hoang dã. Nhờ vị trí đặc biệt, công viên dễ tiếp cận bằng tàu điện ngầm và tàu ngoại ô, mở ra một trải nghiệm hiếm có: chỉ vài chục phút rời khỏi phố xá là đã có thể đi bộ đường dài, đạp xe, trượt tuyết mùa đông hay lặng ngắm thiên nhiên hoang dã ngay bên hông một đại đô thị hơn chục triệu dân.",
        "highlights_vi": [
            "Một trong những vườn quốc gia đầu tiên của nước Nga (chính thức 24/8/1983); diện tích khoảng 116 km², trong đó chừng 83% là rừng, trải qua cả Moskva và tỉnh Moskva, bị chia đôi bởi đường vành đai MKAD.",
            "Tên 'Đảo Nai Sừng Tấm' đặt theo loài nai sừng tấm sống trong rừng; công viên là nơi cư trú của khoảng 44 loài thú và 170 loài chim.",
            "Trạm Sinh học Nai (từ năm 1963) cho phép ngắm nai sừng tấm và hươu ở cự ly gần — vùng đất vốn là khu săn bắn của các Sa hoàng, được bảo tồn từ năm 1799."
        ],
        "practical": {
            "hours_vi": "Khu rừng công cộng có thể vào tự do; các tuyến đường sinh thái và Trạm Sinh học Nai có giờ mở riêng (thường ban ngày, một số điểm nghỉ thứ Hai) — nên xem trang chính thức trước khi đi.",
            "ticket_vi": "Vào khu rừng nhìn chung miễn phí; Trạm Sinh học Nai và các tuyến tham quan có hướng dẫn thu phí nhỏ.",
            "duration_vi": "2–4 giờ hoặc nửa ngày.",
            "best_time_vi": "Cuối xuân đến mùa thu để đi bộ/đạp xe; mùa đông cho trượt tuyết băng đồng; buổi sáng dễ gặp động vật.",
            "tips_vi": "Có thể đến bằng metro tới các ga sát rìa công viên rồi đi bộ vào; mang thuốc chống muỗi vào mùa hè; đi đúng đường mòn đã đánh dấu; nên đặt trước tour Trạm Sinh học Nai."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=37.7775,55.8636&z=13&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=55.8636,37.7775"
        },
        "official_site": "https://losinyiostrov.ru",
        "sources": [
            {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Losiny_Ostrov_National_Park"},
            {"title": "National Parks Association — Losiny Ostrov", "url": "https://nationalparksassociation.org/russia-national-parks/losiny-ostrov-national-park/"}
        ],
        "tags": ["park", "nature", "forest", "outdoor", "national-park", "wildlife", "free"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-loft-project-etagi",
        "slug": "loft-project-etagi",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Loft Project Etagi (Không gian sáng tạo 'Các Tầng Lầu')",
        "name_ru": "Лофт Проект Этажи",
        "name_en": "Loft Project Etagi",
        "categories": ["other"],
        "coordinates": {"lat": 59.9256, "lon": 30.3547},
        "address_vi": "Đại lộ Ligovsky 74 (Ligovsky prospekt, 74), quận Trung tâm, Saint Petersburg",
        "rating": {"value": None, "count": None, "source": "Tripadvisor", "as_of": "2026-07"},
        "review_summary_vi": "Giới trẻ và dân sáng tạo mê Etagi vì bầu không khí 'loft' công nghiệp chất chơi: các phòng tranh độc lập, quán cà phê lạ, cửa hàng đồ cũ – thiết kế, và nhất là sân thượng ngắm toàn cảnh mái nhà thành phố. Nơi đây còn có cả một hostel giá mềm. Điểm trừ thường gặp: sân thượng đôi khi thu phí hoặc phải xếp hàng, một vài góc đã cũ, và tổng thể thiên về không khí – trải nghiệm hơn là triển lãm nghệ thuật tầm cỡ.",
        "presentation_short_vi": "Khu sáng tạo tiên phong nằm trong một nhà máy bánh mì thời Xô-viết cũ trên Đại lộ Ligovsky — năm tầng lầu (nên có tên 'Etagi', nghĩa là 'Các Tầng Lầu') gồm phòng tranh, cửa hàng thiết kế, quán cà phê, hostel và một sân thượng ngắm nhìn biển mái nhà Saint Petersburg.",
        "presentation_long_vi": "Giữa một Saint Petersburg lộng lẫy với cung điện và nhà thờ cổ kính, Loft Project Etagi mang đến gương mặt hoàn toàn khác: trẻ trung, phá cách và rất 'đương đại'. Mở cửa năm 2007 trong toà nhà của Nhà máy bánh mì Smolninsky cũ trên Đại lộ Ligovsky, đây là một trong những không gian kiểu 'loft' đầu tiên ở nước Nga — mô hình biến nhà xưởng công nghiệp bỏ hoang thành tổ hợp văn hoá – sáng tạo. Cái tên 'Etagi' (Các Tầng Lầu) xuất phát từ chính năm tầng của toà nhà, mỗi tầng được cải tạo thành phòng triển lãm, gallery nghệ thuật đương đại, showroom thiết kế, cửa hàng đồ cũ và thời trang độc lập, xen kẽ những quán cà phê và không gian nghỉ chân đậm chất bohemian. Điểm được nhắc tới nhiều nhất là sân thượng — một đài ngắm cảnh (đặc biệt nhộn nhịp vào mùa hè) nơi du khách nhâm nhi cà phê và phóng tầm mắt qua những mái nhà, ống khói và đường chân trời của thành phố. Nằm ngay gần ga metro Ligovsky Prospekt và ga xe lửa Moskovsky, Etagi đã trở thành biểu tượng cho một Saint Petersburg hiện đại, giàu chất nghệ và luôn chuyển động — điểm hẹn lý tưởng cho ai muốn cảm nhận nhịp sống sáng tạo bên cạnh vẻ đẹp cổ điển của cố đô.",
        "highlights_vi": [
            "Mở cửa năm 2007 trong Nhà máy bánh mì Smolninsky cũ — một trong những không gian 'loft'/sáng tạo đầu tiên của nước Nga; tên 'Etagi' (Các Tầng Lầu) lấy từ năm tầng được cải tạo.",
            "Tổ hợp gồm phòng tranh nghệ thuật đương đại, cửa hàng thiết kế – đồ cũ, quán cà phê và hostel; sân thượng là đài ngắm toàn cảnh mái nhà thành phố.",
            "Nằm sát ga metro Ligovsky Prospekt và ga xe lửa Moskovsky — gương mặt của một Saint Petersburg trẻ trung, phá cách và hiện đại."
        ],
        "practical": {
            "hours_vi": "Tổ hợp thường mở cửa hằng ngày từ gần trưa tới tối; mỗi gallery, cửa hàng và sân thượng có giờ riêng, sân thượng đặc biệt đông vào mùa hè — nên xem lịch trước.",
            "ticket_vi": "Vào tổ hợp miễn phí; một số triển lãm và đài ngắm cảnh trên sân thượng thu phí nhỏ.",
            "duration_vi": "1–2 giờ.",
            "best_time_vi": "Buổi chiều đến tối; mùa hè để lên sân thượng ngắm cảnh.",
            "tips_vi": "Gần ga metro Ligovsky Prospekt và ga Moskovsky; có thể kết hợp dạo Đại lộ Nevsky gần đó; hợp để uống cà phê, mua đồ lưu niệm và ngắm phố."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.3547,59.9256&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.9256,30.3547"
        },
        "official_site": None,
        "sources": [
            {"title": "saint-petersburg.com — Loft Project Etagi", "url": "http://www.saint-petersburg.com/museums/loft-project-etagi/"},
            {"title": "Lonely Planet — Loft Project Etagi", "url": "https://www.lonelyplanet.com/russia/st-petersburg/attractions/loft-project-etagi/a/poi-sig/1474220/360547"}
        ],
        "tags": ["creative-space", "modern", "art", "rooftop", "viewpoint", "cafe", "youth"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-bolshoy-obukhovsky-bridge",
        "slug": "bolshoy-obukhovsky-bridge",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Cầu Lớn Obukhovsky (Cầu dây văng 'Vantovy')",
        "name_ru": "Большой Обуховский мост (Вантовый мост)",
        "name_en": "Bolshoy Obukhovsky Bridge",
        "categories": ["bridge"],
        "coordinates": {"lat": 59.8500, "lon": 30.4597},
        "address_vi": "Bắc qua sông Neva, nối Đại lộ Obukhovskoy Oborony với Bờ kè Oktyabrskaya, quận Nevsky, Saint Petersburg",
        "rating": {"value": None, "count": None, "source": "Tripadvisor", "as_of": "2026-07"},
        "review_summary_vi": "Người dân và những ai mê cầu đường ấn tượng vì đây là cây cầu DUY NHẤT bắc qua sông Neva không phải cầu quay — một công trình dây văng hiện đại có thể qua lại 24/7 mà không phải chờ nâng nhịp. Là một phần của Đường vành đai, cầu đẹp nhất khi ngắm từ xa hoặc lúc chạy xe qua; không phải nơi đi bộ dạo cảnh nên phần lớn du khách chỉ ngắm thoáng qua.",
        "presentation_short_vi": "Cây cầu duy nhất bắc qua sông Neva KHÔNG phải cầu quay — công trình dây văng ('Vantovy') hiện đại với nhịp chính 382 m, đủ cao cho tàu thuyền qua bên dưới, cho phép giao thông sang sông suốt ngày đêm như một mắt xích của Đường vành đai Saint Petersburg.",
        "presentation_long_vi": "Ở một thành phố nổi danh với những cây cầu quay mở nhịp về đêm — vốn chia cắt đôi bờ khi các cầu trung tâm đồng loạt nâng lên cho tàu qua — thì Cầu Lớn Obukhovsky là ngoại lệ đặc biệt: cây cầu duy nhất vượt sông Neva mà không cần mở nhịp. Đây là một cầu dây văng, trong tiếng Nga gọi là 'Vantovy Most' (cầu dây văng), với mặt cầu được treo trên những trụ tháp cao; nhờ tĩnh không lớn, tàu thuyền có thể luồn qua bên dưới mà cầu không bao giờ phải nâng lên. Thực chất công trình gồm hai cây cầu song song giống hệt nhau, mỗi cầu gánh một chiều xe, được khánh thành theo hai giai đoạn: cầu thứ nhất ngày 15 tháng 12 năm 2004 và cầu thứ hai ngày 19 tháng 10 năm 2007. Với nhịp chính dài 382 m, đây là cây cầu có nhịp lớn nhất Saint Petersburg. Cầu nối Đại lộ Obukhovskoy Oborony với Bờ kè Oktyabrskaya ở quận Nevsky, thuộc tuyến Đường vành đai KAD bao quanh thành phố — vừa giúp giảm tải giao thông, vừa quan trọng ở chỗ cho phép người dân sang sông vào bất kỳ giờ nào, kể cả lúc nửa đêm khi những cây cầu quay lộng lẫy nơi trung tâm đang mở nhịp. Là một biểu tượng kỹ thuật đương đại, cầu tạo nên thế đối trọng thú vị với vẻ cổ kính của các cầu lịch sử vùng lõi đô thị.",
        "highlights_vi": [
            "Cây cầu DUY NHẤT bắc qua sông Neva không phải cầu quay: nhờ tĩnh không cao cho tàu thuyền qua lại, giao thông có thể sang sông mọi lúc, kể cả ban đêm.",
            "Cầu dây văng ('Vantovy Most') với nhịp chính 382 m — nhịp cầu lớn nhất Saint Petersburg; thực chất gồm hai cây cầu song song cho hai chiều xe.",
            "Khánh thành hai giai đoạn: cầu thứ nhất 15/12/2004, cầu thứ hai 19/10/2007; là một phần của Đường vành đai KAD, nối Đại lộ Obukhovskoy Oborony với Bờ kè Oktyabrskaya."
        ],
        "practical": {
            "hours_vi": "Cầu giao thông, qua lại tự do 24/7; không nâng nhịp nên không có 'giờ mở cầu' như các cầu quay ở trung tâm.",
            "ticket_vi": "Miễn phí (đường công cộng).",
            "duration_vi": "Ngắm hoặc qua cầu khoảng 10–20 phút.",
            "best_time_vi": "Hoàng hôn hoặc buổi tối khi cầu lên đèn; ngắm đẹp từ bờ kè hoặc khi đi trên Đường vành đai.",
            "tips_vi": "Nằm xa trung tâm (quận Nevsky, phía rìa thành phố), tiện nhất khi di chuyển bằng ô tô trên tuyến KAD; không phải điểm đi bộ ngắm cảnh như các cầu ở lõi đô thị."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.4597,59.8500&z=15&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.8500,30.4597"
        },
        "official_site": None,
        "sources": [
            {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Bolshoy_Obukhovsky_Bridge"}
        ],
        "tags": ["bridge", "modern", "engineering", "neva", "cable-stayed", "landmark", "kad"],
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
