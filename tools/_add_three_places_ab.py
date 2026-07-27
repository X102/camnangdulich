# -*- coding: utf-8 -*-
"""_add_three_places_ab.py — Bổ sung 3 địa điểm còn thiếu (lần chạy tự động 2026-07-26, chiều/tối).

Ưu tiên VÙNG: thành phố/thị trấn phụ cận quanh Moskva & Saint Petersburg.

Thêm:
  1) Tỉnh Moskva (moscow-oblast)      : Điền trang Marfino - lâu đài tân Gothic (palace/park_garden/church)
  2) Tỉnh Moskva (moscow-oblast)      : Bảo tàng - Điền trang Muranovo (Tyutchev) (museum/park_garden/church)
  3) Tỉnh Leningrad (leningrad-oblast): Đài tưởng niệm «Vòng tròn Bị phá vỡ» - Con đường Sự sống (monument)

LƯU Ý:
  - Cung điện Gatchina & Priory Palace KHÔNG thêm ở đây vì đã có sẵn trong saint-petersburg.json
    (slug 'gatchina-palace', 'priory-palace') — tránh trùng.
  - Đã đối chiếu để chắc chắn 3 slug dưới đây CHƯA tồn tại trong data/regions.

Nội dung tiếng Việt nguyên gốc (paraphrase, không sao chép nguyên văn), có ghi nguồn.
Toạ độ THẬT (đối chiếu web 2026-07: Wikipedia EN/RU + Thư viện Tổng thống Nga + nguồn du lịch Nga).
Link bản đồ dạng TRỎ-ĐỊA-ĐIỂM (khớp convention tools/retrofit_map_links.py: Yandex tìm theo
tên Nga + vùng, canh giữa bằng ll=lon,lat).

Chạy:  python3 tools/_add_three_places_ab.py
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-26"


def maps_for(name_ru, name_en, region_ru, region_en, lat, lon):
    """Trỏ thẳng tới địa điểm (khớp tools/retrofit_map_links.py để idempotent)."""
    yq = urllib.parse.quote(f"{name_ru}, {region_ru}")
    parts = [name_en]
    if region_en.lower() not in name_en.lower():
        parts.append(region_en)
    parts.append("Russia")
    gq = urllib.parse.quote(", ".join(parts))
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


# ------------------------------------------------------------------ RECORDS
MARFINO_ESTATE = {
    "id": "moscow-oblast-marfino-estate",
    "slug": "marfino-estate",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Điền trang Marfino (Usadba Marfino)",
    "name_ru": "Усадьба Марфино",
    "name_en": "Marfino Estate",
    "categories": ["palace", "park_garden", "church"],
    "coordinates": {"lat": 56.0805, "lon": 37.5634},
    "address_vi": "Làng Marfino, thành phố (okrug) Mytishchi, Tỉnh Moskva; nằm trên bờ cao sông Ucha, cách vành đai MKAD của Moskva khoảng 25 km về phía bắc.",
    "rating": None,
    "presentation_short_vi": (
        "Marfino là một trong những điền trang quý tộc ngoạn mục nhất vùng ngoại ô Moskva, nổi bật "
        "với toà lâu đài chính bằng gạch đỏ mang phong cách tân Gothic (neo-Gothic) do kiến trúc sư "
        "Mikhail Bykovsky tái thiết trong các năm 1837–1839. Quần thể trải dọc bờ cao sông Ucha, gồm "
        "cung điện, nhà thờ cổ, công viên cảnh quan và cây cầu vòm kiểu Gothic soi bóng xuống hồ - "
        "khung cảnh khiến Marfino trở thành phim trường quen thuộc của điện ảnh Nga."
    ),
    "presentation_long_vi": (
        "Marfino được nhắc đến từ thế kỉ 16, thoạt đầu thuộc dòng họ Golovin, rồi sang tay thư lại "
        "Semyon Zaborovsky (1650) và đến năm 1698 thuộc về Boris Golitsyn - người thầy của vị vua "
        "tương lai Pyotr Đại đế. Chính Golitsyn đã đổi tên làng thành Marfino theo tên vợ ông là "
        "Marfa. Năm 1729 điền trang về tay Bá tước Pyotr Saltykov; dưới thời họ Saltykov, Marfino "
        "trở thành một trung tâm văn hoá với các buổi diễn kịch và hoà nhạc thu hút khách từ Moskva. "
        "Sau năm 1805 điền trang sa sút, rồi bị quân Pháp cướp phá năm 1812 trong cuộc xâm lăng của "
        "Napoléon. Diện mạo lộng lẫy hiện nay ra đời trong các năm 1837–1839, khi kiến trúc sư "
        "Mikhail Bykovsky cải tạo toàn bộ toà nhà chính thành một lâu đài tân Gothic theo tinh thần "
        "«thời Nikolai I»: dinh thự gạch đỏ hai tầng với tường răng cưa, cửa sổ vòm nhọn và hoa văn "
        "ren đá. Từ cung điện, một bậc thang lớn dẫn thẳng xuống hồ; bắc qua hồ là cây cầu vòm kiểu "
        "Gothic - hình ảnh biểu tượng của Marfino - còn ở bến nước là đôi tượng sư tử đầu chim "
        "(griffin) trấn giữ. Công trình cổ nhất còn lại là Nhà thờ Giáng Sinh Đức Mẹ (1707), do "
        "Vladimir Belozerov - một nông nô được Golitsyn gửi sang Pháp học kiến trúc - thiết kế theo "
        "lối gần với Baroque châu Âu. Bao quanh các công trình là một công viên cảnh quan rộng chạy "
        "ven sông Ucha. Sau Cách mạng 1917 điền trang bị quốc hữu hoá; từ năm 1933 được giao cho "
        "quân đội và tới nay là viện điều dưỡng «Marfinsky» của Bộ Quốc phòng Nga - nhờ đó quần thể "
        "được giữ gìn khá tốt và mở cửa cho khách tham quan tự do với mục đích phi thương mại."
    ),
    "highlights_vi": [
        "Cung điện tân Gothic gạch đỏ (Bykovsky, 1837–1839) với tường răng cưa, cửa sổ vòm nhọn và trang trí ren đá.",
        "Cây cầu vòm kiểu Gothic bắc qua hồ cùng bến nước có đôi tượng sư tử đầu chim (griffin) - biểu tượng thị giác của Marfino.",
        "Nhà thờ Giáng Sinh Đức Mẹ (1707) do kiến trúc sư nông nô Vladimir Belozerov thiết kế và công viên cảnh quan ven sông Ucha.",
    ],
    "practical": {
        "hours_vi": "Lãnh thổ điền trang do viện điều dưỡng «Marfinsky» của Bộ Quốc phòng quản lý, mở cho khách tham quan tự do (mục đích phi thương mại) vào ban ngày; nội thất cung điện thường không mở cho khách lẻ.",
        "ticket_vi": "Dạo trong khuôn viên thường miễn phí; nên mang theo giấy tờ tuỳ thân vì đây là khu vực do quân đội quản lý.",
        "duration_vi": "Khoảng 1–1,5 giờ để dạo quanh cung điện, cầu Gothic và công viên.",
        "best_time_vi": "Cuối xuân đến đầu thu khi công viên xanh mát; mùa thu lá vàng cho khung ảnh đẹp.",
        "tips_vi": "Từ Moskva có thể đi tàu ngoại ô hướng Savyolovo tới ga Katuar rồi bắt xe/taxi, hoặc xe buýt từ ga metro Altufyevo. Marfino thường được ghép cùng làng nghề sơn mài Fedoskino ở gần đó.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Усадьба Марфино", "Marfino Estate", "Московская область", "Moscow Oblast", 56.0805, 37.5634),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN) — Marfino, Mytishchinsky District", "url": "https://en.wikipedia.org/wiki/Marfino,_Mytishchinsky_District,_Moscow_Oblast"},
        {"title": "Wikipedia (RU) — Марфино (усадьба)", "url": "https://ru.wikipedia.org/wiki/Марфино_(усадьба)"},
    ],
    "tags": ["estate", "palace", "neo-gothic", "park", "church", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


MURANOVO_ESTATE = {
    "id": "moscow-oblast-muranovo-tyutchev-estate",
    "slug": "muranovo-tyutchev-estate",
    "region": "moscow-oblast",
    "region_name_vi": "Tỉnh Moskva",
    "federal_district": "Vùng Trung tâm",
    "name_vi": "Bảo tàng - Điền trang Muranovo (mang tên F. I. Tyutchev)",
    "name_ru": "Музей-усадьба «Мураново» имени Ф. И. Тютчева",
    "name_en": "Muranovo Estate-Museum (Tyutchev)",
    "categories": ["museum", "park_garden", "church"],
    "coordinates": {"lat": 56.17861, "lon": 37.90250},
    "address_vi": "Làng Muranovo, thành phố (okrug) Pushkino, Tỉnh Moskva; cách Moskva khoảng 50 km về phía đông bắc, gần thị trấn Sofrino.",
    "rating": None,
    "presentation_short_vi": (
        "Muranovo là một trong những bảo tàng văn học lâu đời và được gìn giữ nguyên vẹn bậc nhất "
        "nước Nga, gắn với hai nhà thơ lớn Yevgeny Baratynsky và Fyodor Tyutchev. Toà nhà chính bằng "
        "gỗ độc đáo được dựng năm 1842 theo bản vẽ của chính nhà thơ Baratynsky, đến nay vẫn lưu giữ "
        "gần như nguyên vẹn nội thất, thư viện và di vật của các gia đình chủ nhân."
    ),
    "presentation_long_vi": (
        "Điền trang Muranovo hình thành từ năm 1816 và trải qua bốn dòng họ có quan hệ thân tộc: "
        "Engelhardt, Baratynsky, Putyata và Tyutchev. Năm 1842, nhà thơ Yevgeny Baratynsky tự vẽ "
        "kiểu và cho dựng toà nhà chính hai tầng khác thường - lõi gạch bọc gỗ, giữ ấm tốt trong mùa "
        "đông Nga. Bản thân Baratynsky mất sớm (1844), nhưng điền trang sau đó gắn liền với tên tuổi "
        "Fyodor Tyutchev: sau khi nhà thơ qua đời, con trai ông cùng gia đình đã đưa về Muranovo bàn "
        "làm việc, thư viện, thư từ và nhiều kỷ vật của cha, biến nơi đây thành «điền trang của hai "
        "nhà thơ». Tháng 8 năm 1920, hậu duệ gia đình hiến điền trang thành bảo tàng - một trong "
        "những bảo tàng văn học đầu tiên của nước Nga Xô viết - và điều đặc biệt là phần lớn đồ đạc, "
        "tranh, sách vẫn ở đúng vị trí nguyên bản chứ không phải sưu tập lắp ghép. Tháng 7 năm 2006, "
        "một tia sét đánh trúng đã gây hoả hoạn thiêu rụi gần hết toà nhà chính, song nhờ ứng cứu kịp "
        "thời, gần như toàn bộ hiện vật được cứu; công trình sau đó được trùng tu lại theo nguyên "
        "trạng. Trong khuôn viên còn có Nhà thờ Đấng Cứu Thế Không Bởi Tay Người (Spasa "
        "Nerukotvornogo) cùng một công viên cảnh quan với ao, nhà kho, chuồng ngựa và những lối đi "
        "rợp bóng cây - khiến Muranovo vừa là điểm hành hương văn học, vừa là chốn dạo chơi yên bình "
        "cho chuyến đi trong ngày từ Moskva."
    ),
    "highlights_vi": [
        "Toà nhà gỗ hai tầng dựng năm 1842 theo thiết kế của chính nhà thơ Baratynsky - kiến trúc điền trang độc đáo, lõi gạch bọc gỗ.",
        "Nội thất nguyên gốc cùng thư viện, thư từ và kỷ vật của Tyutchev và Baratynsky - «điền trang của hai nhà thơ».",
        "Nhà thờ Đấng Cứu Thế Không Bởi Tay Người và công viên cảnh quan với ao, lối đi rợp bóng cây.",
    ],
    "practical": {
        "hours_vi": "Thường mở Thứ Tư–Chủ nhật, khoảng 10:00–18:00; nghỉ Thứ Hai và Thứ Ba (nên kiểm tra lịch và ngày vệ sinh cuối tháng trước khi đến). Tham quan toà nhà chính thường theo đoàn có hướng dẫn.",
        "ticket_vi": "Có bán vé vào khu điền trang và vé riêng cho tour nội thất; nhiều mức ưu đãi cho học sinh, sinh viên và người cao tuổi.",
        "duration_vi": "Khoảng 1,5–2 giờ cho nhà chính, nhà thờ và công viên.",
        "best_time_vi": "Cuối xuân đến đầu thu; khuôn viên đặc biệt đẹp vào mùa thu lá vàng.",
        "tips_vi": "Từ ga Yaroslavsky (Moskva) đi tàu ngoại ô tới ga Sofrino hoặc Ashukinskaya, rồi bắt xe buýt/taxi tới Muranovo. Có thể kết hợp với tu viện gần Sofrino hoặc điền trang Abramtsevo trong cùng hướng đông bắc.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Музей-усадьба «Мураново»", "Muranovo Estate Museum", "Московская область", "Moscow Oblast", 56.17861, 37.90250),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (EN) — Muranovo", "url": "https://en.wikipedia.org/wiki/Muranovo"},
        {"title": "Museum.ru — Государственный музей-усадьба «Мураново» им. Ф. И. Тютчева", "url": "http://www.museum.ru/muranovo/"},
        {"title": "Wikidata — Muranovo (Q4163696)", "url": "https://www.wikidata.org/wiki/Q4163696"},
    ],
    "tags": ["estate", "museum", "literary", "tyutchev", "baratynsky", "park", "day-trip", "moscow-oblast"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


BROKEN_RING = {
    "id": "leningrad-oblast-broken-ring-memorial",
    "slug": "broken-ring-memorial",
    "region": "leningrad-oblast",
    "region_name_vi": "Tỉnh Leningrad",
    "federal_district": "Vùng Tây Bắc",
    "name_vi": "Đài tưởng niệm «Vòng tròn Bị phá vỡ» (Razorvannoye Koltso)",
    "name_ru": "Мемориал «Разорванное кольцо»",
    "name_en": "Broken Ring Memorial (Road of Life)",
    "categories": ["monument"],
    "coordinates": {"lat": 60.08148, "lon": 31.06767},
    "address_vi": "Km số 40 đường «Con đường Sự sống» (Doroga Zhizni), gần làng Kokkorevo, huyện Vsevolozhsk, Tỉnh Leningrad; nằm ngay bên bờ tây hồ Ladoga.",
    "rating": None,
    "presentation_short_vi": (
        "«Vòng tròn Bị phá vỡ» là một trong những tượng đài Thế chiến II nổi tiếng nhất nước Nga, "
        "dựng năm 1966 bên bờ hồ Ladoga. Hai vòm bê tông khổng lồ tách rời nhau tượng trưng cho vòng "
        "vây phong toả Leningrad, còn khoảng trống ở giữa chính là «Con đường Sự sống» - tuyến tiếp "
        "tế băng qua mặt hồ đóng băng đã cứu sống thành phố trong những năm bị vây hãm."
    ),
    "presentation_long_vi": (
        "Cuộc phong toả Leningrad bắt đầu ngày 8 tháng 9 năm 1941, khi quân Đức chiếm Shlisselburg và "
        "cắt đứt mọi tuyến đường bộ nối thành phố với phần còn lại của đất nước. Hồ Ladoga trở thành "
        "lối tiếp tế cuối cùng: mùa đông, khi mặt hồ đóng băng đủ dày, một tuyến đường băng được mở - "
        "người dân Leningrad gọi là «Con đường Sự sống» (Doroga Zhizni). Riêng mùa đông 1941–1942, "
        "tuyến hoạt động khoảng 152 ngày, đưa được chừng 514.000 người ra khỏi thành phố và chở vào "
        "khoảng 360.000 tấn hàng - chủ yếu là lương thực, cùng nhiên liệu và đạn dược. Con đường vô "
        "cùng nguy hiểm: những ngày đầu băng còn mỏng, hàng chục xe tải đã lọt xuống hồ. Để tưởng nhớ "
        "tuyến đường huyền thoại ấy, ngày 29 tháng 10 năm 1966, đài tưởng niệm «Vòng tròn Bị phá vỡ» "
        "được khánh thành tại km số 40 của Con đường Sự sống, ngay sát bờ hồ Ladoga gần làng "
        "Kokkorevo. Tác giả ý tưởng là nhà điêu khắc Konstantin Simun, cùng kiến trúc sư V. G. "
        "Filippov và kỹ sư I. A. Rybin. Công trình gồm hai bán vòm bê tông cốt thép cao 7 m, nặng 32 "
        "tấn, dựng cách nhau một quãng: hai vòm là vòng vây phong toả, còn khoảng hở ở giữa tượng "
        "trưng cho con đường đã chọc thủng vòng vây để cứu thành phố. Trên nền bê tông dưới chân vòm "
        "in hằn vệt bánh xe tải; bên cạnh có hai quả cầu trắng mô phỏng bệ đèn pha phòng không và một "
        "khẩu pháo cao xạ 85 mm nguyên bản. Đài tưởng niệm là một mắt xích của «Vành đai Vinh quang "
        "Xanh» - chuỗi công trình tưởng niệm chạy vòng quanh Saint Petersburg, đánh dấu tuyến phòng "
        "thủ và những sự kiện bi tráng của cuộc vây hãm. Ngày nay, nơi đây cũng là điểm xuất phát của "
        "giải chạy marathon mùa đông quốc tế «Con đường Sự sống» tổ chức hằng năm."
    ),
    "highlights_vi": [
        "Hai bán vòm bê tông cao 7 m, nặng 32 tấn tách rời nhau - hình tượng vòng vây phong toả bị chọc thủng, khoảng hở giữa chính là «Con đường Sự sống».",
        "Vệt bánh xe tải in trên nền bê tông, hai quả cầu trắng mô phỏng đèn pha phòng không và khẩu pháo cao xạ 85 mm nguyên bản.",
        "Vị trí bên bờ hồ Ladoga - điểm khởi đầu tuyến tiếp tế qua mặt hồ đóng băng và là một phần của «Vành đai Vinh quang Xanh» quanh Saint Petersburg.",
    ],
    "practical": {
        "hours_vi": "Đài tưởng niệm ngoài trời, mở tự do suốt ngày đêm.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Bốn mùa đều tới được; mùa đông tuyết phủ bên hồ Ladoga cho không khí trầm mặc đúng tinh thần đài tưởng niệm. Các ngày lễ tưởng niệm cuộc phong toả (cuối tháng 1) thường có nghi lễ đặt hoa.",
        "tips_vi": "Cách Saint Petersburg khoảng 45 km theo «Con đường Sự sống»; nên kết hợp tham quan Bảo tàng Con đường Sự sống ở Osinovets gần đó. Ăn mặc ấm khi ra sát bờ hồ vì gió lạnh.",
    },
    "photo": None,
    "photo_credit": None,
    "maps": maps_for("Мемориал «Разорванное кольцо»", "Broken Ring Memorial", "Ленинградская область", "Leningrad Oblast", 60.08148, 31.06767),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Разорванное кольцо", "url": "https://ru.wikipedia.org/wiki/Разорванное_кольцо"},
        {"title": "Wikipedia (EN) — Green Belt of Glory", "url": "https://en.wikipedia.org/wiki/Green_Belt_of_Glory"},
        {"title": "Thư viện Tổng thống Nga (Presidential Library) — Memorial «The Broken Ring»", "url": "https://www.prlib.ru/en/node/343340"},
    ],
    "tags": ["monument", "wwii", "memorial", "road-of-life", "siege-of-leningrad", "lake-ladoga", "vsevolozhsk"],
    "status": "enriched",
    "last_updated": TODAY,
    "country": "russia",
}


PLAN = {
    "moscow-oblast.json": [MARFINO_ESTATE, MURANOVO_ESTATE],
    "leningrad-oblast.json": [BROKEN_RING],
}


def main():
    total_added = 0
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
