# -*- coding: utf-8 -*-
"""_add_places_amur_20260728.py — VÙNG: Tỉnh Amur (Амурская область)
(lần chạy tự động 2026-07-28).

Bối cảnh: amur.json hiện có 6 địa điểm. Bổ sung 25 địa điểm THẬT SỰ nổi tiếng/đặc
sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 31 (≥30).

Phân bố loại hình (25 bản ghi mới):
- museum (4): Амурский краеведческий музей им. Новикова-Даурского, Палеонтологический
  музей АмурНЦ (khủng long), Музей истории БАМа (Тында), Свободненский краеведческий музей.
- church (3): Кафедральный собор Благовещения, Свято-Никольский храм (Свободный),
  Кафедральный собор Троицы Живоначальной (Тында).
- theatre (2): Амурский областной театр драмы, Амурская областная филармония.
- park_garden (5): Городской парк (Благовещенск), Первомайский парк, Зейский заповедник,
  Зейское водохранилище, Муравьёвский парк (журавли/аисты).
- monument (3): Памятник Муравьёву-Амурскому, Беседка-ротонда (набережная), Памятник «Челнок».
- bridge (1): Международный мост Благовещенск–Хэйхэ.
- square_street (1): Площадь Победы (Благовещенск).
- other (6): ОКЦ, Пожарная каланча (историч. здание), Зейская ГЭС, Бурейская ГЭС,
  Нижне-Бурейская ГЭС, вокзал Тында (столица БАМа).

TOẠ ĐỘ — xác minh chéo (Yandex Maps schema.org geo / ru.wikipedia geohack / en.wikipedia /
sobory.ru / OpenStreetMap / gem.wiki / railwayz.info, 2026-07-28). Phạm vi tỉnh Amur:
lat ~49–57, lon ~119,5–134,5; tất cả toạ độ nằm trong phạm vi, KHÔNG đảo lat/lon:
  Краеведческий музей 50.258992,127.524630 (Ленина 165); Кафедральный собор 50.261594,
  127.513907 (sobory); Театр драмы 50.259495,127.514194 (Ленина 146); Городской парк
  50.258254,127.512689; Палеонтологический музей 50.260643,127.517827 (Рёлочный пер. 4,
  org Яндекс); Филармония 50.258563,127.531006 (Пионерская 1); Площадь Победы 50.257572,
  127.520966; ОКЦ 50.255466,127.544308 (Ленина 100, org Яндекс); Памятник Муравьёву-
  Амурскому 50.256111,127.526667 (ru.wiki 50°15′22″N 127°31′36″E); мост Благовещенск–Хэйхэ
  50.201297,127.597964 (OSM, Каникурган); Зейская ГЭС 53.769170,127.306390 (en.wiki);
  Зейский заповедник 53.962780,127.372500; Зейское водохранилище 54.416700,127.750000
  (ru.wiki 54°25′N 127°45′E); Музей истории БАМа 55.146600,124.730843 (org Яндекс);
  вокзал Тында 55.139271,124.739072 (railwayz); Бурейская ГЭС 50.269170,130.313330
  (en.wiki); Нижне-Бурейская ГЭС 49.789100,129.979200 (gem.wiki, Новобурейский);
  Муравьёвский парк 49.839722,127.726944 (ru.wiki 49°50′23″N 127°43′37″E); Свято-
  Никольский храм Свободный 51.388677,128.120861 (sobory); Беседка-ротонда 50.256285,
  127.518158 (org Яндекс); Первомайский парк 50.247841,127.569658 (Краснофлотская 2);
  Памятник «Челнок» 50.262703,127.535098 (org Яндекс, 50 лет Октября 15); Собор Троицы
  Тында 55.149021,124.735363 (Красная Пресня 20); Пожарная каланча 50.260858,127.555442
  (Амурская 72); Свободненский музей 51.378998,128.134268 (Зейская 43, Свободный).

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_amur_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "amur"
REGION_NAME_VI = "Tỉnh Amur"
FD = "Vùng Viễn Đông"


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


RECORDS = []

# 1) Амурский областной краеведческий музей им. Г. С. Новикова-Даурского -----------
RECORDS.append(rec(
    "amur-regional-museum",
    "Bảo tàng địa phương tỉnh Amur mang tên G. S. Novikov-Daursky",
    "Амурский областной краеведческий музей имени Г. С. Новикова-Даурского",
    "Amur Regional Museum of Local Lore",
    ["museum"],
    50.258992, 127.524630,
    "Ул. Ленина, 165, thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Một trong những bảo tàng lâu đời và lớn nhất vùng Viễn Đông Nga, thành lập từ năm 1891. Bộ sưu tập hơn 130.000 hiện vật kể lại toàn cảnh thiên nhiên, khảo cổ và lịch sử khai phá vùng Amur, đặt trong toà nhà thương mại cổ kính của hãng «Kunst và Albers».",
    "Bảo tàng địa phương tỉnh Amur ở Blagoveshchensk là kho lưu giữ ký ức của cả một vùng đất biên viễn. Ra đời năm 1891, đây là một trong những bảo tàng cổ nhất và giàu hiện vật nhất của vùng Viễn Đông, với bộ sưu tập vượt 130.000 đơn vị. Bảo tàng toạ lạc trong toà nhà gạch đỏ tráng lệ từng là cửa hàng của hãng thương mại Đức «Kunst và Albers» đầu thế kỷ 20 — bản thân công trình đã là một di tích kiến trúc. Các gian trưng bày dẫn khách đi từ thế giới tự nhiên của rừng taiga và sông Amur, qua văn hoá của các dân tộc bản địa Evenk và người Cossack khai hoang, tới thời kỳ thành lập Blagoveshchensk và những biến động thế kỷ 20. Bảo tàng mang tên nhà nghiên cứu địa phương G. S. Novikov-Daursky, người có công lớn với khoa học vùng Amur. Với du khách Việt, đây là điểm khởi đầu lý tưởng để hiểu vì sao Amur được ví như «cửa ngõ nước Nga bên bờ Thái Bình Dương».",
    [
        "Một trong những bảo tàng lâu đời nhất Viễn Đông (thành lập 1891), hơn 130.000 hiện vật.",
        "Đặt trong toà nhà cổ của hãng thương mại «Kunst và Albers» — di tích kiến trúc đầu thế kỷ 20.",
        "Trưng bày trọn vẹn thiên nhiên, dân tộc bản địa và lịch sử khai phá vùng Amur.",
    ],
    {
        "hours_vi": "Thường mở cửa thứ Ba–Chủ nhật, nghỉ thứ Hai; nên kiểm tra lịch theo mùa.",
        "ticket_vi": "Vé vào cửa giá bình dân; có thêm phí cho tour hướng dẫn và triển lãm chuyên đề.",
        "duration_vi": "Khoảng 1,5–2 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà), tiện ghé cùng buổi dạo bờ kè.",
        "tips_vi": "Nằm ngay trung tâm trên đường Lenin, đi bộ được tới nhà thờ chính toà, nhà hát kịch và bờ kè.",
    },
    [
        {"title": "Wikipedia (RU) — Амурский областной краеведческий музей", "url": "https://ru.wikipedia.org/wiki/Амурский_областной_краеведческий_музей_имени_Г._С._Новикова-Даурского"},
        {"title": "Yandex Maps — Амурский краеведческий музей", "url": "https://yandex.ru/maps/77/blagoveshchensk/"},
    ],
    ["museum", "local-history", "blagoveshchensk", "kunst-albers", "far-east"],
    maps_text("Амурский краеведческий музей", "Благовещенск", "Amur Regional Museum of Local Lore", "Blagoveshchensk", 50.258992, 127.524630),
))

# 2) Кафедральный собор Благовещения Пресвятой Богородицы --------------------------
RECORDS.append(rec(
    "annunciation-cathedral-blagoveshchensk",
    "Nhà thờ chính toà Truyền Tin (Blagoveshchensky sobor)",
    "Кафедральный собор Благовещения Пресвятой Богородицы",
    "Cathedral of the Annunciation (Blagoveshchensk)",
    ["church"],
    50.261594, 127.513907,
    "Ул. Рёлочный переулок, khu trung tâm gần bờ sông Amur, thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Nhà thờ chính toà Chính Thống giáo của Blagoveshchensk, mang tên lễ Truyền Tin — sự kiện chính đã đặt tên cho cả thành phố (Blagoveshchensk nghĩa là «thành phố Truyền Tin»). Ngôi thánh đường năm vòm trắng-xanh là trung tâm tôn giáo của toàn tỉnh Amur.",
    "Chính cái tên Blagoveshchensk bắt nguồn từ lễ Truyền Tin (Blagoveshchenie) của Chính Thống giáo, nên nhà thờ chính toà Truyền Tin có ý nghĩa biểu tượng đặc biệt với thành phố. Ngôi thánh đường hiện nay được xây dựng lại và trở thành trung tâm của giáo phận Blagoveshchensk, nơi đặt ngai toà của giám mục. Với những mái vòm trắng viền xanh vươn cao gần bờ sông Amur, nhà thờ là một trong những công trình dễ nhận biết nhất của thành phố. Bên trong lưu giữ nhiều thánh tượng được tôn kính, trong đó gắn với truyền thống về biểu tượng Đức Mẹ Albazin — thánh tượng bảo trợ của vùng Amur, gắn liền với lịch sử pháo đài Albazin trên biên giới. Nhà thờ vừa là nơi hành lễ của cộng đồng Chính Thống giáo địa phương, vừa là điểm dừng chân để du khách cảm nhận không gian tâm linh và kiến trúc tôn giáo Nga nơi vùng đất giáp Trung Quốc.",
    [
        "Nhà thờ chính toà, trung tâm tôn giáo của toàn giáo phận và tỉnh Amur.",
        "Tên thành phố Blagoveshchensk chính là lấy từ lễ Truyền Tin mà nhà thờ tôn vinh.",
        "Gắn với truyền thống thánh tượng Đức Mẹ Albazin — biểu tượng bảo trợ vùng Amur.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ, thường từ sáng sớm tới chiều tối.",
        "ticket_vi": "Miễn phí (là nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Buổi sáng hoặc các dịp lễ lớn của Chính Thống giáo.",
        "tips_vi": "Nữ nên trùm khăn, ăn mặc kín đáo; giữ yên lặng và xin phép trước khi chụp ảnh bên trong.",
    },
    [
        {"title": "Sobory.ru — Кафедральный собор Благовещения", "url": "https://sobory.ru/article/?object=09344"},
        {"title": "Wikipedia (RU) — Благовещенск (достопримечательности)", "url": "https://ru.wikipedia.org/wiki/Благовещенск"},
    ],
    ["church", "cathedral", "orthodox", "blagoveshchensk", "albazin-icon"],
    maps_text("Кафедральный собор Благовещения", "Благовещенск", "Cathedral of the Annunciation", "Blagoveshchensk", 50.261594, 127.513907),
))

# 3) Амурский областной театр драмы -----------------------------------------------
RECORDS.append(rec(
    "amur-drama-theatre",
    "Nhà hát kịch tỉnh Amur (Amurskiy teatr dramy)",
    "Амурский областной театр драмы",
    "Amur Regional Drama Theatre",
    ["theatre"],
    50.259495, 127.514194,
    "Ул. Ленина, 146, thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Nhà hát kịch lâu đời nhất vùng Viễn Đông Nga, với lịch sử diễn xuất chuyên nghiệp từ cuối thế kỷ 19. Sân khấu là trung tâm đời sống văn hoá của Blagoveshchensk, dựng cả kịch kinh điển Nga lẫn tác phẩm đương đại.",
    "Nhà hát kịch tỉnh Amur là một trong những sân khấu kịch nói lâu đời nhất của toàn vùng Viễn Đông, với truyền thống biểu diễn chuyên nghiệp bắt rễ từ cuối thế kỷ 19 — khi Blagoveshchensk còn là thương cảng sầm uất bên sông Amur. Trải qua hơn một thế kỷ, nhà hát trở thành trái tim đời sống sân khấu của thành phố: nơi đây dàn dựng các vở kinh điển của Chekhov, Ostrovsky, Gogol cùng nhiều tác phẩm hiện đại và kịch dành cho thiếu nhi. Toà nhà nằm ngay trên trục phố Lenin nhộn nhịp, gần bảo tàng địa phương và bờ kè, tạo thành một cụm văn hoá trung tâm rất tiện dạo bộ. Với những khán giả yêu nghệ thuật, một buổi tối xem kịch tại đây là cách thú vị để hoà vào nhịp sinh hoạt của người dân Amur; ngay cả khi không rành tiếng Nga, du khách vẫn có thể cảm nhận không khí trang trọng của một nhà hát tỉnh lỵ vùng biên.",
    [
        "Một trong những nhà hát kịch lâu đời nhất vùng Viễn Đông, truyền thống từ cuối thế kỷ 19.",
        "Trung tâm đời sống sân khấu Blagoveshchensk với kịch kinh điển Nga và tác phẩm đương đại.",
        "Vị trí trung tâm trên phố Lenin, gần bảo tàng, nhà thờ và bờ kè.",
    ],
    {
        "hours_vi": "Có suất diễn theo lịch mùa, thường vào buổi tối và cuối tuần; phòng vé mở ban ngày.",
        "ticket_vi": "Vé giá phải chăng, thay đổi theo vở diễn và hạng ghế.",
        "duration_vi": "Một buổi diễn khoảng 2–3 giờ.",
        "best_time_vi": "Mùa diễn từ thu đến xuân; xem lịch trên trang chính thức của nhà hát.",
        "tips_vi": "Đặt vé trước cho các vở nổi tiếng; đến sớm để gửi áo khoác mùa đông ở quầy garderob.",
    },
    [
        {"title": "Wikipedia (RU) — Амурский областной театр драмы", "url": "https://ru.wikipedia.org/wiki/Амурский_областной_театр_драмы"},
        {"title": "Yandex Maps — Амурский областной театр драмы", "url": "https://yandex.ru/maps/77/blagoveshchensk/"},
    ],
    ["theatre", "drama", "blagoveshchensk", "culture", "performing-arts"],
    maps_text("Амурский областной театр драмы", "Благовещенск", "Amur Regional Drama Theatre", "Blagoveshchensk", 50.259495, 127.514194),
))

# 4) Городской парк культуры и отдыха (Благовещенск) -------------------------------
RECORDS.append(rec(
    "blagoveshchensk-city-park",
    "Công viên văn hoá thành phố Blagoveshchensk (Gorodskoy park)",
    "Городской парк культуры и отдыха",
    "City Park of Culture and Leisure (Blagoveshchensk)",
    ["park_garden"],
    50.258254, 127.512689,
    "Trung tâm thành phố, gần bờ sông Amur và đường Lenin, thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Công viên trung tâm lâu đời của Blagoveshchensk, kề bên bờ kè sông Amur. Nơi người dân dạo chơi, đưa trẻ đi chơi trò chơi và tận hưởng không gian xanh giữa lòng thành phố, đặc biệt nhộn nhịp vào mùa hè.",
    "Công viên văn hoá và nghỉ ngơi thành phố là mảng xanh trung tâm quen thuộc của người Blagoveshchensk, nằm ngay sát bờ kè sông Amur và trục phố Lenin. Đây là kiểu công viên thành phố điển hình của Nga: những hàng cây rợp bóng, lối đi dạo, khu vui chơi thiếu nhi với đu quay và các trò chơi, sân khấu ngoài trời và những quán giải khát nhỏ. Vào mùa hè, công viên trở nên sôi động với tiếng cười trẻ nhỏ, các gia đình đi dạo và những buổi hoà nhạc, sự kiện cộng đồng; mùa đông, không gian phủ tuyết mang vẻ tĩnh lặng khác hẳn. Nhờ vị trí liền kề bờ kè và trung tâm, công viên là điểm nghỉ chân lý tưởng khi kết hợp tham quan các danh thắng lân cận như Khải Hoàn Môn, bờ kè và các tượng đài. Với du khách Việt, đây là nơi dễ chịu để quan sát nhịp sống thường nhật của một thành phố biên giới Nga.",
    [
        "Công viên trung tâm lâu đời, kề bờ kè sông Amur.",
        "Khu vui chơi thiếu nhi, sân khấu ngoài trời và không gian xanh giữa thành phố.",
        "Vị trí đắc địa để kết hợp dạo bờ kè và tham quan trung tâm Blagoveshchensk.",
    ],
    {
        "hours_vi": "Mở cửa tự do; các trò chơi và quầy dịch vụ hoạt động chủ yếu mùa ấm và ban ngày.",
        "ticket_vi": "Vào cửa miễn phí; trả tiền riêng cho từng trò chơi và dịch vụ.",
        "duration_vi": "Khoảng 30–60 phút, lâu hơn nếu đi cùng trẻ em.",
        "best_time_vi": "Chiều mát mùa hè; dịp lễ hội thành phố có nhiều hoạt động.",
        "tips_vi": "Kết hợp cùng buổi dạo bờ kè; có nhiều ghế ngồi và quán ăn nhẹ quanh khu vực.",
    },
    [
        {"title": "Wikipedia (RU) — Благовещенск", "url": "https://ru.wikipedia.org/wiki/Благовещенск"},
        {"title": "Yandex Maps — Городской парк, Благовещенск", "url": "https://yandex.ru/maps/77/blagoveshchensk/"},
    ],
    ["park", "city-park", "blagoveshchensk", "family", "recreation"],
    maps_text("Городской парк культуры и отдыха", "Благовещенск", "City Park of Culture and Leisure", "Blagoveshchensk", 50.258254, 127.512689),
))

# 5) Палеонтологический музей АмурНЦ ДВО РАН (динозавры) ---------------------------
RECORDS.append(rec(
    "paleontology-museum-amurnc",
    "Bảo tàng Cổ sinh vật học Amur (khủng long) — Paleontologicheskiy muzey",
    "Палеонтологический музей АмурНЦ ДВО РАН",
    "Amur Palaeontological Museum",
    ["museum"],
    50.260643, 127.517827,
    "Ул. Рёлочный переулок, 4, thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Bảo tàng lưu giữ bộ sưu tập khủng long lớn bậc nhất nước Nga, với hoá thạch các loài đặc hữu được phát hiện ngay tại Amur: Amurosaurus, Olorotitan, Kerberosaurus. Tỉnh Amur nổi tiếng là một trong những «nghĩa địa khủng long» giàu có nhất châu Á.",
    "Ít ai ngờ vùng Amur bên bờ sông giáp Trung Quốc lại là một trong những xứ sở khủng long phong phú nhất châu Á. Cách đây khoảng 66 triệu năm, nơi đây từng là đầm lầy nhiệt đới nơi sinh sống của những đàn khủng long mỏ vịt khổng lồ; khi thảm hoạ tuyệt chủng ập đến, xương của chúng bị vùi lấp và biến thành các «nghĩa địa khủng long» nổi tiếng ở rìa Blagoveshchensk và ở Kundur. Bảo tàng Cổ sinh vật học của Trung tâm Khoa học Amur trưng bày thành quả của hàng chục năm khai quật: bộ sưu tập được coi là lớn nhất nước Nga về khủng long, gồm hoá thạch và bộ xương phục dựng của các loài lần đầu được mô tả từ chính vùng đất này — Amurosaurus riabinini, Olorotitan arharensis và Kerberosaurus manakini. Không gian trưng bày kể câu chuyện về thế giới cuối kỷ Phấn Trắng, cách các nhà khoa học đọc dấu vết trong đá và tái dựng diện mạo những sinh vật đã mất. Đây là điểm đến hấp dẫn cho cả người lớn lẫn trẻ em yêu thích cổ sinh vật.",
    [
        "Bộ sưu tập khủng long thuộc hàng lớn nhất nước Nga.",
        "Hoá thạch các loài đặc hữu Amur: Amurosaurus, Olorotitan, Kerberosaurus.",
        "Kể câu chuyện «nghĩa địa khủng long» nổi tiếng của vùng Amur (Blagoveshchensk và Kundur).",
    ],
    {
        "hours_vi": "Mở cửa theo giờ hành chính các ngày trong tuần; nên gọi/xem lịch trước vì là bảo tàng khoa học.",
        "ticket_vi": "Vé vào cửa giá bình dân; ưu tiên đi theo tour hướng dẫn để hiểu rõ hiện vật.",
        "duration_vi": "Khoảng 45–90 phút.",
        "best_time_vi": "Quanh năm; rất phù hợp cho gia đình có trẻ em.",
        "tips_vi": "Gần trung tâm và nhà thờ chính toà; kết hợp với Bảo tàng địa phương gần đó để hiểu trọn lịch sử vùng Amur.",
    },
    [
        {"title": "Yandex Maps — Палеонтологический музей (org)", "url": "https://yandex.ru/maps/org/paleontologicheskiy_muzey/1198015675/"},
        {"title": "Wikipedia (EN) — Amurosaurus / Olorotitan (Amur Oblast dinosaurs)", "url": "https://en.wikipedia.org/wiki/Amurosaurus"},
    ],
    ["museum", "dinosaurs", "paleontology", "blagoveshchensk", "amurosaurus", "science"],
    maps_org("https://yandex.ru/maps/org/paleontologicheskiy_muzey/1198015675/", "Amur Palaeontological Museum", "Blagoveshchensk"),
))

# 6) Амурская областная филармония ------------------------------------------------
RECORDS.append(rec(
    "amur-philharmonic",
    "Nhạc viện – Phòng hoà nhạc tỉnh Amur (Amurskaya filarmoniya)",
    "Амурская областная филармония",
    "Amur Regional Philharmonic",
    ["theatre"],
    50.258563, 127.531006,
    "Ул. Пионерская, 1, thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Trung tâm âm nhạc hàn lâm của tỉnh Amur, nơi tổ chức các buổi hoà nhạc giao hưởng, thính phòng, dân ca và biểu diễn của nghệ sĩ khách mời. Một điểm đến văn hoá quan trọng ở trung tâm Blagoveshchensk.",
    "Phòng hoà nhạc (philharmonia) tỉnh Amur là nơi hội tụ đời sống âm nhạc hàn lâm của thành phố Blagoveshchensk. Trên sân khấu của nhạc viện diễn ra các chương trình đa dạng: hoà nhạc giao hưởng và thính phòng, độc tấu piano, biểu diễn nhạc cụ dân tộc Nga, các đêm nhạc jazz, dân ca và những buổi giao lưu với nghệ sĩ từ khắp nước Nga. Đây cũng là nơi các tập thể nghệ thuật địa phương biểu diễn thường xuyên, góp phần nuôi dưỡng đời sống tinh thần của người dân vùng biên. Toà nhà nằm ở trung tâm, thuận tiện kết hợp với các điểm tham quan khác của Blagoveshchensk. Với du khách yêu âm nhạc, một buổi tối tại philharmonia là dịp thưởng thức nghệ thuật biểu diễn Nga trong không gian ấm cúng của một thành phố tỉnh lỵ, đồng thời cảm nhận sự giao thoa giữa truyền thống hàn lâm châu Âu và bản sắc vùng Viễn Đông.",
    [
        "Trung tâm âm nhạc hàn lâm của tỉnh Amur.",
        "Chương trình phong phú: giao hưởng, thính phòng, dân ca, jazz và nghệ sĩ khách mời.",
        "Vị trí trung tâm Blagoveshchensk, dễ kết hợp tham quan.",
    ],
    {
        "hours_vi": "Có chương trình theo lịch mùa, chủ yếu buổi tối; phòng vé mở ban ngày.",
        "ticket_vi": "Vé giá phải chăng, thay đổi theo chương trình.",
        "duration_vi": "Một buổi hoà nhạc khoảng 1,5–2 giờ.",
        "best_time_vi": "Mùa biểu diễn thu–xuân; kiểm tra lịch trước khi tới.",
        "tips_vi": "Đặt vé trước cho các đêm nhạc lớn; trang phục lịch sự được khuyến khích.",
    },
    [
        {"title": "Culture.ru — Амурская областная филармония", "url": "https://www.culture.ru/institutes/25528"},
        {"title": "Yandex Maps — Амурская областная филармония", "url": "https://yandex.ru/maps/77/blagoveshchensk/"},
    ],
    ["philharmonic", "music", "concert", "blagoveshchensk", "culture"],
    maps_text("Амурская областная филармония", "Благовещенск", "Amur Regional Philharmonic", "Blagoveshchensk", 50.258563, 127.531006),
))

# 7) Площадь Победы (Благовещенск) -------------------------------------------------
RECORDS.append(rec(
    "victory-square-blagoveshchensk",
    "Quảng trường Chiến thắng (Ploshchad Pobedy)",
    "Площадь Победы",
    "Victory Square (Blagoveshchensk)",
    ["square_street", "monument"],
    50.257572, 127.520966,
    "Gần bờ kè sông Amur, trung tâm thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Quảng trường tưởng niệm dành cho chiến thắng trong Chiến tranh Vệ quốc Vĩ đại, với Ngọn lửa Vĩnh cửu và các đài tưởng niệm. Nơi diễn ra lễ đặt hoa, duyệt binh ngày 9 tháng 5 và là không gian trang nghiêm sát bờ kè.",
    "Quảng trường Chiến thắng là không gian tưởng niệm trang trọng của Blagoveshchensk, dành để tri ân những người con của vùng Amur đã ngã xuống trong Chiến tranh Vệ quốc Vĩ đại (1941–1945). Trung tâm quảng trường là Ngọn lửa Vĩnh cửu cháy không ngừng, cùng các đài tưởng niệm và bảng khắc tên. Vào ngày 9 tháng 5 — Ngày Chiến thắng, một trong những ngày lễ thiêng liêng nhất của người Nga — nơi đây trở thành tâm điểm với lễ đặt hoa, đoàn «Trung đoàn Bất tử» và các nghi thức cộng đồng. Nằm ngay gần bờ kè sông Amur và các danh thắng trung tâm, quảng trường vừa là chốn tưởng niệm, vừa là không gian công cộng để người dân dạo bộ, gặp gỡ. Với du khách, đây là nơi cảm nhận rõ cách người Nga gìn giữ ký ức lịch sử và lòng biết ơn với thế hệ đi trước, đặc biệt xúc động vào những dịp lễ lớn.",
    [
        "Ngọn lửa Vĩnh cửu và đài tưởng niệm Chiến tranh Vệ quốc Vĩ đại.",
        "Tâm điểm các nghi lễ Ngày Chiến thắng 9/5 tại Blagoveshchensk.",
        "Vị trí sát bờ kè sông Amur, dễ kết hợp dạo bộ trung tâm.",
    ],
    {
        "hours_vi": "Không gian mở, tham quan tự do 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–30 phút.",
        "best_time_vi": "Dịp 9/5 để chứng kiến nghi lễ; buổi tối quảng trường lên đèn đẹp.",
        "tips_vi": "Giữ thái độ trang nghiêm gần Ngọn lửa Vĩnh cửu; kết hợp tham quan bờ kè và Khải Hoàn Môn gần đó.",
    },
    [
        {"title": "Wikipedia (RU) — Благовещенск", "url": "https://ru.wikipedia.org/wiki/Благовещенск"},
        {"title": "Yandex Maps — Площадь Победы, Благовещенск", "url": "https://yandex.ru/maps/77/blagoveshchensk/"},
    ],
    ["square", "memorial", "victory", "eternal-flame", "blagoveshchensk"],
    maps_text("Площадь Победы", "Благовещенск", "Victory Square", "Blagoveshchensk", 50.257572, 127.520966),
))

# 8) Общественно-культурный центр (ОКЦ), Благовещенск ------------------------------
RECORDS.append(rec(
    "okc-blagoveshchensk",
    "Trung tâm Văn hoá – Cộng đồng Blagoveshchensk (OKTs)",
    "Общественно-культурный центр",
    "Public and Cultural Centre (Blagoveshchensk)",
    ["other"],
    50.255466, 127.544308,
    "Ул. Ленина, 100, thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Tổ hợp văn hoá – sự kiện hiện đại của Blagoveshchensk, nơi tổ chức hội nghị, triển lãm, hoà nhạc, liên hoan và các sự kiện lớn của tỉnh Amur. Một trong những công trình công cộng tiêu biểu của thành phố.",
    "Trung tâm Văn hoá – Cộng đồng (thường gọi tắt là OKTs) là một trong những tổ hợp sự kiện hiện đại và đa năng nhất của Blagoveshchensk. Đây là nơi diễn ra hầu hết các sự kiện quy mô lớn của thành phố và tỉnh Amur: hội nghị và diễn đàn, triển lãm, hoà nhạc, liên hoan nghệ thuật, lễ trao giải và các chương trình biểu diễn khách mời. Với hệ thống khán phòng, sân khấu và không gian triển lãm hiện đại, OKTs đóng vai trò như «phòng khách văn hoá» của thành phố, đặc biệt sôi động trong các dịp lễ hội và sự kiện hợp tác Nga – Trung nhờ vị trí biên giới đặc thù của Blagoveshchensk. Nằm trên trục phố Lenin trung tâm, trung tâm này dễ kết hợp với hành trình khám phá thành phố. Với du khách, việc theo dõi lịch sự kiện tại OKTs có thể giúp bắt gặp một buổi hoà nhạc, triển lãm hay lễ hội đặc sắc trong thời gian lưu lại Blagoveshchensk.",
    [
        "Tổ hợp văn hoá – sự kiện hiện đại, đa năng bậc nhất Blagoveshchensk.",
        "Nơi tổ chức hội nghị, triển lãm, hoà nhạc và các sự kiện lớn của tỉnh Amur.",
        "Thường xuyên có sự kiện giao lưu văn hoá Nga – Trung nhờ vị trí biên giới.",
    ],
    {
        "hours_vi": "Mở cửa theo lịch sự kiện; phần lớn hoạt động diễn ra buổi tối và cuối tuần.",
        "ticket_vi": "Tuỳ sự kiện: nhiều chương trình miễn phí, một số bán vé.",
        "duration_vi": "Tuỳ chương trình, thường 1–3 giờ.",
        "best_time_vi": "Khi có sự kiện; xem lịch trước khi tới.",
        "tips_vi": "Kiểm tra lịch sự kiện để chọn đúng chương trình; nằm ngay trung tâm, tiện di chuyển.",
    },
    [
        {"title": "Yandex Maps — Общественно-культурный центр (org)", "url": "https://yandex.ru/maps/org/obshchestvenno_kulturny_tsentr/2420220214/"},
        {"title": "Wikipedia (RU) — Благовещенск", "url": "https://ru.wikipedia.org/wiki/Благовещенск"},
    ],
    ["cultural-center", "events", "blagoveshchensk", "modern", "concert-hall"],
    maps_org("https://yandex.ru/maps/org/obshchestvenno_kulturny_tsentr/2420220214/", "Public and Cultural Centre", "Blagoveshchensk"),
))

# 9) Памятник Н. Н. Муравьёву-Амурскому (Благовещенск) ----------------------------
RECORDS.append(rec(
    "muravyov-amursky-monument",
    "Tượng đài bá tước Muravyov-Amursky",
    "Памятник Н. Н. Муравьёву-Амурскому",
    "Monument to Nikolay Muravyov-Amursky",
    ["monument"],
    50.256111, 127.526667,
    "Trên bờ kè sông Amur (ул. Краснофлотская), thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Tượng đài tôn vinh bá tước Nikolay Muravyov-Amursky — vị Toàn quyền Đông Siberia đã sáp nhập tả ngạn sông Amur vào nước Nga và khai sinh Blagoveshchensk. Bức tượng đồng cao 3 mét đứng trên bờ kè, khánh thành năm 1993.",
    "Bá tước Nikolay Nikolayevich Muravyov-Amursky là nhân vật lịch sử gắn liền với sự ra đời của cả vùng Amur: chính ông, với tư cách Toàn quyền Đông Siberia, đã đưa vùng tả ngạn sông Amur trở về nước Nga qua Hiệp ước Aigun năm 1858 và đặt nền móng cho thành phố Blagoveshchensk. Tượng đài của ông trên bờ kè Blagoveshchensk được khánh thành ngày 17 tháng 7 năm 1993, đúng dịp thành phố tròn 135 tuổi, do nhà điêu khắc địa phương Nikolay Karnabeda thực hiện và đúc đồng tại Belogorsk. Bức tượng cao ba mét khắc hoạ vị bá tước trong tư thế uy nghi, tay trái cầm cuộn giấy tượng trưng cho việc xác lập chủ quyền vùng tả ngạn Amur. Năm 2014, trong đợt cải tạo bờ kè, tượng được dịch về phía nam khoảng 40 mét để hài hoà hơn với cảnh quan mới. Đứng ngay bên dòng Amur nhìn sang Trung Quốc, tượng đài là một trong những biểu tượng lịch sử được chụp ảnh nhiều nhất của thành phố.",
    [
        "Tôn vinh người sáp nhập vùng Amur vào Nga (Hiệp ước Aigun 1858) và khai sinh Blagoveshchensk.",
        "Tượng đồng cao 3 m, khánh thành năm 1993 nhân 135 năm thành phố.",
        "Vị trí biểu tượng trên bờ kè, nhìn thẳng sang thành phố Hắc Hà của Trung Quốc.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–20 phút.",
        "best_time_vi": "Chiều tối mùa hè khi bờ kè lên đèn; kết hợp ngắm hoàng hôn trên sông Amur.",
        "tips_vi": "Mang giấy tờ tuỳ thân (khu vực biên giới); tránh chụp lính biên phòng và tàu tuần tra.",
    },
    [
        {"title": "Wikipedia (RU) — Памятник Муравьёву-Амурскому (Благовещенск)", "url": "https://ru.wikipedia.org/wiki/Памятник_Муравьёву-Амурскому_(Благовещенск)"},
        {"title": "Yandex Maps — Памятник Муравьёву-Амурскому", "url": "https://yandex.ru/maps/77/blagoveshchensk/"},
    ],
    ["monument", "muravyov-amursky", "history", "embankment", "blagoveshchensk"],
    maps_text("Памятник Муравьёву-Амурскому", "Благовещенск", "Monument to Muravyov-Amursky", "Blagoveshchensk", 50.256111, 127.526667),
))

# 10) Международный мост Благовещенск–Хэйхэ ---------------------------------------
RECORDS.append(rec(
    "blagoveshchensk-heihe-bridge",
    "Cầu quốc tế Blagoveshchensk – Hắc Hà (qua sông Amur)",
    "Международный автомобильный мост Благовещенск — Хэйхэ",
    "Blagoveshchensk–Heihe International Bridge",
    ["bridge"],
    50.201297, 127.597964,
    "Bắc qua sông Amur ở khu vực Kanikurgan, phía nam Blagoveshchensk, nối sang Hắc Hà (Trung Quốc), tỉnh Amur, Nga.",
    "Cây cầu đường bộ quốc tế đầu tiên nối Nga và Trung Quốc qua sông Amur, khánh thành năm 2019 và thông xe năm 2022. Biểu tượng của hợp tác biên giới Nga – Trung, dài khoảng 1 km phần vượt sông.",
    "Cầu quốc tế Blagoveshchensk – Hắc Hà là cây cầu đường bộ đầu tiên bắc qua sông Amur nối trực tiếp nước Nga với Trung Quốc — một cột mốc lịch sử sau nhiều thập kỷ hai bờ chỉ qua lại bằng phà mùa hè và đường băng trên sông đóng băng mùa đông. Công trình hoàn thành phần xây lắp năm 2019 và chính thức thông xe cho vận tải hàng hoá, hành khách năm 2022. Cầu nằm ở khu vực Kanikurgan phía nam Blagoveshchensk, với nhịp chính vượt sông và hệ thống đường dẫn, cửa khẩu hải quan hiện đại hai bên. Đây không chỉ là hạ tầng giao thông mà còn là biểu tượng sống động của quan hệ láng giềng và giao thương Nga – Trung ở vùng Viễn Đông. Với du khách, cây cầu là điểm nhấn hiện đại thú vị bên cạnh khung cảnh cổ kính của bờ kè trung tâm; nhiều tour địa phương đưa khách tới ngắm và tìm hiểu vai trò của công trình trong tuyến vận tải xuyên biên giới.",
    [
        "Cầu đường bộ đầu tiên nối Nga và Trung Quốc qua sông Amur.",
        "Hoàn thành 2019, thông xe 2022 — biểu tượng hợp tác biên giới Nga – Trung.",
        "Nằm ở khu vực Kanikurgan phía nam Blagoveshchensk, có cửa khẩu hải quan hiện đại.",
    ],
    {
        "hours_vi": "Là công trình giao thông/cửa khẩu; ngắm cảnh từ xa tự do, qua cầu phải theo thủ tục biên giới.",
        "ticket_vi": "Miễn phí khi ngắm từ bờ; qua cầu (hàng hoá/hành khách) theo quy định hải quan.",
        "duration_vi": "Ngắm cảnh khoảng 20–30 phút.",
        "best_time_vi": "Ban ngày trời quang để nhìn rõ hai bờ; mùa hè thuận tiện di chuyển.",
        "tips_vi": "Đây là khu vực biên giới nhạy cảm — tuân thủ biển báo, không tự ý tiến sát cửa khẩu hay chụp lực lượng chức năng.",
    },
    [
        {"title": "OpenStreetMap — Blagoveshchensk–Heihe bridge", "url": "https://www.openstreetmap.org/way/1091190391"},
        {"title": "Wikipedia (EN) — Amur Bridge (Blagoveshchensk–Heihe)", "url": "https://en.wikipedia.org/wiki/Blagoveshchensk–Heihe_bridge"},
    ],
    ["bridge", "border", "russia-china", "amur-river", "blagoveshchensk", "modern"],
    maps_text("Международный мост Благовещенск Хэйхэ", "Благовещенск", "Blagoveshchensk Heihe International Bridge", "Blagoveshchensk", 50.201297, 127.597964),
))

# 11) Зейская ГЭС -----------------------------------------------------------------
RECORDS.append(rec(
    "zeya-dam",
    "Đập thuỷ điện Zeya (Zeyskaya GES)",
    "Зейская ГЭС",
    "Zeya Hydroelectric Dam",
    ["other"],
    53.769170, 127.306390,
    "Trên sông Zeya, sát thành phố Zeya, huyện Zeysky, tỉnh Amur, Nga.",
    "Nhà máy thuỷ điện lớn đầu tiên của vùng Viễn Đông, đập bê tông trọng lực cao 115,5 m chắn ngang sông Zeya. Công trình tạo nên hồ chứa Zeya khổng lồ và là biểu tượng công nghiệp – kỹ thuật của tỉnh Amur.",
    "Đập thuỷ điện Zeya là công trình năng lượng mang tính bước ngoặt của vùng Viễn Đông Nga — nhà máy thuỷ điện lớn đầu tiên của cả khu vực. Đập bê tông trọng lực cao 115,5 mét, dài gần 1.300 mét, chắn ngang sông Zeya tại nơi dòng sông cắt qua dãy núi Tukuringra, nơi được gọi là «Cổng Zeya». Khởi công năm 1965 và đưa vào vận hành từ năm 1975, nhà máy có công suất khoảng 1.330 MW, mỗi năm sản xuất gần 5 tỷ kWh điện, đồng thời giữ vai trò cực kỳ quan trọng trong việc điều tiết lũ cho hạ lưu sông Amur. Phía sau đập là hồ chứa Zeya mênh mông trải dài hàng trăm ki-lô-mét. Với du khách, khối bê tông đồ sộ giữa cảnh núi rừng taiga là một cảnh tượng hùng vĩ, đặc biệt khi các cửa xả tràn hoạt động; thị trấn Zeya bên cạnh cũng là cửa ngõ để khám phá khu bảo tồn thiên nhiên Zeya. Đây là điểm đến hấp dẫn cho những ai quan tâm tới kỳ quan kỹ thuật và cảnh quan thiên nhiên vùng Amur.",
    [
        "Nhà máy thuỷ điện lớn đầu tiên của vùng Viễn Đông (vận hành 1975).",
        "Đập bê tông trọng lực cao 115,5 m tại «Cổng Zeya», công suất ~1.330 MW.",
        "Giữ vai trò điều tiết lũ quan trọng cho hạ lưu sông Amur; tạo nên hồ chứa Zeya.",
    ],
    {
        "hours_vi": "Là công trình năng lượng; ngắm cảnh bên ngoài tự do, vào bên trong cần đăng ký tour có phép.",
        "ticket_vi": "Ngắm cảnh miễn phí; tham quan nội bộ (nếu có) theo chương trình của nhà máy.",
        "duration_vi": "Khoảng 30–60 phút cho phần ngắm cảnh.",
        "best_time_vi": "Cuối hè – đầu thu khi mực nước cao, có thể được chứng kiến xả tràn.",
        "tips_vi": "Tuân thủ khu vực cấm quanh công trình; kết hợp thăm thị trấn Zeya và khu bảo tồn Zeya.",
    },
    [
        {"title": "Wikipedia (EN) — Zeya Dam", "url": "https://en.wikipedia.org/wiki/Zeya_Dam"},
        {"title": "Global Energy Monitor — Zeya hydroelectric plant", "url": "https://www.gem.wiki/Zeya_hydroelectric_plant"},
    ],
    ["dam", "hydroelectric", "zeya-river", "engineering", "far-east"],
    maps_text("Зейская ГЭС", "Зея", "Zeya Hydroelectric Dam", "Zeya", 53.769170, 127.306390),
))

# 12) Зейский заповедник ----------------------------------------------------------
RECORDS.append(rec(
    "zeya-nature-reserve",
    "Khu bảo tồn thiên nhiên Zeya (Zeyskiy zapovednik)",
    "Зейский заповедник",
    "Zeya Nature Reserve",
    ["park_garden"],
    53.962780, 127.372500,
    "Trên vùng núi thượng nguồn sông Zeya, dãy Tukuringra, phía bắc thành phố Zeya, huyện Zeysky, tỉnh Amur, Nga.",
    "Khu bảo tồn thiên nhiên nghiêm ngặt (zapovednik) thành lập năm 1963 để bảo vệ hệ sinh thái taiga miền núi và nghiên cứu tác động của hồ chứa Zeya. Địa hình núi non với hơn 200 suối, hệ động thực vật giao thoa của nhiều vùng địa lý.",
    "Khu bảo tồn thiên nhiên Zeya trải trên sườn đông của dãy Tukuringra, nơi thượng nguồn sông Zeya, được thành lập từ năm 1963 — một phần để làm «vùng đối chứng» nghiên cứu ảnh hưởng sinh thái của đập và hồ chứa Zeya. Đây là một zapovednik, tức khu bảo tồn nghiêm ngặt bậc nhất của Nga, nơi thiên nhiên gần như được giữ nguyên vẹn. Hơn 90% diện tích phủ rừng taiga với thông rụng lá, sồi Mông Cổ, vân sam và tuyết tùng phân tầng theo độ cao; địa hình núi non có hơn hai trăm con suối và thác ghềnh. Vị trí đặc biệt trên các dãy núi khiến nơi đây trở thành điểm gặp gỡ của nhiều luồng động vật — Đông Siberia, Mãn Châu, Daur, Mông Cổ và Okhotsk-Kamchatka. Là khu bảo tồn nghiêm ngặt, phần lớn diện tích đóng cửa với du khách phổ thông, nhưng có ba tuyến du lịch sinh thái được mở với giấy phép đăng ký trước, từ đường mòn giáo dục 3 km tới các cung leo núi 2–3 ngày ngắm cảnh từ đỉnh Tukuringra. Văn phòng khu bảo tồn đặt tại thành phố Zeya.",
    [
        "Zapovednik (bảo tồn nghiêm ngặt) từ 1963, nghiên cứu tác động sinh thái của hồ chứa Zeya.",
        "Rừng taiga miền núi trên dãy Tukuringra, hơn 200 suối và thác ghềnh.",
        "Ba tuyến du lịch sinh thái cần giấy phép; văn phòng tại thành phố Zeya.",
    ],
    {
        "hours_vi": "Chỉ tham quan theo tuyến sinh thái được cấp phép; đăng ký trước qua ban quản lý ở Zeya.",
        "ticket_vi": "Có phí tuyến và phí hướng dẫn; một số tuyến yêu cầu tiêm phòng ve rừng.",
        "duration_vi": "Từ ~3 giờ (đường mòn ngắn) tới 2–3 ngày (cung leo núi).",
        "best_time_vi": "Cuối xuân đến đầu thu; tránh mùa gấu sinh sản và mùa đông đóng cửa một số tuyến.",
        "tips_vi": "Liên hệ ban quản lý ở thành phố Zeya để xin phép và hướng dẫn; chuẩn bị chống ve, giày leo núi và nước.",
    },
    [
        {"title": "Wikipedia (EN) — Zeya Nature Reserve", "url": "https://en.wikipedia.org/wiki/Zeya_Nature_Reserve"},
        {"title": "Trang chính thức — Зейский заповедник", "url": "http://zeyzap.ru/"},
    ],
    ["nature-reserve", "zapovednik", "taiga", "tukuringra", "ecotourism", "zeya"],
    maps_text("Зейский заповедник", "Зея", "Zeya Nature Reserve", "Zeya", 53.962780, 127.372500),
))

# 13) Зейское водохранилище -------------------------------------------------------
RECORDS.append(rec(
    "zeya-reservoir",
    "Hồ chứa Zeya (Zeyskoe vodokhranilishche)",
    "Зейское водохранилище",
    "Zeya Reservoir",
    ["park_garden"],
    54.416700, 127.750000,
    "Trên sông Zeya, phía trên thành phố Zeya, huyện Zeysky, tỉnh Amur, Nga.",
    "Hồ chứa nhân tạo khổng lồ hình thành sau đập thuỷ điện Zeya, rộng khoảng 2.420 km² — lớn thứ ba nước Nga về thể tích. Vùng nước mênh mông giữa núi rừng, điểm câu cá và ngắm cảnh hoang sơ của miền Bắc Amur.",
    "Hồ chứa Zeya là một trong những vùng nước nhân tạo lớn nhất nước Nga, hình thành khi đập thuỷ điện Zeya chặn dòng sông trong những năm 1974–1980. Với diện tích khoảng 2.420 km², dài tới 227 km và rộng nhất 24 km, hồ đứng thứ ba toàn Liên bang Nga về thể tích, chỉ sau hồ Bratsk và Krasnoyarsk. Ở đoạn hẹp trong dãy Tukuringra, hồ mang dáng vẻ một hẻm nước sâu với những vịnh do các phụ lưu tạo thành; càng lên phía bắc, trong lòng chảo Thượng Zeya, hồ mở ra thành mặt nước rộng như biển hồ. Tuyến đường sắt Baikal–Amur (BAM) chạy dọc bờ bắc và vượt qua một vịnh của hồ bằng cây cầu đường sắt dài 1.100 mét. Vào mùa đông, mặt hồ đóng băng dày tới hơn một mét. Là vùng hồ xa xôi giữa núi rừng taiga, Zeya thu hút những người ưa câu cá (cá măng, cá diếc bạc), chèo thuyền và tìm kiếm cảnh quan hoang sơ; thị trấn Zeya và khu vực đập là điểm ngắm hồ thuận tiện nhất.",
    [
        "Hồ chứa nhân tạo lớn thứ ba nước Nga về thể tích (~2.420 km²).",
        "Dài 227 km giữa núi rừng taiga, mùa đông đóng băng dày hơn 1 m.",
        "Tuyến đường sắt BAM chạy dọc bờ bắc, vượt hồ bằng cầu dài 1.100 m.",
    ],
    {
        "hours_vi": "Không gian thiên nhiên mở; tiếp cận thuận tiện nhất từ thành phố Zeya và khu vực đập.",
        "ticket_vi": "Miễn phí; dịch vụ thuê thuyền, tour câu cá tính phí riêng.",
        "duration_vi": "Từ nửa ngày tới nhiều ngày nếu đi câu cá, cắm trại.",
        "best_time_vi": "Mùa hè cho chèo thuyền, câu cá; mùa đông ngắm hồ băng.",
        "tips_vi": "Vùng xa xôi, chuẩn bị hậu cần kỹ; đi cùng hướng dẫn địa phương nếu ra hồ bằng thuyền.",
    },
    [
        {"title": "Wikipedia (RU) — Зейское водохранилище", "url": "https://ru.wikipedia.org/wiki/Зейское_водохранилище"},
        {"title": "Wikipedia (EN) — Zeya Dam (Zeya Reservoir)", "url": "https://en.wikipedia.org/wiki/Zeya_Dam"},
    ],
    ["reservoir", "lake", "zeya", "fishing", "taiga", "bam"],
    maps_text("Зейское водохранилище", "Зея", "Zeya Reservoir", "Zeya", 54.416700, 127.750000),
))

# 14) Музей истории БАМа (Тында) --------------------------------------------------
RECORDS.append(rec(
    "bam-history-museum-tynda",
    "Bảo tàng Lịch sử tuyến đường sắt BAM (Muzey istorii BAMa)",
    "Музей истории БАМа",
    "BAM History Museum (Tynda)",
    ["museum"],
    55.146600, 124.730843,
    "Thành phố Tynda, tỉnh Amur, Nga.",
    "Bảo tàng độc đáo kể câu chuyện về tuyến đường sắt Baikal–Amur (BAM) huyền thoại — một trong những công trình xây dựng vĩ đại nhất thời Liên Xô. Đặt tại Tynda, «thủ đô của BAM».",
    "Nằm ở Tynda — thành phố được mệnh danh là «thủ đô của BAM» — Bảo tàng Lịch sử tuyến đường sắt Baikal–Amur kể lại một trong những trang sử xây dựng hào hùng và gian khổ nhất của thời Liên Xô. Tuyến BAM dài hơn 4.300 km xuyên qua rừng taiga, núi non và vùng băng vĩnh cửu của Siberia và Viễn Đông, được xây dựng chủ yếu trong thập niên 1970–1980 bởi hàng vạn thanh niên tình nguyện từ khắp Liên bang. Bảo tàng lưu giữ tư liệu, ảnh, đồ dùng, dụng cụ lao động và những câu chuyện đời thường của các «bamovtsy» — những người dựng nên tuyến đường và cả thành phố Tynda giữa hoang vu. Các gian trưng bày tái hiện điều kiện sống trong lều bạt và toa tàu, tinh thần lao động tập thể, cũng như thiên nhiên khắc nghiệt mà họ phải chinh phục. Với du khách, đây là nơi cảm nhận sâu sắc quy mô và cái giá của công trình BAM, đồng thời hiểu vì sao Tynda tự hào là biểu tượng của cả một thế hệ.",
    [
        "Kể câu chuyện tuyến đường sắt BAM huyền thoại — đại công trình thời Liên Xô.",
        "Đặt tại Tynda, «thủ đô của BAM», tái hiện đời sống của những «bamovtsy».",
        "Tư liệu, ảnh và hiện vật về lao động, thiên nhiên khắc nghiệt và xây dựng thành phố.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Kết hợp tham quan ga Tynda hoành tráng gần đó để hiểu trọn di sản BAM.",
    },
    [
        {"title": "Yandex Maps — Музей истории БАМа (org)", "url": "https://yandex.com/maps/org/muzey_istorii_bama/83754552496/"},
        {"title": "Wikipedia (EN) — Baikal–Amur Mainline", "url": "https://en.wikipedia.org/wiki/Baikal–Amur_Mainline"},
    ],
    ["museum", "bam", "railway", "tynda", "soviet-history"],
    maps_org("https://yandex.com/maps/org/muzey_istorii_bama/83754552496/", "BAM History Museum", "Tynda"),
))

# 15) Железнодорожный вокзал Тында ------------------------------------------------
RECORDS.append(rec(
    "tynda-railway-station",
    "Nhà ga Tynda (Vokzal Tynda) — «thủ đô của BAM»",
    "Железнодорожный вокзал Тында",
    "Tynda Railway Station",
    ["other"],
    55.139271, 124.739072,
    "Thành phố Tynda, tỉnh Amur, Nga.",
    "Nhà ga trung tâm của Tynda — nút giao then chốt của tuyến đường sắt BAM. Toà nhà ga đồ sộ, hiện đại theo phong cách Xô-viết muộn, được ví như «cây đàn piano» và là biểu tượng kiến trúc của cả tuyến BAM.",
    "Nhà ga Tynda là một trong những công trình biểu tượng nhất của tuyến đường sắt Baikal–Amur. Tynda là đầu mối then chốt nơi tuyến BAM giao với nhánh nối xuống tuyến xuyên Siberia, nên thành phố được gọi là «thủ đô của BAM». Toà nhà ga được xây dựng trong thời kỳ đại công trình BAM và mang dáng vẻ đồ sộ, hiện đại đặc trưng của kiến trúc Xô-viết muộn — với khối mái vươn cao khác thường mà người dân hay ví von như hình dáng một cây đàn piano hay cánh buồm. Vào thời hoàng kim, đây là niềm tự hào của những người xây dựng tuyến đường, một «cung điện» giữa vùng taiga hoang vu để đón đưa hàng vạn công nhân và hành khách. Ngày nay, nhà ga vẫn là cửa ngõ chính của Tynda, điểm khởi hành của những hành trình đường sắt dài xuyên Viễn Đông. Với du khách yêu thích đường sắt và lịch sử Xô-viết, đứng trước nhà ga Tynda là cách trực quan để cảm nhận tầm vóc và tinh thần của công trình BAM.",
    [
        "Đầu mối then chốt của tuyến BAM — Tynda là «thủ đô của BAM».",
        "Kiến trúc Xô-viết muộn đồ sộ, được ví như «cây đàn piano» giữa rừng taiga.",
        "Điểm khởi hành của các hành trình đường sắt dài xuyên Viễn Đông.",
    ],
    {
        "hours_vi": "Nhà ga hoạt động phục vụ hành khách; sảnh mở theo giờ tàu.",
        "ticket_vi": "Vào ga miễn phí; vé tàu mua riêng theo hành trình.",
        "duration_vi": "Ngắm và chụp ảnh khoảng 20–40 phút.",
        "best_time_vi": "Quanh năm; ban ngày để ngắm rõ kiến trúc mặt tiền.",
        "tips_vi": "Kết hợp với Bảo tàng lịch sử BAM gần đó; giữ ý khi chụp trong khu vực an ninh nhà ga.",
    },
    [
        {"title": "Railwayz.info — станция Тында", "url": "https://railwayz.info/photolines/station/10215"},
        {"title": "Wikipedia (RU) — Тында", "url": "https://ru.wikipedia.org/wiki/Тында"},
    ],
    ["railway-station", "bam", "tynda", "soviet-architecture", "landmark"],
    maps_text("Железнодорожный вокзал Тында", "Тында", "Tynda Railway Station", "Tynda", 55.139271, 124.739072),
))

# 16) Бурейская ГЭС ---------------------------------------------------------------
RECORDS.append(rec(
    "bureya-dam",
    "Đập thuỷ điện Bureya (Bureyskaya GES)",
    "Бурейская ГЭС",
    "Bureya Hydroelectric Dam",
    ["other"],
    50.269170, 130.313330,
    "Trên sông Bureya, gần thị trấn Talakan, huyện Bureysky, tỉnh Amur, Nga.",
    "Nhà máy thuỷ điện lớn nhất vùng Viễn Đông Nga, đập bê tông trọng lực cao 140 m trên sông Bureya. Công suất lắp đặt 2.010 MW — một trong những công trình năng lượng quan trọng nhất miền Đông nước Nga.",
    "Đập thuỷ điện Bureya là công trình thuỷ điện lớn nhất vùng Viễn Đông Nga, chắn ngang sông Bureya gần thị trấn Talakan. Đập bê tông trọng lực cao 140 mét, dài 736 mét, với sáu tổ máy tổng công suất 2.010 MW — mỗi tổ máy 335 MW. Ý tưởng xây dựng có từ năm 1976, nhưng công trình bị đình trệ suốt thập niên 1990 và chỉ được khởi động lại vào năm 1999; tổ máy đầu tiên phát điện năm 2003 và toàn bộ công trình hoàn thành năm 2009. Nhà máy đóng vai trò then chốt trong việc cấp điện cho miền Đông nước Nga và điều tiết dòng chảy sông Bureya. Khối đập khổng lồ giữa cảnh núi rừng, đặc biệt khi các cửa xả tràn hoạt động phun nước trắng xoá, là một cảnh tượng hùng vĩ. Cùng với nhà máy Nizhne-Bureyskaya ở hạ lưu, cụm thuỷ điện Bureya thể hiện quy mô công nghiệp năng lượng của vùng Amur. Đây là điểm tham quan thú vị cho những ai quan tâm tới kỹ thuật và cảnh quan.",
    [
        "Nhà máy thuỷ điện lớn nhất vùng Viễn Đông Nga (công suất 2.010 MW).",
        "Đập bê tông trọng lực cao 140 m trên sông Bureya, hoàn thành năm 2009.",
        "Cùng nhà máy Nizhne-Bureyskaya tạo thành cụm thuỷ điện điều tiết sông Bureya.",
    ],
    {
        "hours_vi": "Công trình năng lượng; ngắm cảnh bên ngoài, tham quan nội bộ cần đăng ký có phép.",
        "ticket_vi": "Ngắm cảnh miễn phí; tour nội bộ (nếu có) theo chương trình nhà máy.",
        "duration_vi": "Khoảng 30–60 phút phần ngắm cảnh.",
        "best_time_vi": "Cuối hè khi mực nước cao, có thể chứng kiến xả tràn.",
        "tips_vi": "Tuân thủ khu vực an ninh quanh đập; thị trấn Talakan là điểm dừng chân gần nhất.",
    },
    [
        {"title": "Wikipedia (EN) — Bureya Dam", "url": "https://en.wikipedia.org/wiki/Bureya_Dam"},
        {"title": "Global Energy Monitor — Bureyskaya hydroelectric plant", "url": "https://www.gem.wiki/Bureyskaya_hydroelectric_plant"},
    ],
    ["dam", "hydroelectric", "bureya-river", "talakan", "engineering"],
    maps_text("Бурейская ГЭС", "Талакан", "Bureya Hydroelectric Dam", "Talakan", 50.269170, 130.313330),
))

# 17) Нижне-Бурейская ГЭС ---------------------------------------------------------
RECORDS.append(rec(
    "nizhne-bureyskaya-hpp",
    "Đập thuỷ điện Hạ Bureya (Nizhne-Bureyskaya GES)",
    "Нижне-Бурейская ГЭС",
    "Nizhne-Bureyskaya Hydroelectric Plant",
    ["other"],
    49.789100, 129.979200,
    "Trên sông Bureya, gần thị trấn Novoburejskij, huyện Bureysky, tỉnh Amur, Nga.",
    "Nhà máy thuỷ điện «điều áp» xây ở hạ lưu đập Bureya, hoàn thành giữa thập niên 2010. Công trình hiện đại giúp ổn định dòng chảy do nhà máy Bureya xả ra, đồng thời bổ sung nguồn điện cho vùng Amur.",
    "Nhà máy thuỷ điện Hạ Bureya được xây dựng ở hạ lưu đập Bureya với vai trò «điều áp» (contra-regulator): nó tiếp nhận và làm mượt dòng chảy dao động do nhà máy thuỷ điện Bureya phía trên xả ra khi tăng giảm công suất, nhờ đó bảo vệ hạ lưu và ổn định mực nước. Đây là một trong những công trình thuỷ điện mới của nước Nga hiện đại, hoàn thành và đưa vào vận hành giữa thập niên 2010, đồng thời bổ sung một nguồn điện đáng kể cho lưới điện vùng Amur. Nằm gần thị trấn Novoburejskij, cụm đập tràn thấp trải rộng trên sông Bureya tạo nên một hồ chứa nhỏ và cảnh quan mặt nước yên bình khác hẳn khối đập cao vút của nhà máy Bureya ở thượng lưu. Cùng nhau, hai nhà máy tạo thành một hệ thống thuỷ điện bậc thang tiêu biểu. Với du khách quan tâm tới năng lượng và kỹ thuật hiện đại, đây là điểm bổ sung thú vị khi khám phá vùng Bureya.",
    [
        "Nhà máy «điều áp» ở hạ lưu đập Bureya, ổn định dòng chảy và mực nước.",
        "Công trình thuỷ điện mới của nước Nga hiện đại, vận hành giữa thập niên 2010.",
        "Cùng nhà máy Bureya tạo thành hệ thống thuỷ điện bậc thang trên sông Bureya.",
    ],
    {
        "hours_vi": "Công trình năng lượng; ngắm cảnh bên ngoài tự do.",
        "ticket_vi": "Miễn phí khi ngắm từ bờ.",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Mùa ấm để thuận tiện di chuyển và ngắm mặt nước.",
        "tips_vi": "Tuân thủ khu vực an ninh; kết hợp cùng đập Bureya ở thượng lưu để thấy hệ thống bậc thang.",
    },
    [
        {"title": "Global Energy Monitor — Nizhne-Bureyskaya hydroelectric plant", "url": "https://www.gem.wiki/Nizhne-Bureyskaya_hydroelectric_plant"},
        {"title": "Wikipedia (RU) — Нижне-Бурейская ГЭС", "url": "https://ru.wikipedia.org/wiki/Нижне-Бурейская_ГЭС"},
    ],
    ["dam", "hydroelectric", "bureya-river", "novoburejskij", "modern"],
    maps_text("Нижне-Бурейская ГЭС", "Новобурейский", "Nizhne-Bureyskaya Hydroelectric Plant", "Novoburejskij", 49.789100, 129.979200),
))

# 18) Муравьёвский парк устойчивого природопользования ----------------------------
RECORDS.append(rec(
    "muravyovka-park",
    "Công viên Muravyovka (thiên đường sếu và cò)",
    "Муравьёвский парк устойчивого природопользования",
    "Muravyovka Park",
    ["park_garden"],
    49.839722, 127.726944,
    "Gần làng Muravyovka, huyện Tambovsky, cách Blagoveshchensk khoảng 65 km, tỉnh Amur, Nga.",
    "Công viên thiên nhiên tư nhân đầu tiên của nước Nga, thành lập năm 1996 để bảo vệ vùng đất ngập nước quý giá — nơi làm tổ của loài sếu Daurian và sếu Nhật quý hiếm. Điểm ngắm chim nổi tiếng bậc nhất vùng Amur.",
    "Công viên Muravyovka nằm giữa những cánh đồng ngập nước bao la ở lưu vực sông Amur, huyện Tambovsky, cách Blagoveshchensk khoảng 65 km. Đây là công viên bảo tồn thiên nhiên phi nhà nước đầu tiên của nước Nga, ra đời năm 1996 nhờ ý tưởng của nhà khoa học Sergey Smirenski cùng sự hỗ trợ của các quỹ bảo tồn quốc tế. Trên diện tích khoảng 6.500 ha, công viên là nơi sinh trưởng của hơn 700 loài thực vật và là chốn dừng chân, làm tổ, trú đông của hơn 300 loài chim — trong đó có nhiều loài nằm trong Sách Đỏ nước Nga. Nổi tiếng nhất là hai loài sếu quý hiếm làm tổ tại đây: sếu Daurian và sếu Nhật (sếu đầu đỏ). Điểm đặc biệt trong triết lý của công viên là mô hình «sử dụng bền vững»: con người và thiên nhiên cùng tồn tại, người dân địa phương vẫn canh tác, chăn thả trong khi các vùng trọng yếu được bảo vệ. Với người yêu thiên nhiên và chim hoang dã, Muravyovka là điểm ngắm sếu, cò và các loài chim di cư hàng đầu của vùng Viễn Đông.",
    [
        "Công viên bảo tồn thiên nhiên tư nhân đầu tiên của nước Nga (từ 1996).",
        "Nơi làm tổ của sếu Daurian và sếu Nhật quý hiếm; hơn 300 loài chim.",
        "Vùng đất ngập nước tầm quan trọng quốc tế, mô hình «sử dụng bền vững».",
    ],
    {
        "hours_vi": "Tham quan theo chương trình của công viên; nên liên hệ trước để đăng ký và có hướng dẫn.",
        "ticket_vi": "Có phí tham quan/tour; các chương trình sinh thái và tình nguyện riêng.",
        "duration_vi": "Từ nửa ngày tới trọn ngày; có thể lưu trú để ngắm chim.",
        "best_time_vi": "Mùa xuân và thu — thời điểm sếu, cò và chim di cư tập trung đông nhất.",
        "tips_vi": "Mang ống nhòm và ống kính tele; giữ yên lặng, không lại gần tổ chim; đặt lịch trước với ban quản lý.",
    },
    [
        {"title": "Wikipedia (RU) — Муравьёвский парк", "url": "https://ru.wikipedia.org/wiki/Муравьёвский_парк"},
        {"title": "Wikipedia (EN) — Muraviovka Park", "url": "https://en.wikipedia.org/wiki/Muraviovka_Park"},
    ],
    ["wetland", "cranes", "birdwatching", "nature-park", "tambovsky", "conservation"],
    maps_text("Муравьёвский парк", "Тамбовский район", "Muravyovka Park", "Tambovka", 49.839722, 127.726944),
))

# 19) Свято-Никольский храм (Свободный) -------------------------------------------
RECORDS.append(rec(
    "svobodny-st-nicholas-church",
    "Nhà thờ Thánh Nikolai ở Svobodny (Svyato-Nikolskiy khram)",
    "Свято-Никольский храм",
    "St. Nicholas Church (Svobodny)",
    ["church"],
    51.388677, 128.120861,
    "Ул. Пушкина, 7, thành phố Svobodny, tỉnh Amur, Nga.",
    "Nhà thờ gỗ Chính Thống giáo lịch sử ở thành phố Svobodny, xây từ đầu thế kỷ 20 (khoảng năm 1913). Một trong những ngôi thánh đường bằng gỗ hiếm hoi còn lại ở vùng Amur, mang vẻ đẹp mộc mạc của kiến trúc gỗ Nga.",
    "Thành phố Svobodny bên sông Zeya từng là một trung tâm đường sắt quan trọng của vùng Amur, và Nhà thờ Thánh Nikolai là một trong những di tích tôn giáo lâu đời của nơi đây. Được dựng từ đầu thế kỷ 20, vào khoảng năm 1913, đây là một ngôi thánh đường bằng gỗ theo truyền thống kiến trúc nhà thờ gỗ Nga — loại công trình ngày càng hiếm gặp ở vùng Viễn Đông sau những biến động của thế kỷ 20. Ngôi nhà thờ với thân gỗ ấm áp, mái vòm và tháp chuông thanh thoát là nơi thờ phụng của cộng đồng Chính Thống giáo địa phương, đồng thời là chứng nhân cho lịch sử hình thành và phát triển của Svobodny. Trải qua thời kỳ Xô-viết khi nhiều nhà thờ bị đóng cửa hoặc phá bỏ, sự tồn tại của ngôi thánh đường này càng thêm ý nghĩa. Với du khách đi sâu vào vùng Amur, đây là điểm dừng chân giúp cảm nhận nét đẹp mộc mạc, tĩnh lặng của kiến trúc gỗ tôn giáo Nga nơi tỉnh lỵ.",
    [
        "Nhà thờ gỗ Chính Thống giáo lịch sử, xây khoảng năm 1913.",
        "Một trong số ít thánh đường bằng gỗ còn lại ở vùng Amur.",
        "Chứng nhân lịch sử của thành phố đường sắt Svobodny.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ lễ hằng ngày.",
        "ticket_vi": "Miễn phí (nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 15–30 phút.",
        "best_time_vi": "Buổi sáng hoặc các dịp lễ Chính Thống giáo.",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn; xin phép trước khi chụp ảnh bên trong.",
    },
    [
        {"title": "Sobory.ru — Свято-Никольский храм (Свободный)", "url": "https://sobory.ru/article/?object=20712"},
        {"title": "Wikipedia (RU) — Свободный (город)", "url": "https://ru.wikipedia.org/wiki/Свободный_(город)"},
    ],
    ["church", "wooden-church", "orthodox", "svobodny", "history"],
    maps_text("Свято-Никольский храм", "Свободный", "St. Nicholas Church", "Svobodny", 51.388677, 128.120861),
))

# 20) Беседка-ротонда (набережная Благовещенска) ----------------------------------
RECORDS.append(rec(
    "blagoveshchensk-rotunda",
    "Mái vòm Rotunda trên bờ kè Blagoveshchensk",
    "Беседка-ротонда",
    "Rotunda on the Amur Embankment",
    ["monument"],
    50.256285, 127.518158,
    "Trên bờ kè sông Amur, gần công viên trung tâm, thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Mái vòm rotunda duyên dáng bên bờ kè sông Amur — một trong những biểu tượng được chụp ảnh nhiều nhất của Blagoveshchensk. Công trình tròn với hàng cột trắng, nhìn thẳng sang thành phố Hắc Hà của Trung Quốc bên kia sông.",
    "Mái vòm Rotunda là một trong những điểm nhấn kiến trúc dễ thương và được yêu thích nhất trên bờ kè sông Amur ở Blagoveshchensk. Đó là một vọng lâu hình tròn với hàng cột trắng nâng đỡ mái vòm thanh thoát, đặt ngay sát mép nước nhìn thẳng sang thành phố Hắc Hà (Heihe) của Trung Quốc bên kia dòng Amur. Rotunda đã trở thành «phông nền» quen thuộc cho vô số bức ảnh cưới, ảnh kỷ niệm và ảnh check-in của cả người dân lẫn du khách; đây cũng là nơi hò hẹn, dạo mát và ngắm hoàng hôn lý tưởng. Vào buổi tối, khi ánh đèn từ hai bờ sông bừng sáng, khung cảnh quanh rotunda càng thêm lung linh. Nằm trong cụm danh thắng của bờ kè cùng Khải Hoàn Môn, tượng đài Muravyov-Amursky và Quảng trường Chiến thắng, mái vòm là một điểm dừng ngắn nhưng gần như không thể bỏ qua khi dạo bờ kè. Với du khách Việt, đây là chỗ chụp ảnh đẹp để ghi lại khoảnh khắc «một bước tới Trung Quốc» qua dòng sông biên giới.",
    [
        "Mái vòm rotunda cột trắng — biểu tượng chụp ảnh của bờ kè Blagoveshchensk.",
        "Nhìn thẳng sang thành phố Hắc Hà (Trung Quốc) bên kia sông Amur.",
        "Nằm trong cụm danh thắng bờ kè: Khải Hoàn Môn, tượng đài, Quảng trường Chiến thắng.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–15 phút.",
        "best_time_vi": "Hoàng hôn và buổi tối mùa hè khi hai bờ lên đèn.",
        "tips_vi": "Điểm chụp ảnh đẹp; mang giấy tờ tuỳ thân vì là khu vực biên giới.",
    },
    [
        {"title": "Yandex Maps — Беседка-ротонда (org)", "url": "https://yandex.ru/maps/org/besedka_rotonda/160058638353/"},
        {"title": "Wikipedia (RU) — Благовещенск", "url": "https://ru.wikipedia.org/wiki/Благовещенск"},
    ],
    ["rotunda", "embankment", "landmark", "photo-spot", "blagoveshchensk", "china-view"],
    maps_org("https://yandex.ru/maps/org/besedka_rotonda/160058638353/", "Rotunda on the Amur Embankment", "Blagoveshchensk"),
))

# 21) Первомайский парк (Благовещенск) --------------------------------------------
RECORDS.append(rec(
    "pervomaisky-park-blagoveshchensk",
    "Công viên Pervomaisky (Công viên Mồng Một Tháng Năm)",
    "Первомайский парк",
    "Pervomaisky Park (Blagoveshchensk)",
    ["park_garden"],
    50.247841, 127.569658,
    "Ул. Краснофлотская, 2, ven bờ sông Amur, thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Công viên ven sông ở phía đông bờ kè Blagoveshchensk, không gian xanh yên bình để dạo bộ, đạp xe và nghỉ ngơi. Điểm thư giãn được người dân yêu thích, tách khỏi khu trung tâm nhộn nhịp.",
    "Công viên Pervomaisky (mang tên ngày Quốc tế Lao động 1/5) là một mảng xanh dễ chịu nằm ven sông Amur, về phía đông so với khu bờ kè trung tâm của Blagoveshchensk. Đây là kiểu công viên thành phố thư thái với những lối đi dạo dưới tán cây, ghế nghỉ, khu vui chơi và tầm nhìn ra dòng sông biên giới. So với đoạn bờ kè trung tâm luôn đông đúc, Pervomaisky yên tĩnh hơn, là nơi người dân địa phương ra tập thể dục buổi sáng, đưa trẻ đi chơi hay đơn giản là ngồi ngắm sông. Vào mùa hè, công viên rợp bóng mát và mang lại cảm giác gần gũi với thiên nhiên ngay trong lòng thành phố; mùa đông, khung cảnh phủ tuyết lại có nét đẹp tĩnh lặng riêng. Với du khách muốn tìm một khoảng lặng thư giãn hoặc đi dạo, đạp xe dọc sông Amur ngoài khu trung tâm, Pervomaisky là lựa chọn nhẹ nhàng và thoải mái.",
    [
        "Công viên ven sông Amur, yên tĩnh hơn khu bờ kè trung tâm.",
        "Không gian xanh để đi dạo, đạp xe, tập thể dục và ngắm sông.",
        "Điểm thư giãn quen thuộc của người dân Blagoveshchensk.",
    ],
    {
        "hours_vi": "Không gian mở, tham quan tự do; dịch vụ hoạt động chủ yếu mùa ấm.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–45 phút.",
        "best_time_vi": "Sáng sớm hoặc chiều mát mùa hè.",
        "tips_vi": "Kết hợp đi dạo/đạp xe dọc sông Amur; mang nước và đồ chống nắng vào mùa hè.",
    },
    [
        {"title": "Yandex Maps — Первомайский парк, Благовещенск", "url": "https://yandex.ru/maps/77/blagoveshchensk/"},
        {"title": "Wikipedia (RU) — Благовещенск", "url": "https://ru.wikipedia.org/wiki/Благовещенск"},
    ],
    ["park", "riverside", "amur-river", "blagoveshchensk", "recreation"],
    maps_text("Первомайский парк", "Благовещенск", "Pervomaisky Park", "Blagoveshchensk", 50.247841, 127.569658),
))

# 22) Памятник «Челнок» (Благовещенск) --------------------------------------------
RECORDS.append(rec(
    "chelnok-monument-blagoveshchensk",
    "Tượng «Người buôn Chelnok» (Pamyatnik Chelnoku)",
    "Памятник «Челнок»",
    "The Shuttle Trader Monument",
    ["monument"],
    50.262703, 127.535098,
    "Ул. 50 лет Октября, 15, thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Bức tượng đường phố độc đáo tôn vinh những «chelnok» — người buôn con thoi chở hàng qua biên giới Nga – Trung thời thập niên 1990. Một biểu tượng dí dỏm phản ánh lịch sử thương mại biên giới đặc trưng của Blagoveshchensk.",
    "«Chelnok» (nghĩa đen là «con thoi») là tên gọi dân dã cho những người buôn nhỏ thời kỳ hậu Xô-viết đầu thập niên 1990 — họ mang vác những túi hàng khổng lồ, qua lại như con thoi giữa Blagoveshchensk và thành phố Hắc Hà bên kia sông để buôn quần áo, đồ gia dụng, thực phẩm. Trong giai đoạn kinh tế khó khăn, chính những chelnok này đã nuôi sống nhiều gia đình và làm nên sức sống thương mại đặc trưng của vùng biên. Bức tượng đường phố ở Blagoveshchensk khắc hoạ hình ảnh một người buôn con thoi trĩu nặng túi hàng — vừa hài hước, đời thường, vừa gợi nhớ một thời đã qua. Đây là kiểu tượng «genre» (đời thường) rất được ưa chuộng ở các thành phố Nga, nơi người dân và du khách thích chụp ảnh và chạm tay «lấy may». Với du khách Việt, bức tượng là một góc nhìn thú vị và đầy tính người về lịch sử giao thương Nga – Trung, một câu chuyện gần gũi với chính trải nghiệm buôn bán biên mậu ở nhiều nơi.",
    [
        "Tôn vinh những «chelnok» — người buôn con thoi qua biên giới Nga – Trung thập niên 1990.",
        "Tượng đường phố đời thường dí dỏm, phản ánh lịch sử thương mại biên giới Blagoveshchensk.",
        "Điểm chụp ảnh thú vị, gần gũi ở trung tâm thành phố.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do 24/7.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10 phút.",
        "best_time_vi": "Quanh năm; ban ngày để chụp ảnh rõ nét.",
        "tips_vi": "Kết hợp dạo phố trung tâm; là điểm check-in vui khi tìm hiểu lịch sử biên mậu.",
    },
    [
        {"title": "Yandex Maps — Памятник «Челнок» (org)", "url": "https://yandex.ru/maps/org/chelnok/164073208857/"},
        {"title": "Wikipedia (RU) — Благовещенск", "url": "https://ru.wikipedia.org/wiki/Благовещенск"},
    ],
    ["monument", "genre-sculpture", "chelnok", "trade-history", "blagoveshchensk", "photo-spot"],
    maps_org("https://yandex.ru/maps/org/chelnok/164073208857/", "The Shuttle Trader Monument", "Blagoveshchensk"),
))

# 23) Кафедральный собор Троицы Живоначальной (Тында) -----------------------------
RECORDS.append(rec(
    "tynda-trinity-cathedral",
    "Nhà thờ chính toà Chúa Ba Ngôi ở Tynda (Sobor Troitsy)",
    "Кафедральный собор Троицы Живоначальной",
    "Holy Trinity Cathedral (Tynda)",
    ["church"],
    55.149021, 124.735363,
    "Ул. Красная Пресня, 20, thành phố Tynda, tỉnh Amur, Nga.",
    "Nhà thờ chính toà Chính Thống giáo của Tynda, trung tâm tôn giáo của cả vùng bắc Amur trên tuyến BAM. Ngôi thánh đường với những mái vòm vàng nổi bật giữa thành phố đường sắt trẻ tuổi.",
    "Nhà thờ chính toà Chúa Ba Ngôi là trung tâm tôn giáo Chính Thống giáo của Tynda — thành phố «thủ đô của BAM» ở phía bắc tỉnh Amur. Khác với các nhà thờ cổ ở miền tây nước Nga, đây là một ngôi thánh đường tương đối trẻ, ra đời cùng với sự phát triển của Tynda sau thời kỳ xây dựng tuyến đường sắt Baikal–Amur, đáp ứng nhu cầu tâm linh của cộng đồng cư dân mới nơi vùng đất taiga khắc nghiệt. Với những mái vòm dát vàng lấp lánh vươn lên trên nền phố phường và núi rừng, nhà thờ trở thành một điểm nhấn kiến trúc và tinh thần của thành phố. Bên trong, không gian trang nghiêm với thánh tượng, đèn nến và các nghi lễ Chính Thống giáo mang lại cảm giác ấm áp giữa vùng đất lạnh giá. Đối với du khách dừng chân ở Tynda trên hành trình đường sắt xuyên Viễn Đông, nhà thờ là nơi cảm nhận đời sống tâm linh và sự gắn kết cộng đồng của một thành phố sinh ra từ đại công trình BAM.",
    [
        "Nhà thờ chính toà Chính Thống giáo, trung tâm tôn giáo của Tynda và vùng bắc Amur.",
        "Mái vòm dát vàng nổi bật giữa thành phố đường sắt trẻ tuổi.",
        "Ngôi thánh đường sinh ra cùng sự phát triển của Tynda thời hậu BAM.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ lễ hằng ngày.",
        "ticket_vi": "Miễn phí (nơi thờ phụng đang hoạt động).",
        "duration_vi": "Khoảng 20–30 phút.",
        "best_time_vi": "Buổi sáng hoặc dịp lễ Chính Thống giáo; mùa hè dễ di chuyển.",
        "tips_vi": "Ăn mặc kín đáo, nữ trùm khăn; kết hợp tham quan Bảo tàng BAM và ga Tynda.",
    },
    [
        {"title": "Yandex Maps — Кафедральный собор Троицы Живоначальной, Тында", "url": "https://yandex.ru/maps/"},
        {"title": "Wikipedia (RU) — Тында", "url": "https://ru.wikipedia.org/wiki/Тында"},
    ],
    ["church", "cathedral", "orthodox", "tynda", "golden-domes", "bam"],
    maps_text("Кафедральный собор Троицы Живоначальной", "Тында", "Holy Trinity Cathedral", "Tynda", 55.149021, 124.735363),
))

# 24) Пожарная каланча (Благовещенск) ---------------------------------------------
RECORDS.append(rec(
    "blagoveshchensk-fire-tower",
    "Tháp cứu hoả lịch sử Blagoveshchensk (Pozharnaya kalancha)",
    "Пожарная каланча",
    "Historic Fire Watchtower (Blagoveshchensk)",
    ["other"],
    50.260858, 127.555442,
    "Ул. Амурская, 72, thành phố Blagoveshchensk, tỉnh Amur, Nga.",
    "Tháp canh cứu hoả bằng gạch lịch sử từ đầu thế kỷ 20, một trong những công trình kiến trúc cổ đặc trưng của Blagoveshchensk. Biểu tượng của thời kỳ thành phố thương mại phồn thịnh bên sông Amur.",
    "Tháp cứu hoả (pozharnaya kalancha) là một trong những công trình kiến trúc lịch sử đáng chú ý của Blagoveshchensk, gợi nhớ thời kỳ thành phố còn là một thương cảng phồn thịnh đầu thế kỷ 20. Vào thời đó, khi phần lớn nhà cửa còn bằng gỗ và nguy cơ hoả hoạn luôn rình rập, những tháp canh cao vươn lên trên mái phố là «con mắt» của đội cứu hoả: người trực trên đỉnh tháp quan sát toàn thành phố để phát hiện khói lửa và báo động kịp thời. Toà tháp gạch của Blagoveshchensk với hình khối đặc trưng và phần vọng gác trên cao đã trở thành một điểm mốc kiến trúc quen thuộc, được người dân xem như một phần di sản đô thị. Nằm trên phố Amurskaya trung tâm, tháp cứu hoả là một điểm dừng thú vị cho những ai quan tâm tới lịch sử và kiến trúc cổ của thành phố, bổ sung cho bức tranh về một Blagoveshchensk giao thương sầm uất thuở ban đầu bên dòng sông biên giới.",
    [
        "Tháp canh cứu hoả bằng gạch lịch sử từ đầu thế kỷ 20.",
        "Một trong những công trình kiến trúc cổ đặc trưng của Blagoveshchensk.",
        "Gợi nhớ thời kỳ thành phố thương mại gỗ phồn thịnh bên sông Amur.",
    ],
    {
        "hours_vi": "Ngắm kiến trúc từ bên ngoài (tuỳ thời điểm có thể không mở vào trong).",
        "ticket_vi": "Miễn phí khi ngắm từ ngoài.",
        "duration_vi": "Khoảng 10–15 phút.",
        "best_time_vi": "Ban ngày để ngắm rõ chi tiết kiến trúc.",
        "tips_vi": "Kết hợp dạo phố trung tâm lịch sử; hỏi thông tin địa phương nếu muốn vào bên trong.",
    },
    [
        {"title": "Yandex Maps — Пожарная каланча, Благовещенск", "url": "https://yandex.ru/maps/77/blagoveshchensk/"},
        {"title": "Wikipedia (RU) — Благовещенск", "url": "https://ru.wikipedia.org/wiki/Благовещенск"},
    ],
    ["fire-tower", "historic-architecture", "landmark", "blagoveshchensk", "heritage"],
    maps_text("Пожарная каланча", "Благовещенск", "Historic Fire Watchtower", "Blagoveshchensk", 50.260858, 127.555442),
))

# 25) Свободненский краеведческий музей им. Н. И. Попова ---------------------------
RECORDS.append(rec(
    "svobodny-museum",
    "Bảo tàng địa phương Svobodny mang tên N. I. Popov",
    "Свободненский краеведческий музей имени Н. И. Попова",
    "Svobodny Museum of Local Lore",
    ["museum"],
    51.378998, 128.134268,
    "Ул. Зейская, 43, thành phố Svobodny, tỉnh Amur, Nga.",
    "Bảo tàng địa phương của thành phố Svobodny, lưu giữ lịch sử vùng bắc-trung Amur, tuyến đường sắt và câu chuyện của một trong những đô thị lớn của tỉnh. Điểm tìm hiểu văn hoá địa phương bên ngoài thủ phủ Blagoveshchensk.",
    "Bảo tàng địa phương Svobodny mang tên nhà nghiên cứu N. I. Popov là nơi lưu giữ ký ức của thành phố Svobodny và vùng phụ cận — một trong những đô thị lớn và quan trọng của tỉnh Amur, từng phát triển mạnh nhờ vị trí trên tuyến đường sắt. Bộ sưu tập của bảo tàng dẫn khách qua nhiều lớp lịch sử: thiên nhiên và địa chất của vùng, đời sống của cư dân bản địa và những người khai hoang, quá trình hình thành thành phố quanh nhà ga, những biến động của thế kỷ 20 và cả giai đoạn hiện đại khi vùng đất này gắn với sân bay vũ trụ Vostochny gần đó. Qua các hiện vật, tài liệu, ảnh và mô hình, bảo tàng giúp du khách hiểu về nhịp sống và bản sắc của một thành phố tỉnh lỵ vùng Viễn Đông. Với những ai muốn khám phá Amur sâu hơn, vượt ra ngoài thủ phủ Blagoveshchensk, đây là điểm dừng chân giá trị để cảm nhận lịch sử địa phương một cách chân thực và gần gũi.",
    [
        "Bảo tàng địa phương của Svobodny — một trong những đô thị lớn của tỉnh Amur.",
        "Trưng bày thiên nhiên, lịch sử khai hoang, đường sắt và thời hiện đại của vùng.",
        "Điểm tìm hiểu văn hoá địa phương bên ngoài thủ phủ Blagoveshchensk.",
    ],
    {
        "hours_vi": "Thường mở thứ Ba–Chủ nhật, giờ hành chính; nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa giá bình dân; có tour hướng dẫn.",
        "duration_vi": "Khoảng 1 giờ.",
        "best_time_vi": "Quanh năm (bảo tàng trong nhà).",
        "tips_vi": "Kết hợp tham quan Nhà thờ Thánh Nikolai và trung tâm Svobodny; tiện khi trên đường tới vùng Vostochny.",
    },
    [
        {"title": "Yandex Maps — Свободненский краеведческий музей им. Н. И. Попова", "url": "https://yandex.ru/maps/11/svobodny/"},
        {"title": "Wikipedia (RU) — Свободный (город)", "url": "https://ru.wikipedia.org/wiki/Свободный_(город)"},
    ],
    ["museum", "local-history", "svobodny", "railway", "amur"],
    maps_text("Свободненский краеведческий музей", "Свободный", "Svobodny Museum of Local Lore", "Svobodny", 51.378998, 128.134268),
))


def main():
    path = os.path.join(REGIONS, f"{REGION}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    existing_slugs = {p.get("slug") for p in data}
    existing_ids = {p.get("id") for p in data}

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
