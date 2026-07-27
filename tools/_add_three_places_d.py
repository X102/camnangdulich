# -*- coding: utf-8 -*-
"""Bổ sung 3 địa điểm nổi tiếng/hiện đại còn thiếu vào Cẩm nang Du lịch Nga.
Nội dung tiếng Việt nguyên gốc (không sao chép nguyên văn), có ghi nguồn.
Tạo backup trước khi ghi, kiểm tra trùng slug/id. Chạy: python3 tools/_add_three_places_d.py"""
import json, os, shutil, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-25"


def maps_for(lat, lon):
    return {
        "yandex": f"https://yandex.com/maps/?pt={lon},{lat}&z=16&l=map",
        "google": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
    }


def null_rating():
    return {"value": None, "count": None, "source": None, "as_of": None}


RECORDS = {
    "moscow": [
        {
            "id": "moscow-borodino-panorama",
            "slug": "borodino-panorama",
            "region": "moscow",
            "region_name_vi": "Moskva",
            "federal_district": "Thành phố trực thuộc liên bang",
            "name_vi": "Bảo tàng - Toàn cảnh 'Trận Borodino' (Bô-rô-đi-nô)",
            "name_ru": "Музей-панорама «Бородинская битва»",
            "name_en": "Battle of Borodino Panorama (Museum-Panorama)",
            "categories": ["museum", "monument"],
            "coordinates": {"lat": 55.738761, "lon": 37.523151},
            "address_vi": "Đại lộ Kutuzovsky (Ku-tu-dốp-xki), số 38, công trình 1, Moscow 121170; gần ga tàu điện ngầm Kutuzovskaya và Park Pobedy.",
            "rating": null_rating(),
            "review_summary_vi": "Du khách thường ấn tượng mạnh với bức tranh vòng khổng lồ và hiệu ứng nhập vai như đứng giữa chiến trường; nhiều người khuyên nên đi kèm thuyết minh để hiểu rõ diễn biến trận đánh 1812.",
            "presentation_short_vi": "Bảo tàng trưng bày bức tranh toàn cảnh (panorama) khổng lồ dài khoảng 115 m, cao 15 m do hoạ sĩ Franz Roubaud vẽ, tái hiện thời khắc quyết định của trận Borodino năm 1812 giữa quân Nga và đại quân của Napoléon. Toà nhà tròn hiện nay khánh thành năm 1962 trên đại lộ Kutuzovsky, gần Khải Hoàn Môn và đồi Poklonnaya.",
            "presentation_long_vi": "Trận Borodino ngày 7 tháng 9 năm 1812 là trận đánh đẫm máu nhất trong cuộc Chiến tranh Vệ quốc chống Napoléon, với hơn một phần tư triệu binh sĩ tham chiến. Để kỷ niệm 100 năm sự kiện, hoạ sĩ Franz Roubaud (1856–1928) đã hoàn thành bức tranh toàn cảnh đồ sộ, lần đầu ra mắt công chúng năm 1912. Sau nhiều năm lưu lạc và hư hại, tác phẩm được phục chế và đặt trong một toà nhà - bảo tàng hình tròn xây riêng, khánh thành năm 1962 nhân 150 năm chiến thắng. Khi bước vào phòng tròn, du khách đứng trên bục quan sát ở trung tâm, xung quanh là bức tranh vải bao kín 360 độ kết hợp mô hình, địa hình giả và hiệu ứng âm thanh, tạo cảm giác như đang đứng giữa chiến trường vào đúng thời khắc giao tranh ác liệt nhất. Ngoài phòng panorama, bảo tàng còn trưng bày vũ khí, quân phục, tranh và hiện vật kể lại toàn bộ chiến dịch năm 1812, từ khi quân Pháp vượt biên giới cho tới lúc rút chạy. Cụm di tích quanh bảo tàng gồm tượng đài Nguyên soái Kutuzov, 'Ngôi nhà gỗ Kutuzov' (nơi diễn ra hội đồng quân sự Fili quyết định tạm bỏ ngỏ Moscow) và Khải Hoàn Môn gần đó, hợp thành một quần thể tưởng niệm cuộc chiến 1812 ngay trên trục đại lộ Kutuzovsky.",
            "highlights_vi": [
                "Bức tranh toàn cảnh 360° dài khoảng 115 m, cao 15 m của Franz Roubaud (ra mắt năm 1912), tái hiện trận Borodino 1812.",
                "Toà nhà bảo tàng hình tròn khánh thành năm 1962; bục quan sát trung tâm kết hợp mô hình và âm thanh tạo cảm giác nhập vai.",
                "Nằm trong quần thể tưởng niệm 1812 cùng tượng đài Kutuzov, 'Nhà gỗ Kutuzov' và Khải Hoàn Môn kề bên.",
            ],
            "practical": {
                "hours_vi": "Mở cửa thứ Bảy–thứ Tư 10:00–18:00; thứ Năm 10:00–21:00. Đóng cửa thứ Sáu và thứ Năm cuối cùng của tháng (quầy vé đóng trước giờ đóng cửa khoảng 45 phút).",
                "ticket_vi": "Vé tham khảo khoảng 400 rúp/người lớn, ưu đãi khoảng 200 rúp; Chủ nhật thứ ba hằng tháng thường miễn phí. Nên kiểm tra giá mới trên trang chính thức.",
                "duration_vi": "Khoảng 1–1,5 giờ.",
                "best_time_vi": "Ngày thường để tránh đông; có thể kết hợp tham quan Khải Hoàn Môn và đồi Poklonnaya (Công viên Chiến thắng) liền kề.",
                "tips_vi": "Nên xem panorama cùng phần thuyết minh để hiểu diễn biến; khu vực còn có tượng đài Kutuzov và Nhà gỗ Kutuzov để ghé thăm.",
            },
            "photo": None,
            "photo_credit": None,
            "maps": maps_for(55.738761, 37.523151),
            "official_site": "https://1812panorama.ru",
            "sources": [
                {"title": "Trang chính thức — Музей-панорама «Бородинская битва»", "url": "https://1812panorama.ru/"},
                {"title": "Advantour — The Battle of Borodino Panorama, Moscow", "url": "https://www.advantour.com/russia/moscow/museums/borodino-panorama-museum.htm"},
                {"title": "Atlas Obscura — Borodino Panorama", "url": "https://www.atlasobscura.com/places/borodino-panorama"},
            ],
            "tags": ["museum", "history", "1812", "panorama", "napoleonic-wars", "kutuzovsky"],
            "status": "enriched",
            "last_updated": TODAY,
        },
        {
            "id": "moscow-zhivopisny-bridge",
            "slug": "zhivopisny-bridge",
            "region": "moscow",
            "region_name_vi": "Moskva",
            "federal_district": "Thành phố trực thuộc liên bang",
            "name_vi": "Cầu Zhivopisny (Ji-vô-pi-xnưi — 'Cầu Phong Cảnh')",
            "name_ru": "Живописный мост",
            "name_en": "Zhivopisny Bridge (Picturesque Bridge)",
            "categories": ["bridge", "monument"],
            "coordinates": {"lat": 55.776389, "lon": 37.443056},
            "address_vi": "Phía tây bắc Moscow, trên trục đại lộ Krasnopresnensky – đại lộ Nguyên soái Zhukov, bắc qua sông Moskva cạnh công viên tự nhiên Serebryany Bor (Xê-rê-bri-a-nưi Bor).",
            "rating": null_rating(),
            "review_summary_vi": "Nhiều người xem đây là cây cầu có kiến trúc ấn tượng bậc nhất Moscow, rất hợp để ngắm và chụp ảnh từ bờ sông; một số tiếc rằng 'đĩa bay' bằng kính trên đỉnh vòm đến nay vẫn đóng cửa, không thể lên tham quan.",
            "presentation_short_vi": "Cầu Zhivopisny ('Cầu Phong Cảnh') là cầu dây văng đầu tiên của Moscow và là cầu dây văng cao nhất châu Âu, khánh thành ngày 27/12/2007. Điểm nhấn là vòm thép đỏ khổng lồ đưa công trình vươn cao khoảng 105 m bắc qua sông Moskva, bên dưới treo một 'đĩa bay' bằng kính hình elip từng được dự tính làm nhà hàng.",
            "presentation_long_vi": "Cầu Zhivopisny nằm ở phía tây bắc Moscow, thuộc trục đại lộ Krasnopresnensky – đại lộ Nguyên soái Zhukov, ngay cạnh công viên tự nhiên Serebryany Bor. Vì cả hai bờ sông tại đây đều là vùng bảo tồn thiên nhiên cấm xây dựng, các phương án cầu truyền thống đều không phù hợp; kiến trúc sư Nikolay Shumakov đã đưa ra lời giải độc đáo: trụ cầu là một vòm thép lớn, mặt cầu được treo vào vòm bằng hệ dây cáp, và phần lớn chiều dài cầu chạy dọc theo lòng sông thay vì cắt ngang để tránh xâm phạm đảo - rừng Serebryany Bor và không cản trở giao thông đường thuỷ. Toàn tuyến cầu hình chữ S dài 1.460 m, rộng 37 m, nhịp chính 409,5 m, mặt cầu cao khoảng 30 m trên mặt nước. Vòm thép sơn đỏ có nhịp khoảng 182 m, đưa tổng chiều cao công trình lên khoảng 105 m — biến nơi đây thành cầu dây văng cao nhất châu Âu và một biểu tượng kiến trúc hiện đại của thủ đô (năm 2017, kiến trúc sư Shumakov được trao giải Auguste Perret danh giá cho công trình này). Ngay dưới đỉnh vòm treo một buồng ngắm cảnh bằng kính hình elip, thường được ví như 'đĩa bay', dài 33 m và nặng khoảng 1.000 tấn. Kết cấu này lần lượt được dự tính làm nhà hàng trên cao rồi phòng đăng ký kết hôn, song đến nay vẫn bỏ trống và đóng cửa vì các vướng mắc về kỹ thuật, phòng cháy và kinh phí. Dù 'chiếc đĩa' chưa mở, hình bóng vòm đỏ in trên mặt sông vẫn là cảnh tượng ấn tượng, được nhiều người ngắm và chụp ảnh từ bờ Serebryany Bor hoặc từ khu đồi Krylatskoye.",
            "highlights_vi": [
                "Cầu dây văng đầu tiên của Moscow và cao nhất châu Âu, khánh thành 27/12/2007 (kiến trúc sư Nikolay Shumakov).",
                "Vòm thép đỏ nhịp khoảng 182 m, đưa công trình cao ~105 m; tuyến cầu hình chữ S dài 1.460 m chạy dọc theo lòng sông.",
                "'Đĩa bay' bằng kính hình elip treo dưới vòm (nặng ~1.000 tấn), từng dự tính làm nhà hàng/phòng cưới nhưng vẫn đóng cửa.",
            ],
            "practical": {
                "hours_vi": "Là cầu giao thông, có thể ngắm tự do bất kỳ lúc nào; không có giờ đóng/mở.",
                "ticket_vi": "Miễn phí (không bán vé). Buồng 'đĩa bay' trên đỉnh vòm không mở cho khách tham quan.",
                "duration_vi": "Khoảng 20–40 phút để ngắm và chụp ảnh.",
                "best_time_vi": "Lúc hoàng hôn hoặc khi lên đèn để thấy vòm đỏ nổi bật; ngắm đẹp nhất từ bờ sông Serebryany Bor hoặc khu Krylatskoye.",
                "tips_vi": "Không có lối lên đỉnh vòm; nên ngắm và chụp từ bờ sông, tiện kết hợp dạo rừng - bãi tắm Serebryany Bor. Không có ga tàu điện ngầm ngay cạnh — thường tới bằng ô tô/taxi hoặc đi metro tới Krylatskoye rồi bắt xe buýt.",
            },
            "photo": None,
            "photo_credit": None,
            "maps": maps_for(55.776389, 37.443056),
            "official_site": None,
            "sources": [
                {"title": "Wikipedia (EN) — Zhivopisny Bridge", "url": "https://en.wikipedia.org/wiki/Zhivopisny_Bridge"},
                {"title": "Википедия — Живописный мост", "url": "https://ru.wikipedia.org/wiki/Живописный_мост"},
                {"title": "Structurae — Zhivopisny Bridge (Moscow, 2007)", "url": "https://structurae.net/en/structures/zhivopisny-bridge"},
            ],
            "tags": ["bridge", "modern", "architecture", "cable-stayed", "moskva-river", "krylatskoye"],
            "status": "enriched",
            "last_updated": TODAY,
        },
    ],
    "saint-petersburg": [
        {
            "id": "saint-petersburg-artillery-museum",
            "slug": "artillery-museum",
            "region": "saint-petersburg",
            "region_name_vi": "Saint Petersburg",
            "federal_district": "Thành phố trực thuộc liên bang",
            "name_vi": "Bảo tàng Lịch sử - Quân sự Pháo binh, Công binh và Thông tin Liên lạc (Bảo tàng Pháo binh)",
            "name_ru": "Военно-исторический музей артиллерии, инженерных войск и войск связи",
            "name_en": "Military Historical Museum of Artillery, Engineers and Signal Corps",
            "categories": ["museum"],
            "coordinates": {"lat": 59.9539, "lon": 30.3138},
            "address_vi": "Công viên Aleksandrovsky (A-lếch-xan-đrốp-xki), số 7, Saint Petersburg; ga tàu điện ngầm Gorkovskaya. Bảo tàng nằm trong công trình Kronverk (Crôn-véc) hình móng ngựa, đối diện Pháo đài Petropavlovsk qua eo Kronverksky.",
            "rating": null_rating(),
            "review_summary_vi": "Du khách — đặc biệt là các gia đình có trẻ nhỏ và người yêu lịch sử quân sự — rất thích thú với khu trưng bày pháo, xe tăng và tên lửa ngoài trời rộng lớn; nhiều người nhận xét bộ sưu tập quá đồ sộ nên cần vài giờ mới xem hết.",
            "presentation_short_vi": "Đây là một trong những bảo tàng quân sự lâu đời và lớn nhất thế giới, đặt trong công trình phòng thủ Kronverk hình móng ngựa ngay cạnh Pháo đài Petropavlovsk. Bộ sưu tập bắt nguồn từ kho vũ khí do Pyotr Đại đế lập từ năm 1703, ngày nay có hơn 850.000 hiện vật cùng khoảng 250 khẩu pháo, xe tăng và bệ phóng tên lửa trưng bày ngoài trời.",
            "presentation_long_vi": "Nguồn gốc bảo tàng gắn với chỉ dụ của Pyotr Đại đế năm 1703 về việc giữ lại những khẩu pháo cổ và vũ khí chiến lợi phẩm quý hiếm để lưu niệm — khởi đầu cho gian 'Đáng ghi nhớ' (Достопамятный зал) đặt tại xưởng pháo binh. Trải qua ba thế kỷ, bộ sưu tập phát triển thành Bảo tàng Lịch sử - Quân sự Pháo binh, Công binh và Thông tin Liên lạc ngày nay, do Bộ Quốc phòng Nga quản lý. Từ giữa thế kỷ 19, bảo tàng chuyển về toà Kronverk — vành đai phòng thủ hình móng ngựa bằng gạch đỏ được xây thời Nikolai I để bảo vệ Pháo đài Petropavlovsk. Bên trong, các gian trưng bày dẫn dắt người xem đi suốt lịch sử quân sự Nga: từ vũ khí thời trung cổ, những khẩu pháo do bậc thầy Andrei Chokhov đúc, quân phục và huân chương của các hoàng đế và danh tướng, cho tới vũ khí của hai cuộc thế chiến và thời Chiến tranh Lạnh. Nổi bật có bệ phóng rocket 'Katyusha' huyền thoại của Thế chiến II và một gian riêng dành cho nhà thiết kế Mikhail Kalashnikov cùng khẩu súng trường AK-47 nổi tiếng toàn cầu. Sân ngoài trời rộng lớn bày hàng trăm khẩu pháo, giàn tên lửa và khí tài các thời kỳ — điểm đến đặc biệt hấp dẫn với những ai yêu lịch sử quân sự và cả trẻ em.",
            "highlights_vi": [
                "Một trong những bảo tàng quân sự lâu đời và lớn nhất thế giới, khởi nguồn từ kho vũ khí của Pyotr Đại đế (1703).",
                "Sân ngoài trời trưng bày khoảng 250 khẩu pháo, xe tăng, giàn tên lửa; tổng bộ sưu tập hơn 850.000 hiện vật.",
                "Có bệ phóng 'Katyusha' của Thế chiến II và gian trưng bày về Mikhail Kalashnikov cùng súng AK-47.",
            ],
            "practical": {
                "hours_vi": "Mở cửa thứ Tư–Chủ nhật 11:00–18:00 (ngừng nhận khách và bán vé từ 17:00). Nghỉ thứ Hai, thứ Ba và thứ Năm cuối cùng của tháng.",
                "ticket_vi": "Vé tham khảo (2026): người lớn 500 rúp; học sinh/người dưới 18 tuổi và người hưu trí 200 rúp; sinh viên đại học 300 rúp; trẻ dưới 7 tuổi miễn phí. Nên kiểm tra giá mới trên trang chính thức.",
                "duration_vi": "Khoảng 2–3 giờ nếu xem cả khu trong nhà và ngoài trời.",
                "best_time_vi": "Buổi sáng và ngày nắng ráo để dạo khu pháo ngoài trời; kết hợp tham quan Pháo đài Petropavlovsk và Công viên Aleksandrovsky gần đó.",
                "tips_vi": "Khu trưng bày ngoài trời rất rộng và hợp với trẻ em, nên mang giày thoải mái. Có thể ghé cùng tuần dương hạm Rạng Đông và đảo Zayachy trong một buổi.",
            },
            "photo": None,
            "photo_credit": None,
            "maps": maps_for(59.9539, 30.3138),
            "official_site": "https://www.artillery-museum.ru",
            "sources": [
                {"title": "Wikipedia (EN) — Military Historical Museum of Artillery, Engineers and Signal Corps", "url": "https://en.wikipedia.org/wiki/Military_Historical_Museum_of_Artillery,_Engineers_and_Signal_Corps"},
                {"title": "Культура.РФ — Военно-исторический музей артиллерии, инженерных войск и войск связи", "url": "https://www.culture.ru/institutes/11186/voenno-istoricheskii-muzei-artillerii-inzhenernykh-voisk-i-voisk-svyazi"},
                {"title": "spb-guide.ru — Артиллерийский музей: giờ mở cửa 2026 và giá vé", "url": "https://www.spb-guide.ru/artillerijskij-muzej.htm"},
            ],
            "tags": ["museum", "military", "artillery", "weapons", "history", "kronverk"],
            "status": "enriched",
            "last_updated": TODAY,
        },
    ],
}


def main():
    summary = []
    for region, recs in RECORDS.items():
        path = os.path.join(REGIONS, region + ".json")
        arr = json.load(open(path, encoding="utf-8"))
        existing_slugs = {r.get("slug") for r in arr}
        existing_ids = {r.get("id") for r in arr}
        to_add = []
        for rec in recs:
            if rec["slug"] in existing_slugs or rec["id"] in existing_ids:
                print(f"  ~ Bo qua (da ton tai): {region}/{rec['slug']}")
                continue
            to_add.append(rec)
        if not to_add:
            continue
        bak = path + f".bak_add_{STAMP}"
        shutil.copy2(path, bak)
        arr.extend(to_add)
        json.dump(arr, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        for rec in to_add:
            summary.append(f"{region}: + {rec['name_vi']} ({rec['coordinates']['lat']},{rec['coordinates']['lon']})")
        print(f"  + {region}: them {len(to_add)} ban ghi (tong file: {len(arr)}); backup: {os.path.basename(bak)}")
    print("\n=== DA THEM ===")
    for s in summary:
        print(" -", s)


if __name__ == "__main__":
    main()
