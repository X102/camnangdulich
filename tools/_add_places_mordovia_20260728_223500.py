# -*- coding: utf-8 -*-
"""_add_places_mordovia_20260728_223500.py — VÙNG: Cộng hoà Mordovia (Республика Мордовия)
(lần chạy tự động 2026-07-28).

Bối cảnh: mordovia.json hiện có 7 địa điểm (saransk-ushakov-cathedral, erzia-museum-saransk,
sanaksar-monastery, makarovsky-pogost, mordovsky-nature-reserve, temnikov-historic,
pushkin-square-saransk). Bổ sung 26 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại
hình → đưa vùng lên 33. TRÁNH trùng 7 điểm trên.

Trung tâm là Saransk; mở rộng sang Rузаевка/Ruzaevka, Краснослободск/Krasnoslobodsk, Инсар/Insar,
Темников/Temnikov, làng nghề Подлесная Тавла (Podlesnaya Tavla), tu viện Пайгарм & Чуфарово,
điền trang Огарёва (Старое Акшино), nhà-bảo tàng Эрьзя (Баево), công viên thiên nhiên Симкино.

Phân bố loại hình (26 bản ghi mới):
- museum (6): Музей военного и трудового подвига 1941–1945, краеведческий музей им. Воронина,
  Музей мордовской народной культуры, Этно-кудо (Подлесная Тавла), Дом-музей Эрьзи (Баево),
  Темниковский музей им. Ушакова.
- theatre (4): Национальный драмтеатр, Театр оперы и балета им. Яушева, Русский драмтеатр,
  Театр кукол.
- church (4): Церковь Иоанна Богослова (Саранск), Троицкая церковь (Саранск), Пайгармский
  Параскево-Вознесенский монастырь, Чуфаровский Троицкий монастырь.
- monument (2): Монумент «Навеки с Россией», памятник героям-стратонавтам.
- square_street (3): площадь Тысячелетия, Фонтанный спуск, Соборная площадь.
- park_garden (1): Симкинский природный парк («Старый дуб»).
- palace/усадьба (1): Староакшинская усадьба Огарёвых.
- other (5): Мордовия Арена, Пугачёвская палатка, Краснослободск, Рузаевка, Инсар.

TOẠ ĐỘ — xác minh chéo (OpenStreetMap/Nominatim, ru.wikipedia, sobory.ru, autotravel/komandirovka,
Yandex Maps org — 2026-07-28). Phạm vi Mordovia lat ~53.5–55.2, lon ~42–46.5 — tất cả toạ độ nằm
trong phạm vi, KHÔNG đảo lat/lon. Nhiều điểm đã đối chiếu TRỰC TIẾP với OSM trong lần chạy này:
  Мордовия Арена 54.181830,45.204429 (OSM stadium); пл.Тысячелетия 54.187253,45.183938 (OSM);
  Фонтанный спуск 54.179440,45.186110 (Wikimapia, đoạn đầu dốc); «Навеки с Россией» 54.177758,
  45.188944 (OSM node); Музей воен.-труд. подвига 54.180278,45.183611 (ru.wiki); краевед. музей
  Воронина 54.177449,45.179817 (OSM); Музей морд. нар. культуры 54.180617,45.192961 (OSM ✓);
  Нац.драмтеатр 54.180671,45.191553 (OSM); Театр оперы и балета Яушева 54.185970,45.180096 (OSM);
  Русский драмтеатр 54.181084,45.175126 (OSM ✓); Театр кукол 54.191887,45.189691 (OSM ✓); ц.
  Иоанна Богослова 54.182475,45.178922 (OSM ✓, старейшее здание Саранска 1693); Троицкая ц.
  54.186210,45.191271 (OSM ✓); Пугачёвская палатка 54.173357,45.187784 (OSM здание, ул.Московская
  48); пам. стратонавтам 54.195834,45.189339 (OSM node); Соборная пл. 54.182715,45.181792 (OSM);
  Пайгармский монастырь 54.079072,44.830798 (sobory + Yandex org); Чуфаровский монастырь
  54.423406,45.518804 (sobory; рядом хутор OSM 54.418,45.511); Этно-кудо (Подл.Тавла) 54.095472,
  45.473996 (komandirovka GPS; OSM село 54.0958,45.4758); Симкинский парк 54.255109,46.173334
  (OSM село Симкино — điểm neo công viên); усадьба Огарёва (Ст.Акшино) 54.290821,44.707245 (OSM
  село ✓); Дом-музей Эрьзи (Баево) 54.830780,46.369340 (autotravel; OSM село 54.8345,46.3711);
  Темниковский музей Ушакова 54.632121,43.200942 (OSM museum ✓, ул.Коммунистическая 19);
  Краснослободск 54.430672,43.777900 (OSM ✓ — SỬA lỗi 44.45 của bản tra sơ bộ, khớp реку Мокша
  và собор cùng thị trấn 43.79); Рузаевка 54.058735,44.954391 (OSM ✓); Инсар 53.867741,44.371407
  (OSM ✓).

GHI CHÚ (điểm đã cân nhắc và BỎ / KHÔNG bịa toạ độ):
- «Симкинский дуб» (cây sồi cổ ~600 năm): KHÔNG có bài ru.wikipedia (đã kiểm tra: "В Википедии нет
  статьи"); toạ độ 54.184,46.177 chỉ có ở znanierussia và lệch ~7.8 km về nam so với làng Симкино
  → KHÔNG dùng toạ độ cây sồi; thay vào đó NEO điểm vào làng Симкино (OSM xác minh) và mô tả công
  viên + cây sồi. Toạ độ điểm là của làng, TIN CẬY.
- Ковылкино & Ардатов (thị trấn): loại hình «other/thị trấn» đã đủ đại diện (Краснослободск,
  Рузаевка, Инсар + Темников đã có); bỏ để tránh trùng loại. Vùng Ардатов vẫn được đại diện qua
  Дом-музей Эрьзи (Баево).
- Собор Троицы (Краснослободск): собор LỊCH SỬ hiện KHÔNG hoạt động (bị nhà máy dệt chiếm) → bỏ để
  tránh liệt kê hai mục cho một thị trấn nhỏ.
- Loại «fortress/kremlin» & «bridge»: Mordovia KHÔNG còn pháo đài/kremlin nguyên vẹn (ostrog Saransk
  1641 và thành Temnikov đã mất) và không có cầu nổi tiếng → hai loại này không có bản ghi hợp lệ.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_mordovia_20260728_223500.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "mordovia"
REGION_NAME_VI = "Cộng hoà Mordovia"
FD = "Vùng Volga"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def maps_org(yandex_org_url, name_en, city_en):
    """Ưu tiên URL trang tổ chức/địa điểm Yandex (chính xác nhất) + Google text-search."""
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": yandex_org_url,
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def rec(slug, name_vi, name_ru, name_en, categories, lat, lon, address_vi,
        short, long, highlights, practical, sources, tags, maps,
        official_site=None):
    return {
        "id": f"{REGION}-{slug}",
        "slug": slug,
        "region": REGION,
        "region_name_vi": REGION_NAME_VI,
        "federal_district": FD,
        "name_vi": name_vi,
        "name_ru": name_ru,
        "name_en": name_en,
        "categories": categories,
        "coordinates": {"lat": lat, "lon": lon},
        "address_vi": address_vi,
        "rating": {"value": None, "count": None, "source": None, "as_of": None},
        "review_summary_vi": "",
        "presentation_short_vi": short,
        "presentation_long_vi": long,
        "highlights_vi": highlights,
        "practical": practical,
        "photo": None,
        "photo_credit": None,
        "maps": maps,
        "official_site": official_site,
        "sources": sources,
        "tags": tags,
        "status": "enriched",
        "last_updated": TODAY,
        "country": "russia",
    }


def p(hours, ticket, duration, best, tips):
    return {"hours_vi": hours, "ticket_vi": ticket, "duration_vi": duration,
            "best_time_vi": best, "tips_vi": tips}


RECORDS = []

# ============================ ĐIỂM HIỆN ĐẠI / other ============================

# 1) Мордовия Арена -------------------------------------------------------------
RECORDS.append(rec(
    "mordovia-arena",
    "Sân vận động Mordovia Arena",
    "Стадион «Мордовия Арена»",
    "Mordovia Arena",
    ["other"],
    54.181830, 45.204429,
    "Phố Volgogradskaya 1, khu Yubileyny, thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Mordovia Arena là sân vận động hiện đại nhất nước cộng hoà, xây dựng cho World Cup 2018 với sức chứa khoảng 44.000 chỗ. Mặt tiền màu cam rực rỡ lấy cảm hứng từ hình mặt trời trong văn hoá Mordvin, biến sân thành biểu tượng đô thị mới của Saransk.",
    "Khánh thành năm 2018 cho Vòng chung kết bóng đá thế giới, Mordovia Arena là công trình thể thao tham vọng nhất từng được xây ở Cộng hoà Mordovia và cũng là điểm 'check-in' hiện đại được nhiều du khách tìm đến. Sân nằm bên bờ sông Insar, thuộc khu Yubileyny của Saransk, với thiết kế bầu dục và lớp vỏ ngoài phối các sắc cam, đỏ, vàng gợi liên tưởng đến mặt trời và hoa văn thêu truyền thống của người Mordvin. Trong kỳ World Cup, nơi đây từng đón bốn trận đấu vòng bảng cùng dòng cổ động viên quốc tế, đưa tên tuổi Saransk lên bản đồ thế giới. Sức chứa hơn 44.000 chỗ (giảm bớt sau giải để phù hợp nhu cầu địa phương), sân hiện là nơi thi đấu của câu lạc bộ bóng đá địa phương và tổ chức các sự kiện thể thao, hòa nhạc lớn. Khu vực xung quanh được quy hoạch thành công viên và không gian dạo bộ ven sông, thu hút người dân đến tập thể dục, chụp ảnh. Với kiến trúc bắt mắt và ý nghĩa lịch sử thể thao, Mordovia Arena là điểm dừng đáng ghé để cảm nhận diện mạo đương đại của thủ phủ Mordovia.",
    [
        "Sân vận động chính của Mordovia, xây cho World Cup 2018, sức chứa khoảng 44.000 chỗ.",
        "Mặt tiền màu cam - vàng lấy cảm hứng từ biểu tượng mặt trời và hoa văn thêu Mordvin.",
        "Từng tổ chức bốn trận vòng bảng World Cup và nhiều sự kiện thể thao, hòa nhạc lớn.",
    ],
    p("Khu vực bên ngoài và công viên ven sông tham quan tự do; vào sân theo lịch trận đấu hoặc sự kiện.",
      "Đi dạo quanh sân miễn phí; vé xem trận đấu/sự kiện mua theo chương trình.",
      "30–45 phút (ngắm bên ngoài); lâu hơn nếu xem sự kiện.",
      "Chiều tối mùa hè, khi có sự kiện hoặc để chụp ảnh mặt tiền lên đèn.",
      "Kết hợp dạo công viên ven sông Insar; ngày có trận đấu nên đến sớm để tránh đông."),
    [
        {"title": "Wikipedia (RU) — Мордовия Арена", "url": "https://ru.wikipedia.org/wiki/Мордовия_Арена"},
        {"title": "Wikipedia (EN) — Mordovia Arena", "url": "https://en.wikipedia.org/wiki/Mordovia_Arena"},
    ],
    ["stadium", "modern", "football", "worldcup2018", "landmark"],
    maps_org("https://yandex.ru/maps/org/mordoviya_arena/140121004362/", "Mordovia Arena", "Saransk"),
))

# 2) Пугачёвская палатка --------------------------------------------------------
RECORDS.append(rec(
    "pugachev-palate-saransk",
    "Nhà cổ Pugachev (Pugachyovskaya palatka)",
    "Пугачёвская палатка",
    "Pugachev's Palate (Pugachyovskaya palatka)",
    ["other"],
    54.173357, 45.187784,
    "Phố Moskovskaya 48 (sân sau Nhà thờ Ba Thánh), thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Nhà cổ Pugachev là công trình dân dụng bằng đá cổ nhất còn lại ở Saransk, dựng từ thế kỷ 17. Tên gọi gắn với thủ lĩnh khởi nghĩa nông dân Yemelyan Pugachev, người từng chiếm Saransk năm 1774 và tương truyền lưu lại đây.",
    "Nép trong khu phố cổ Saransk, gần Nhà thờ Ba Thánh trên phố Moskovskaya, 'Pugachyovskaya palatka' là một ngôi nhà đá nhỏ nhưng mang giá trị lịch sử đặc biệt: đây được xem là công trình dân dụng (thế tục) bằng đá lâu đời nhất còn tồn tại của thành phố, có niên đại từ cuối thế kỷ 17. Kiến trúc mộc mạc với tường dày, cửa vòm và mái đơn giản là điển hình cho nhà ở của tầng lớp thương nhân, quan chức Nga thời tiền Petrine. Sức hút của di tích nằm ở cái tên: mùa hè năm 1774, trong cuộc khởi nghĩa nông dân rung chuyển đế chế, thủ lĩnh Yemelyan Pugachev đã tiến vào và chiếm Saransk; dân gian truyền rằng ông từng dừng chân, nghỉ lại tại chính ngôi nhà này, nên nó được gọi là 'lều Pugachev'. Dù quy mô khiêm tốn và thường chỉ ngắm từ bên ngoài, di tích là một mảnh ghép quý của lịch sử đô thị, minh chứng cho lớp kiến trúc cổ hiếm hoi sống sót qua các đợt quy hoạch. Với du khách yêu lịch sử, đây là điểm dừng nhanh thú vị khi dạo bộ khám phá trung tâm cổ của Saransk.",
    [
        "Công trình dân dụng bằng đá cổ nhất còn lại ở Saransk (thế kỷ 17).",
        "Gắn với thủ lĩnh khởi nghĩa nông dân Yemelyan Pugachev, người chiếm Saransk năm 1774.",
        "Mảnh ghép hiếm hoi của lớp kiến trúc tiền Petrine giữa lòng phố cổ.",
    ],
    p("Là di tích ngoài trời, ngắm tự do; nội thất thường không mở tham quan thường xuyên.",
      "Miễn phí (ngắm bên ngoài).",
      "15–20 phút.",
      "Kết hợp khi đi dạo trung tâm cổ Saransk, ban ngày ánh sáng đẹp.",
      "Nằm trong sân Nhà thờ Ba Thánh; đi bộ dễ kết hợp với các điểm ở phố Moskovskaya."),
    [
        {"title": "Wikipedia (RU) — Саранск (история)", "url": "https://ru.wikipedia.org/wiki/Саранск"},
        {"title": "Yandex Maps — Пугачёвская палатка", "url": "https://yandex.ru/maps/org/pugachyovskaya_palatka/119475148720/"},
    ],
    ["history", "heritage", "pugachev", "oldtown", "monument"],
    maps_org("https://yandex.ru/maps/org/pugachyovskaya_palatka/119475148720/", "Pugachev Palate", "Saransk"),
))

# ============================ BẢO TÀNG (museum) ============================

# 3) Музей военного и трудового подвига 1941–1945 -------------------------------
RECORDS.append(rec(
    "military-labor-museum-saransk",
    "Bảo tàng Chiến công Quân sự và Lao động 1941–1945",
    "Мемориальный музей военного и трудового подвига 1941–1945 годов",
    "Memorial Museum of Military and Labour Feat of 1941–1945",
    ["museum"],
    54.180278, 45.183611,
    "Phố Sovetskaya 34a (Quảng trường Chiến thắng), thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Bảo tàng tưởng niệm mở năm 1995 nhân 50 năm Chiến thắng, kể câu chuyện đóng góp của Mordovia trong Thế chiến II. Toà nhà mái vòm mạ vàng có đường viền mô phỏng ranh giới nước cộng hoà, là trung tâm của quần thể Quảng trường Chiến thắng.",
    "Nằm trong quần thể Quảng trường Chiến thắng ở trung tâm Saransk, Bảo tàng Chiến công Quân sự và Lao động 1941–1945 là điểm tưởng niệm quan trọng nhất của Mordovia về Cuộc Chiến tranh Vệ quốc Vĩ đại. Bảo tàng khánh thành ngày 6/5/1995 đúng dịp kỷ niệm 50 năm Chiến thắng, với kiến trúc giàu tính biểu tượng: mặt bằng công trình phỏng theo đường ranh giới của nước cộng hoà, phần mái tạo dáng như chiếc mũ 'kokoshnik' Nga và điểm bằng một vòm nhỏ mạ vàng nổi bật. Bên trong trưng bày vũ khí, quân trang, thư từ, ảnh tư liệu và hiện vật cá nhân của những người con Mordovia ra trận cũng như hậu phương lao động, khắc hoạ cả 'chiến công quân sự' lẫn 'chiến công lao động' như tên gọi. Xung quanh bảo tàng là ngọn lửa vĩnh cửu, các đài tưởng niệm và khu trưng bày khí tài quân sự ngoài trời (xe tăng, pháo, máy bay) mà du khách có thể lại gần. Đây vừa là nơi giáo dục lịch sử cho thế hệ trẻ, vừa là địa điểm tổ chức các nghi lễ trọng thể ngày 9/5. Với kiến trúc đặc sắc và không gian tưởng niệm trang nghiêm, bảo tàng là điểm đến ý nghĩa để hiểu ký ức chiến tranh của vùng đất này.",
    [
        "Toà nhà mái vòm mạ vàng có đường viền phỏng theo ranh giới Cộng hoà Mordovia.",
        "Mở năm 1995 nhân 50 năm Chiến thắng, trung tâm quần thể Quảng trường Chiến thắng.",
        "Khu trưng bày khí tài quân sự ngoài trời và ngọn lửa vĩnh cửu ngay bên cạnh.",
    ],
    p("Thường mở cửa cả tuần trừ một ngày đầu tuần, khoảng 10:00–18:00 (nên kiểm tra trước).",
      "Vé vào ở mức khiêm tốn; khu ngoài trời tham quan tự do.",
      "1–1,5 giờ.",
      "Quanh năm; đặc biệt sôi động dịp Ngày Chiến thắng 9/5.",
      "Kết hợp đi bộ trên phố Sovetskaya tới Quảng trường Sobornaya và Nhà thờ Ushakov gần đó."),
    [
        {"title": "Wikipedia (RU) — Мемориальный музей военного и трудового подвига 1941—1945 гг.", "url": "https://ru.wikipedia.org/wiki/Мемориальный_музей_военного_и_трудового_подвига_1941—1945_гг."},
        {"title": "Wikipedia (RU) — Саранск", "url": "https://ru.wikipedia.org/wiki/Саранск"},
    ],
    ["museum", "history", "wwii", "memorial", "indoor"],
    maps_text("Мемориальный музей военного и трудового подвига 1941–1945", "Саранск",
              "Memorial Museum of Military and Labour Feat", "Saransk", 54.180278, 45.183611),
))

# 4) Краеведческий музей им. И. Д. Воронина -------------------------------------
RECORDS.append(rec(
    "voronin-local-lore-museum-saransk",
    "Bảo tàng Địa phương học Mordovia mang tên I.D. Voronin",
    "Мордовский республиканский объединённый краеведческий музей имени И. Д. Воронина",
    "Voronin Mordovian Republican Museum of Local Lore",
    ["museum"],
    54.177449, 45.179817,
    "Phố Saranskaya 2 (khu phức hợp Bảo tàng - Lưu trữ bên sông Saranka), thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Thành lập năm 1918, đây là bảo tàng địa phương học lâu đời và lớn nhất Mordovia với hơn 120.000 hiện vật. Từ năm 2017 bảo tàng chuyển về khu phức hợp Bảo tàng - Lưu trữ hiện đại bên sông Saranka.",
    "Bảo tàng Địa phương học Cộng hoà Mordovia mang tên nhà sử học I.D. Voronin là kho lưu trữ ký ức toàn diện nhất về thiên nhiên, lịch sử và con người của vùng đất này. Được thành lập từ ngày 29/11/1918, đây là một trong những bảo tàng lâu đời nhất khu vực, và từ năm 2005 mang tên Ivan Dmitrievich Voronin để tri ân người có công gây dựng. Bộ sưu tập đồ sộ với hơn 120.000 hiện vật trải rộng từ khảo cổ, khoáng vật, động thực vật bản địa đến trang phục, đồ thủ công, vũ khí và tư liệu về hai dân tộc Moksha và Erzya cùng lịch sử hình thành nước cộng hoà. Từ năm 2017, bảo tàng chuyển về toà nhà trung tâm của một khu phức hợp Bảo tàng - Lưu trữ mới xây bên bờ sông Saranka, với không gian trưng bày rộng rãi, hiện đại và nhiều chi nhánh chuyên đề. Các gian trưng bày được dàn dựng sinh động, kết hợp hiện vật gốc với mô hình, âm thanh và màn hình tương tác, phù hợp cho cả gia đình lẫn khách nghiên cứu. Đây là điểm khởi đầu lý tưởng để nắm bắt bức tranh tổng thể về Mordovia trước khi khám phá các địa danh khác.",
    [
        "Bảo tàng địa phương học lâu đời nhất Mordovia (thành lập 1918), hơn 120.000 hiện vật.",
        "Trưng bày toàn diện về thiên nhiên, khảo cổ và hai dân tộc Moksha - Erzya.",
        "Đặt trong khu phức hợp Bảo tàng - Lưu trữ hiện đại bên sông Saranka (từ 2017).",
    ],
    p("Thường mở cửa cả tuần trừ một ngày đầu tuần, khoảng 10:00–18:00 (kiểm tra lịch trước).",
      "Vé vào ở mức khiêm tốn; ưu đãi cho học sinh, sinh viên, người cao tuổi.",
      "1,5–2 giờ.",
      "Quanh năm, rất hợp ngày mưa hoặc mùa đông.",
      "Là điểm khởi đầu để hiểu tổng quan Mordovia; hỏi trước về các chi nhánh chuyên đề."),
    [
        {"title": "Wikipedia (RU) — Мордовский республиканский объединённый краеведческий музей имени И. Д. Воронина", "url": "https://ru.wikipedia.org/wiki/Мордовский_республиканский_объединённый_краеведческий_музей_имени_И._Д._Воронина"},
        {"title": "Официальный сайт — Мордовский краеведческий музей", "url": "https://mrom.ru/"},
    ],
    ["museum", "local-lore", "history", "ethnography", "indoor"],
    maps_text("Мордовский республиканский краеведческий музей имени И. Д. Воронина", "Саранск",
              "Voronin Museum of Local Lore", "Saransk", 54.177449, 45.179817),
    official_site="https://mrom.ru/",
))

# 5) Музей мордовской народной культуры -----------------------------------------
RECORDS.append(rec(
    "mordovian-national-culture-museum-saransk",
    "Bảo tàng Văn hoá Dân gian Mordovia",
    "Музей мордовской народной культуры",
    "Museum of Mordovian National Culture",
    ["museum"],
    54.180617, 45.192961,
    "Phố Sovetskaya 19, thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Bảo tàng chuyên đề mở năm 1999 trong một dinh thự thương nhân đầu thế kỷ 20, dành riêng cho văn hoá dân gian của người Moksha và Erzya. Khoảng 4.000 hiện vật gồm trang phục, biểu tượng tôn giáo, gốm và đồ gia dụng truyền thống.",
    "Toạ lạc trong một ngôi nhà gạch duyên dáng của thương nhân đầu thế kỷ 20 trên phố Sovetskaya, Bảo tàng Văn hoá Dân gian Mordovia là nơi lý tưởng để đắm mình vào bản sắc của hai tộc người Mordvin: Moksha và Erzya. Khai trương ngày 6/10/1999, bảo tàng tập trung khoảng 4.000 hiện vật phản ánh đời sống vật chất và tinh thần truyền thống: những bộ trang phục dân tộc thêu tay rực rỡ với trang sức bằng đồng và vỏ ốc, các biểu tượng tín ngưỡng, tranh thánh, đồ gốm, dụng cụ dệt, nông cụ và vật dụng sinh hoạt trong ngôi nhà gỗ Mordvin. Ngay tấm biển tên bảo tàng cũng được viết bằng ba thứ tiếng - Nga, Moksha và Erzya - nhấn mạnh tinh thần gìn giữ ngôn ngữ và di sản. Không gian trưng bày ấm cúng, tái hiện các góc sinh hoạt, lễ hội và nghi thức vòng đời, giúp du khách hình dung rõ nét nếp sống của cư dân bản địa vùng Volga. Đây là điểm bổ trợ tuyệt vời cho Bảo tàng Mỹ thuật Erzia gần đó, cùng nhau vẽ nên chân dung văn hoá trọn vẹn của Mordovia.",
    [
        "Chuyên sâu về văn hoá dân gian hai tộc người Moksha và Erzya.",
        "Khoảng 4.000 hiện vật: trang phục thêu tay, gốm, đồ gia dụng, biểu tượng tín ngưỡng.",
        "Đặt trong dinh thự thương nhân đầu thế kỷ 20; biển tên viết bằng ba thứ tiếng.",
    ],
    p("Thường mở cửa cả tuần trừ một ngày đầu tuần, khoảng 10:00–18:00 (kiểm tra trước).",
      "Vé vào ở mức khiêm tốn.",
      "1–1,5 giờ.",
      "Quanh năm; là điểm trong nhà lý tưởng cho ngày lạnh.",
      "Kết hợp với Bảo tàng Mỹ thuật Erzia gần đó để hiểu trọn vẹn văn hoá Mordovia."),
    [
        {"title": "Wikipedia (RU) — Музей мордовской народной культуры", "url": "https://ru.wikipedia.org/wiki/Музей_мордовской_народной_культуры"},
        {"title": "Culture.ru — Музей мордовской народной культуры", "url": "https://www.culture.ru/"},
    ],
    ["museum", "ethnography", "moksha", "erzya", "culture"],
    maps_text("Музей мордовской народной культуры", "Саранск",
              "Museum of Mordovian National Culture", "Saransk", 54.180617, 45.192961),
))

# 6) Этно-кудо (Подлесная Тавла) ------------------------------------------------
RECORDS.append(rec(
    "etno-kudo-podlesnaya-tavla",
    "Nhà-bảo tàng 'Etno-Kudo' làng Podlesnaya Tavla",
    "Дом-музей мордовской народной культуры «Этно-кудо» имени В. И. Ромашкина",
    "Etno-Kudo House-Museum of Mordovian Folk Culture (Podlesnaya Tavla)",
    ["museum"],
    54.095472, 45.473996,
    "Làng Podlesnaya Tavla, huyện Kochkurovsky, Cộng hoà Mordovia, Nga (cách Saransk ~35 km về đông nam)",
    "'Etno-Kudo' (nghĩa là 'ngôi nhà dân tộc' trong tiếng Erzya) là nhà-bảo tàng văn hoá dân gian ở làng Podlesnaya Tavla nổi tiếng nghề chạm khắc gỗ. Mở năm 2006, mang tên nhạc sĩ dân gian V.I. Romashkin, người sáng lập ban nhạc 'Torama'.",
    "Nằm ở làng Podlesnaya Tavla thuộc huyện Kochkurovsky, cách Saransk chừng 35 km, nhà-bảo tàng 'Etno-Kudo' là nơi lưu giữ hồn cốt nghề thủ công và âm nhạc dân gian Erzya. Cái tên 'Etno-Kudo' trong tiếng Erzya có nghĩa là 'ngôi nhà dân tộc'; bảo tàng khai trương ngày 6/9/2006 và mang tên Vladimir Romashkin - nhạc sĩ, nhà nghiên cứu văn hoá dân gian và người sáng lập ban nhạc nam nổi tiếng 'Torama'. Podlesnaya Tavla từ lâu được biết đến là trung tâm nghề chạm khắc gỗ của Mordovia, nơi những nghệ nhân biến khúc gỗ thành tượng ngựa, chim, nhân vật thần thoại và đồ dùng trang trí đậm phong cách Mordvin. Trong không gian ngôi nhà gỗ truyền thống, du khách được ngắm bộ sưu tập tác phẩm điêu khắc, nhạc cụ dân tộc, trang phục và vật dụng, thậm chí có thể xem nghệ nhân trình diễn hoặc tham gia lớp học chạm khắc, làm đồ lưu niệm. Bảo tàng là một phần của Trung tâm Văn hoá Dân tộc Mordovia, thường tổ chức các buổi giao lưu âm nhạc, lễ hội và trải nghiệm thủ công. Đây là điểm đến sống động, mang tính tương tác cao cho ai muốn tiếp xúc trực tiếp với di sản dân gian còn 'sống' của người Erzya.",
    [
        "Nằm ở làng Podlesnaya Tavla - trung tâm nghề chạm khắc gỗ truyền thống của Mordovia.",
        "Mở năm 2006, mang tên nhạc sĩ dân gian V.I. Romashkin, người sáng lập ban nhạc 'Torama'.",
        "Có trình diễn, lớp học chạm khắc và giao lưu âm nhạc dân tộc cho du khách trải nghiệm.",
    ],
    p("Đón khách theo lịch, tốt nhất nên liên hệ/đặt trước, nhất là với đoàn.",
      "Có thu phí tham quan và phí trải nghiệm thủ công (mức khiêm tốn).",
      "1–2 giờ (chưa kể di chuyển).",
      "Mùa ấm (tháng 5–9) thuận tiện đi lại; các dịp lễ hội dân gian rất sôi động.",
      "Cách Saransk ~35 km, nên đi ô tô/tour; đặt trước để có nghệ nhân trình diễn và mua đồ chạm khắc làm quà."),
    [
        {"title": "Culture.ru — «Этно-кудо» им. В. И. Ромашкина", "url": "https://www.culture.ru/"},
        {"title": "Wikipedia (RU) — Подлесная Тавла", "url": "https://ru.wikipedia.org/wiki/Подлесная_Тавла"},
    ],
    ["museum", "crafts", "woodcarving", "erzya", "folk"],
    maps_text("Этно-кудо Подлесная Тавла", "Мордовия",
              "Etno-Kudo House-Museum", "Podlesnaya Tavla", 54.095472, 45.473996),
))

# 7) Дом-музей С. Д. Эрьзи (Баево) ----------------------------------------------
RECORDS.append(rec(
    "erzia-house-museum-baevo",
    "Nhà-bảo tàng S.D. Erzia tại làng Baevo",
    "Дом-музей С. Д. Эрьзи в селе Баево",
    "S.D. Erzia House-Museum in Baevo",
    ["museum"],
    54.830780, 46.369340,
    "Làng Baevo, huyện Ardatovsky, Cộng hoà Mordovia, Nga (quê hương nhà điêu khắc Stepan Erzia)",
    "Nhà-bảo tàng nằm tại làng Baevo, quê hương của nhà điêu khắc lừng danh Stepan Erzia (Nefyodov). Mở năm 1976 nhân 100 năm ngày sinh của ông, tái hiện ngôi nhà gỗ Mordvin điển hình và tôn vinh sự nghiệp nghệ thuật của người con nổi tiếng nhất vùng.",
    "Ở làng Baevo xa xôi thuộc huyện Ardatovsky, phía đông bắc Mordovia, có một nhà-bảo tàng giản dị nhưng đầy tự hào dành cho Stepan Dmitrievich Erzia (tên thật Nefyodov, 1876–1959) - nhà điêu khắc gốc Mordvin được mệnh danh là 'Rodin của nước Nga'. Chính tại ngôi làng này, cậu bé Stepan chào đời trong một gia đình nông dân Erzya, và sau này lấy chính tên tộc người mình làm nghệ danh 'Erzia' như một tuyên ngôn về cội nguồn. Nhà-bảo tàng được khánh thành năm 1976 nhân kỷ niệm 100 năm ngày sinh của ông, dựng theo kiểu ngôi nhà gỗ (izba) một tầng đặc trưng của người Mordvin, gần vị trí gia đình Nefyodov từng sinh sống. Bên trong trưng bày các bản sao tác phẩm, tư liệu, ảnh và hiện vật về cuộc đời phiêu bạt của nghệ sĩ - từ nước Nga qua Ý, Pháp đến Argentina, nơi ông tạc nên những pho tượng gỗ cứng bất hủ. Cụm di tích còn có đài tưởng niệm, tượng Erzia và nhà thờ Pokrov gần đó. Là chi nhánh của Bảo tàng Mỹ thuật Erzia ở Saransk, nơi đây bổ sung chiều sâu về gốc gác cho hành trình tìm hiểu người nghệ sĩ, đặc biệt ý nghĩa với ai đã ghé bảo tàng chính ở thủ phủ.",
    [
        "Nằm tại Baevo - làng quê nơi sinh ra nhà điêu khắc Stepan Erzia (Nefyodov).",
        "Mở năm 1976 nhân 100 năm ngày sinh, tái hiện ngôi nhà gỗ Mordvin truyền thống.",
        "Chi nhánh của Bảo tàng Mỹ thuật Erzia ở Saransk, cùng đài tưởng niệm và tượng nghệ sĩ.",
    ],
    p("Mở cửa theo lịch bảo tàng địa phương; nên liên hệ trước vì ở vùng xa.",
      "Vé vào ở mức khiêm tốn.",
      "1–1,5 giờ (chưa kể di chuyển).",
      "Mùa ấm (tháng 5–9) để đường sá thuận tiện.",
      "Ở khá xa Saransk (đông bắc, gần Ardatov); nên đi ô tô/tour; hợp với ai muốn tìm hiểu sâu về Erzia."),
    [
        {"title": "Wikipedia (RU) — Эрьзя, Степан Дмитриевич", "url": "https://ru.wikipedia.org/wiki/Эрьзя,_Степан_Дмитриевич"},
        {"title": "Wikipedia (RU) — Баево (Мордовия)", "url": "https://ru.wikipedia.org/wiki/Баево_(Мордовия)"},
    ],
    ["museum", "erzia", "sculpture", "birthplace", "culture"],
    maps_text("Дом-музей Эрьзи Баево", "Мордовия",
              "S.D. Erzia House-Museum", "Baevo", 54.830780, 46.369340),
))

# 8) Темниковский музей им. Ф. Ф. Ушакова ---------------------------------------
RECORDS.append(rec(
    "temnikov-ushakov-museum",
    "Bảo tàng Lịch sử - Địa phương học Temnikov mang tên F.F. Ushakov",
    "Темниковский историко-краеведческий музей имени Ф. Ф. Ушакова",
    "Temnikov Museum of History and Local Lore named after F.F. Ushakov",
    ["museum"],
    54.632121, 43.200942,
    "Phố Kommunisticheskaya 19, thị trấn Temnikov, Cộng hoà Mordovia, Nga",
    "Đây là bảo tàng lâu đời nhất Mordovia, có nguồn gốc từ năm 1901, đặt trong toà nhà bệnh viện đầu thế kỷ 19 do đô đốc Ushakov tài trợ. Hơn 1.000 hiện vật liên quan đến vị đô đốc bất bại, gồm cả bức tượng bán thân phục dựng từ hộp sọ.",
    "Ở thị trấn cổ Temnikov bên sông Moksha, Bảo tàng Lịch sử - Địa phương học mang tên đô đốc Fyodor Ushakov giữ danh hiệu bảo tàng lâu đời nhất Cộng hoà Mordovia, với cội nguồn từ năm 1901 và được tái lập năm 1966. Điều đặc biệt là bảo tàng đặt trong toà nhà từng là bệnh viện xây đầu thế kỷ 19 nhờ tiền tài trợ của chính đô đốc Ushakov - người đã chọn vùng đất này làm nơi an nghỉ. Bộ sưu tập hơn một nghìn hiện vật xoay quanh cuộc đời và sự nghiệp của vị chỉ huy hải quân bất bại: mô hình tàu chiến, bản đồ hải trận, tư liệu và kỷ vật, cùng điểm nhấn là bức tượng bán thân của Ushakov được nhà nhân chủng học M. Gerasimov phục dựng dựa trên hộp sọ - giúp hình dung diện mạo thật của ông. Ngoài chủ đề Ushakov, bảo tàng còn giới thiệu lịch sử, thiên nhiên, nghề thủ công và đời sống của vùng Temnikov qua nhiều thế kỷ. Trong hành trình về miền tây bắc Mordovia - nơi có Tu viện Sanaksar và Khu bảo tồn thiên nhiên - ghé bảo tàng này là cách tuyệt vời để kết nối câu chuyện lịch sử của cả vùng đất.",
    [
        "Bảo tàng lâu đời nhất Mordovia (nguồn gốc từ 1901).",
        "Đặt trong toà nhà bệnh viện đầu thế kỷ 19 do đô đốc Ushakov tài trợ.",
        "Tượng bán thân Ushakov phục dựng từ hộp sọ bởi nhà nhân chủng học Gerasimov.",
    ],
    p("Mở cửa theo giờ hành chính, thường nghỉ một ngày đầu tuần (kiểm tra trước).",
      "Vé vào ở mức khiêm tốn.",
      "1–1,5 giờ.",
      "Mùa hè, kết hợp hành trình tây bắc Mordovia.",
      "Dễ kết hợp với Tu viện Sanaksar và Khu bảo tồn thiên nhiên Mordovia gần Temnikov."),
    [
        {"title": "Wikipedia (RU) — Темников", "url": "https://ru.wikipedia.org/wiki/Темников"},
        {"title": "Culture.ru — Темниковский музей им. Ф. Ф. Ушакова", "url": "https://www.culture.ru/"},
    ],
    ["museum", "history", "ushakov", "temnikov", "local-lore"],
    maps_text("Темниковский музей имени Ф. Ф. Ушакова", "Темников",
              "Temnikov Ushakov Museum", "Temnikov", 54.632121, 43.200942),
))

# ============================ NHÀ HÁT (theatre) ============================

# 9) Национальный драматический театр -------------------------------------------
RECORDS.append(rec(
    "mordovian-national-drama-theatre-saransk",
    "Nhà hát Kịch Dân tộc Mordovia",
    "Мордовский государственный национальный драматический театр",
    "Mordovian State National Drama Theatre",
    ["theatre"],
    54.180671, 45.191553,
    "Phố Sovetskaya 27, thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Nhà hát dân tộc độc đáo của Mordovia, có lịch sử từ năm 1932 và là sân khấu duy nhất trong vùng dàn dựng vở diễn bằng cả ba ngôn ngữ: Moksha, Erzya và Nga.",
    "Nằm trên phố Sovetskaya sầm uất ở trung tâm Saransk, Nhà hát Kịch Dân tộc Mordovia là niềm tự hào văn hoá của nước cộng hoà và là một hiện tượng sân khấu hiếm có ở Nga. Lịch sử đoàn kịch bắt đầu từ năm 1932, với vở diễn đầu tiên - bản dựng 'Giông tố' của Ostrovsky bằng tiếng Erzya - ra mắt năm 1934. Điểm làm nên bản sắc riêng của nhà hát là việc dàn dựng các vở diễn bằng cả ba ngôn ngữ: Moksha, Erzya và Nga, qua đó gìn giữ và tôn vinh tiếng nói của hai dân tộc Mordvin bên cạnh tiếng Nga. Kịch mục phong phú, từ kịch cổ điển Nga và thế giới đến các tác phẩm dựa trên văn học, sử thi và truyền thuyết dân gian Mordvin, giúp khán giả tiếp cận di sản văn hoá bản địa qua ngôn ngữ nghệ thuật sống động. Toà nhà nhà hát khang trang là điểm hẹn quen thuộc của người dân Saransk mỗi tối cuối tuần. Với du khách, dù rào cản ngôn ngữ, một buổi diễn ở đây - đặc biệt là vở mang màu sắc dân tộc - vẫn là trải nghiệm đáng nhớ để cảm nhận tâm hồn Mordovia.",
    [
        "Nhà hát dân tộc có lịch sử từ 1932, vở đầu tiên (1934) diễn bằng tiếng Erzya.",
        "Sân khấu duy nhất trong vùng dàn dựng vở bằng cả ba ngôn ngữ: Moksha, Erzya và Nga.",
        "Kịch mục khai thác sử thi và truyền thuyết dân gian Mordvin.",
    ],
    p("Buổi diễn thường vào buổi tối; phòng vé mở theo giờ, xem lịch trên trang chính thức.",
      "Vé theo suất diễn, giá hợp lý.",
      "2–2,5 giờ mỗi suất.",
      "Mùa diễn thu - đông - xuân; cuối tuần đông khán giả.",
      "Đặt vé trước cho vở nổi bật; nằm ngay trung tâm, dễ kết hợp dạo phố Sovetskaya."),
    [
        {"title": "Wikipedia (RU) — Мордовский национальный драматический театр", "url": "https://ru.wikipedia.org/wiki/Мордовский_национальный_драматический_театр"},
        {"title": "Culture.ru — Мордовский национальный драматический театр", "url": "https://www.culture.ru/"},
    ],
    ["theatre", "culture", "moksha", "erzya", "performing-arts"],
    maps_org("https://yandex.ru/maps/org/mordovskiy_gosudarstvenny_natsionalny_dramaticheskiy_teatr/1072996893/",
             "Mordovian National Drama Theatre", "Saransk"),
))

# 10) Театр оперы и балета им. И. М. Яушева --------------------------------------
RECORDS.append(rec(
    "yaushev-opera-ballet-theatre-saransk",
    "Nhà hát Opera và Ballet mang tên I.M. Yaushev",
    "Государственный музыкальный театр имени И. М. Яушева (театр оперы и балета)",
    "State Opera and Ballet Theatre named after I.M. Yaushev",
    ["theatre"],
    54.185970, 45.180096,
    "Phố Bogdana Khmelnitskogo 36, thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Nhà hát nhạc kịch chính của Mordovia, chuyển về toà nhà mới 714 chỗ năm 2011 và được nâng cấp thành Nhà hát Opera và Ballet năm 2024. Mang tên ca sĩ Illarion Yaushev, kịch mục gồm opera, ballet, operetta và chương trình cho thiếu nhi.",
    "Là trung tâm nghệ thuật hàn lâm của Cộng hoà Mordovia, Nhà hát mang tên ca sĩ opera Illarion Yaushev mở ra cánh cửa vào thế giới opera, ballet và operetta cho khán giả Saransk. Sau nhiều năm hoạt động trong toà nhà cũ, năm 2011 nhà hát chuyển về công trình mới hiện đại với khán phòng khoảng 714 chỗ, trang bị sân khấu và âm thanh đạt chuẩn, cho phép dàn dựng những vở diễn quy mô lớn. Đến tháng 2/2024, nhà hát chính thức được nâng cấp và đổi tên thành Nhà hát Opera và Ballet, khẳng định vị thế trong đời sống văn hoá vùng Volga. Kịch mục đa dạng trải từ các vở opera và ballet kinh điển thế giới, operetta vui nhộn đến những tác phẩm dựa trên đề tài và âm nhạc dân tộc Mordvin, cùng nhiều chương trình dành cho thiếu nhi. Không gian nội thất sang trọng, dàn nhạc và nghệ sĩ được đào tạo bài bản mang đến những đêm diễn chất lượng. Với du khách, một buổi tối thưởng thức opera hay ballet tại đây là cách tinh tế để cảm nhận nhịp sống văn hoá đương đại của thủ phủ Mordovia.",
    [
        "Nhà hát nhạc kịch chính của Mordovia, chuyển về toà nhà mới 714 chỗ năm 2011.",
        "Được nâng cấp thành Nhà hát Opera và Ballet năm 2024.",
        "Kịch mục gồm opera, ballet, operetta và các chương trình cho thiếu nhi.",
    ],
    p("Buổi diễn thường vào buổi tối; phòng vé theo giờ, xem lịch trên trang chính thức.",
      "Vé theo suất, nhiều mức giá.",
      "2–3 giờ mỗi suất.",
      "Mùa diễn thu - đông - xuân.",
      "Đặt vé trước cho các vở lớn; trang phục lịch sự sẽ hợp không khí nhà hát."),
    [
        {"title": "Wikipedia (RU) — Музыкальный театр имени И. М. Яушева", "url": "https://ru.wikipedia.org/wiki/Государственный_музыкальный_театр_имени_И._М._Яушева"},
        {"title": "Culture.ru — Театр оперы и балета им. И. М. Яушева", "url": "https://www.culture.ru/"},
    ],
    ["theatre", "opera", "ballet", "music", "performing-arts"],
    maps_text("Государственный музыкальный театр имени И. М. Яушева", "Саранск",
              "Yaushev Opera and Ballet Theatre", "Saransk", 54.185970, 45.180096),
))

# 11) Русский драматический театр -----------------------------------------------
RECORDS.append(rec(
    "russian-drama-theatre-saransk",
    "Nhà hát Kịch Nga Cộng hoà Mordovia",
    "Государственный русский драматический театр Республики Мордовия",
    "State Russian Drama Theatre of the Republic of Mordovia",
    ["theatre"],
    54.181084, 45.175126,
    "Phố Sovetskaya 60, thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Nhà hát kịch nói tiếng Nga lâu đời của Mordovia, thành lập năm 1932, hoạt động trong toà nhà năm 1961 được xếp hạng di sản. Từ năm 2005 là nơi tổ chức liên hoan sân khấu quốc tế 'Đồng bào' (Sootechestvenniki).",
    "Được thành lập ngày 25/8/1932, Nhà hát Kịch Nga Cộng hoà Mordovia là một trong những đoàn nghệ thuật lâu đời và giàu truyền thống nhất Saransk, chuyên dàn dựng kịch nói bằng tiếng Nga. Toà nhà hiện nay được xây năm 1961 trên phố Sovetskaya, mang phong cách kiến trúc đặc trưng của thời kỳ đó và được công nhận là di sản văn hoá cấp cộng hoà. Trong gần một thế kỷ, nhà hát đã dàn dựng hàng trăm vở diễn từ kịch kinh điển Nga và thế giới đến tác phẩm đương đại, trở thành điểm hẹn văn hoá quen thuộc của người dân thành phố. Một dấu ấn nổi bật là từ năm 2005, nhà hát trở thành nơi đăng cai Liên hoan sân khấu quốc tế các nhà hát kịch Nga mang tên 'Đồng bào' (Sootechestvenniki), quy tụ nhiều đoàn kịch nói tiếng Nga trong và ngoài nước, đưa Saransk thành điểm gặp gỡ của nghệ thuật sân khấu tiếng Nga. Với dàn diễn viên chuyên nghiệp và kịch mục đa dạng, đây là lựa chọn dễ tiếp cận cho du khách nói tiếng Nga muốn thưởng thức một đêm kịch chất lượng ngay trung tâm thủ phủ.",
    [
        "Nhà hát kịch nói tiếng Nga thành lập năm 1932, một trong những đoàn lâu đời nhất Saransk.",
        "Toà nhà năm 1961 được xếp hạng di sản văn hoá cấp cộng hoà.",
        "Đăng cai Liên hoan sân khấu quốc tế 'Đồng bào' từ năm 2005.",
    ],
    p("Buổi diễn thường vào buổi tối; phòng vé theo giờ, xem lịch trên trang chính thức.",
      "Vé theo suất, giá hợp lý.",
      "2–2,5 giờ mỗi suất.",
      "Mùa diễn thu - đông - xuân.",
      "Đặt vé trước; nằm trên trục phố Sovetskaya, dễ kết hợp tham quan trung tâm."),
    [
        {"title": "Wikipedia (RU) — Русский драматический театр Республики Мордовия", "url": "https://ru.wikipedia.org/wiki/Русский_драматический_театр_Республики_Мордовия"},
        {"title": "Culture.ru — Русский драматический театр", "url": "https://www.culture.ru/"},
    ],
    ["theatre", "drama", "russian", "culture", "performing-arts"],
    maps_text("Государственный русский драматический театр Республики Мордовия", "Саранск",
              "Russian Drama Theatre of Mordovia", "Saransk", 54.181084, 45.175126),
))

# 12) Театр кукол ---------------------------------------------------------------
RECORDS.append(rec(
    "mordovia-puppet-theatre-saransk",
    "Nhà hát Múa rối Cộng hoà Mordovia",
    "Государственный театр кукол Республики Мордовия",
    "State Puppet Theatre of the Republic of Mordovia",
    ["theatre"],
    54.191887, 45.189691,
    "Phố Volodarskogo 90A, thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Nhà hát múa rối thành lập năm 1938, dành cho khán giả nhỏ tuổi với kịch mục dựa trên cổ tích kinh điển và văn hoá dân gian Mordvin. Có trụ sở cố định từ năm 1979.",
    "Nhà hát Múa rối Cộng hoà Mordovia là điểm đến được các gia đình có trẻ nhỏ yêu thích ở Saransk. Thành lập năm 1938, trong suốt 42 năm đầu đoàn không có nhà hát riêng mà phải lưu diễn khắp nơi, cho đến năm 1979 mới được giao toà nhà cũ của cung văn hoá ngành đường sắt trên phố Volodarskogo làm trụ sở cố định. Từ đó, nơi đây trở thành 'ngôi nhà cổ tích' của thiếu nhi Mordovia, với những buổi diễn rối sinh động, đầy màu sắc và âm nhạc. Kịch mục khai thác kho tàng truyện cổ tích kinh điển của Nga và thế giới, đồng thời dàn dựng nhiều vở dựa trên truyền thuyết, cổ tích dân gian Mordvin, giúp trẻ em tiếp xúc sớm với di sản văn hoá bản địa. Các nghệ sĩ điều khiển rối điêu luyện kết hợp trang trí sân khấu bắt mắt, tạo nên những màn trình diễn vừa vui nhộn vừa giàu tính giáo dục. Đây là lựa chọn lý tưởng cho du khách đi cùng con nhỏ, hoặc đơn giản là ai muốn tìm một trải nghiệm nhẹ nhàng, ấm áp giữa chuyến khám phá thành phố.",
    [
        "Nhà hát múa rối thành lập năm 1938, có trụ sở cố định từ 1979.",
        "Kịch mục dựa trên cổ tích kinh điển và truyền thuyết dân gian Mordvin.",
        "Điểm đến lý tưởng cho gia đình có trẻ nhỏ.",
    ],
    p("Buổi diễn thường vào cuối tuần và ban ngày, phù hợp trẻ em; xem lịch trên trang chính thức.",
      "Vé theo suất, giá rất phải chăng.",
      "45–75 phút mỗi suất.",
      "Cuối tuần, dịp nghỉ lễ và kỳ nghỉ học của trẻ.",
      "Đặt vé trước cho suất cuối tuần; phù hợp gia đình có con nhỏ."),
    [
        {"title": "Wikipedia (RU) — Мордовский государственный театр кукол", "url": "https://ru.wikipedia.org/wiki/Мордовский_государственный_театр_кукол"},
        {"title": "Culture.ru — Театр кукол Республики Мордовия", "url": "https://www.culture.ru/"},
    ],
    ["theatre", "puppet", "family", "children", "folk"],
    maps_text("Государственный театр кукол Республики Мордовия", "Саранск",
              "Mordovia State Puppet Theatre", "Saransk", 54.191887, 45.189691),
))

# ============================ NHÀ THỜ / TU VIỆN (church) ============================

# 13) Церковь Иоанна Богослова (Саранск) ----------------------------------------
RECORDS.append(rec(
    "ioann-bogoslov-church-saransk",
    "Nhà thờ Thánh Gioan Thần học (công trình cổ nhất Saransk)",
    "Церковь Иоанна Богослова",
    "Church of St. John the Theologian (Saransk)",
    ["church"],
    54.182475, 45.178922,
    "Phố Demokraticheskaya (khu Streletskaya sloboda cũ), thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Xây bằng đá năm 1693, đây là công trình lâu đời nhất còn tồn tại ở Saransk và cả vùng, được xếp hạng di tích kiến trúc cấp liên bang. Từng giữ vai trò nhà thờ chính toà của giáo phận giai đoạn 1991–2006.",
    "Trong khu phố cổ Saransk, trên nền của làng cung thủ (Streletskaya sloboda) xưa, Nhà thờ Thánh Gioan Thần học lặng lẽ giữ danh hiệu công trình lâu đời nhất còn nguyên vẹn của thành phố và cả nước cộng hoà. Được các cung thủ (streltsy) dựng bằng đá năm 1693, thay cho ngôi nhà thờ gỗ trước đó, thánh đường mang phong cách kiến trúc Nga cuối thế kỷ 17 với khối tường trắng chắc chắn, các mái vòm cổ điển và tháp chuông, thể hiện vẻ đẹp mộc mạc mà trang nghiêm của thời tiền Petrine. Nhờ giá trị lịch sử và kiến trúc, nhà thờ được công nhận là di tích cấp liên bang. Trải qua hơn ba thế kỷ với bao thăng trầm, công trình vẫn đứng vững và trong giai đoạn 1991–2006 từng đảm nhận vai trò nhà thờ chính toà của giáo phận Saransk, trước khi vị trí này chuyển sang Nhà thờ Ushakov mới xây. Ngày nay, nhà thờ vẫn là nơi hành lễ đều đặn và là điểm chiêm bái quen thuộc. Với du khách, đây là nơi cảm nhận rõ nhất chiều sâu lịch sử của Saransk - một 'nhân chứng đá' đã tồn tại từ thuở thành phố còn là pháo đài biên ải.",
    [
        "Công trình lâu đời nhất còn tồn tại ở Saransk và cả vùng (xây bằng đá năm 1693).",
        "Di tích kiến trúc cấp liên bang mang phong cách Nga cuối thế kỷ 17.",
        "Từng là nhà thờ chính toà của giáo phận Saransk giai đoạn 1991–2006.",
    ],
    p("Mở cửa hằng ngày theo lịch lễ; nên đến ngoài giờ hành lễ để tham quan.",
      "Miễn phí (công đức tuỳ tâm).",
      "20–30 phút.",
      "Sáng hoặc chiều ngoài giờ lễ; kết hợp dạo phố cổ.",
      "Ăn mặc kín đáo, nữ nên trùm khăn; giữ yên lặng trong giờ lễ."),
    [
        {"title": "Wikipedia (RU) — Церковь Иоанна Богослова (Саранск)", "url": "https://ru.wikipedia.org/wiki/Церковь_Иоанна_Богослова_(Саранск)"},
        {"title": "Sobory.ru — Церковь Иоанна Богослова (Саранск)", "url": "https://sobory.ru/article/?object=04452"},
    ],
    ["church", "orthodox", "history", "architecture", "oldest"],
    maps_text("Церковь Иоанна Богослова", "Саранск",
              "Church of St. John the Theologian", "Saransk", 54.182475, 45.178922),
))

# 14) Троицкая церковь (Саранск) ------------------------------------------------
RECORDS.append(rec(
    "trinity-church-saransk",
    "Nhà thờ Chúa Ba Ngôi (Troitskaya tserkov, Saransk)",
    "Троицкая церковь",
    "Trinity Church (Saransk)",
    ["church"],
    54.186210, 45.191271,
    "Góc phố Volodarskogo và phố Bogdana Khmelnitskogo, thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Một trong những nhà thờ cổ nhất Mordovia, khởi dựng bằng đá khoảng năm 1700 và hoàn thiện năm 1771. Bị đóng cửa thời Xô Viết, được trả lại cho Giáo hội và phục hồi từ khoảng năm 2000.",
    "Toạ lạc ở góc phố Volodarskogo và Bogdana Khmelnitskogo, Nhà thờ Chúa Ba Ngôi là một trong những thánh đường cổ kính nhất còn lại của Saransk và Mordovia. Công trình bằng đá được khởi dựng vào khoảng năm 1700 và hoàn thiện toàn bộ vào năm 1771, với ba bàn thờ mà bàn thờ chính dâng kính Chúa Ba Ngôi Ban Sự Sống. Kiến trúc mang dấu ấn Baroque Nga tỉnh lẻ, với khối nhà thờ, phần refectory và tháp chuông nối liền, những chi tiết trang trí bằng gạch và mái vòm duyên dáng gợi nhớ vẻ đẹp của các nhà thờ thế kỷ 18. Dưới thời Xô Viết, như nhiều thánh đường khác, nhà thờ bị đóng cửa vào đầu thập niên 1930 và bị trưng dụng cho các mục đích thế tục, nhiều phần trang trí và mái vòm hư hại. Đến khoảng năm 2000, công trình được trao trả cho Giáo hội Chính thống, trùng tu và khôi phục hoạt động tôn giáo. Ngày nay, nhà thờ lại vang tiếng chuông và đón giáo dân, đồng thời là một điểm ngắm kiến trúc lịch sử thú vị cho du khách dạo bộ trong trung tâm cổ Saransk.",
    [
        "Một trong những nhà thờ cổ nhất Mordovia (khởi dựng ~1700, hoàn thiện 1771).",
        "Ba bàn thờ, bàn thờ chính dâng kính Chúa Ba Ngôi Ban Sự Sống.",
        "Bị đóng cửa thời Xô Viết, được phục hồi từ khoảng năm 2000.",
    ],
    p("Mở cửa theo lịch lễ; nên đến ngoài giờ hành lễ để tham quan.",
      "Miễn phí (công đức tuỳ tâm).",
      "20–30 phút.",
      "Sáng hoặc chiều ngoài giờ lễ.",
      "Ăn mặc kín đáo, nữ nên trùm khăn; kết hợp dạo trung tâm cổ Saransk."),
    [
        {"title": "Sobory.ru — Троицкая церковь (Саранск)", "url": "https://sobory.ru/article/?object=12827"},
        {"title": "Wikipedia (RU) — Саранск", "url": "https://ru.wikipedia.org/wiki/Саранск"},
    ],
    ["church", "orthodox", "history", "architecture", "baroque"],
    maps_text("Троицкая церковь", "Саранск",
              "Trinity Church", "Saransk", 54.186210, 45.191271),
))

# 15) Пайгармский Параскево-Вознесенский монастырь ------------------------------
RECORDS.append(rec(
    "paygarma-paraskeva-convent",
    "Tu viện nữ Paraskeva-Thăng Thiên Paygarma",
    "Пайгармский Параскево-Вознесенский женский монастырь",
    "Paygarma Paraskevo-Ascension Convent",
    ["church"],
    54.079072, 44.830798,
    "Làng Paygarm, huyện Ruzaevsky, Cộng hoà Mordovia, Nga (gần thành phố Ruzaevka)",
    "Tu viện nữ nổi tiếng lập năm 1864 quanh những suối nước thánh nơi tìm thấy tượng Thánh Paraskeva. Với các suối thiêng và hồ tắm, đây là một trong những điểm hành hương đông khách nhất Mordovia.",
    "Nằm ở làng Paygarm thuộc huyện Ruzaevsky, gần thành phố Ruzaevka, Tu viện nữ Paraskeva-Thăng Thiên Paygarma là một trong những trung tâm hành hương sầm uất và được yêu mến nhất Cộng hoà Mordovia. Tu viện được thành lập năm 1864 trên vùng đất do nữ ân nhân M.M. Kiseleva hiến tặng, gắn với truyền thuyết về những dòng suối thiêng nơi người ta tìm thấy một bức tượng (hình tượng) Thánh nữ Paraskeva - vị thánh được dân gian đặc biệt sùng kính. Quần thể tu viện dần hình thành với những công trình đồ sộ như Nhà thờ chính toà Uspensky (Đức Mẹ An Nghỉ, xây 1874–1890) và nhà thờ Thăng Thiên (Voznesensky, từ 1893), cùng các dãy nhà tu, tường bao và tháp chuông. Điều thu hút đông đảo khách hành hương là ba dòng suối nước thánh cùng những nhà tắm (kupel), nơi tín hữu đến cầu nguyện, lấy nước và trầm mình với niềm tin về sức mạnh chữa lành. Không gian tu viện thanh tịnh, cây xanh bao quanh mang lại cảm giác an yên. Nằm không xa Saransk, đây là điểm đến kết hợp giữa hành hương tâm linh và chiêm ngưỡng kiến trúc Chính thống giáo thế kỷ 19.",
    [
        "Tu viện nữ lập năm 1864 quanh những suối nước thánh gắn với Thánh Paraskeva.",
        "Có Nhà thờ chính toà Uspensky (1874–1890) và nhà thờ Thăng Thiên (từ 1893).",
        "Ba dòng suối thiêng và nhà tắm - điểm hành hương đông khách bậc nhất Mordovia.",
    ],
    p("Mở cửa hằng ngày đón khách hành hương theo lịch tu viện, thường từ sáng đến chiều tối.",
      "Miễn phí (công đức tuỳ tâm).",
      "1–1,5 giờ.",
      "Mùa hè và các dịp lễ kính Thánh Paraskeva; đông khách cuối tuần.",
      "Gần Ruzaevka, cách Saransk không xa; nữ mang khăn và váy dài; mang chai để lấy nước suối thánh."),
    [
        {"title": "Sobory.ru — Пайгармский Параскево-Вознесенский монастырь", "url": "https://sobory.ru/article/?object=17594"},
        {"title": "Wikipedia (RU) — Пайгарма", "url": "https://ru.wikipedia.org/wiki/Пайгарма"},
    ],
    ["monastery", "convent", "orthodox", "pilgrimage", "holy-spring"],
    maps_org("https://yandex.ru/maps/org/paraskevo_voznesenskiy_paygarmskiy_zhenskiy_monastyr/1289855628/",
             "Paygarma Paraskevo-Ascension Convent", "Ruzaevsky District"),
))

# 16) Свято-Троицкий Чуфаровский монастырь --------------------------------------
RECORDS.append(rec(
    "chufarovo-trinity-monastery",
    "Tu viện Chúa Ba Ngôi Chufarovo",
    "Свято-Троицкий Чуфаровский мужской монастырь",
    "Chufarovo Holy Trinity Monastery",
    ["church"],
    54.423406, 45.518804,
    "Làng Bolshoye Chufarovo, huyện Romodanovsky, Cộng hoà Mordovia, Nga",
    "Tu viện có nguồn gốc từ giữa thế kỷ 19, do người nông dân khổ hạnh Ignaty Vershin lập làm nhà tế bần. Thời Xô Viết bị biến thành nhà tù điều tra của NKVD; nay là tu viện nam với nhà thờ tưởng niệm các Tân Tử đạo.",
    "Ở làng Bolshoye Chufarovo thuộc huyện Romodanovsky, phía bắc Saransk, Tu viện Chúa Ba Ngôi Chufarovo mang trong mình một câu chuyện vừa linh thiêng vừa bi tráng. Cộng đồng tu hành ở đây khởi nguồn từ giữa thập niên 1840, khi người nông dân - trưởng lão khổ hạnh Ignaty Vershin lập nên một nhà tế bần (bogadelnya) cho người nghèo và cô quả; về sau nơi này phát triển thành tu viện. Nhưng bước ngoặt đen tối đến vào thời Xô Viết: tu viện bị đóng cửa và biến thành một nhà tù điều tra của cơ quan NKVD - người dân địa phương quen gọi bằng cái tên 'Chufara'. Nhiều tù nhân, trong đó có các giáo sĩ, đã chịu khổ nạn và bỏ mình tại đây trong những năm khủng bố. Sau khi được phục hồi làm tu viện nam từ năm 1994 và cung hiến lại cho Chúa Ba Ngôi, một nhà thờ dâng kính các Tân Tử đạo (xây năm 1997) đã được dựng lên để tưởng niệm những nạn nhân thời Stalin. Ngày nay, tu viện là nơi tĩnh tâm, cầu nguyện và cũng là một 'địa chỉ ký ức' nhắc nhở về một chương đau thương của lịch sử. Với du khách quan tâm đến lịch sử tôn giáo và thế kỷ 20 của nước Nga, Chufarovo là điểm đến giàu chiều sâu.",
    [
        "Khởi nguồn từ giữa thế kỷ 19, do trưởng lão khổ hạnh Ignaty Vershin lập làm nhà tế bần.",
        "Thời Xô Viết bị biến thành nhà tù điều tra của NKVD ('Chufara').",
        "Nay là tu viện nam với nhà thờ tưởng niệm các Tân Tử đạo (1997).",
    ],
    p("Mở cửa hằng ngày đón khách theo lịch tu viện, thường từ sáng đến chiều tối.",
      "Miễn phí (công đức tuỳ tâm).",
      "1–1,5 giờ (chưa kể di chuyển).",
      "Mùa hè; tránh mùa mưa đường xấu.",
      "Cách Saransk qua Romodanovo; nên đi ô tô; nữ mang khăn và váy dài."),
    [
        {"title": "Sobory.ru — Свято-Троицкий Чуфаровский монастырь", "url": "https://sobory.ru/article/?object=17590"},
        {"title": "Wikipedia (RU) — Большое Чуфарово", "url": "https://ru.wikipedia.org/wiki/Большое_Чуфарово"},
    ],
    ["monastery", "orthodox", "history", "memory", "pilgrimage"],
    maps_org("https://yandex.ru/maps/org/troitskiy_chufarovskiy_muzhskoy_monastyr/1734746722/",
             "Chufarovo Holy Trinity Monastery", "Romodanovsky District"),
))

# ============================ ĐÀI TƯỞNG NIỆM (monument) ============================

# 17) Монумент «Навеки с Россией» -----------------------------------------------
RECORDS.append(rec(
    "forever-with-russia-monument-saransk",
    "Đài tưởng niệm 'Mãi mãi cùng nước Nga'",
    "Монумент «Навеки с Россией»",
    "Monument 'Forever with Russia'",
    ["monument"],
    54.177758, 45.188944,
    "Phố Moskovskaya (đầu dốc đài phun nước), thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Đài tưởng niệm dựng năm 1986 nhân 500 năm dân tộc Mordvin sáp nhập vào nước Nga. Hai người phụ nữ bằng đồng trong trang phục Mordvin nâng bó lúa mì, đứng trên bệ đá granite cao khoảng 20 mét.",
    "Sừng sững ở đầu dốc đài phun nước trên phố Moskovskaya, đài tưởng niệm 'Mãi mãi cùng nước Nga' (Naveki s Rossiey) là một trong những biểu tượng điêu khắc đô thị nổi bật của Saransk. Công trình được dựng năm 1986 nhân kỷ niệm 500 năm dân tộc Mordvin gia nhập nhà nước Nga - một cột mốc lịch sử được nhấn mạnh trong bản sắc của nước cộng hoà. Tác phẩm do kiến trúc sư I.A. Pokrovsky và nhà điêu khắc I.D. Brodsky thực hiện, khắc hoạ hai người phụ nữ bằng đồng - biểu tượng cho dân tộc Nga và dân tộc Mordvin - trong trang phục truyền thống, cùng nâng bó lúa mì như hình ảnh của tình hữu nghị, sự no ấm và gắn bó. Bệ tượng bằng đá granite cao khoảng 20 mét vươn lên trên đỉnh dốc, tạo điểm nhấn thị giác cho cả trục không gian chạy từ Quảng trường Sovetskaya xuống Công viên Pushkin. Xung quanh là quảng trường thoáng đãng, bậc thang và đài phun nước, nơi người dân thường dạo bộ và chụp ảnh. Với du khách, đây vừa là một tác phẩm nghệ thuật hoành tráng vừa là chìa khoá để hiểu câu chuyện lịch sử làm nên căn tính của Mordovia.",
    [
        "Dựng năm 1986 nhân 500 năm dân tộc Mordvin gia nhập nước Nga.",
        "Hai phụ nữ bằng đồng trong trang phục truyền thống nâng bó lúa mì trên bệ granite ~20 m.",
        "Điểm nhấn của trục không gian từ Quảng trường Sovetskaya xuống Công viên Pushkin.",
    ],
    p("Đài ngoài trời, tham quan tự do cả ngày.",
      "Miễn phí.",
      "15–20 phút.",
      "Chiều tối khi đài phun nước và đèn hoạt động (mùa ấm).",
      "Kết hợp đi bộ dọc dốc đài phun nước xuống Công viên Pushkin."),
    [
        {"title": "Wikipedia (RU) — Саранск (памятники)", "url": "https://ru.wikipedia.org/wiki/Саранск"},
        {"title": "Culture.ru — Монумент «Навеки с Россией»", "url": "https://www.culture.ru/"},
    ],
    ["monument", "history", "sculpture", "landmark", "outdoor"],
    maps_text("Монумент Навеки с Россией", "Саранск",
              "Monument Forever with Russia", "Saransk", 54.177758, 45.188944),
))

# 18) Памятник героям-стратонавтам ----------------------------------------------
RECORDS.append(rec(
    "stratonauts-monument-saransk",
    "Đài tưởng niệm các anh hùng khí cầu tầng bình lưu",
    "Памятник героям-стратонавтам",
    "Monument to the Heroes-Stratonauts",
    ["monument"],
    54.195834, 45.189339,
    "Quảng trường Geroev-Stratonavtov (gần ga đường sắt), thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Đài tưởng niệm khánh thành năm 1963 tưởng nhớ ba nhà thám hiểm tầng bình lưu tử nạn năm 1934 khi khinh khí cầu 'Osoaviakhim-1' rơi gần Mordovia. Tượng một phi công trên bệ đá labradorite.",
    "Trên quảng trường mang tên Các anh hùng khí cầu tầng bình lưu, gần ga đường sắt Saransk, có một đài tưởng niệm gắn với một sự kiện bi tráng của lịch sử hàng không Xô Viết. Ngày 30/1/1934, khinh khí cầu tầng bình lưu 'Osoaviakhim-1' đạt độ cao kỷ lục hơn 22 km, nhưng trên đường hạ xuống đã gặp nạn và rơi ở khu vực gần Potizh-Ostrog phía nam Mordovia, khiến ba thành viên phi hành đoàn - Fedoseenko, Vasenko và Usyskin - thiệt mạng. Để tưởng nhớ họ, đài tưởng niệm được dựng và khánh thành ngày 30/1/1963, đúng 29 năm sau thảm kịch. Tác phẩm - do nhà điêu khắc A.A. Pismenny và kiến trúc sư A.N. Dushkin thực hiện - khắc hoạ hình tượng một phi công vươn lên trên bệ đá labradorite sẫm màu, gợi tinh thần quả cảm chinh phục bầu trời. Đài nằm ở khu vực cửa ngõ giao thông của thành phố, trở thành một điểm mốc quen thuộc và là nơi đặt hoa tưởng niệm. Với du khách, công trình vừa là một tác phẩm điêu khắc thời Xô Viết đáng chú ý, vừa là câu chuyện ít người biết về mối liên hệ giữa Mordovia và những trang sử chinh phục tầng bình lưu.",
    [
        "Tưởng nhớ ba nhà thám hiểm khí cầu 'Osoaviakhim-1' tử nạn năm 1934 gần Mordovia.",
        "Khánh thành năm 1963, tượng một phi công trên bệ đá labradorite.",
        "Điểm mốc quen thuộc ở khu vực cửa ngõ ga đường sắt Saransk.",
    ],
    p("Đài ngoài trời, tham quan tự do cả ngày.",
      "Miễn phí.",
      "10–15 phút.",
      "Ban ngày; tiện ghé khi đến/rời ga đường sắt.",
      "Gần ga tàu, hợp để ngắm nhanh khi di chuyển; tìm hiểu trước câu chuyện Osoaviakhim-1 để cảm nhận ý nghĩa."),
    [
        {"title": "Wikipedia (RU) — Осоавиахим-1", "url": "https://ru.wikipedia.org/wiki/Осоавиахим-1"},
        {"title": "Wikipedia (RU) — Саранск", "url": "https://ru.wikipedia.org/wiki/Саранск"},
    ],
    ["monument", "history", "soviet", "aviation", "outdoor"],
    maps_text("Памятник героям-стратонавтам", "Саранск",
              "Monument to the Heroes-Stratonauts", "Saransk", 54.195834, 45.189339),
))

# ============================ QUẢNG TRƯỜNG / PHỐ (square_street) ============================

# 19) Площадь Тысячелетия -------------------------------------------------------
RECORDS.append(rec(
    "millennium-square-saransk",
    "Quảng trường Thiên niên kỷ (Ploshchad Tysyacheletiya)",
    "Площадь Тысячелетия",
    "Millennium Square",
    ["square_street"],
    54.187253, 45.183938,
    "Gần Đại học Quốc gia Mordovia, trung tâm thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Quảng trường hiện đại khánh thành năm 2012 nhân 1000 năm tình đoàn kết giữa dân tộc Mordvin và nước Nga. Trung tâm là đài phun nước 'Ngôi sao Mordovia' khổng lồ với những tia nước vọt cao.",
    "Là một trong những không gian công cộng mới và ấn tượng nhất Saransk, Quảng trường Thiên niên kỷ được khánh thành năm 2012 để đánh dấu cột mốc 1000 năm tình đoàn kết giữa các dân tộc Mordvin và nước Nga. Quảng trường nằm gần khuôn viên Đại học Quốc gia Mordovia, mang diện mạo hiện đại với những mảng lát đá rộng, cây xanh và không gian mở thoáng đãng. Điểm nhấn nổi bật nhất là đài phun nước lớn hình 'Ngôi sao Mordovia' - biểu tượng mặt trời bảy cánh gắn với văn hoá bản địa - với đường kính lên tới khoảng 60 mét và những cột nước có thể vọt cao hàng chục mét. Vào mùa ấm, đài phun nước hoạt động với chương trình nước, ánh sáng và âm nhạc buổi tối, biến quảng trường thành điểm hẹn giải trí sôi động của người dân và du khách. Đây cũng là nơi tổ chức các sự kiện lớn, lễ hội thành phố và hoạt động sinh viên. Với kiến trúc cảnh quan bắt mắt và ý nghĩa biểu tượng sâu sắc, Quảng trường Thiên niên kỷ là điểm dừng lý tưởng để cảm nhận diện mạo đương đại và tinh thần tự hào dân tộc của Saransk.",
    [
        "Khánh thành năm 2012 nhân 1000 năm dân tộc Mordvin đoàn kết với nước Nga.",
        "Đài phun nước 'Ngôi sao Mordovia' khổng lồ (đường kính ~60 m) với tia nước vọt cao.",
        "Chương trình nước - ánh sáng - âm nhạc buổi tối vào mùa ấm.",
    ],
    p("Quảng trường ngoài trời, tham quan tự do; đài phun nước hoạt động theo mùa ấm.",
      "Miễn phí.",
      "30–45 phút.",
      "Chiều tối mùa hè khi đài phun nước biểu diễn ánh sáng - âm nhạc.",
      "Đến vào buổi tối để xem show nước; gần khuôn viên đại học, không khí trẻ trung."),
    [
        {"title": "Wikipedia (RU) — Саранск", "url": "https://ru.wikipedia.org/wiki/Саранск"},
        {"title": "Culture.ru — Площадь Тысячелетия (Саранск)", "url": "https://www.culture.ru/"},
    ],
    ["square", "modern", "fountain", "landmark", "family"],
    maps_text("Площадь Тысячелетия", "Саранск",
              "Millennium Square", "Saransk", 54.187253, 45.183938),
))

# 20) Фонтанный спуск -----------------------------------------------------------
RECORDS.append(rec(
    "fountain-descent-saransk",
    "Dốc đài phun nước (Fontanny spusk)",
    "Фонтанный спуск (каскад фонтанов)",
    "Fountain Descent (cascade of fountains)",
    ["square_street"],
    54.179440, 45.186110,
    "Phố Moskovskaya, nối Quảng trường Sovetskaya xuống Công viên Pushkin, thành phố Saransk, Cộng hoà Mordovia, Nga",
    "Chuỗi bậc thang - đài phun nước dài khoảng 250 m nối Quảng trường Sovetskaya xuống Công viên Pushkin, hình thành từ thập niên 1970–80. Dọc dốc có tượng đài Pushkin và các nhà sáng lập Saransk.",
    "Nối liền phần trên của trung tâm Saransk với Công viên Pushkin bên dưới, Dốc đài phun nước là một tuyến đi bộ - cảnh quan duyên dáng và được người dân yêu thích. Đây là chuỗi bậc thang xen kẽ các bồn phun nước chảy tầng, kéo dài khoảng 250 mét, được hình thành từ thập niên 1970–1980 và được xem là quần thể đài phun nước đầu tiên của thành phố. Từ khu vực Quảng trường Sovetskaya, lối đi thoải dần xuống thung lũng sông Saranka và công viên, tạo nên một trục cảnh quan liền mạch, nơi tiếng nước chảy róc rách hoà cùng bóng cây mát rượi. Dọc theo dốc là những công trình điêu khắc và tượng đài, trong đó có tượng đại thi hào A.S. Pushkin và tượng đài các nhà sáng lập Saransk, biến con dốc thành một 'phòng trưng bày ngoài trời' nhỏ. Vào mùa hè, khi các đài phun hoạt động, đây là nơi lý tưởng để dạo mát, chụp ảnh và nghỉ chân; buổi tối lên đèn càng thêm lãng mạn. Với du khách, Dốc đài phun nước là một trải nghiệm đi bộ dễ chịu, kết nối tự nhiên nhiều điểm tham quan ở trung tâm.",
    [
        "Chuỗi bậc thang - đài phun nước dài ~250 m, quần thể đài phun đầu tiên của Saransk.",
        "Nối Quảng trường Sovetskaya xuống Công viên Pushkin dọc thung lũng sông Saranka.",
        "Dọc dốc có tượng Pushkin và tượng đài các nhà sáng lập thành phố.",
    ],
    p("Không gian ngoài trời, dạo tự do; đài phun nước hoạt động theo mùa ấm.",
      "Miễn phí.",
      "20–40 phút.",
      "Chiều tối mùa hè khi đài phun nước và đèn hoạt động.",
      "Đi bộ từ trên xuống Công viên Pushkin; tiện kết hợp đài 'Navek s Rossiey' ở đầu dốc."),
    [
        {"title": "Wikipedia (RU) — Саранск", "url": "https://ru.wikipedia.org/wiki/Саранск"},
        {"title": "Culture.ru — Достопримечательности Саранска", "url": "https://www.culture.ru/"},
    ],
    ["square", "fountain", "walking", "park", "outdoor"],
    maps_text("Фонтанный спуск", "Саранск",
              "Fountain Descent", "Saransk", 54.179440, 45.186110),
))

# 21) Соборная площадь ----------------------------------------------------------
RECORDS.append(rec(
    "sobornaya-square-saransk",
    "Quảng trường Sobornaya (Quảng trường Nhà thờ Chính toà)",
    "Соборная площадь",
    "Sobornaya (Cathedral) Square",
    ["square_street"],
    54.182715, 45.181792,
    "Trung tâm thành phố Saransk (quanh Nhà thờ Ushakov), Cộng hoà Mordovia, Nga",
    "Quảng trường trung tâm hình thành năm 2006 quanh Nhà thờ Chính toà Ushakov mới xây - thánh đường cao nhất vùng Volga. Đây là không gian nghi lễ và biểu tượng chính của thủ phủ Saransk.",
    "Là trái tim không gian của Saransk hiện đại, Quảng trường Sobornaya được hình thành năm 2006 cùng với việc khánh thành Nhà thờ Chính toà Thánh Fyodor Ushakov - thánh đường Chính thống cao nhất vùng Volga (khoảng 63 mét). Quảng trường rộng rãi, lát đá, với đài phun nước, các lối đi, bồn hoa và tượng đô đốc Ushakov, tạo nên một tổng thể trang nghiêm mà thoáng đãng. Đây là nơi diễn ra các nghi lễ tôn giáo trọng thể, sự kiện thành phố, lễ hội và cũng là điểm dạo bộ, thư giãn quen thuộc của người dân mỗi chiều. Vào các dịp lễ lớn và buổi tối, khi nhà thờ và quảng trường lên đèn, khung cảnh trở nên đặc biệt ấn tượng, thu hút đông người đến chụp ảnh và tận hưởng không khí. Bao quanh quảng trường là các công trình hành chính, văn hoá và những trục phố chính, nên đây thường là điểm khởi đầu tự nhiên cho hành trình khám phá trung tâm Saransk. Dù còn khá mới, Quảng trường Sobornaya đã trở thành biểu tượng và niềm tự hào của thủ phủ Mordovia.",
    [
        "Quảng trường trung tâm hình thành năm 2006 quanh Nhà thờ Chính toà Ushakov.",
        "Không gian rộng với đài phun nước và tượng đô đốc Ushakov.",
        "Nơi diễn ra nghi lễ, sự kiện lớn và là biểu tượng của thủ phủ Saransk.",
    ],
    p("Quảng trường ngoài trời, tham quan tự do cả ngày.",
      "Miễn phí.",
      "30–45 phút.",
      "Chiều tối khi nhà thờ và quảng trường lên đèn; các dịp lễ lớn.",
      "Là điểm khởi đầu để tham quan trung tâm; kết hợp Nhà thờ Ushakov ngay bên cạnh."),
    [
        {"title": "Wikipedia (RU) — Собор Феодора Ушакова (Саранск)", "url": "https://ru.wikipedia.org/wiki/Собор_Феодора_Ушакова_(Саранск)"},
        {"title": "Wikipedia (RU) — Саранск", "url": "https://ru.wikipedia.org/wiki/Саранск"},
    ],
    ["square", "landmark", "central", "outdoor", "orthodox"],
    maps_text("Соборная площадь", "Саранск",
              "Sobornaya Square", "Saransk", 54.182715, 45.181792),
))

# ============================ CÔNG VIÊN / THIÊN NHIÊN (park_garden) ============================

# 22) Симкинский природный парк -------------------------------------------------
RECORDS.append(rec(
    "simkino-nature-park",
    "Công viên thiên nhiên Simkino và cây sồi cổ",
    "Симкинский природный парк устойчивого развития",
    "Simkino Nature Park (Symkinsky Park)",
    ["park_garden"],
    54.255109, 46.173334,
    "Gần làng Simkino, huyện Bolshebereznikovsky, Cộng hoà Mordovia, Nga (thung lũng sông Sura)",
    "Công viên thiên nhiên trong vùng ngập lũ sông Sura, nổi tiếng với cây sồi cổ thụ hàng trăm năm tuổi - được xem là cây thiêng của người Mordvin và công nhận là di tích thiên nhiên năm 2012.",
    "Ẩn mình trong thung lũng ngập lũ của sông Sura ở huyện Bolshebereznikovsky, phía đông Mordovia, Công viên thiên nhiên Simkino là một ốc đảo xanh gắn với tín ngưỡng và truyền thuyết của người Mordvin. Công viên trải rộng khoảng một nghìn ha rừng ven sông, đồng cỏ và đầm nước, là nơi bảo tồn hệ động thực vật của vùng chuyển tiếp rừng - thảo nguyên. Báu vật nổi tiếng nhất của công viên là một cây sồi cổ thụ (Quercus robur) khổng lồ, ước tính vài trăm năm tuổi, cao chừng 25–30 mét, được công nhận là di tích thiên nhiên năm 2012. Với người Erzya bản địa, cây sồi này từ lâu được coi là cây thiêng, gắn với các nghi lễ cầu mùa, sinh sôi và những câu chuyện dân gian; nhiều du khách đến đây để chạm vào thân cây, buộc dải ruy băng và cầu nguyện theo truyền thống. Xung quanh, các lối mòn sinh thái, suối nguồn và cảnh quan sông nước tạo nên không gian yên bình để đi bộ, dã ngoại và hoà mình vào thiên nhiên. Là điểm đến kết hợp giữa sinh thái và văn hoá tâm linh bản địa, Simkino mang lại trải nghiệm khác biệt so với các danh thắng đô thị của Mordovia.",
    [
        "Công viên thiên nhiên rộng khoảng 1.000 ha trong thung lũng ngập lũ sông Sura.",
        "Cây sồi cổ thụ hàng trăm năm tuổi - di tích thiên nhiên (2012), được coi là cây thiêng của người Mordvin.",
        "Lối mòn sinh thái, suối nguồn và cảnh quan sông nước để đi bộ, dã ngoại.",
    ],
    p("Không gian thiên nhiên ngoài trời; nên đi ban ngày, có thể cần hướng dẫn viên địa phương cho các tuyến.",
      "Thường miễn phí hoặc phí thấp; một số tuyến/tour có thu phí.",
      "Nửa ngày (chưa kể di chuyển).",
      "Từ cuối tháng 5 đến tháng 9, khi thời tiết ấm và cây cối tươi tốt.",
      "Ở khá xa Saransk về phía đông; nên đi ô tô; mang giày đi rừng, thuốc chống côn trùng và nước uống."),
    [
        {"title": "Wikipedia (RU) — Большеберезниковский район", "url": "https://ru.wikipedia.org/wiki/Большеберезниковский_район"},
        {"title": "Официальный туризм Мордовии — Симкинский парк", "url": "https://www.culture.ru/"},
    ],
    ["nature", "park", "oak", "sura", "ecotourism"],
    maps_text("Симкинский природный парк Симкино", "Мордовия",
              "Simkino Nature Park", "Bolshebereznikovsky District", 54.255109, 46.173334),
))

# ============================ ĐIỀN TRANG (palace/усадьба) ============================

# 23) Староакшинская усадьба Огарёвых -------------------------------------------
RECORDS.append(rec(
    "ogarev-estate-staroe-akshino",
    "Điền trang gia tộc Ogaryov ở Staroe Akshino",
    "Староакшинская усадьба Огарёвых",
    "Ogaryov Family Estate in Staroe Akshino",
    ["palace"],
    54.290821, 44.707245,
    "Làng Staroe Akshino, huyện Staroshaygovsky, Cộng hoà Mordovia, Nga",
    "Điền trang tổ tiên của nhà thơ, nhà cách mạng Nikolai Ogaryov (bạn thân của Herzen). Dinh thự chính không còn, nhưng chuỗi hồ, hàng cây 'ngõ Ogaryov' trăm tuổi và công viên cảnh quan vẫn được gìn giữ, có bảo tàng tưởng niệm mở năm 1975.",
    "Ở làng Staroe Akshino thuộc huyện Staroshaygovsky, có một điền trang mang đậm dấu ấn văn học và lịch sử tư tưởng Nga: điền trang của gia tộc Ogaryov - nơi gắn với tên tuổi Nikolai Platonovich Ogaryov (1813–1877), nhà thơ, nhà chính luận và nhà cách mạng, người bạn tâm giao cùng chí hướng với Alexander Herzen. Đây từng là dinh cơ của dòng họ, nơi Ogaryov trải qua những năm tháng và ấp ủ nhiều ý tưởng tiến bộ của mình. Đáng tiếc, toà nhà chính của điền trang đã không còn tồn tại qua những biến thiên thời gian; song những gì còn lại vẫn đủ gợi lên không khí của một trang viên quý tộc thế kỷ 19: chuỗi hồ nước bậc thang, hàng cây gia (linden) và thông rụng lá trăm tuổi được gọi là 'ngõ Ogaryov', cùng khu công viên cảnh quan trải rộng. Năm 1975, một bảo tàng tưởng niệm đã được mở để tôn vinh nhà thơ và giới thiệu về gia tộc Ogaryov cũng như những nhân vật liên quan như N.A. Tuchkova-Ogaryova và nhà thơ N.M. Satin. Với du khách yêu văn học và lịch sử, đây là điểm đến trầm mặc, nơi cảnh quan và ký ức hoà quyện giữa vùng quê yên tĩnh của Mordovia.",
    [
        "Điền trang tổ tiên của nhà thơ - nhà cách mạng Nikolai Ogaryov, bạn thân của Herzen.",
        "Dinh thự chính không còn, nhưng chuỗi hồ, 'ngõ Ogaryov' trăm tuổi và công viên cảnh quan vẫn còn.",
        "Có bảo tàng tưởng niệm mở năm 1975 về gia tộc Ogaryov.",
    ],
    p("Cảnh quan ngoài trời tham quan tự do; bảo tàng/khu tưởng niệm mở theo lịch, nên hỏi trước.",
      "Dạo công viên miễn phí; bảo tàng (nếu mở) thu phí nhỏ.",
      "1–1,5 giờ (chưa kể di chuyển).",
      "Mùa hè và đầu thu khi cây cối và hồ nước đẹp nhất.",
      "Ở vùng quê xa Saransk; nên đi ô tô; tìm hiểu trước về Ogaryov và Herzen để cảm nhận sâu hơn."),
    [
        {"title": "Wikipedia (RU) — Огарёв, Николай Платонович", "url": "https://ru.wikipedia.org/wiki/Огарёв,_Николай_Платонович"},
        {"title": "Wikipedia (RU) — Старошайговский район", "url": "https://ru.wikipedia.org/wiki/Старошайговский_район"},
    ],
    ["estate", "manor", "literary", "ogaryov", "park"],
    maps_text("Усадьба Огарёва Старое Акшино", "Мордовия",
              "Ogaryov Estate", "Staroe Akshino", 54.290821, 44.707245),
))

# ============================ THỊ TRẤN / ĐÔ THỊ (other) ============================

# 24) Краснослободск ------------------------------------------------------------
RECORDS.append(rec(
    "krasnoslobodsk-town",
    "Thị trấn cổ Krasnoslobodsk",
    "Краснослободск",
    "Krasnoslobodsk",
    ["other"],
    54.430672, 43.777900,
    "Thị trấn Krasnoslobodsk, huyện Krasnoslobodsky, Cộng hoà Mordovia, Nga (bên sông Moksha)",
    "Thị trấn thương mại cổ bên tả ngạn sông Moksha, cách Saransk khoảng 107 km về phía tây. Trở thành thành phố huyện năm 1780, nổi tiếng với kiến trúc nhà buôn cổ và các di tích tôn giáo.",
    "Bên tả ngạn dòng Moksha thơ mộng, cách Saransk chừng 107 km về phía tây, Krasnoslobodsk là một trong những thị trấn giàu lịch sử của Cộng hoà Mordovia. Khu định cư này có nguồn gốc từ một pháo đài - làng nghề trên tuyến phòng thủ biên giới thời Sa hoàng, và đến năm 1780 chính thức trở thành thành phố huyện (uezd) thuộc vùng phó vương Penza. Suốt thế kỷ 18–19, nhờ vị trí bên sông và trên các tuyến buôn bán, thị trấn phát triển thành một trung tâm thương mại sầm uất với tầng lớp thương nhân giàu có, để lại nhiều dinh thự, dãy phố buôn (torgovye ryady) và công trình tôn giáo mang phong cách kiến trúc tỉnh lẻ đặc trưng. Dạo bước trong trung tâm, du khách vẫn bắt gặp những ngôi nhà gạch cổ kính, nhịp sống chậm rãi và khung cảnh sông nước yên bình đặc trưng của nước Nga sâu trong nội địa. Thị trấn cũng là cửa ngõ để khám phá vùng nông thôn phía tây Mordovia. Dù không ồn ào dịch vụ du lịch, chính sự mộc mạc và bề dày lịch sử khiến Krasnoslobodsk trở thành điểm dừng chân dễ chịu cho ai muốn tìm hiểu chiều sâu văn hoá vùng đất này.",
    [
        "Thị trấn thương mại cổ bên sông Moksha, thành phố huyện từ năm 1780.",
        "Kiến trúc nhà buôn, dãy phố buôn và công trình tôn giáo tỉnh lẻ đặc trưng.",
        "Cửa ngõ khám phá vùng nông thôn phía tây Mordovia.",
    ],
    p("Tham quan ngoài trời tự do; các cơ sở địa phương mở theo giờ hành chính.",
      "Dạo thị trấn miễn phí.",
      "2–3 giờ.",
      "Mùa hè khi thời tiết thuận lợi để đi dạo.",
      "Cách Saransk ~107 km; nên đi ô tô; dịch vụ du lịch còn ít nên chuẩn bị ăn uống, đi lại trước."),
    [
        {"title": "Wikipedia (RU) — Краснослободск (Мордовия)", "url": "https://ru.wikipedia.org/wiki/Краснослободск_(Мордовия)"},
        {"title": "Wikipedia (EN) — Krasnoslobodsk, Republic of Mordovia", "url": "https://en.wikipedia.org/wiki/Krasnoslobodsk,_Republic_of_Mordovia"},
    ],
    ["town", "history", "moksha", "merchant", "oldtown"],
    maps_text("Краснослободск", "Мордовия",
              "Krasnoslobodsk", "Mordovia", 54.430672, 43.777900),
))

# 25) Рузаевка ------------------------------------------------------------------
RECORDS.append(rec(
    "ruzaevka-town",
    "Thành phố đường sắt Ruzaevka",
    "Рузаевка",
    "Ruzaevka",
    ["other"],
    54.058735, 44.954391,
    "Thành phố Ruzaevka, huyện Ruzaevsky, Cộng hoà Mordovia, Nga (cách Saransk ~25 km)",
    "Thành phố lớn thứ hai của Mordovia và là đầu mối đường sắt quan trọng với depot đầu máy lớn. Nổi tiếng với 'nước Cộng hoà Ruzaevka' - sự kiện công nhân đường sắt tự quản năm 1905.",
    "Nằm cách Saransk khoảng 25 km, Ruzaevka là thành phố lớn thứ hai của Cộng hoà Mordovia và mang đậm căn tính của một 'thành phố đường sắt'. Được nhắc đến lần đầu năm 1631, khu định cư này thực sự chuyển mình khi tuyến đường sắt đi qua vào cuối thế kỷ 19, biến nó thành một đầu mối giao thông quan trọng trên mạng lưới đường sắt Nga với depot đầu máy quy mô lớn và đông đảo công nhân. Chính đội ngũ công nhân đường sắt đã làm nên trang sử đáng nhớ nhất của thành phố: trong Cách mạng 1905, họ đã lập nên cái gọi là 'nước Cộng hoà Ruzaevka' - một chính quyền tự quản ngắn ngủi của công nhân, trở thành biểu tượng của phong trào công nhân Nga đầu thế kỷ 20. Ruzaevka chính thức trở thành thành phố năm 1937 và ngày nay vẫn là trung tâm công nghiệp - giao thông năng động, đồng thời là một 'vệ tinh' gắn bó chặt chẽ với thủ phủ Saransk. Với du khách, thành phố là nơi cảm nhận nhịp sống công nghiệp - đường sắt của vùng, và là điểm trung chuyển thuận tiện để đến Tu viện Paygarma linh thiêng gần đó.",
    [
        "Thành phố lớn thứ hai Mordovia, đầu mối đường sắt với depot đầu máy lớn.",
        "Gắn với 'nước Cộng hoà Ruzaevka' - chính quyền tự quản của công nhân năm 1905.",
        "Điểm trung chuyển thuận tiện để đến Tu viện Paygarma gần đó.",
    ],
    p("Tham quan ngoài trời tự do; cơ sở địa phương theo giờ hành chính.",
      "Dạo thành phố miễn phí.",
      "1,5–2 giờ.",
      "Quanh năm; mùa hè dễ đi lại hơn.",
      "Cách Saransk ~25 km, có tàu và xe khách; kết hợp thăm Tu viện Paygarma."),
    [
        {"title": "Wikipedia (RU) — Рузаевка", "url": "https://ru.wikipedia.org/wiki/Рузаевка"},
        {"title": "Wikipedia (EN) — Ruzayevka", "url": "https://en.wikipedia.org/wiki/Ruzayevka"},
    ],
    ["town", "railway", "history", "industrial", "revolution1905"],
    maps_text("Рузаевка", "Мордовия",
              "Ruzaevka", "Mordovia", 54.058735, 44.954391),
))

# 26) Инсар ---------------------------------------------------------------------
RECORDS.append(rec(
    "insar-town",
    "Thị trấn pháo đài cổ Insar",
    "Инсар",
    "Insar",
    ["other"],
    53.867741, 44.371407,
    "Thị trấn Insar, huyện Insarsky, Cộng hoà Mordovia, Nga (thị trấn cực nam của vùng)",
    "Thị trấn cực nam của Mordovia, lập năm 1647 làm pháo đài trên tuyến phòng thủ đông nam của nhà nước Nga. Vẫn giữ bố cục phố cổ thế kỷ 17–18, dãy phố buôn xưa và tu viện Svyato-Olginsky.",
    "Ở cực nam Cộng hoà Mordovia, bên dòng sông Insar nơi hợp lưu với sông Issa, thị trấn Insar là một trong những đô thị có nguồn gốc quân sự cổ xưa của vùng. Được thành lập năm 1647 như một pháo đài trên tuyến phòng thủ đông nam của nhà nước Nga (zasechnaya cherta), Insar ra đời để canh giữ vùng biên chống các cuộc tập kích từ thảo nguyên. Qua thời gian, tiền đồn quân sự dần trở thành đô thị tỉnh lẻ; đến năm 1708 nó được nhắc đến như một thị trấn và trải qua nhiều thay đổi hành chính. Điều thú vị là Insar vẫn lưu giữ được bố cục đường phố lịch sử của thế kỷ 17–18, cùng những dãy phố buôn (torgovye ryady) cổ và tu viện nữ Svyato-Olginsky, tạo nên không khí trầm mặc của một thị trấn Nga xưa. Vùng đất này còn gắn với những tên tuổi văn hoá như nhà thơ N.P. Ogaryov, N.M. Satin và nhà Cách mạng Tháng Chạp A.A. Tuchkov. Với du khách ưa khám phá những góc ít người biết, Insar mang đến trải nghiệm về một đô thị pháo đài cổ, nơi lịch sử biên ải và đời sống tỉnh lẻ yên bình đan xen.",
    [
        "Thị trấn cực nam Mordovia, lập năm 1647 làm pháo đài trên tuyến phòng thủ đông nam.",
        "Giữ bố cục phố cổ thế kỷ 17–18, dãy phố buôn xưa và tu viện Svyato-Olginsky.",
        "Gắn với các tên tuổi Ogaryov, Satin và nhà Cách mạng Tháng Chạp Tuchkov.",
    ],
    p("Tham quan ngoài trời tự do; cơ sở địa phương theo giờ hành chính.",
      "Dạo thị trấn miễn phí.",
      "1,5–2 giờ.",
      "Mùa hè khi thời tiết thuận lợi.",
      "Ở phía nam, xa Saransk; nên đi ô tô; dịch vụ du lịch tối giản, chuẩn bị trước."),
    [
        {"title": "Wikipedia (RU) — Инсар (город)", "url": "https://ru.wikipedia.org/wiki/Инсар_(город)"},
        {"title": "Wikipedia (EN) — Insar", "url": "https://en.wikipedia.org/wiki/Insar"},
    ],
    ["town", "fortress-origin", "history", "oldtown", "provincial"],
    maps_text("Инсар", "Мордовия",
              "Insar", "Mordovia", 53.867741, 44.371407),
))


def main():
    path = os.path.join(REGIONS, f"{REGION}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    existing_slugs = {pl.get("slug") for pl in data}
    existing_ids = {pl.get("id") for pl in data}

    added, skipped = [], []
    for r in RECORDS:
        if r["slug"] in existing_slugs or r["id"] in existing_ids:
            skipped.append(r["slug"])
            continue
        data.append(r)
        existing_slugs.add(r["slug"])
        existing_ids.add(r["id"])
        added.append(r["slug"])

    if added:
        bak = f"{path}.bak_add_{TS}"
        shutil.copyfile(path, bak)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Backup: {os.path.basename(bak)}")

    print(f"REGION={REGION}  ADDED={len(added)}  SKIPPED(dup)={len(skipped)}  TOTAL_NOW={len(data)}")
    if added:
        print("  + " + "\n  + ".join(added))
    if skipped:
        print("  (skip dup): " + ", ".join(skipped))


if __name__ == "__main__":
    main()
