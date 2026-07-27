# -*- coding: utf-8 -*-
"""Bổ sung 3 địa điểm nổi tiếng còn thiếu vào DB Cẩm nang Du lịch Nga.
Nội dung tiếng Việt nguyên gốc (tự soạn), rating để trống (chưa có nguồn xác thực).
Có kiểm tra trùng slug/id và tạo backup .bak_add_<timestamp> trước khi ghi.
"""
import json, os, datetime, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGIONS = os.path.join(ROOT, "data", "regions")
TODAY = "2026-07-25"
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

RMETA = {
    "moscow": ("Moskva", "Thành phố trực thuộc liên bang"),
    "saint-petersburg": ("Saint Petersburg", "Thành phố trực thuộc liên bang"),
}


def maps(lat, lon):
    return {"yandex": f"https://yandex.com/maps/?pt={lon},{lat}&z=16&l=map",
            "google": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"}


def rec(region, slug, name_vi, name_ru, name_en, cats, lat, lon, addr, short, long, hl,
        tags, practical, sources, status="enriched", official_site=None):
    nv, fed = RMETA[region]
    return {
        "id": f"{region}-{slug}", "slug": slug, "region": region,
        "region_name_vi": nv, "federal_district": fed,
        "name_vi": name_vi, "name_ru": name_ru, "name_en": name_en,
        "categories": cats, "coordinates": {"lat": lat, "lon": lon}, "address_vi": addr,
        "rating": {"value": None, "count": None, "source": None, "as_of": None},
        "review_summary_vi": "",
        "presentation_short_vi": short, "presentation_long_vi": long,
        "highlights_vi": hl, "practical": practical,
        "photo": None, "photo_credit": None,
        "maps": maps(lat, lon), "official_site": official_site,
        "sources": sources, "tags": tags, "status": status, "last_updated": TODAY,
    }


CANDIDATES = [
    rec("moscow", "hermitage-garden",
        "Vườn Hermitage (Sad «Ermitazh»)", "Сад «Эрмитаж»", "Moscow Hermitage Garden",
        ["park_garden", "theatre"], 55.77111, 37.60750,
        "Phố Karetny Ryad 3, quận Tverskoy, trung tâm Moskva (gần metro Chekhovskaya, Tsvetnoy Bulvar, Pushkinskaya/Tverskaya)",
        "Khu vườn giải trí lịch sử ngay giữa lòng Moskva, mang diện mạo hiện nay từ năm 1894 nhờ thương gia Yakov Shchukin. Được xem là 'cái nôi' của sân khấu và điện ảnh thủ đô — nơi có buổi chiếu phim công cộng đầu tiên ở Moskva và những vở diễn đầu của đoàn kịch tiền thân Nhà hát Nghệ thuật Moskva. Ngày nay là ốc đảo xanh ôm trọn ba nhà hát (Ermitazh, Sfera và Novaya Opera), quanh năm rộn ràng lễ hội, hoà nhạc ngoài trời và sân trượt băng mùa đông.",
        "Nằm nép mình sau phố Karetny Ryad, chỉ vài bước chân từ đại lộ Tverskaya sầm uất, Vườn Hermitage là một trong những góc lãng mạn và giàu chất nghệ thuật nhất trung tâm Moskva. Mảnh đất này đã có truyền thống làm vườn vui chơi công cộng từ đầu thế kỷ 19, nhưng diện mạo hiện nay gắn liền với thương gia Yakov Shchukin: năm 1894 ông thuê lại khu đất đang bỏ hoang, cải tạo trong khoảng một năm và mở cửa khu vườn 'Ermitazh' mới vào mùa hè 1895. Shchukin cho cải tạo một xưởng cũ thành nhà hát, dựng thêm sân khấu ngoài trời và mái che, biến nơi đây thành trung tâm giải trí thời thượng của giới thị dân Moskva. Chính tại khu vườn này đã diễn ra một trong những buổi chiếu phim công cộng đầu tiên ở Moskva (năm 1896), và đoàn kịch tiền thân của Nhà hát Nghệ thuật Moskva (MKhT) từng biểu diễn trong vườn vào những năm cuối thế kỷ 19. Trải qua hơn một thế kỷ, Vườn Hermitage vẫn giữ vai trò 'thánh địa' sân khấu: trong khuôn viên rợp bóng cây hiện có tới ba nhà hát cùng hoạt động — Nhà hát Ermitazh, Nhà hát Sfera và Nhà hát Novaya Opera (Nhạc kịch Mới). Ngày thường, đây là nơi người Moskva tới đọc sách trên ghế dài, hẹn hò bên đài phun nước và bồn hoa, cho trẻ chơi ở khu vui chơi; vào mùa cao điểm, khu vườn lại bừng lên với các liên hoan âm nhạc, hội chợ sách, chợ phiên và biểu diễn ngoài trời. Mùa đông, một phần vườn được biến thành sân trượt băng lung linh ánh đèn. Nhỏ nhắn nhưng đậm đặc ký ức văn hoá, Vườn Hermitage là điểm dừng chân dễ chịu để cảm nhận nhịp sống nghệ thuật của thủ đô Nga.",
        ["Diện mạo hiện nay do thương gia Yakov Shchukin tạo dựng: thuê đất năm 1894, mở cửa khu vườn 'Ermitazh' mới vào mùa hè 1895.",
         "Được xem là cái nôi của sân khấu – điện ảnh Moskva: nơi có buổi chiếu phim công cộng đầu tiên (1896) và những buổi diễn đầu của đoàn kịch tiền thân Nhà hát Nghệ thuật Moskva.",
         "Trong vườn có ba nhà hát cùng hoạt động — Ermitazh, Sfera và Novaya Opera — cùng lễ hội, hoà nhạc ngoài trời và sân trượt băng mùa đông."],
        ["park", "theatre", "free", "outdoor", "central", "cultural"],
        {"hours_vi": "Vườn mở cửa tự do hằng ngày (thường từ sáng tới khuya); mỗi nhà hát và sự kiện có lịch, giờ và vé riêng.",
         "ticket_vi": "Vào vườn miễn phí; vé xem kịch/hoà nhạc, một số lễ hội hoặc sân trượt băng mua riêng.",
         "duration_vi": "1–1,5 giờ (lâu hơn nếu xem biểu diễn).",
         "best_time_vi": "Cuối xuân đến đầu thu cho không gian ngoài trời; mùa đông có sân trượt băng.",
         "tips_vi": "Xem trước lịch diễn của ba nhà hát; kết hợp dạo phố Tverskaya và đại lộ Tsvetnoy gần đó."},
        [{"title": "Moscow Hermitage Garden — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Moscow_Hermitage_Garden"},
         {"title": "History of the Hermitage Garden — mos.ru", "url": "https://www.mos.ru/en/news/item/78097073/"},
         {"title": "Hermitage Garden — DiscoverMoscow.com", "url": "https://discovermoscow.com/en/places/parki/sad-ermitazh/"}]),

    rec("moscow", "chistye-prudy",
        "Ao Trong (Chistye Prudy) và Đại lộ Chistoprudny", "Чистые пруды (Чистопрудный бульвар)",
        "Chistye Prudy (Clean Ponds) and Chistoprudny Boulevard",
        ["park_garden", "square_street"], 55.76208, 37.64460,
        "Đại lộ Chistoprudny (Chistoprudny bulvar), quận Basmanny — thuộc Vành đai Đại lộ, trung tâm Moskva (ngay metro Chistye Prudy)",
        "Một trong những đoạn đẹp và được yêu thích nhất của Vành đai Đại lộ Moskva: hồ nước rộng nằm giữa đại lộ rợp bóng cây, viền quanh là quán cà phê, tượng đài và nhà hát. Cái tên 'Ao Trong' ra đời sau khi hồ nước từng bị gọi là 'Ao Bẩn' được nạo vét, làm sạch hồi đầu thế kỷ 18 — gắn với công tước Menshikov. Mùa hè là chốn dạo bộ, đạp vịt; mùa đông hồ đóng băng thành sân trượt lộ thiên.",
        "Chistye Prudy — 'Ao Trong' — là một trong những địa chỉ dạo chơi được người Moskva yêu mến nhất trên Vành đai Đại lộ (Bulvarnoe koltso), tuyến đại lộ hình vòng cung ôm lấy khu trung tâm lịch sử. Hồ nước ở đây vốn hình thành từ một con đập trên dòng suối Rachka nhỏ. Đến đầu thế kỷ 18, khu vực này ô nhiễm tới mức bị gọi là 'Poganye prudy' — 'Ao Bẩn'. Theo giai thoại đô thị, khi công tước Aleksandr Menshikov — cận thần thân tín của Pyotr Đại đế — cho xây nhà thờ Tổng lãnh thiên thần Gabriel (còn gọi là Tháp Menshikov) ở gần đó, ông đã ra lệnh nạo vét, làm sạch hồ và cấm đổ rác thải xuống nước; từ đó cái tên 'Chistye Prudy' (Ao Trong) ra đời và tồn tại đến nay. Ngày nay, dải đại lộ Chistoprudny chạy dọc hồ là không gian công cộng lý tưởng: hàng cây cổ thụ, ghế dài, bồn hoa, quán cà phê và nhà hàng nối nhau. Ở đầu đại lộ là tượng đài nhà văn – nhà ngoại giao Aleksandr Griboedov (dựng năm 1959), còn ngay bên hồ là Nhà hát Sovremennik trứ danh — sân khấu ra đời trong 'thời kỳ tan băng' Khrushchev cuối thập niên 1950 và trở thành một biểu tượng của kịch nghệ Nga hiện đại. Mùa hè, du khách thong dong tản bộ, đạp vịt trên hồ, nghe nhạc đường phố; sang đông, mặt hồ đóng băng biến thành một trong những sân trượt băng ngoài trời quen thuộc nhất khu trung tâm. Ngay cạnh là ga metro Chistye Prudy (khai trương năm 1935) — điểm hẹn quen thuộc của người Moskva.",
        ["Tên 'Ao Trong' (Chistye Prudy) ra đời sau khi hồ 'Ao Bẩn' được nạo vét, làm sạch hồi đầu thế kỷ 18 — gắn với công tước Menshikov và Tháp Menshikov gần đó.",
         "Thuộc Vành đai Đại lộ lịch sử; ven hồ có tượng đài văn hào Griboedov (1959) và Nhà hát Sovremennik nổi tiếng.",
         "Mùa hè để dạo bộ, đạp vịt trên hồ; mùa đông hồ đóng băng thành sân trượt lộ thiên giữa trung tâm Moskva."],
        ["pond", "boulevard", "free", "outdoor", "central"],
        {"hours_vi": "Không gian công cộng ngoài trời, mở tự do suốt ngày; Nhà hát Sovremennik và các quán ven hồ có giờ riêng.",
         "ticket_vi": "Miễn phí dạo chơi; thuê thuyền/đạp vịt, trượt băng hoặc xem kịch mua vé riêng.",
         "duration_vi": "Khoảng 1 giờ (thong thả hơn nếu ngồi cà phê hoặc trượt băng).",
         "best_time_vi": "Cuối xuân đến đầu thu để tản bộ; mùa đông để trượt băng trên hồ.",
         "tips_vi": "Xuống metro Chistye Prudy là tới ngay; kết hợp đi bộ dọc Vành đai Đại lộ sang Sretensky và Pokrovsky."},
        [{"title": "Chistye Prudy — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Chistye_Prudy"},
         {"title": "Chistoprudny Boulevard — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Chistoprudny_Boulevard"},
         {"title": "Sovremennik Theatre — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Sovremennik_Theatre"}]),

    rec("saint-petersburg", "gostiny-dvor",
        "Thương xá Gostiny Dvor Lớn (Bolshoy Gostiny Dvor)", "Большой Гостиный двор", "Great Gostiny Dvor",
        ["square_street", "other"], 59.93390, 30.33500,
        "Đại lộ Nevsky 35, quận Trung tâm (Tsentralny), Saint Petersburg (có lối ra thẳng từ ga metro Gostiny Dvor)",
        "Thương xá cổ và lớn nhất Saint Petersburg — và là một trong những trung tâm mua sắm có mái vòm ra đời sớm nhất thế giới. Toà nhà tân cổ điển hai tầng với dãy hành lang vòm chạy hơn một cây số quanh sân trong, do kiến trúc sư Vallin de la Mothe thiết kế và xây dựng suốt các năm 1761–1785. Đến nay vẫn là một bách hoá tổng hợp sầm uất ngay trên đại lộ Nevsky.",
        "Trải dài ở góc giao giữa đại lộ Nevsky và phố Sadovaya, Bolshoy Gostiny Dvor (Thương xá Lớn) là khu mua sắm lâu đời và bề thế nhất Saint Petersburg, đồng thời được xem là một trong những thương xá có mái che ra đời sớm nhất thế giới. 'Gostiny dvor' trong tiếng Nga cổ có nghĩa là khu nhà dành cho thương nhân (gost) tới buôn bán và lưu trú. Toà nhà đá hiện nay được khởi công năm 1761 và hoàn tất năm 1785 theo thiết kế tân cổ điển sơ kỳ của kiến trúc sư gốc Pháp Jean-Baptiste Vallin de la Mothe. Trước đó, nhiều kiến trúc sư lừng danh như Rastrelli và Rinaldi cũng từng đệ trình phương án; bản vẽ lộng lẫy theo phong cách baroque của Rastrelli bị gạt đi vì quá tốn kém, nhường chỗ cho lối kiến trúc giản dị mà cân đối hơn. Kết quả là một khối nhà hình tứ giác không đều, gồm hai tầng hành lang vòm bao quanh một sân trong; chu vi mặt tiền dài tới hơn một cây số, ôm trọn diện tích khoảng 53.000 m². Cuối thế kỷ 18, kiến trúc sư Giacomo Quarenghi còn dựng thêm các dãy nhà phụ ở phía tây trên phố Dumskaya. Suốt hơn hai thế kỷ, Gostiny Dvor luôn là trái tim thương mại của thành phố; ngày nay nơi đây vẫn hoạt động như một bách hoá tổng hợp lớn với hàng trăm gian hàng thời trang, mỹ phẩm, quà lưu niệm và quán cà phê. Ga tàu điện ngầm Gostiny Dvor có lối lên thẳng bên trong toà nhà, khiến đây vừa là điểm mua sắm, vừa là cột mốc định vị quen thuộc giữa đại lộ Nevsky nhộn nhịp.",
        ["Thương xá cổ và lớn nhất Saint Petersburg, một trong những khu mua sắm có mái vòm ra đời sớm nhất thế giới.",
         "Xây theo thiết kế tân cổ điển của Jean-Baptiste Vallin de la Mothe (1761–1785); phương án baroque xa hoa của Rastrelli bị loại vì quá tốn kém.",
         "Hai tầng hành lang vòm bao quanh sân trong, chu vi mặt tiền hơn 1 km (~53.000 m²); nay vẫn là bách hoá sầm uất, có lối metro lên thẳng bên trong."],
        ["shopping", "architecture", "landmark", "nevsky-prospekt", "historic"],
        {"hours_vi": "Mở cửa hằng ngày như một trung tâm thương mại (thường khoảng 10:00–22:00); giờ từng gian hàng có thể khác nhau.",
         "ticket_vi": "Vào tham quan, mua sắm miễn phí.",
         "duration_vi": "30 phút – 1 giờ (lâu hơn nếu mua sắm).",
         "best_time_vi": "Quanh năm; tiện ghé khi dạo đại lộ Nevsky.",
         "tips_vi": "Có lối ra vào thẳng từ ga metro Gostiny Dvor; kết hợp tham quan Nevsky, cửa hàng Eliseyev và Nhà Singer gần đó."},
        [{"title": "Great Gostiny Dvor — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Great_Gostiny_Dvor"},
         {"title": "Bolshoy Gostiny Dvor — saint-petersburg.com", "url": "http://www.saint-petersburg.com/buildings/bolshoy-gostiny-dvor/"},
         {"title": "The Great Gostiny Dvor — VisitRussia", "url": "https://visitrussia.com/citiesguide/spb/places/the_great_gostiny_dvor"}]),
]


def main():
    added, skipped = {}, []
    for r in CANDIDATES:
        path = os.path.join(REGIONS, r["region"] + ".json")
        arr = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
        if any(x.get("slug") == r["slug"] or x.get("id") == r["id"] for x in arr):
            skipped.append(r["id"])
            continue
        bak = f"{path}.bak_add_{STAMP}"
        if not os.path.exists(bak):
            shutil.copy2(path, bak)
        arr.append(r)
        json.dump(arr, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        added.setdefault(r["region"], []).append(r["slug"])
    print("SKIPPED (da ton tai):", skipped or "none")
    for reg, slugs in added.items():
        print(f"+ {reg}: them {len(slugs)} -> {', '.join(slugs)}")
    if not added:
        print("Khong co dia diem moi nao duoc them.")


if __name__ == "__main__":
    main()
