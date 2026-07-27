# -*- coding: utf-8 -*-
"""_add_three_places_i.py — Bổ sung 3 địa điểm nổi tiếng còn thiếu (lần chạy tự động 2026-07-25, đợt i).

Thêm:
  1) Moskva            — Cầu Krym (Krymsky Most) — cây cầu treo dây xích duy nhất của Moskva.
  2) Moskva            — Nhà hát Múa rối Trung ương Obraztsov — nhà hát rối lớn nhất thế giới, đồng hồ mặt tiền trứ danh.
  3) Saint Petersburg  — Lyceum Hoàng gia Tsarskoye Selo — nơi Pushkin theo học, nay là bảo tàng-tưởng niệm.

Nội dung tiếng Việt nguyên gốc (không dịch/sao chép nguyên văn). Toạ độ thật đã kiểm chứng.
Chạy:  python3 tools/_add_three_places_i.py
"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TODAY = "2026-07-25"
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def maps_for(lat, lon):
    return {
        "yandex": f"https://yandex.com/maps/?pt={lon},{lat}&z=17&l=map",
        "google": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
    }


KRYMSKY_BRIDGE = {
    "id": "moscow-krymsky-bridge",
    "slug": "krymsky-bridge",
    "region": "moscow",
    "region_name_vi": "Moskva",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Cầu Krym (Krymsky Most — 'Cầu Crưm')",
    "name_ru": "Крымский мост",
    "name_en": "Krymsky Bridge (Crimean Bridge)",
    "categories": ["bridge"],
    "coordinates": {"lat": 55.73389, "lon": 37.59889},
    "address_vi": "Bắc qua sông Moskva, đưa Vành đai Vườn (Sadovoye Koltso) sang sông, nối Công viên Gorky với công viên điêu khắc Muzeon và Phòng tranh Tretyakov Mới; gần ga tàu điện ngầm Park Kultury.",
    "rating": None,
    "review_summary_vi": "Khách bộ hành khen đây là điểm dạo mát và chụp ảnh thú vị bắc ngang sông Moskva, thuận tiện nối Công viên Gorky với công viên điêu khắc Muzeon và Phòng tranh Tretyakov Mới; dáng cáp thép cong mềm mại được nhắc tới nhiều. Nhược điểm là cầu nằm trên Vành đai Vườn đông xe nên khá ồn và lộng gió.",
    "presentation_short_vi": "Cây cầu treo (dây xích) duy nhất của Moskva, khánh thành năm 1938, đưa Vành đai Vườn qua sông Moskva. Nhịp chính dài 168 m với hai tháp thép đứng độc lập, nối Công viên Gorky ở bờ này với công viên tượng Muzeon và Phòng tranh Tretyakov Mới ở bờ kia.",
    "presentation_long_vi": "Nằm cách Điện Kremlin khoảng 1,8 km về phía tây nam, Cầu Krym là cây cầu treo duy nhất ở Moskva và là một trong những công trình kỹ thuật được yêu thích của thành phố. Cây cầu hiện nay khánh thành ngày 1 tháng 5 năm 1938, trong đợt cải tạo lớn trung tâm Moskva thời kỳ ấy, do kỹ sư B. P. Konstantinov phụ trách phần kết cấu và kiến trúc sư A. V. Vlasov lo phần tạo hình. Đây đã là cây cầu thứ tư dựng tại vị trí này; chiếc đầu tiên là một cầu phao bằng gỗ có từ năm 1786. Tên gọi 'Krym' (Krymsky) bắt nguồn từ khu 'Sân Krym' xa xưa bên bờ sông — nơi từng tiếp đón phái đoàn của Hãn quốc Krym — chứ không liên quan tới bán đảo theo nghĩa hiện đại. Điểm đặc biệt về kết cấu nằm ở chỗ: hai tháp thép đứng độc lập, không nối với nhau ở phía trên; những sợi xích thép bản lớn vắt qua đỉnh tháp rồi neo xuống hai mố cầu, đỡ lấy mặt cầu treo bên dưới — một giải pháp hiếm gặp tạo nên dáng vẻ thanh thoát đặc trưng. Cầu dài khoảng 668 m tính cả đường dẫn (riêng phần cầu chính khoảng 262,5 m), rộng 38,4 m với sáu làn xe và hai lối đi bộ rộng hai bên. Đứng trên cầu, du khách có tầm nhìn thoáng ra mặt sông Moskva, Công viên Gorky, tượng đài Pyotr Đại đế của điêu khắc gia Tsereteli và những mái vòm phía xa. Buổi tối, hệ thống chiếu sáng nghệ thuật làm nổi bật đường cong của cáp thép, biến cây cầu thành điểm ngắm cảnh và chụp ảnh quen thuộc của người Moskva.",
    "highlights_vi": [
        "Cây cầu treo (dây xích) duy nhất ở Moskva, khánh thành ngày 1/5/1938.",
        "Hai tháp thép đứng độc lập, xích thép vắt qua đỉnh tháp rồi neo xuống mố — giải pháp kết cấu hiếm gặp; nhịp chính 168 m.",
        "Nối Công viên Gorky với công viên điêu khắc Muzeon và Phòng tranh Tretyakov Mới, đẹp nhất khi lên đèn buổi tối.",
    ],
    "practical": {
        "hours_vi": "Mở cửa 24/7 (cầu giao thông công cộng, có lối đi bộ hai bên).",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–30 phút để tản bộ và ngắm cảnh.",
        "best_time_vi": "Chiều muộn và buổi tối khi cầu lên đèn; kết hợp dạo Công viên Gorky và Muzeon.",
        "tips_vi": "Từ ga tàu điện ngầm Park Kultury đi bộ vài phút là tới; có thể sang bờ đối diện thăm Muzeon và Phòng tranh Tretyakov Mới.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(55.73389, 37.59889),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Krymsky_Bridge"},
        {"title": "Structurae", "url": "https://structurae.net/en/structures/krymsky-bridge"},
    ],
    "tags": ["bridge", "outdoor", "free", "landmark"],
    "status": "enriched",
    "last_updated": TODAY,
}


OBRAZTSOV = {
    "id": "moscow-obraztsov-puppet-theatre",
    "slug": "obraztsov-puppet-theatre",
    "region": "moscow",
    "region_name_vi": "Moskva",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Nhà hát Múa rối Trung ương mang tên S.V. Obraztsov (Teatr Kukol imeni Obraztsova, Ô-brát-xốp)",
    "name_ru": "Государственный академический центральный театр кукол имени С. В. Образцова",
    "name_en": "Sergey Obraztsov State Academic Central Puppet Theatre",
    "categories": ["theatre"],
    "coordinates": {"lat": 55.77722, "lon": 37.61083},
    "address_vi": "Phố Sadovaya-Samotyochnaya, số 3, Moskva (trên Vành đai Vườn); gần ga tàu điện ngầm Tsvetnoy Bulvar, Dostoevskaya và Mayakovskaya.",
    "rating": None,
    "review_summary_vi": "Phụ huynh và du khách yêu thích đây là điểm đến ấm áp cho cả gia đình: các vở rối dàn dựng công phu, hấp dẫn cả trẻ em lẫn người lớn, cộng thêm bảo tàng rối phong phú ngay trong toà nhà. Ai cũng nhắc tới chiếc đồng hồ trên mặt tiền — nên canh giờ chẵn để xem các nhân vật cổ tích lần lượt xuất hiện. Lưu ý nên đặt vé trước vì suất diễn hay kín chỗ.",
    "presentation_short_vi": "Nhà hát múa rối lớn nhất thế giới, thành lập năm 1931 bởi nghệ sĩ bậc thầy Sergei Obraztsov. Toà nhà trên Vành đai Vườn nổi tiếng với chiếc đồng hồ cơ khí độc đáo ngoài mặt tiền và một bảo tàng rối tầm cỡ quốc tế bên trong.",
    "presentation_long_vi": "Thành lập ngày 16 tháng 9 năm 1931 và gắn liền với tên tuổi nghệ sĩ nhân dân Sergei Vladimirovich Obraztsov, đây là nhà hát múa rối lớn nhất thế giới xét cả về quy mô lẫn bộ sưu tập. Từ năm 1970, nhà hát chuyển về toà nhà hiện nay trên phố Sadovaya-Samotyochnaya, đoạn thuộc Vành đai Vườn. Điểm khiến ai đi ngang cũng dừng lại là chiếc đồng hồ lớn gắn trên mặt tiền, do các nhà điêu khắc Dmitry Shakhovsky và Pavel Shimes thực hiện năm 1970: mặt đồng hồ có mười hai ngôi nhà nhỏ, cứ mỗi giờ lại có một chú gà trống cất tiếng gáy rồi một nhân vật cổ tích bước ra theo điệu dân ca Nga; đến đúng trưa và nửa đêm thì cả mười hai cánh cửa cùng mở, biến khoảnh khắc xem giờ thành một màn trình diễn tí hon. Bên trong, các khán phòng dàn dựng những vở rối kinh điển cho nhiều lứa tuổi, trong đó có cả những vở dành riêng cho khán giả người lớn — điều đã làm nên tên tuổi của trường phái Obraztsov. Tầng trệt là bảo tàng rối do chính nhà hát gây dựng từ thập niên 1930, lưu giữ hàng nghìn con rối từ khắp nước Nga và nhiều quốc gia, được coi là một trong những bộ sưu tập rối lớn và giá trị nhất thế giới. Với sự kết hợp giữa sân khấu sống động, bảo tàng và chiếc đồng hồ biểu tượng, nơi đây là điểm đến lý tưởng cho gia đình có trẻ nhỏ cũng như những ai yêu nghệ thuật múa rối.",
    "highlights_vi": [
        "Nhà hát múa rối lớn nhất thế giới, do Sergei Obraztsov sáng lập năm 1931.",
        "Đồng hồ cơ khí trên mặt tiền (1970) với 12 ngôi nhà nhỏ: mỗi giờ một nhân vật cổ tích xuất hiện, đúng trưa và nửa đêm cả 12 cùng mở.",
        "Bảo tàng rối ngay trong toà nhà, lưu giữ hàng nghìn con rối — một trong những bộ sưu tập lớn nhất thế giới.",
    ],
    "practical": {
        "hours_vi": "Theo lịch biểu diễn; phòng vé và bảo tàng mở gần như hằng ngày. Nên kiểm tra lịch trên trang chính thức.",
        "ticket_vi": "Mua vé theo suất diễn; vé thăm bảo tàng rối tính riêng. Giá thay đổi theo chương trình.",
        "duration_vi": "Buổi diễn khoảng 1–2 giờ; thêm 30–45 phút cho bảo tàng.",
        "best_time_vi": "Canh đúng giờ chẵn để xem màn đồng hồ; suất cuối tuần hợp cho gia đình, nên đặt trước.",
        "tips_vi": "Đứng trước mặt tiền vào phút giao giờ để xem đồng hồ; đi bộ ít phút từ ga Tsvetnoy Bulvar, gần Rạp xiếc Nikulin.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(55.77722, 37.61083),
    "official_site": "https://puppet.ru",
    "sources": [
        {"title": "Nhà hát Obraztsov — Lịch sử (trang chính thức)", "url": "https://puppet.ru/en/about/history/theatre-history"},
        {"title": "Moscow City Web Site (mos.ru)", "url": "https://www.mos.ru/en/news/item/76522073/"},
    ],
    "tags": ["theatre", "family", "indoor", "landmark", "top"],
    "status": "enriched",
    "last_updated": TODAY,
}


TSARSKOYE_LYCEUM = {
    "id": "saint-petersburg-tsarskoye-selo-lyceum",
    "slug": "tsarskoye-selo-lyceum",
    "region": "saint-petersburg",
    "region_name_vi": "Saint Petersburg",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Lyceum Hoàng gia Tsarskoye Selo — Bảo tàng-Lyceum tưởng niệm (nơi Pushkin theo học)",
    "name_ru": "Императорский Царскосельский лицей (Мемориальный Музей-Лицей)",
    "name_en": "Imperial Tsarskoye Selo Lyceum (Pushkin Memorial Lyceum Museum)",
    "categories": ["museum"],
    "coordinates": {"lat": 59.71750, "lon": 30.39694},
    "address_vi": "Phố Sadovaya, số 2, thành phố Pushkin (Tsarskoye Selo), Saint Petersburg; nằm sát Cung điện Ekaterina, cách trung tâm thành phố khoảng 25 km về phía nam.",
    "rating": None,
    "review_summary_vi": "Du khách, nhất là những người yêu văn học Nga, xúc động khi được tận mắt thấy căn phòng số 14 của Pushkin cùng giảng đường và thư viện được phục dựng tỉ mỉ. Nhiều người khuyên nên mua kèm vé thăm Cung điện Ekaterina liền kề. Điểm lưu ý: bảo tàng nhỏ, hay đông vào mùa cao điểm nên đi sớm hoặc đặt vé trước.",
    "presentation_short_vi": "Ngôi trường nội trú danh giá nơi đại thi hào Aleksandr Pushkin theo học khoá đầu tiên (1811–1817). Nằm trong một cánh của Cung điện Ekaterina ở Tsarskoye Selo, nay là bảo tàng phục dựng giảng đường, thư viện và các phòng ngủ học sinh đúng thời Pushkin.",
    "presentation_long_vi": "Được Hoàng đế Aleksandr I cho lập theo sắc lệnh và khai giảng ngày 19 tháng 10 năm 1811, Lyceum Tsarskoye Selo là một trong những học viện tinh hoa bậc nhất của Đế quốc Nga, dành đào tạo con em quý tộc cho các vị trí trọng yếu trong bộ máy nhà nước. Trường đặt trong một cánh nhà bốn tầng nối với Cung điện Ekaterina bằng một vòm bắc qua phố Sadovaya, do kiến trúc sư Vasily Stasov cải tạo cho phù hợp việc dạy học. Mỗi khoá chỉ nhận khoảng ba mươi học sinh, theo chương trình khép kín sáu năm, kết hợp cổ văn, ngoại ngữ, lịch sử, khoa học và luật. Học sinh sống nội trú trong những căn phòng nhỏ chừng ba mét vuông, được đánh số thay vì đặt tên, cửa để ngỏ suốt ngày đêm; căn phòng số 14 là của Pushkin. Chính tại đây, khoá tốt nghiệp đầu tiên năm 1817 đã sản sinh ra không chỉ nhà thơ vĩ đại nhất nước Nga mà còn nhiều nhân vật kiệt xuất như nhà ngoại giao — thủ tướng tương lai Aleksandr Gorchakov và nhà thơ Anton Delvig. Ngày 19 tháng 10 về sau trở thành 'Ngày Lyceum' được Pushkin và bạn học nhắc tới trong thơ. Năm 1844 trường chuyển về Sankt-Peterburg (đổi tên thành Lyceum Aleksandr) và đóng cửa năm 1918. Đến năm 1949, một bảo tàng-tưởng niệm được mở ngay trong toà nhà lịch sử, tái hiện Đại giảng đường, phòng đọc báo, thư viện, các lớp học và phòng ngủ học sinh đúng như thuở Pushkin còn theo học. Ngày nay thuộc quần thể Bảo tàng Toàn Nga mang tên A.S. Pushkin, đây là điểm đến không thể bỏ qua với người yêu văn chương khi ghé Tsarskoye Selo.",
    "highlights_vi": [
        "Nơi Aleksandr Pushkin theo học khoá đầu tiên (1811–1817); phòng ngủ số 14 của ông được phục dựng nguyên trạng.",
        "Đại giảng đường, thư viện và lớp học tái hiện đúng thời Pushkin; mở làm bảo tàng-tưởng niệm từ năm 1949.",
        "Ngày khai giảng 19/10 trở thành 'Ngày Lyceum' đi vào thơ Pushkin; toà nhà nằm ngay cạnh Cung điện Ekaterina.",
    ],
    "practical": {
        "hours_vi": "Thường mở khoảng 10:30–18:00; đóng cửa Thứ Ba và ngày Thứ Sáu cuối tháng (nên kiểm tra lịch theo mùa).",
        "ticket_vi": "Bán vé riêng; có thể mua kèm hành trình tham quan Tsarskoye Selo. Có dịch vụ máy thuyết minh.",
        "duration_vi": "Khoảng 1 giờ cho phần tham quan có hướng dẫn.",
        "best_time_vi": "Kết hợp trong ngày thăm Cung điện Ekaterina và Phòng Hổ phách; mùa hè đông khách nên đi sớm.",
        "tips_vi": "Lối vào ở số 2 phố Sadovaya; nên đặt vé Tsarskoye Selo trước vào mùa cao điểm để tránh xếp hàng.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(59.71750, 30.39694),
    "official_site": "https://museumpushkin.ru",
    "sources": [
        {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Tsarskoye_Selo_Lyceum"},
        {"title": "Russia Beyond", "url": "https://www.rbth.com/education/326427-tsarskoye-selo-lyceum-pushkin-opened"},
    ],
    "tags": ["museum", "history", "literature", "pushkin", "landmark"],
    "status": "enriched",
    "last_updated": TODAY,
}


PLAN = {
    "moscow": [KRYMSKY_BRIDGE, OBRAZTSOV],
    "saint-petersburg": [TSARSKOYE_LYCEUM],
}


def main():
    total_added = 0
    for region, recs in PLAN.items():
        path = os.path.join(REGIONS, f"{region}.json")
        arr = json.load(open(path, encoding="utf-8"))
        have = {p.get("slug") for p in arr}
        # sao lưu trước khi ghi
        bak = f"{path}.bak_add_{STAMP}"
        json.dump(arr, open(bak, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        added_here = []
        for r in recs:
            if r["slug"] in have:
                print(f"  = {region}: bo qua (da co) {r['slug']}")
                continue
            arr.append(r)
            added_here.append(r["slug"])
            total_added += 1
        json.dump(arr, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"  + {region}: them {len(added_here)} -> {added_here} | tong dia diem vung: {len(arr)} | backup: {os.path.basename(bak)}")
    print(f"TONG CONG THEM MOI: {total_added}")


if __name__ == "__main__":
    main()
