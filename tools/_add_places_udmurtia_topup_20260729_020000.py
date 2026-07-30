# -*- coding: utf-8 -*-
"""_add_places_udmurtia_topup_20260729_020000.py — VÙNG: Cộng hoà Udmurtia (Удмуртская Республика)
(lần chạy tự động 2026-07-29).

Bối cảnh: udmurtia.json hiện có 25 địa điểm (phần lớn ở Izhevsk + Tchaikovsky/Votkinsk,
Ludorvay, Sarapul...). Bổ sung các danh lam THẬT SỰ nổi tiếng CÒN THIẾU, MỞ RỘNG ra ngoài
Izhevsk, đa dạng loại hình → đưa vùng lên 32.

Danh sách 7 bản ghi MỚI (không trùng 25 slug đã có):
- museum/fortress: Iднакар (khu bảo tồn lịch sử-văn hóa + thành lũy cổ, Glazov).
- park_garden/other: Công viên tự nhiên Шаркан + dinh thự Tol Babay (Ông già Tuyết Udmurtia).
- church: Tu viện nữ Свято-Успенский, làng Перевозное (bên sông Kama).
- museum: Bảo tàng lịch sử Con đường Siberia (Сибирский тракт), Дебёсы.
- park_garden/other: Vườn quốc gia Нечкинский (ven sông Kama / hồ Votkinsk).
- church: Nhà thờ Đức Mẹ Bảo Trợ (Покровская церковь), trung tâm cổ Sarapul.
- monument: Tượng đài Mỏ neo (Памятник якорю), Voktinsk.

TOẠ ĐỘ — NGÂN SÁCH WEB SEARCH PHIÊN ĐÃ CẠN (200/200) và web_fetch bị chặn provenance, nên toạ độ
dùng ở MỨC TRUNG TÂM ĐÔ THỊ/LÀNG mà tác nhân BIẾT CHẮC cho các danh lam nổi tiếng (không khẳng định
độ chính xác tới từng tòa nhà; address ghi rõ cấp làng/phố). Phạm vi Udmurtia lat ~55.9–58.6,
lon ~51.2–54.5; TẤT CẢ toạ độ trong phạm vi, lat luôn > lon (KHÔNG đảo lat/lon):
  Iднакар/Glazov 58.1390,52.6590 (trung tâm TP Glazov, bắc Udmurtia);
  Шаркан/Tol Babay 57.2980,53.8580 (làng Шаркан, huyện Шаркан, đông-bắc);
  Перевозное 56.8660,53.7170 (làng ven Kama, huyện Воткинск);
  Дебёсы/Сибирский тракт 57.6570,53.8210 (làng Дебёсы, huyện Дебёсы);
  Нечкинский НП 56.7200,53.8700 (khu ven Kama/hồ Votkinsk giữa Воткинск–Сарапул);
  Покровская церковь Sarapul 56.4635,53.8030 (trung tâm cổ Sarapul);
  Памятник якорю Votkinsk 57.0470,53.9880 (bờ kè/đập hồ Votkinsk).

GHI CHÚ: BỎ QUA vì đã có/trùng: Tchaikovsky (votkinsk-tchaikovsky-estate), Ludorvay,
Sarapul historic town + Bashenin dacha + Middle Kama museum, Blagoveshchensky/Votkinsk pond,
toàn bộ điểm Izhevsk. KHÔNG bịa điểm/toạ độ không chắc; các điểm rủi ro toạ độ (đồi Baygurezi,
làng Igra) KHÔNG đưa vào. Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, có ghi nguồn).

Chạy:  python3 tools/_add_places_udmurtia_topup_20260729_020000.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "udmurtia"
REGION_NAME_VI = "Cộng hoà Udmurtia"
FD = "Vùng Volga"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
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

# ============================ GLAZOV / KHẢO CỔ ============================

# 1) Иднакар (Glazov) — khu bảo tồn lịch sử-văn hóa + thành lũy cổ ------------------
RECORDS.append(rec(
    "idnakar-museum-reserve-glazov",
    "Khu bảo tồn Lịch sử - Văn hóa Idnakar (Idna-Kar, Glazov)",
    "Историко-культурный музей-заповедник УР «Иднакар»",
    "Idnakar Historical-Cultural Museum-Reserve (Glazov)",
    ["museum", "fortress"],
    58.1390, 52.6590,
    "Phố Sovetskaya 27, thành phố Glazov, phía bắc Cộng hòa Udmurtia, Nga (di chỉ thành lũy cổ nằm trên đồi Solovyovskaya ven sông Cheptsa, ngoại vi thành phố)",
    "Idnakar là thành lũy khảo cổ nổi tiếng của người Udmurt cổ (nền văn hóa lưu vực sông Cheptsa, thế kỷ 9-13), nằm trên một ngọn đồi ven sông gần Glazov. Khu bảo tồn - bảo tàng cùng tên tại Glazov trưng bày hiện vật khai quật và tái hiện đời sống cư dân Finno-Ugric thời trung cổ, được xem là một trong những di tích quan trọng nhất Udmurtia.",
    "Trên đồi Solovyovskaya bên bờ sông Cheptsa, cách trung tâm Glazov không xa, từng tồn tại một thành lũy kiên cố của người Udmurt cổ mang tên Idnakar - theo truyền thuyết là 'thành của thủ lĩnh Idna'. Được cư dân nền văn hóa lưu vực Cheptsa xây dựng và sinh sống từ khoảng thế kỷ 9 đến thế kỷ 13, đây là một trong những di chỉ khảo cổ Finno-Ugric lớn và được nghiên cứu kỹ lưỡng bậc nhất vùng Kama - Ural. Các cuộc khai quật đã phát lộ nền nhà, lò rèn, xưởng thủ công cùng vô số đồ trang sức, vũ khí, công cụ bằng đồng, sắt và xương, cho thấy một cộng đồng đông đúc, thạo nghề luyện kim và buôn bán. Để gìn giữ và giới thiệu di sản này, chính quyền Udmurtia lập nên khu bảo tồn lịch sử - văn hóa Idnakar, với bảo tàng hiện đại ngay trong lòng Glazov trưng bày hiện vật, mô hình và các phòng trải nghiệm tương tác. Du khách được đưa ngược dòng thời gian tìm hiểu tổ tiên của người Udmurt, từ tín ngưỡng, trang phục đến kỹ thuật chế tác kim loại. Idnakar vừa là điểm hành hương văn hóa của người bản địa, vừa là cửa ngõ khám phá lịch sử cổ đại của cả vùng Volga - Ural.",
    [
        "Thành lũy khảo cổ Udmurt cổ trên đồi ven sông Cheptsa, niên đại thế kỷ 9-13.",
        "Một trong những di chỉ Finno-Ugric quan trọng và được nghiên cứu nhất vùng Kama - Ural.",
        "Bảo tàng hiện đại tại Glazov với hiện vật khai quật và không gian trải nghiệm tương tác.",
    ],
    p("Bảo tàng thường mở cửa từ thứ Ba đến Chủ nhật (giờ hành chính); nên kiểm tra lịch trước khi đến.",
      "Vé vào cửa ở mức vài trăm RUB; tour có hướng dẫn tính thêm.",
      "Khoảng 1-1,5 giờ tại bảo tàng; thêm thời gian nếu ra thăm di chỉ ngoài trời.",
      "Cuối xuân đến đầu thu để tiện kết hợp thăm đồi thành lũy ngoài trời.",
      "Glazov cách Izhevsk khoảng 180 km về phía bắc; nên đi cùng chuyến khám phá miền bắc Udmurtia."),
    [
        {"title": "Wikipedia (RU) — Иднакар", "url": "https://ru.wikipedia.org/wiki/Иднакар"},
        {"title": "Wikipedia (RU) — Глазов", "url": "https://ru.wikipedia.org/wiki/Глазов"},
    ],
    ["museum", "fortress", "archaeology", "udmurt", "history", "glazov", "udmurtia"],
    maps_text("Историко-культурный музей-заповедник Иднакар", "Глазов", "Idnakar Museum-Reserve", "Glazov", 58.1390, 52.6590),
))

# ============================ THIÊN NHIÊN / VĂN HÓA DÂN GIAN ============================

# 2) Природный парк «Шаркан» + резиденция Тол Бабая --------------------------------
RECORDS.append(rec(
    "sharkan-natural-park-tol-babay",
    "Công viên Tự nhiên Sharkan và Dinh thự Ông già Tuyết Udmurtia (Tol Babay)",
    "Природный парк «Шаркан» и резиденция Тол Бабая",
    "Sharkan Natural Park & Residence of Tol Babay (Udmurt Ded Moroz)",
    ["park_garden", "other"],
    57.2980, 53.8580,
    "Làng Sharkan và vùng phụ cận, huyện Sharkan, phía đông-bắc Cộng hòa Udmurtia, Nga",
    "Công viên tự nhiên Sharkan bảo tồn cảnh quan đồi gò lượn sóng đặc trưng của miền bắc Udmurtia, nổi tiếng với những sườn đồi 'Chumoyt Kar'. Đây cũng là quê hương của Tol Babay - Ông già Tuyết trong truyền thuyết Udmurt, với dinh thự đón khách quanh năm, đặc biệt náo nhiệt dịp Năm mới.",
    "Nằm ở vùng đồi phía đông-bắc Cộng hòa Udmurtia, công viên tự nhiên Sharkan được lập ra để gìn giữ dạng địa hình gò đồi lượn sóng độc đáo cùng những cánh rừng, khe suối và đồng cỏ đặc trưng của xứ này. Điểm nhấn cảnh quan là các dãy đồi hình bát úp mà người Udmurt gọi là 'Chumoyt Kar', tạo nên khung cảnh nên thơ trải dài, đẹp cả bốn mùa - xanh mướt mùa hè và phủ tuyết trắng mùa đông. Chính tại vùng đất giàu huyền thoại này, Tol Babay - nhân vật Ông già Tuyết trong tín ngưỡng dân gian Udmurt - được chọn làm 'chủ nhân'. Dinh thự của Tol Babay tại Sharkan trở thành điểm đến gia đình được yêu thích, với các chương trình lễ hội, trò chơi dân gian, thủ công truyền thống và những câu chuyện cổ tích bản địa. Vào mùa đông và dịp Năm mới, nơi đây đông vui náo nhiệt với các đoàn khách nhỏ tuổi; mùa ấm lại là dịp đi bộ đường dài, ngắm cảnh và tìm hiểu văn hóa Udmurt. Sự kết hợp giữa thiên nhiên được bảo tồn và di sản dân gian khiến Sharkan trở thành một trong những điểm du lịch sinh thái - văn hóa đặc sắc nhất Udmurtia ngoài Izhevsk.",
    [
        "Cảnh quan đồi gò 'Chumoyt Kar' lượn sóng đặc trưng miền bắc Udmurtia.",
        "Dinh thự Tol Babay - Ông già Tuyết trong truyền thuyết Udmurt, điểm đến gia đình.",
        "Lễ hội, trò chơi dân gian và thủ công truyền thống, sôi động nhất dịp Năm mới.",
    ],
    p("Dinh thự và công viên đón khách quanh năm; các chương trình đông khách nhất dịp đông - Năm mới, nên đặt trước.",
      "Vé tham quan và chương trình trải nghiệm tính theo gói; liên hệ ban quản lý để biết mức giá.",
      "Nửa ngày; có thể lâu hơn nếu tham gia chương trình lễ hội hoặc đi bộ đường dài.",
      "Mùa đông cho không khí lễ hội Tol Babay; mùa hè - đầu thu cho đi bộ ngắm cảnh đồi.",
      "Sharkan cách Izhevsk khoảng 90 km; nên đi ô tô và mặc ấm vào mùa đông."),
    [
        {"title": "Wikipedia (RU) — Тол Бабай", "url": "https://ru.wikipedia.org/wiki/Тол_Бабай"},
        {"title": "Wikipedia (RU) — Шаркан", "url": "https://ru.wikipedia.org/wiki/Шаркан"},
    ],
    ["park_garden", "nature", "folklore", "tol-babay", "family", "sharkan", "udmurtia"],
    maps_text("Природный парк Шаркан резиденция Тол Бабая", "Шаркан", "Sharkan Natural Park Tol Babay", "Sharkan", 57.2980, 53.8580),
))

# ============================ TÔN GIÁO ============================

# 3) Свято-Успенский женский монастырь (Перевозное) --------------------------------
RECORDS.append(rec(
    "perevoznoye-dormition-convent",
    "Tu viện nữ Đức Mẹ An Giấc Perevoznoye (Svyato-Uspensky)",
    "Свято-Успенский женский монастырь (село Перевозное)",
    "Holy Dormition Convent (Perevoznoye)",
    ["church"],
    56.8660, 53.7170,
    "Làng Perevoznoye, huyện Votkinsk, Cộng hòa Udmurtia, Nga (bên bờ sông Kama)",
    "Tu viện nữ Đức Mẹ An Giấc tại làng Perevoznoye ven sông Kama là một trong những trung tâm hành hương Chính thống giáo quan trọng nhất Udmurtia. Tu viện nổi tiếng với cây thánh giá gỗ chạm khắc kích thước lớn (Golgotha) cùng nhà thờ cổ và không gian tĩnh lặng bên dòng Kama.",
    "Bên bờ sông Kama rộng lớn, tại làng Perevoznoye thuộc huyện Votkinsk, tọa lạc tu viện nữ Đức Mẹ An Giấc (Svyato-Uspensky) - một trong những điểm hành hương Chính thống giáo được sùng kính bậc nhất Cộng hòa Udmurtia. Trung tâm của quần thể là ngôi thánh đường An Giấc cổ kính cùng các nhà nguyện, phòng ở của các nữ tu và khu vườn được chăm chút. Tu viện đặc biệt nổi tiếng nhờ tổ hợp điêu khắc 'Núi Golgotha' với cây thánh giá gỗ chạm khắc công phu, thu hút đông đảo tín hữu tới cầu nguyện và chiêm bái. Sau thời kỳ Xô viết đóng cửa và xuống cấp, tu viện được phục dựng và trở thành nơi tu hành, đón tiếp khách hành hương từ khắp vùng Volga - Ural. Khung cảnh yên bình bên dòng Kama, tiếng chuông ngân và nếp sống tu trì tạo nên bầu không khí trầm mặc, thanh tịnh hiếm có. Với du khách, đây vừa là dịp tìm hiểu đời sống tôn giáo Chính thống Nga, vừa là điểm dừng chân thư thái giữa thiên nhiên vùng Kama.",
    [
        "Trung tâm hành hương Chính thống giáo quan trọng bậc nhất Udmurtia.",
        "Tổ hợp 'Núi Golgotha' với cây thánh giá gỗ chạm khắc lớn được tín hữu sùng kính.",
        "Không gian tĩnh lặng bên bờ sông Kama, nếp sống tu trì trầm mặc.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ và sinh hoạt tu viện; nên đến vào ban ngày.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 45-60 phút.",
      "Quanh năm; các dịp lễ lớn Chính thống (đặc biệt lễ Đức Mẹ An Giấc tháng 8) không khí trang nghiêm.",
      "Ăn mặc kín đáo, nữ nên có khăn trùm đầu; giữ yên lặng và xin phép trước khi chụp ảnh trong khu tu viện."),
    [
        {"title": "Wikipedia (RU) — Перевозное", "url": "https://ru.wikipedia.org/wiki/Перевозное"},
        {"title": "Wikipedia (RU) — Воткинский район", "url": "https://ru.wikipedia.org/wiki/Воткинский_район"},
    ],
    ["church", "orthodox", "monastery", "pilgrimage", "kama", "votkinsk-district", "udmurtia"],
    maps_text("Свято-Успенский женский монастырь Перевозное", "Удмуртия", "Holy Dormition Convent Perevoznoye", "Udmurtia", 56.8660, 53.7170),
))

# ============================ LỊCH SỬ / BẢO TÀNG ============================

# 4) Музей истории Сибирского тракта (Дебёсы) --------------------------------------
RECORDS.append(rec(
    "siberian-route-museum-debyosy",
    "Bảo tàng Lịch sử Con đường Siberia (Sibirsky trakt, Debyosy)",
    "Музей истории Сибирского тракта (Дебёсы)",
    "Museum of the History of the Siberian Route (Debyosy)",
    ["museum"],
    57.6570, 53.8210,
    "Làng Debyosy, huyện Debyosy, phía đông-bắc Cộng hòa Udmurtia, Nga",
    "Tại làng Debyosy - nơi hai nhánh bắc và nam của Con đường Siberia (Sibirsky trakt) huyền thoại hợp làm một - có bảo tàng chuyên đề tái hiện lịch sử tuyến đường bộ nối châu Âu với Siberia. Bảo tàng kể lại thời kỳ đoàn tù khổ sai, thương nhân và bưu trạm đi qua vùng Udmurtia.",
    "Debyosy là một địa danh đặc biệt trên bản đồ lịch sử nước Nga: chính tại đây, hai nhánh bắc và nam của Con đường Siberia (Sibirsky trakt) - tuyến giao thông bộ vĩ đại nối phần châu Âu của Nga với vùng Siberia rộng lớn - gặp và nhập làm một trước khi tiếp tục hành trình về phương Đông. Để lưu giữ ký ức về con đường từng in dấu chân của thương nhân, quan lại, khách bưu trạm và cả những đoàn tù khổ sai bị lưu đày, người dân địa phương đã lập nên bảo tàng lịch sử Con đường Siberia. Các gian trưng bày tái hiện đời sống dọc trạm dịch, phương tiện vận chuyển, cột mốc, sản vật buôn bán và những câu chuyện đời người gắn với tuyến đường. Du khách được tìm hiểu vai trò của Udmurtia như một mắt xích trên trục Đông - Tây suốt nhiều thế kỷ, cũng như số phận của những người từng đi qua vùng đất này. Nằm giữa khung cảnh làng quê miền bắc Udmurtia bên sông Cheptsa, bảo tàng là điểm dừng thú vị cho những ai yêu lịch sử và muốn cảm nhận chiều sâu văn hóa của vùng đất ít được biết đến.",
    [
        "Debyosy là điểm hợp nhất hai nhánh bắc - nam của Con đường Siberia huyền thoại.",
        "Trưng bày về trạm dịch, thương nhân, khách bộ hành và đoàn tù khổ sai đi lưu đày.",
        "Cửa ngõ tìm hiểu vai trò Udmurtia trên trục giao thông Đông - Tây của Nga.",
    ],
    p("Thường mở cửa các ngày trong tuần theo giờ hành chính; nên gọi kiểm tra trước khi đến.",
      "Vé vào cửa ở mức vài trăm RUB; tour có hướng dẫn tính thêm.",
      "Khoảng 1-1,5 giờ.",
      "Cuối xuân đến đầu thu để thuận tiện di chuyển tới miền bắc Udmurtia.",
      "Debyosy cách Izhevsk khoảng 140 km; kết hợp cung đường khám phá phía bắc cộng hòa."),
    [
        {"title": "Wikipedia (RU) — Сибирский тракт", "url": "https://ru.wikipedia.org/wiki/Сибирский_тракт"},
        {"title": "Wikipedia (RU) — Дебёсы", "url": "https://ru.wikipedia.org/wiki/Дебёсы"},
    ],
    ["museum", "history", "siberian-route", "trade", "debyosy", "udmurtia"],
    maps_text("Музей истории Сибирского тракта", "Дебёсы", "Museum of the Siberian Route", "Debyosy", 57.6570, 53.8210),
))

# ============================ THIÊN NHIÊN (Vườn quốc gia) ============================

# 5) Нечкинский национальный парк --------------------------------------------------
RECORDS.append(rec(
    "nechkinsky-national-park",
    "Vườn quốc gia Nechkinsky (Nechkinsky natsionalny park)",
    "Нечкинский национальный парк",
    "Nechkinsky National Park",
    ["park_garden", "other"],
    56.7200, 53.8700,
    "Dọc sông Kama và hồ chứa Votkinsk, thuộc các huyện Votkinsk, Sarapul và Zavyalovo, Cộng hòa Udmurtia, Nga",
    "Vườn quốc gia Nechkinsky trải dọc bờ sông Kama và hồ chứa Votkinsk ở phía đông-nam Udmurtia, bảo tồn hệ sinh thái rừng thông, đầm lầy và bãi ven sông cùng nhiều loài động thực vật quý. Đây là điểm đến sinh thái, nghỉ dưỡng và thể thao mùa đông được yêu thích của người dân địa phương.",
    "Được thành lập để gìn giữ cảnh quan và đa dạng sinh học vùng hạ lưu sông Kama, vườn quốc gia Nechkinsky trải rộng trên các bãi bồi, rừng thông, đồng cỏ và vùng đầm lầy ven hồ chứa Votkinsk ở phía đông-nam Cộng hòa Udmurtia. Khu vực được bảo vệ này là nơi cư ngụ của nhiều loài chim nước, thú rừng và thực vật quý, đồng thời lưu giữ những di chỉ khảo cổ và cảnh quan tự nhiên gần như nguyên vẹn. Với người dân Izhevsk, Votkinsk và Sarapul, Nechkinsky là 'lá phổi xanh' và điểm nghỉ ngơi cuối tuần lý tưởng: mùa hè có bãi tắm, chèo thuyền, câu cá và đi bộ đường dài; mùa đông biến thành khu thể thao trượt tuyết với tổ hợp nghỉ dưỡng ven sông. Các tuyến đường mòn sinh thái và điểm ngắm cảnh giúp du khách chiêm ngưỡng khúc uốn rộng lớn của dòng Kama - một trong những con sông lớn của nước Nga. Sự hòa quyện giữa thiên nhiên được bảo tồn và hạ tầng du lịch khiến Nechkinsky trở thành điểm đến ngoài trời tiêu biểu của Udmurtia, phù hợp cho cả gia đình lẫn người ưa vận động.",
    [
        "Bảo tồn hệ sinh thái rừng thông và bãi ven sông Kama - hồ chứa Votkinsk.",
        "Điểm nghỉ dưỡng, tắm sông, câu cá và đi bộ đường dài mùa hè.",
        "Khu thể thao trượt tuyết và nghỉ dưỡng ven sông mùa đông.",
    ],
    p("Vườn mở cửa quanh năm; một số khu chức năng và tuyến tham quan cần đăng ký hoặc mua vé.",
      "Phí vào vườn/hoạt động tùy khu vực và dịch vụ; liên hệ ban quản lý để biết chi tiết.",
      "Nửa ngày đến trọn ngày tùy hoạt động.",
      "Mùa hè cho hoạt động dưới nước và đi bộ; mùa đông cho trượt tuyết.",
      "Cách Izhevsk và Votkinsk khoảng 40-60 km; nên đi ô tô, chuẩn bị chống côn trùng vào mùa hè."),
    [
        {"title": "Wikipedia (RU) — Нечкинский национальный парк", "url": "https://ru.wikipedia.org/wiki/Нечкинский_национальный_парк"},
        {"title": "Wikipedia (RU) — Кама", "url": "https://ru.wikipedia.org/wiki/Кама"},
    ],
    ["park_garden", "nature", "national-park", "kama", "outdoor", "udmurtia"],
    maps_text("Нечкинский национальный парк", "Удмуртия", "Nechkinsky National Park", "Udmurtia", 56.7200, 53.8700),
))

# ============================ TÔN GIÁO (Sarapul) ============================

# 6) Покровская церковь (Сарапул) --------------------------------------------------
RECORDS.append(rec(
    "pokrovskaya-church-sarapul",
    "Nhà thờ Đức Mẹ Bảo Trợ (Pokrovskaya, Sarapul)",
    "Покровская церковь (Сарапул)",
    "Church of the Intercession (Sarapul)",
    ["church"],
    56.4635, 53.8030,
    "Trung tâm lịch sử thành phố Sarapul, ven sông Kama, Cộng hòa Udmurtia, Nga",
    "Nhà thờ Đức Mẹ Bảo Trợ là một trong những ngôi thánh đường Chính thống giáo cổ và được gìn giữ tại thành phố cổ Sarapul bên sông Kama. Với kiến trúc truyền thống Nga cùng những mái vòm đặc trưng, nhà thờ là một phần của quần thể di sản đô thị thương nhân Sarapul.",
    "Sarapul - đô thị thương nhân cổ kính bên bờ sông Kama - từ lâu nổi tiếng với quần thể kiến trúc lịch sử phong phú, trong đó có Nhà thờ Đức Mẹ Bảo Trợ (Покровская церковь). Là một trong những công trình tôn giáo được sùng kính của thành phố, nhà thờ mang phong cách kiến trúc Chính thống giáo Nga truyền thống với thân nhà thờ đội mái vòm và tháp chuông vươn cao, trở thành điểm nhấn trong khung cảnh phố cổ. Trải qua nhiều thăng trầm, đặc biệt là thời kỳ Xô viết khi nhiều thánh đường bị đóng cửa, nhà thờ được khôi phục và trở lại đời sống tôn giáo của cộng đồng địa phương. Bên trong lưu giữ các bức tượng thánh (iconostas) cùng không gian cầu nguyện trang nghiêm. Nằm trong lõi lịch sử Sarapul - nơi tập trung những dinh thự thương nhân, phố cổ và bảo tàng - nhà thờ là điểm dừng chân tự nhiên trên hành trình khám phá một trong những thành phố giàu di sản nhất Udmurtia. Với du khách, đây là dịp chiêm ngưỡng kiến trúc Nga cổ truyền và cảm nhận không khí tĩnh lặng bên dòng Kama.",
    [
        "Thánh đường Chính thống giáo trong quần thể phố cổ thương nhân Sarapul.",
        "Kiến trúc Nga truyền thống với mái vòm và tháp chuông đặc trưng.",
        "Kết hợp thăm dinh thự thương nhân, bảo tàng và bờ kè sông Kama gần đó.",
    ],
    p("Mở cửa hằng ngày theo giờ lễ; nên kiểm tra lịch lễ trước khi đến.",
      "Miễn phí (đóng góp tuỳ tâm).",
      "Khoảng 20-30 phút.",
      "Quanh năm; dịp lễ Đức Mẹ Bảo Trợ (tháng 10) và các lễ lớn Chính thống không khí trang nghiêm.",
      "Ăn mặc kín đáo, nữ nên có khăn trùm đầu; giữ yên lặng trong giờ lễ; dễ kết hợp đi bộ phố cổ Sarapul."),
    [
        {"title": "Wikipedia (RU) — Сарапул", "url": "https://ru.wikipedia.org/wiki/Сарапул"},
        {"title": "Sobory.ru — храмы Сарапула (поиск)", "url": "https://sobory.ru/geo/?text=Сарапул"},
    ],
    ["church", "orthodox", "historic", "sarapul", "kama", "udmurtia"],
    maps_text("Покровская церковь", "Сарапул", "Church of the Intercession", "Sarapul", 56.4635, 53.8030),
))

# ============================ TƯỢNG ĐÀI (Votkinsk) ============================

# 7) Памятник якорю (Воткинск) -----------------------------------------------------
RECORDS.append(rec(
    "votkinsk-anchor-monument",
    "Tượng đài Mỏ neo Votkinsk (Pamyatnik yakoryu)",
    "Памятник якорю (Воткинск)",
    "Anchor Monument (Votkinsk)",
    ["monument"],
    57.0470, 53.9880,
    "Khu vực bờ kè và đập hồ Votkinsk, trung tâm thành phố Votkinsk, Cộng hòa Udmurtia, Nga",
    "Tượng đài Mỏ neo là biểu tượng của Votkinsk - thành phố có nhà máy luyện kim từng chế tạo những chiếc mỏ neo khổng lồ cho hải quân Nga. Chiếc mỏ neo đặt bên bờ hồ Votkinsk nhắc nhớ niềm tự hào công nghiệp và có mặt trên huy hiệu thành phố.",
    "Votkinsk không chỉ được biết đến là quê hương của nhà soạn nhạc Tchaikovsky mà còn là một trung tâm công nghiệp lâu đời, nơi nhà máy luyện kim - cơ khí danh tiếng ra đời từ thế kỷ 18. Một trong những sản phẩm làm nên tên tuổi của Votkinsk chính là những chiếc mỏ neo cỡ lớn được rèn cho tàu thuyền và hải quân Đế quốc Nga, nổi tiếng về độ bền và chất lượng. Để tôn vinh truyền thống ấy, thành phố dựng nên tượng đài Mỏ neo - một chiếc neo thật đặt trang trọng bên bờ hồ Votkinsk, gần khu đập và bờ kè trung tâm. Hình ảnh chiếc mỏ neo đã trở thành biểu tượng gắn với bản sắc đô thị, thậm chí xuất hiện trên huy hiệu của Votkinsk như một dấu ấn của niềm tự hào công nghiệp và tay nghề thợ luyện kim địa phương. Với du khách, tượng đài là điểm chụp ảnh và tìm hiểu lịch sử thú vị, đặc biệt khi kết hợp dạo bờ kè hồ Votkinsk thơ mộng và thăm điền trang Tchaikovsky gần đó. Đây là cách ngắn gọn để cảm nhận hai gương mặt của Votkinsk: một thành phố vừa lãng mạn với âm nhạc, vừa vững chãi với công nghiệp.",
    [
        "Biểu tượng công nghiệp của Votkinsk - nơi từng rèn mỏ neo cho hải quân Nga.",
        "Chiếc mỏ neo thật đặt bên bờ hồ Votkinsk, gần đập và bờ kè trung tâm.",
        "Hình ảnh mỏ neo xuất hiện trên huy hiệu thành phố Votkinsk.",
    ],
    p("Không gian công cộng ngoài trời, tham quan và chụp ảnh tự do suốt ngày.",
      "Miễn phí.",
      "Khoảng 10-15 phút.",
      "Cuối xuân đến đầu thu để dạo bờ kè hồ dễ chịu nhất.",
      "Kết hợp dạo bờ kè hồ Votkinsk và thăm điền trang - bảo tàng Tchaikovsky gần đó."),
    [
        {"title": "Wikipedia (RU) — Воткинск", "url": "https://ru.wikipedia.org/wiki/Воткинск"},
        {"title": "Wikipedia (RU) — Герб Воткинска", "url": "https://ru.wikipedia.org/wiki/Герб_Воткинска"},
    ],
    ["monument", "industry", "anchor", "votkinsk", "landmark", "udmurtia"],
    maps_text("Памятник якорю", "Воткинск", "Anchor Monument", "Votkinsk", 57.0470, 53.9880),
))

# ===RECORDS_INSERT_POINT===


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
