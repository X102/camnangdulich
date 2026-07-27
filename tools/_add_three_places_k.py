# -*- coding: utf-8 -*-
"""_add_three_places_k.py — Bổ sung 3 địa điểm nổi tiếng/hiện đại còn thiếu (lần chạy tự động 2026-07-25, đợt k).

Thêm:
  1) Moskva            — Bảo tàng Trung tâm Các Lực lượng Vũ trang (Central Armed Forces Museum) — nơi lưu giữ Lá cờ Chiến thắng gốc.
  2) Saint Petersburg  — Nhà thờ Chính toà Chúa Biến Hình (Spaso-Preobrazhensky) — hàng rào ghép từ nòng đại bác Thổ.
  3) Nizhny Novgorod   — Cáp treo vượt sông Volga (2012) với nhịp qua nước từng dài nhất châu Âu.

Nội dung tiếng Việt nguyên gốc (không dịch/sao chép nguyên văn). Toạ độ thật đã kiểm chứng qua web.
Chạy:  python3 tools/_add_three_places_k.py
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


CENTRAL_ARMED_FORCES_MUSEUM = {
    "id": "moscow-central-armed-forces-museum",
    "slug": "central-armed-forces-museum",
    "region": "moscow",
    "region_name_vi": "Moskva",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Bảo tàng Trung tâm Các Lực lượng Vũ trang (Tsentralny Muzey Vooruzhyonnykh Sil, Xen-tran-nưi Mu-dây)",
    "name_ru": "Центральный музей Вооружённых сил",
    "name_en": "Central Armed Forces Museum",
    "categories": ["museum"],
    "coordinates": {"lat": 55.78472, "lon": 37.61722},
    "country": "russia",
    "address_vi": "Phố Sovetskoy Armii, số 2, công trình 1, Moskva 129110 (khu Meshchansky, cạnh Nhà hát Trung ương Quân đội Nga và Công viên Ekaterininsky); gần ga tàu điện ngầm Dostoevskaya và Novoslobodskaya.",
    "rating": None,
    "review_summary_vi": "Nhiều du khách xem đây là một trong những bảo tàng quân sự đáng đến nhất Moskva, ấn tượng nhất với khu trưng bày ngoài trời gồm xe tăng, pháo, máy bay và tên lửa mà trẻ em rất thích. Không ít người xúc động khi tận mắt thấy Lá cờ Chiến thắng gốc và các quân kỳ thu được của phát xít. Một lưu ý thường gặp: phần lớn chú thích bằng tiếng Nga, nên khách nước ngoài nên thuê hướng dẫn hoặc dùng ứng dụng dịch.",
    "presentation_short_vi": "Một trong những bảo tàng lịch sử quân sự lớn nhất thế giới, thành lập tháng 12 năm 1919. Bảo tàng kể lại chặng đường của các lực lượng vũ trang Nga và Liên Xô qua hơn hai mươi gian trưng bày cùng khu khí tài ngoài trời, nơi lưu giữ báu vật là Lá cờ Chiến thắng cắm trên nóc nhà Quốc hội Đức năm 1945.",
    "presentation_long_vi": "Ra đời từ tháng 12 năm 1919, ngay trong những năm nội chiến, Bảo tàng Trung tâm Các Lực lượng Vũ trang là một trong những bảo tàng lịch sử quân sự lâu đời và đồ sộ nhất thế giới. Từ năm 1965, bảo tàng chuyển về toà nhà hiện nay ở phía bắc Moskva, bên phố Sovetskoy Armii, cạnh Nhà hát Trung ương Quân đội Nga và Công viên Ekaterininsky. Bộ sưu tập hơn 800.000 hiện vật được sắp đặt trong khoảng hai mươi tư gian phòng, dẫn người xem đi suốt lịch sử quân đội Nga và Liên Xô: từ thời nội chiến, hai cuộc thế chiến, Chiến tranh Vệ quốc Vĩ đại cho tới thời hiện đại. Hiện vật quý giá nhất là Lá cờ Chiến thắng — lá cờ đỏ được cắm trên nóc toà nhà Quốc hội Đức (Reichstag) ở Berlin tháng 5 năm 1945; bên cạnh đó là các quân kỳ mặt trận và những lá cờ thu được của quân phát xít, từng bị ném xuống chân Lăng Lenin trong Lễ duyệt binh Chiến thắng. Gian Chiến tranh Lạnh trưng bày mảnh vỡ chiếc máy bay do thám U-2 của Mỹ bị bắn rơi trên bầu trời Liên Xô năm 1960, cùng nhiều kỷ vật khác. Ngoài trời, một khoảng sân rộng bày khoảng 160 mẫu khí tài thế kỷ 20 — xe tăng, pháo, tàu bọc thép, đoàn tàu bọc thép, máy bay và tên lửa — nơi các gia đình và người yêu lịch sử quân sự đặc biệt ưa thích.",
    "highlights_vi": [
        "Thành lập tháng 12 năm 1919, thuộc hàng bảo tàng lịch sử quân sự lớn nhất thế giới với hơn 800.000 hiện vật trong khoảng 24 gian trưng bày.",
        "Lưu giữ Lá cờ Chiến thắng gốc — lá cờ cắm trên nóc nhà Quốc hội Đức ở Berlin tháng 5-1945 — cùng các quân kỳ thu được của phát xít.",
        "Sân trưng bày ngoài trời với khoảng 160 mẫu khí tài thế kỷ 20: xe tăng, pháo, tàu và đoàn tàu bọc thép, máy bay, tên lửa.",
    ],
    "practical": {
        "hours_vi": "Thường mở cửa từ giữa tuần đến Chủ nhật (khoảng 10:00–17:00), nghỉ thứ Hai và thứ Ba; nên kiểm tra lịch trên trang chính thức trước khi đến.",
        "ticket_vi": "Vé vào cửa có thu phí, ưu đãi cho học sinh - sinh viên và người cao tuổi; khu khí tài ngoài trời có thể mua vé riêng. Giá thay đổi theo thời điểm.",
        "duration_vi": "Khoảng 1,5–2,5 giờ cho cả khu trong nhà và sân ngoài trời.",
        "best_time_vi": "Mùa hè thuận lợi để thăm khu khí tài ngoài trời; các ngày lễ quân đội (23-2, 9-5) không khí đặc biệt sôi động.",
        "tips_vi": "Chú thích chủ yếu bằng tiếng Nga — nên thuê hướng dẫn hoặc dùng ứng dụng dịch; đi bộ ít phút từ ga Dostoevskaya, dễ kết hợp với Nhà hát Quân đội Nga và Bảo tàng Lịch sử Gulag gần đó.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(55.78472, 37.61722),
    "official_site": "http://www.cmaf.ru/",
    "sources": [
        {"title": "Central Armed Forces Museum — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Central_Armed_Forces_Museum"},
        {"title": "Bảo tàng Trung tâm Các Lực lượng Vũ trang — Culture.ru", "url": "https://www.culture.ru/institutes/12381/centralnyi-muzei-vooruzhennykh-sil-rossiiskoi-federacii"},
        {"title": "Trang chính thức Bảo tàng (cmaf.ru)", "url": "http://www.cmaf.ru/"},
    ],
    "tags": ["museum", "history", "military", "indoor", "family"],
    "status": "enriched",
    "last_updated": TODAY,
}


TRANSFIGURATION_CATHEDRAL = {
    "id": "saint-petersburg-transfiguration-cathedral",
    "slug": "transfiguration-cathedral",
    "region": "saint-petersburg",
    "region_name_vi": "Saint Petersburg",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Nhà thờ Chính toà Chúa Biến Hình (Spaso-Preobrazhensky Sobor, Xpa-xô Prê-ô-bra-zhen-xki)",
    "name_ru": "Спасо-Преображенский собор",
    "name_en": "Transfiguration Cathedral (Spaso-Preobrazhensky Cathedral)",
    "categories": ["church"],
    "coordinates": {"lat": 59.94304, "lon": 30.35244},
    "country": "russia",
    "address_vi": "Quảng trường Preobrazhenskaya, số 1, Sankt-Peterburg (quận Trung tâm); gần ga tàu điện ngầm Chernyshevskaya.",
    "rating": None,
    "review_summary_vi": "Du khách thường khen ngôi nhà thờ có không gian trang nghiêm, yên tĩnh và ít đông đúc hơn các thánh đường nổi tiếng trên phố Nevsky, hợp để chiêm nghiệm. Nhiều người ấn tượng nhất với hàng rào độc đáo ghép từ nòng đại bác chiến lợi phẩm của quân Thổ. Vì đây là nhà thờ đang hoạt động, khách được nhắc ăn mặc kín đáo và giữ yên lặng khi có lễ.",
    "presentation_short_vi": "Thánh đường của Trung đoàn Cận vệ Preobrazhensky, xây lại theo phong cách Đế chế bởi kiến trúc sư Vasily Stasov và được thánh hiến năm 1829. Nổi bật với hàng rào làm từ 102 nòng đại bác thu được của quân Thổ, dựng để mừng chiến thắng trong cuộc chiến Nga - Thổ 1828–1829.",
    "presentation_long_vi": "Toạ lạc trên quảng trường Preobrazhenskaya yên tĩnh giữa trung tâm Sankt-Peterburg, Nhà thờ Chính toà Chúa Biến Hình gắn liền với Trung đoàn Cận vệ Preobrazhensky — đơn vị tinh nhuệ từng đưa Nữ hoàng Elizaveta lên ngôi năm 1741. Ngôi thánh đường đầu tiên dựng giữa thế kỷ 18, nhưng đến năm 1825 thì bị hoả hoạn thiêu rụi. Kiến trúc sư Vasily Stasov được giao dựng lại; công trình mới hoàn thành và được thánh hiến năm 1829 theo phong cách Đế chế (hậu cổ điển) trang nghiêm, mái vòm chính vươn cao khoảng 41,5 mét, nổi bật giữa khu phố. Điểm độc đáo bậc nhất là hàng rào bao quanh, dựng trong các năm 1832–1833 để tôn vinh chiến thắng của nước Nga trong cuộc chiến Nga - Thổ Nhĩ Kỳ 1828–1829: 102 nòng đại bác bằng đồng thu được từ các pháo đài Thổ như Izmail, Varna, Silistra được đặt trên 34 bệ đá granite, cứ ba nòng một bệ, miệng chúc xuống đất hàm ý sẽ không bao giờ khai hoả nữa. Trên nhiều nòng pháo vẫn còn quốc huy Đế quốc Ottoman và cả những cái tên mà người Thổ từng đặt cho súng. Trải qua thời Xô Viết đầy biến động, đây là một trong số ít nhà thờ ở Sankt-Peterburg chưa từng đóng cửa, liên tục duy trì các buổi lễ, và đến nay vẫn lưu giữ nhiều biểu tượng gắn với hào khí của trung đoàn cận vệ năm xưa.",
    "highlights_vi": [
        "Thánh đường của Trung đoàn Cận vệ Preobrazhensky, xây lại bởi kiến trúc sư Vasily Stasov và thánh hiến năm 1829 theo phong cách Đế chế.",
        "Hàng rào độc nhất vô nhị ghép từ 102 nòng đại bác đồng thu được của quân Thổ, đặt trên 34 bệ đá, miệng súng chúc xuống — mừng chiến thắng Nga - Thổ 1828–1829.",
        "Một trong số ít nhà thờ ở Sankt-Peterburg không đóng cửa suốt thời Xô Viết, liên tục duy trì hoạt động thờ phụng.",
    ],
    "practical": {
        "hours_vi": "Mở cửa hằng ngày, thường khoảng 8:00–20:00 theo giờ lễ; nên tránh giờ hành lễ nếu chỉ muốn tham quan.",
        "ticket_vi": "Vào cửa tự do (nhà thờ đang hoạt động); hoan nghênh quyên góp tuỳ tâm.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Buổi sáng yên tĩnh; ngắm hàng rào đại bác rõ và đẹp nhất dưới ánh sáng ban ngày.",
        "tips_vi": "Ăn mặc kín đáo, nữ nên trùm khăn khi vào trong; dễ kết hợp dạo bộ tới phố Nevsky, Vườn Tauride hoặc ga Chernyshevskaya gần đó.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(59.94304, 30.35244),
    "official_site": None,
    "sources": [
        {"title": "Transfiguration Cathedral, Saint Petersburg — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Transfiguration_Cathedral_(Saint_Petersburg)"},
        {"title": "Спасо-Преображенский собор — Sobory.ru", "url": "https://sobory.ru/article/?object=01539"},
        {"title": "Transfiguration Cathedral — saint-petersburg.com", "url": "http://www.saint-petersburg.com/cathedrals/transfiguration-cathedral/"},
    ],
    "tags": ["church", "history", "architecture", "military", "free"],
    "status": "enriched",
    "last_updated": TODAY,
}


NIZHNY_NOVGOROD_CABLEWAY = {
    "id": "nizhny-novgorod-cableway",
    "slug": "nizhny-novgorod-cableway",
    "region": "nizhny-novgorod",
    "region_name_vi": "Tỉnh Nizhny Novgorod",
    "federal_district": "Vùng Volga",
    "name_vi": "Cáp treo Nizhny Novgorod (Nizhegorodskaya Kanatnaya Doroga, Ka-nát-na-ya Đô-rô-ga)",
    "name_ru": "Нижегородская канатная дорога",
    "name_en": "Nizhny Novgorod Cableway",
    "categories": ["other"],
    "coordinates": {"lat": 56.3377, "lon": 44.0493},
    "country": "russia",
    "address_vi": "Ga dưới ở Nizhny Novgorod: kè Kazanskaya, số 8A (gần Quảng trường Sennaya); tuyến vượt sông Volga sang thành phố Bor.",
    "rating": None,
    "review_summary_vi": "Du khách thích thú vì được ngắm sông Volga, dải bờ kè và Kremlin Nizhny Novgorod từ trên cao trong cabin nhỏ — trải nghiệm vừa là phương tiện đi lại vừa là trò giải trí. Trẻ em đặc biệt hào hứng. Nhiều người khuyên đi lúc trời quang và lưu ý cáp có thể chạy chậm hoặc tạm dừng khi gió lớn; phía Bor không có nhiều điểm chơi nên khách thường mua vé khứ hồi rồi quay lại ngay.",
    "presentation_short_vi": "Tuyến cáp treo vượt sông Volga dài 3.661 m, khánh thành năm 2012, nối Nizhny Novgorod với thành phố Bor. Nhịp vượt mặt nước không trụ đỡ dài 861 m của tuyến từng được xem là dài nhất châu Âu, mang lại tầm nhìn ngoạn mục xuống dòng Volga.",
    "presentation_long_vi": "Khánh thành ngày 9 tháng 2 năm 2012, cáp treo Nizhny Novgorod ban đầu được xây để giải bài toán đi lại: đưa cư dân băng qua sông Volga rộng lớn sang thành phố Bor ở bờ đối diện nhanh hơn nhiều so với đường bộ hay tàu. Nhưng rồi tuyến cáp do hãng Poma của Pháp thi công lại nhanh chóng trở thành một điểm tham quan được yêu thích. Với chiều dài 3.661 mét và nhịp vượt mặt nước không trụ đỡ lên tới 861 mét, tuyến từng giữ kỷ lục nhịp qua nước dài nhất châu Âu; những cột trụ cao hơn 80 mét đỡ dây cáp băng ngang dòng sông. Mỗi chuyến đi kéo dài khoảng mười ba phút, đủ để hành khách thu vào tầm mắt khung cảnh mở rộng: dòng Volga uốn lượn, dải bờ kè, những mái vòm nhà thờ và cả Kremlin Nizhny Novgorod cổ kính phía xa. Nhìn từ cabin treo lơ lửng giữa trời, cảnh quan đổi thay theo mùa — mặt nước lấp lánh mùa hè, băng tuyết trắng xoá mùa đông — khiến chuyến 'bay' ngắn ngủi trở nên đáng nhớ. Vào những ngày gió mạnh, hệ thống có thể tự động giảm tốc hoặc tạm dừng, nên du khách hãy kiểm tra lịch chạy trước khi đến.",
    "highlights_vi": [
        "Khánh thành năm 2012, dài 3.661 m, do hãng Poma (Pháp) xây dựng để vượt sông Volga sang thành phố Bor.",
        "Nhịp vượt mặt nước không trụ đỡ dài 861 m — từng được coi là dài nhất châu Âu; trụ cáp cao hơn 80 m.",
        "Mỗi lượt khoảng 13 phút, mở tầm nhìn toàn cảnh sông Volga, bờ kè và Kremlin Nizhny Novgorod.",
    ],
    "practical": {
        "hours_vi": "Khoảng 06:45–21:00; nghỉ kỹ thuật thứ Hai và thứ Năm 10:45–13:00 (nên kiểm tra lịch trên trang chính thức).",
        "ticket_vi": "Một chiều khoảng 100 rúp; trẻ 7–12 tuổi khoảng 50 rúp; dưới 7 tuổi miễn phí (giá tham khảo, có thể thay đổi).",
        "duration_vi": "~13 phút mỗi lượt; tính cả chờ và đi khứ hồi khoảng 45–60 phút.",
        "best_time_vi": "Ngày trời quang để ngắm sông Volga; hoàng hôn và mùa đông băng tuyết đặc biệt đẹp.",
        "tips_vi": "Ga dưới cách Kremlin Nizhny Novgorod khoảng 30 phút đi bộ, gần Quảng trường Sennaya; mang theo áo ấm vì trên cao lộng gió; gió lớn có thể khiến cáp chạy chậm.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(56.3377, 44.0493),
    "official_site": "http://nnkd.ru/",
    "sources": [
        {"title": "Nizhny Novgorod Cableway — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Nizhny_Novgorod_Cableway"},
        {"title": "Cáp treo Nizhny Novgorod — NashaPlaneta.net", "url": "https://nashaplaneta.net/europe/russia/nizhny-novgorod-dostoprimechatelnosti-kanatnaya-doroga_en"},
        {"title": "Trang chính thức (nnkd.ru)", "url": "http://nnkd.ru/"},
    ],
    "tags": ["modern", "viewpoint", "family", "outdoor", "transport"],
    "status": "enriched",
    "last_updated": TODAY,
}


PLAN = {
    "moscow": [CENTRAL_ARMED_FORCES_MUSEUM],
    "saint-petersburg": [TRANSFIGURATION_CATHEDRAL],
    "nizhny-novgorod": [NIZHNY_NOVGOROD_CABLEWAY],
}


def main():
    total_added = 0
    for region, recs in PLAN.items():
        path = os.path.join(REGIONS, f"{region}.json")
        arr = json.load(open(path, encoding="utf-8"))
        have_slug = {p.get("slug") for p in arr}
        have_id = {p.get("id") for p in arr}
        # sao lưu trước khi ghi
        bak = f"{path}.bak_add_{STAMP}"
        json.dump(arr, open(bak, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        added_here = []
        for r in recs:
            if r["slug"] in have_slug or r["id"] in have_id:
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
