# -*- coding: utf-8 -*-
"""_add_places_lipetsk_20260728_220519.py — VÙNG: Tỉnh Lipetsk (Липецкая область)
(lần chạy tự động 2026-07-28).

Bối cảnh: lipetsk.json hiện có 7 địa điểm (Yelets, Tu viện Zadonsk, Kudykina Gora,
Galichya Gora, Nhà thờ Thăng Thiên Yelets, Nizhny Park, Voргольские скалы). Bổ sung 24
địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại hình → đưa vùng lên 31.

Trung tâm là thành phố Lipetsk (thành phố spa/nước khoáng) và thành phố cổ Yelets.

Phân bố loại hình (24 bản ghi mới):
- church (6): Христорождественский собор (Липецк), Древне-Успенская церковь/Успенский
  монастырь (Липецк), Сезёновский Иоанно-Казанский монастырь, Елецкий Знаменский монастырь,
  Троекуровский монастырь, Великокняжеская церковь (Елец).
- museum (4): Липецкий обл. краеведческий музей, Дом-музей Т. Н. Хренникова (Елец),
  Музей И. А. Бунина (Елец), Музей народных ремёсел и промыслов/кружево (Елец).
- theatre (1): Липецкий театр драмы им. Л. Н. Толстого.
- park_garden (5): Матырское водохранилище, Быханов сад, Верхний парк (Липецк),
  Липецкий зоопарк, Комсомольский пруд (Липецк).
- park_garden+other (1): Аргамач-Пальна (khu du lịch mạo hiểm gần Елец).
- palace/other (2): Усадьба Скорняково-Архангельское, Замок Борки.
- monument (2): Шуховская башня (Полибино), Памятник Петру I (Липецк).
- square_street (3): Соборная площадь (Липецк), Данков (город), Чаплыгин/Раненбург (город).

TOẠ ĐỘ — xác minh chéo qua ru.wikipedia coordinates API (prop=coordinates) và
OpenStreetMap/Nominatim (2026-07-28). Phạm vi Lipetsk lat ~51,8–53,6; lon ~37,8–40,8 —
tất cả toạ độ trong phạm vi, KHÔNG đảo lat/lon:
  Христорождественский собор 52.6095028,39.6007139 (ru.wiki Собор Рождества Христова);
  Успенский монастырь/Древне-Успенская церковь 52.6123587,39.6100351 (OSM, ул.Салтыкова-Щедрина);
  краеведческий музей 52.6141872,39.6082404 (OSM, ул.Ленина 25); театр драмы 52.6050597,39.5906264
  (OSM, Театральная пл.2); Матырское вдхр 52.5839,39.7478 (ru.wiki); Сезёновский м-рь
  53.075967,39.3128 (ru.wiki); Елецкий Знаменский м-рь 52.6379,38.49782 (ru.wiki); Полибино/
  Шуховская башня 53.5025,38.97639 (ru.wiki Полибино, Данковский р-н); Аргамач-Пальна
  52.68083,38.59528 (ru.wiki); Быханов сад 52.61889,39.59056 (ru.wiki); Данков 53.25,39.15
  (ru.wiki); Дом-музей Хренникова 52.6274,38.5051 (ru.wiki); Липецкий зоопарк 52.604799,39.607715
  (ru.wiki); Троекуровский м-рь 52.977491,38.974026 (ru.wiki); Верхний парк 52.61333,39.60917
  (ru.wiki); Великокняжеская церковь 52.6242107,38.5002014 (OSM, Yelets); Скорняково-Архангельское
  52.6807568,38.9149519 (OSM, гл.дом усадьбы); Музей Бунина 52.6187272,38.4937984 (OSM, ул.Горького 16);
  Замок Борки 52.15278,38.10972 (ru.wiki с.Борки, Тербунский р-н); Соборная площадь 52.608596,39.599551
  (ru.wiki); Музей народных ремёсел 52.6212563,38.4971203 (OSM, ул.Ленина 68, Yelets); Чаплыгин
  53.2430150,39.9668010 (OSM town); Комсомольский пруд 52.6063684,39.5966108 (OSM); Памятник Петру I
  52.6039947,39.6004404 (OSM, площадь Петра Великого).

GHI CHÚ: đã BỎ QUA vài đối tượng vì KHÔNG khớp toạ độ tin cậy trong công cụ: Тюнинский
Богородице-Тихоновский монастырь (không có node OSM/бài wiki tên rõ), «Дом Мастера»/
Художественный музей им. Сорокина (OSM không trả kết quả theo tên). KHÔNG bịa toạ độ.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_lipetsk_20260728_220519.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "lipetsk"
REGION_NAME_VI = "Tỉnh Lipetsk"
FD = "Vùng Trung tâm"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def osm_src(lat, lon):
    return {"title": "OpenStreetMap", "url": f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=17/{lat}/{lon}"}


def wiki_src(title_ru):
    return {"title": f"Wikipedia (RU) — {title_ru}", "url": "https://ru.wikipedia.org/wiki/" + urllib.parse.quote(title_ru.replace(' ', '_'))}


def wiki_search_src(q):
    return {"title": f"Wikipedia (RU) — tìm: {q}", "url": "https://ru.wikipedia.org/w/index.php?" + urllib.parse.urlencode({"search": q})}


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


def prac(hours, ticket, duration, best_time, tips):
    return {"hours_vi": hours, "ticket_vi": ticket, "duration_vi": duration,
            "best_time_vi": best_time, "tips_vi": tips}


RECORDS = []

# ================= THÀNH PHỐ LIPETSK =================

# 1) Христорождественский собор (Собор Рождества Христова), Липецк
RECORDS.append(rec(
    "christ-nativity-cathedral-lipetsk",
    "Nhà thờ chính tòa Giáng Sinh, Lipetsk (Khri-xtô-rô-giơ-đe-xtven-xki)",
    "Христорождественский собор (Собор Рождества Христова)",
    "Cathedral of the Nativity of Christ, Lipetsk",
    ["church"],
    52.6095028, 39.6007139,
    "Quảng trường Ленина-Соборная 4, trung tâm thành phố Lipetsk, tỉnh Lipetsk, Nga (trên đồi Nhà thờ, cạnh Ngọn lửa Vĩnh cửu).",
    "Nhà thờ chính tòa Giáng Sinh là biểu tượng của thành phố Lipetsk, tọa lạc trên đồi Nhà thờ giữa Quảng trường Ленина-Соборная. Công trình phong cách cổ điển với mái vòm vàng và tháp chuông cao được khởi công cuối thế kỷ 18, là điểm nhấn kiến trúc của toàn thành phố.",
    "Sừng sững trên đồi Nhà thờ (Соборная гора) ở tim thành phố Lipetsk, Nhà thờ chính tòa Giáng Sinh (Христорождественский собор) là công trình tôn giáo lớn nhất và cũng là biểu tượng quen thuộc của thủ phủ tỉnh. Được xây dựng theo phong cách cổ điển Nga trong khoảng thời gian dài từ cuối thế kỷ 18 sang thế kỷ 19, nhà thờ gồm khối chính đội mái vòm vàng cùng tháp chuông nhiều tầng vươn cao, có thể nhìn thấy từ nhiều nơi trong thành phố. Từng bị đóng cửa và sử dụng làm nơi khác trong thời Xô Viết, đến cuối thế kỷ 20 nhà thờ được trả lại cho Giáo hội, trùng tu và trở thành nhà thờ chính tòa của giáo phận Lipetsk. Nằm ngay cạnh là Quảng trường Ленина-Соборная với Ngọn lửa Vĩnh cửu và đài tưởng niệm, nên khu vực này vừa là trung tâm tâm linh vừa là trung tâm lễ hội, tụ họp của người dân. Buổi tối khi lên đèn, mái vòm và tháp chuông tạo nên khung cảnh nổi bật giữa lòng thành phố.",
    [
        "Biểu tượng của Lipetsk: nhà thờ chính tòa mái vòm vàng trên đồi Nhà thờ.",
        "Kiến trúc cổ điển Nga với tháp chuông nhiều tầng vươn cao.",
        "Nằm ngay Quảng trường Ленина-Соборная cùng Ngọn lửa Vĩnh cửu - trung tâm thành phố.",
    ],
    prac(
        "Mở cửa hằng ngày theo giờ lễ, thường khoảng 7:00–19:00.",
        "Miễn phí vào cửa (khuyến khích quyên góp).",
        "Khoảng 30–45 phút.",
        "Quanh năm; đẹp vào các đại lễ Chính thống và buổi tối khi lên đèn.",
        "Ăn mặc kín đáo, nữ nên trùm khăn; kết hợp dạo Quảng trường Соборная và đồi Nhà thờ.",
    ),
    [wiki_src("Собор Рождества Христова (Липецк)"), osm_src(52.6095028, 39.6007139)],
    ["cathedral", "orthodox", "landmark", "lipetsk", "architecture"],
    maps_text("Христорождественский собор", "Липецк", "Cathedral of the Nativity of Christ", "Lipetsk", 52.6095028, 39.6007139),
))

# 2) Древне-Успенская церковь / Свято-Успенский Липецкий монастырь
RECORDS.append(rec(
    "dormition-church-lipetsk",
    "Nhà thờ cổ Đức Mẹ An Giấc và Tu viện Uspensky (U-xpen-xki)",
    "Древне-Успенская церковь (Свято-Успенский Липецкий монастырь)",
    "Ancient Dormition Church (Assumption Monastery), Lipetsk",
    ["church"],
    52.6123587, 39.6100351,
    "Ул. Салтыкова-Щедрина, khu Cây Đen (Древне-Успенская), thành phố Lipetsk, tỉnh Lipetsk, Nga (bên sườn dốc gần suối khoáng).",
    "Nhà thờ cổ Đức Mẹ An Giấc là công trình cổ nhất còn lại của thành phố Lipetsk, có từ khoảng cuối thế kỷ 17. Nằm nép bên sườn dốc gần các mạch nước khoáng, ngôi nhà thờ nhỏ bằng đá trắng là hạt nhân của Tu viện Uspensky ngày nay.",
    "Ẩn mình bên sườn dốc dẫn xuống công viên và các mạch nước khoáng, Nhà thờ cổ Đức Mẹ An Giấc (Древне-Успенская церковь) được xem là công trình lâu đời nhất còn tồn tại của thành phố Lipetsk, xây dựng vào khoảng cuối thế kỷ 17. Đây từng là nhà thờ của một đan viện nhỏ (Пароменский монастырь) gắn với truyền thống suối nước thánh của vùng. Trải qua nhiều thăng trầm - bị đóng cửa thời Xô Viết rồi được phục hồi - ngôi nhà thờ đá trắng khiêm nhường với mái vòm đơn sơ nay là trung tâm của Tu viện Uspensky (Свято-Успенский Липецкий монастырь) được tái lập. Kiến trúc mộc mạc kiểu Nga cổ, khuôn viên yên tĩnh cùng nguồn nước thánh gần đó khiến nơi này trở thành điểm hành hương và tham quan lịch sử đáng quý giữa lòng thành phố hiện đại. Du khách thường kết hợp ghé đây khi dạo bộ ở khu công viên và suối khoáng dưới chân đồi.",
    [
        "Công trình cổ nhất còn lại của thành phố Lipetsk (khoảng cuối thế kỷ 17).",
        "Kiến trúc nhà thờ đá trắng kiểu Nga cổ, mộc mạc và yên tĩnh.",
        "Hạt nhân của Tu viện Uspensky tái lập, gần nguồn nước thánh và công viên.",
    ],
    prac(
        "Mở cửa hằng ngày theo giờ lễ, thường khoảng 8:00–19:00.",
        "Miễn phí (có thể quyên góp tùy tâm).",
        "Khoảng 30–45 phút.",
        "Mùa ấm (tháng 5–9) khi khuôn viên và lối dạo bên suối đẹp nhất.",
        "Đi giày thoải mái vì đường dốc; kết hợp thăm suối khoáng và công viên dưới chân đồi.",
    ),
    [wiki_search_src("Древне-Успенская церковь Липецк"), osm_src(52.6123587, 39.6100351)],
    ["church", "monastery", "orthodox", "oldest", "lipetsk", "history"],
    maps_text("Свято-Успенский Липецкий монастырь", "Липецк", "Ancient Dormition Church", "Lipetsk", 52.6123587, 39.6100351),
))

# 3) Липецкий областной краеведческий музей
RECORDS.append(rec(
    "lipetsk-regional-museum",
    "Bảo tàng Địa phương học tỉnh Lipetsk",
    "Липецкий областной краеведческий музей",
    "Lipetsk Regional Museum of Local Lore",
    ["museum"],
    52.6141872, 39.6082404,
    "Ул. Ленина 25, thành phố Lipetsk, tỉnh Lipetsk, Nga (khu phố cổ, gần đồi Nhà thờ).",
    "Bảo tàng Địa phương học tỉnh Lipetsk là bảo tàng lâu đời và lớn nhất vùng, giới thiệu toàn cảnh thiên nhiên, lịch sử và văn hóa của tỉnh - từ thời Pyotr Đại đế lập các xưởng luyện sắt tới khu điều dưỡng nước khoáng và công nghiệp hiện đại.",
    "Nằm trong một tòa nhà cổ trên phố Ленина ở trung tâm lịch sử Lipetsk, Bảo tàng Địa phương học tỉnh (Липецкий областной краеведческий музей) là bảo tàng chủ đạo của vùng, với lịch sử hình thành từ đầu thế kỷ 20. Các gian trưng bày dẫn dắt du khách qua nhiều lớp lịch sử: hệ động thực vật và địa chất của vùng thảo nguyên rừng, thời kỳ Pyotr Đại đế cho lập các xưởng luyện gang bên sông (khởi nguồn của thành phố), sự ra đời của khu điều dưỡng nước khoáng Lipetsk đầu thế kỷ 19, đời sống thương nhân - nông dân, cho tới thời kỳ công nghiệp hóa với tổ hợp luyện kim khổng lồ. Bộ sưu tập phong phú gồm cổ vật khảo cổ, tiền xu, trang phục, đồ thủ công, tài liệu và hiện vật về các danh nhân gắn với vùng đất. Đây là điểm khởi đầu lý tưởng để hiểu về Lipetsk trước khi khám phá thành phố, phù hợp với mọi lứa tuổi.",
    [
        "Bảo tàng chủ đạo, lâu đời nhất tỉnh Lipetsk với bộ sưu tập phong phú.",
        "Kể trọn hành trình từ xưởng luyện sắt thời Pyotr tới khu spa nước khoáng và công nghiệp.",
        "Vị trí trung tâm trên phố Ленина, gần đồi Nhà thờ và khu phố cổ.",
    ],
    prac(
        "Thường 10:00–18:00; nghỉ thứ Hai (nên kiểm tra trước).",
        "Vé khoảng 150–300 RUB; có ưu đãi cho học sinh, người cao tuổi.",
        "Khoảng 1–2 giờ.",
        "Quanh năm; thuận tiện kết hợp tham quan trung tâm thành phố.",
        "Kết hợp thăm Nhà thờ Giáng Sinh và Quảng trường Соборная gần đó.",
    ),
    [wiki_search_src("Липецкий областной краеведческий музей"), osm_src(52.6141872, 39.6082404)],
    ["museum", "history", "local-lore", "lipetsk", "culture"],
    maps_text("Липецкий областной краеведческий музей", "Липецк", "Lipetsk Regional Museum of Local Lore", "Lipetsk", 52.6141872, 39.6082404),
))

# 4) Липецкий театр драмы им. Л. Н. Толстого
RECORDS.append(rec(
    "lipetsk-drama-theatre",
    "Nhà hát kịch Lipetsk mang tên Lev Tolstoy",
    "Липецкий государственный академический театр драмы имени Л. Н. Толстого",
    "Lipetsk State Academic Drama Theatre named after Leo Tolstoy",
    ["theatre"],
    52.6050597, 39.5906264,
    "Quảng trường Театральная 2, thành phố Lipetsk, tỉnh Lipetsk, Nga.",
    "Nhà hát kịch quốc gia Lipetsk mang tên đại văn hào Lev Tolstoy là sân khấu kịch nói hàng đầu của tỉnh. Tọa lạc tại Quảng trường Театральная, nhà hát nổi tiếng với liên hoan sân khấu quốc tế mang tên Tolstoy tổ chức thường niên.",
    "Là trung tâm đời sống sân khấu của tỉnh, Nhà hát kịch quốc gia Lipetsk mang tên L. N. Tolstoy (Липецкий театр драмы им. Л. Н. Толстого) có bề dày lịch sử từ giữa thế kỷ 20 và được phong danh hiệu 'hàn lâm' nhờ chất lượng nghệ thuật. Tòa nhà hát bề thế ngự trên Quảng trường Театральная, là điểm nhấn kiến trúc của khu vực. Sân khấu dàn dựng đa dạng từ kịch kinh điển Nga và thế giới đến các vở đương đại, phục vụ cả khán giả lớn tuổi lẫn trẻ em. Điểm đặc biệt khiến nhà hát nổi tiếng cả nước là Liên hoan Sân khấu Quốc tế mang tên Lev Tolstoy - nơi quy tụ các đoàn kịch trong và ngoài nước, gắn với di sản của văn hào từng sống và sáng tác ở vùng đất lân cận. Với người yêu nghệ thuật, một buổi tối xem kịch tại đây là cách thú vị để cảm nhận nhịp sống văn hóa của Lipetsk.",
    [
        "Sân khấu kịch nói hàng đầu tỉnh, mang tên đại văn hào Lev Tolstoy.",
        "Tòa nhà hát bề thế trên Quảng trường Театральная - điểm nhấn kiến trúc.",
        "Nổi tiếng với Liên hoan Sân khấu Quốc tế mang tên Tolstoy.",
    ],
    prac(
        "Phòng vé mở ban ngày; suất diễn thường bắt đầu 18:00–19:00, nghỉ hè giữa mùa.",
        "Vé thường khoảng 300–1.000 RUB tùy vở và vị trí.",
        "Một buổi diễn khoảng 2–3 giờ.",
        "Mùa diễn từ thu đến xuân; dịp liên hoan Tolstoy đặc biệt sôi động.",
        "Đặt vé trước qua phòng vé/website; đến sớm để tham quan sảnh nhà hát.",
    ),
    [wiki_search_src("Липецкий театр драмы имени Толстого"), osm_src(52.6050597, 39.5906264)],
    ["theatre", "drama", "culture", "lipetsk", "tolstoy"],
    maps_text("Липецкий театр драмы им. Л. Н. Толстого", "Липецк", "Lipetsk Drama Theatre", "Lipetsk", 52.6050597, 39.5906264),
))

# 5) Матырское водохранилище
RECORDS.append(rec(
    "matyrskoye-reservoir",
    "Hồ chứa Matyrskoye (Ma-tư-rơ-xkô-e)",
    "Матырское водохранилище",
    "Matyrskoye Reservoir",
    ["park_garden"],
    52.5839, 39.7478,
    "Trên sông Матыра, phía đông nam thành phố Lipetsk (giáp thành phố và huyện Gryazinsky), tỉnh Lipetsk, Nga.",
    "Matyrskoye là hồ chứa nhân tạo lớn nhất tỉnh Lipetsk, được tạo thành trên sông Matyra để cấp nước cho tổ hợp luyện kim. Ngày nay hồ là điểm nghỉ dưỡng, tắm mát, câu cá và thể thao dưới nước yêu thích của cư dân thành phố.",
    "Trải rộng ở phía đông nam Lipetsk, Hồ chứa Matyrskoye (Матырское водохранилище) hình thành khi người ta đắp đập trên sông Matyra vào thập niên 1970 để phục vụ nhu cầu nước của tổ hợp luyện kim Novolipetsk. Với chiều dài hàng chục ki-lô-mét và diện tích mặt nước rộng lớn, hồ nhanh chóng trở thành 'biển' của người Lipetsk - nơi nghỉ ngơi cuối tuần lý tưởng. Dọc bờ hồ là các bãi tắm, khu nghỉ dưỡng, trại hè, bến thuyền và những điểm câu cá đông đúc vào mùa hè. Du khách có thể tắm mát, chèo thuyền, đi mô-tô nước, câu cá hay đơn giản là dã ngoại dưới tán cây ven bờ. Vào mùa đông, mặt hồ đóng băng thu hút người câu cá trên băng. Hệ sinh thái quanh hồ cũng khá phong phú với nhiều loài chim nước. Đây là điểm đến gần gũi, dễ tiếp cận cho những ai muốn kết hợp tham quan thành phố với thư giãn bên mặt nước.",
    [
        "Hồ chứa nhân tạo lớn nhất tỉnh - 'biển' nghỉ dưỡng của người Lipetsk.",
        "Bãi tắm, bến thuyền, câu cá và thể thao dưới nước sôi động mùa hè.",
        "Cảnh quan ven bờ và chim nước phong phú; câu cá trên băng mùa đông.",
    ],
    prac(
        "Khu vực mặt nước và bờ hồ mở tự do; các bãi tắm/khu dịch vụ hoạt động ban ngày.",
        "Vào các bãi tắm công cộng thường miễn phí; một số dịch vụ (thuyền, mô-tô nước) tính phí.",
        "Nửa ngày đến trọn ngày.",
        "Mùa hè (tháng 6–8) để tắm và thể thao nước; mùa đông cho câu cá trên băng.",
        "Mang đồ bơi, kem chống nắng; chú ý an toàn khi bơi và tuân thủ khu vực cho phép.",
    ),
    [wiki_src("Матырское водохранилище"), osm_src(52.5839, 39.7478)],
    ["reservoir", "lake", "beach", "fishing", "recreation", "nature"],
    maps_text("Матырское водохранилище", "Липецкая область", "Matyrskoye Reservoir", "Lipetsk Oblast", 52.5839, 39.7478),
))

# 6) Сезёновский Иоанно-Казанский монастырь
RECORDS.append(rec(
    "sezyonovo-monastery",
    "Tu viện Ioanno-Kazansky ở Sezyonovo (Xê-di-ô-nốp)",
    "Сезёновский Иоанно-Казанский монастырь",
    "Sezyonovo St John–Kazan Convent",
    ["church"],
    53.075967, 39.3128,
    "Làng Сезёново, huyện Lebedyansky, tỉnh Lipetsk, Nga (phía bắc tỉnh).",
    "Tu viện nữ Ioanno-Kazansky ở làng Sezyonovo là một trung tâm hành hương nổi bật phía bắc tỉnh Lipetsk, gắn với vị ẩn tu được tôn kính Ioann Sezyonovsky. Quần thể nổi bật với nhà thờ chính đồ sộ và tháp chuông cao vươn lên giữa vùng đồng quê.",
    "Ở làng Сезёново thuộc huyện Lebedyansky phía bắc tỉnh Lipetsk, Tu viện nữ Ioanno-Kazansky (Сезёновский Иоанно-Казанский монастырь) là một điểm hành hương Chính thống giáo quan trọng của vùng. Tu viện gắn liền với thánh nhân Ioann Sezyonovsky - một vị ẩn tu (затворник) được người dân hết mực tôn kính từ đầu thế kỷ 19; chính quanh nơi ông tu hành mà cộng đồng nữ tu hình thành và phát triển thành tu viện. Quần thể kiến trúc gây ấn tượng với ngôi nhà thờ chính (собор) đồ sộ mang phong cách cổ điển - Nga cùng tháp chuông cao vươn lên giữa khung cảnh đồng quê thanh bình. Sau thời gian bị đóng cửa và hư hại trong thời Xô Viết, tu viện được khôi phục và đón khách hành hương trở lại. Du khách tìm đến đây để chiêm bái, cầu nguyện, lấy nước thánh và tận hưởng bầu không khí tĩnh lặng, tách biệt khỏi phố thị. Đây cũng là điểm dừng đáng giá trên hành trình khám phá vùng Lebedyan cổ kính.",
    [
        "Trung tâm hành hương gắn với thánh ẩn tu Ioann Sezyonovsky.",
        "Nhà thờ chính đồ sộ và tháp chuông cao giữa khung cảnh đồng quê.",
        "Không gian tu viện tĩnh lặng, có nguồn nước thánh cho khách hành hương.",
    ],
    prac(
        "Mở cửa hằng ngày cho khách hành hương theo giờ lễ (sáng và chiều).",
        "Miễn phí vào cửa (có thể quyên góp).",
        "Khoảng 1 giờ.",
        "Mùa ấm (tháng 5–9); các dịp lễ lớn đông khách hành hương.",
        "Ăn mặc kín đáo, nữ mang khăn trùm; mang chai lấy nước thánh, kết hợp thăm Lebedyan.",
    ),
    [wiki_src("Сезёновский Иоанно-Казанский монастырь"), osm_src(53.075967, 39.3128)],
    ["monastery", "convent", "orthodox", "pilgrimage", "bell-tower", "lebedyan"],
    maps_text("Сезёновский Иоанно-Казанский монастырь", "Липецкая область", "Sezyonovo Convent", "Lipetsk Oblast", 53.075967, 39.3128),
))

# 7) Елецкий Знаменский монастырь
RECORDS.append(rec(
    "yelets-znamensky-convent",
    "Tu viện Znamensky (Dấu Chỉ Đức Mẹ), Yelets",
    "Елецкий Знаменский монастырь",
    "Znamensky Convent, Yelets",
    ["church"],
    52.6379, 38.49782,
    "Đồi Kamennaya Gora, phố Слободская, thành phố Yelets, tỉnh Lipetsk, Nga (trên cao nhìn xuống sông Bystraya Sosna).",
    "Tu viện nữ Znamensky ngự trên đồi Kamennaya Gora ở Yelets, nhìn xuống sông Bystraya Sosna. Được lập từ thế kỷ 17, đây là một trong những tu viện đẹp và linh thiêng nhất thành phố cổ, với tầm nhìn toàn cảnh khu phố cổ và nguồn nước thánh dưới chân đồi.",
    "Tọa lạc trên đồi Đá (Каменная гора) ở thành phố cổ Yelets, Tu viện nữ Znamensky (Елецкий Знаменский монастырь) là một trong những điểm tâm linh và thắng cảnh đẹp nhất của phố cổ ngàn năm. Nguồn gốc tu viện có từ thế kỷ 17, ban đầu là một đan viện nam rồi chuyển thành tu viện nữ vào thế kỷ 18. Từ trên đồi, du khách phóng tầm mắt bao quát toàn cảnh Yelets với những mái vòm nhà thờ, dòng sông Bystraya Sosna uốn lượn và khu phố thương gia cổ kính. Trong thời Xô Viết tu viện bị đóng cửa và tàn phá nặng nề, nhưng từ cuối thế kỷ 20 đã được khôi phục công phu với nhà thờ, tháp chuông, các dãy nhà tu và tường bao trắng muốt. Dưới chân đồi có nguồn nước thánh được người dân và khách hành hương lui tới. Sự kết hợp giữa giá trị tâm linh, kiến trúc được phục dựng và vị trí ngắm cảnh tuyệt đẹp khiến nơi đây trở thành điểm dừng không thể bỏ qua khi ghé Yelets.",
    [
        "Tu viện nữ trên đồi Đá, ngắm toàn cảnh phố cổ Yelets và sông Bystraya Sosna.",
        "Lịch sử từ thế kỷ 17, được phục dựng công phu sau thời Xô Viết.",
        "Nguồn nước thánh dưới chân đồi thu hút khách hành hương.",
    ],
    prac(
        "Mở cửa hằng ngày cho khách hành hương theo giờ lễ.",
        "Miễn phí vào cửa (có thể quyên góp).",
        "Khoảng 45–60 phút.",
        "Mùa ấm (tháng 5–9); buổi sáng đẹp cho ảnh toàn cảnh.",
        "Đường lên đồi hơi dốc; ăn mặc kín đáo, nữ mang khăn; kết hợp dạo phố cổ Yelets.",
    ),
    [wiki_src("Елецкий Знаменский монастырь"), osm_src(52.6379, 38.49782)],
    ["convent", "monastery", "orthodox", "yelets", "viewpoint", "old-town"],
    maps_text("Елецкий Знаменский монастырь", "Елец", "Znamensky Convent", "Yelets", 52.6379, 38.49782),
))

# 8) Шуховская башня в Полибино (усадьба Нечаевых)
RECORDS.append(rec(
    "shukhov-tower-polibino",
    "Tháp Shukhov ở Polibino (Su-khốp / Pô-li-bi-nô)",
    "Шуховская (гиперболоидная) башня в Полибино",
    "Shukhov Hyperboloid Tower in Polibino",
    ["monument"],
    53.5025, 38.97639,
    "Làng Полибино, huyện Dankovsky, tỉnh Lipetsk, Nga (trong khuôn viên điền trang Nechaev, phía bắc tỉnh).",
    "Tháp Shukhov ở Polibino là tháp kết cấu hyperboloid lưới thép đầu tiên trên thế giới, do kỹ sư thiên tài Vladimir Shukhov dựng năm 1896. Đứng trong khuôn viên điền trang Nechaev, ngọn tháp là một cột mốc của lịch sử kiến trúc - kỹ thuật nhân loại.",
    "Giữa vùng quê phía bắc tỉnh Lipetsk, tại làng Полибино, đứng sừng sững một công trình có ý nghĩa toàn cầu: Tháp Shukhov - tháp lưới thép kết cấu hyperboloid (một mặt cong tạo từ các thanh thẳng) đầu tiên trên thế giới. Kỹ sư - nhà phát minh lỗi lạc Vladimir Shukhov trình làng kết cấu này tại Triển lãm toàn Nga ở Nizhny Novgorod năm 1896; sau triển lãm, nhà công nghiệp - chủ điền trang Yuri Nechaev-Maltsev đã mua lại và cho dựng ngọn tháp trong khuôn viên điền trang Polibino của mình. Với thiết kế nhẹ, chắc và thanh thoát đến bất ngờ, nguyên lý hyperboloid của Shukhov về sau được ứng dụng khắp thế giới cho tháp truyền hình, cột nước, cột buồm và nhà chọc trời. Bên cạnh tháp là quần thể điền trang Nechaev cổ kính - nơi từng đón tiếp nhiều danh nhân văn hóa Nga. Sau nhiều năm xuống cấp, ngọn tháp đã được trùng tu và trở thành điểm hành hương của giới kiến trúc, kỹ thuật cùng du khách yêu lịch sử. Đây thực sự là một 'báu vật kỹ thuật' hiếm có của nước Nga.",
    [
        "Tháp kết cấu hyperboloid lưới thép ĐẦU TIÊN trên thế giới (V. Shukhov, 1896).",
        "Cột mốc lịch sử kiến trúc - kỹ thuật, nguyên lý sau này lan ra toàn cầu.",
        "Nằm trong khuôn viên điền trang Nechaev cổ kính ở làng Polibino.",
    ],
    prac(
        "Khu vực ngoài trời, tham quan ban ngày; điền trang có thể cần liên hệ trước.",
        "Tham quan tháp thường miễn phí; một số hoạt động/khu điền trang có thể thu phí.",
        "Khoảng 1–1,5 giờ.",
        "Cuối xuân đến đầu thu (tháng 5–9); ngày khô ráo để chụp ảnh tháp.",
        "Đường tới làng khá xa, nên đi xe riêng/tour; kết hợp thăm thành phố Dankov gần đó.",
    ),
    [wiki_src("Полибино (Данковский район)"), osm_src(53.5025, 38.97639)],
    ["shukhov", "hyperboloid", "engineering", "monument", "estate", "polibino"],
    maps_text("Шуховская башня в Полибино", "Липецкая область", "Shukhov Tower Polibino", "Lipetsk Oblast", 53.5025, 38.97639),
))

# 9) Аргамач-Пальна
RECORDS.append(rec(
    "argamach-palna",
    "Công viên du lịch Argamach-Palna (Ạc-ga-mách Pan-na)",
    "Аргамач-Пальна",
    "Argamach-Palna Nature & Adventure Park",
    ["park_garden", "other"],
    52.68083, 38.59528,
    "Làng Аргамач-Пальна, huyện Yeletsky, tỉnh Lipetsk, Nga (bên bờ sông Пальна, gần Yelets).",
    "Argamach-Palna là khu du lịch sinh thái - mạo hiểm nằm bên bờ sông Palna gần Yelets, nổi tiếng với vách đá vôi, hang động, khu khảo cổ và các hoạt động ngoài trời. Đây là điểm đến kết hợp thiên nhiên, khảo cổ và trải nghiệm phiêu lưu cho gia đình và giới trẻ.",
    "Bên bờ sông Пальна quanh co, cách thành phố cổ Yelets không xa, khu Аргамач-Пальна là một trong những điểm du lịch sinh thái - mạo hiểm sống động nhất tỉnh Lipetsk. Cảnh quan nổi bật với những vách đá vôi, hang động nhỏ và thung lũng sông đẹp như tranh - dấu tích của một vùng địa chất cổ. Nơi đây còn có ý nghĩa khảo cổ khi phát lộ các di chỉ cư trú thời tiền sử; du khách có thể tham gia 'công viên khảo cổ' với những hoạt động phục dựng đời sống người xưa. Khu du lịch cung cấp đa dạng trải nghiệm: đi bộ đường mòn, leo vách đá, đu dây, bắn cung, chèo thuyền, cắm trại và các chương trình giáo dục - trại hè cho trẻ em. Có khu lưu trú, nhà gỗ và dịch vụ ăn uống phục vụ khách nghỉ qua đêm. Sự hòa quyện giữa thiên nhiên hoang sơ, chiều sâu khảo cổ và các hoạt động vận động khiến Argamach-Palna trở thành lựa chọn hấp dẫn cho gia đình, nhóm bạn và những ai ưa khám phá.",
    [
        "Vách đá vôi, hang động và thung lũng sông Palna đẹp như tranh gần Yelets.",
        "Công viên khảo cổ với di chỉ tiền sử và hoạt động phục dựng đời sống người xưa.",
        "Đa dạng trải nghiệm: leo núi, đu dây, bắn cung, cắm trại, trại hè cho trẻ em.",
    ],
    prac(
        "Khu du lịch mở ban ngày; nhiều hoạt động cần đăng ký trước, nhất là nhóm/trại hè.",
        "Vào khu vực có thể thu phí; các hoạt động và lưu trú tính phí riêng.",
        "Nửa ngày đến trọn ngày (có thể nghỉ qua đêm).",
        "Cuối xuân đến đầu thu (tháng 5–9) cho hoạt động ngoài trời.",
        "Đặt trước các chương trình; đi giày bám tốt, mang nước và đồ chống nắng.",
    ),
    [wiki_src("Аргамач-Пальна"), osm_src(52.68083, 38.59528)],
    ["nature", "adventure", "archaeology", "cliffs", "camping", "yelets"],
    maps_text("Аргамач-Пальна", "Липецкая область", "Argamach-Palna", "Lipetsk Oblast", 52.68083, 38.59528),
))

# 10) Быханов сад
RECORDS.append(rec(
    "bykhanov-garden-lipetsk",
    "Vườn Bykhanov (Bư-kha-nốp), Lipetsk",
    "Быханов сад",
    "Bykhanov Garden",
    ["park_garden"],
    52.61889, 39.59056,
    "Ул. Первомайская, thành phố Lipetsk, tỉnh Lipetsk, Nga.",
    "Vườn Bykhanov là một trong những công viên lâu đời và được yêu thích của Lipetsk, mang tên gia đình nhà làm vườn Bykhanov nổi tiếng. Đây là không gian xanh mát với cây cổ thụ, lối dạo, đài phun nước và các trò chơi giải trí giữa lòng thành phố.",
    "Nằm ở khu vực trung tâm Lipetsk, Vườn Bykhanov (Быханов сад) là công viên gắn với tên tuổi gia đình Bykhanov - những nhà làm vườn, ươm cây nổi tiếng của thành phố cuối thế kỷ 19, đầu thế kỷ 20, người đã góp phần phủ xanh Lipetsk. Trải qua thời gian, khu vườn trở thành một công viên văn hóa - nghỉ ngơi quen thuộc với người dân. Dưới những tán cây cổ thụ rợp bóng là các lối dạo bộ, thảm hoa, đài phun nước, sân chơi và khu trò chơi giải trí cho trẻ em. Công viên là nơi lý tưởng để đi dạo, tập thể dục buổi sáng, cho trẻ vui chơi hay đơn giản là tránh nắng hè. Vào các dịp lễ hội, đây thường là nơi diễn ra hoạt động cộng đồng, biểu diễn ngoài trời. Với không khí trong lành, bóng cây và vị trí thuận tiện, Vườn Bykhanov là một 'lá phổi xanh' được nhiều thế hệ cư dân Lipetsk gắn bó.",
    [
        "Công viên lâu đời mang tên gia đình làm vườn Bykhanov nổi tiếng của Lipetsk.",
        "Cây cổ thụ rợp bóng, lối dạo, đài phun nước và khu trò chơi trẻ em.",
        "Không gian nghỉ ngơi, thể dục và lễ hội quen thuộc của cư dân.",
    ],
    prac(
        "Mở cửa tự do hằng ngày; khu trò chơi hoạt động ban ngày đến tối.",
        "Vào cửa miễn phí; một số trò chơi tính phí.",
        "Khoảng 1–1,5 giờ.",
        "Mùa ấm (tháng 5–9) khi cây xanh và đài phun nước hoạt động.",
        "Kết hợp dạo trung tâm thành phố; mang tiền lẻ cho các trò chơi trẻ em.",
    ),
    [wiki_src("Быханов сад"), osm_src(52.61889, 39.59056)],
    ["park", "garden", "recreation", "family", "lipetsk", "green"],
    maps_text("Быханов сад", "Липецк", "Bykhanov Garden", "Lipetsk", 52.61889, 39.59056),
))

# 11) Данков
RECORDS.append(rec(
    "dankov-town",
    "Thị trấn cổ Dankov (Đan-cốp)",
    "Данков",
    "Dankov Town",
    ["square_street"],
    53.25, 39.15,
    "Thành phố Dankov, phía bắc tỉnh Lipetsk, Nga (bên sông Đông).",
    "Dankov là một thị trấn cổ bên sông Đông ở phía bắc tỉnh Lipetsk, có lịch sử từ thời trung cổ như một tiền đồn phòng thủ. Ngày nay thị trấn quyến rũ bởi nhịp sống chậm, những nhà thờ cổ, bảo tàng địa phương và khung cảnh sông nước yên bình.",
    "Bên dòng sông Đông ở cực bắc tỉnh Lipetsk, Dankov (Данков) là một trong những đô thị lâu đời của vùng, khởi nguồn từ thời trung cổ như một pháo đài canh giữ biên cương phía nam nước Nga trước các cuộc xâm nhập của quân du mục. Trải qua nhiều biến động, thị trấn nhỏ hồi sinh vào thế kỷ 18–19 thành một trung tâm buôn bán và thủ công của vùng thượng nguồn sông Đông. Dạo bước trong Dankov hôm nay, du khách bắt gặp những dãy phố tỉnh lẻ yên tĩnh, các nhà thờ Chính thống cổ như nhà thờ Tikhvin, quảng trường trung tâm và bảo tàng địa phương lưu giữ ký ức vùng đất - trong đó có cả bộ sưu tập mỹ thuật đáng ngạc nhiên. Khung cảnh sông Đông thanh bình, những mái vòm nhà thờ và nhịp sống chậm rãi tạo nên sức hút mộc mạc, hoài niệm. Dankov cũng là điểm khởi đầu thuận tiện để đến làng Polibino với tháp Shukhov nổi tiếng gần đó.",
    [
        "Thị trấn cổ bên sông Đông, khởi nguồn là pháo đài phòng thủ trung cổ.",
        "Nhà thờ Chính thống cổ, quảng trường trung tâm và bảo tàng địa phương có sưu tập mỹ thuật.",
        "Nhịp sống chậm, cảnh sông nước yên bình; gần làng Polibino với tháp Shukhov.",
    ],
    prac(
        "Khu phố mở tự do; bảo tàng thường 10:00–17:00, nghỉ thứ Hai.",
        "Dạo phố miễn phí; vé bảo tàng khoảng 100–200 RUB.",
        "Khoảng 2–3 giờ.",
        "Cuối xuân đến đầu thu (tháng 5–9), thời tiết dễ chịu để đi bộ.",
        "Kết hợp thăm tháp Shukhov ở Polibino; mang giày thoải mái đi bộ.",
    ),
    [wiki_src("Данков"), osm_src(53.25, 39.15)],
    ["town", "history", "don-river", "old-town", "churches", "museum"],
    maps_text("Данков", "Липецкая область", "Dankov", "Lipetsk Oblast", 53.25, 39.15),
))

# 12) Дом-музей Т. Н. Хренникова (Елец)
RECORDS.append(rec(
    "khrennikov-house-museum-yelets",
    "Nhà lưu niệm nhạc sĩ Tikhon Khrennikov (Khren-ni-cốp)",
    "Дом-музей Т. Н. Хренникова",
    "Tikhon Khrennikov House Museum",
    ["museum"],
    52.6274, 38.5051,
    "Ул. Маяковского, thành phố Yelets, tỉnh Lipetsk, Nga (ngôi nhà nơi nhạc sĩ sinh ra).",
    "Nhà lưu niệm Tikhon Khrennikov ở Yelets là ngôi nhà nơi nhà soạn nhạc Xô Viết lừng danh chào đời. Bảo tàng tái hiện cuộc đời và sự nghiệp của ông qua đồ đạc gia đình, nhạc cụ, bản thảo và kỷ vật, giữa khung cảnh phố cổ Yelets.",
    "Tọa lạc trong một ngôi nhà thương gia cổ ở thành phố Yelets, Nhà lưu niệm Tikhon Khrennikov (Дом-музей Т. Н. Хренникова) tôn vinh người con nổi tiếng nhất của thành phố trong lĩnh vực âm nhạc - nhà soạn nhạc, người lãnh đạo Hội Nhạc sĩ Liên Xô suốt nhiều thập niên. Sinh năm 1913 chính tại ngôi nhà này, Khrennikov là tác giả của nhiều bản giao hưởng, nhạc kịch, ca khúc và nhạc phim quen thuộc với nhiều thế hệ khán giả Nga. Bảo tàng, mở cửa vào cuối thế kỷ 20 với sự tham gia của chính nhạc sĩ, tái hiện không gian sống của một gia đình thương gia tỉnh lẻ đầu thế kỷ 20 cùng hành trình sự nghiệp của ông: nội thất nguyên bản, cây đàn piano, bản thảo, thư từ, ảnh, giải thưởng và nhiều kỷ vật cá nhân. Đây là điểm đến giàu cảm xúc cho người yêu âm nhạc và những ai muốn hiểu thêm về đời sống văn hóa - trí thức của Yelets. Mộ phần của nhạc sĩ cũng nằm gần đó, trong khuôn viên ngôi nhà theo di nguyện.",
    [
        "Ngôi nhà nơi nhà soạn nhạc Xô Viết Tikhon Khrennikov chào đời (1913).",
        "Nội thất gia đình thương gia đầu thế kỷ 20, piano, bản thảo và kỷ vật.",
        "Điểm đến cho người yêu âm nhạc giữa lòng phố cổ Yelets.",
    ],
    prac(
        "Thường 10:00–18:00; nghỉ thứ Hai (nên kiểm tra trước).",
        "Vé khoảng 100–200 RUB; có ưu đãi cho học sinh.",
        "Khoảng 45–60 phút.",
        "Quanh năm; kết hợp tham quan phố cổ Yelets.",
        "Có thể yêu cầu hướng dẫn viên; kết hợp thăm Nhà thờ Thăng Thiên và bảo tàng Bunin gần đó.",
    ),
    [wiki_src("Дом-музей Т. Н. Хренникова"), osm_src(52.6274, 38.5051)],
    ["museum", "music", "composer", "khrennikov", "yelets", "memorial"],
    maps_text("Дом-музей Т. Н. Хренникова", "Елец", "Khrennikov House Museum", "Yelets", 52.6274, 38.5051),
))

# 13) Липецкий зоопарк
RECORDS.append(rec(
    "lipetsk-zoo",
    "Vườn thú Lipetsk",
    "Липецкий зоопарк",
    "Lipetsk Zoo",
    ["park_garden", "other"],
    52.604799, 39.607715,
    "Petrovsky proezd 2 (trong Công viên Hạ/Nizhny Park), thành phố Lipetsk, tỉnh Lipetsk, Nga.",
    "Vườn thú Lipetsk nằm trong khuôn viên Công viên Hạ lịch sử, là một trong những vườn thú lâu đời của vùng Trung tâm nước Nga. Nơi đây nuôi dưỡng hàng trăm loài động vật và là điểm tham quan yêu thích của các gia đình có trẻ nhỏ.",
    "Nằm gọn trong khuôn viên Công viên Hạ (Нижний парк) - khu điều dưỡng nước khoáng lịch sử của thành phố - Vườn thú Lipetsk (Липецкий зоопарк) được thành lập năm 1973 và dần phát triển thành một trong những vườn thú đáng chú ý của vùng Trung tâm. Trên diện tích không quá lớn nhưng bố trí gọn gàng, vườn thú nuôi dưỡng hàng trăm loài động vật từ khắp các châu lục: thú lớn như hổ, sư tử, gấu, linh trưởng, cùng nhiều loài chim, bò sát, thú móng guốc và động vật quý hiếm nằm trong Sách Đỏ. Vườn thú tham gia các chương trình bảo tồn, nhân giống và giáo dục môi trường, thường tổ chức hoạt động cho học sinh và gia đình. Với vị trí ngay trung tâm, dễ kết hợp cùng các điểm vui chơi của Công viên Hạ (đài phun nước, suối khoáng, trò chơi), đây là điểm đến quen thuộc và lý tưởng cho các gia đình có trẻ nhỏ khi ghé Lipetsk.",
    [
        "Vườn thú lâu đời (từ 1973) trong lòng Công viên Hạ lịch sử của Lipetsk.",
        "Hàng trăm loài động vật, gồm nhiều loài quý hiếm trong Sách Đỏ.",
        "Tham gia bảo tồn, nhân giống và giáo dục môi trường; hợp với gia đình.",
    ],
    prac(
        "Mở cửa hằng ngày, thường khoảng 9:00–20:00 mùa hè (mùa đông đóng sớm hơn).",
        "Vé khoảng 200–400 RUB; trẻ nhỏ ưu đãi/miễn phí tùy độ tuổi.",
        "Khoảng 1,5–2 giờ.",
        "Mùa ấm (tháng 5–9) khi nhiều loài được thả ra khu ngoài trời.",
        "Kết hợp tham quan Công viên Hạ; không cho thú ăn ngoài quy định.",
    ),
    [wiki_src("Липецкий зоопарк"), osm_src(52.604799, 39.607715)],
    ["zoo", "animals", "family", "conservation", "lipetsk", "park"],
    maps_text("Липецкий зоопарк", "Липецк", "Lipetsk Zoo", "Lipetsk", 52.604799, 39.607715),
))

# 14) Троекуровский (Иларионовский) монастырь
RECORDS.append(rec(
    "troekurovo-monastery",
    "Tu viện Troekurovo (Trô-e-cu-rốp)",
    "Дмитриевский Иларионовский Троекуровский монастырь",
    "Troekurovo (Ilarionovsky) Convent",
    ["church"],
    52.977491, 38.974026,
    "Làng Троекурово, huyện Lebedyansky, tỉnh Lipetsk, Nga.",
    "Tu viện nữ Troekurovo ở huyện Lebedyansky gắn với vị ẩn tu được tôn kính Ilarion Troekurovsky. Quần thể tu viện với nhà thờ nhiều mái vòm và tháp chuông là một trung tâm hành hương thanh tịnh của vùng thượng lưu sông Đông.",
    "Ở làng Троекурово thuộc huyện Lebedyansky, Tu viện nữ Troekurovo (Дмитриевский Иларионовский Троекуровский монастырь) là một điểm hành hương Chính thống giáo được người dân vùng thượng lưu sông Đông tôn kính. Tu viện gắn liền với thánh Ilarion Troekurovsky - một vị ẩn tu (затворник) sống khổ hạnh vào thế kỷ 19 và được ngưỡng mộ vì đời sống tâm linh sâu sắc; cộng đồng tu hành hình thành quanh nơi ông ẩn tu rồi phát triển thành tu viện. Quần thể gồm các nhà thờ với những mái vòm xanh - vàng, tháp chuông và dãy nhà tu nằm giữa khung cảnh đồng quê yên ả. Sau thời kỳ bị đóng cửa và hư hại dưới thời Xô Viết, tu viện được khôi phục và đón khách hành hương trở lại, gìn giữ xá lợi cùng truyền thống cầu nguyện. Không gian tĩnh lặng, khuôn viên chăm chút và bầu không khí thành kính khiến nơi đây trở thành điểm dừng chân thanh thản, thường được kết hợp trong hành trình khám phá vùng Lebedyan và các tu viện lân cận.",
    [
        "Tu viện nữ gắn với thánh ẩn tu Ilarion Troekurovsky (thế kỷ 19).",
        "Nhà thờ mái vòm xanh - vàng và tháp chuông giữa đồng quê Lebedyan.",
        "Trung tâm hành hương thanh tịnh, gìn giữ xá lợi và truyền thống cầu nguyện.",
    ],
    prac(
        "Mở cửa hằng ngày cho khách hành hương theo giờ lễ.",
        "Miễn phí vào cửa (có thể quyên góp).",
        "Khoảng 45–60 phút.",
        "Mùa ấm (tháng 5–9); các dịp lễ lớn đông khách hành hương.",
        "Ăn mặc kín đáo, nữ mang khăn; kết hợp thăm tu viện Sezyonovo và Lebedyan.",
    ),
    [wiki_src("Троекуровский монастырь"), osm_src(52.977491, 38.974026)],
    ["convent", "monastery", "orthodox", "pilgrimage", "lebedyan", "relics"],
    maps_text("Троекуровский монастырь", "Липецкая область", "Troekurovo Convent", "Lipetsk Oblast", 52.977491, 38.974026),
))

# 15) Верхний парк (Липецк)
RECORDS.append(rec(
    "verkhny-park-lipetsk",
    "Công viên Thượng (Verkhny Park), Lipetsk",
    "Верхний парк",
    "Verkhny (Upper) Park, Lipetsk",
    ["park_garden"],
    52.61333, 39.60917,
    "Trung tâm thành phố Lipetsk (trên đồi, nối với đồi Nhà thờ), tỉnh Lipetsk, Nga.",
    "Công viên Thượng là công viên trên cao ở trung tâm Lipetsk, đối lại với Công viên Hạ dưới chân đồi. Đây là không gian dạo bộ, ngắm cảnh thành phố với các lối đi rợp bóng cây, đài quan sát và những góc lãng mạn được người dân yêu thích.",
    "Trải trên vùng đất cao ở trung tâm Lipetsk, Công viên Thượng (Верхний парк) tạo thành một cặp đôi kinh điển với Công viên Hạ (Нижний парк) dưới chân đồi - hai lá phổi xanh gắn với lịch sử khu điều dưỡng nước khoáng của thành phố. Từ thời khu spa Lipetsk phát triển ở thế kỷ 19, khu vực trên cao này đã được quy hoạch thành nơi dạo chơi cho khách điều dưỡng, với các lối đi bộ rợp bóng cây, thảm cỏ và điểm ngắm cảnh. Ngày nay, Công viên Thượng là nơi đi dạo, tập thể dục, hẹn hò và thư giãn quen thuộc; từ mép công viên và các đài quan sát, du khách có thể phóng tầm mắt xuống phần thành phố phía dưới. Không gian yên tĩnh, nhiều cây xanh cùng vị trí gần đồi Nhà thờ, Nhà thờ Giáng Sinh và các bảo tàng khiến nơi đây trở thành điểm dừng dễ chịu khi khám phá trung tâm Lipetsk, đặc biệt vào những buổi chiều mát.",
    [
        "Công viên trên cao ở trung tâm Lipetsk, cặp đôi với Công viên Hạ.",
        "Lối đi rợp bóng cây, điểm ngắm cảnh thành phố từ trên đồi.",
        "Gần đồi Nhà thờ, Nhà thờ Giáng Sinh và các bảo tàng trung tâm.",
    ],
    prac(
        "Mở cửa tự do hằng ngày.",
        "Miễn phí.",
        "Khoảng 45–60 phút.",
        "Mùa ấm (tháng 5–9); buổi chiều mát để dạo và ngắm cảnh.",
        "Kết hợp thăm Nhà thờ Giáng Sinh và bảo tàng địa phương; mang giày đi bộ.",
    ),
    [wiki_src("Верхний парк (Липецк)"), osm_src(52.61333, 39.60917)],
    ["park", "green", "viewpoint", "promenade", "lipetsk", "spa-heritage"],
    maps_text("Верхний парк", "Липецк", "Verkhny Park", "Lipetsk", 52.61333, 39.60917),
))

# 16) Великокняжеская церковь (Елец)
RECORDS.append(rec(
    "grand-ducal-church-yelets",
    "Nhà thờ Đại Công tước, Yelets (Vê-li-cô-cnhia-giê-xkaia)",
    "Великокняжеская церковь (храм во имя Михаила Тверского и Александра Невского)",
    "Grand-Ducal Church, Yelets",
    ["church"],
    52.6242107, 38.5002014,
    "Ул. Советская, thành phố Yelets, tỉnh Lipetsk, Nga.",
    "Nhà thờ Đại Công tước ở Yelets là một viên ngọc kiến trúc đầu thế kỷ 20, kết hợp phong cách Nga - hiện đại (modern) với mái vòm pha lê độc đáo. Được xây dựng nhanh chóng để tưởng niệm và tri ân hoàng gia, công trình nổi bật với nội thất tinh xảo và cây thánh giá bằng pha lê.",
    "Giữa khu phố cổ Yelets, Nhà thờ Đại Công tước (Великокняжеская церковь) - chính thức mang tên Thánh Mikhail xứ Tver và Alexander Nevsky - là một trong những công trình tôn giáo độc đáo nhất thành phố. Được xây dựng chỉ trong thời gian ngắn quanh năm 1911 bằng nguồn tài trợ của thương gia giàu có Zausailov, nhà thờ ra đời để kỷ niệm chuyến viếng thăm của một vị đại công tước và gắn với hoàng gia Romanov. Kiến trúc pha trộn tinh tế giữa phong cách Nga truyền thống và trào lưu Modern (Art Nouveau) đầu thế kỷ 20: những mái vòm được ốp vật liệu đặc biệt, cây thánh giá và các chi tiết trang trí bằng pha lê lấp lánh, cùng hệ thống chiếu sáng điện tân tiến so với thời bấy giờ. Bên trong, nội thất được trang hoàng lộng lẫy với đá ceramic, khung tượng thánh và các chi tiết mạ vàng. Liền kề là 'Ngôi nhà của các tu sĩ' (Дом призрения) cũng do Zausailov xây. Sống sót qua thời Xô Viết và được phục hồi, nhà thờ ngày nay là điểm tham quan không thể bỏ qua khi ghé Yelets, minh chứng cho sự phồn thịnh và gu thẩm mỹ tinh tế của giới thương nhân thành phố.",
    [
        "Kiến trúc độc đáo pha trộn Nga truyền thống và phong cách Modern đầu thế kỷ 20.",
        "Mái vòm ốp vật liệu đặc biệt và thánh giá, chi tiết bằng pha lê lấp lánh.",
        "Gắn với hoàng gia Romanov và nhà tài trợ - thương gia Zausailov của Yelets.",
    ],
    prac(
        "Mở cửa hằng ngày theo giờ lễ, thường khoảng 8:00–19:00.",
        "Miễn phí vào cửa (có thể quyên góp).",
        "Khoảng 30–45 phút.",
        "Quanh năm; ánh sáng đẹp làm nổi bật chi tiết pha lê vào ngày nắng.",
        "Ăn mặc kín đáo; kết hợp dạo phố cổ và thăm Nhà thờ Thăng Thiên, bảo tàng Bunin.",
    ),
    [wiki_search_src("Великокняжеская церковь Елец"), osm_src(52.6242107, 38.5002014)],
    ["church", "modern", "art-nouveau", "yelets", "romanov", "architecture"],
    maps_text("Великокняжеская церковь", "Елец", "Grand-Ducal Church", "Yelets", 52.6242107, 38.5002014),
))

# 17) Усадьба Скорняково-Архангельское
RECORDS.append(rec(
    "skornyakovo-arkhangelskoye-estate",
    "Điền trang Skornyakovo-Arkhangelskoye (Xcoóc-nhia-cô-vô)",
    "Усадьба Скорняково-Архангельское",
    "Skornyakovo-Arkhangelskoye Estate",
    ["palace", "park_garden"],
    52.6807568, 38.9149519,
    "Làng Скорняково, huyện Zadonsky, tỉnh Lipetsk, Nga (bên bờ sông Đông).",
    "Skornyakovo-Arkhangelskoye là một điền trang quý tộc thế kỷ 18–19 bên bờ sông Đông, từng thuộc về gia đình tướng Muravyov. Sau khi được trùng tu công phu, nơi đây trở thành khu nghỉ dưỡng - du lịch điền trang với nhà chính, nhà thờ, vườn cảnh và các sự kiện văn hóa.",
    "Bên bờ sông Đông thơ mộng ở huyện Zadonsky, điền trang Скорняково-Архангельское là một trong những khu điền trang quý tộc được phục dựng đẹp nhất tỉnh Lipetsk. Hình thành từ thế kỷ 18–19, điền trang từng gắn với gia đình danh tướng Nikolai Muravyov-Karsky - một nhân vật quân sự nổi tiếng của nước Nga thế kỷ 19. Quần thể gồm nhà chính (усадебный дом), nhà thờ Tổng lãnh thiên thần Mikhail (Архангельская церковь) mà từ đó có tên gọi, cùng các công trình phụ trợ, vườn cảnh và không gian bên sông. Sau nhiều thập niên hoang phế thời Xô Viết, điền trang đã được một chủ đầu tư tư nhân trùng tu công phu, biến thành một khu nghỉ dưỡng - du lịch điền trang cao cấp: có nhà hàng, khu lưu trú, không gian tổ chức sự kiện, lễ cưới, festival âm nhạc và ẩm thực ngoài trời. Du khách đến đây để tận hưởng kiến trúc điền trang Nga cổ điển, tản bộ trong vườn, thưởng thức ẩm thực và hòa mình vào các sự kiện văn hóa bên dòng sông Đông. Đây là ví dụ hiếm hoi và thành công về việc 'hồi sinh' di sản điền trang thành điểm đến du lịch sống động.",
    [
        "Điền trang quý tộc thế kỷ 18–19 bên sông Đông, gắn với tướng Muravyov.",
        "Nhà chính, nhà thờ Tổng lãnh thiên thần Mikhail và vườn cảnh được trùng tu công phu.",
        "Khu nghỉ dưỡng - du lịch điền trang với ẩm thực, sự kiện và festival ngoài trời.",
    ],
    prac(
        "Khu điền trang mở cửa cho khách tham quan/nghỉ dưỡng; nên đặt trước khi có sự kiện.",
        "Vào tham quan có thể thu phí; ẩm thực, lưu trú và sự kiện tính phí riêng.",
        "Nửa ngày (có thể nghỉ qua đêm).",
        "Mùa ấm (tháng 5–9), nhất là dịp có festival âm nhạc/ẩm thực.",
        "Đặt trước nhà hàng/phòng nghỉ; đi xe riêng vì nằm ở vùng quê ven sông.",
    ),
    [wiki_search_src("Усадьба Скорняково-Архангельское"), osm_src(52.6807568, 38.9149519)],
    ["estate", "manor", "don-river", "resort", "history", "zadonsk"],
    maps_text("Усадьба Скорняково-Архангельское", "Липецкая область", "Skornyakovo-Arkhangelskoye Estate", "Lipetsk Oblast", 52.6807568, 38.9149519),
))

# 18) Литературно-мемориальный музей И. А. Бунина (Елец)
RECORDS.append(rec(
    "bunin-museum-yelets",
    "Bảo tàng văn học tưởng niệm Ivan Bunin (Bu-nin)",
    "Литературно-мемориальный музей И. А. Бунина",
    "Ivan Bunin Literary Memorial Museum",
    ["museum"],
    52.6187272, 38.4937984,
    "Ул. Горького 16, thành phố Yelets, tỉnh Lipetsk, Nga.",
    "Bảo tàng văn học tưởng niệm Ivan Bunin ở Yelets nằm trong ngôi nhà nơi văn hào - chủ nhân giải Nobel Văn học 1933 - từng trọ học thời niên thiếu. Bảo tàng lưu giữ kỷ vật, bản thảo và tái hiện không gian gắn với tuổi trẻ của nhà văn tại thành phố cổ.",
    "Tại thành phố cổ Yelets, Bảo tàng văn học tưởng niệm I. A. Bunin (Литературно-мемориальный музей И. А. Бунина) tôn vinh Ivan Bunin - nhà văn, nhà thơ Nga đầu tiên đoạt giải Nobel Văn học (năm 1933). Bảo tàng đặt trong ngôi nhà nơi Bunin từng ở trọ trong những năm theo học tại trường trung học Yelets thời niên thiếu - quãng đời để lại dấu ấn sâu đậm trong nhiều tác phẩm của ông. Các gian trưng bày tái hiện không khí đời sống tỉnh lẻ nước Nga cuối thế kỷ 19, giới thiệu tuổi thơ, gia đình, quá trình học tập và sự nghiệp văn chương của Bunin qua bản thảo, thư từ, ấn phẩm đầu tay, ảnh tư liệu, đồ dùng cá nhân và các hiện vật gắn với thời kỳ lưu vong ở Pháp. Yelets và vùng quê xung quanh chính là bối cảnh của nhiều trang viết nổi tiếng của ông. Đây là điểm đến ý nghĩa cho người yêu văn học, giúp cảm nhận cội nguồn cảm hứng của một trong những cây bút lớn nhất văn học Nga.",
    [
        "Ngôi nhà nơi Ivan Bunin - Nobel Văn học 1933 - ở trọ thời đi học ở Yelets.",
        "Bản thảo, thư từ, ấn phẩm và kỷ vật tái hiện tuổi trẻ và sự nghiệp của nhà văn.",
        "Bối cảnh Yelets và vùng quê là nguồn cảm hứng cho nhiều tác phẩm của Bunin.",
    ],
    prac(
        "Thường 10:00–18:00; nghỉ thứ Hai (nên kiểm tra trước).",
        "Vé khoảng 100–200 RUB; có ưu đãi cho học sinh.",
        "Khoảng 45–60 phút.",
        "Quanh năm; kết hợp tham quan phố cổ Yelets.",
        "Có thể yêu cầu thuyết minh; kết hợp thăm nhà lưu niệm Khrennikov và Nhà thờ Thăng Thiên.",
    ),
    [wiki_search_src("Литературно-мемориальный музей Бунина Елец"), osm_src(52.6187272, 38.4937984)],
    ["museum", "literature", "bunin", "nobel", "yelets", "memorial"],
    maps_text("Литературно-мемориальный музей И. А. Бунина", "Елец", "Bunin Museum", "Yelets", 52.6187272, 38.4937984),
))

# 19) Замок Борки
RECORDS.append(rec(
    "borki-castle",
    "Lâu đài Borki (Boóc-ki) của hoàng thân Romanov",
    "Замок Борки (усадьба-храм в Борках)",
    "Borki Castle",
    ["palace", "other"],
    52.15278, 38.10972,
    "Làng Борки, huyện Terbunsky, tỉnh Lipetsk, Nga (phía nam tỉnh).",
    "Lâu đài Borki là một công trình tân Gothic độc đáo ở phía nam tỉnh Lipetsk, gắn với đại công tước Andrei Romanov. Kiến trúc pháo đài - lâu đài bằng đá với tháp nhọn giữa vùng quê tạo nên khung cảnh 'châu Âu' hiếm thấy, thu hút khách du lịch và các buổi chụp ảnh.",
    "Ở làng Борки thuộc huyện Terbunsky phía nam tỉnh Lipetsk, một công trình đá kiểu tân Gothic (neo-Gothic) mọc lên giữa vùng thảo nguyên - đó là Lâu đài Borki (Замок Борки). Công trình được xây dựng đầu thế kỷ 20 trên phần đất từng thuộc đại công tước Andrei Vladimirovich Romanov - cháu của Sa hoàng - như một quần thể điền trang kết hợp nhà thờ và các công trình mang dáng dấp lâu đài phương Tây với tường đá, tháp nhọn và ô cửa vòm nhọn. Trải qua thời Xô Viết với nhiều công năng khác nhau và giai đoạn xuống cấp, 'lâu đài' này về sau được quan tâm trùng tu và trở thành một điểm du lịch độc đáo của vùng. Dáng vẻ cổ tích, 'rất châu Âu' giữa khung cảnh làng quê Nga khiến Borki trở thành phông nền yêu thích cho các buổi chụp ảnh cưới, sự kiện và du khách hiếu kỳ. Với những ai yêu kiến trúc lạ và thích khám phá các góc ít người biết của nước Nga, Lâu đài Borki là một điểm đến bất ngờ và đáng nhớ.",
    [
        "Công trình tân Gothic (neo-Gothic) hiếm thấy giữa vùng quê nam Lipetsk.",
        "Gắn với đại công tước Andrei Romanov - cháu của Sa hoàng.",
        "Dáng vẻ 'lâu đài châu Âu' - phông nền chụp ảnh và điểm du lịch độc đáo.",
    ],
    prac(
        "Khu vực ngoài trời; tham quan ban ngày, một số phần có thể cần liên hệ trước.",
        "Vào tham quan có thể miễn phí hoặc thu phí tượng trưng tùy thời điểm.",
        "Khoảng 45–60 phút.",
        "Cuối xuân đến đầu thu (tháng 5–9); ánh sáng đẹp cho ảnh vào sáng/chiều.",
        "Nằm khá xa trung tâm, nên đi xe riêng; kiểm tra tình trạng mở cửa trước khi đến.",
    ),
    [wiki_src("Борки (Тербунский район)"), osm_src(52.15278, 38.10972)],
    ["castle", "neo-gothic", "romanov", "estate", "photography", "terbuny"],
    maps_text("Замок Борки", "Липецкая область", "Borki Castle", "Lipetsk Oblast", 52.15278, 38.10972),
))

# 20) Соборная площадь (Ленина-Соборная площадь), Липецк
RECORDS.append(rec(
    "sobornaya-square-lipetsk",
    "Quảng trường Nhà thờ lớn (Sobornaya), Lipetsk",
    "Соборная площадь (Ленина-Соборная площадь)",
    "Cathedral Square (Sobornaya Square), Lipetsk",
    ["square_street"],
    52.608596, 39.599551,
    "Trung tâm thành phố Lipetsk (trên đồi Nhà thờ), tỉnh Lipetsk, Nga.",
    "Quảng trường Nhà thờ lớn là quảng trường trung tâm và trái tim của Lipetsk. Bao quanh là Nhà thờ chính tòa Giáng Sinh, tòa nhà chính quyền, Ngọn lửa Vĩnh cửu và đài tưởng niệm - nơi diễn ra các sự kiện, lễ hội lớn của thành phố.",
    "Ngự trên đồi Nhà thờ ở tim thành phố, Quảng trường Nhà thờ lớn (Соборная площадь, tên đầy đủ Ленина-Соборная площадь) là không gian công cộng quan trọng và biểu tượng nhất của Lipetsk. Đây là nơi hội tụ các công trình tiêu biểu: Nhà thờ chính tòa Giáng Sinh với mái vòm vàng, tòa nhà chính quyền tỉnh, tượng đài Lenin, Ngọn lửa Vĩnh cửu cùng đài tưởng niệm các liệt sĩ. Quảng trường rộng rãi, lát đá, là địa điểm tổ chức những sự kiện trọng đại của thành phố: duyệt binh, lễ hội thành phố, hòa nhạc, hội chợ, bắn pháo hoa và các buổi tụ họp đông người. Từ mép quảng trường trên cao, du khách có thể ngắm nhìn phần thành phố phía dưới và khu công viên. Buổi tối, khi nhà thờ và các công trình lên đèn, quảng trường trở nên lung linh và là nơi dạo mát yêu thích của cư dân. Đây cũng là điểm khởi đầu tự nhiên cho hành trình khám phá trung tâm lịch sử Lipetsk.",
    [
        "Quảng trường trung tâm và biểu tượng của Lipetsk, trên đồi Nhà thờ.",
        "Bao quanh có Nhà thờ Giáng Sinh, tòa nhà chính quyền, Ngọn lửa Vĩnh cửu.",
        "Nơi diễn ra lễ hội, duyệt binh, hòa nhạc và bắn pháo hoa của thành phố.",
    ],
    prac(
        "Không gian mở, dạo chơi tự do mọi lúc.",
        "Miễn phí.",
        "Khoảng 30–45 phút.",
        "Đẹp cả ngày; buổi tối khi lên đèn và các dịp lễ hội thành phố.",
        "Kết hợp thăm Nhà thờ Giáng Sinh, bảo tàng địa phương và Công viên Thượng gần đó.",
    ),
    [wiki_src("Соборная площадь (Липецк)"), osm_src(52.608596, 39.599551)],
    ["square", "city-center", "landmark", "lipetsk", "eternal-flame"],
    maps_text("Соборная площадь", "Липецк", "Cathedral Square", "Lipetsk", 52.608596, 39.599551),
))

# 21) Музей народных ремёсел и промыслов (Елец) - ren Yelets
RECORDS.append(rec(
    "yelets-folk-crafts-museum",
    "Bảo tàng nghề thủ công dân gian (ren Yelets)",
    "Музей народных ремёсел и промыслов",
    "Museum of Folk Crafts and Trades, Yelets",
    ["museum"],
    52.6212563, 38.4971203,
    "Ул. Ленина 68, thành phố Yelets, tỉnh Lipetsk, Nga.",
    "Bảo tàng nghề thủ công dân gian ở Yelets giới thiệu các nghề truyền thống của thành phố, nổi bật nhất là nghề ren Yelets (елецкое кружево) tinh xảo nức tiếng cả nước Nga. Du khách được chiêm ngưỡng các tác phẩm ren, đồ thủ công và tìm hiểu bàn tay tài hoa của nghệ nhân địa phương.",
    "Đặt trong một ngôi nhà cổ trên phố Ленина ở trung tâm Yelets, Bảo tàng nghề thủ công dân gian và các nghề truyền thống (Музей народных ремёсел и промыслов) là nơi tôn vinh bàn tay tài hoa của người dân thành phố cổ. Ngôi sao của bảo tàng là nghề ren Yelets (елецкое кружево) - một trong những dòng ren thủ công danh tiếng nhất nước Nga, với những tấm ren mỏng manh, hoa văn tinh vi được đan bằng con suốt (кружево на коклюшках) từ thế kỷ 19. Bên cạnh ren, bảo tàng còn trưng bày và giới thiệu nhiều nghề truyền thống khác của vùng Yelets như dệt, thêu, gốm, rèn, làm tẩu (елецкие курительные трубки), đồ gỗ và nhạc cụ dân gian. Du khách có thể chiêm ngưỡng các tác phẩm tinh xảo, tìm hiểu quy trình chế tác, đôi khi xem trình diễn của nghệ nhân và mua sản phẩm thủ công làm quà. Đây là điểm đến thú vị để hiểu về chiều sâu văn hóa - thủ công của Yelets, bổ sung hoàn hảo cho hành trình dạo phố cổ.",
    [
        "Tôn vinh nghề ren Yelets (елецкое кружево) tinh xảo nức tiếng nước Nga.",
        "Giới thiệu nhiều nghề truyền thống: dệt, thêu, gốm, rèn, làm tẩu, đồ gỗ.",
        "Có thể xem chế tác và mua sản phẩm thủ công làm quà lưu niệm.",
    ],
    prac(
        "Thường 10:00–18:00; nghỉ thứ Hai (nên kiểm tra trước).",
        "Vé khoảng 100–200 RUB; có ưu đãi cho học sinh.",
        "Khoảng 45–60 phút.",
        "Quanh năm; kết hợp tham quan phố cổ Yelets.",
        "Hỏi về trình diễn nghề và mua ren Yelets làm quà; kết hợp thăm bảo tàng Bunin gần đó.",
    ),
    [wiki_search_src("Музей народных ремёсел и промыслов Елец"), osm_src(52.6212563, 38.4971203)],
    ["museum", "crafts", "lace", "yelets", "folk-art", "souvenir"],
    maps_text("Музей народных ремёсел и промыслов", "Елец", "Museum of Folk Crafts", "Yelets", 52.6212563, 38.4971203),
))

# 22) Чаплыгин (Раненбург)
RECORDS.append(rec(
    "chaplygin-town",
    "Thị trấn cổ Chaplygin (Sáp-lư-ghin / Ranenburg)",
    "Чаплыгин (Раненбург)",
    "Chaplygin (Ranenburg) Town",
    ["square_street"],
    53.2430150, 39.9668010,
    "Thành phố Chaplygin, phía đông bắc tỉnh Lipetsk, Nga.",
    "Chaplygin - tên cũ Ranenburg - là một thị trấn cổ do Pyotr Đại đế đặt tên, gắn với một pháo đài nhỏ và điền trang của Aleksandr Menshikov. Ngày nay thị trấn quyến rũ bởi kiến trúc tỉnh lẻ thế kỷ 18–19, nhà thờ cổ và bầu không khí lịch sử yên bình.",
    "Ở phía đông bắc tỉnh Lipetsk, thị trấn Chaplygin (Чаплыгин) mang trong mình một quá khứ đặc biệt dưới cái tên cổ Ranenburg (Раненбург). Đầu thế kỷ 18, chính Sa hoàng Pyotr Đại đế đã đặt tên cho pháo đài nhỏ nơi đây; vùng đất sau đó trở thành điền trang của Aleksandr Menshikov - cận thần quyền lực bậc nhất của nhà vua. Đến thời Xô Viết, thị trấn được đổi tên thành Chaplygin để vinh danh nhà khoa học Sergei Chaplygin - người con của quê hương, một trong những cha đẻ của ngành khí động học Nga. Dạo bước trong thị trấn hôm nay, du khách bắt gặp những dãy phố tỉnh lẻ tĩnh lặng với kiến trúc thế kỷ 18–19, các nhà thờ Chính thống cổ, quảng trường trung tâm, khu chợ thương gia và bảo tàng địa phương. Nhịp sống chậm rãi, những công trình cổ được gìn giữ và bầu không khí hoài niệm khiến Chaplygin trở thành điểm dừng chân thú vị cho những ai muốn cảm nhận một nước Nga tỉnh lẻ đậm chất lịch sử, tránh xa sự ồn ào của đô thị lớn.",
    [
        "Thị trấn cổ Ranenburg do Pyotr Đại đế đặt tên, gắn với điền trang Menshikov.",
        "Đổi tên theo nhà khí động học Sergei Chaplygin - người con của quê hương.",
        "Kiến trúc tỉnh lẻ thế kỷ 18–19, nhà thờ cổ và bảo tàng địa phương yên bình.",
    ],
    prac(
        "Khu phố mở tự do; bảo tàng thường 10:00–17:00, nghỉ thứ Hai.",
        "Dạo phố miễn phí; vé bảo tàng khoảng 100–200 RUB.",
        "Khoảng 2–3 giờ.",
        "Cuối xuân đến đầu thu (tháng 5–9), thời tiết dễ chịu để đi bộ.",
        "Đi xe riêng vì cách trung tâm Lipetsk khá xa; mang giày thoải mái.",
    ),
    [wiki_src("Чаплыгин"), osm_src(53.2430150, 39.9668010)],
    ["town", "history", "peter-the-great", "menshikov", "old-town", "ranenburg"],
    maps_text("Чаплыгин", "Липецкая область", "Chaplygin", "Lipetsk Oblast", 53.2430150, 39.9668010),
))

# 23) Комсомольский пруд (Липецк)
RECORDS.append(rec(
    "komsomolsky-pond-lipetsk",
    "Hồ Komsomolsky (Côm-xô-môn), Lipetsk",
    "Комсомольский пруд",
    "Komsomolsky Pond, Lipetsk",
    ["park_garden"],
    52.6063684, 39.5966108,
    "Trung tâm thành phố Lipetsk (gần Công viên Hạ), tỉnh Lipetsk, Nga.",
    "Hồ Komsomolsky là hồ nước ngay trung tâm Lipetsk, gắn liền với khu điều dưỡng nước khoáng và Công viên Hạ. Bờ hồ được cải tạo thành khu dạo bộ, bãi tắm và không gian nghỉ ngơi hiện đại, là điểm hẹn quen thuộc của người dân thành phố.",
    "Nằm ngay trung tâm Lipetsk, sát khu Công viên Hạ lịch sử, Hồ Komsomolsky (Комсомольский пруд) là một hồ nước nhân tạo có nguồn gốc từ hệ thống hồ - đập gắn với các xưởng luyện sắt và khu điều dưỡng nước khoáng của thành phố. Trải qua các đợt chỉnh trang, khu vực quanh hồ đã được cải tạo thành một không gian công cộng hiện đại và hấp dẫn: kè lát đá, lối đi dạo, ghế nghỉ, đài phun nước, bãi tắm mùa hè, điểm cho thuê thuyền đạp nước và các quán cà phê ven bờ. Đây là nơi người dân đến đi dạo, chạy bộ, hẹn hò, cho trẻ vui chơi và thư giãn bên mặt nước ngay giữa lòng thành phố. Vào mùa hè, bãi tắm và mặt hồ nhộn nhịp; các buổi tối và dịp lễ, khu vực bờ hồ thường có hoạt động văn hóa, chiếu sáng nghệ thuật. Vị trí trung tâm, dễ tiếp cận cùng cảnh quan mặt nước khiến Hồ Komsomolsky trở thành một trong những góc thư giãn được yêu thích nhất của Lipetsk.",
    [
        "Hồ nước ngay trung tâm Lipetsk, gắn với khu spa nước khoáng và Công viên Hạ.",
        "Bờ hồ cải tạo hiện đại: kè đá, lối dạo, bãi tắm, thuyền đạp nước, quán cà phê.",
        "Điểm dạo bộ, nghỉ ngơi và hoạt động văn hóa yêu thích của cư dân.",
    ],
    prac(
        "Khu vực bờ hồ mở tự do; bãi tắm và dịch vụ hoạt động ban ngày mùa hè.",
        "Dạo bờ hồ miễn phí; thuê thuyền và một số dịch vụ tính phí.",
        "Khoảng 45–60 phút.",
        "Mùa hè (tháng 6–8) để tắm và thuê thuyền; buổi tối mát mẻ để dạo.",
        "Kết hợp tham quan Công viên Hạ và trung tâm thành phố; mang đồ bơi nếu muốn tắm.",
    ),
    [wiki_src("Комсомольский пруд"), osm_src(52.6063684, 39.5966108)],
    ["pond", "lake", "promenade", "beach", "lipetsk", "recreation"],
    maps_text("Комсомольский пруд", "Липецк", "Komsomolsky Pond", "Lipetsk", 52.6063684, 39.5966108),
))

# 24) Памятник Петру I (Липецк)
RECORDS.append(rec(
    "peter-the-great-monument-lipetsk",
    "Tượng đài Pyotr Đại đế, Lipetsk",
    "Памятник Петру I",
    "Monument to Peter the Great, Lipetsk",
    ["monument"],
    52.6039947, 39.6004404,
    "Quảng trường Петра Великого, thành phố Lipetsk, tỉnh Lipetsk, Nga.",
    "Tượng đài Pyotr Đại đế trên Quảng trường Petra Velikogo là một trong những đài kỷ niệm quan trọng của Lipetsk, tri ân vị Sa hoàng đã khai sinh thành phố qua việc lập các xưởng luyện sắt. Cột đài cao với tượng đồng và các phù điêu là điểm nhấn ở trung tâm.",
    "Trên Quảng trường Petra Velikogo (площадь Петра Великого) ở trung tâm Lipetsk, Tượng đài Pyotr Đại đế (Памятник Петру I) là một biểu tượng thể hiện lòng biết ơn của thành phố đối với vị Sa hoàng đã khai sinh ra nó. Chính dưới thời Pyotr Đại đế, các xưởng luyện gang - thép (Липские железоделательные заводы) được lập bên sông vào đầu thế kỷ 18 để phục vụ chiến tranh và hạm đội, đặt nền móng cho sự ra đời của thành phố Lipetsk. Đài tưởng niệm hiện đại được khánh thành năm 1996 nhân dịp kỷ niệm thành phố, gồm một cột đài cao vươn lên với tượng nhà vua và các phù điêu bằng đồng khắc họa những cảnh gắn với lịch sử luyện kim, đóng tàu và công lao của Pyotr. Tượng đài đứng giữa không gian quảng trường thoáng đãng, gần các đài phun nước và khu dạo bộ, trở thành điểm chụp ảnh và gặp gỡ quen thuộc. Với du khách, đây là nơi lý tưởng để hình dung cội nguồn công nghiệp - lịch sử của Lipetsk và vai trò của Pyotr Đại đế đối với vùng đất này.",
    [
        "Đài kỷ niệm vị Sa hoàng đã khai sinh Lipetsk qua các xưởng luyện sắt.",
        "Cột đài cao với tượng đồng và phù điêu về luyện kim, đóng tàu (khánh thành 1996).",
        "Trên Quảng trường Petra Velikogo thoáng đãng - điểm chụp ảnh, gặp gỡ trung tâm.",
    ],
    prac(
        "Không gian mở, tham quan tự do mọi lúc.",
        "Miễn phí.",
        "Khoảng 15–30 phút.",
        "Đẹp cả ngày; buổi tối khi quảng trường và đài phun nước lên đèn.",
        "Kết hợp dạo trung tâm, Hồ Komsomolsky và Nhà thờ Giáng Sinh gần đó.",
    ),
    [wiki_search_src("Памятник Петру I Липецк"), osm_src(52.6039947, 39.6004404)],
    ["monument", "peter-the-great", "history", "lipetsk", "square"],
    maps_text("Памятник Петру I", "Липецк", "Monument to Peter the Great", "Lipetsk", 52.6039947, 39.6004404),
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
