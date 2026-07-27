# -*- coding: utf-8 -*-
"""_add_three_places_o.py — Bổ sung 3 địa điểm nổi tiếng/hiện đại còn thiếu (Moscow x1, SPB x2).
Nội dung tiếng Việt nguyên gốc, tọa độ thật, ghi nguồn. Chạy: python3 tools/_add_three_places_o.py"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-26"

NEW = [
    {
        "id": "moscow-vasnetsov-house-museum",
        "slug": "vasnetsov-house-museum",
        "region": "moscow",
        "region_name_vi": "Moskva",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Nhà-Bảo tàng Viktor Vasnetsov (Ngôi nhà 'terem' cổ tích)",
        "name_ru": "Дом-музей В. М. Васнецова",
        "name_en": "Viktor Vasnetsov House-Museum",
        "categories": ["museum"],
        "coordinates": {"lat": 55.77669, "lon": 37.62608},
        "address_vi": "Ngõ Vasnetsov 13 (pereulok Vasnetsova, 13), quận Meshchansky, Moskva",
        "rating": {"value": None, "count": None, "source": "Tripadvisor", "as_of": "2026-07"},
        "review_summary_vi": "Du khách thường mô tả nơi đây như bước vào một câu chuyện cổ tích Nga: ngôi nhà gỗ hình 'terem' nhỏ nhắn, ấm cúng, treo đầy tranh và đồ nội thất do chính hoạ sĩ thiết kế. Nhiều người khen không gian yên tĩnh, ít đông đúc và nhân viên thân thiện; một số lưu ý bảo tàng khá nhỏ, nằm lẩn trong khu dân cư nên hơi khó tìm, và phần chú thích chủ yếu bằng tiếng Nga.",
        "presentation_short_vi": "Ngôi nhà gỗ hình 'terem' cổ tích do danh hoạ Viktor Vasnetsov tự thiết kế và sống tới cuối đời — nay là bảo tàng lưu niệm (chi nhánh Bảo tàng Tretyakov), trưng bày tranh sử thi, đồ nội thất và những lò sưởi ốp gạch men do chính ông vẽ kiểu.",
        "presentation_long_vi": "Nép mình giữa những chung cư hiện đại ở quận Meshchansky là một ngôi nhà gỗ nhỏ trông như bước ra từ truyện cổ tích Nga — mái vòm hình thùng sơn ô carô đỏ-lục, phần gác lửng bằng gỗ nhô ra như một toà 'terem' thời trung cổ. Đó là tổ ấm mà Viktor Vasnetsov (1848–1926), bậc thầy của dòng tranh sử thi và cổ tích Nga với những kiệt tác như 'Ba tráng sĩ', 'Alyonushka' hay 'Ivan Tsarevich cưỡi sói xám', tự tay phác thảo và cho dựng trong hai năm 1893–1894. Vốn say mê nghệ thuật dân gian và kiến trúc Nga cổ, ông biến chính ngôi nhà thành một tác phẩm: phòng khách dựng theo lối phòng của giới quý tộc boyar thế kỷ 17, còn phòng ăn lại mộc mạc như gian bếp nông dân, tất cả nối nhau bằng cầu thang gỗ và những chiếc lò sưởi ốp gạch men rực rỡ do ông thiết kế. Hoạ sĩ sống và làm việc tại đây cho tới khi qua đời năm 1926; đến năm 1953, ngôi nhà mở cửa thành bảo tàng lưu niệm và ngày nay là một chi nhánh của Bảo tàng Tretyakov. Bên trong vẫn giữ nguyên xưởng vẽ trên tầng hai với những bức tranh khổ lớn về đề tài thần thoại, cùng bàn ghế, giá vẽ và vật dụng gắn bó với cuộc đời ông. Nhỏ nhắn và ít khách, nơi đây là điểm dừng chân lý tưởng cho những ai muốn cảm nhận tâm hồn Nga qua lăng kính cổ tích.",
        "highlights_vi": [
            "Ngôi nhà do chính Viktor Vasnetsov thiết kế theo phong cách 'Tân Nga' (neo-Russian), dựng năm 1893–1894 với hình dáng toà 'terem' gỗ truyền thống.",
            "Nội thất pha trộn hai thời kỳ: phòng khách kiểu boyar thế kỷ 17 và phòng ăn mộc mạc như nhà nông dân, cùng những lò sưởi ốp gạch men do hoạ sĩ tự vẽ kiểu.",
            "Mở cửa thành bảo tàng năm 1953, nay là chi nhánh của Bảo tàng Tretyakov, lưu giữ xưởng vẽ và nhiều tranh sử thi – cổ tích của ông."
        ],
        "practical": {
            "hours_vi": "Thường 10:00–17:00; nghỉ thứ Hai và thứ Ba (lịch có thể thay đổi — nên xem trang của Bảo tàng Tretyakov).",
            "ticket_vi": "Bán vé tại chỗ, giá phải chăng; có ưu đãi cho học sinh, sinh viên và người cao tuổi.",
            "duration_vi": "45 phút – 1 giờ.",
            "best_time_vi": "Ngày thường để tránh đông; có thể kết hợp cùng khu Prospekt Mira và Vườn Bách thảo Aptekarsky gần đó.",
            "tips_vi": "Gần ga metro Sukharevskaya và Prospekt Mira; nhà nằm trong ngõ nhỏ yên tĩnh nên dùng bản đồ để tìm; có thể phải bọc giày khi vào tham quan."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=37.62608,55.77669&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=55.77669,37.62608"
        },
        "official_site": None,
        "sources": [
            {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Viktor_Vasnetsov"},
            {"title": "Rusmania — Viktor Vasnetsov House-Museum", "url": "https://rusmania.com/central/moscow-federal-city/moscow/meschansky/beyond-the-garden-ring-around-olimpiysky-prospekt/viktor-vasnetsov-house-museum"}
        ],
        "tags": ["museum", "art", "architecture", "indoor", "terem", "tretyakov"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-twelve-collegia",
        "slug": "twelve-collegia",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Toà nhà Mười hai Collegia (Zdanie Dvenadtsati Kollegiy)",
        "name_ru": "Здание Двенадцати коллегий",
        "name_en": "Twelve Collegia (Building of the Twelve Colleges)",
        "categories": ["monument"],
        "coordinates": {"lat": 59.94167, "lon": 30.29861},
        "address_vi": "Bờ kè Đại học 7–9 (Universitetskaya naberezhnaya, 7–9), đảo Vasilievsky, Saint Petersburg",
        "rating": {"value": None, "count": None, "source": "Tripadvisor", "as_of": "2026-07"},
        "review_summary_vi": "Du khách mê kiến trúc và lịch sử ấn tượng với dãy nhà gạch đỏ dài tít tắp bên bờ Neva — công trình đồ sộ nhất còn lại từ thời Pyotr Đại đế. Nhiều người trầm trồ hành lang tầng hai dài gần 400 m thông suốt cùng bầu không khí học thuật của ngôi trường đại học lâu đời; lưu ý đây là toà nhà đang hoạt động nên chủ yếu ngắm từ bên ngoài, muốn vào trong thường phải theo tour hoặc ghé Bảo tàng-Căn hộ Mendeleev.",
        "presentation_short_vi": "Công trình bề thế nhất còn sót lại từ thời Pyotr Đại đế — dãy mười hai khối nhà gạch đỏ nối liền dài tới hơn 400 m bên bờ Neva, xưa là trụ sở các 'bộ' của đế chế, nay là toà nhà chính của Đại học Tổng hợp Saint Petersburg.",
        "presentation_long_vi": "Chạy vuông góc với dòng Neva trên đảo Vasilievsky là một dãy nhà gạch đỏ ba tầng dài hun hút, nối nhau thành mười hai khối giống hệt tạo cảm giác như một công trình khổng lồ duy nhất — đó là Toà nhà Mười hai Collegia, kiến trúc bề thế nhất còn lại từ thời Pyotr Đại đế ở Saint Petersburg. Được đặt hàng từ năm 1718 và xây dựng trong các năm 1722–1744 theo thiết kế của kiến trúc sư trưởng Domenico Trezzini (cùng Theodor Schwertfeger), toà nhà ra đời để chứa bộ máy chính quyền non trẻ của nước Nga: Viện Nguyên lão (Senat), Thánh Công đồng (Synod) và chín 'collegia' — các cơ quan tương đương bộ ngày nay, phụ trách ngoại giao, quân sự, hải quân, tư pháp, thương mại, khoáng sản… Mỗi khối vốn có mặt tiền và lối vào riêng theo phong cách Baroque thời Pyotr, về sau được thông nối bằng một hành lang chạy dọc suốt tầng hai — nay dài gần 400 m và trở thành chi tiết được nhắc đến nhiều nhất. Khi guồng máy hành chính chuyển sang các bộ và dời đi nơi khác, năm 1835 toà nhà được giao cho Trường Đại học Saint Petersburg; từ đó tới nay đây là toà nhà chính và trụ sở của trường — một trong những đại học lâu đời, danh giá bậc nhất nước Nga, nơi từng gắn với tên tuổi Dmitri Mendeleev, cha đẻ Bảng tuần hoàn các nguyên tố hoá học (căn hộ – bảo tàng tưởng niệm ông vẫn nằm trong khuôn viên). Dù chủ yếu được ngắm nhìn từ bờ kè hay từ dãy phố Mendeleevskaya, toà nhà vẫn là một trang sử sống động về buổi đầu của nước Nga hiện đại.",
        "highlights_vi": [
            "Công trình lớn nhất còn lại từ thời Pyotr Đại đế; xây 1722–1744 theo thiết kế của Domenico Trezzini, gồm 12 khối nhà nối liền dài 400–440 m.",
            "Ban đầu là trụ sở của Viện Nguyên lão, Thánh Công đồng và chín 'collegia' (các bộ) của đế chế Nga.",
            "Từ năm 1835 trở thành toà nhà chính của Đại học Tổng hợp Saint Petersburg; gắn với Mendeleev và Bảng tuần hoàn, hành lang tầng hai dài gần 400 m."
        ],
        "practical": {
            "hours_vi": "Ngắm bên ngoài tự do 24/7; bên trong là trường đại học đang hoạt động, chỉ vào được theo tour đăng ký trước hoặc khi thăm Bảo tàng-Căn hộ Mendeleev (thường mở ban ngày, nghỉ cuối tuần).",
            "ticket_vi": "Ngắm bên ngoài miễn phí; bảo tàng Mendeleev và tour hành lang thu phí nhỏ.",
            "duration_vi": "20–40 phút (lâu hơn nếu vào bảo tàng).",
            "best_time_vi": "Kết hợp dạo bờ kè Đại học cùng Kunstkamera, Cung điện Menshikov và tượng Nhân sư Ai Cập gần đó.",
            "tips_vi": "Gần ga metro Vasileostrovskaya; mặt tiền dài quay ra phố Mendeleevskaya chứ không nhìn ra sông, nên đi sâu vào đảo một chút để thấy trọn chiều dài."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.29861,59.94167&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.94167,30.29861"
        },
        "official_site": None,
        "sources": [
            {"title": "Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Twelve_Collegia"}
        ],
        "tags": ["monument", "architecture", "history", "landmark", "university", "petrine"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-divo-ostrov",
        "slug": "divo-ostrov",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Công viên giải trí Divo Ostrov ('Đảo Kỳ Diệu')",
        "name_ru": "Диво Остров",
        "name_en": "Divo Ostrov Amusement Park",
        "categories": ["other", "park_garden"],
        "coordinates": {"lat": 59.97217, "lon": 30.2549},
        "address_vi": "Phố Kemskaya 1A (ul. Kemskaya, 1A), đảo Krestovsky, trong Công viên Chiến thắng Primorsky, Saint Petersburg",
        "rating": {"value": None, "count": None, "source": "Tripadvisor", "as_of": "2026-07"},
        "review_summary_vi": "Gia đình có trẻ nhỏ và các bạn trẻ mê cảm giác mạnh đều thích Divo Ostrov: công viên giải trí lớn nhất thành phố với đủ loại trò từ nhẹ nhàng tới 'tim đập chân run', lại nằm trong công viên cây xanh mát mẻ ven vịnh. Điểm cộng thường được nhắc: vé vào cổng miễn phí, chỉ trả tiền theo trò chơi, và tầm nhìn thành phố từ vòng đu quay. Điểm trừ: đông và xếp hàng lâu vào cuối tuần mùa hè, giá một số trò khá cao, và công viên chỉ mở theo mùa.",
        "presentation_short_vi": "Công viên giải trí lớn nhất Saint Petersburg, mở cửa năm 2003 trên đảo Krestovsky — thiên đường của tàu lượn siêu tốc, tháp rơi tự do và vòng đu quay khổng lồ ngắm toàn cảnh thành phố, nằm giữa Công viên Chiến thắng Primorsky xanh mát.",
        "presentation_long_vi": "Nằm trong khoảng xanh mát của Công viên Chiến thắng Primorsky trên đảo Krestovsky, Divo Ostrov — dịch nôm na là 'Đảo Kỳ Diệu' — là công viên giải trí lớn nhất và nhộn nhịp nhất Saint Petersburg. Mở cửa ngày 4 tháng 6 năm 2003, đây là điểm đến hiện đại tương đối trẻ so với vô số cung điện và bảo tàng cổ kính của thành phố, nhưng nhanh chóng trở thành nơi vui chơi quen thuộc của các gia đình lẫn giới trẻ. Công viên chia thành nhiều khu: khu dành cho trẻ nhỏ với đu quay ngựa gỗ, xe điện đụng và những trò nhẹ nhàng; khu cảm giác mạnh với các tàu lượn siêu tốc uốn lượn, tháp rơi tự do, trò 'phóng' bật người lên cao và máng trượt nước; điểm nhấn là vòng đu quay khổng lồ, từ trên cao có thể phóng tầm mắt ra sân vận động Gazprom Arena, vịnh Phần Lan và những mái vòm xa xa của thành phố. Vé vào cổng thường miễn phí, du khách chỉ trả tiền theo từng trò hoặc mua vé trọn gói cả ngày. Do khí hậu phương Bắc, công viên chỉ hoạt động theo mùa, thường từ giữa tháng Tư đến giữa tháng Mười. Kết hợp cùng sân Gazprom Arena, Công viên 300 năm Saint Petersburg và những lối dạo ven vịnh, Divo Ostrov mang lại một mảng trải nghiệm rất khác: năng động, hiện đại và đầy tiếng cười, cân bằng với vẻ trầm mặc cổ điển thường thấy ở cố đô.",
        "highlights_vi": [
            "Công viên giải trí lớn nhất Saint Petersburg, khai trương ngày 4/6/2003 trên đảo Krestovsky.",
            "Đủ loại trò chơi từ khu thiếu nhi tới tàu lượn siêu tốc, tháp rơi tự do và vòng đu quay ngắm toàn cảnh thành phố cùng vịnh Phần Lan.",
            "Vào cổng miễn phí, trả tiền theo trò; chỉ mở theo mùa (thường giữa tháng Tư đến giữa tháng Mười) do khí hậu phương Bắc."
        ],
        "practical": {
            "hours_vi": "Hoạt động theo mùa, khoảng giữa tháng Tư đến giữa tháng Mười; giờ mở thay đổi theo mùa, thường từ 11:00 đến khoảng 21:00–22:00 (cuối tuần mùa hè mở lâu hơn).",
            "ticket_vi": "Vào cổng miễn phí; trả tiền theo từng trò chơi hoặc mua vé trọn gói cả ngày — xem giá cập nhật trên trang chính thức.",
            "duration_vi": "Nửa ngày (2–4 giờ), lâu hơn nếu đi cùng trẻ nhỏ.",
            "best_time_vi": "Ngày hè nắng ráo; nên đi sớm hoặc ngày thường để tránh xếp hàng lâu.",
            "tips_vi": "Gần ga metro Krestovsky Ostrov và sân Gazprom Arena; kiểm tra lịch mở cửa theo mùa trước khi đến; nhiều trò có giới hạn chiều cao/độ tuổi."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.2549,59.97217&z=16&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.97217,30.2549"
        },
        "official_site": "https://www.divo-ostrov.ru",
        "sources": [
            {"title": "Trang chính thức Divo Ostrov", "url": "https://www.divo-ostrov.ru"},
            {"title": "Wikidata", "url": "https://www.wikidata.org/wiki/Q4161277"}
        ],
        "tags": ["amusement-park", "family", "outdoor", "modern", "entertainment", "krestovsky"],
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
