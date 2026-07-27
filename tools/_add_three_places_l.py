# -*- coding: utf-8 -*-
"""_add_three_places_l.py — Bổ sung 3 địa điểm nổi tiếng/hiện đại còn thiếu (lần chạy tự động 2026-07-26, đợt l).

Thêm:
  1) Moskva            — Tượng đài Pyotr Đại đế (Tsereteli, 1997), tượng ~98 m bên sông Moskva.
  2) Saint Petersburg  — Cung điện Mùa Hè của Pyotr Đại đế (1710–1714), toà nhà cổ nhất thành phố.
  3) Saint Petersburg  — Phố Kiến trúc sư Rossi (Ulitsa Zodchego Rossi), phố tân cổ điển tỉ lệ hoàn hảo.

Nội dung tiếng Việt NGUYÊN GỐC (không dịch/sao chép nguyên văn). Toạ độ thật đã kiểm chứng qua web.
Chạy:  python3 tools/_add_three_places_l.py
"""
import json, os, datetime, urllib.parse

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
        "moscow", "peter-the-great-statue",
        "Tượng đài Pyotr Đại đế (Pi-ốt Đại đế)",
        "Памятник Петру I",
        "Monument to Peter the Great (Peter the Great Statue)",
        ["monument"],
        55.7386, 37.6083,
        "Mũi phía tây đảo Balchug (đảo Bolotny), nơi sông Moskva tách khỏi kênh Vodootvodny, quận Yakimanka — gần cụm nhà máy Tháng Mười Đỏ, đối diện Nhà thờ Chúa Cứu Thế.",
        "Bức tượng đồng khổng lồ cao khoảng 98 m vươn lên từ một hòn đảo nhỏ giữa sông Moskva — một trong những tượng đài cao nhất thế giới. Do nhà điêu khắc Zurab Tsereteli dựng năm 1997 để kỷ niệm 300 năm Hải quân Nga, đây là bóng dáng vừa hoành tráng vừa gây tranh cãi bậc nhất của Moskva hiện đại.",
        "Ít công trình nào của Moskva hiện đại lại vừa nổi tiếng vừa bị bàn tán nhiều như tượng đài Pyotr Đại đế. Cao khoảng 98 mét — tương đương toà nhà ba mươi tầng — pho tượng đứng chênh vênh trên mũi đảo Balchug, ngay chỗ dòng Moskva chia đôi ôm lấy kênh Vodootvodny. Tác phẩm do điêu khắc gia Zurab Tsereteli thực hiện và khánh thành năm 1997, nhân dịp kỷ niệm 300 năm ngày thành lập Hải quân Nga — lực lượng do chính Pyotr Đại đế sáng lập. Vị Sa hoàng được tạc trong tư thế đứng trên boong một con tàu, tay nâng cuộn giấy mạ vàng như đang chỉ huy hạm đội, bên dưới là cụm chiến thuyền đồng phun nước. Điều trớ trêu thường được nhắc đến: Pyotr Đại đế vốn không ưa Moskva và đã dời kinh đô về Saint Petersburg, vậy mà lại được dựng tượng đồ sộ ngay giữa lòng thành phố này. Ngay từ khi ra mắt, tượng đã liên tục lọt vào các danh sách 'công trình xấu nhất thế giới', kèm giai thoại dai dẳng (bị tác giả bác bỏ) rằng nó được cải biên từ một pho tượng Christopher Columbus từng bị nhiều nước chối từ. Dù khen hay chê, đây vẫn là một cột mốc thị giác của Moskva — đẹp nhất khi ngắm từ cầu đi bộ Patriarshy, cầu Krymsky hay kè công viên Gorky lúc lên đèn.",
        [
            "Cao khoảng 98 m — một trong những tượng đài cao nhất thế giới; Sa hoàng đứng trên boong tàu, tay nâng cuộn giấy mạ vàng, dưới chân là cụm chiến thuyền đồng.",
            "Khánh thành năm 1997 để kỷ niệm 300 năm Hải quân Nga do Pyotr Đại đế lập — trớ trêu vì ông không ưa Moskva và đã dời đô về Saint Petersburg.",
            "Gây tranh cãi nổi tiếng: nhiều lần bị bình chọn là tượng đài 'xấu nhất thế giới', kèm tin đồn (đã bị bác bỏ) rằng vốn là tượng Columbus được sửa lại.",
        ],
        {
            "hours_vi": "Ngắm ngoài trời 24/7; không có lối cho khách lên đảo hay vào trong bệ tượng.",
            "ticket_vi": "Miễn phí (chỉ ngắm và chụp từ bên ngoài).",
            "duration_vi": "15–30 phút (kết hợp dạo cầu Patriarshy/Krymsky).",
            "best_time_vi": "Hoàng hôn và buổi tối khi tượng lên đèn; hoặc kết hợp đi dạo Muzeon – Tháng Mười Đỏ.",
            "tips_vi": "Góc chụp toàn cảnh đẹp nhất từ cầu đi bộ Patriarshy, cầu Krymsky, kè công viên Gorky hoặc khu Tháng Mười Đỏ đối diện.",
        },
        [
            {"title": "Wikipedia (EN) — Monument to Peter I", "url": "https://en.wikipedia.org/wiki/Monument_to_Peter_I"},
            {"title": "Rusmania — Peter the Great Monument", "url": "https://rusmania.com/central/moscow-federal-city/moscow/yakimanka/within-the-garden-ring-balchug-island/peter-the-great-monument"},
        ],
        ["monument", "landmark", "outdoor", "river", "viewpoint", "free", "modern"],
    ),
    # ------------------------------------------------------ 2. SAINT PETERSBURG
    rec(
        "saint-petersburg", "summer-palace-peter-the-great",
        "Cung điện Mùa Hè của Pyotr Đại đế (Le-tni Dvo-rets)",
        "Летний дворец Петра I",
        "Summer Palace of Peter the Great",
        ["palace", "museum"],
        59.9472, 30.3361,
        "Góc đông bắc Vườn Mùa Hè (Letny Sad), bên sông Fontanka gần chỗ đổ ra sông Neva, quận Trung tâm.",
        "Toà nhà cổ nhất còn nguyên vẹn của Saint Petersburg (1710–1714) và cũng là dinh nghỉ hè giản dị của chính Pyotr Đại đế, nằm khiêm nhường ở góc đông bắc Vườn Mùa Hè. Ngôi nhà hai tầng màu vàng theo lối Hà Lan nay là bảo tàng (chi nhánh Bảo tàng Nga) với nội thất phục dựng đúng thời Pyotr.",
        "Nép mình ở góc đông bắc Vườn Mùa Hè, bên dòng Fontanka gần nơi sông đổ ra Neva, Cung điện Mùa Hè là toà nhà cổ nhất còn nguyên vẹn của Saint Petersburg. Được kiến trúc sư Domenico Trezzini — người cũng dựng Pháo đài Petropavlovskaya — xây trong các năm 1710–1714, đây là nơi Pyotr Đại đế muốn có một mái nhà thật giản dị, thực dụng, đúng gu Hà Lan mà ông ngưỡng mộ. Ngôi nhà hai tầng chỉ vỏn vẹn mười bốn phòng (bảy phòng mỗi tầng): tầng trệt dành cho Sa hoàng, tầng trên cho Hoàng hậu Ekaterina. Dù nhỏ, cung điện lại là nơi 'đi đầu' của cả thành phố: toà nhà bằng đá đầu tiên, có hệ thống nước máy dẫn vào và thoát nước tự chảy đầu tiên, tận dụng chính dòng Fontanka. Mặt tiền được trang trí bằng 29 bức phù điêu ngụ ngôn ca ngợi chiến thắng của nước Nga trong Đại chiến Bắc Âu. Vì không có lò sưởi, cung điện chỉ dùng vào mùa ấm, thường từ tháng Năm đến đầu mùa thu. Ngày nay là bảo tàng tái hiện căn hộ riêng, gian bếp và xưởng tiện gỗ mà Sa hoàng ưa thích — một trong những ô cửa thân mật nhất để nhìn vào đời sống thường ngày của vị vua cải cách nước Nga.",
        [
            "Toà nhà cổ nhất còn nguyên vẹn của Saint Petersburg (1710–1714), do Domenico Trezzini xây — dinh nghỉ hè giản dị của Pyotr Đại đế theo lối Hà Lan.",
            "Hàng loạt cái 'đầu tiên' của thành phố: toà nhà bằng đá đầu tiên, có nước máy dẫn vào và hệ thống thoát nước tự chảy đầu tiên nhờ dòng Fontanka.",
            "Mặt tiền gắn 29 bức phù điêu ngụ ngôn ca ngợi chiến thắng trong Đại chiến Bắc Âu; nội thất được phục dựng đúng thời Pyotr Đại đế.",
        ],
        {
            "hours_vi": "Thường chỉ mở mùa ấm (khoảng tháng 5–tháng 9), đóng khi độ ẩm cao; giờ tham khảo 10:00–18:00 và nghỉ một ngày trong tuần — nên kiểm tra lịch Bảo tàng Nga trước khi đến.",
            "ticket_vi": "Vé riêng của Bảo tàng Nhà nước Nga (chi nhánh); vào Vườn Mùa Hè thì miễn phí.",
            "duration_vi": "30–45 phút.",
            "best_time_vi": "Mùa hè (tháng 6–8), kết hợp dạo Vườn Mùa Hè.",
            "tips_vi": "Cung điện chỉ mở mùa ấm và giới hạn khách; nên đi buổi sáng, kết hợp Vườn Mùa Hè, Lâu đài Mikhailovsky và Cánh đồng Sao Hoả gần đó.",
        },
        [
            {"title": "Wikipedia (EN) — Summer Palace of Peter the Great", "url": "https://en.wikipedia.org/wiki/Summer_Palace_of_Peter_the_Great"},
            {"title": "Encyclopaedia Britannica — Summer Palace", "url": "https://www.britannica.com/place/Summer-Palace-Saint-Petersburg-Russia"},
            {"title": "saint-petersburg.com — Summer Palace", "url": "http://www.saint-petersburg.com/palaces/summer-palace-of-peter-the-great/"},
        ],
        ["palace", "museum", "history", "peter-the-great", "summer-garden", "indoor"],
    ),
    # ------------------------------------------------------ 3. SAINT PETERSBURG
    rec(
        "saint-petersburg", "rossi-street",
        "Phố Kiến trúc sư Rossi (U-li-txa Zod-che-vo Rossi)",
        "Улица зодчего Росси",
        "Architect Rossi Street (Ulitsa Zodchego Rossi)",
        ["square_street"],
        59.9305, 30.3361,
        "Nối Quảng trường Ostrovsky (sau lưng Nhà hát Alexandrinsky) tới Quảng trường Lomonosov, quận Trung tâm.",
        "Có lẽ là con phố cân đối bậc nhất nước Nga: hai dãy nhà tân cổ điển giống hệt nhau soi gương qua lòng đường, do kiến trúc sư Carlo Rossi thiết kế (1828–1834) với tỉ lệ 'vàng' — dài 220 m, cao 22 m, rộng đúng 22 m. Đây cũng là nơi toạ lạc của Học viện Ba lê Vaganova lừng danh thế giới.",
        "Ngắn nhưng gần như hoàn hảo, phố Kiến trúc sư Rossi là bài học sống động về sự hài hoà của kiến trúc tân cổ điển. Được Carlo Rossi — kiến trúc sư gốc Ý đứng sau nhiều quần thể tráng lệ của kinh đô Nga — thiết kế và xây dựng trong các năm 1828–1834, con phố gồm hai dãy nhà ba tầng giống hệt nhau, đối xứng tuyệt đối qua trục đường ở giữa. Tỉ lệ tuân theo quy chuẩn cổ điển một cách nghiêm ngặt đến mức được ví như tỉ lệ vàng: nhà cao 22 m, lòng đường rộng đúng 22 m, còn chiều dài 220 m thì gấp tròn mười lần chiều rộng. Những hàng cột Doric ghép đôi, gam màu vàng nhạt điểm trắng đồng nhất khiến cả con phố như một dàn đồng ca kiến trúc. Phố chạy từ Quảng trường Ostrovsky — ngay sau lưng Nhà hát Alexandrinsky — tới Quảng trường Lomonosov, là một phần trong quần thể đô thị đồ sộ mà Rossi tạo dựng. Toà nhà số 2 từ năm 1836 đã là trụ sở của Học viện Ba lê Nga Vaganova, cái nôi đào tạo những huyền thoại như Anna Pavlova, Nijinsky, Nureyev và Baryshnikov; nơi đây còn có Thư viện – Bảo tàng Sân khấu của thành phố. Yên tĩnh và cực kỳ ăn ảnh, con phố (mang tên Rossi từ năm 1923) là điểm dừng chân yêu thích của giới nhiếp ảnh.",
        [
            "Tỉ lệ chuẩn mực đến mức lý tưởng: cao 22 m, rộng 22 m, dài 220 m (gấp mười lần) — mẫu mực của kiến trúc tân cổ điển do Carlo Rossi dựng (1828–1834).",
            "Hai dãy nhà giống hệt nhau soi gương qua lòng đường — một trong những cảnh phố đối xứng đẹp nhất thế giới.",
            "Toà nhà số 2 là trụ sở Học viện Ba lê Nga Vaganova từ năm 1836 — nơi đào tạo Anna Pavlova, Nijinsky, Nureyev và Baryshnikov.",
        ],
        {
            "hours_vi": "Phố ngoài trời, tham quan tự do 24/7 (Học viện Vaganova không mở cho khách vãng lai).",
            "ticket_vi": "Miễn phí.",
            "duration_vi": "15–30 phút.",
            "best_time_vi": "Sáng sớm khi phố còn vắng, dễ chụp toàn cảnh đối xứng.",
            "tips_vi": "Kết hợp Nhà hát Alexandrinsky, Quảng trường Ostrovsky (tượng đài Ekaterina II) và Đại lộ Nevsky ngay cạnh.",
        },
        [
            {"title": "Wikipedia (EN) — 2 Rossi Street", "url": "https://en.wikipedia.org/wiki/2_Rossi_Street"},
            {"title": "saint-petersburg.com — Ulitsa Zodchego Rossi", "url": "http://www.saint-petersburg.com/streets/zodchego-rossi-street/"},
        ],
        ["street", "architecture", "neoclassical", "ballet", "free", "outdoor", "photo"],
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
