# -*- coding: utf-8 -*-
"""_add_three_places_s.py — Bổ sung 3 địa điểm nổi tiếng còn thiếu.
Moscow: Nhà thờ Che Chở Đức Mẹ ở Fili (Baroque Naryshkin).
Saint Petersburg: Khải Hoàn Môn Moskva; Nhà thờ Chính toà Thánh Sampson.
Nội dung tiếng Việt nguyên gốc; toạ độ & dữ kiện đã kiểm chứng qua nguồn ghi trong 'sources'.
Chạy: python3 tools/_add_three_places_s.py
"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TODAY = "2026-07-26"
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

NEW = [
    {
        "id": "moscow-intercession-church-fili",
        "slug": "intercession-church-fili",
        "region": "moscow",
        "region_name_vi": "Moskva",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Nhà thờ Che Chở Đức Mẹ ở Fili (Tserkov Pokrova v Filyakh)",
        "name_ru": "Церковь Покрова Пресвятой Богородицы в Филях",
        "name_en": "Church of the Intercession at Fili",
        "categories": ["church"],
        "coordinates": {"lat": 55.7507, "lon": 37.5101},
        "address_vi": "Đường Novozavodskaya, số 6, quận Filyovsky Park (Fili), Moskva, 121087",
        "rating": None,
        "review_summary_vi": "Khách tham quan thường trầm trồ trước dáng vẻ thanh thoát, cân đối và sắc hồng - trắng nổi bật của nhà thờ, xem đây là một trong những ví dụ đẹp nhất của Baroque Naryshkin ở Moskva. Nhiều người đặc biệt ấn tượng với bộ khám thờ chín tầng chạm trổ bên trong. Lưu ý hay gặp: nhà thờ tầng trên chỉ mở vào mùa ấm nên không phải lúc nào cũng vào xem được nội thất — nên tra giờ trước khi đến.",
        "presentation_short_vi": "Một trong những viên ngọc của kiến trúc Baroque Moskva (Baroque Naryshkin), do quý tộc Lev Naryshkin — cậu ruột của Pyotr Đại đế — cho xây trong điền trang Fili vào khoảng năm 1690–1694. Ngôi nhà thờ hồng - trắng dựng theo kiểu tháp bát giác xếp tầng, gồm hai nhà thờ chồng lên nhau: nhà thờ mùa đông Che Chở Đức Mẹ ở tầng dưới và nhà thờ mùa hè kính Chúa Cứu Thế ở tầng trên — nơi còn giữ được bộ khám thờ (iconostas) chín tầng nguyên bản hiếm có.",
        "presentation_long_vi": "Nằm ở phía tây Moskva, nhà thờ Fili là kiệt tác được nhắc đến nhiều nhất mỗi khi người ta nói về Baroque Naryshkin — dòng kiến trúc rực rỡ cuối thế kỷ 17 mang tên gia tộc Naryshkin. Chủ nhân điền trang, quý tộc Lev Kirillovich Naryshkin, là em của Hoàng thái hậu Natalia và là cậu ruột của Pyotr Đại đế; tương truyền ông khấn dựng nhà thờ để tạ ơn thoát nạn sau vụ binh biến Streltsy năm 1682 từng cướp đi sinh mạng hai người anh của ông. Công trình xây trong khoảng 1690–1694, đặt trên một tầng hầm cao (podklet) có hành lang mở bao quanh cùng ba cầu thang lớn dẫn lên; thân nhà thờ vươn cao bằng những khối bát giác nhỏ dần về đỉnh. Bên trong nhà thờ tầng trên là báu vật thật sự: bộ khám thờ chạm trổ chín tầng do nghệ nhân Karp Zolotarev cùng thợ vẽ icon từ Xưởng Vũ khí Kremlin thực hiện, gần như còn nguyên vẹn. Sau nhiều lần hư hại — quân Pháp năm 1812, rồi thời Xô-viết và Thế chiến II khiến nhà thờ mất hết vòm mái — công trình được trùng tu công phu suốt các năm 1955–1980 và từng là chi nhánh Bảo tàng Andrei Rublev. Đứng ở đây, du khách còn có thể phóng tầm mắt sang những tòa tháp kính hiện đại của khu Moskva-City.",
        "highlights_vi": [
            "Kiệt tác tiêu biểu của phong cách Baroque Naryshkin (Baroque Moskva), xây khoảng 1690–1694 trong điền trang của quý tộc Lev Naryshkin — cậu ruột của Pyotr Đại đế.",
            "Cấu trúc tháp bát giác xếp tầng trên tầng hầm cao với ba cầu thang lớn; thực chất là hai nhà thờ chồng nhau (mùa đông ở dưới, mùa hè ở trên).",
            "Bộ khám thờ (iconostas) chín tầng nguyên bản do Karp Zolotarev và thợ Xưởng Vũ khí Kremlin thực hiện — hiếm có về mức độ bảo tồn."
        ],
        "practical": {
            "hours_vi": "Nhà thờ dưới (mùa đông) mở cửa hằng ngày, thường khoảng 8:00–19:00. Nhà thờ trên với khám thờ nguyên bản chỉ mở vào mùa ấm (thường 15/5–15/10), giờ tham quan hẹp (khoảng 12:00–18:00). Nên kiểm tra lịch trước khi đến.",
            "ticket_vi": "Vào tham quan hiện thường miễn phí (có thể đóng góp tùy tâm); một số tour có hướng dẫn thu phí riêng.",
            "duration_vi": "Khoảng 30–60 phút.",
            "best_time_vi": "Từ cuối xuân đến đầu thu, khi nhà thờ tầng trên mở cửa; ban ngày nắng đẹp để thấy rõ sắc hồng - trắng và các chi tiết chạm khắc.",
            "tips_vi": "Đi tàu điện ngầm tới ga Fili hoặc Bagrationovskaya rồi đi bộ. Đây là nhà thờ đang hoạt động nên giữ trang phục, thái độ phù hợp; muốn xem khám thờ nguyên bản thì phải canh đúng mùa mở nhà thờ tầng trên."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=37.5101,55.7507&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=55.7507,37.5101"
        },
        "official_site": "https://fili.moseparh.ru/",
        "sources": [
            {"title": "Church of the Intercession at Fili — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Church_of_the_Intercession_at_Fili"},
            {"title": "Церковь Покрова Пресвятой Богородицы в Филях — sobory.ru", "url": "https://sobory.ru/article/?object=02066"},
            {"title": "A Moscow Baroque Pearl: The Church of the Intercession in Fili — Uỷ ban UNESCO LB Nga", "url": "https://unesco.ru/en/news/56-baroque-pearl/"}
        ],
        "tags": ["church", "baroque", "naryshkin-baroque", "architecture", "history", "17th-century"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-moscow-triumphal-gate",
        "slug": "moscow-triumphal-gate",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Khải Hoàn Môn Moskva (Moskovskiye Triumfalnye Vorota)",
        "name_ru": "Московские триумфальные ворота",
        "name_en": "Moscow Triumphal Gate",
        "categories": ["monument"],
        "coordinates": {"lat": 59.8914, "lon": 30.3192},
        "address_vi": "Quảng trường Moskovskiye Vorota (Ploshchad Moskovskiye Vorota), Đại lộ Moskovsky, quận Moskovsky, Saint Petersburg; ngay cạnh ga tàu điện ngầm Moskovskie Vorota.",
        "rating": None,
        "review_summary_vi": "Du khách ấn tượng với quy mô bề thế và những hàng cột gang màu sẫm của cổng, cùng câu chuyện lịch sử ít người biết: cổng từng bị tháo rời rồi được dùng làm phòng tuyến chống tăng trong Thế chiến II. Vị trí ngay cửa ga metro khiến nhiều người thấy tiện ghé qua. Điểm lưu ý: công trình đứng giữa trục đường lớn đông xe, cần cẩn thận khi băng qua để chụp ảnh, và bản thân cổng chủ yếu để ngắm từ bên ngoài.",
        "presentation_short_vi": "Cổng khải hoàn bằng gang đồ sộ ở cửa ngõ phía nam Saint Petersburg — trên trục đường đi Moskva — do kiến trúc sư Vasily Stasov thiết kế, dựng năm 1834–1838 để tôn vinh chiến thắng của quân Nga trong các cuộc chiến với Ba Tư, Thổ Nhĩ Kỳ và cuộc dẹp loạn ở Ba Lan cuối thập niên 1820 - đầu 1830. Khi khánh thành, đây là công trình lớn nhất thế giới được lắp ghép hoàn toàn bằng kim loại.",
        "presentation_long_vi": "Ý tưởng dựng một cổng khải hoàn ở lối vào Saint Petersburg từ hướng Moskva đã có từ thời Ekaterina II, nhưng phải đến đời Nikolai I nó mới thành hình. Kiến trúc sư Vasily Stasov — người trước đó đã dựng lại Khải Hoàn Môn Narva — được giao thiết kế, và công trình được xây trong các năm 1834–1838, khánh thành ngày 16/10/1838. Cổng có hình một hàng cột đôi mười hai cột theo thức Doric (kiểu propylaea), tôn vinh chiến công của quân Nga trong cuộc chiến Nga - Ba Tư (1826–1828), Nga - Thổ Nhĩ Kỳ (1828–1829) và việc dẹp cuộc nổi dậy ở Vương quốc Ba Lan (1830–1831). Điểm đặc biệt là gần như toàn bộ được đúc bằng gang: mỗi cột ghép từ chín khối, tổng khối lượng mười hai cột lên tới khoảng 450 tấn; phía trên là dải phù điêu gồm 30 pho tượng thần hộ mệnh gò bằng đồng lá, do nhà điêu khắc Boris Orlovsky thực hiện. Vào thời điểm khánh thành, đây là kết cấu kim loại lắp ghép lớn nhất thế giới. Năm 1936 cổng bị tháo dỡ; trong thời kỳ Vây hãm Leningrad, các khối gang được tận dụng làm chướng ngại vật chống tăng ở tuyến phòng thủ phía nam thành phố. Cổng được phục dựng lại trong các năm 1958–1960 và nay đứng ngay lối ra ga metro cùng tên, rất dễ ghé thăm.",
        "highlights_vi": [
            "Do kiến trúc sư Vasily Stasov thiết kế, dựng năm 1834–1838, tôn vinh chiến thắng của quân Nga trước Ba Tư, Thổ Nhĩ Kỳ và trong cuộc dẹp loạn ở Ba Lan.",
            "Hàng propylaea mười hai cột Doric đúc bằng gang — công trình kim loại lắp ghép lớn nhất thế giới khi khánh thành; phù điêu 30 thần hộ mệnh bằng đồng của Boris Orlovsky.",
            "Từng bị tháo dỡ năm 1936 và dùng gang làm chướng ngại chống tăng thời Vây hãm Leningrad; được phục dựng trong các năm 1958–1960."
        ],
        "practical": {
            "hours_vi": "Đài tưởng niệm ngoài trời — có thể ngắm và chụp ảnh mọi lúc.",
            "ticket_vi": "Miễn phí.",
            "duration_vi": "Khoảng 15–20 phút.",
            "best_time_vi": "Ban ngày để thấy rõ chi tiết cột gang và dải phù điêu đồng; buổi tối cổng được chiếu sáng khá đẹp.",
            "tips_vi": "Xuống ga metro Moskovskie Vorota là tới ngay chân cổng. Cổng nằm giữa đại lộ Moskovsky nhiều xe cộ, chú ý an toàn khi băng đường để tới gần chụp ảnh; có thể kết hợp tham quan Quảng trường Moskovskaya và tòa Nhà Xô-viết ở gần đó."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.3192,59.8914&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.8914,30.3192"
        },
        "official_site": None,
        "sources": [
            {"title": "Moscow Triumphal Gate — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Moscow_Triumphal_Gate"},
            {"title": "Московские триумфальные ворота — Википедия (RU)", "url": "https://ru.wikipedia.org/wiki/Московские_триумфальные_ворота"},
            {"title": "The Moscow Gate in St. Petersburg — Saint-Petersburg.com", "url": "http://www.saint-petersburg.com/monuments/moscow-gate/"}
        ],
        "tags": ["monument", "arch", "cast-iron", "history", "military", "outdoor", "free"],
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia"
    },
    {
        "id": "saint-petersburg-sampson-cathedral",
        "slug": "sampson-cathedral",
        "region": "saint-petersburg",
        "region_name_vi": "Saint Petersburg",
        "federal_district": "Thành phố trực thuộc liên bang",
        "name_vi": "Nhà thờ Chính toà Thánh Sampson Hiếu Khách (Sampsonievsky Sobor)",
        "name_ru": "Сампсониевский собор",
        "name_en": "Saint Sampson's Cathedral",
        "categories": ["church"],
        "coordinates": {"lat": 59.9684, "lon": 30.3428},
        "address_vi": "Đại lộ Bolshoy Sampsonievsky, số 41, quận Vyborgsky, Saint Petersburg; gần ga tàu điện ngầm Vyborgskaya.",
        "rating": None,
        "review_summary_vi": "Nhiều du khách bất ngờ thú vị khi khám phá một nhà thờ cổ, yên tĩnh và được trùng tu đẹp mắt nằm ngoài lộ trình du lịch quen thuộc, đặc biệt khen bộ khám thờ dát vàng và không khí tĩnh lặng. Vì nằm ở khu Vyborg cách trung tâm nên cần đi thêm một quãng; đây là điểm phù hợp với người quan tâm kiến trúc và lịch sử nhà thờ Nga hơn là khách chỉ ghé nhanh.",
        "presentation_short_vi": "Một trong những nhà thờ cổ nhất còn tồn tại ở Saint Petersburg, mang sắc xanh lam - trắng đặc trưng cùng tháp chuông thanh mảnh. Nhà thờ khởi nguồn từ năm 1709 để ghi công chiến thắng Poltava trước quân Thụy Điển — trận đánh diễn ra đúng ngày lễ Thánh Sampson; công trình bằng đá hiện nay hoàn thành năm 1740 và nay là bảo tàng thuộc quần thể Nhà thờ Thánh Isaac.",
        "presentation_long_vi": "Năm 1709, để tạ ơn chiến thắng vang dội trước quân Thụy Điển trong trận Poltava — diễn ra đúng ngày lễ Thánh Sampson Hiếu Khách (27/6) — Pyotr Đại đế cho dựng một nhà thờ gỗ ở vùng ven phía bắc thành phố non trẻ. Bên cạnh là một trong những nghĩa trang đầu tiên của Saint Petersburg, nơi an nghỉ của nhiều nhân vật ngoại quốc lỗi lạc từng phụng sự nước Nga như nhà điêu khắc Carlo Rastrelli, kiến trúc sư Domenico Trezzini và ngự y Blumentrost. Đến năm 1740, nhà thờ đá cùng tháp chuông thay cho công trình gỗ; tuy không còn lưu tên kiến trúc sư, nhiều ý kiến cho rằng đó là tác phẩm của Trezzini. Ban đầu chỉ có một vòm trung tâm, đến năm 1761 nhà thờ được bổ sung bốn vòm nhỏ theo lối Nga truyền thống. Bên trong còn giữ bộ khám thờ chạm trổ dát vàng thế kỷ 18 cùng nhiều icon quý từ thế kỷ 17–18. Cuối thập niên 1930, nhà thờ bị đóng cửa, nội thất bị dỡ bỏ và biến thành kho chứa rau, còn tượng Pyotr Đại đế trước cổng thì bị chuyển đi. Từ thập niên 1970, Bảo tàng Nhà thờ Thánh Isaac tiếp quản và trùng tu toàn diện; từ năm 2002 nhà thờ hoạt động tôn giáo trở lại, và năm 2006 một bản sao tượng Pyotr Đại đế được dựng lại phía trước.",
        "highlights_vi": [
            "Một trong những nhà thờ cổ nhất còn tồn tại của Saint Petersburg; khởi nguồn năm 1709 để ghi công chiến thắng Poltava, công trình đá hoàn thành năm 1740.",
            "Kiến trúc Baroque xanh lam - trắng với tháp chuông đẹp; ban đầu một vòm, thêm bốn vòm nhỏ kiểu Nga năm 1761; bên trong có khám thờ dát vàng thế kỷ 18 và nhiều icon cổ.",
            "Nay là bảo tàng thuộc quần thể Nhà thờ Thánh Isaac; phía trước có tượng đài Pyotr Đại đế (bản sao dựng lại năm 2006)."
        ],
        "practical": {
            "hours_vi": "Mở cửa hằng ngày, khoảng 11:00–19:00 (nhận khách vào lần cuối lúc 18:00). Nên kiểm tra lại lịch của Bảo tàng Nhà thờ Thánh Isaac trước khi đi.",
            "ticket_vi": "Có vé vào tham quan với mức phí nhỏ; thuê máy thuyết minh (audio-guide, nhiều thứ tiếng) khoảng 100 rúp. Chụp ảnh thường được miễn phí.",
            "duration_vi": "Khoảng 45–60 phút.",
            "best_time_vi": "Ban ngày để chiêm ngưỡng nội thất và tháp chuông; nhà thờ khá vắng nên thích hợp cho ai muốn tham quan thong thả.",
            "tips_vi": "Nhà thờ nằm ở khu Vyborg, cách trung tâm một quãng — tiện nhất là đi metro tới ga Vyborgskaya rồi đi bộ. Công trình có lối tiếp cận cho xe lăn; có nghi lễ vào cuối tuần và ngày lễ."
        },
        "photo": None,
        "photo_credit": None,
        "maps": {
            "yandex": "https://yandex.com/maps/?pt=30.3428,59.9684&z=17&l=map",
            "google": "https://www.google.com/maps/search/?api=1&query=59.9684,30.3428"
        },
        "official_site": "http://eng.cathedral.ru/sampsonievskii_sobor/",
        "sources": [
            {"title": "Saint Sampson's Cathedral — Wikipedia (EN)", "url": "https://en.wikipedia.org/wiki/Saint_Sampson%27s_Cathedral"},
            {"title": "Cathedral of St. Sampson the Hospitable — Saint-Petersburg.com", "url": "http://www.saint-petersburg.com/cathedrals/st-sampson-cathedral/"},
            {"title": "St. Sampson Cathedral — Advantour", "url": "https://www.advantour.com/russia/saint-petersburg/attractions/st-sampson-cathedral.htm"}
        ],
        "tags": ["church", "cathedral", "baroque", "history", "poltava", "museum", "18th-century"],
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
