# -*- coding: utf-8 -*-
"""_add_three_places_h.py — Bổ sung 3 địa điểm nổi tiếng còn thiếu (lần chạy tự động 2026-07-25).

Thêm:
  1) Moskva  — Vườn Bách thảo Chính mang tên N.V. Tsitsin (GBS RAN) — vườn bách thảo lớn nhất châu Âu.
  2) Moskva  — Rạp xiếc Lớn Moskva trên Đại lộ Vernadsky (khác Rạp xiếc Nikulin đã có).
  3) Saint Petersburg — Vườn Mikhailovsky (Carlo Rossi), cạnh Nhà thờ Trên Máu Đổ.

Nội dung tiếng Việt nguyên gốc (không dịch/sao chép nguyên văn). Toạ độ thật đã kiểm chứng.
Chạy:  python3 tools/_add_three_places_h.py
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


BOTANICAL = {
    "id": "moscow-main-botanical-garden",
    "slug": "main-botanical-garden",
    "region": "moscow",
    "region_name_vi": "Moskva",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Vườn Bách thảo Chính mang tên N.V. Tsitsin (Glavny Botanichesky Sad, Ga-la-vơ-nưi Ba-ta-nhi-tra-xki Xát)",
    "name_ru": "Главный ботанический сад имени Н. В. Цицина РАН",
    "name_en": "Tsitsin Main Botanical Garden of the Russian Academy of Sciences",
    "categories": ["park_garden"],
    "coordinates": {"lat": 55.83847, "lon": 37.604007},
    "address_vi": "Phố Botanicheskaya, số 4, Moskva; gần các ga tàu điện ngầm Vladykino, Botanichesky Sad và VDNKh.",
    "rating": None,
    "review_summary_vi": "Du khách thường mô tả đây là 'lá phổi xanh' rộng lớn và yên bình của Moskva, lý tưởng để đi dạo cả ngày; điểm được khen nhiều nhất là Vườn Nhật Bản và rừng sồi cổ thụ. Vì khuôn viên quá rộng nên một số người thấy dễ lạc và khuyên nên mang theo bản đồ, nước uống.",
    "presentation_short_vi": "Vườn bách thảo lớn nhất châu Âu, rộng khoảng 331 héc-ta ngay trong lòng Moskva. Do Viện Hàn lâm Khoa học Liên Xô lập năm 1945, nơi đây quy tụ khoảng 21.000 giống loài thực vật, có rừng sồi nguyên sinh, vườn hồng, Vườn Nhật Bản và nhà kính nhiệt đới.",
    "presentation_long_vi": "Nằm ở phía bắc Moskva, ngay sát Trung tâm Triển lãm VDNKh, Vườn Bách thảo Chính của Viện Hàn lâm Khoa học Nga là một trong những vườn thực vật lớn và quan trọng nhất thế giới, đồng thời được xem là lớn nhất châu Âu với diện tích khoảng 331 héc-ta. Vườn được thành lập tháng 4 năm 1945, ngay khi Thế chiến II vừa khép lại, như một biểu tượng cho công cuộc kiến thiết và khát vọng khoa học của đất nước. Người đặt nền móng và dẫn dắt vườn suốt 35 năm là viện sĩ Nikolai Vasilyevich Tsitsin, một nhà thực vật và di truyền học lỗi lạc; đến năm 1991 vườn chính thức mang tên ông. Điểm độc đáo của nơi đây là cách bố trí các khu trưng bày theo vùng địa lý - du khách có thể lần lượt đi qua thảm thực vật đặc trưng của Trung Âu, Kavkaz, Siberia cho tới vùng Viễn Đông nước Nga, tựa như một chuyến du hành thu nhỏ khắp lục địa Á-Âu. Trong khuôn viên còn có một khu rừng sồi tự nhiên với những cây cổ thụ hàng trăm năm tuổi được gìn giữ nguyên vẹn, vườn hồng (rosarium) rực rỡ vào đầu mùa hè, bộ sưu tập tử đinh hương, cùng nhà kính nhiệt đới lưu giữ nhiều loài cây phương nam. Khu Vườn Nhật Bản với hồ nước, thác nhỏ, đèn đá và những cây phong lá đỏ là góc được yêu thích bậc nhất, đặc biệt vào mùa thu. Rộng rãi, tĩnh lặng và giàu giá trị khoa học, đây là nơi lý tưởng để tránh xa nhịp sống đô thị mà không cần rời khỏi thành phố.",
    "highlights_vi": [
        "Vườn bách thảo lớn nhất châu Âu (khoảng 331 héc-ta) với chừng 21.000 giống loài thực vật.",
        "Thành lập năm 1945, mang tên viện sĩ N.V. Tsitsin - giám đốc đầu tiên gắn bó với vườn suốt 35 năm.",
        "Có Vườn Nhật Bản, vườn hồng, rừng sồi nguyên sinh và các khu trưng bày cây theo vùng địa lý.",
    ],
    "practical": {
        "hours_vi": "Công viên mở cửa hằng ngày, khung giờ thay đổi theo mùa (thường khoảng 10:00–20:00 vào mùa ấm). Vườn Nhật Bản và nhà kính có giờ mở riêng, thường đóng vào mùa lạnh.",
        "ticket_vi": "Dạo phần lớn công viên miễn phí; Vườn Nhật Bản, nhà kính (fondovaya oranzhereya) và một số khu chuyên đề bán vé riêng.",
        "duration_vi": "Khoảng 2–4 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu; tháng 5–6 mùa tử đinh hương và hoa hồng, mùa thu lá phong đỏ ở Vườn Nhật Bản.",
        "tips_vi": "Khuôn viên rất rộng nên đi giày thoải mái và mang theo nước; có thể kết hợp tham quan VDNKh liền kề.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(55.83847, 37.604007),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Special:Search?search=Moscow%20Botanical%20Garden%20of%20Academy%20of%20Sciences"},
        {"title": "Encyclopaedia Britannica", "url": "https://www.britannica.com/place/Main-Botanical-Garden-of-the-Academy-of-Sciences"},
    ],
    "tags": ["park_garden", "park", "garden", "nature", "outdoor", "top"],
    "status": "enriched",
    "last_updated": TODAY,
}

CIRCUS = {
    "id": "moscow-great-moscow-state-circus",
    "slug": "great-moscow-state-circus",
    "region": "moscow",
    "region_name_vi": "Moskva",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Rạp xiếc Lớn Nhà nước Moskva trên Đại lộ Vernadsky (Bolshoy Moskovsky Tsirk, Bôn-sôi Ma-xcốp-xki Xưrk)",
    "name_ru": "Большой Московский государственный цирк на проспекте Вернадского",
    "name_en": "Great Moscow State Circus (Vernadsky Avenue)",
    "categories": ["theatre"],
    "coordinates": {"lat": 55.694495, "lon": 37.54029},
    "address_vi": "Đại lộ Vernadsky, số 7, Moskva 119296; đối diện Đại học Tổng hợp Quốc gia Moskva (MGU), gần ga tàu điện ngầm Universitet.",
    "rating": None,
    "review_summary_vi": "Khán giả đánh giá đây là điểm đến hàng đầu cho gia đình có trẻ nhỏ, ấn tượng nhất là quy mô hoành tráng và các màn biểu diễn nước, đu bay, thú và ảo thuật trên năm sàn diễn thay đổi. Một vài ý kiến lưu ý nên chọn hạng ghế gần để xem rõ và cân nhắc yếu tố có tiết mục thú biểu diễn.",
    "presentation_short_vi": "Một trong những rạp xiếc cố định lớn nhất thế giới với 3.400 chỗ ngồi, khánh thành năm 1971. Điểm đặc biệt là năm sàn diễn có thể hoán đổi, nâng lên từ dưới lòng đất chỉ trong ít phút: sàn tròn cổ điển, bể nước, sân băng, sàn đua ngựa và sàn hiệu ứng ánh sáng.",
    "presentation_long_vi": "Vươn lên bên Đại lộ Vernadsky, ngay đối diện toà nhà chính của Đại học Tổng hợp Moskva trên Đồi Chim Sẻ, Rạp xiếc Lớn Nhà nước Moskva là niềm tự hào của nghệ thuật xiếc Nga. Công trình khánh thành ngày 30 tháng 4 năm 1971, dưới thời Tổng Bí thư Leonid Brezhnev, với mái vòm cao 36 mét và khán phòng 3.400 chỗ - quy mô đưa nó vào hàng những rạp xiếc cố định lớn nhất thế giới. Bí quyết làm nên danh tiếng của rạp nằm ở năm sàn diễn có thể hoán đổi cho nhau: một sàn tròn cổ điển, một bể nước cho các màn trình diễn dưới nước, một sân băng, một sàn dành cho tiết mục đua ngựa và một sàn chuyên hiệu ứng - ánh sáng. Các sàn được cất giấu bên dưới và có thể nâng lên thay thế nhau chỉ trong vài phút, cho phép dàn dựng những chương trình quy mô lớn, biến hoá liên tục mà ít sân khấu nào sánh được. Cần phân biệt rạp xiếc này với Rạp xiếc Nikulin cổ kính hơn trên Đại lộ Tsvetnoy ở trung tâm: cả hai đều nổi tiếng, nhưng đây là cơ sở hiện đại, đồ sộ hơn, thường dành cho các vở diễn hoành tráng có yếu tố nước và kỹ xảo. Với truyền thống đào tạo nghệ sĩ xiếc bậc thầy của nước Nga, mỗi buổi diễn ở đây là sự kết hợp giữa kỹ thuật nhào lộn điêu luyện, hài kịch và những màn dàn dựng công phu, phù hợp cho mọi lứa tuổi.",
    "highlights_vi": [
        "Một trong những rạp xiếc cố định lớn nhất thế giới: 3.400 chỗ ngồi, vòm cao 36 mét.",
        "Năm sàn diễn hoán đổi (tròn cổ điển, bể nước, sân băng, đua ngựa, hiệu ứng) nâng lên chỉ trong ít phút.",
        "Khánh thành năm 1971, đối diện Đại học Tổng hợp Moskva - khác với Rạp xiếc Nikulin cổ hơn trên Đại lộ Tsvetnoy.",
    ],
    "practical": {
        "hours_vi": "Mở cửa theo lịch biểu diễn; các suất thường vào buổi tối và cuối tuần, tăng thêm suất dịp lễ, nghỉ hè và nghỉ đông.",
        "ticket_vi": "Mua vé theo từng suất diễn; giá thay đổi theo hạng ghế và chương trình. Nên đặt trước cho suất cuối tuần.",
        "duration_vi": "Mỗi buổi diễn khoảng 2–2,5 giờ (có giải lao).",
        "best_time_vi": "Các suất cuối tuần rất hợp với gia đình có trẻ nhỏ; nên đặt vé sớm cho mùa cao điểm.",
        "tips_vi": "Đừng nhầm với Rạp xiếc Nikulin trên Đại lộ Tsvetnoy; đến sớm để gửi đồ và ổn định chỗ ngồi trước giờ diễn.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(55.694495, 37.54029),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Special:Search?search=Great%20Moscow%20State%20Circus"},
        {"title": "Circopedia", "url": "https://www.circopedia.org/Bolshoi_Circus"},
    ],
    "tags": ["theatre", "circus", "family", "show", "entertainment"],
    "status": "enriched",
    "last_updated": TODAY,
}

MIKHAILOVSKY = {
    "id": "saint-petersburg-mikhailovsky-garden",
    "slug": "mikhailovsky-garden",
    "region": "saint-petersburg",
    "region_name_vi": "Saint Petersburg",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Vườn Mikhailovsky (Mikhaylovsky Sad, Mi-khai-lốp-xki Xát)",
    "name_ru": "Михайловский сад",
    "name_en": "Mikhailovsky Garden",
    "categories": ["park_garden"],
    "coordinates": {"lat": 59.9397, "lon": 30.3328},
    "address_vi": "Phố Sadovaya, số 2, Saint Petersburg; nằm sau Cung điện Mikhailovsky (Bảo tàng Nga), cạnh Nhà thờ Chúa Cứu Thế trên Máu Đổ; gần ga tàu điện ngầm Nevsky Prospekt/Gostiny Dvor.",
    "rating": None,
    "review_summary_vi": "Du khách khen đây là ốc đảo xanh yên tĩnh ngay cạnh những điểm tham quan sầm uất, đẹp để nghỉ chân, chụp ảnh với Nhà thờ Trên Máu Đổ và hàng rào gang trứ danh. Điểm lưu ý duy nhất là vườn có thể đóng cửa theo mùa để bảo dưỡng, nên kiểm tra trước khi tới.",
    "presentation_short_vi": "Khu vườn cảnh quan lịch sử hiếm có ngay giữa trung tâm Saint Petersburg, trải dài từ Cung điện Mikhailovsky (Bảo tàng Nga) tới Nhà thờ Trên Máu Đổ. Do kiến trúc sư Carlo Rossi tái thiết vào thập niên 1820, vườn pha trộn phong cách Pháp quy củ và Anh phóng khoáng bên bờ sông Moika.",
    "presentation_long_vi": "Ẩn mình sau Cung điện Mikhailovsky - nay là Bảo tàng Nga - Vườn Mikhailovsky là một trong những mẫu mực quý hiếm của nghệ thuật vườn cảnh Nga thế kỷ 18 đến đầu thế kỷ 19. Lịch sử khu đất trải dài từ thời Pyotr Đại đế, từng đi qua bàn tay của nhiều bậc thầy như Bartolomeo Rastrelli, nhưng diện mạo còn giữ tới nay chủ yếu là công trình của kiến trúc sư Carlo Rossi. Thập niên 1820, khi được Aleksandr I giao thiết kế cả một quần thể theo phong cách Đế chế (Empire) quanh Cung điện Mikhailovsky, Rossi đã tái quy hoạch khu vườn thành phần không thể tách rời của tổng thể kiến trúc ấy. Điều làm nên nét đặc biệt là sự hoà quyện hai trường phái: vườn Pháp quy củ với những lối đi thẳng tắp, thảm cỏ cân đối ở gần cung điện, chuyển dần sang vườn cảnh kiểu Anh phóng khoáng với thảm cỏ lượn sóng, lùm cây tự nhiên và hồ nhỏ phía bờ sông Moika. Vườn được giới hạn bởi phố Sadovaya ở phía đông, sông Moika ở phía bắc và kênh Griboedov ở phía tây, tạo nên một không gian khép kín, tĩnh lặng đối lập với sự nhộn nhịp của Đại lộ Nevsky gần đó. Dọc ranh giới phía bắc là hàng rào gang uốn lượn tinh xảo do kiến trúc sư Alfred Parland - người dựng Nhà thờ Trên Máu Đổ - thiết kế, nay trở thành một trong những biểu tượng được chụp ảnh nhiều nhất. Ngày nay do Bảo tàng Nga quản lý, vườn còn là nơi tổ chức liên hoan thường niên 'Những khu vườn Hoàng gia nước Nga', và luôn là chốn dừng chân lý tưởng giữa hành trình khám phá trung tâm lịch sử của thành phố.",
    "highlights_vi": [
        "Do kiến trúc sư Carlo Rossi tái thiết thập niên 1820, kết hợp phong cách vườn Pháp quy củ và vườn cảnh Anh.",
        "Nằm liền kề Cung điện Mikhailovsky (Bảo tàng Nga) và Nhà thờ Trên Máu Đổ, có hàng rào gang nghệ thuật trứ danh.",
        "Là nơi tổ chức liên hoan 'Những khu vườn Hoàng gia nước Nga' và là ốc đảo yên tĩnh giữa trung tâm thành phố.",
    ],
    "practical": {
        "hours_vi": "Mở cửa hằng ngày theo mùa (thường khoảng 10:00–22:00 mùa hè); có thể đóng cửa vào mùa lạnh hoặc những ngày bảo dưỡng thảm cỏ - nên kiểm tra lịch trước khi đến.",
        "ticket_vi": "Vào cửa miễn phí (một số sự kiện, liên hoan có thể bán vé riêng).",
        "duration_vi": "Khoảng 45 phút – 1,5 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu; đẹp nhất khi kết hợp tham quan Bảo tàng Nga và Nhà thờ Trên Máu Đổ liền kề.",
        "tips_vi": "Cổng vào ở phía phố Sadovaya và gần Nhà thờ Trên Máu Đổ; có thể kết hợp dạo bộ dọc kênh Griboedov.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(59.9397, 30.3328),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Mikhailovsky_Garden"},
        {"title": "In Your Pocket - St. Petersburg", "url": "https://www.inyourpocket.com/st-petersburg-en/mikhailovsky-garden_141330v"},
    ],
    "tags": ["park_garden", "garden", "free", "outdoor", "landmark"],
    "status": "enriched",
    "last_updated": TODAY,
}

PLAN = {
    "moscow": [BOTANICAL, CIRCUS],
    "saint-petersburg": [MIKHAILOVSKY],
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
                print(f"  = {region}: bỏ qua (đã có) {r['slug']}")
                continue
            arr.append(r)
            added_here.append(r["slug"])
            total_added += 1
        json.dump(arr, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"  + {region}: them {len(added_here)} -> {added_here} | tong dia diem vung: {len(arr)} | backup: {os.path.basename(bak)}")
    print(f"TONG CONG THEM MOI: {total_added}")


if __name__ == "__main__":
    main()
