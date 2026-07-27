# -*- coding: utf-8 -*-
"""_add_three_places_m.py — Bổ sung 3 địa điểm nổi tiếng/hiện đại còn thiếu (lần chạy tự động 2026-07-26, đợt m).

Thêm:
  1) Moskva            — Cáp treo Đồi Chim Sẻ (Московская канатная дорога, 2018), cáp treo chở khách đầu tiên của Moskva.
  2) Moskva            — Tháp Menshikov / Nhà thờ Tổng lãnh thiên thần Gabriel (1704–1707), công trình baroque Petrine cổ nhất Moskva.
  3) Saint Petersburg  — Chizhik-Pyzhik (1994), đài kỷ niệm nhỏ nhất thành phố bên sông Fontanka.

Nội dung tiếng Việt NGUYÊN GỐC (không dịch/sao chép nguyên văn). Toạ độ thật đã kiểm chứng qua web.
Chạy:  python3 tools/_add_three_places_m.py
"""
import json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
QUEUE = os.path.join(ROOT, "_source", "regions_queue.json")
TODAY = "2026-07-26"
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

RMETA = {}
if os.path.exists(QUEUE):
    for r in json.load(open(QUEUE, encoding="utf-8")).get("regions", []):
        RMETA[r["slug"]] = (r.get("name_vi", r["slug"]), r.get("federal_district", ""))


def maps_for(lat, lon):
    return {
        "yandex": f"https://yandex.com/maps/?pt={lon},{lat}&z=17&l=map",
        "google": f"https://www.google.com/maps/search/?api=1&query={lat},{lon}",
    }


def rec(region, slug, name_vi, name_ru, name_en, cats, lat, lon, addr,
        short, long, hl, practical, sources, tags, official_site=None):
    nv, fed = RMETA.get(region, (region, ""))
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
        "maps": maps_for(lat, lon), "official_site": official_site,
        "sources": sources, "tags": tags, "status": "enriched",
        "last_updated": TODAY, "country": "russia",
    }


