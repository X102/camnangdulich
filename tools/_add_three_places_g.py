# -*- coding: utf-8 -*-
"""Bổ sung 3 địa điểm nổi tiếng còn thiếu vào CSDL Cẩm nang Du lịch Nga.
Chạy: python3 add_places_g.py  (thao tác trực tiếp trên data/regions/*.json)"""
import json, os, datetime, sys

ROOT = "/sessions/zealous-clever-tesla/mnt/russia-tourism"
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def maps_for(lat, lon):
    return {
        "yandex": f"https://yandex.com/maps/?pt={lon},{lat}&z=17&l=map",
        "google": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
    }


RECORDS = {
    "moscow": {
        "id": "moscow-tolstoy-khamovniki-estate",
        "slug": "tolstoy-khamovniki-estate",
        "region": "moscow",
        "region_name_vi": "Moskva",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Bảo tàng – Điền trang L.N. Tolstoy ở Khamovniki (Tôn-xtôi, Kha-mốp-ni-ki)",
        "name_ru": "Музей-усадьба Л. Н. Толстого «Хамовники»",
        "name_en": "Leo Tolstoy Estate Museum in Khamovniki",
        "categories": ["museum"],
        "coordinates": {"lat": 55.734202, "lon": 37.585907},
        "address_vi": "Ulitsa Lva Tolstogo 21, khu Khamovniki, Moskva (gần ga metro Park Kultury)",
        "rating": None,
        "presentation_short_vi": "Đây là ngôi nhà gỗ mà đại văn hào Lev Tolstoy mua năm 1882 và sống cùng gia đình vào mỗi mùa đông cho tới năm 1901. Trong chính căn nhà này, ông đã viết gần một trăm tác phẩm, tiêu biểu là tiểu thuyết 'Phục sinh' và truyện vừa 'Cái chết của Ivan Ilyich'. Nội thất và đồ dùng của gia đình được gìn giữ gần như nguyên vẹn, tạo cảm giác chủ nhân chỉ vừa mới rời đi.",
        "presentation_long_vi": "Nằm ở khu Khamovniki yên tĩnh phía tây nam trung tâm Moskva, điền trang gỗ hai tầng này là nơi Lev Tolstoy chọn làm chốn cư ngụ mùa đông cho gia đình đông con của mình. Ông mua lại khu nhà vào năm 1882, cho sửa sang và nới thêm phòng, rồi luân phiên sống giữa đây và trang viên Yasnaya Polyana ở tỉnh Tula suốt gần hai mươi năm. Chính trong những căn phòng ấm áp này, nhà văn đã hoàn thành gần một trăm tác phẩm ở giai đoạn cuối đời, trong đó có tiểu thuyết 'Phục sinh' cùng các truyện vừa 'Cái chết của Ivan Ilyich', 'Bản sonata Kreutzer' và 'Cha Sergius'. Sau Cách mạng, ngôi nhà được quốc hữu hoá và mở cửa thành bảo tàng tưởng niệm từ năm 1921; ngày nay nó là một chi nhánh của Bảo tàng Quốc gia L.N. Tolstoy. Điều khiến nơi đây đặc biệt là hầu hết bàn ghế, sách vở, nhạc cụ và vật dụng sinh hoạt đều là hiện vật gốc của gia đình, được đặt đúng vị trí cũ. Bao quanh nhà là một khu vườn rợp bóng cây — ốc đảo xanh hiếm hoi giữa phố xá, nơi Tolstoy từng đi dạo và tiếp khách. Đến đây, du khách như bước thẳng vào đời sống thường nhật của một trong những cây bút vĩ đại nhất văn học thế giới.",
        "highlights_vi": [
            "Ngôi nhà gỗ Tolstoy mua năm 1882, nơi ông sống các mùa đông tới 1901 và viết gần 100 tác phẩm.",
            "Nội thất, sách vở và đồ dùng phần lớn là hiện vật gốc của gia đình, giữ nguyên cách bài trí xưa.",
            "Khu vườn cây xanh mát bao quanh — không gian tĩnh lặng hiếm có giữa lòng Moskva.",
        ],
        "practical": {
            "hours_vi": "Thường mở thứ Ba–Chủ nhật, khoảng 10:00–18:00 (phòng vé đóng sớm hơn); nghỉ thứ Hai và một ngày cuối tháng — nên kiểm tra lịch trên web trước khi đi.",
            "ticket_vi": "Khoảng 400–500 RUB/người lớn (2026); có ưu đãi cho học sinh, sinh viên — xem giá cập nhật trên web.",
            "duration_vi": "1–1,5 giờ.",
            "best_time_vi": "Cuối xuân đến đầu thu để kết hợp dạo khu vườn xanh mát.",
            "tips_vi": "Gần ga metro Park Kultury; sàn nhà lát gỗ nên khách thường phải mang bọc giày; rất hợp với người yêu văn chương Nga.",
        },
        "photo": None,
        "photo_credit": None,
        "maps": maps_for(55.734202, 37.585907),
        "official_site": "https://tolstoymuseum.ru",
        "sources": [
            {"title": "Rusmania — Lev Tolstoy Estate-Museum in Khamovniki", "url": "https://rusmania.com/central/moscow-federal-city/moscow/khamovniki/beyond-the-garden-ring-around-devichye-pole/lev-tolstoy-estate-museum-in-khamovniki"},
            {"title": "DiscoverMoscow — Leo Tolstoy Estate and Museum in Khamovniki", "url": "https://discovermoscow.com/en/places/muzej/muzej-usadba-l-n-tolstogo-v-hamovnikah/"},
            {"title": "In Your Pocket — Lev Tolstoy Memorial Estate in Khamovniki", "url": "https://www.inyourpocket.com/moscow/lev-tolstoy-memorial-estate-in-khamovniki_37772v"},
        ],
        "tags": ["museum", "history", "literary", "indoor", "garden"],
        "status": "enriched",
        "last_updated": "2026-07-25",
    },
    "saint-petersburg": {
        "id": "saint-petersburg-priory-palace",
        "slug": "priory-palace",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Cung điện Priory ở Gatchina (Prioratsky dvorets, Pri-ô-rát-xki)",
        "name_ru": "Приоратский дворец",
        "name_en": "Priory Palace",
        "categories": ["palace"],
        "coordinates": {"lat": 59.558056, "lon": 30.121389},
        "address_vi": "Công viên Priory, thành phố Gatchina, tỉnh Leningrad, cách trung tâm Saint Petersburg khoảng 45 km về phía nam",
        "rating": None,
        "presentation_short_vi": "Cung điện Priory là công trình 'độc nhất vô nhị' của nước Nga: gần như toàn bộ được xây bằng đất nện. Do kiến trúc sư Nikolay Lvov dựng năm 1799 bên hồ Đen trong công viên Gatchina, toà nhà nhỏ nhắn mang dáng tu viện này ban đầu dành cho Dòng Hiệp sĩ Malta.",
        "presentation_long_vi": "Ẩn mình bên bờ hồ Đen (Chyornoye ozero) trong công viên Priory ở thành phố Gatchina, cung điện Priory trông giống một tu viện Gothic khiêm nhường hơn là một dinh thự hoàng gia — và đó chính là nét quyến rũ của nó. Công trình gắn với một thử nghiệm kỹ thuật táo bạo: năm 1799, kiến trúc sư kiêm nhà phát minh Nikolay Lvov đã dựng gần như toàn bộ toà nhà bằng đất nện. Người ta nện chặt từng lớp đất dày chừng 6–8 cm trong khuôn gỗ, mỗi lớp lại thêm một lớp vữa vôi đặc biệt, để rồi tạo nên những bức tường vững chãi đến bất ngờ — ngay cả trên nền đất ẩm ven hồ. Sa hoàng Pavel I cho xây cung điện này gắn với Dòng Hiệp sĩ Malta mà ông làm Đại Sư, nên nó còn được gọi thân mật là 'Tu viện nhỏ'. Trải qua hơn hai thế kỷ mưa nắng và cả bom đạn Thế chiến, những bức tường đất vẫn đứng vững, khiến đây trở thành công trình đất nện duy nhất còn sót lại ở Nga từ cuối thế kỷ 18. Ngày nay cung điện là bảo tàng, giới thiệu lịch sử Dòng Malta, chân dung kiến trúc sư Lvov và kỹ thuật xây tường đất độc đáo. Tháp chuông cao vút soi bóng xuống mặt hồ tạo nên khung cảnh nên thơ, là điểm dừng thú vị khi khám phá quần thể Gatchina.",
        "highlights_vi": [
            "Công trình đất nện duy nhất còn tồn tại ở Nga từ cuối thế kỷ 18 — sáng tạo kỹ thuật của Nikolay Lvov (1799).",
            "Gắn với Dòng Hiệp sĩ Malta dưới thời Sa hoàng Pavel I, nên có biệt danh 'Tu viện nhỏ'.",
            "Tháp chuông và toà nhà soi bóng bên hồ Đen giữa công viên Priory — khung cảnh lãng mạn khác lạ.",
        ],
        "practical": {
            "hours_vi": "Khoảng 10:00–18:00 (phòng vé đóng lúc 17:00); nghỉ thứ Hai và thứ Ba — nên kiểm tra lịch trên web.",
            "ticket_vi": "Vé vào cửa vài trăm rúp/người lớn (2026); có ưu đãi cho học sinh, sinh viên — xem giá cập nhật trên web.",
            "duration_vi": "Khoảng 1 giờ cho cung điện; cộng thêm thời gian dạo công viên Priory.",
            "best_time_vi": "Cuối xuân đến đầu thu khi công viên xanh mát và mặt hồ phản chiếu đẹp.",
            "tips_vi": "Nên kết hợp trong cùng chuyến thăm cung điện Gatchina; đi tàu ngoại ô từ ga Baltiysky đến Gatchina rồi đi bộ hoặc bắt xe tới công viên Priory.",
        },
        "photo": None,
        "photo_credit": None,
        "maps": maps_for(59.558056, 30.121389),
        "official_site": "https://gatchinapalace.ru/en/dvorec/",
        "sources": [
            {"title": "Gatchina State Museum — Prioratsky Palace (trang chính thức)", "url": "https://gatchinapalace.ru/en/dvorec/"},
            {"title": "Russia Beyond — The origins of Russia's palace made out of EARTH", "url": "https://www.rbth.com/travel/330884-russian-priory-palace-gatchina"},
            {"title": "Wikipedia (EN) — Priory Palace", "url": "https://en.wikipedia.org/wiki/Priory_Palace"},
        ],
        "tags": ["palace", "daytrip", "history", "unusual", "imperial"],
        "status": "enriched",
        "last_updated": "2026-07-25",
    },
    "nizhny-novgorod": {
        "id": "nizhny-novgorod-bolshaya-pokrovskaya",
        "slug": "bolshaya-pokrovskaya",
        "region": "nizhny-novgorod",
        "region_name_vi": "Tỉnh Nizhny Novgorod",
        "federal_district": "Vùng Volga",
        "name_vi": "Phố Bolshaya Pokrovskaya (Bôn-sai-a Pô-krốp-xkai-a)",
        "name_ru": "Большая Покровская улица",
        "name_en": "Bolshaya Pokrovskaya Street",
        "categories": ["square_street"],
        "coordinates": {"lat": 56.322222, "lon": 44.000556},
        "address_vi": "Phố Bolshaya Pokrovskaya, trung tâm lịch sử thành phố Nizhny Novgorod (nối Quảng trường Minin và Pozharsky với Quảng trường Lyadov)",
        "rating": None,
        "presentation_short_vi": "Bolshaya Pokrovskaya là phố đi bộ chính và là 'trái tim' của khu trung tâm lịch sử Nizhny Novgorod, thường được ví như 'phố Arbat của Nizhny'. Con phố dài hơn 2 km, phần lớn dành cho người đi bộ, rợp bóng những toà nhà cổ, quán cà phê cùng nhiều bức tượng đồng đời thường ngộ nghĩnh.",
        "presentation_long_vi": "Nếu chỉ có thời gian dạo một con phố ở Nizhny Novgorod, hãy chọn Bolshaya Pokrovskaya. Đây là tuyến phố cổ và sầm uất bậc nhất thành phố, kéo dài hơn hai cây số từ Quảng trường Minin và Pozharsky bên chân thành Kremlin xuống tới Quảng trường Lyadov, trong đó phần lớn chiều dài (khoảng 1,3 km) đã được biến thành phố đi bộ từ đầu thập niên 1980. Hình thành và phát triển mạnh từ giữa thế kỷ 17 nhờ nằm gần trục đường lớn đi Moskva, con phố từng là nơi cư ngụ của giới quý tộc và thương nhân giàu có, để lại một quần thể kiến trúc thế kỷ 19 – đầu thế kỷ 20 duyên dáng còn được gìn giữ tốt. Điểm nhấn nổi bật là toà Nhà hát Kịch Nghệ thuật Nizhny Novgorod bề thế và toà nhà Ngân hàng Nhà nước mang phong cách tân-Nga lộng lẫy như một cung điện cổ tích. Người dân trìu mến gọi phố là 'Pokrovka'. Dọc lối đi, du khách sẽ bắt gặp hàng loạt tượng đồng đời thường sinh động — chú dê vui nhộn, quý bà bên ghế dài, người thợ ảnh, chú mèo… — những điểm chụp ảnh được yêu thích. Về chiều tối, phố lên đèn, nghệ sĩ đường phố biểu diễn, quán xá nhộn nhịp, biến Pokrovskaya thành nơi tản bộ lý tưởng để cảm nhận nhịp sống của thành phố bên sông Volga.",
        "highlights_vi": [
            "Phố đi bộ chính và cổ kính bậc nhất Nizhny Novgorod, được ví như 'phố Arbat của thành phố'.",
            "Quần thể kiến trúc thế kỷ 19 – đầu 20 nổi bật với Nhà hát Kịch và toà nhà Ngân hàng Nhà nước tráng lệ.",
            "Hàng loạt tượng đồng đời thường ngộ nghĩnh (chú dê, quý bà, người thợ ảnh…) là điểm chụp ảnh yêu thích.",
        ],
        "practical": {
            "hours_vi": "Phố mở tự do suốt cả ngày.",
            "ticket_vi": "Miễn phí.",
            "duration_vi": "1–2 giờ tản bộ.",
            "best_time_vi": "Chiều muộn đến tối, nhất là cuối tuần, khi phố lên đèn và có biểu diễn đường phố.",
            "tips_vi": "Đầu phố là thành Kremlin Nizhny Novgorod; giữa phố có ga metro Gorkovskaya — dễ kết hợp tham quan. Hai bên phố có nhiều quán cà phê, nhà hàng và cửa hàng lưu niệm.",
        },
        "photo": None,
        "photo_credit": None,
        "maps": maps_for(56.322222, 44.000556),
        "official_site": None,
        "sources": [
            {"title": "Wikipedia (EN) — Bolshaya Pokrovskaya Street", "url": "https://en.wikipedia.org/wiki/Bolshaya_Pokrovskaya_Street"},
            {"title": "Advantour — Bolshaya Pokrovskaya Street, Nizhny Novgorod", "url": "https://www.advantour.com/russia/nizhny-novgorod/bolshaya-pokrovskaya-street.htm"},
            {"title": "Travel portal Nizhny Novgorod region — Walking route along Bolshaya Pokrovskaya", "url": "https://nn-tourist.ru/en/stati/marshrut-po-pokrovke"},
        ],
        "tags": ["outdoor", "free", "square_street", "walk", "architecture"],
        "status": "enriched",
        "last_updated": "2026-07-25",
    },
}


def main():
    added, skipped = [], []
    for region, rec in RECORDS.items():
        path = os.path.join(REGIONS, region + ".json")
        arr = json.load(open(path, encoding="utf-8"))
        slugs = {r.get("slug") for r in arr}
        if rec["slug"] in slugs:
            skipped.append((region, rec["slug"]))
            print(f"SKIP (đã tồn tại): {region}/{rec['slug']}")
            continue
        # backup theo đúng quy ước các lần chạy trước
        bak = f"{path}.bak_add_{TS}"
        with open(bak, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        arr.append(rec)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        added.append((region, rec["slug"], len(arr)))
        print(f"ADDED: {region}/{rec['slug']} -> tổng {len(arr)} địa điểm trong vùng (backup: {os.path.basename(bak)})")
    print("\nSUMMARY added:", added)
    print("SUMMARY skipped:", skipped)


if __name__ == "__main__":
    main()
