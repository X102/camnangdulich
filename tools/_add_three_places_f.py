# -*- coding: utf-8 -*-
"""_add_three_places_f.py — Bổ sung 3 địa điểm nổi tiếng/hiện đại còn thiếu.
- Saint Petersburg: Tàu điện ngầm SPb (Avtovo & các ga sâu) ; Bảo tàng Nghệ thuật Đường phố
- Moskva: Bảo tàng Lịch sử Gulag
Nội dung tiếng Việt nguyên gốc; toạ độ & dữ kiện đã kiểm chứng qua nguồn (xem 'sources').
Chạy: python3 tools/_add_three_places_f.py
"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REG = os.path.join(ROOT, "data", "regions")
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-25"

def maps_for(lat, lon):
    return {
        "yandex": f"https://yandex.com/maps/?pt={lon},{lat}&z=17&l=map",
        "google": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
    }

# ---------------- RECORDS ----------------
spb_metro = {
    "id": "saint-petersburg-metro",
    "slug": "metro",
    "region": "saint-petersburg",
    "region_name_vi": "Saint Petersburg",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Tàu điện ngầm Saint Petersburg (ga Avtovo & các ga sâu, lộng lẫy)",
    "name_ru": "Петербургский метрополитен",
    "name_en": "Saint Petersburg Metro",
    "categories": ["monument"],
    "coordinates": {"lat": 59.86732, "lon": 30.26135},
    "address_vi": "Ga Avtovo (tuyến 1 — Kirovsko–Vyborgskaya), Quận Kirovsky, Saint Petersburg",
    "rating": None,
    "presentation_short_vi": "Metro Saint Petersburg không chỉ để đi lại mà còn là điểm tham quan: nhiều ga xây như 'cung điện dưới lòng đất' với đá hoa cương, tranh khảm và đèn chùm. Ga Avtovo với hàng cột ốp thủy tinh đúc từng lọt top ga đẹp nhất thế giới, còn Admiralteyskaya là ga sâu nhất nước Nga.",
    "presentation_long_vi": "Vì Saint Petersburg dựng trên nền đất đầm lầy, metro của thành phố phải đào rất sâu — và người ta đã biến những đường hầm ấy thành các 'cung điện dưới lòng đất'. Khai trương ngày 15/11/1955 với tuyến đầu tiên, hệ thống nay có nhiều ga trang trí công phu bằng đá hoa cương, tranh khảm, phù điêu đồng và đèn chùm. Toạ độ ở đây đặt tại Avtovo — ga nổi tiếng nhất: mái vòm được đỡ bởi hàng cột mà nhiều cột được ốp thủy tinh đúc lấp lánh từ nhà máy Lomonosov thay cho đá cẩm thạch, tạo hiệu ứng như pha lê. Năm 2014, báo The Guardian xếp Avtovo vào danh sách 12 ga metro đẹp nhất thế giới. Đừng bỏ lỡ Admiralteyskaya — ga sâu nhất nước Nga, nằm ở độ sâu khoảng 86 m và tiếp cận bằng một trong những thang cuốn dài nhất thế giới (khoảng 137 m); cùng các ga Kirovsky Zavod, Pushkinskaya hay Ploshchad Vosstaniya cũng rất đáng ngắm. Chỉ với giá đúng một lượt đi tàu, bạn được chiêm ngưỡng tất cả. Lưu ý biển chỉ dẫn chủ yếu bằng tiếng Nga (Cyrillic); nên tránh giờ cao điểm để dễ tham quan và chụp ảnh.",
    "highlights_vi": [
        "Ga Avtovo (mở năm 1955) có các cột ốp thủy tinh đúc từ nhà máy Lomonosov; năm 2014 được The Guardian xếp vào 12 ga metro đẹp nhất thế giới.",
        "Ga Admiralteyskaya sâu khoảng 86 m — sâu nhất nước Nga — do thành phố nằm trên nền đầm lầy phải đào sâu; thang cuốn dài tới khoảng 137 m.",
        "Chỉ trả đúng giá một lượt metro là có thể tham quan hàng loạt ga được trang trí như cung điện ngầm.",
    ],
    "practical": {
        "hours_vi": "Metro chạy hằng ngày khoảng 05:30–24:00 (một số ga/lối lên đóng sớm hơn).",
        "ticket_vi": "Chỉ giá vé metro thường cho mỗi lượt: dùng token (zheton) hoặc thẻ Podorozhnik; không thu phí tham quan riêng.",
        "duration_vi": "1–2 giờ để đi qua các ga đẹp nhất.",
        "best_time_vi": "Ngoài giờ cao điểm (giữa buổi sáng hoặc đầu chiều) để dễ chụp ảnh.",
        "tips_vi": "Ghi sẵn tên ga bằng Cyrillic; giữ token/thẻ khi đổi tuyến; tránh khung 8–10h và 17–19h đông đúc.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(59.86732, 30.26135),
    "official_site": "https://metro.spb.ru",
    "sources": [
        {"title": "Wikipedia (EN) — Avtovo (Saint Petersburg Metro)", "url": "https://en.wikipedia.org/wiki/Avtovo_(Saint_Petersburg_Metro)"},
        {"title": "Russia Beyond — Deepest subway station: Admiralteyskaya", "url": "https://www.gw2ru.com/science-and-tech/234517-deepest-subway-russia-admiralteyskaya"},
        {"title": "Russia Beyond — Most unusual stations of the St. Petersburg Metro", "url": "https://www.gw2ru.com/travel/3280-petersburg-metro-unusual-stations"},
    ],
    "tags": ["architecture", "landmark", "cheap", "indoor", "top"],
    "status": "enriched",
    "last_updated": TODAY,
}

spb_streetart = {
    "id": "saint-petersburg-street-art-museum",
    "slug": "street-art-museum",
    "region": "saint-petersburg",
    "region_name_vi": "Saint Petersburg",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Bảo tàng Nghệ thuật Đường phố (Muzey Ulichnogo Iskusstva)",
    "name_ru": "Музей стрит-арта",
    "name_en": "Street Art Museum",
    "categories": ["museum"],
    "coordinates": {"lat": 59.9612, "lon": 30.4529},
    "address_vi": "Shosse Revolyutsii 84, Saint Petersburg (lối vào từ Industrialny Prospekt); nằm trong khuôn viên một nhà máy nhựa lá đang hoạt động",
    "rating": None,
    "presentation_short_vi": "Một bảo tàng nghệ thuật đương đại độc đáo nằm ngay trong khuôn viên nhà máy sản xuất nhựa lá vẫn đang vận hành ở phía đông Saint Petersburg. Ra đời năm 2012, nơi đây trưng bày những bức tường graffiti, tác phẩm khổ lớn và street-art của nghệ sĩ trong và ngoài nước.",
    "presentation_long_vi": "Nếu đã 'bội thực' cung điện và nhà thờ baroque, Bảo tàng Nghệ thuật Đường phố là làn gió hoàn toàn khác của Saint Petersburg. Bảo tàng hình thành năm 2012 sau một buổi 'tiệc graffiti' trong xưởng bỏ hoang của một nhà máy sản xuất nhựa lá (laminated plastics) ở phía đông thành phố — và điều đặc biệt là nhà máy đến nay vẫn hoạt động. Không gian chia làm hai phần: khu trưng bày thường trực nằm trong khuôn viên sản xuất, nơi các bức tường xưởng, bồn chứa và ống khói trở thành nền cho những tác phẩm khổ lớn; và khu triển lãm công cộng dành cho các dự án theo mùa, thường xoay quanh một chủ đề xã hội. Bộ sưu tập quy tụ tác phẩm của nhiều nghệ sĩ street-art đương đại Nga và quốc tế, thường được tham quan theo tour có hướng dẫn để hiểu bối cảnh mỗi bức vẽ. Đây là điểm đến hợp với người mê nghệ thuật đương đại, nhiếp ảnh và văn hóa đô thị. Lưu ý bảo tàng nằm xa trung tâm và chủ yếu mở theo mùa ấm, có nhiều khu ngoài trời, nên hãy kiểm tra lịch mở cửa và sự kiện trên trang chính thức trước khi đến.",
    "highlights_vi": [
        "Ra đời năm 2012 từ một buổi 'tiệc graffiti' trong xưởng bỏ hoang; nằm ngay trong nhà máy nhựa lá vẫn đang hoạt động.",
        "Kết hợp khu trưng bày thường trực trong khuôn viên sản xuất và khu triển lãm công cộng theo chủ đề, đổi mới theo mùa.",
        "Quy tụ tác phẩm của nhiều nghệ sĩ street-art Nga và quốc tế; nên tham quan theo tour có hướng dẫn.",
    ],
    "practical": {
        "hours_vi": "Chủ yếu mở theo mùa (khoảng mùa xuân–thu); ngày giờ thay đổi theo triển lãm — nên xem lịch trên web chính thức.",
        "ticket_vi": "Có vé vào cửa/tour có hướng dẫn, giá thay đổi theo chương trình (kiểm tra trên web).",
        "duration_vi": "1,5–2,5 giờ.",
        "best_time_vi": "Ngày nắng ấm; cuối tuần thường có tour và sự kiện.",
        "tips_vi": "Xa trung tâm — đi metro tới ga Ladozhskaya rồi bắt xe buýt/taxi; nhiều khu ngoài trời nên mặc thoải mái; đặt tour trước nếu muốn có hướng dẫn.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(59.9612, 30.4529),
    "official_site": "https://streetartmuseum.ru",
    "sources": [
        {"title": "Street Art Museum — trang chính thức (EN)", "url": "https://streetartmuseum.ru/english/"},
        {"title": "Lonely Planet — Street Art Museum", "url": "https://www.lonelyplanet.com/points-of-interest/street-art-museum/1491565"},
        {"title": "In Your Pocket — Street Art Museum", "url": "https://www.inyourpocket.com/st-petersburg-en/street-art-museum_144939v"},
    ],
    "tags": ["modern", "art", "indoor", "offbeat"],
    "status": "enriched",
    "last_updated": TODAY,
}

moscow_gulag = {
    "id": "moscow-gulag-history-museum",
    "slug": "gulag-history-museum",
    "region": "moscow",
    "region_name_vi": "Moskva",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Bảo tàng Lịch sử Gulag (Muzey Istorii GULAGa)",
    "name_ru": "Музей истории ГУЛАГа",
    "name_en": "Gulag History Museum",
    "categories": ["museum"],
    "coordinates": {"lat": 55.777097, "lon": 37.611485},
    "address_vi": "1-y Samotyochny Pereulok 9, kor. 1, Moskva (gần ga metro Dostoevskaya / Novoslobodskaya)",
    "rating": None,
    "presentation_short_vi": "Bảo tàng nhà nước tưởng niệm và tái hiện lịch sử hệ thống trại lao động cưỡng bức Gulag thời Xô-viết. Thành lập năm 2001 và chuyển tới toà nhà mới rộng hơn năm 2015, nơi đây lưu giữ hiện vật gốc, bản đồ mạng lưới trại và câu chuyện cá nhân của các nạn nhân bị đàn áp chính trị.",
    "presentation_long_vi": "Đây là một trong những bảo tàng gợi nhiều suy ngẫm nhất Moskva. 'GULAG' là tên viết tắt của cơ quan quản lý hệ thống trại lao động cưỡng bức thời Liên Xô, nơi hàng triệu người — trong đó có rất nhiều nạn nhân bị đàn áp chính trị — từng bị giam giữ. Bảo tàng ra đời năm 2001, ban đầu nằm trên phố Petrovka ở trung tâm; đến ngày 30/10/2015, đúng Ngày Tưởng niệm các nạn nhân bị đàn áp chính trị, bảo tàng mở cửa trở lại tại một toà nhà đầu thế kỷ 20 rộng hơn, được kiến trúc sư cải tạo lại. Trưng bày kết hợp hiện vật gốc từ các trại (như cánh cửa xà lim, vật dụng cá nhân của tù nhân), bản đồ lớn cho thấy mạng lưới trại trải khắp Liên Xô, cùng màn hình tương tác, phim tài liệu ngắn và lời kể của những người sống sót. Trong khuôn viên còn có một khu vườn tưởng niệm. Bảo tàng đặt trọng tâm vào ký ức và giáo dục lịch sử hơn là giải trí, nên phù hợp với du khách quan tâm tới lịch sử thế kỷ 20 của nước Nga. Không gian có thể nặng nề về cảm xúc; hãy dành đủ thời gian và cân nhắc khi đi cùng trẻ nhỏ.",
    "highlights_vi": [
        "Thành lập năm 2001; mở cửa lại tại toà nhà mới rộng hơn đúng Ngày Tưởng niệm nạn nhân bị đàn áp chính trị (30/10/2015).",
        "Trưng bày hiện vật gốc từ các trại, bản đồ mạng lưới trại khắp Liên Xô, màn hình tương tác và lời kể của người sống sót.",
        "Trong khuôn viên có vườn tưởng niệm; bảo tàng thiên về ký ức và giáo dục lịch sử.",
    ],
    "practical": {
        "hours_vi": "11:00–19:00; thứ Năm 12:00–21:00. Đóng cửa thứ Hai và ngày thứ Sáu cuối cùng của tháng.",
        "ticket_vi": "Vé khoảng 300 RUB (2026); thường miễn phí vào Chủ nhật cuối tháng — nên kiểm tra lại trên web.",
        "duration_vi": "1,5–2 giờ.",
        "best_time_vi": "Buổi sáng giữa tuần cho không gian yên tĩnh; nên dùng hướng dẫn viên hoặc audio guide.",
        "tips_vi": "Gần ga metro Dostoevskaya và Novoslobodskaya; nội dung có thể nặng nề về cảm xúc — cân nhắc khi đi cùng trẻ nhỏ; xem lịch triển lãm tạm thời trên web.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(55.777097, 37.611485),
    "official_site": "https://gmig.ru",
    "sources": [
        {"title": "Museums Association — International opening: Gulag History Museum, Moscow", "url": "https://www.museumsassociation.org/museums-journal/features/2016/03/01042016-international-opening-gulag-history-museum-moscow/"},
        {"title": "Russia Beyond — Gulag Museum in Moscow gets new building", "url": "https://www.rbth.com/arts/2015/11/05/gulag-museum-in-moscow-gets-new-building_537307"},
        {"title": "Rusmania — Gulag Museum", "url": "https://rusmania.com/central/moscow-federal-city/moscow/meschansky/beyond-the-garden-ring-around-suvorovskaya-ploschad/gulag-museum"},
    ],
    "tags": ["museum", "history", "indoor", "modern"],
    "status": "enriched",
    "last_updated": TODAY,
}

PLAN = {
    "saint-petersburg": [spb_metro, spb_streetart],
    "moscow": [moscow_gulag],
}

def main():
    for region, recs in PLAN.items():
        path = os.path.join(REG, f"{region}.json")
        arr = json.load(open(path, encoding="utf-8"))
        have_ids = {r.get("id") for r in arr}
        have_slugs = {r.get("slug") for r in arr}
        # backup once per region before writing
        bak = f"{path}.bak_add_{STAMP}"
        json.dump(arr, open(bak, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        added = []
        for rec in recs:
            if rec["id"] in have_ids or rec["slug"] in have_slugs:
                print(f"  = BỎ QUA (đã tồn tại): {rec['id']}")
                continue
            arr.append(rec)
            added.append(rec["id"])
        json.dump(arr, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"[{region}] +{len(added)} bản ghi: {added} -> tổng {len(arr)} (backup: {os.path.basename(bak)})")

if __name__ == "__main__":
    main()