NEW = [
    # ---------------------------------------------------------------- 1. MOSKVA
    rec(
        "moscow", "vorobyovy-gory-cable-car",
        "Cáp treo Đồi Chim Sẻ (Moskovskaya Kanatnaya Doroga)",
        "Московская канатная дорога",
        "Moskva River Cable Car (Vorobyovy Gory)",
        ["other"],
        55.708113, 37.545471,
        "Ga trên ('Vorobyovy Gory') ở phố Kosygina 28, Đồi Chim Sẻ; nối sang ga dưới ở khu liên hợp thể thao Luzhniki bên kia sông Moskva, quận Ramenki/Khamovniki.",
        "Tuyến cáp treo chở khách đầu tiên của Moskva, khánh thành cuối năm 2018, dài 720 m vắt qua sông Moskva — nối đài ngắm cảnh trên Đồi Chim Sẻ với sân vận động Luzhniki. Cabin kính tám chỗ đưa du khách lơ lửng trên mặt sông, thu vào tầm mắt toàn cảnh Luzhniki, cụm cao ốc Moskva-City và tòa nhà chính Đại học MGU.",
        "Là cáp treo chở khách đầu tiên trong lịch sử Moskva, tuyến Vorobyovy Gory – Luzhniki khánh thành cuối tháng 11/2018 và nhanh chóng trở thành một cách ngắm thành phố kiểu mới. Đường cáp dài 720 m bắc qua sông Moskva với ba ga: ga trên 'Vorobyovy Gory' ngay cạnh đài ngắm cảnh nổi tiếng trên Đồi Chim Sẻ, ga giữa 'Novaya Liga' và ga dưới 'Luzhniki' bên chân sân vận động. Những chiếc cabin kính do hãng Bartholet (Thụy Sĩ) cung cấp thiết bị, lắp ráp tại Nga, mỗi cabin chở tám khách, có sưởi, màn hình thông tin và cả móc treo ván trượt cho mùa đông; ngoài ra còn có cabin hạng Premium với ghế bọc da cho các dịp đặc biệt. Mỗi lượt 'bay' chỉ vài phút nhưng mở ra góc nhìn hiếm có: phía dưới là dòng Moskva, một bên là lòng chảo sân Luzhniki, xa xa là những tòa tháp chọc trời của Moskva-City và ngọn tháp tân cổ điển của MGU trên đỉnh đồi. Khung cảnh đẹp nhất vào lúc hoàng hôn và khi thành phố lên đèn; mùa đông, đồi Chim Sẻ còn biến thành điểm trượt tuyết ngay trong lòng thủ đô. Có thể tới bằng metro (Vorobyovy Gory, Sportivnaya) hoặc tuyến vòng MCC (ga Luzhniki), rồi kết hợp tham quan đài ngắm cảnh và khuôn viên MGU ngay cạnh.",
        [
            "Cáp treo chở khách đầu tiên của Moskva, khánh thành tháng 11/2018; tuyến dài 720 m với ba ga, cabin kính tám chỗ có sưởi và màn hình.",
            "Từ cabin (hoặc từ đài ngắm Đồi Chim Sẻ) mở ra toàn cảnh sân Luzhniki, cụm cao ốc Moskva-City, sông Moskva và tòa nhà chính MGU.",
            "Mùa đông, Đồi Chim Sẻ thành điểm trượt tuyết/ván ngay trong thành phố — cabin có móc treo ván; cảnh đẹp nhất lúc hoàng hôn và khi lên đèn.",
        ],
        {
            "hours_vi": "Thường mở khoảng 11:00–23:00; có thể nghỉ một buổi/ngày trong tuần để bảo trì — nên xem lịch chính thức trước khi đi.",
            "ticket_vi": "Có thu phí (vé một chiều/khứ hồi, có hạng cabin Premium); mua qua thẻ Troika hoặc tại quầy. Giá thay đổi theo mùa và loại vé — nên tra giá mới nhất trên trang chính thức.",
            "duration_vi": "Mỗi lượt bay khoảng 5 phút; cả trải nghiệm 30–45 phút.",
            "best_time_vi": "Hoàng hôn và buổi tối khi thành phố lên đèn; mùa đông tuyết phủ rất ảo diệu.",
            "tips_vi": "Đi metro tới Vorobyovy Gory hoặc Sportivnaya, hoặc ga MCC Luzhniki; kết hợp đài ngắm cảnh Đồi Chim Sẻ và tòa nhà chính MGU ngay cạnh.",
        },
        [
            {"title": "Wikipedia (EN) — Moskva River Cable Car", "url": "https://en.wikipedia.org/wiki/Moskva_River_Cable_Car"},
            {"title": "The Moscow Times — Moscow Opens First-Ever Cable Car Line at Luzhniki", "url": "https://www.themoscowtimes.com/2018/11/26/moscow-opens-first-ever-cable-car-line-luzhniki-a63604"},
            {"title": "Luzhniki (trang chính thức) — Moscow ropeway in Luzhniki", "url": "https://eng.luzhniki.ru/news/moscow-ropeway-luzhniki/"},
        ],
        ["cable_car", "modern", "viewpoint", "river", "panorama", "family", "winter"],
    ),
    # ---------------------------------------------------------------- 2. MOSKVA
    rec(
        "moscow", "menshikov-tower",
        "Tháp Menshikov – Nhà thờ Tổng lãnh thiên thần Gabriel (Men-si-cốp)",
        "Меншикова башня (Церковь Архангела Гавриила)",
        "Menshikov Tower (Church of the Archangel Gabriel)",
        ["church", "monument"],
        55.7614, 37.6389,
        "Ngõ Arkhangelsky (Arkhangelsky pereulok) 15a, quận Basmanny, gần Ao Trong (Chistye Prudy) — trong vành đai Đại lộ (Bulvarnoye Koltso), Moskva.",
        "Nhà thờ – tháp chuông baroque cao vút do Hoàng thân Aleksandr Menshikov, sủng thần của Pyotr Đại đế, cho dựng năm 1704–1707 gần Ao Trong. Đây là công trình baroque Petrine (phong cách thời Pyotr Đại đế) cổ nhất còn lại ở Moskva; ban đầu cao 81 m — ngang Tháp chuông Ivan Đại đế trong Kremlin — và là tòa nhà cao nhất thành phố thời bấy giờ.",
        "Nép trong một con ngõ yên tĩnh gần Ao Trong, Tháp Menshikov là một trong những viên ngọc kiến trúc ít được du khách để ý nhất của Moskva. Nhà thờ mang tên Tổng lãnh thiên thần Gabriel được Hoàng thân Aleksandr Menshikov — cánh tay phải và bạn thân của Pyotr Đại đế — cho xây lại trong các năm 1704–1707 làm nhà thờ riêng cho dinh thự của mình. Đứng đầu công trình là kiến trúc sư Ivan Zarudny, cùng nhóm thợ Ý – Thụy Sĩ đến từ các bang Ticino, Fribourg và thợ đá Nga từ Kostroma, Yaroslavl; kiến trúc sư Domenico Trezzini cũng góp mặt ở giai đoạn đầu trước khi được điều về Saint Petersburg. Khi hoàn thành, tháp cao 81 m, đúng bằng Tháp chuông Ivan Đại đế trong Kremlin, đỉnh gắn chóp nhọn 30 m với hình thiên thần mạ vàng làm chong chóng gió; bên trong treo tới 50 quả chuông và một chiếc đồng hồ điểm chuông kiểu Anh. Là tòa nhà cao nhất Moskva thời đó và cũng là công trình đầu tiên của thành phố được trang trí dày đặc tượng điêu khắc, người dân quen gọi nó là 'em gái của Tháp chuông Ivan Đại đế'. Năm 1723, một tia sét đánh trúng gây hỏa hoạn thiêu rụi toàn bộ phần chóp gỗ và bộ đồng hồ, chuông rơi xuống làm sập trần; ngọn tháp cụt đầu suốt nửa thế kỷ cho đến khi được phục dựng vào các năm 1773–1780 với mái vòm baroque nhỏ gọn như ta thấy hôm nay. Tháp thuộc kiểu nhà thờ hiếm gặp 'chuông đặt trên thân' (izhe pod kolokoly); trớ trêu là ngày nay chính nó lại không còn chuông — việc rung chuông do nhà thờ Feodor Stratilat kế bên (nhà thờ mùa đông) đảm nhiệm. Công trình may mắn thoát trận hỏa hoạn năm 1812, được xếp hạng di tích kiến trúc cấp liên bang, và hiện là nhà thờ Chính thống đang hoạt động — đại diện (podvorye) của Giáo hội Chính thống Antioch tại Moskva.",
        [
            "Công trình baroque Petrine cổ nhất còn lại ở Moskva, do Hoàng thân Menshikov cho dựng 1704–1707, kiến trúc sư Ivan Zarudny cùng thợ Ý – Thụy Sĩ và thợ đá Nga.",
            "Ban đầu cao 81 m — ngang Tháp chuông Ivan Đại đế — và là tòa nhà cao nhất Moskva; đỉnh gắn thiên thần mạ vàng, có 50 chuông và đồng hồ điểm chuông kiểu Anh.",
            "Năm 1723 bị sét đánh cháy rụi phần chóp gỗ; phục dựng thập niên 1770 với mái vòm baroque hiện nay. Nay là nhà thờ đang hoạt động (đại diện Giáo hội Antioch tại Moskva).",
        ],
        {
            "hours_vi": "Nhà thờ Chính thống đang hoạt động; mở cửa ban ngày và trong giờ lễ. Nên mặc trang phục lịch sự, nữ nên trùm khăn.",
            "ticket_vi": "Miễn phí (có thể quyên góp tuỳ tâm).",
            "duration_vi": "20–30 phút.",
            "best_time_vi": "Ban ngày để ngắm rõ chi tiết điêu khắc baroque; kết hợp dạo Ao Trong.",
            "tips_vi": "Đi metro Chistye Prudy / Turgenevskaya / Sretensky Bulvar; tháp nằm khuất trong ngõ Arkhangelsky — kết hợp Ao Trong và Đại lộ Chistoprudny gần đó.",
        },
        [
            {"title": "Wikipedia (EN) — Menshikov Tower", "url": "https://en.wikipedia.org/wiki/Menshikov_Tower"},
            {"title": "mos.ru — Styled in Petrine Baroque: the uniqueness of Menshikov Tower", "url": "https://www.mos.ru/en/news/item/95092073/"},
            {"title": "Rusmania — Menshikov Tower and St Theodore Stratelates' Church", "url": "https://rusmania.com/central/moscow-federal-city/moscow/krasnoselsky/around-the-boulevard-ring-chistoprudny-bulvar/menshikov-tower-and-st-theodore-stratelates-church"},
        ],
        ["church", "baroque", "petrine_baroque", "landmark", "architecture", "free", "historic"],
    ),
    # ------------------------------------------------------ 3. SAINT PETERSBURG
    rec(
        "saint-petersburg", "chizhik-pyzhik",
        "Chizhik-Pyzhik (chú chim tí hon bên sông Fontanka)",
        "Чижик-Пыжик",
        "Chizhik-Pyzhik",
        ["monument"],
        59.941667, 30.337778,
        "Kè sông Fontanka, cạnh Cầu Kỹ sư số 1 (Panteleymonovsky most), gần chỗ sông Moika tách khỏi Fontanka — đối diện Lâu đài Mikhailovsky và Vườn Mùa Hè, quận Trung tâm.",
        "Đài kỷ niệm nhỏ nhất Saint Petersburg: chú chim chizh (một loài sẻ ria/hồng tước) bằng đồng chỉ cao 11 cm, đậu trên gờ đá kè sông Fontanka ngay cạnh Cầu Panteleymonovsky. Được đặt năm 1994, chú chim tí hon gắn với một bài đồng dao trứ danh và tục ném đồng xu cầu may khiến ai đi ngang cũng nán lại thử vận.",
        "Giữa những cung điện và nhà thờ tráng lệ của Saint Petersburg, có một 'nhân vật' bé xíu lại được yêu mến bậc nhất: Chizhik-Pyzhik. Đó là tượng đồng một chú chim chizh cao vỏn vẹn 11 cm, đậu trên một mấu đá nhô ra từ bức tường kè granite của sông Fontanka, ngay dưới chân Cầu Kỹ sư số 1 (Panteleymonovsky), tại khúc sông Moika bắt đầu tách khỏi Fontanka. Bức tượng ra đời ngày 19/11/1994 trong khuôn khổ liên hoan hài hước 'Ostap Vàng', theo ý tưởng của nhà văn Andrei Bitov, do nghệ sĩ người Gruzia Revaz Gabriadze (người sáng lập Nhà hát Múa rối Tbilisi) tạo hình và kiến trúc sư Vyacheslav Bukhaev thực hiện. Cái tên ngộ nghĩnh bắt nguồn từ biệt danh của sinh viên Trường Luật Hoàng gia (hoạt động 1835–1918) từng đóng đô ngay gần đó bên bờ Fontanka: đồng phục của họ màu xanh lá điểm vàng, mùa đông đội mũ lông 'pyzhik' — trông hệt bộ lông chim chizh, nên bị gọi vui là 'chizhiki-pyzhiki', và từ đó có bài đồng dao 'Chizhik-pyzhik, mày đã ở đâu?'. Ngày nay du khách truyền nhau một tục lệ: đứng trên cầu tung một đồng xu, nếu xu đậu lại được trên bệ đá tí hon mà không rơi xuống nước thì điều ước sẽ thành. Vì quá nhỏ và quá nổi tiếng, chú chim từng nhiều lần bị kẻ gian lấy trộm rồi lại được đúc và dựng lại. Tượng thấp và dễ bỏ lỡ — hãy nhìn xuống lan can phía kè Fontanka gần cầu; tiện đường có thể kết hợp Vườn Mùa Hè, Lâu đài Mikhailovsky, Cánh đồng Sao Hỏa và Nhà thờ trên Máu Đổ.",
        [
            "Cao vỏn vẹn 11 cm — đài kỷ niệm nhỏ nhất Saint Petersburg — đậu trên gờ đá kè sông Fontanka, dễ bỏ lỡ nếu không nhìn xuống lan can gần Cầu Panteleymonovsky.",
            "Đặt năm 1994 (ý tưởng của nhà văn Andrei Bitov, tạo hình bởi nghệ sĩ Revaz Gabriadze); lấy cảm hứng từ biệt danh 'chizhik-pyzhik' của sinh viên Trường Luật Hoàng gia gần đó và bài đồng dao cùng tên.",
            "Tục ném đồng xu: ai tung được xu đậu lại trên bệ mà không rơi xuống nước sẽ gặp may — tượng từng nhiều lần bị lấy trộm rồi lại được dựng lại.",
        ],
        {
            "hours_vi": "Ngoài trời, xem tự do 24/7 (nên tới ban ngày cho dễ tìm và an toàn).",
            "ticket_vi": "Miễn phí (mang theo vài đồng xu để thử vận may).",
            "duration_vi": "5–10 phút.",
            "best_time_vi": "Ban ngày; kết hợp trong lịch trình quanh Vườn Mùa Hè – Lâu đài Mikhailovsky.",
            "tips_vi": "Tượng nằm thấp dưới chân cầu Panteleymonovsky phía kè Fontanka — nhìn qua lan can xuống sát mặt nước. Kết hợp Vườn Mùa Hè, Cánh đồng Sao Hỏa, Nhà thờ trên Máu Đổ.",
        },
        [
            {"title": "saint-petersburg.com — Statue of Chizhik Pyzhik", "url": "http://www.saint-petersburg.com/monuments/chizhik-pyzhik/"},
            {"title": "Atlas Obscura — Chizhik Pyzhik", "url": "https://www.atlasobscura.com/places/chizhik-pyzhik"},
            {"title": "Rusmania — Chizhi-Pizhi Monument", "url": "https://rusmania.com/north-western/st-petersburg-federal-city/st-petersburg/central-islands/on-spassky-island/chizhi-pizhi-monument"},
        ],
        ["monument", "bronze", "tiny", "folklore", "coin", "free", "outdoor", "quirky"],
    ),
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
        # backup once per file before modifying
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
            print(f"[OK] {region}.json -> {len(data)} bản ghi (backup: {os.path.basename(bak)})")
        else:
            os.remove(bak)  # nothing added, drop the useless backup

    print("ĐÃ THÊM:", added or "(không có)")
    print("BỎ QUA (đã tồn tại):", skipped or "(không)")


if __name__ == "__main__":
    main()
