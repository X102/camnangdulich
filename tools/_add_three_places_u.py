# -*- coding: utf-8 -*-
"""_add_three_places_u.py — Bổ sung 3 địa điểm nổi tiếng còn thiếu.
Moscow: Trung tâm Triển lãm Manezh (nguyên Nhà tập cưỡi ngựa Hoàng gia).
Saint Petersburg: Nghĩa trang Bậc thầy Nghệ thuật (Nghĩa trang Tikhvin) - Bảo tàng Điêu khắc Đô thị.
Kazan (Tatarstan): Khu phố Tatar Cổ (Staro-Tatarskaya Sloboda) - Nhà thờ Hồi giáo Al-Marjani & hồ Kaban.
Nội dung tiếng Việt nguyên gốc; toạ độ & dữ kiện đã kiểm chứng qua nguồn ghi trong 'sources'.
Chạy: python3 tools/_add_three_places_u.py
"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TODAY = "2026-07-26"
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

NEW = [
    {
        "id": "moscow-manege-exhibition-hall",
        "slug": "manege-exhibition-hall",
        "region": "moscow",
        "region_name_vi": "Moskva",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Trung tâm Triển lãm Manezh (Ma-nhe-giơ) – nguyên là Nhà tập cưỡi ngựa Hoàng gia",
        "name_ru": "Центральный выставочный зал «Манеж»",
        "name_en": "Manege Central Exhibition Hall",
        "categories": ["monument"],
        "coordinates": {"lat": 55.7535, "lon": 37.6125},
        "address_vi": "Quảng trường Manezhnaya (Manezhnaya ploshchad) 1, Moskva; sát Vườn Alexander và Kremlin, gần ga metro Okhotny Ryad / Aleksandrovsky Sad / Biblioteka imeni Lenina",
        "rating": None,
        "review_summary_vi": """Du khách nhận xét đây là điểm triển lãm ngay giữa trung tâm, chỉ cách Quảng trường Đỏ và Vườn Alexander vài bước chân, với không gian rộng và sáng. Vì nội dung trưng bày thay đổi liên tục nên trải nghiệm phụ thuộc vào triển lãm đang diễn ra; một số người lưu ý rằng bên trong đã được hiện đại hóa sau vụ cháy năm 2004 nên không còn giữ hệ mái gỗ nguyên bản.""",
        "presentation_short_vi": """Tòa nhà tân cổ điển màu vàng nhạt bề thế ngay sát tường Kremlin, khởi công năm 1817 để mừng 5 năm chiến thắng Napoleon. Nổi tiếng nhờ hệ vì kèo gỗ vượt nhịp khoảng 45 m không cần cột đỡ ở giữa; nay là một trong những không gian triển lãm - sự kiện nghệ thuật quan trọng nhất trung tâm Moskva.""",
        "presentation_long_vi": """Ngay bên Vườn Alexander và tường thành Kremlin, tòa nhà dài màu vàng nhạt này là một trong những công trình tân cổ điển bề thế nhất Moskva. Manezh được khởi công năm 1817 để kỷ niệm tròn 5 năm chiến thắng quân Napoleon trong Chiến tranh Vệ quốc 1812. Kỹ sư người Tây Ban Nha Agustín de Betancourt đã thiết kế một hệ vì kèo gỗ vượt nhịp khoảng 45 mét mà không cần một chiếc cột đỡ nào ở giữa — kỳ tích kỹ thuật thời đó, đủ rộng để cả một trung đoàn bộ binh diễn tập bên trong. Ít năm sau, kiến trúc sư Osip Bové khoác cho công trình lớp mặt tiền tân cổ điển trang nhã còn thấy đến ngày nay. Ban đầu đây là nơi huấn luyện kỵ binh và duyệt binh trong nhà (manège nghĩa là trường cưỡi ngựa); từ thập niên 1830, tòa nhà bắt đầu được dùng cho hòa nhạc, hội chợ và triển lãm. Tháng 3 năm 2004, một trận hỏa hoạn lớn đã thiêu rụi toàn bộ phần mái gỗ lịch sử cùng nội thất và khiến hai lính cứu hỏa thiệt mạng. Chỉ trong chưa đầy một năm, Manezh được phục dựng và mở cửa trở lại vào tháng 2 năm 2005. Ngày nay đây là một trong những không gian triển lãm và sự kiện nghệ thuật hàng đầu ở lõi trung tâm thủ đô, nằm cạnh Quảng trường Đỏ và Quảng trường Manezhnaya sầm uất.""",
        "highlights_vi": [
            "Khởi công năm 1817 mừng 5 năm chiến thắng Napoleon; hệ vì kèo gỗ vượt nhịp khoảng 45 m không cột của kỹ sư Agustín de Betancourt là kỳ tích kỹ thuật đương thời.",
            "Mặt tiền tân cổ điển do kiến trúc sư Osip Bové thực hiện; khoảng trống bên trong rộng đến mức cả một trung đoàn bộ binh có thể diễn tập.",
            "Bị hỏa hoạn tàn phá tháng 3/2004 (hai lính cứu hỏa hy sinh) rồi được phục dựng, mở lại tháng 2/2005; nay là trung tâm triển lãm - sự kiện lớn cạnh Quảng trường Đỏ."
        ],
        "practical": {
            "hours_vi": "Mở cửa theo lịch từng triển lãm, thường khoảng 12:00–22:00 và có thể tạm đóng giữa hai kỳ trưng bày; nên kiểm tra chương trình trước khi đến.",
            "ticket_vi": "Giá vé tùy theo triển lãm đang diễn ra; một số sự kiện vào cửa miễn phí.",
            "duration_vi": "Khoảng 1–2 giờ tùy triển lãm.",
            "best_time_vi": "Kết hợp khi tham quan Quảng trường Đỏ, Vườn Alexander và Quảng trường Manezhnaya.",
            "tips_vi": "Ngay các ga metro Okhotny Ryad / Aleksandrovsky Sad / Biblioteka imeni Lenina. Tra cứu triển lãm hiện hành để chọn đúng chủ đề yêu thích."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=37.6125,55.7535&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=55.7535,37.6125"
        },
        "official_site": None,
        "sources": [
            {"title": "Manege Central Exhibition Hall — Rusmania", "url": "https://rusmania.com/central/moscow-federal-city/moscow/central-moscow/around-manezhnaya-ploschad/manege-central-exhibition-hall"},
            {"title": "Who burned Moscow's main exhibition hall? — Russia Beyond", "url": "https://www.rbth.com/history/329666-who-burned-moscows-main-exhibition"},
            {"title": "Manege Central Exhibition Hall — DiscoverMoscow", "url": "https://discovermoscow.com/en/places/dostoprimechatelnosti/centralnyj-vystavochnyj-zal-manezh/"}
        ],
        "tags": ["architecture", "exhibition", "landmark", "neoclassical", "city-center"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-necropolis-masters-of-arts",
        "slug": "necropolis-masters-of-arts",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Nghĩa trang Bậc thầy Nghệ thuật (Nghĩa trang Tikhvin) – Bảo tàng Điêu khắc Đô thị",
        "name_ru": "Некрополь мастеров искусств (Тихвинское кладбище)",
        "name_en": "Necropolis of Masters of Arts (Tikhvin Cemetery)",
        "categories": ["monument", "museum"],
        "coordinates": {"lat": 59.9215, "lon": 30.3861},
        "address_vi": "Trong Tu viện Aleksandr Nevsky, bên Quảng trường Aleksandr Nevsky, Saint Petersburg; ga metro Ploshchad Aleksandra Nevskogo",
        "rating": None,
        "review_summary_vi": """Du khách yêu nhạc cổ điển và văn học Nga xem đây là điểm 'phải đến' để viếng mộ các thần tượng và ngắm những bia mộ - tượng đài tinh xảo. Không gian yên tĩnh, nhiều cây xanh, tách khỏi sự ồn ào của đại lộ Nevsky. Một số người thấy vé vào hơi cao so với diện tích và khuyên nên có sơ đồ hoặc hướng dẫn để tìm đúng các ngôi mộ nổi tiếng.""",
        "presentation_short_vi": """Nằm ngay bên trong cổng Tu viện Aleksandr Nevsky, nghĩa trang mở năm 1823 này là nơi yên nghỉ của nhiều tên tuổi lớn của văn hóa Nga: văn hào Dostoevsky và các nhà soạn nhạc Tchaikovsky, Glinka, Mussorgsky, Borodin, Rimsky-Korsakov. Mỗi bia mộ là một tác phẩm điêu khắc, biến chuyến viếng thăm thành cả một buổi thưởng lãm nghệ thuật.""",
        "presentation_long_vi": """Nằm ngay bên trong cổng Tu viện Aleksandr Nevsky, Nghĩa trang Tikhvin - nay mang tên 'Nghĩa trang của các Bậc thầy Nghệ thuật' - là nơi an nghỉ của rất nhiều tên tuổi lớn trong văn hóa Nga. Nghĩa trang được mở năm 1823 khi khu mộ cổ Lazarevskoe kế bên đã quá chật, rồi dần trở thành nơi chôn cất danh giá bậc nhất kinh đô. Tại đây có mộ của văn hào Fyodor Dostoevsky, của các nhà soạn nhạc lừng danh như Pyotr Tchaikovsky, Mikhail Glinka, Modest Mussorgsky, Alexander Borodin và Nikolai Rimsky-Korsakov - gần như trọn vẹn nhóm 'Khỏe khoắn' (Moguchaya Kuchka) - cùng các họa sĩ Ivan Kramskoy, Ivan Shishkin, kiến trúc sư Carlo Rossi và biên đạo múa Marius Petipa. Vào thập niên 1930, chính quyền Xô-viết cải tạo nghĩa trang thành một 'bảo tàng ngoài trời': nhiều ngôi mộ của giới nghệ sĩ được quy tập từ các nghĩa trang khác về đây, trong khi những phần mộ không thuộc chủ đề nghệ thuật bị di dời. Từ năm 1932, nơi này thuộc Bảo tàng Điêu khắc Đô thị Quốc gia và được tổ chức như một công viên tưởng niệm, với các lối đi chuyên đề - 'lối của các nhà soạn nhạc' ở phía bắc, khu họa sĩ - điêu khắc ở phía tây. Mỗi tấm bia là một tác phẩm điêu khắc, khiến chuyến viếng thăm vừa là hành trình tưởng niệm, vừa là buổi thưởng lãm nghệ thuật tang chế Nga. Lưu ý: đây là bảo tàng có bán vé, tách biệt với khu tu viện đang hoạt động ngay cạnh.""",
        "highlights_vi": [
            "Mở năm 1823; nơi an nghỉ của Dostoevsky, Tchaikovsky, Glinka, Mussorgsky, Borodin, Rimsky-Korsakov, họa sĩ Kramskoy và Shishkin, kiến trúc sư Rossi, biên đạo Petipa.",
            "Thập niên 1930 được cải tạo thành 'Nghĩa trang của các Bậc thầy Nghệ thuật' - nhiều mộ nghệ sĩ được quy tập từ các nghĩa trang khác trong thành phố về đây.",
            "Thuộc Bảo tàng Điêu khắc Đô thị Quốc gia từ năm 1932; mỗi phần mộ là một tác phẩm điêu khắc - bảo tàng có vé, tách biệt với tu viện đang hoạt động."
        ],
        "practical": {
            "hours_vi": "Thường mở cửa hằng ngày khoảng 9:30–18:00 (mùa đông có thể ngắn hơn); nên kiểm tra lịch của bảo tàng trước khi đến.",
            "ticket_vi": "Có bán vé vào (vé riêng cho Nghĩa trang Bậc thầy Nghệ thuật và Nghĩa trang thế kỷ 18 kế bên); học sinh - sinh viên, trẻ em thường có ưu đãi.",
            "duration_vi": "Khoảng 45 phút–1 giờ.",
            "best_time_vi": "Ban ngày; cuối xuân đến đầu thu khi cây xanh tươi tốt.",
            "tips_vi": "Vào từ Quảng trường Aleksandr Nevsky (ga metro Ploshchad Aleksandra Nevskogo). Xin sơ đồ tại quầy vé để dễ tìm mộ Dostoevsky, Tchaikovsky; kết hợp thăm Tu viện Aleksandr Nevsky ngay cạnh."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.3861,59.9215&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.9215,30.3861"
        },
        "official_site": None,
        "sources": [
            {"title": "Tikhvin Cemetery — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Tikhvin_Cemetery"},
            {"title": "Cemetery and Tombs of the Alexander Nevsky Monastery — Saint-Petersburg.com", "url": "http://www.saint-petersburg.com/cemeteries/cemetery-and-tombs-of-the-alexander-nevsky-monastery/"},
            {"title": "Necropolis of the St. Alexander Nevsky Lavra — lavraspb.ru", "url": "https://lavraspb.ru/en"}
        ],
        "tags": ["necropolis", "cemetery", "composers", "dostoevsky", "tchaikovsky", "museum", "history"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "tatarstan-old-tatar-sloboda",
        "slug": "old-tatar-sloboda",
        "region": "tatarstan",
        "region_name_vi": "Cộng hoà Tatarstan",
        "federal_district": "Vùng Volga",
        "name_vi": "Khu phố Tatar Cổ (Staro-Tatarskaya Sloboda) – Nhà thờ Hồi giáo Al-Marjani & hồ Kaban",
        "name_ru": "Старо-Татарская слобода",
        "name_en": "Old Tatar Settlement (Staro-Tatarskaya Sloboda)",
        "categories": ["square_street"],
        "coordinates": {"lat": 55.7797, "lon": 49.1175},
        "address_vi": "Dọc phố đi bộ Kayum Nasyri và bờ hồ Nizhny Kaban, phía nam Điện Kremlin Kazan, thành phố Kazan, Cộng hoà Tatarstan",
        "rating": None,
        "review_summary_vi": """Du khách thích không khí yên bình, đầy màu sắc của khu phố với những ngôi nhà gỗ sơn màu và các thánh đường Hồi giáo; nhiều người khen đây là nơi tốt nhất để tìm hiểu văn hóa, ẩm thực Tatar và chụp ảnh bên hồ Kaban. Một số ý kiến cho rằng vài đoạn phố đã được tu sửa mới nên hơi 'du lịch hóa', nhưng tổng thể vẫn rất đáng để tản bộ thong thả.""",
        "presentation_short_vi": """Khu phố lịch sử của người Tatar trải dọc bờ hồ Kaban, phía nam Điện Kremlin Kazan. Hình thành sau năm 1552, đây là trái tim văn hóa Tatar với Nhà thờ Hồi giáo Al-Marjani (1766–1770) - đền Hồi giáo bằng đá đầu tiên của Kazan - cùng phố đi bộ Kayum Nasyri và những dãy nhà gỗ, dinh thự thương nhân cổ.""",
        "presentation_long_vi": """Trải dọc bờ hồ Kaban ở phía nam Điện Kremlin Kazan, Khu phố Tatar Cổ là trái tim của văn hóa Tatar trong lòng thành phố. Khu định cư này hình thành sau năm 1552, khi Sa hoàng Ivan Bạo chúa chiếm Kazan và người Tatar theo đạo Hồi bị dời ra sống bên ngoài thành, phía bên kia hồ Kaban. Trong hơn hai thế kỷ, cư dân bị hạn chế xây dựng, cho tới khi Nữ hoàng Ekaterina II (Catherine Đại đế) ghé thăm năm 1767 và cho phép dựng nhà thờ Hồi giáo bằng đá. Nhờ đó, Nhà thờ Hồi giáo Al-Marjani ra đời trong các năm 1766–1770 bằng tiền quyên góp của dân làng - ngôi đền Hồi giáo bằng đá đầu tiên ở Kazan sau năm 1552, và là nhà thờ Hồi giáo duy nhất trong thành phố không bị đóng cửa suốt thời Xô-viết. Tên gọi Al-Marjani nhằm tôn vinh nhà thần học kiêm sử gia Şihabetdin Marcani từng hành đạo tại đây vào thế kỷ 19. Khu phố được tổ chức theo các 'mahalla' - mỗi cộng đồng có một nhà thờ, trường madrasah và nhà ở quây quần; đến nay vẫn còn nhiều nhà gỗ, dinh thự thương nhân cổ và các thánh đường khác như Apanaev, Nurulla. Con phố đi bộ Kayum Nasyri cùng bờ kè hồ Kaban được chỉnh trang khang trang là nơi lý tưởng để tản bộ, thưởng thức ẩm thực Tatar và cảm nhận nhịp sống truyền thống của xứ sở này.""",
        "highlights_vi": [
            "Hình thành sau năm 1552 khi người Tatar Hồi giáo bị dời ra sống bên kia hồ Kaban; là khu bảo tồn văn hóa Tatar tiêu biểu của Kazan.",
            "Nhà thờ Hồi giáo Al-Marjani (1766–1770) - đền Hồi giáo bằng đá đầu tiên ở Kazan sau năm 1552, dựng sau chuyến thăm năm 1767 của Ekaterina II; mở cửa suốt thời Xô-viết.",
            "Phố đi bộ Kayum Nasyri và bờ kè hồ Kaban được chỉnh trang đẹp; còn nhiều nhà gỗ, dinh thự thương nhân và các thánh đường Apanaev, Nurulla."
        ],
        "practical": {
            "hours_vi": "Khu phố ngoài trời, dạo bộ tự do suốt cả ngày; các nhà thờ Hồi giáo và bảo tàng nhỏ mở theo giờ riêng (lưu ý giờ cầu nguyện).",
            "ticket_vi": "Đi dạo trong khu phố miễn phí; vào bên trong một số nhà thờ/bảo tàng có thể cần trang phục phù hợp hoặc phí nhỏ.",
            "duration_vi": "Khoảng 1,5–3 giờ.",
            "best_time_vi": "Cuối xuân đến đầu thu; chiều muộn để tản bộ và ngắm hoàng hôn bên hồ Kaban.",
            "tips_vi": "Từ Điện Kremlin Kazan hoặc phố Bauman đi bộ hoặc taxi tới; nữ giới nên mang khăn choàng khi vào thánh đường. Kết hợp thử các món Tatar như echpochmak, chak-chak."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=49.1175,55.7797&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=55.7797,49.1175"
        },
        "official_site": None,
        "sources": [
            {"title": "Old Tatar Settlement (Staro-Tatarskaya Sloboda) — Advantour", "url": "https://www.advantour.com/russia/kazan/staro-tatarskaya-sloboda.htm"},
            {"title": "Märcani Mosque, Kazan — Advantour", "url": "https://www.advantour.com/russia/kazan/marcani-mosque.htm"},
            {"title": "Märcani Mosque — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/M%C3%A4rcani_Mosque"}
        ],
        "tags": ["tatar-culture", "historic-district", "mosque", "lake", "pedestrian", "kazan"],
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
