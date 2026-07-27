# -*- coding: utf-8 -*-
"""Bổ sung 3 địa điểm nổi tiếng còn thiếu vào DB Cẩm nang Du lịch Nga (đợt B, 2026-07-25).
Nội dung tiếng Việt nguyên gốc (tự soạn, không dịch nguyên văn), rating để trống (chưa có nguồn xác thực).
Có kiểm tra trùng slug/id và tạo backup .bak_add_<timestamp> trước khi ghi.
Địa điểm: Cầu đi bộ Patriarshy (Moskva), Điền trang & Công viên Kuzminki (Moskva),
          Tượng Nhân sư Ai Cập trên bờ kè Đại học (Saint Petersburg).
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
    rec("moscow", "patriarshy-bridge",
        "Cầu đi bộ Patriarshy (Patriarshy Most)", "Патриарший мост", "Patriarshy Bridge",
        ["bridge"], 55.74361, 37.60778,
        "Bắc qua sông Moskva, nối khuôn viên Nhà thờ Chúa Cứu Thế với khu Bersenevka/Yakimanka và tiếp tục qua kênh Vodootvodny sang bờ kè Kadashevskaya, quận trung tâm Moskva (gần metro Kropotkinskaya)",
        "Cây cầu đi bộ duyên dáng bắc qua sông Moskva ngay cạnh Nhà thờ Chúa Cứu Thế — một trong những điểm ngắm cảnh và chụp ảnh được yêu thích bậc nhất thủ đô. Từ mặt cầu, tầm mắt mở ra mái vòm vàng của nhà thờ, tường thành Kremlin, cụm nhà máy Tháng Mười Đỏ và tượng đài Pyotr Đại đế khổng lồ. Cầu khánh thành năm 2004 theo phong cách tân cổ điển, dài khoảng 203 m và chỉ dành cho người đi bộ.",
        "Bắc ngang sông Moskva ở ngay sát Nhà thờ Chúa Cứu Thế, Cầu Patriarshy (Patriarshy Most — 'Cầu Thượng phụ', gọi theo vị Thượng phụ Chính thống giáo Nga có toà tại nhà thờ bên cạnh) là một trong những cây cầu đi bộ được ưa chuộng nhất Moskva. Cầu được xây dựng trong các năm 2002–2004 theo thiết kế của kiến trúc sư Mikhail Posokhin, nằm trong nỗ lực chỉnh trang khu trung tâm quanh nhà thờ vừa được phục dựng. Ban đầu cầu nối bờ bắc (khuôn viên nhà thờ) với đảo giữa sông ở khu Bersenevka; đến năm 2007, một nhánh nối dài bắc tiếp qua kênh Vodootvodny sang bờ kè Kadashevskaya, giúp du khách đi bộ liền mạch từ nhà thờ sang khu phố cổ Zamoskvorechye. Toàn cầu dài khoảng 203 m, rộng chừng 15 m, kết cấu thép nhưng khoác lối trang trí tân cổ điển hài hoà với nhà thờ: lan can gang chạm trổ, đèn lồng kiểu cổ và những đài ngắm cảnh nhô ra. Chính những đài ngắm này biến cây cầu thành 'ban công' tuyệt đẹp giữa lòng thủ đô: nhìn về một phía là mái vòm vàng rực và bức tường trắng của Nhà thờ Chúa Cứu Thế, phía kia là tường gạch đỏ cùng các tháp của Kremlin, xa hơn là cụm sáng tạo Tháng Mười Đỏ (Krasny Oktyabr) và tượng đài Pyotr Đại đế cao gần trăm mét của nhà điêu khắc Zurab Tsereteli. Ban ngày, cầu là lối tản bộ thư thái; khi hoàng hôn buông và cả thành phố lên đèn, nơi đây trở thành điểm hẹn lãng mạn của các cặp đôi và tay máy. Vào cửa hoàn toàn miễn phí, Cầu Patriarshy là điểm dừng chân gần như bắt buộc khi tham quan Nhà thờ Chúa Cứu Thế.",
        ["Cầu đi bộ nối thẳng khuôn viên Nhà thờ Chúa Cứu Thế với bờ nam sông Moskva; xây năm 2002–2004 (KTS Mikhail Posokhin), năm 2007 nối dài qua kênh Vodootvodny sang bờ kè Kadashevskaya.",
         "Một trong những điểm ngắm cảnh – chụp ảnh đẹp nhất Moskva: thu trọn mái vòm vàng của nhà thờ, tường Kremlin, nhà máy Tháng Mười Đỏ và tượng đài Pyotr Đại đế của Tsereteli.",
         "Dài khoảng 203 m, chỉ dành cho người đi bộ; lan can gang, đèn lồng cổ và các đài ngắm cảnh trang trí hài hoà với kiến trúc nhà thờ — lãng mạn cả ngày lẫn đêm."],
        ["bridge", "free", "outdoor", "viewpoint", "central", "modern"],
        {"hours_vi": "Cầu đi bộ ngoài trời, mở tự do 24/7.",
         "ticket_vi": "Miễn phí.",
         "duration_vi": "20–40 phút.",
         "best_time_vi": "Hoàng hôn và buổi tối khi nhà thờ cùng thành phố lên đèn; ngày trời trong để ngắm toàn cảnh.",
         "tips_vi": "Kết hợp thăm Nhà thờ Chúa Cứu Thế và đài quan sát của nhà thờ; đi bộ tiếp sang cụm nghệ thuật Tháng Mười Đỏ (Krasny Oktyabr) và Nhà Văn hoá GES-2 bên kia sông."},
        [{"title": "Patriarshy Bridge — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Patriarshy_Bridge"},
         {"title": "Patriarshiy Most (Moscow, 2004) — Structurae", "url": "https://structurae.net/en/structures/patriarshiy-most"},
         {"title": "Patriarshy Bridge, Moscow — Visitor Guide", "url": "https://audiala.com/en/russia/moscow/patriarshy-bridge"}]),

    rec("moscow", "kuzminki",
        "Điền trang và Công viên Kuzminki (Vlakhernskoye-Kuzminki)", "Усадьба Кузьминки (Влахернское-Кузьминки)",
        "Kuzminki Estate (Vlakhernskoye-Kuzminki)",
        ["park_garden", "palace", "museum"], 55.69528, 37.78472,
        "Phố Topolevaya alleya, quận Kuzminki, phía đông nam Moskva (gần metro Kuzminki/Volzhskaya); thuộc Công viên lịch sử Kuzminki-Lyublino",
        "Điền trang quý tộc thế kỷ 18–19 của dòng họ Golitsyn, nay là một trong những công viên rừng – hồ nước rộng và đẹp nhất phía đông nam Moskva, thường được ví là 'Versailles của nước Nga'. Quần thể kiến trúc tân cổ điển do kiến trúc sư Domenico Gilardi tạo dựng thập niên 1830, cùng chuỗi hồ, cầu đá, đền đài và Bảo tàng Văn hoá Điền trang.",
        "Nằm ở phía đông nam thủ đô, Kuzminki (tên đầy đủ Vlakhernskoye-Kuzminki) từng là một trong những điền trang tráng lệ nhất vùng ngoại vi Moskva. Vùng đất này thời Pyotr Đại đế được ban cho gia tộc thương nhân – kỹ nghệ Stroganov, rồi qua hôn nhân chuyển sang dòng họ quý tộc Golitsyn và hưng thịnh dưới tay họ suốt hơn một thế kỷ. Cái tên 'Vlakhernskoye' bắt nguồn từ biểu tượng Đức Mẹ Vlakherna (Blachernae) được gia tộc tôn kính và lưu giữ trong nhà thờ của điền trang. Diện mạo cổ điển còn thấy hôm nay phần lớn hình thành vào thập niên 1830, khi kiến trúc sư người Thuỵ Sĩ – Ý Domenico Gilardi cùng các cộng sự tái thiết quần thể theo phong cách Đế chế (Empire): nổi bật là 'Sân Ngựa' (Konny dvor) với vọng lâu âm nhạc, những cánh cổng gang tinh xảo và các tượng thần biển (hà mã) bằng gang do nhà điêu khắc Pyotr Klodt thực hiện. Bao quanh khu trung tâm là một chuỗi hồ nước nối nhau trên dòng suối Churilikha, điểm xuyết cầu đá, bến thuyền và các công trình nhỏ theo lối cổ điển, tạo nên khung cảnh nên thơ mà người đương thời từng ngợi ca. Sau Cách mạng, điền trang trải qua nhiều biến động và từng là nơi đặt viện nghiên cứu; đến năm 1999, phần lõi lịch sử được lập thành Bảo tàng Văn hoá Điền trang (một chi nhánh của Bảo tàng Moskva), với các trưng bày về dòng họ Golitsyn và nếp sống quý tộc Nga thế kỷ 19. Ngày nay, Kuzminki là công viên công cộng mênh mông: người Moskva tới đây dạo bộ dưới tán rừng, đạp xe, chèo thuyền và cho trẻ vui chơi mùa hè, trượt tuyết – trượt băng mùa đông. Rộng rãi, xanh mát và giàu dấu ấn lịch sử, đây là chốn lý tưởng để tạm rời sự ồn ào của trung tâm.",
        ["Điền trang của dòng họ quý tộc Golitsyn, mang tên 'Vlakhernskoye' theo biểu tượng Đức Mẹ Vlakherna được tôn kính; quần thể tân cổ điển hiện nay do KTS Domenico Gilardi tạo dựng thập niên 1830.",
         "Nổi bật với 'Sân Ngựa' (Konny dvor) cùng vọng lâu âm nhạc, cổng gang và các tượng thần biển bằng gang của nhà điêu khắc Pyotr Klodt; chuỗi hồ trên dòng Churilikha uốn quanh công viên.",
         "Từ năm 1999 là Bảo tàng Văn hoá Điền trang (thuộc Bảo tàng Moskva); nay là công viên rừng – hồ rộng lớn để dạo bộ, đạp xe, chèo thuyền mùa hè và trượt tuyết mùa đông."],
        ["park", "estate", "palace", "museum", "free", "outdoor", "golitsyn"],
        {"hours_vi": "Công viên mở tự do hằng ngày; các toà bảo tàng (Sân Ngựa và nhà phụ) thường mở khoảng 10:00–18:00 và đóng cửa thứ Hai — nên kiểm tra lịch trước.",
         "ticket_vi": "Vào công viên miễn phí; các gian trưng bày trong bảo tàng bán vé riêng.",
         "duration_vi": "2–3 giờ (có thể nửa ngày nếu dạo hết công viên).",
         "best_time_vi": "Cuối xuân đến đầu thu cho cây xanh và mặt hồ; mùa đông có lối trượt tuyết, trượt băng.",
         "tips_vi": "Đi metro tới ga Kuzminki hoặc Volzhskaya; khuôn viên rất rộng nên mang giày thoải mái; có thể kết hợp thăm điền trang Lyublino gần đó."},
        [{"title": "Vlakhernskoye-Kuzminki — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Vlakhernskoye-Kuzminki"},
         {"title": "Kuzminki Estate (Museum of Estate Culture) — Rusmania", "url": "https://rusmania.com/central/moscow-federal-city/moscow/outer-east/kuzminki-district/kuzminki-estate-museum-of-estate-culture"},
         {"title": "Kuzminki-Lyublino Museum Reserve — mos.ru", "url": "https://www.mos.ru/en/news/item/152202073/"}]),

    rec("saint-petersburg", "university-embankment-sphinxes",
        "Tượng Nhân sư Ai Cập trên bờ kè Đại học (Sfinksy na Universitetskoy naberezhnoy)",
        "Сфинксы на Университетской набережной", "Egyptian Sphinxes on the University Embankment",
        ["monument"], 59.93778, 30.28861,
        "Bờ kè Đại học (Universitetskaya naberezhnaya), trước Viện Hàn lâm Mỹ thuật, đảo Vasilievsky, Saint Petersburg",
        "Cặp tượng nhân sư Ai Cập cổ thật sự — khoảng 3.500 năm tuổi, tạc từ đá granite Aswan cho đền thờ Pharaoh Amenhotep III gần Thebes (Luxor). Được đưa về Nga năm 1832 và an vị trên bờ kè trước Viện Hàn lâm Mỹ thuật, đôi nhân sư trở thành một trong những biểu tượng cổ kính và huyền bí bậc nhất Saint Petersburg.",
        "Trên bờ kè Đại học của đảo Vasilievsky, ngay trước toà nhà uy nghi của Viện Hàn lâm Mỹ thuật, có hai pho tượng nhân sư khiến bất cứ ai đi qua cũng phải dừng bước. Khác với những bản sao trang trí thường thấy, đây là hai tác phẩm Ai Cập cổ đại thứ thiệt: được tạc bằng đá granite hồng Aswan khoảng 3.500 năm trước, mang khuôn mặt của Pharaoh Amenhotep III và từng canh giữ lối vào đền thờ tang lễ của ông ở gần Thebes (Luxor ngày nay). Đôi tượng được phát lộ trong các cuộc khai quật hồi thập niên 1820 và nhanh chóng gây chú ý ở châu Âu giữa cơn sốt 'Ai Cập học'. Theo ghi chép, nhà văn kiêm lữ khách người Nga Andrei Muravyov đã nhìn thấy chúng ở Ai Cập năm 1830 và viết thư đề nghị triều đình mua về; sau khi Hoàng đế Nikolai I chuẩn thuận, hai pho tượng vượt biển tới Saint Petersburg năm 1832. Để đón chúng, người ta cho xây lại đoạn bờ kè đá granite trước Viện Hàn lâm Mỹ thuật theo 'phong cách Ai Cập' do kiến trúc sư Konstantin Ton thiết kế; công trình hoàn tất năm 1834, về sau còn điểm thêm những chiếc đèn – ghế đồng hình quái điểu griffin ở bậc thang xuống sông Neva. Hai nhân sư quay mặt vào nhau qua lối bậc dẫn xuống mặt nước, lặng lẽ ngắm dòng Neva suốt gần hai thế kỷ. Người dân thành phố truyền tai rằng vẻ mặt của chúng dường như thay đổi theo ánh sáng trong ngày — dịu dàng lúc bình minh và bí ẩn hơn khi chiều tà. Miễn phí và luôn mở, đôi nhân sư là điểm dừng chân không thể bỏ qua khi dạo bờ kè, đặc biệt huyền ảo trong những đêm trắng mùa hè.",
        ["Nhân sư Ai Cập thật sự: khoảng 3.500 năm tuổi, tạc bằng đá granite Aswan mang khuôn mặt Pharaoh Amenhotep III, từng đứng trước đền thờ của ông gần Thebes (Luxor).",
         "Được nhà văn – lữ khách Andrei Muravyov nhìn thấy ở Ai Cập và đề xuất mua; đưa về Saint Petersburg năm 1832, an vị trên bờ kè trong các năm 1832–1834.",
         "Bờ kè đá granite trước Viện Hàn lâm Mỹ thuật do KTS Konstantin Ton thiết kế theo 'phong cách Ai Cập', điểm thêm đèn – ghế đồng hình griffin; nay là một trong những biểu tượng cổ kính, huyền bí nhất thành phố."],
        ["monument", "landmark", "free", "outdoor", "egyptian", "ancient", "neva"],
        {"hours_vi": "Ngoài trời, tham quan tự do 24/7.",
         "ticket_vi": "Miễn phí.",
         "duration_vi": "20–30 phút.",
         "best_time_vi": "Ban ngày để nhìn rõ chi tiết chạm khắc; hoàng hôn và đêm trắng mùa hè cho khung cảnh sông Neva lãng mạn.",
         "tips_vi": "Kết hợp dạo bờ kè Đại học, thăm Kunstkamera, Cung điện Menshikov và Viện Hàn lâm Mỹ thuật gần đó; cẩn thận khi xuống bậc thang sát mép nước."},
        [{"title": "Quay with Sphinxes — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Quay_with_Sphinxes"},
         {"title": "The Sphinxes at the Academy of Arts — saint-petersburg.com", "url": "http://www.saint-petersburg.com/monuments/sphinxes-at-the-academy-of-arts/"},
         {"title": "University quay with sphinxes — Geomerid", "url": "https://geomerid.com/en/place/university-quay-with-sphinxes-in-saint-petersburg-travel-attraction/overview/"}]),
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
