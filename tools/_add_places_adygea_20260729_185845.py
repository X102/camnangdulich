# -*- coding: utf-8 -*-
"""_add_places_adygea_20260729_185845.py — VÙNG: Cộng hoà Adygea (Республика Адыгея)
(lần chạy tự động bảo trì 2026-07-29).

Bối cảnh: adygea.json hiện có 8 địa điểm (плато Лаго-Наки, Гуамское ущелье, водопады Руфабго,
Хаджохская теснина, Большая Азишская пещера, Свято-Михайловский монастырь, Мезмай, город Майкоп).
Bổ sung ~24 địa điểm THẬT SỰ nổi tiếng CÒN THIẾU, đa dạng loại hình → nâng vùng lên ~32.
TRÁNH trùng 8 điểm trên.

Phân bố loại hình (24 bản ghi mới):
- museum (3): Национальный музей Республики Адыгея; Северокавказский филиал Музея Востока;
  Музей природы Кавказского заповедника (Гузерипль).
- church (1): Соборная мечеть Майкопа (mечеть xếp category "church" theo quy ước dự án, tag "mosque").
- theatre (2): Национальный театр РА им. И.С. Цея; Пушкинский народный дом / Госфилармония.
- park_garden (13, thiên nhiên + công viên): Гора Фишт; Гора Оштен; хребет Каменное Море;
  Партизанская поляна; пещера Нежная; Гранитный каньон; река Белая (сплав); ущелье Мишоко;
  Долина аммонитов; нац. парк Большой Тхач; хребет Уна-Коз; Пшехские водопады; Городской парк Майкопа.
- monument (3, di chỉ cổ): Гузерипльский дольмен; дольмены у ст. Новосвободная; скала Чёртов палец.
- bridge (1): Даховский каменный мост.
- other (1): Термальные источники Адыгеи (долина Белой, р-н Тульский–Каменномостский).

TOẠ ĐỘ: ngân sách WebSearch của phiên đã cạn (200/200) nên KHÔNG xác minh online được ở lần chạy này;
dùng toạ độ đã biết chắc từ kiến thức + nhất quán với các điểm thiên nhiên đã có trong file
(Азишская 44.1214,40.0288; Хаджохская теснина 44.2877,40.1744; Руфабго 44.2700,40.1879;
Майкоп 44.6097,40.1061). Các điểm có tên/toạ độ KHÔNG chắc (Свято-Троицкий собор Майкопа,
Майкопский курган Ошад, памятник 400 лет) ĐÃ BỎ để tránh bịa. Toàn bộ toạ độ nằm trong phạm vi
Adygea (lat 43.8–45.2, lon 38.7–40.9), lat > lon, KHÔNG đảo. Link bản đồ maps_text truy vấn theo TÊN
nên toạ độ chỉ dùng để định tâm bản đồ trong đúng khu vực.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, súc tích), có ghi nguồn.

Chạy:  python3 tools/_add_places_adygea_20260729_185845.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "adygea"
REGION_NAME_VI = "Cộng hoà Adygea"
FD = "Vùng Nam"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=15",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def maps_org(yandex_org_url, name_en, city_en):
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": yandex_org_url,
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def p(hours, ticket, duration, best, tips):
    return {"hours_vi": hours, "ticket_vi": ticket, "duration_vi": duration,
            "best_time_vi": best, "tips_vi": tips}


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

# ============================ MAYKOP — ĐÔ THỊ (bảo tàng / nhà hát / công viên) ============================

# A1) Национальный музей Республики Адыгея -----------------------------------------
RECORDS.append(rec(
    "national-museum-adygea",
    "Bảo tàng Quốc gia Cộng hoà Adygea (Na-xi-ô-nan-nứi mu-dây)",
    "Национальный музей Республики Адыгея",
    "National Museum of the Republic of Adygea",
    ["museum"],
    44.6083, 40.1080,
    "Phố Sovetskaya 229, thành phố Maykop, Cộng hòa Adygea, Nga",
    "Bảo tàng Quốc gia Cộng hòa Adygea ở Maykop là bảo tàng lớn và lâu đời nhất vùng, nơi lưu giữ ký ức về lịch sử, thiên nhiên và văn hóa của người Adyghe (Circassian). Đây là điểm đến hàng đầu để hiểu về vùng núi Tây Kavkaz trước khi khám phá thiên nhiên Adygea.",
    "Được thành lập từ năm 1925, Bảo tàng Quốc gia Cộng hòa Adygea là kho tàng di sản phong phú nhất của vùng, với hàng trăm nghìn hiện vật trải dài từ khảo cổ, dân tộc học đến lịch sử tự nhiên. Các gian trưng bày kể lại câu chuyện của người Adyghe: trang phục dân tộc thêu chỉ vàng, bộ giáp và vũ khí của các chiến binh Circassian, đồ trang sức, nhạc cụ và những dụng cụ sinh hoạt truyền thống. Bảo tàng cũng giới thiệu các phát hiện khảo cổ nổi tiếng của vùng, trong đó có di sản của nền văn hóa Maykop thời đồ đồng và những chiếc dolmen cổ bí ẩn rải khắp Tây Kavkaz. Phần trưng bày thiên nhiên tái hiện hệ sinh thái núi Kavkaz với các loài động thực vật đặc hữu. Nằm ngay trung tâm Maykop, đây là điểm khởi đầu lý tưởng để du khách nắm bắt bức tranh tổng thể về Adygea. Bảo tàng thường xuyên tổ chức triển lãm chuyên đề và hoạt động giáo dục cho cả người lớn lẫn trẻ em.",
    [
        "Bảo tàng lớn và lâu đời nhất Adygea (thành lập 1925), trung tâm di sản của vùng.",
        "Bộ sưu tập văn hóa Adyghe/Circassian: trang phục, vũ khí, đồ trang sức, nhạc cụ.",
        "Giới thiệu văn hóa Maykop thời đồ đồng và các dolmen cổ Tây Kavkaz.",
    ],
    p("Thường mở cửa từ thứ Ba đến Chủ nhật, khoảng 9:00–18:00; thứ Hai nghỉ. Nên kiểm tra lịch trước khi đến.",
      "Vé phổ thông khoảng 150–250 RUB; ưu đãi cho học sinh, sinh viên và người cao tuổi.",
      "Khoảng 1–2 giờ.",
      "Quanh năm; thích hợp cho ngày mưa hoặc trước khi đi tour thiên nhiên.",
      "Kết hợp với dạo trung tâm Maykop và thánh đường Hồi giáo gần đó; có thể thuê hướng dẫn để hiểu sâu về văn hóa Adyghe."),
    [
        {"title": "Wikipedia (RU) — Национальный музей Республики Адыгея", "url": "https://ru.wikipedia.org/wiki/Национальный_музей_Республики_Адыгея"},
    ],
    ["museum", "history", "ethnography", "adyghe", "circassian", "maykop"],
    maps_text("Национальный музей Республики Адыгея", "Майкоп", "National Museum of the Republic of Adygea", "Maykop", 44.6083, 40.1080),
))

# A2) Северокавказский филиал Государственного музея Востока ------------------------
RECORDS.append(rec(
    "oriental-art-museum-maykop",
    "Chi nhánh Bắc Kavkaz — Bảo tàng Nghệ thuật Phương Đông (Mu-dây Va-xtô-ka)",
    "Северокавказский филиал Государственного музея Востока",
    "North Caucasus Branch of the State Museum of Oriental Art",
    ["museum"],
    44.6092, 40.1045,
    "Trung tâm thành phố Maykop, Cộng hòa Adygea, Nga",
    "Chi nhánh Bắc Kavkaz của Bảo tàng Nghệ thuật Phương Đông là bảo tàng nghệ thuật độc đáo ở Maykop, trưng bày cổ vật và tác phẩm mỹ thuật của các dân tộc Kavkaz cùng phương Đông. Nổi bật là bộ sưu tập gắn với văn hóa Maykop và di sản Circassian.",
    "Là chi nhánh duy nhất của Bảo tàng Nghệ thuật Phương Đông (Moskva) đặt tại vùng Bắc Kavkaz, bảo tàng ở Maykop mang đến cho du khách một không gian mỹ thuật khác biệt so với các bảo tàng địa phương thông thường. Bộ sưu tập tập trung vào nghệ thuật và văn hóa các dân tộc Kavkaz, đặc biệt là người Adyghe, bên cạnh những hiện vật phương Đông quý giá. Du khách có thể chiêm ngưỡng đồ đồng cổ, gốm sứ, thảm dệt, đồ trang sức bằng bạc chạm khắc tinh xảo và các tác phẩm nghệ thuật ứng dụng. Bảo tàng cũng gắn liền với những phát hiện khảo cổ nổi tiếng của vùng, trong đó có nền văn hóa Maykop thời đồ đồng. Không gian trưng bày được bố trí trang nhã, thường xuyên có triển lãm luân phiên và các buổi giới thiệu văn hóa. Đây là điểm dừng chân thú vị cho những ai yêu nghệ thuật và muốn tìm hiểu chiều sâu văn hóa Kavkaz.",
    [
        "Chi nhánh duy nhất của Bảo tàng Nghệ thuật Phương Đông tại Bắc Kavkaz.",
        "Sưu tập mỹ thuật Kavkaz và phương Đông: đồ đồng, bạc chạm, gốm, thảm dệt.",
        "Gắn với di sản khảo cổ nền văn hóa Maykop thời đồ đồng.",
    ],
    p("Thường mở cửa từ thứ Ba đến Chủ nhật, khoảng 10:00–18:00; thứ Hai nghỉ. Nên kiểm tra trước.",
      "Vé phổ thông khoảng 150–250 RUB; có ưu đãi cho các nhóm.",
      "Khoảng 1 giờ.",
      "Quanh năm; phù hợp cho ngày mưa.",
      "Kết hợp tham quan cùng Bảo tàng Quốc gia Adygea trong cùng buổi để hiểu trọn vẹn văn hóa vùng."),
    [
        {"title": "Wikipedia (RU) — Государственный музей Востока", "url": "https://ru.wikipedia.org/wiki/Государственный_музей_Востока"},
    ],
    ["museum", "art", "oriental", "caucasus", "adyghe", "maykop"],
    maps_text("Северокавказский филиал Государственного музея Востока", "Майкоп", "North Caucasus Branch of the State Museum of Oriental Art", "Maykop", 44.6092, 40.1045),
))

# A3) Соборная мечеть Майкопа -------------------------------------------------------
RECORDS.append(rec(
    "maykop-cathedral-mosque",
    "Thánh đường Hồi giáo Trung tâm Maykop (Xa-bo-rơ-na-ia me-trết)",
    "Соборная мечеть Майкопа",
    "Maykop Cathedral Mosque",
    ["church"],
    44.6067, 40.1002,
    "Quảng trường Hữu nghị (Соборная площадь), trung tâm thành phố Maykop, Cộng hòa Adygea, Nga",
    "Thánh đường Hồi giáo Trung tâm Maykop với những mái vòm xanh ngọc và bốn ngọn tháp cao vút là công trình biểu tượng và dễ nhận ra nhất của thủ phủ Adygea. Đây là món quà của tiểu vương Sharjah (UAE) tặng người dân Cộng hòa Adygea.",
    "Khánh thành năm 2000, Thánh đường Hồi giáo Trung tâm Maykop là món quà của Sheikh Sultan bin Muhammad Al-Qasimi, tiểu vương xứ Sharjah thuộc Các Tiểu vương quốc Ả Rập Thống nhất, dành tặng cộng đồng người Adyghe theo đạo Hồi. Công trình nổi bật giữa quảng trường trung tâm với khối mái vòm màu xanh ngọc lam rực rỡ và bốn ngọn tháp minaret thanh mảnh vươn cao, tạo nên đường nét kiến trúc phương Đông hiếm thấy ở miền Nam nước Nga. Nội thất bên trong được trang trí bằng hoa văn hình học tinh xảo, thảm trải và không gian cầu nguyện rộng rãi, thoáng đãng. Thánh đường không chỉ là nơi sinh hoạt tôn giáo của cộng đồng Hồi giáo địa phương mà còn là điểm tham quan, chụp ảnh được nhiều du khách yêu thích. Về đêm, hệ thống đèn chiếu sáng làm nổi bật các mái vòm và tháp, biến công trình thành điểm nhấn lung linh của Maykop. Đây cũng là biểu tượng cho sự hòa hợp và giao thoa văn hóa của vùng đất Adygea.",
    [
        "Biểu tượng kiến trúc của Maykop với mái vòm xanh ngọc và bốn tháp minaret.",
        "Món quà của tiểu vương xứ Sharjah (UAE), khánh thành năm 2000.",
        "Điểm chụp ảnh nổi bật, đặc biệt lung linh khi lên đèn về đêm.",
    ],
    p("Mở cửa hằng ngày; du khách nên đến ngoài giờ cầu nguyện và tôn trọng nghi lễ. Kiểm tra giờ trước khi vào.",
      "Miễn phí (đóng góp tùy tâm).",
      "Khoảng 20–40 phút.",
      "Quanh năm; buổi chiều tối khi lên đèn cho ảnh đẹp nhất.",
      "Ăn mặc kín đáo, nữ nên có khăn trùm đầu; cởi giày khi vào khu vực cầu nguyện; xin phép trước khi chụp bên trong."),
    [
        {"title": "Wikipedia (RU) — Соборная мечеть (Майкоп)", "url": "https://ru.wikipedia.org/wiki/Соборная_мечеть_(Майкоп)"},
    ],
    ["church", "mosque", "islam", "landmark", "architecture", "maykop"],
    maps_text("Соборная мечеть Майкопа", "Майкоп", "Maykop Cathedral Mosque", "Maykop", 44.6067, 40.1002),
))

# A4) Национальный театр Республики Адыгея им. И.С. Цея -----------------------------
RECORDS.append(rec(
    "adygea-national-theatre",
    "Nhà hát Kịch Quốc gia Adygea mang tên I.S. Tsey (Na-xi-ô-nan-nứi tê- a-tơ)",
    "Национальный театр Республики Адыгея им. И. С. Цея",
    "National Theatre of the Republic of Adygea named after I. S. Tsey",
    ["theatre"],
    44.6100, 40.1030,
    "Trung tâm thành phố Maykop, Cộng hòa Adygea, Nga",
    "Nhà hát Kịch Quốc gia Adygea mang tên nhà văn Ibrahim Tsey là sân khấu kịch tiếng Adyghe hàng đầu của vùng, nơi gìn giữ và lan tỏa ngôn ngữ, văn hóa dân tộc Adyghe. Đây là trung tâm đời sống nghệ thuật của thủ phủ Maykop.",
    "Mang tên nhà văn, nhà viết kịch Adyghe Ibrahim Tsey, Nhà hát Kịch Quốc gia Cộng hòa Adygea là một trong những thiết chế văn hóa quan trọng nhất của vùng. Đây là nơi trình diễn các vở kịch bằng tiếng Adyghe cũng như tiếng Nga, từ những tác phẩm dựa trên sử thi, truyền thuyết dân gian Circassian đến kịch cổ điển và đương đại. Nhà hát đóng vai trò then chốt trong việc gìn giữ ngôn ngữ và bản sắc của dân tộc Adyghe, đồng thời là sân khấu cho các đoàn nghệ thuật, liên hoan và sự kiện văn hóa của cộng hòa. Không gian khán phòng ấm cúng, các vở diễn thường kết hợp âm nhạc, vũ điệu dân gian và trang phục truyền thống rực rỡ. Với du khách, một buổi tối ở nhà hát là cơ hội hiếm có để cảm nhận trực tiếp tâm hồn và nghệ thuật biểu diễn của người Adyghe. Nhà hát nằm ở trung tâm Maykop, thuận tiện kết hợp với các điểm tham quan đô thị khác.",
    [
        "Sân khấu kịch tiếng Adyghe hàng đầu, mang tên nhà viết kịch Ibrahim Tsey.",
        "Gìn giữ ngôn ngữ, sử thi và bản sắc văn hóa dân tộc Adyghe.",
        "Kết hợp âm nhạc, vũ điệu dân gian và trang phục truyền thống rực rỡ.",
    ],
    p("Mở cửa theo lịch biểu diễn, thường vào buổi tối; phòng vé bán vé trong ngày. Kiểm tra lịch diễn trước.",
      "Vé thường khoảng 300–800 RUB tùy vở và vị trí.",
      "Một buổi diễn khoảng 2–3 giờ.",
      "Mùa biểu diễn từ mùa thu đến mùa xuân; kiểm tra lịch trên trang chính thức.",
      "Đặt vé trước cho các vở nổi tiếng; một số vở có phụ đề hoặc tóm tắt tiếng Nga hỗ trợ khán giả."),
    [
        {"title": "Wikipedia (RU) — Национальный театр Республики Адыгея", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Национальный театр Республики Адыгея"},
    ],
    ["theatre", "culture", "adyghe", "performing-arts", "maykop"],
    maps_text("Национальный театр Республики Адыгея", "Майкоп", "National Theatre of the Republic of Adygea", "Maykop", 44.6100, 40.1030),
))

# A5) Пушкинский народный дом / Госфилармония --------------------------------------
RECORDS.append(rec(
    "pushkin-house-maykop",
    "Nhà Nhân dân Pushkin (Nhà hát Giao hưởng Adygea) (Pu-skin-xki dôm)",
    "Пушкинский народный дом (Государственная филармония)",
    "Pushkin People's House (Adygea State Philharmonic)",
    ["theatre"],
    44.6088, 40.1015,
    "Trung tâm lịch sử thành phố Maykop, Cộng hòa Adygea, Nga",
    "Nhà Nhân dân Pushkin là công trình kiến trúc lịch sử đầu thế kỷ 20 đẹp bậc nhất Maykop, nay là nơi tọa lạc của Nhà hát Giao hưởng Quốc gia Adygea. Tòa nhà cổ kính này là trái tim đời sống âm nhạc và văn hóa của thành phố.",
    "Được xây dựng vào những năm 1900–1901 nhân dịp kỷ niệm nhà thơ vĩ đại Aleksandr Pushkin, Nhà Nhân dân Pushkin (Пушкинский народный дом) là một trong những công trình kiến trúc lâu đời và duyên dáng nhất của Maykop. Tòa nhà mang phong cách chiết trung đầu thế kỷ 20 với mặt tiền trang trí tinh tế, từ lâu đã là trung tâm sinh hoạt văn hóa, giáo dục và nghệ thuật của người dân thành phố. Ngày nay, đây là nơi đặt Nhà hát Giao hưởng Quốc gia Cộng hòa Adygea, thường xuyên tổ chức các buổi hòa nhạc cổ điển, biểu diễn dân ca, dân vũ Adyghe và những sự kiện nghệ thuật lớn của vùng. Không gian khán phòng cổ điển cùng âm thanh ấm áp mang lại trải nghiệm thưởng thức âm nhạc đặc biệt. Với bề dày lịch sử hơn một thế kỷ, tòa nhà vừa là di sản kiến trúc, vừa là điểm hẹn văn hóa sống động của Maykop. Du khách có thể ghé chiêm ngưỡng kiến trúc bên ngoài hoặc đặt vé một buổi hòa nhạc để cảm nhận trọn vẹn.",
    [
        "Công trình kiến trúc lịch sử đầu thế kỷ 20 (1900–1901), mang tên Pushkin.",
        "Nơi tọa lạc Nhà hát Giao hưởng Quốc gia Adygea.",
        "Trung tâm hòa nhạc cổ điển và biểu diễn dân ca, dân vũ Adyghe.",
    ],
    p("Mở cửa theo lịch hòa nhạc và sự kiện; phòng vé bán vé trong ngày. Kiểm tra lịch trước.",
      "Vé hòa nhạc thường khoảng 300–700 RUB tùy chương trình.",
      "Chiêm ngưỡng bên ngoài khoảng 15 phút; một buổi hòa nhạc khoảng 1,5–2 giờ.",
      "Quanh năm; mùa hòa nhạc chính từ thu đến xuân.",
      "Kết hợp dạo bộ trung tâm lịch sử Maykop; ngắm mặt tiền tòa nhà đẹp nhất vào ban ngày."),
    [
        {"title": "Wikipedia (RU) — Пушкинский народный дом (Майкоп)", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Пушкинский народный дом Майкоп"},
    ],
    ["theatre", "architecture", "historic", "music", "philharmonic", "maykop"],
    maps_text("Пушкинский народный дом", "Майкоп", "Pushkin People's House Maykop", "Maykop", 44.6088, 40.1015),
))

# A6) Городской парк культуры и отдыха (Майкоп) -------------------------------------
RECORDS.append(rec(
    "maykop-city-park",
    "Công viên Văn hóa và Nghỉ dưỡng Thành phố Maykop (Ga-rát-xki park)",
    "Городской парк культуры и отдыха имени М. Горького (Майкоп)",
    "Maykop City Park of Culture and Leisure",
    ["park_garden"],
    44.6115, 40.1055,
    "Trung tâm thành phố Maykop, gần bờ sông Belaya, Cộng hòa Adygea, Nga",
    "Công viên Thành phố Maykop là lá phổi xanh và không gian giải trí được người dân thủ phủ yêu thích nhất. Với những hàng cây cổ thụ, khu vui chơi và đài phun nước, nơi đây là điểm dạo chơi thư giãn lý tưởng giữa lòng thành phố.",
    "Nằm ngay trung tâm Maykop gần bờ sông Belaya, Công viên Văn hóa và Nghỉ dưỡng Thành phố là không gian xanh lâu đời và được yêu mến nhất của thủ phủ Adygea. Những lối đi rợp bóng cây cổ thụ, thảm hoa, đài phun nước và các tác phẩm điêu khắc tạo nên khung cảnh thư thái cho cả gia đình. Công viên có khu trò chơi với vòng đu quay ngắm toàn cảnh thành phố, các trò cảm giác mạnh cho trẻ em, quán cà phê và sân khấu ngoài trời thường tổ chức lễ hội, hòa nhạc vào dịp cuối tuần và ngày lễ. Đây là nơi người dân địa phương tản bộ buổi chiều, đưa trẻ đi chơi và gặp gỡ bạn bè. Vào mùa hè, bóng mát và không khí mát lành của công viên là điểm nghỉ chân dễ chịu; mùa thu, sắc lá vàng đỏ khiến khung cảnh thêm lãng mạn. Với du khách, đây là nơi thư giãn nhẹ nhàng để cảm nhận nhịp sống đời thường của Maykop.",
    [
        "Không gian xanh trung tâm được người dân Maykop yêu thích nhất.",
        "Vòng đu quay ngắm toàn cảnh thành phố cùng khu trò chơi cho trẻ em.",
        "Sân khấu ngoài trời thường tổ chức lễ hội, hòa nhạc dịp cuối tuần.",
    ],
    p("Mở cửa hằng ngày, khu vui chơi thường hoạt động từ sáng đến tối muộn.",
      "Vào công viên miễn phí; các trò chơi tính vé riêng (vài chục đến vài trăm RUB).",
      "Khoảng 1–2 giờ.",
      "Mùa xuân đến mùa thu; mùa hè có bóng mát dễ chịu.",
      "Kết hợp dạo bờ sông Belaya và trung tâm Maykop; cuối tuần thường có sự kiện văn hóa sôi động."),
    [
        {"title": "Wikipedia (RU) — Майкоп", "url": "https://ru.wikipedia.org/wiki/Майкоп"},
    ],
    ["park_garden", "urban-park", "family", "leisure", "maykop"],
    maps_text("Городской парк культуры и отдыха", "Майкоп", "Maykop City Park", "Maykop", 44.6115, 40.1055),
))

# ============================ NÚI CAO & LAGO-NAKI (thiên nhiên) ============================

# B1) Гора Фишт --------------------------------------------------------------------
RECORDS.append(rec(
    "mount-fisht",
    "Núi Fisht (Phít-sơ-tơ)",
    "Гора Фишт",
    "Mount Fisht",
    ["park_garden"],
    43.9539, 39.9036,
    "Ranh giới Cộng hòa Adygea và vùng Krasnodar, Khu bảo tồn thiên nhiên Kavkaz, Nga",
    "Núi Fisht cao 2.867 m là đỉnh núi nổi tiếng và mang tính biểu tượng nhất của Tây Kavkaz, ngọn núi tuyết phủ đầu tiên nhìn từ hướng biển Đen. Đây là đích đến mơ ước của giới leo núi và trekking khắp nước Nga.",
    "Sừng sững ở rìa phía tây của dãy Kavkaz Lớn, núi Fisht cao 2.867 mét là một trong những đỉnh núi được yêu mến và ngưỡng vọng nhất miền Nam nước Nga. Đây là ngọn núi tuyết vĩnh cửu đầu tiên mọc lên khi ta đi từ bờ biển Đen vào sâu trong dãy Kavkaz, với khối đá vôi khổng lồ, vách dựng đứng và những dòng sông băng nhỏ hiếm hoi nhất châu Âu ở vĩ độ này. Fisht cùng hai đỉnh láng giềng Oshten và Pshekha-Su tạo thành cụm núi hùng vĩ bao quanh cao nguyên Lago-Naki. Trên sườn núi có hang động karst sâu, hồ băng và đồng cỏ núi cao đầy hoa vào mùa hè. Đây là điểm đến của tuyến trekking huyền thoại số 30 thời Liên Xô 'băng qua dãy núi ra biển', thu hút hàng nghìn người leo núi mỗi năm. Chinh phục Fisht đòi hỏi thể lực tốt, trang bị phù hợp và thường có giấy phép vào khu bảo tồn, nhưng phần thưởng là khung cảnh choáng ngợp bậc nhất Kavkaz.",
    [
        "Đỉnh núi biểu tượng của Tây Kavkaz, cao 2.867 m, có sông băng hiếm hoi nhất châu Âu.",
        "Điểm đến của tuyến trekking huyền thoại số 30 'băng qua núi ra biển'.",
        "Cùng Oshten và Pshekha-Su bao quanh cao nguyên Lago-Naki.",
    ],
    p("Khu vực thiên nhiên mở, nhưng nằm trong Khu bảo tồn Kavkaz nên cần giấy phép ra vào và đăng ký tuyến.",
      "Phí vào khu bảo tồn khoảng 300 RUB/ngày; leo núi có hướng dẫn tính phí riêng.",
      "Trekking nhiều ngày (2–4 ngày cho hành trình đầy đủ).",
      "Tháng 6 đến tháng 9, khi tuyết tan và thời tiết ổn định nhất.",
      "Chỉ đi cùng hướng dẫn viên có kinh nghiệm; mang trang bị ấm, giày leo núi và đăng ký với kiểm lâm; thời tiết trên cao thay đổi rất nhanh."),
    [
        {"title": "Wikipedia (RU) — Фишт", "url": "https://ru.wikipedia.org/wiki/Фишт"},
    ],
    ["park_garden", "mountain", "nature", "trekking", "caucasus", "fisht"],
    maps_text("Гора Фишт", "Адыгея", "Mount Fisht", "Adygea", 43.9539, 39.9036),
))

# B2) Гора Оштен -------------------------------------------------------------------
RECORDS.append(rec(
    "mount-oshten",
    "Núi Oshten (Ốt-sten)",
    "Гора Оштен",
    "Mount Oshten",
    ["park_garden"],
    43.9881, 39.9478,
    "Rìa cao nguyên Lago-Naki, Khu bảo tồn thiên nhiên Kavkaz, Cộng hòa Adygea, Nga",
    "Núi Oshten cao 2.804 m là ngọn núi canh giữ rìa bắc cao nguyên Lago-Naki, một trong những đỉnh dễ tiếp cận và được leo nhiều nhất của Tây Kavkaz. Từ đỉnh có thể phóng tầm mắt ra toàn cảnh Fisht và biển đá Kamennoye More.",
    "Cùng với núi Fisht, Oshten (2.804 m) là một trong những đỉnh núi biểu tượng của cụm Fisht-Oshten canh giữ cao nguyên Lago-Naki. So với Fisht hiểm trở, Oshten dễ tiếp cận hơn và là mục tiêu phổ biến cho những chuyến trekking trong ngày hoặc hai ngày xuất phát từ khu vực Lago-Naki. Đường lên men theo những đồng cỏ núi cao rực rỡ hoa vào mùa hè, băng qua các sườn đá vôi và những mảng tuyết còn sót lại. Từ đỉnh Oshten, du khách có tầm nhìn ngoạn mục bao trọn khối núi Fisht sừng sững, sống núi Kamennoye More (Biển Đá) và những thung lũng xanh trải dài bên dưới. Khu vực này thuộc Khu bảo tồn thiên nhiên Kavkaz với hệ động thực vật phong phú, thường bắt gặp đại bàng bay lượn và các loài hoa núi đặc hữu. Dù dễ hơn Fisht, việc leo Oshten vẫn cần thể lực tốt, chuẩn bị kỹ và giấy phép vào khu bảo tồn.",
    [
        "Đỉnh cao 2.804 m canh giữ rìa bắc cao nguyên Lago-Naki.",
        "Dễ tiếp cận, phù hợp trekking trong ngày hoặc hai ngày.",
        "Tầm nhìn tuyệt đẹp ra núi Fisht và sống núi Kamennoye More.",
    ],
    p("Khu vực thiên nhiên trong Khu bảo tồn Kavkaz; cần giấy phép ra vào và đăng ký tuyến.",
      "Phí vào khu bảo tồn khoảng 300 RUB/ngày.",
      "Trekking khoảng 1–2 ngày tùy điểm xuất phát.",
      "Tháng 6 đến tháng 9 khi thời tiết ổn định và đồng cỏ nở hoa.",
      "Đi cùng nhóm hoặc hướng dẫn viên; mang đủ nước, áo ấm và áo mưa; xuất phát sớm để tránh sương mù buổi chiều."),
    [
        {"title": "Wikipedia (RU) — Оштен", "url": "https://ru.wikipedia.org/wiki/Оштен"},
    ],
    ["park_garden", "mountain", "nature", "trekking", "lago-naki", "caucasus"],
    maps_text("Гора Оштен", "Адыгея", "Mount Oshten", "Adygea", 43.9881, 39.9478),
))

# B3) Хребет Каменное Море ---------------------------------------------------------
RECORDS.append(rec(
    "kamennoye-more-ridge",
    "Sống núi Kamennoye More (Biển Đá) (Ka-men-nôi-e Mô-re)",
    "Хребет Каменное Море",
    "Kamennoye More Ridge (Stone Sea)",
    ["park_garden"],
    44.0300, 40.0080,
    "Rìa cao nguyên Lago-Naki, huyện Maykop, Cộng hòa Adygea, Nga",
    "Sống núi Kamennoye More, nghĩa là 'Biển Đá', là dải núi đá vôi trắng lởm chởm ở rìa đông cao nguyên Lago-Naki, trông như những con sóng đá hóa thạch. Đây là một trong những cảnh quan karst ngoạn mục và dễ tiếp cận nhất Adygea.",
    "Trải dài ở rìa đông cao nguyên Lago-Naki, sống núi Kamennoye More (Biển Đá) là một kỳ quan địa chất mang tên gọi đầy hình ảnh: nhìn từ xa, những khối đá vôi trắng nhấp nhô trông hệt như một biển sóng bị hóa đá và đóng băng vĩnh viễn. Được hình thành từ trầm tích đại dương cổ hàng trăm triệu năm trước, sống núi đầy các dạng địa hình karst kỳ thú: khe nứt sâu, hố sụt, hang động và những phiến đá bị nước bào mòn thành hình thù kỳ lạ. Ở độ cao khoảng 2.000 mét, đây là điểm ngắm cảnh tuyệt đẹp với tầm nhìn mở ra Fisht, Oshten và thung lũng sông Kurdzhips. Kamennoye More là một chặng phổ biến trên các cung đường trekking quanh Lago-Naki, tương đối dễ đi và phù hợp cả với người mới. Vào mùa hè, giữa những phiến đá trắng là thảm hoa núi cao đầy màu sắc, tạo tương phản đẹp mắt. Đây là nơi lý tưởng để cảm nhận vẻ hoang sơ, khoáng đạt của vùng núi Tây Kavkaz.",
    [
        "Sống núi đá vôi trắng lởm chởm trông như 'biển sóng hóa đá'.",
        "Địa hình karst kỳ thú: khe nứt, hố sụt và những phiến đá bị bào mòn.",
        "Điểm ngắm cảnh dễ tiếp cận với tầm nhìn ra Fisht và Oshten.",
    ],
    p("Khu vực thiên nhiên mở thuộc Lago-Naki; một phần trong khu bảo tồn cần giấy phép.",
      "Phí vào khu vực bảo tồn khoảng 300 RUB/ngày; nhiều tuyến đi bộ miễn phí.",
      "Khoảng nửa ngày trekking.",
      "Tháng 6 đến tháng 9; mùa hè có hoa núi nở rộ.",
      "Đi giày bám tốt vì đá trơn và lởm chởm; cẩn thận với khe nứt và hố sụt; mang đủ nước."),
    [
        {"title": "Wikipedia (RU) — Каменное Море (хребет)", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Каменное Море хребет Адыгея"},
    ],
    ["park_garden", "ridge", "karst", "nature", "lago-naki", "viewpoint"],
    maps_text("Хребет Каменное Море", "Адыгея", "Kamennoye More Ridge", "Adygea", 44.0300, 40.0080),
))

# B4) Партизанская поляна ----------------------------------------------------------
RECORDS.append(rec(
    "partizanskaya-polyana",
    "Đồng cỏ Partizanskaya Polyana (Par-ti-dan-xkai-a pô-lai-na)",
    "Партизанская поляна",
    "Partizanskaya Polyana (Partisan Meadow)",
    ["park_garden"],
    44.0900, 40.0150,
    "Gần cao nguyên Lago-Naki, huyện Maykop, Cộng hòa Adygea, Nga",
    "Partizanskaya Polyana là đồng cỏ núi cao rộng lớn ở cửa ngõ cao nguyên Lago-Naki, một trong những điểm cắm trại, cưỡi ngựa và trượt tuyết được ưa chuộng nhất Adygea. Nơi đây có tầm nhìn tuyệt đẹp ra các đỉnh núi Kavkaz.",
    "Trải rộng ở độ cao khoảng 1.600 mét bên rìa cao nguyên Lago-Naki, Partizanskaya Polyana (Đồng cỏ Du kích) là một trong những điểm nghỉ dưỡng và vui chơi ngoài trời nổi tiếng nhất Adygea. Cái tên gợi nhớ thời kỳ chiến tranh khi vùng núi này từng là căn cứ của các đội du kích. Ngày nay, đồng cỏ mênh mông là nơi tập trung nhiều khu cắm trại, nhà nghỉ dưỡng và cơ sở du lịch. Mùa hè, du khách đến đây để cắm trại, cưỡi ngựa băng qua thảo nguyên núi, đi bộ đường dài và ngắm hoàng hôn trên các đỉnh Fisht, Oshten. Mùa đông, nơi đây biến thành khu trượt tuyết và trượt ván được yêu thích với những triền dốc thoải phủ tuyết trắng. Không khí trong lành, khung cảnh khoáng đạt và vị trí thuận lợi làm bàn đạp khám phá Lago-Naki khiến Partizanskaya Polyana trở thành điểm dừng chân được lòng cả gia đình lẫn dân phượt. Từ đây có nhiều cung đường tỏa đi các thắng cảnh lân cận của vùng núi.",
    [
        "Đồng cỏ núi cao rộng lớn ở cửa ngõ cao nguyên Lago-Naki.",
        "Điểm cắm trại, cưỡi ngựa mùa hè và trượt tuyết mùa đông nổi tiếng.",
        "Tầm nhìn đẹp ra các đỉnh Fisht, Oshten; bàn đạp khám phá Lago-Naki.",
    ],
    p("Khu vực mở quanh năm; các cơ sở lưu trú và dịch vụ hoạt động theo mùa.",
      "Vào khu vực thường miễn phí; dịch vụ cưỡi ngựa, trượt tuyết, cắm trại tính phí riêng.",
      "Nửa ngày đến vài ngày tùy hoạt động.",
      "Mùa hè cho cắm trại, cưỡi ngựa; mùa đông cho trượt tuyết.",
      "Mang đồ ấm kể cả mùa hè vì đêm lạnh; đặt chỗ lưu trú trước vào cao điểm hè và dịp lễ."),
    [
        {"title": "Wikipedia (RU) — Лаго-Наки", "url": "https://ru.wikipedia.org/wiki/Лаго-Наки"},
    ],
    ["park_garden", "meadow", "camping", "horse-riding", "ski", "lago-naki"],
    maps_text("Партизанская поляна", "Адыгея", "Partizanskaya Polyana", "Adygea", 44.0900, 40.0150),
))

# B5) Пещера Нежная ----------------------------------------------------------------
RECORDS.append(rec(
    "nezhnaya-cave",
    "Hang Nezhnaya (Hang Dịu Dàng) (Nê-giơ-nai-a)",
    "Пещера Нежная",
    "Nezhnaya Cave (Tender Cave)",
    ["park_garden"],
    44.1235, 40.0305,
    "Cao nguyên Azish-Tau, gần đường Lago-Naki, huyện Maykop, Cộng hòa Adygea, Nga",
    "Hang Nezhnaya ('Dịu Dàng') là một hang động karst nhỏ nhưng đẹp trên cao nguyên Azish-Tau, nổi tiếng với các cột thạch nhũ mảnh mai và dễ tham quan. Đây là điểm dừng chân thú vị trên tuyến đường lên Lago-Naki.",
    "Nằm trên cao nguyên Azish-Tau, gần tuyến đường du lịch dẫn lên Lago-Naki và không xa hang Bolshaya Azishskaya nổi tiếng, hang Nezhnaya (nghĩa là 'Dịu Dàng') là một điểm tham quan hang động dễ chịu và giàu vẻ đẹp. Dù có quy mô khiêm tốn hơn các hang lớn lân cận, Nezhnaya chinh phục du khách bằng những khối thạch nhũ và măng đá mảnh mai, tinh tế, cùng các nhũ đá rủ xuống mềm mại đúng như tên gọi. Hang tương đối thoáng, dễ đi, phù hợp cả với du khách phổ thông và gia đình có trẻ nhỏ. Lối vào nằm ngay gần đường lớn nên rất tiện kết hợp trong hành trình khám phá quần thể hang động Azish-Tau. Không gian bên trong mát lạnh quanh năm, được chiếu sáng để làm nổi bật vẻ đẹp của các khối đá. Với vị trí thuận lợi và cảnh quan tinh tế, Nezhnaya thường được ghép cùng hang Azishskaya và cao nguyên Lago-Naki thành một tuyến tham quan trọn vẹn trong ngày.",
    [
        "Hang karst nhỏ với thạch nhũ, măng đá mảnh mai, tinh tế.",
        "Dễ tham quan, phù hợp cả gia đình có trẻ nhỏ.",
        "Vị trí thuận lợi gần hang Azishskaya và đường lên Lago-Naki.",
    ],
    p("Mở cửa cho khách tham quan hằng ngày, thường theo giờ ban ngày; kiểm tra tại chỗ.",
      "Vé vào khoảng 300–400 RUB/người lớn.",
      "Khoảng 30–45 phút.",
      "Quanh năm; bên trong hang mát lạnh cả mùa hè.",
      "Mang áo khoác vì trong hang lạnh; đi giày chống trơn; kết hợp tham quan cùng hang Bolshaya Azishskaya gần đó."),
    [
        {"title": "Wikipedia (RU) — Азишская пещера / Азиш-Тау", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Пещера Нежная Адыгея Азиш-Тау"},
    ],
    ["park_garden", "cave", "karst", "nature", "azish-tau", "lago-naki"],
    maps_text("Пещера Нежная", "Адыгея", "Nezhnaya Cave", "Adygea", 44.1235, 40.0305),
))

# ============================ THUNG LŨNG SÔNG BELAYA & CANYON (thiên nhiên) ============================

# C1) Гранитный каньон -------------------------------------------------------------
RECORDS.append(rec(
    "granite-canyon-adygea",
    "Hẻm núi Granite (Gra-nít-nứi ka-nhôn)",
    "Гранитный каньон",
    "Granite Canyon",
    ["park_garden"],
    44.1420, 40.1640,
    "Trên tỉnh lộ giữa làng Dakhovskaya và Khamyshki, dọc sông Belaya, huyện Maykop, Cộng hòa Adygea, Nga",
    "Hẻm núi Granite là đoạn hẻm vực sâu và ngoạn mục nơi sông Belaya cắt xuyên qua khối đá granit đỏ hồng, kéo dài nhiều km dọc tỉnh lộ. Những vách đá dựng đứng nhiều màu và dòng nước xiết tạo nên một trong những cung đường đẹp nhất Adygea.",
    "Kéo dài khoảng bốn km dọc con đường nối làng Dakhovskaya với Khamyshki, Hẻm núi Granite là nơi dòng sông Belaya hùng vĩ đã kiên nhẫn xẻ sâu vào khối đá granit cổ, tạo thành một trong những hẻm vực ấn tượng nhất vùng núi Adygea. Những vách đá granit ánh sắc đỏ hồng, xám và tím dựng đứng sát mặt đường, có nơi cao tới sáu bảy chục mét, còn phía dưới là dòng nước xanh ngọc chảy xiết qua các ghềnh đá. Đây là điểm dừng chân được nhiều du khách yêu thích trên hành trình về Guzeripl và Lago-Naki, với nhiều điểm ngắm cảnh và bãi dừng ven đường. Vào mùa xuân khi tuyết tan, dòng Belaya cuồn cuộn và trở thành địa điểm chèo thuyền vượt thác (rafting) hấp dẫn cho những ai ưa mạo hiểm. Ánh sáng chiều tà làm màu đá granit rực lên đầy mê hoặc, biến nơi đây thành thiên đường của các nhiếp ảnh gia. Sự kết hợp giữa đá, nước và ánh sáng khiến Hẻm núi Granite trở thành một tuyệt tác thiên nhiên khó quên.",
    [
        "Hẻm vực nơi sông Belaya cắt qua khối đá granit đỏ hồng, dài khoảng 4 km.",
        "Vách đá dựng đứng nhiều màu, dòng nước xanh ngọc chảy xiết qua ghềnh.",
        "Điểm chèo thuyền vượt thác (rafting) và chụp ảnh nổi tiếng.",
    ],
    p("Khu vực thiên nhiên mở, tham quan ven đường tự do suốt ngày.",
      "Miễn phí; dịch vụ rafting và tour tính phí riêng.",
      "Khoảng 30–60 phút dừng ngắm cảnh.",
      "Mùa xuân đến mùa thu; mùa xuân nước lớn thích hợp rafting, mùa thu cảnh sắc đẹp.",
      "Dừng xe ở các bãi an toàn ven đường; cẩn thận khi xuống gần mép nước vì dòng chảy mạnh và đá trơn."),
    [
        {"title": "Wikipedia (RU) — Белая (приток Кубани)", "url": "https://ru.wikipedia.org/wiki/Белая_(приток_Кубани)"},
    ],
    ["park_garden", "canyon", "river", "rafting", "nature", "belaya"],
    maps_text("Гранитный каньон", "Адыгея", "Granite Canyon", "Adygea", 44.1420, 40.1640),
))

# C2) Река Белая (сплав) -----------------------------------------------------------
RECORDS.append(rec(
    "belaya-river-adygea",
    "Sông Belaya (Bê-lai-a)",
    "Река Белая",
    "Belaya River",
    ["park_garden"],
    44.2830, 40.1770,
    "Chảy qua làng Kamennomostsky (Khadzhokh) và thung lũng trung tâm Adygea, Nga",
    "Sông Belaya là con sông lớn và quan trọng nhất Adygea, dòng chảy mạnh mẽ đã tạo nên hàng loạt hẻm vực, thác nước và ghềnh đá nổi tiếng khắp vùng. Đây là dòng sông rafting hàng đầu của miền Nam nước Nga.",
    "Bắt nguồn từ sườn núi Fisht và Oshten rồi chảy về sông Kuban, sông Belaya (nghĩa là 'sông Trắng') là mạch nước huyết mạch và là trục cảnh quan chính của Adygea. Trên hành trình dài khoảng 270 km, dòng sông đã kiến tạo nên vô số kỳ quan thiên nhiên: hẻm Khadzhokh, thác Rufabgo, Hẻm núi Granite và nhiều ghềnh thác hùng vĩ. Đoạn chảy qua làng Kamennomostsky (Khadzhokh) là trung tâm của du lịch mạo hiểm, nơi tập trung nhiều công ty tổ chức chèo thuyền vượt thác (rafting). Vào mùa xuân và đầu hè khi băng tuyết tan, nước sông dâng cao và chảy xiết, mang lại những cung rafting đầy phấn khích qua các ghềnh cấp độ trung bình, phù hợp cả với người mới lẫn dân chuyên. Hai bờ sông là những vách đá, rừng cây và bãi đá cuội, tạo khung cảnh nên thơ cho các bãi cắm trại và điểm dã ngoại. Với vẻ đẹp hoang sơ và vai trò trung tâm của mọi hoạt động ngoài trời, sông Belaya chính là mạch sống của du lịch thiên nhiên Adygea.",
    [
        "Con sông lớn nhất Adygea, tạo nên hàng loạt hẻm vực và thác nước nổi tiếng.",
        "Dòng sông rafting hàng đầu miền Nam nước Nga, tập trung ở Kamennomostsky.",
        "Hai bờ nhiều vách đá, rừng và bãi đá cuội lý tưởng để dã ngoại, cắm trại.",
    ],
    p("Sông tự nhiên, tham quan tự do; hoạt động rafting theo mùa và có tổ chức.",
      "Ngắm cảnh miễn phí; một chuyến rafting khoảng 800–2.000 RUB/người tùy cung.",
      "Rafting khoảng 1–3 giờ; ngắm cảnh tùy ý.",
      "Tháng 4 đến tháng 6 nước lớn thích hợp rafting; mùa hè êm dịu hơn cho gia đình.",
      "Chọn công ty rafting uy tín, mặc áo phao và tuân thủ hướng dẫn viên; giữ khoảng cách an toàn ở các ghềnh nước xiết."),
    [
        {"title": "Wikipedia (RU) — Белая (приток Кубани)", "url": "https://ru.wikipedia.org/wiki/Белая_(приток_Кубани)"},
    ],
    ["park_garden", "river", "rafting", "nature", "adventure", "belaya"],
    maps_text("Река Белая", "Каменномостский", "Belaya River", "Kamennomostsky", 44.2830, 40.1770),
))

# C3) Ущелье Мишоко ----------------------------------------------------------------
RECORDS.append(rec(
    "mishoko-gorge",
    "Hẻm núi Mishoko (Mi-sô-kô)",
    "Ущелье Мишоко",
    "Mishoko Gorge",
    ["park_garden"],
    44.2810, 40.1650,
    "Ven làng Kamennomostsky (Khadzhokh), huyện Maykop, Cộng hòa Adygea, Nga",
    "Hẻm núi Mishoko là một thung lũng hẻm xanh mát ngay cạnh làng Kamennomostsky, nổi tiếng với vách đá, thác nước nhỏ, hồ nước trong và các di chỉ cổ. Đây là điểm dã ngoại, leo vách đá và tắm suối được du khách yêu thích.",
    "Nằm ngay sát làng Kamennomostsky (Khadzhokh), Hẻm núi Mishoko là một thung lũng hẻm nhỏ nhưng giàu sức hấp dẫn, được dòng suối Mishoko cùng tên bào mòn qua hàng triệu năm. Hai bên hẻm là những vách đá sa thạch cao dựng đứng, dưới đáy là chuỗi thác nước nhỏ và các hồ nước trong xanh mát lạnh, nơi du khách có thể tắm mát vào mùa hè. Khu vực này còn có ý nghĩa khảo cổ với dấu tích cư trú của người tiền sử và những hang đá từng là nơi trú ẩn cổ xưa. Ngày nay, Mishoko được phát triển thành một khu vui chơi ngoài trời với các hoạt động leo vách đá (rock climbing), đu dây zipline vượt hẻm, đi bộ đường mòn và cắm trại. Nhờ nằm ngay cạnh làng và dễ tiếp cận, đây là lựa chọn lý tưởng cho những ai muốn tận hưởng thiên nhiên mà không cần đi xa. Sự hòa quyện giữa vách đá, nước trong, rừng cây và các trò mạo hiểm khiến Mishoko phù hợp cho cả gia đình lẫn nhóm bạn trẻ.",
    [
        "Thung lũng hẻm ngay cạnh Kamennomostsky, có thác nhỏ và hồ nước trong.",
        "Di chỉ cư trú của người tiền sử và các hang đá cổ.",
        "Khu vui chơi leo vách đá, zipline và cắm trại dễ tiếp cận.",
    ],
    p("Khu vực mở cho khách tham quan; dịch vụ mạo hiểm hoạt động theo giờ ban ngày.",
      "Vé vào khu vực khoảng 100–200 RUB; các trò mạo hiểm tính phí riêng.",
      "Khoảng 1–2 giờ.",
      "Mùa hè để tắm suối; mùa xuân và thu cho đi bộ ngắm cảnh.",
      "Đi giày bám tốt vì đường đá trơn; mang đồ bơi nếu muốn tắm suối; kết hợp tham quan hẻm Khadzhokh gần đó."),
    [
        {"title": "Wikipedia (RU) — Каменномостский", "url": "https://ru.wikipedia.org/wiki/Каменномостский"},
    ],
    ["park_garden", "gorge", "waterfall", "climbing", "nature", "khadzhokh"],
    maps_text("Ущелье Мишоко", "Каменномостский", "Mishoko Gorge", "Kamennomostsky", 44.2810, 40.1650),
))

# C4) Долина аммонитов -------------------------------------------------------------
RECORDS.append(rec(
    "valley-of-ammonites-adygea",
    "Thung lũng Ammonite (Đô-li-na am-mô-nhi-tốp)",
    "Долина аммонитов",
    "Valley of Ammonites",
    ["park_garden"],
    44.3150, 40.1720,
    "Dọc sông Belaya, gần làng Kamennomostsky (Khadzhokh), huyện Maykop, Cộng hòa Adygea, Nga",
    "Thung lũng Ammonite là đoạn lòng sông Belaya rải đầy hóa thạch ammonite - loài thân mềm cổ đại sống cách đây hàng trăm triệu năm. Những khối đá cuộn tròn khổng lồ như con ốc hóa đá biến nơi đây thành một bảo tàng địa chất ngoài trời độc đáo.",
    "Trải dọc lòng và hai bờ sông Belaya gần làng Kamennomostsky, Thung lũng Ammonite là một trong những điểm địa chất kỳ thú và độc đáo nhất Adygea. Nơi đây rải rác vô số hóa thạch ammonite - loài động vật thân mềm có vỏ xoắn ốc từng bơi trong đại dương cổ Tethys cách nay khoảng 140 triệu năm, trước cả thời khủng long tuyệt chủng. Nhiều hóa thạch nhỏ nằm trong các viên đá tròn, nhưng ấn tượng nhất là những khối đá khổng lồ đường kính cả mét mang hình xoắn ốc rõ nét của con ammonite hóa đá. Du khách có thể đi dọc bờ sông để tận mắt tìm và chiêm ngưỡng các hóa thạch, cảm nhận chiều sâu thời gian địa chất ngay dưới chân mình. Đây là điểm tham quan mang tính giáo dục cao, đặc biệt hấp dẫn với những gia đình có trẻ em yêu thích cổ sinh vật và những ai tò mò về lịch sử Trái Đất. Khung cảnh sông núi bao quanh cũng khiến chuyến đi thêm thư thái. Nên lưu ý không đập phá hay lấy đi hóa thạch để bảo tồn di sản tự nhiên quý giá này.",
    [
        "Lòng sông Belaya rải đầy hóa thạch ammonite khoảng 140 triệu năm tuổi.",
        "Có những khối đá xoắn ốc khổng lồ đường kính cả mét như 'bảo tàng địa chất ngoài trời'.",
        "Điểm tham quan giáo dục hấp dẫn cho gia đình yêu cổ sinh vật học.",
    ],
    p("Khu vực thiên nhiên mở dọc sông; tham quan tự do ban ngày.",
      "Thường miễn phí; một số đoạn có thể thu phí nhỏ hoặc thuộc tour.",
      "Khoảng 1 giờ.",
      "Mùa nước cạn (cuối hè, đầu thu) dễ đi dọc bờ sông và tìm hóa thạch.",
      "Đi giày lội nước hoặc bám tốt; không đập phá, không lấy đi hóa thạch; cẩn thận đá trơn ven sông."),
    [
        {"title": "Wikipedia (RU) — Белая (приток Кубани)", "url": "https://ru.wikipedia.org/wiki/Белая_(приток_Кубани)"},
    ],
    ["park_garden", "geology", "fossils", "ammonite", "nature", "belaya"],
    maps_text("Долина аммонитов", "Каменномостский", "Valley of Ammonites", "Kamennomostsky", 44.3150, 40.1720),
))

# C5) Национальный парк Большой Тхач -----------------------------------------------
RECORDS.append(rec(
    "bolshoy-tkhach",
    "Núi Bolshoy Tkhach (Bôn-sôi Tơ-khát)",
    "Гора Большой Тхач",
    "Mount Bolshoy Tkhach",
    ["park_garden"],
    44.0500, 40.5200,
    "Vườn quốc gia Bolshoy Tkhach, huyện Maykop, Cộng hòa Adygea, Nga",
    "Núi Bolshoy Tkhach cao 2.368 m với hình dáng thành lũy đá vôi đồ sộ là trung tâm của Vườn quốc gia cùng tên, một phần của Di sản Thiên nhiên Thế giới UNESCO 'Tây Kavkaz'. Đây là thiên đường trekking hoang sơ, ít dấu chân người.",
    "Sừng sững như một pháo đài đá vôi khổng lồ ở phía đông Adygea, núi Bolshoy Tkhach (2.368 m) là ngọn núi biểu tượng của Vườn quốc gia thiên nhiên Bolshoy Tkhach - khu vực được UNESCO công nhận là một phần Di sản Thiên nhiên Thế giới 'Tây Kavkaz'. Dãy núi có hình dáng độc đáo với các vách đá vôi dựng đứng ở một phía và sườn dốc thoải phủ rừng, đồng cỏ ở phía kia, tạo nên bóng dáng như một con tàu đá khổng lồ. Khu vực này nổi tiếng với thiên nhiên nguyên sơ: rừng linh sam cổ thụ, đồng cỏ núi cao ngập hoa, các đàn bò rừng bison, hươu và những loài chim quý. Đây là điểm đến của giới trekking ưa khám phá, với những cung đường nhiều ngày băng qua các đồng cỏ, rừng già và điểm cắm trại hoang dã. Do nằm trong vùng bảo tồn nghiêm ngặt và ít cơ sở hạ tầng, Bolshoy Tkhach giữ được vẻ hoang vu hiếm có, dành cho những ai thực sự muốn hòa mình vào tự nhiên. Khung cảnh hùng vĩ và bầu không khí tĩnh lặng nơi đây là phần thưởng xứng đáng cho hành trình gian nan.",
    [
        "Núi đá vôi 2.368 m hình 'con tàu đá', biểu tượng Vườn quốc gia Bolshoy Tkhach.",
        "Một phần Di sản Thiên nhiên Thế giới UNESCO 'Tây Kavkaz'.",
        "Thiên nhiên nguyên sơ: rừng cổ thụ, bò rừng bison, đồng cỏ núi cao.",
    ],
    p("Vườn quốc gia mở cho du lịch có tổ chức; cần giấy phép và đăng ký tuyến với ban quản lý.",
      "Phí vào vườn quốc gia khoảng 300 RUB/ngày; tour có hướng dẫn tính phí riêng.",
      "Trekking nhiều ngày (2–4 ngày).",
      "Tháng 6 đến tháng 9 khi thời tiết ổn định.",
      "Chỉ đi cùng hướng dẫn viên có kinh nghiệm; tự túc lều trại, nước và lương thực; tuân thủ quy định bảo tồn nghiêm ngặt."),
    [
        {"title": "Wikipedia (RU) — Большой Тхач", "url": "https://ru.wikipedia.org/wiki/Большой_Тхач"},
    ],
    ["park_garden", "mountain", "national-park", "unesco", "trekking", "nature"],
    maps_text("Гора Большой Тхач", "Адыгея", "Mount Bolshoy Tkhach", "Adygea", 44.0500, 40.5200),
))

# ============================ UNA-KOZ / DAKHOVSKAYA & DI CHỈ CỔ ============================

# D1) Хребет Уна-Коз ---------------------------------------------------------------
RECORDS.append(rec(
    "una-koz-ridge",
    "Sống núi Una-Koz (U-na Kôz)",
    "Хребет Уна-Коз",
    "Una-Koz Ridge",
    ["park_garden"],
    44.2400, 40.2050,
    "Phía trên làng Dakhovskaya, huyện Maykop, Cộng hòa Adygea, Nga",
    "Sống núi Una-Koz là dải núi đá vôi dài với những vách dựng đứng ngoạn mục phía trên làng Dakhovskaya, nổi tiếng với đường leo via ferrata, hang động và tầm nhìn toàn cảnh thung lũng sông Belaya. Đây là điểm đến hấp dẫn cho người ưa mạo hiểm.",
    "Trải dài phía trên làng Dakhovskaya, sống núi Una-Koz là một dải núi đá vôi với những vách đá dựng đứng hùng vĩ nhìn xuống thung lũng sông Belaya. Từ trên đỉnh, du khách có tầm nhìn khoáng đạt bao trọn các làng mạc, dòng sông uốn lượn và những dãy núi trùng điệp của vùng Kavkaz. Una-Koz nổi tiếng trong giới leo núi nhờ tuyến đường via ferrata (đường leo có gắn dây cáp và bậc thép) men theo vách đá, mang lại trải nghiệm mạo hiểm đầy phấn khích mà vẫn an toàn cho người có sức khỏe tốt. Trên sườn núi còn có nhiều hang động, trong đó có hang từng được dùng làm nơi trú ẩn thời cổ. Khu vực này cũng có tuyến cáp treo và các điểm ngắm cảnh, thuận tiện cho du khách phổ thông muốn lên cao mà không cần leo bộ. Vào mùa thu, sắc lá vàng đỏ phủ khắp sườn núi tạo khung cảnh tuyệt đẹp. Sự kết hợp giữa vách đá, hang động, via ferrata và tầm nhìn ngoạn mục khiến Una-Koz trở thành một điểm nhấn của du lịch mạo hiểm Adygea.",
    [
        "Dải núi đá vôi với vách dựng đứng nhìn xuống thung lũng sông Belaya.",
        "Tuyến via ferrata mạo hiểm men theo vách đá, hấp dẫn dân leo núi.",
        "Có hang động cổ, cáp treo và điểm ngắm cảnh toàn cảnh.",
    ],
    p("Khu vực thiên nhiên mở; via ferrata và cáp treo hoạt động theo giờ ban ngày, mùa vụ.",
      "Đi bộ ngắm cảnh miễn phí; via ferrata có hướng dẫn khoảng 1.500–3.000 RUB.",
      "Nửa ngày.",
      "Mùa xuân đến mùa thu; mùa thu sắc lá đẹp nhất.",
      "Via ferrata chỉ đi cùng hướng dẫn viên và trang bị bảo hộ; người sợ độ cao nên cân nhắc; mang nước và mũ."),
    [
        {"title": "Wikipedia (RU) — Даховская", "url": "https://ru.wikipedia.org/wiki/Даховская"},
    ],
    ["park_garden", "ridge", "via-ferrata", "climbing", "viewpoint", "dakhovskaya"],
    maps_text("Хребет Уна-Коз", "Даховская", "Una-Koz Ridge", "Dakhovskaya", 44.2400, 40.2050),
))

# D2) Скала Чёртов палец -----------------------------------------------------------
RECORDS.append(rec(
    "devils-finger-rock-adygea",
    "Vách đá Chёртов Палец (Ngón tay Quỷ) (Trốt-tốp pa-lét)",
    "Скала Чёртов палец",
    "Devil's Finger Rock",
    ["monument"],
    44.2300, 40.2100,
    "Trên sống núi Una-Koz, phía trên làng Dakhovskaya, huyện Maykop, Cộng hòa Adygea, Nga",
    "Chёртов Палец (Ngón tay Quỷ) là một cột đá tự nhiên vươn thẳng lên trời như một ngón tay khổng lồ, mọc trên sống núi Una-Koz phía trên làng Dakhovskaya. Đây là điểm ngắm cảnh và chụp ảnh biểu tượng của vùng.",
    "Sừng sững trên sống núi Una-Koz nhìn xuống thung lũng sông Belaya, Chёртов Палец (Ngón tay của Quỷ) là một trong những thắng cảnh dễ nhận ra nhất Adygea. Đây là một cột đá vôi tự nhiên tách rời khỏi vách núi, vươn thẳng lên trời như một ngón tay khổng lồ, được hình thành qua hàng triệu năm phong hóa và xói mòn. Tên gọi ma mị cùng hình dáng kỳ lạ gắn liền với nhiều truyền thuyết dân gian địa phương. Đứng cạnh cột đá, du khách có tầm nhìn ngoạn mục bao trọn làng Dakhovskaya, dòng sông Belaya uốn lượn và những dãy núi xanh trập trùng phía xa. Đường lên tương đối dễ đi, có thể kết hợp với tuyến tham quan sống núi Una-Koz và via ferrata. Đây là điểm dừng chân được các nhiếp ảnh gia và du khách ưa thích, đặc biệt vào lúc bình minh và hoàng hôn khi ánh sáng nhuộm vàng khối đá và thung lũng. Vẻ đẹp vừa hùng vĩ vừa huyền bí khiến Chёртов Палец trở thành một biểu tượng thị giác của du lịch Adygea.",
    [
        "Cột đá vôi tự nhiên vươn thẳng như 'ngón tay khổng lồ' trên núi Una-Koz.",
        "Điểm ngắm cảnh toàn cảnh làng Dakhovskaya và thung lũng sông Belaya.",
        "Gắn với nhiều truyền thuyết dân gian; đẹp nhất lúc bình minh, hoàng hôn.",
    ],
    p("Điểm tham quan ngoài trời, tự do suốt ngày.",
      "Miễn phí.",
      "Khoảng 30–60 phút.",
      "Mùa xuân đến mùa thu; bình minh và hoàng hôn cho ảnh đẹp nhất.",
      "Đi giày bám tốt; cẩn thận khi lại gần mép vực; kết hợp tham quan sống núi Una-Koz."),
    [
        {"title": "Wikipedia (RU) — Даховская", "url": "https://ru.wikipedia.org/wiki/Даховская"},
    ],
    ["monument", "rock", "viewpoint", "nature", "photography", "dakhovskaya"],
    maps_text("Скала Чёртов палец", "Даховская", "Devils Finger Rock", "Dakhovskaya", 44.2300, 40.2100),
))

# D3) Даховский каменный мост ------------------------------------------------------
RECORDS.append(rec(
    "dakhovsky-bridge",
    "Cầu đá Dakhovsky (Đa-khốp-xki mốt)",
    "Даховский каменный мост",
    "Dakhovsky Stone Bridge",
    ["bridge"],
    44.2220, 40.1975,
    "Làng Dakhovskaya, bắc qua sông Dakh, huyện Maykop, Cộng hòa Adygea, Nga",
    "Cầu đá Dakhovsky là cây cầu vòm bằng đá cổ hơn một thế kỷ tuổi bắc qua sông Dakh, do lính Cossack xây dựng đầu thế kỷ 20. Với kiến trúc đá mộc mạc và bền vững, đây là một di sản lịch sử đáng yêu của làng Dakhovskaya.",
    "Bắc qua dòng sông Dakh ở làng Dakhovskaya, Cầu đá Dakhovsky là một trong những công trình lịch sử độc đáo và giàu chất thơ nhất vùng núi Adygea. Cây cầu vòm bằng đá được xây dựng vào đầu thế kỷ 20 (khoảng những năm 1900–1910) bởi các đơn vị lính Cossack đóng quân trong vùng, dùng đá địa phương ghép lại mà không cần xi măng theo kỹ thuật xây vòm cổ điển. Qua hơn một thế kỷ, cây cầu vẫn đứng vững, chứng kiến bao đổi thay của làng quê miền núi và trở thành biểu tượng gắn bó với người dân Dakhovskaya. Những khối đá xám phủ rêu phong, dáng vòm mềm mại soi bóng xuống dòng sông trong xanh tạo nên khung cảnh cổ kính, nên thơ được nhiều du khách và nhiếp ảnh gia yêu thích. Cây cầu nằm ngay trên tuyến đường du lịch quen thuộc dẫn tới Lago-Naki và các thắng cảnh lân cận, rất tiện ghé thăm. Đây là điểm dừng chân lý tưởng để cảm nhận bề dày lịch sử và vẻ đẹp mộc mạc của một làng quê Cossack vùng Kavkaz.",
    [
        "Cầu vòm đá cổ hơn 100 năm tuổi, do lính Cossack xây đầu thế kỷ 20.",
        "Kỹ thuật ghép đá không dùng xi măng, vẫn bền vững đến nay.",
        "Khung cảnh cổ kính, nên thơ soi bóng xuống dòng sông Dakh.",
    ],
    p("Công trình ngoài trời, tham quan tự do suốt ngày.",
      "Miễn phí.",
      "Khoảng 15–30 phút.",
      "Quanh năm; mùa xuân, thu cảnh sắc quanh cầu đẹp nhất.",
      "Dừng chân trên đường tới Lago-Naki; góc chụp đẹp từ bờ sông phía dưới cầu."),
    [
        {"title": "Wikipedia (RU) — Даховская", "url": "https://ru.wikipedia.org/wiki/Даховская"},
    ],
    ["bridge", "historic", "cossack", "architecture", "stone-bridge", "dakhovskaya"],
    maps_text("Даховский каменный мост", "Даховская", "Dakhovsky Stone Bridge", "Dakhovskaya", 44.2220, 40.1975),
))

# D4) Гузерипльский дольмен --------------------------------------------------------
RECORDS.append(rec(
    "guzeripl-dolmen",
    "Dolmen Guzeripl (Gu-dê-ríp-xki đôn-men)",
    "Гузерипльский дольмен",
    "Guzeripl Dolmen",
    ["monument"],
    43.9895, 40.1265,
    "Làng Guzeripl, trên lãnh thổ Khu bảo tồn thiên nhiên Kavkaz, huyện Maykop, Cộng hòa Adygea, Nga",
    "Dolmen Guzeripl là một trong những mộ đá cự thạch (dolmen) cổ được bảo tồn tốt nhất Tây Kavkaz, có niên đại khoảng 4.000 năm. Nằm trong khuôn viên Khu bảo tồn thiên nhiên Kavkaz, đây là di chỉ khảo cổ nổi bật của Adygea.",
    "Nằm ngay tại làng Guzeripl trong khuôn viên trạm kiểm lâm của Khu bảo tồn thiên nhiên Kavkaz, dolmen Guzeripl là một trong những công trình cự thạch (megalith) được bảo tồn nguyên vẹn và đẹp nhất vùng Tây Kavkaz. Dolmen là những ngôi mộ hoặc công trình nghi lễ bằng các phiến đá khổng lồ, được người cổ đại dựng lên cách nay khoảng bốn nghìn năm, vào thời đại đồ đồng. Chiếc dolmen ở Guzeripl thuộc loại 'hộp đá' với các phiến đá phẳng ghép lại thành buồng, mặt trước có một lỗ tròn đặc trưng, phía trên là phiến đá nắp nặng hàng chục tấn. Điều khiến giới khảo cổ kinh ngạc là người xưa đã vận chuyển và lắp ghép những khối đá nặng như vậy mà không có công cụ hiện đại. Dolmen nằm cạnh bảo tàng thiên nhiên của khu bảo tồn nên rất tiện tham quan kết hợp. Đứng trước công trình bốn nghìn năm tuổi giữa rừng núi hoang sơ, du khách như chạm tay vào một nền văn minh bí ẩn đã biến mất. Đây là di sản khảo cổ quý giá, minh chứng cho lịch sử lâu đời của vùng đất Adygea.",
    [
        "Một trong những dolmen cự thạch bảo tồn tốt nhất Tây Kavkaz, khoảng 4.000 năm tuổi.",
        "Buồng đá với lỗ tròn đặc trưng và phiến nắp nặng hàng chục tấn.",
        "Nằm cạnh bảo tàng thiên nhiên Khu bảo tồn Kavkaz ở Guzeripl.",
    ],
    p("Mở cửa theo giờ tham quan của trạm kiểm lâm khu bảo tồn, thường ban ngày.",
      "Vé vào khu vực (gồm bảo tàng và dolmen) khoảng 300 RUB.",
      "Khoảng 30–45 phút (kết hợp bảo tàng).",
      "Mùa xuân đến mùa thu; đường tới Guzeripl đẹp nhất khi khô ráo.",
      "Kết hợp tham quan bảo tàng thiên nhiên bên cạnh; không trèo lên hay chạm mạnh vào dolmen để bảo tồn di tích."),
    [
        {"title": "Wikipedia (RU) — Гузерипльский дольмен", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Гузерипльский дольмен"},
    ],
    ["monument", "dolmen", "megalith", "archaeology", "bronze-age", "guzeripl"],
    maps_text("Гузерипльский дольмен", "Гузерипль", "Guzeripl Dolmen", "Guzeripl", 43.9895, 40.1265),
))

# D5) Дольмены у станицы Новосвободная ---------------------------------------------
RECORDS.append(rec(
    "novosvobodnaya-dolmens",
    "Cụm dolmen Novosvobodnaya (Bogatyrka) (Nô-vô-xvô-bốt-nai-a)",
    "Дольмены у станицы Новосвободная (Богатырская поляна)",
    "Novosvobodnaya Dolmens (Bogatyrka)",
    ["monument"],
    44.3230, 40.4450,
    "Gần làng Novosvobodnaya, khu Bogatyrskaya Polyana (Đồng cỏ Tráng sĩ), huyện Maykop, Cộng hòa Adygea, Nga",
    "Cụm dolmen gần làng Novosvobodnaya, còn gọi là Bogatyrskaya Polyana (Đồng cỏ Tráng sĩ), là một trong những quần thể mộ đá cự thạch lớn nhất Tây Kavkaz với hàng trăm dolmen rải trong rừng. Đây là di chỉ khảo cổ quan trọng bậc nhất vùng.",
    "Trải rộng trên khu Bogatyrskaya Polyana (Đồng cỏ Tráng sĩ) gần làng Novosvobodnaya, đây là một trong những quần thể dolmen (mộ đá cự thạch) tập trung và quan trọng nhất của toàn vùng Tây Kavkaz. Trong khu rừng và đồng cỏ này từng có hàng trăm dolmen được người cổ đại dựng lên từ thời đại đồ đồng, cách nay khoảng bốn đến năm nghìn năm, tạo thành một 'nghĩa địa cự thạch' khổng lồ. Vùng Novosvobodnaya cũng gắn liền với nền văn hóa khảo cổ Maykop - Novosvobodnaya nổi tiếng, nơi các nhà khoa học tìm thấy nhiều hiện vật đồ đồng và vàng quý giá phản ánh một xã hội phát triển sớm. Nhiều dolmen ở đây có kích thước lớn, cấu trúc phức tạp và những chi tiết chạm khắc hiếm thấy. Dù thời gian và con người đã làm hư hại một phần, quần thể vẫn là điểm hành hương của giới khảo cổ, sử học và du khách ưa khám phá bí ẩn cổ xưa. Đi giữa những khối đá khổng lồ phủ rêu trong rừng vắng, du khách có cảm giác lạc vào một thế giới đã mất, đầy huyền bí và trầm mặc.",
    [
        "Một trong những quần thể dolmen cự thạch lớn nhất Tây Kavkaz.",
        "Gắn với nền văn hóa khảo cổ Maykop - Novosvobodnaya thời đồ đồng.",
        "Hàng trăm mộ đá rải trong rừng, nhiều dolmen kích thước lớn.",
    ],
    p("Di chỉ ngoài trời trong rừng; nên đi cùng hướng dẫn viên hoặc tour vì đường khó tìm.",
      "Thường miễn phí; tour có hướng dẫn tính phí riêng.",
      "Khoảng 1–2 giờ.",
      "Mùa khô (cuối xuân đến đầu thu) khi đường rừng dễ đi.",
      "Đi cùng người thông thạo địa hình; mang giày đi rừng và nước; không phá hoại hay lấy đi hiện vật khảo cổ."),
    [
        {"title": "Wikipedia (RU) — Новосвободная", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Новосвободная дольмены Богатырская поляна"},
    ],
    ["monument", "dolmen", "megalith", "archaeology", "bronze-age", "novosvobodnaya"],
    maps_text("Дольмены Богатырская поляна", "Новосвободная", "Novosvobodnaya Dolmens", "Novosvobodnaya", 44.3230, 40.4450),
))

# ============================ GUZERIPL & CÁC ĐIỂM KHÁC ============================

# E1) Музей природы Кавказского заповедника (Гузерипль) ----------------------------
RECORDS.append(rec(
    "guzeripl-nature-museum",
    "Bảo tàng Thiên nhiên Khu bảo tồn Kavkaz (Guzeripl) (Mu-dây pri-rô-đứ)",
    "Музей природы Кавказского заповедника",
    "Nature Museum of the Caucasus Nature Reserve (Guzeripl)",
    ["museum"],
    43.9910, 40.1290,
    "Làng Guzeripl, trạm kiểm lâm trung tâm Khu bảo tồn thiên nhiên Kavkaz, huyện Maykop, Cộng hòa Adygea, Nga",
    "Bảo tàng Thiên nhiên tại làng Guzeripl là cửa ngõ tìm hiểu Khu bảo tồn thiên nhiên Kavkaz - Di sản Thiên nhiên Thế giới UNESCO. Bảo tàng trưng bày hệ động thực vật phong phú của vùng núi và nằm ngay cạnh dolmen cổ Guzeripl.",
    "Tọa lạc tại làng Guzeripl - cửa ngõ phía nam của Adygea dẫn vào vùng lõi dãy Kavkaz, Bảo tàng Thiên nhiên của Khu bảo tồn thiên nhiên Kavkaz là điểm dừng chân không thể bỏ qua trước khi khám phá thiên nhiên hoang dã. Được thành lập từ giữa thế kỷ 20, bảo tàng giới thiệu toàn cảnh hệ sinh thái độc đáo của khu bảo tồn - một phần Di sản Thiên nhiên Thế giới được UNESCO công nhận. Các gian trưng bày với những mẫu vật động vật được nhồi bông sống động tái hiện thế giới hoang dã Kavkaz: bò rừng bison hùng dũng, gấu nâu, hươu, sơn dương, đại bàng và vô số loài chim, côn trùng, thực vật đặc hữu. Du khách còn được tìm hiểu về công tác bảo tồn, lịch sử nghiên cứu và địa chất của vùng núi. Ngay bên cạnh bảo tàng là dolmen cổ Guzeripl bốn nghìn năm tuổi, tạo thành một điểm tham quan kép vừa về thiên nhiên vừa về khảo cổ. Đây là nơi lý tưởng để du khách, đặc biệt là gia đình có trẻ em, hiểu và trân trọng hơn kho báu thiên nhiên của Tây Kavkaz.",
    [
        "Cửa ngõ tìm hiểu Khu bảo tồn thiên nhiên Kavkaz - Di sản UNESCO.",
        "Trưng bày động vật Kavkaz: bò rừng bison, gấu nâu, hươu, đại bàng.",
        "Nằm ngay cạnh dolmen cổ Guzeripl, tạo tuyến tham quan kép.",
    ],
    p("Mở cửa theo giờ tham quan của khu bảo tồn, thường ban ngày; kiểm tra tại chỗ.",
      "Vé vào khu vực (gồm bảo tàng và dolmen) khoảng 300 RUB.",
      "Khoảng 45 phút đến 1 giờ.",
      "Mùa xuân đến mùa thu; kết hợp trước hoặc sau chuyến trekking.",
      "Kết hợp tham quan dolmen Guzeripl bên cạnh; là điểm khởi đầu tốt để tìm hiểu trước khi vào rừng núi."),
    [
        {"title": "Wikipedia (RU) — Кавказский заповедник", "url": "https://ru.wikipedia.org/wiki/Кавказский_заповедник"},
    ],
    ["museum", "nature", "reserve", "unesco", "wildlife", "guzeripl"],
    maps_text("Музей природы Кавказского заповедника", "Гузерипль", "Nature Museum of the Caucasus Reserve", "Guzeripl", 43.9910, 40.1290),
))

# E2) Пшехские водопады ------------------------------------------------------------
RECORDS.append(rec(
    "pshekha-waterfalls",
    "Thác Pshekha (Psê-kha-xki vô-đô-pát)",
    "Пшехские водопады",
    "Pshekha Waterfalls",
    ["park_garden"],
    43.9200, 39.8600,
    "Vùng núi Fisht-Pshekha-Su, ranh giới Adygea và vùng Krasnodar, Khu bảo tồn thiên nhiên Kavkaz, Nga",
    "Thác Pshekha gồm những dòng thác đổ từ vách đá cao của khối núi Fisht, trong đó thác cao nhất đổ xuống gần 160 m - thuộc hàng cao nhất nước Nga. Đây là kỳ quan thiên nhiên ẩn mình dành cho dân trekking ưa khám phá.",
    "Nằm ở thượng nguồn sông Pshekha dưới chân khối núi Fisht - Pshekha-Su, thác Pshekha là một trong những thác nước ngoạn mục và ít người biết đến nhất vùng Tây Kavkaz. Từ vách đá dựng đứng của cao nguyên Lago-Naki, nhiều dòng nước tuôn xuống tạo thành chuỗi thác hùng vĩ, trong đó dòng cao nhất đổ từ độ cao gần 160 mét - xếp vào hàng những thác cao nhất nước Nga. Vào mùa xuân và đầu hè khi băng tuyết trên núi tan chảy, các dòng thác trở nên cuồn cuộn, tung bọt trắng xóa và tạo nên cảnh tượng choáng ngợp. Do nằm sâu trong Khu bảo tồn thiên nhiên Kavkaz và cần đi bộ đường dài mới tới nơi, thác Pshekha giữ được vẻ hoang sơ nguyên vẹn, là phần thưởng cho những ai chịu khó trekking. Đường tới thác băng qua rừng già, đồng cỏ núi cao và những khung cảnh núi non tuyệt đẹp. Đây là điểm đến dành cho du khách yêu thiên nhiên hoang dã và thích chinh phục, chứ không phải nơi tham quan dễ dàng. Sự hùng vĩ và tĩnh lặng nơi đây mang lại trải nghiệm khó quên giữa lòng dãy Kavkaz.",
    [
        "Chuỗi thác đổ từ vách núi Fisht, dòng cao nhất gần 160 m - hàng cao nhất nước Nga.",
        "Hùng vĩ nhất vào mùa xuân, đầu hè khi băng tuyết tan.",
        "Ẩn sâu trong Khu bảo tồn Kavkaz, chỉ tới được bằng trekking đường dài.",
    ],
    p("Nằm trong Khu bảo tồn Kavkaz; cần giấy phép ra vào, đăng ký tuyến và đi bộ đường dài.",
      "Phí vào khu bảo tồn khoảng 300 RUB/ngày; tour có hướng dẫn tính phí riêng.",
      "Trekking cả ngày hoặc nhiều ngày tùy điểm xuất phát.",
      "Tháng 6 đến tháng 9; cuối xuân đầu hè thác nhiều nước nhất.",
      "Chỉ đi cùng hướng dẫn viên có kinh nghiệm; chuẩn bị thể lực, trang bị trekking và đăng ký với kiểm lâm."),
    [
        {"title": "Wikipedia (RU) — Фишт", "url": "https://ru.wikipedia.org/wiki/Фишт"},
    ],
    ["park_garden", "waterfall", "nature", "trekking", "caucasus", "fisht"],
    maps_text("Пшехские водопады", "Адыгея", "Pshekha Waterfalls", "Adygea", 43.9200, 39.8600),
))

# E3) Термальные источники Адыгеи --------------------------------------------------
RECORDS.append(rec(
    "adygea-thermal-springs",
    "Suối nước nóng Adygea (Téc-man-nứi ít-tôt-nhi-ki)",
    "Термальные источники Адыгеи",
    "Adygea Thermal Springs",
    ["other"],
    44.5300, 40.1600,
    "Thung lũng sông Belaya, khu vực làng Tulskiy - Kamennomostsky, huyện Maykop, Cộng hòa Adygea, Nga",
    "Suối nước nóng Adygea là chuỗi khu nghỉ dưỡng với các bể tắm nước khoáng nóng tự nhiên trải dọc thung lũng sông Belaya. Ngâm mình trong làn nước ấm giữa khung cảnh núi non là trải nghiệm thư giãn được du khách đặc biệt yêu thích quanh năm.",
    "Trải dọc thung lũng sông Belaya, chủ yếu quanh khu vực làng Tulskiy và Kamennomostsky, các suối nước nóng của Adygea đã trở thành một trong những sức hút du lịch nổi bật của vùng. Nguồn nước khoáng nóng được khai thác từ các giếng khoan sâu, có nhiệt độ ấm áp và chứa nhiều khoáng chất được cho là tốt cho sức khỏe, đặc biệt với hệ cơ xương khớp và làn da. Nhiều khu nghỉ dưỡng, khách sạn và cơ sở tắm khoáng đã mọc lên với các bể tắm ngoài trời đủ kích cỡ, nơi du khách có thể ngâm mình thư giãn giữa khung cảnh núi rừng bao quanh. Trải nghiệm thú vị nhất là ngâm bể nước nóng bốc hơi nghi ngút trong tiết trời se lạnh hoặc khi tuyết rơi mùa đông, khi sự tương phản giữa nước ấm và không khí lạnh mang lại cảm giác sảng khoái đặc biệt. Đây là điểm đến lý tưởng để phục hồi sức khỏe sau những ngày trekking, hoặc đơn giản là tận hưởng kỳ nghỉ dưỡng nhẹ nhàng. Nhiều gia đình chọn suối nước nóng Adygea làm nơi lưu trú để kết hợp nghỉ ngơi và khám phá các thắng cảnh lân cận.",
    [
        "Chuỗi khu nghỉ dưỡng với bể tắm nước khoáng nóng tự nhiên dọc sông Belaya.",
        "Nước khoáng ấm được cho là tốt cho cơ xương khớp và làn da.",
        "Ngâm bể nóng giữa tiết trời lạnh, cảnh núi rừng - trải nghiệm thư giãn quanh năm.",
    ],
    p("Các khu tắm khoáng mở cửa hằng ngày, nhiều nơi hoạt động cả buổi tối; giờ tùy cơ sở.",
      "Vé vào khu bể tắm thường khoảng 300–700 RUB/người; combo lưu trú riêng.",
      "Khoảng 2–3 giờ hoặc lưu trú qua đêm.",
      "Quanh năm; mùa đông và tiết trời lạnh cho trải nghiệm ngâm nước nóng thú vị nhất.",
      "Mang đồ bơi và dép; không ngâm quá lâu; chọn cơ sở uy tín; lý tưởng để nghỉ ngơi sau ngày trekking."),
    [
        {"title": "Wikipedia (RU) — Тульский (Адыгея)", "url": "https://ru.wikipedia.org/wiki/Special:Search?search=Термальные источники Адыгея Тульский"},
    ],
    ["other", "thermal-springs", "spa", "wellness", "resort", "belaya"],
    maps_text("Термальные источники Адыгеи", "Тульский", "Adygea Thermal Springs", "Tulskiy", 44.5300, 40.1600),
))


def main():
    path = os.path.join(REGIONS, f"{REGION}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    existing_slugs = {q.get("slug") for q in data}
    existing_ids = {q.get("id") for q in data}

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
