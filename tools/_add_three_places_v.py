# -*- coding: utf-8 -*-
"""_add_three_places_v.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26).

Thêm:
  1) Moscow          : Toà nhà Anh Cổ (Stary Angliyskiy Dvor) — museum/monument
  2) Saint Petersburg: Bảo tàng Lịch sử Tôn giáo (GMIR) — museum
  3) Saint Petersburg: Bảo tàng - Điền trang I.E. Repin «Penaty» (Repino) — museum/park

Nội dung tiếng Việt nguyên gốc, có ghi nguồn. Tọa độ thật.
Chạy:  python3 tools/_add_three_places_v.py
"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-26"


def maps_for(lat, lon):
    return {
        "yandex": f"https://yandex.com/maps/?pt={lon},{lat}&z=17&l=map",
        "google": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
    }


# ------------------------------------------------------------------ RECORDS
OLD_ENGLISH_COURT = {
    "id": "moscow-old-english-court",
    "slug": "old-english-court",
    "region": "moscow",
    "region_name_vi": "Moskva",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Toà nhà Anh Cổ (Stary Angliyskiy Dvor)",
    "name_ru": "Старый Английский двор",
    "name_en": "Old English Court",
    "categories": ["museum", "monument"],
    "coordinates": {"lat": 55.75236, "lon": 37.62688},
    "address_vi": "Ulitsa Varvarka, 4A, Kitai-Gorod, Moskva (rìa phía bắc Công viên Zaryadye)",
    "rating": None,
    "presentation_short_vi": (
        "Toà nhà đá trắng hiếm hoi còn sót lại từ đầu thế kỷ 16, từng là trụ sở của Công ty "
        "Thương mại Muscovy của người Anh — một trong những công trình dân sự cổ nhất Moskva, "
        "nay là bảo tàng nhỏ nằm ngay rìa Công viên Zaryadye."
    ),
    "presentation_long_vi": (
        "Nép mình trên phố cổ Varvarka, ngay cạnh Công viên Zaryadye và Quảng trường Đỏ, «Toà nhà "
        "Anh Cổ» là chứng nhân sống động của mối bang giao Nga–Anh khởi đầu từ thời Ivan Bạo chúa. "
        "Năm 1556, sau khi nhà hàng hải Anh Richard Chancellor tình cờ mở được tuyến đường biển "
        "phương Bắc tới Nga, Sa hoàng Ivan IV đã ban toà nhà đá này cho Công ty Muscovy làm nơi ở và "
        "buôn bán được miễn thuế — một đặc ân hiếm có thời bấy giờ. Qua nhiều thế kỷ, công trình bị "
        "cơi nới, che lấp và gần như chìm vào quên lãng; mãi tới thập niên 1960, kiến trúc sư trùng "
        "tu lừng danh Pyotr Baranovsky mới phát lộ và phục dựng lại diện mạo trung cổ nguyên bản của "
        "nó. Bảo tàng chính thức khai trương năm 1994, với sự hiện diện của Nữ hoàng Anh Elizabeth II "
        "trong chuyến thăm cấp nhà nước tới Nga. Bên trong, du khách được ngắm gian phòng khách với "
        "chiếc lò sưởi lớn, hầm chứa hàng hoá dày tường và những hiện vật tái hiện đời sống thương "
        "nhân, cùng câu chuyện về con đường biển Bạch Hải từng nối nước Nga với châu Âu. Đây là một "
        "điểm dừng nhỏ mà giàu chiều sâu lịch sử, rất dễ ghép vào hành trình dạo bộ Zaryadye và khu "
        "phố cổ Kitai-Gorod."
    ),
    "highlights_vi": [
        "Một trong những công trình kiến trúc dân sự (phi tôn giáo) cổ nhất còn tồn tại ở Moskva, có từ đầu thế kỷ 16.",
        "Được Sa hoàng Ivan Bạo chúa ban cho Công ty Thương mại Muscovy của Anh năm 1556 để ở và buôn bán miễn thuế.",
        "Bảo tàng khai trương năm 1994 với sự hiện diện của Nữ hoàng Elizabeth II; diện mạo trung cổ do KTS Pyotr Baranovsky phục dựng.",
    ],
    "practical": {
        "hours_vi": "Thứ Ba, Năm, Bảy, Chủ nhật: 10:00–18:00; Thứ Tư, Sáu: 11:00–19:00. Đóng cửa Thứ Hai và Thứ Sáu cuối tháng.",
        "ticket_vi": "Vé vào cửa ở mức thấp; nên xem giá mới nhất trên trang Công viên Zaryadye.",
        "duration_vi": "30–45 phút.",
        "best_time_vi": "Ghép cùng buổi dạo Công viên Zaryadye và các nhà thờ cổ trên phố Varvarka.",
        "tips_vi": "Nằm ngay lối vào phía Varvarka của Công viên Zaryadye; tiện kết hợp Quảng trường Đỏ, GUM và các nhà thờ cổ Kitai-Gorod.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(55.75236, 37.62688),
    "official_site": "https://www.zaryadyepark.ru/en/services/old-english-courtyard/",
    "sources": [
        {"title": "Wikipedia (EN) — Old English Court", "url": "https://en.wikipedia.org/wiki/Old_English_Court"},
        {"title": "Công viên Zaryadye — Old English Court", "url": "https://www.zaryadyepark.ru/en/services/old-english-courtyard/"},
        {"title": "Moscow City (mos.ru) — Old English Court becomes part of Zaryadye Park", "url": "https://www.mos.ru/en/news/item/79038073/"},
    ],
    "tags": ["museum", "history", "architecture", "kitai-gorod", "zaryadye"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}

MUSEUM_RELIGION = {
    "id": "saint-petersburg-museum-history-of-religion",
    "slug": "museum-history-of-religion",
    "region": "saint-petersburg",
    "region_name_vi": "Saint Petersburg",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Bảo tàng Lịch sử Tôn giáo Quốc gia (GMIR)",
    "name_ru": "Государственный музей истории религии",
    "name_en": "State Museum of the History of Religion",
    "categories": ["museum"],
    "coordinates": {"lat": 59.9312, "lon": 30.3037},
    "address_vi": "Ulitsa Pochtamtskaya, 14, Saint Petersburg (đối diện Bưu điện Trung tâm)",
    "rating": None,
    "presentation_short_vi": (
        "Bảo tàng độc nhất vô nhị ở Nga chuyên về lịch sử các tôn giáo thế giới — từ tín ngưỡng "
        "nguyên thuỷ, các nền tôn giáo cổ đại tới Do Thái giáo, Phật giáo, Ki-tô giáo và Hồi giáo — "
        "với bộ sưu tập hàng trăm nghìn hiện vật."
    ),
    "presentation_long_vi": (
        "Ra đời năm 1932 theo quyết định của Viện Hàn lâm Khoa học Xô-viết, đây là bảo tàng nhà nước "
        "duy nhất ở Nga và một trong số rất ít trên thế giới trình bày lịch sử tôn giáo như một hiện "
        "tượng văn hoá của nhân loại. Người khởi xướng và giám đốc đầu tiên là nhà dân tộc học "
        "Vladimir Bogoraz. Trong nhiều thập niên thời Xô-viết, bảo tàng đặt ngay trong Nhà thờ Kazan "
        "và từng mang màu sắc «vô thần»; sang năm 2000 nó dời về toà nhà riêng trên phố Pochtamtskaya "
        "— vốn là dinh thự của Bá tước Sergey Yaguzhinsky rồi sau thuộc Bưu điện Hoàng gia — và định "
        "hình lại theo hướng nghiên cứu khách quan, tôn trọng mọi tín ngưỡng. Các gian trưng bày đưa "
        "người xem đi qua tín ngưỡng thời tiền sử, tôn giáo Ai Cập và Lưỡng Hà cổ đại, thế giới Hy–La, "
        "rồi tới các tôn giáo lớn còn hiện diện hôm nay, qua vô số mô hình đền đài, tượng thần, thánh "
        "tích, thư tịch, tranh icon và đồ thờ tự. Với bộ sưu tập lên tới hàng trăm nghìn hiện vật, đây "
        "là điểm đến lý tưởng cho ai muốn hiểu bức tranh tôn giáo đa dạng của loài người — lại chỉ cách "
        "Nhà thờ Thánh Isaac vài phút đi bộ."
    ),
    "highlights_vi": [
        "Bảo tàng nhà nước duy nhất ở Nga dành riêng cho lịch sử tôn giáo thế giới, thành lập năm 1932.",
        "Từng đặt trong Nhà thờ Kazan tới năm 2000, nay ở toà dinh thự cổ trên phố Pochtamtskaya, đối diện Bưu điện Trung tâm.",
        "Bộ sưu tập trải khắp các nền tôn giáo từ thời tiền sử, cổ đại tới Do Thái giáo, Phật giáo, Ki-tô giáo và Hồi giáo.",
    ],
    "practical": {
        "hours_vi": "Thứ Năm–Thứ Hai: 10:00–18:00; Thứ Ba: 13:00–21:00. Đóng cửa Thứ Tư.",
        "ticket_vi": "Vé vào cửa mức phổ thông; xem giá mới nhất trên trang chính thức.",
        "duration_vi": "1–1,5 giờ.",
        "best_time_vi": "Ghép cùng Nhà thờ Thánh Isaac và Kỵ sĩ Đồng ở ngay gần.",
        "tips_vi": "Ga metro gần nhất: Admiralteyskaya (rồi đi bộ). Nằm trên phố Pochtamtskaya, đối diện Bưu điện chính của thành phố.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(59.9312, 30.3037),
    "official_site": "https://gmir.ru/",
    "sources": [
        {"title": "Wikipedia (EN) — Museum of the History of Religion", "url": "https://en.wikipedia.org/wiki/Museum_of_the_History_of_Religion"},
        {"title": "Saint-Petersburg.com — Museum of the History of Religion", "url": "http://www.saint-petersburg.com/museums/museum-of-the-history-of-religion/"},
        {"title": "Lonely Planet — Museum of the History of Religion", "url": "https://www.lonelyplanet.com/russia/st-petersburg/sennaya-kolomna/attractions/museum-of-the-history-of-religion/a/poi-sig/1480439/1336040"},
    ],
    "tags": ["museum", "religion", "history", "indoor", "st-isaac-area"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}

REPIN_PENATY = {
    "id": "saint-petersburg-repin-penaty",
    "slug": "repin-penaty",
    "region": "saint-petersburg",
    "region_name_vi": "Saint Petersburg",
    "federal_district": "Thành phố trực thuộc liên bang",
    "name_vi": "Bảo tàng - Điền trang I.E. Repin «Penaty» (Pê-na-tư)",
    "name_ru": "Музей-усадьба И. Е. Репина «Пенаты»",
    "name_en": "Repin's Penaty (Penates) Estate Museum",
    "categories": ["museum", "park_garden"],
    "coordinates": {"lat": 60.1760, "lon": 29.8610},
    "address_vi": "Primorskoe shosse, 411, làng Repino, quận Kurortny, Saint Petersburg (bên bờ Vịnh Phần Lan, cách trung tâm ~45 km)",
    "rating": None,
    "presentation_short_vi": (
        "Ngôi nhà - khu vườn ven Vịnh Phần Lan, nơi danh hoạ hiện thực Ilya Repin sống 30 năm cuối "
        "đời: căn nhà gỗ độc đáo với xưởng vẽ mái kính, bàn ăn có mâm xoay, và mộ hoạ sĩ nằm ngay "
        "trong vườn thông."
    ),
    "presentation_long_vi": (
        "«Penaty» — đặt theo tên các vị thần hộ gia trong tín ngưỡng La Mã cổ — là điền trang mà "
        "danh hoạ Ilya Repin (1844–1930), tác giả kiệt tác «Những người kéo thuyền trên sông Volga», "
        "mua năm 1899 (đứng tên người vợ thứ hai Natalia Nordman) và gắn bó suốt ba thập niên cuối "
        "đời. Nơi đây thuộc làng Repino — thời Repin còn mang tên Kuokkala và nằm trên đất Phần Lan — "
        "bên bờ Vịnh Phần Lan, cách trung tâm Sankt-Peterburg khoảng 45 km. Ngôi nhà gỗ do chính hoạ "
        "sĩ phác thảo, với nhiều sáng kiến lạ mắt: mái và vách kính đón ánh sáng tự nhiên cho xưởng "
        "vẽ, chiếc bàn ăn tròn có mâm xoay để khách tự phục vụ mà không cần người hầu. Vào các buổi "
        "họp mặt «thứ Tư» nổi tiếng, Penaty từng đón giới tinh hoa văn nghệ Nga như Gorky, Chaliapin, "
        "Mayakovsky. Repin qua đời năm 1930 và được an táng ngay trong khu vườn theo di nguyện. Ngôi "
        "nhà nguyên bản bị thiêu rụi trong Thế chiến II, sau được phục dựng theo bản vẽ cũ và mở cửa "
        "lại đầu thập niên 1960 dưới sự bảo trợ của Viện Hàn lâm Nghệ thuật. Ngày nay Penaty là một "
        "phần của Di sản Thế giới UNESCO «Trung tâm lịch sử Sankt-Peterburg và các cụm công trình liên "
        "quan». Dạo bước trong rừng thông rợp bóng dẫn ra tới bờ biển, du khách cảm nhận rõ nguồn cảm "
        "hứng thiên nhiên đã nuôi dưỡng ngòi bút của Repin."
    ),
    "highlights_vi": [
        "Nơi danh hoạ Ilya Repin sống, sáng tác 30 năm cuối đời (1899–1930) và được an táng ngay trong khu vườn.",
        "Nhà gỗ do Repin tự thiết kế với xưởng vẽ mái kính và chiếc bàn ăn có mâm xoay độc đáo.",
        "Bị phá huỷ trong Thế chiến II, phục dựng theo bản vẽ cũ; nay là một phần của Di sản Thế giới UNESCO ở Sankt-Peterburg.",
    ],
    "practical": {
        "hours_vi": "Mở cửa hằng ngày trừ Thứ Hai và Thứ Ba; 10:30–16:00 (15/5–15/9) hoặc 10:30–17:00 (15/9–15/5). Nên đặt vé trực tuyến trước và kiểm tra lịch mới nhất.",
        "ticket_vi": "Mua vé trực tuyến trên trang chính thức.",
        "duration_vi": "1–2 giờ (cả nhà và vườn).",
        "best_time_vi": "Mùa hè và đầu thu, khi rừng thông và bờ vịnh đẹp nhất.",
        "tips_vi": "Đi tàu điện (elektrichka) từ Ga Phần Lan tới ga Repino rồi đi bộ ~10–15 phút, hoặc xe buýt 211 từ metro Chernaya Rechka; đi ô tô theo đường Primorskoe shosse.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for(60.1760, 29.8610),
    "official_site": "https://artsacademymuseum.org/en/branches/penaty-estate-museum-of-ilya-repin/",
    "sources": [
        {"title": "Wikipedia (EN) — Penaty Memorial Estate", "url": "https://en.wikipedia.org/wiki/Penaty_Memorial_Estate"},
        {"title": "Arts Academy Museum — Ilya Repin's Penaty Memorial Estate", "url": "https://artsacademymuseum.org/en/branches/penaty-estate-museum-of-ilya-repin/"},
        {"title": "Saint-Petersburg.com — Penaty Estate Museum of Ilya Repin", "url": "http://www.saint-petersburg.com/museums/penaty-estate-museum-of-ilya-repin/"},
    ],
    "tags": ["museum", "estate", "art", "repin", "gulf-of-finland", "kurortny", "unesco"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow.json": [OLD_ENGLISH_COURT],
    "saint-petersburg.json": [MUSEUM_RELIGION, REPIN_PENATY],
}


def main():
    total_added = 0
    grand_total = 0
    for fname, recs in PLAN.items():
        path = os.path.join(REGIONS, fname)
        arr = json.load(open(path, encoding="utf-8"))
        existing_slugs = {p.get("slug") for p in arr}
        existing_ids = {p.get("id") for p in arr}
        to_add = []
        for r in recs:
            if r["slug"] in existing_slugs or r["id"] in existing_ids:
                print(f"  = BỎ QUA (đã có): {fname} :: {r['slug']}")
                continue
            to_add.append(r)
        if not to_add:
            continue
        # backup
        bak = path + f".bak_add_{TS}"
        with open(bak, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        arr.extend(to_add)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        total_added += len(to_add)
        print(f"  + {fname}: thêm {len(to_add)} địa điểm -> tổng {len(arr)} (backup: {os.path.basename(bak)})")
        for r in to_add:
            print(f"        - {r['name_vi']}  [{','.join(r['categories'])}]  ({r['coordinates']['lat']},{r['coordinates']['lon']})")

    print(f"\nTổng đã thêm lần này: {total_added} địa điểm.")


if __name__ == "__main__":
    main()
