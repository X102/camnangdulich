# -*- coding: utf-8 -*-
"""_add_places_komi_20260728_221036.py — VÙNG: Cộng hoà Komi (Республика Коми)
(lần chạy tự động 2026-07-28).

Bối cảnh: komi.json hiện có 7 địa điểm (Manpupuner, Pechoro-Ilych, Yugyd Va, Syktyvkar,
Ust-Vym, Finno-Ugric Ethnopark, Ust-Tsilma). Bổ sung 24 địa điểm THẬT SỰ nổi tiếng/đặc sắc
CÒN THIẾU, đa dạng loại hình → đưa vùng lên 31.

Komi nổi bật về THIÊN NHIÊN (núi Ural, sông, hang), bên cạnh trung tâm văn hoá Syktyvkar
(nhà thờ, nhà hát, bảo tàng, quảng trường), các thành phố phương Bắc/Bắc Cực (Vorkuta,
Pechora, Inta, Ukhta) và di sản tôn giáo (tu viện Kyltovo, Ulyanovo).

Phân bố loại hình (24 bản ghi mới):
- museum (4): Национальный музей РК, Национальная галерея РК, Музей И.А. Куратова,
  Геологический музей им. А.А. Чернова.
- theatre (2): Театр оперы и балета РК, Театр драмы им. В. Савина.
- church (4): Свято-Стефановский собор, Свято-Казанский храм (Кочпон), Кылтовский монастырь,
  Троице-Стефано-Ульяновский монастырь.
- monument (2): Пожарная каланча (символ Сыктывкара), Профиль Ленина на горе Ветлосян (Ухта).
- park_garden (6): Кировский парк, гора Народная, гора Манарага, гора Сабля, река Щугор,
  Уньинская пещера.
- square_street (5): Стефановская площадь, Воркута, Печора, Инта, Ухта.
- other (1): Серёгово (соляной курорт).

TOẠ ĐỘ — xác minh chéo (ru.wikipedia geohack/API, OpenStreetMap/Nominatim, sobory.ru, 2ГИС,
tonkosti/russpass, 2026-07-28). Phạm vi Komi lat ~59–68, lon ~46–66 — tất cả toạ độ trong
phạm vi, KHÔNG đảo lat/lon:
  Свято-Стефановский собор 61.67778,50.83139; Театр оперы и балета 61.66611,50.81917
  (Коммунистическая 32); Национальный музей РК 61.66947,50.83815 (Коммунистическая 6);
  Кировский парк 61.67438,50.84140; Национальная галерея РК 61.66949,50.84239 (Кирова 44);
  Театр драмы им. Савина 61.66990,50.82490 (Первомайская 56); Стефановская площадь
  61.66861,50.83556; Свято-Казанский храм (Кочпон) 61.63718,50.87053 (sobory.ru/16... ;
  Набережная 10); Пожарная каланча 61.6731,50.8375 (ru.wiki 61°40′23″N 50°50′15″E,
  Советская 9); Музей И.А. Куратова 61.67350,50.83924 (OSM museum, Орджоникидзе 2);
  Геол. музей Чернова 61.67086,50.82477 (OSM Институт геологии, Первомайская 54);
  Народная 65.0333,60.1167; Манарага 65.0478,59.7628; Сабля 64.77672,58.88796 (OSM peak);
  Щугор устье 64.2533,57.5903; Уньинская пещера 61.781,58.524 (geomem/outdoors);
  Воркута 67.5,64.0333; Печора 65.11667,57.11667; Инта 66.03981,60.13152; Ухта
  63.56667,53.70000; Профиль Ленина (Ветлосян) 63.55884,53.75297; Кылтовский монастырь
  62.32052,50.99436 (sobory); Троице-Стефано-Ульяновский монастырь 61.82470,53.55630;
  Серёгово 62.32601,50.69849 (санаторий).

GHI CHÚ: đã BỎ QUA vì không xác minh được toạ độ tin cậy / trùng lặp / có vấn đề:
  «Богатырь-Щелье» (không có node OSM/bài wiki; nguồn địa chất gắn với sông Bolshaya Synya
  chứ không phải Щугор — toạ độ không chắc), озеро Донты (không có toạ độ tra cứu trực tiếp,
  chỉ ước lượng theo làng Дон), Мемориал жертвам ГУЛАГа ở Юр-Шор/Воркута (toạ độ chỉ theo
  làng, và theo tin 2026 đài đã bị tháo dỡ), Параськины озёра (không có node OSM). KHÔNG
  bịa toạ độ — thành phố Воркута đã bao quát chủ đề Bắc Cực/Gulag/tundra.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_komi_20260728_221036.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "komi"
REGION_NAME_VI = "Cộng hoà Komi"
FD = "Vùng Tây Bắc"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16",
        "google": f"https://www.google.com/maps/search/?api=1&query={gq}",
    }


def maps_org(yandex_org_url, name_en, city_en):
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


def P(hours, ticket, duration, best, tips):
    return {
        "hours_vi": hours,
        "ticket_vi": ticket,
        "duration_vi": duration,
        "best_time_vi": best,
        "tips_vi": tips,
    }


def nature_P(duration, best, tips):
    return P(
        "Đối tượng thiên nhiên ngoài trời, tham quan ban ngày; không có giờ cố định.",
        "Không thu vé cố định; khu vực trong vườn quốc gia/khu bảo tồn cần giấy phép và đăng ký.",
        duration, best, tips,
    )


RECORDS = []

# ==================== SYKTYVKAR — VĂN HOÁ ĐÔ THỊ ====================

# 1) Свято-Стефановский кафедральный собор
RECORDS.append(rec(
    "stefanovsky-cathedral",
    "Nhà thờ chính tòa Thánh Stefan (Stefanovsky)",
    "Свято-Стефановский кафедральный собор",
    "St. Stephen's Cathedral (Syktyvkar)",
    ["church"],
    61.67778, 50.83139,
    "Trung tâm Syktyvkar, cạnh Quảng trường Stefanovskaya, Cộng hòa Komi, Nga.",
    "Nhà thờ chính tòa Thánh Stefan là ngôi thánh đường lớn nhất và là biểu tượng tôn giáo của Syktyvkar, với những mái vòm dát vàng nổi bật giữa trung tâm thành phố. Được xây lại vào đầu thế kỷ 21 để tưởng nhớ Thánh Stefan xứ Perm - người Kitô hóa dân tộc Komi.",
    "Sừng sững ngay trung tâm Syktyvkar, Nhà thờ chính tòa Thánh Stefan (Stefanovsky) là công trình tôn giáo quan trọng nhất của Cộng hòa Komi, mang tên Thánh Stefan xứ Perm - nhà truyền giáo thế kỷ 14 đã đưa Kitô giáo và chữ viết đến với người Komi. Ngôi nhà thờ chính tòa nguyên thủy dựng cuối thế kỷ 19 từng bị phá hủy trong thời kỳ Xô Viết chống tôn giáo. Công trình hiện nay được khởi công cuối những năm 1990 và khánh thành đầu thập niên 2000, phỏng theo phong cách nhà thờ Nga truyền thống với năm mái vòm dát vàng lấp lánh và tháp chuông cao. Bên trong là những bức bích họa, biểu tượng thánh (icon) và không gian cầu nguyện trang nghiêm. Nằm sát Quảng trường Stefanovskaya - trái tim của thành phố, nhà thờ là điểm hành hương, nơi cử hành các đại lễ Chính thống giáo và cũng là mốc kiến trúc dễ nhận biết nhất khi du khách dạo bước ở trung tâm Syktyvkar.",
    [
        "Thánh đường lớn nhất Komi, mang tên Thánh Stefan xứ Perm - người Kitô hóa người Komi",
        "Năm mái vòm dát vàng, xây lại đầu thế kỷ 21 thay cho nhà thờ bị phá thời Xô Viết",
        "Nằm cạnh Quảng trường Stefanovskaya, trung tâm đời sống tôn giáo của thành phố",
    ],
    P(
        "Mở cửa cho tín hữu và khách tham quan hằng ngày, thường từ sáng tới chiều tối; giờ lễ theo lịch phụng vụ.",
        "Vào nhà thờ miễn phí; có thể quyên góp hoặc mua nến, đồ lưu niệm tôn giáo.",
        "Khoảng 30-45 phút.",
        "Quanh năm; đặc biệt sinh động vào các đại lễ Giáng sinh và Phục sinh Chính thống giáo.",
        "Ăn mặc kín đáo, nữ giới nên trùm khăn; giữ yên lặng khi có thánh lễ; kết hợp tham quan Quảng trường Stefanovskaya kề bên.",
    ),
    [
        {"title": "Wikipedia (RU) — Стефановский собор (Сыктывкар)", "url": "https://ru.wikipedia.org/wiki/Стефановский_собор_(Сыктывкар)"},
        {"title": "Sobory.ru — Собор Стефана Пермского", "url": "https://sobory.ru/article/?object=09873"},
    ],
    ["church", "cathedral", "orthodox", "syktyvkar", "landmark", "stephen-of-perm"],
    maps_text("Свято-Стефановский кафедральный собор", "Сыктывкар", "St. Stephen's Cathedral", "Syktyvkar", 61.67778, 50.83139),
))

# 2) Театр оперы и балета Республики Коми
RECORDS.append(rec(
    "komi-opera-ballet-theatre",
    "Nhà hát Opera và Ballet Cộng hòa Komi",
    "Государственный театр оперы и балета Республики Коми",
    "Komi Republic State Opera and Ballet Theatre",
    ["theatre"],
    61.66611, 50.81917,
    "Ул. Коммунистическая 32, Syktyvkar, Cộng hòa Komi, Nga.",
    "Nhà hát Opera và Ballet Cộng hòa Komi là sân khấu nghệ thuật hàn lâm hàng đầu của vùng, nơi trình diễn opera, ballet và nhạc giao hưởng. Nhà hát nổi tiếng với Liên hoan nghệ thuật 'Mùa xuân Sylva' mang tầm quốc gia.",
    "Ra đời năm 1958, Nhà hát Opera và Ballet Cộng hòa Komi là trung tâm nghệ thuật hàn lâm lớn nhất của xứ Komi, tọa lạc trên phố Kommunisticheskaya ở trung tâm Syktyvkar. Sân khấu này dàn dựng các vở opera kinh điển của Nga và thế giới, những vở ballet lừng danh, cùng các buổi hòa nhạc giao hưởng, đồng thời góp phần gìn giữ và phát triển nghệ thuật sân khấu mang bản sắc Komi. Đoàn nhà hát từng lưu diễn nhiều nơi và được đánh giá cao về chất lượng biểu diễn. Sự kiện nổi bật nhất là Liên hoan nghệ thuật opera và ballet 'Mùa xuân Sylva' (Sи́ктывкарса тулыс), tổ chức thường niên từ năm 1991, quy tụ nghệ sĩ khách mời từ khắp nước Nga và quốc tế. Với khán phòng trang nhã và chương trình phong phú, đây là điểm đến không thể bỏ qua cho du khách muốn thưởng thức đời sống văn hóa tinh hoa của thủ phủ Komi.",
    [
        "Nhà hát opera - ballet hàn lâm lớn nhất Komi, thành lập năm 1958",
        "Chủ nhà của Liên hoan nghệ thuật thường niên 'Mùa xuân Sylva' từ năm 1991",
        "Trình diễn opera, ballet kinh điển và các buổi hòa nhạc giao hưởng",
    ],
    P(
        "Mở cửa theo lịch biểu diễn, thường vào buổi tối; phòng vé mở ban ngày.",
        "Vé theo từng suất diễn, giá phải chăng so với các nhà hát lớn ở Nga.",
        "Một buổi diễn khoảng 2-3 giờ.",
        "Mùa diễn thu - xuân; đặc biệt là dịp Liên hoan 'Mùa xuân Sylva' (thường tháng 4-5).",
        "Đặt vé trước qua trang chính thức; đến sớm để kịp gửi áo khoác mùa đông; trang phục lịch sự.",
    ),
    [
        {"title": "Wikipedia (RU) — Театр оперы и балета Республики Коми", "url": "https://ru.wikipedia.org/wiki/Театр_оперы_и_балета_Республики_Коми"},
        {"title": "2ГИС — Театр оперы и балета РК", "url": "https://2gis.ru/syktyvkar"},
    ],
    ["theatre", "opera", "ballet", "syktyvkar", "culture", "festival"],
    maps_text("Государственный театр оперы и балета Республики Коми", "Сыктывкар", "Komi Opera and Ballet Theatre", "Syktyvkar", 61.66611, 50.81917),
))

# 3) Национальный музей Республики Коми
RECORDS.append(rec(
    "national-museum-komi",
    "Bảo tàng Quốc gia Cộng hòa Komi",
    "Национальный музей Республики Коми",
    "National Museum of the Komi Republic",
    ["museum"],
    61.66947, 50.83815,
    "Ул. Коммунистическая 6, Syktyvkar, Cộng hòa Komi, Nga (nhiều tòa nhà ở trung tâm).",
    "Bảo tàng Quốc gia Cộng hòa Komi là bảo tàng lâu đời và lớn nhất vùng, thành lập năm 1911. Bộ sưu tập đồ sộ giới thiệu thiên nhiên, khảo cổ, lịch sử và văn hóa dân tộc Komi qua hàng trăm nghìn hiện vật.",
    "Được thành lập năm 1911, Bảo tàng Quốc gia Cộng hòa Komi là thiết chế bảo tàng lâu đời và quan trọng bậc nhất của xứ Komi, lưu giữ hàng trăm nghìn hiện vật trải rộng nhiều lĩnh vực. Bảo tàng gồm nhiều phân khu và tòa nhà ở trung tâm Syktyvkar, trưng bày về giới tự nhiên phương Bắc (động - thực vật, địa chất), khảo cổ học với các di chỉ cổ xưa, lịch sử vùng đất, và đặc biệt là dân tộc học Komi: trang phục truyền thống, đồ thủ công, dụng cụ săn bắt - đánh cá, tín ngưỡng và nếp sống của người Komi (Zyryan). Đây là nơi lý tưởng để du khách hiểu về cội nguồn, phong tục và bản sắc của dân tộc Finno-Ugric bản địa trước khi khám phá vùng sâu. Bảo tàng cũng thường xuyên tổ chức triển lãm chuyên đề, chương trình giáo dục và sự kiện văn hóa, đóng vai trò trung tâm bảo tồn di sản của cả nước cộng hòa.",
    [
        "Bảo tàng lâu đời nhất Komi, thành lập năm 1911",
        "Bộ sưu tập lớn về thiên nhiên, khảo cổ, lịch sử và dân tộc học Komi",
        "Trưng bày trang phục, đồ thủ công và tín ngưỡng của người Komi bản địa",
    ],
    P(
        "Thường mở cửa 10:00-18:00, nghỉ một ngày đầu tuần; kiểm tra lịch từng phân khu.",
        "Vé vào cửa ở mức phải chăng (thường vài trăm RUB); có vé gộp nhiều phân khu.",
        "Khoảng 1,5-2 giờ cho một tòa trưng bày chính.",
        "Quanh năm; là điểm đến trong nhà lý tưởng cho mùa đông giá lạnh.",
        "Bắt đầu từ phân khu dân tộc học để hiểu văn hóa Komi; hỏi vé gộp nếu muốn xem nhiều tòa nhà.",
    ),
    [
        {"title": "Wikipedia (RU) — Национальный музей Республики Коми", "url": "https://ru.wikipedia.org/wiki/Национальный_музей_Республики_Коми"},
        {"title": "Национальный музей РК (сайт)", "url": "https://museumkomi.ru/"},
    ],
    ["museum", "history", "ethnography", "komi", "syktyvkar", "nature"],
    maps_text("Национальный музей Республики Коми", "Сыктывкар", "National Museum of the Komi Republic", "Syktyvkar", 61.66947, 50.83815),
    official_site="https://museumkomi.ru/",
))

# 4) Кировский парк
RECORDS.append(rec(
    "kirov-park-syktyvkar",
    "Công viên Kirov (Syktyvkar)",
    "Кировский парк (Парк имени С. М. Кирова)",
    "Kirov Park (Syktyvkar)",
    ["park_garden"],
    61.67438, 50.84140,
    "Trung tâm Syktyvkar, bên bờ cao sông Sysola, Cộng hòa Komi, Nga.",
    "Công viên Kirov là công viên trung tâm lâu đời và được yêu thích nhất Syktyvkar, nằm trên bờ cao nhìn ra sông Sysola. Đây là nơi dạo chơi, nghỉ ngơi quen thuộc của người dân với những lối đi rợp bóng cây và đài quan sát ngắm sông.",
    "Trải dài trên bờ cao bên sông Sysola ngay giữa lòng Syktyvkar, Công viên Kirov (mang tên nhà cách mạng S. M. Kirov) là không gian xanh trung tâm và lâu đời của thành phố, gắn bó với nhiều thế hệ cư dân. Có nguồn gốc từ một khu vườn công cộng hình thành từ thế kỷ 19, công viên ngày nay là nơi tản bộ, tập thể dục và thư giãn ưa thích với những hàng cây rợp bóng, lối đi lát đá, đài phun nước, tượng đài và khu vui chơi. Điểm hấp dẫn nhất là điểm ngắm cảnh trên bờ dốc cao, từ đó phóng tầm mắt ra dòng Sysola uốn lượn và vùng đồng bằng bên kia sông - khung cảnh đẹp nhất vào lúc hoàng hôn. Vào mùa hè, công viên nhộn nhịp các sự kiện, lễ hội thành phố; mùa đông lại phủ tuyết trắng thơ mộng. Đây là nơi cảm nhận nhịp sống thư thái của thủ phủ Komi.",
    [
        "Công viên trung tâm lâu đời nhất Syktyvkar, gốc từ khu vườn công cộng thế kỷ 19",
        "Điểm ngắm sông Sysola tuyệt đẹp từ bờ dốc cao, lý tưởng lúc hoàng hôn",
        "Không gian dạo chơi, lễ hội và thư giãn quen thuộc của người dân",
    ],
    P(
        "Công viên mở tự do, có thể dạo chơi cả ngày; các trò chơi/dịch vụ hoạt động ban ngày.",
        "Vào công viên miễn phí; một số trò chơi giải trí thu phí riêng.",
        "Khoảng 45-60 phút.",
        "Cuối xuân đến đầu thu cho cây xanh và ngắm sông; mùa đông đẹp với tuyết.",
        "Ghé điểm ngắm bờ sông lúc hoàng hôn; kết hợp dạo trung tâm và các bảo tàng lân cận.",
    ),
    [
        {"title": "Wikipedia (RU) — Сыктывкар (достопримечательности)", "url": "https://ru.wikipedia.org/wiki/Сыктывкар"},
        {"title": "2ГИС — Кировский парк, Сыктывкар", "url": "https://2gis.ru/syktyvkar"},
    ],
    ["park", "city-park", "river-view", "syktyvkar", "leisure", "sysola"],
    maps_text("Кировский парк", "Сыктывкар", "Kirov Park", "Syktyvkar", 61.67438, 50.84140),
))

# 5) Национальная галерея Республики Коми
RECORDS.append(rec(
    "komi-national-gallery",
    "Phòng trưng bày Nghệ thuật Quốc gia Komi",
    "Национальная галерея Республики Коми",
    "National Gallery of the Komi Republic",
    ["museum"],
    61.66949, 50.84239,
    "Ул. Кирова 44, Syktyvkar, Cộng hòa Komi, Nga.",
    "Phòng trưng bày Nghệ thuật Quốc gia Komi là bảo tàng mỹ thuật chính của vùng, lưu giữ bộ sưu tập hội họa, đồ họa và điêu khắc Nga cùng nghệ thuật của các họa sĩ Komi. Đây là trung tâm đời sống mỹ thuật của Syktyvkar.",
    "Nằm trong một tòa nhà lịch sử trên phố Kirov ở trung tâm Syktyvkar, Phòng trưng bày Nghệ thuật Quốc gia Cộng hòa Komi là bảo tàng mỹ thuật hàng đầu của vùng. Được thành lập năm 1943 (giữa thời chiến), phòng trưng bày sở hữu bộ sưu tập phong phú gồm hội họa, đồ họa, điêu khắc và nghệ thuật trang trí - ứng dụng, trải từ nghệ thuật Nga cổ điển (icon, tranh chân dung) đến hội họa Xô Viết và đương đại. Đặc biệt, nơi đây gìn giữ và tôn vinh tác phẩm của các nghệ sĩ tạo hình Komi, phản ánh thiên nhiên, con người và truyền thống phương Bắc. Bảo tàng thường xuyên tổ chức triển lãm luân phiên, các buổi giao lưu, lớp học nghệ thuật và sự kiện văn hóa. Với du khách yêu mỹ thuật, đây là điểm dừng chân giàu cảm hứng để tìm hiểu tinh thần sáng tạo của xứ Komi trong không gian trưng bày trang nhã.",
    [
        "Bảo tàng mỹ thuật chính của Komi, thành lập năm 1943",
        "Sưu tập hội họa, đồ họa, điêu khắc Nga và nghệ thuật của họa sĩ Komi",
        "Trung tâm triển lãm và giáo dục nghệ thuật của Syktyvkar",
    ],
    P(
        "Thường mở 10:00-18:00, nghỉ một ngày đầu tuần; kiểm tra lịch triển lãm.",
        "Vé vào cửa phải chăng; triển lãm đặc biệt có thể thu vé riêng.",
        "Khoảng 1-1,5 giờ.",
        "Quanh năm; điểm đến trong nhà lý tưởng khi thời tiết lạnh.",
        "Xem lịch triển lãm luân phiên trước khi đến; nhiều tác phẩm về thiên nhiên và con người Komi rất đáng chú ý.",
    ),
    [
        {"title": "Wikipedia (RU) — Национальная галерея Республики Коми", "url": "https://ru.wikipedia.org/wiki/Национальная_галерея_Республики_Коми"},
        {"title": "Национальная галерея РК (сайт)", "url": "https://ngrkomi.ru/"},
    ],
    ["museum", "art-gallery", "fine-arts", "komi", "syktyvkar", "culture"],
    maps_text("Национальная галерея Республики Коми", "Сыктывкар", "National Gallery of the Komi Republic", "Syktyvkar", 61.66949, 50.84239),
    official_site="https://ngrkomi.ru/",
))

# 6) Академический театр драмы имени В. Савина
RECORDS.append(rec(
    "savin-drama-theatre",
    "Nhà hát Kịch hàn lâm mang tên V. Savin",
    "Академический театр драмы имени В. Савина",
    "V. Savin Academic Drama Theatre",
    ["theatre"],
    61.66990, 50.82490,
    "Ул. Первомайская 56, Syktyvkar, Cộng hòa Komi, Nga.",
    "Nhà hát Kịch hàn lâm mang tên Viktor Savin là nhà hát kịch lâu đời nhất Komi, biểu diễn bằng cả tiếng Nga và tiếng Komi. Nhà hát mang tên nhà văn - nhà viết kịch Komi Viktor Savin, người đặt nền móng cho sân khấu dân tộc.",
    "Là nhà hát kịch lâu đời và uy tín nhất Cộng hòa Komi, Nhà hát Kịch hàn lâm mang tên V. Savin có lịch sử từ những năm 1930, gắn với sự ra đời của sân khấu chuyên nghiệp ở xứ Komi. Nhà hát mang tên Viktor Savin (Nёбдінса Виттор) - nhà thơ, nhà viết kịch và nhà hoạt động văn hóa Komi tiên phong, người sáng lập nền kịch nghệ dân tộc. Đoàn kịch dàn dựng cả các tác phẩm kinh điển Nga - thế giới lẫn những vở diễn bằng tiếng Komi phản ánh đời sống, lịch sử và tâm hồn dân tộc bản địa, góp phần bảo tồn ngôn ngữ Komi trên sân khấu. Tọa lạc trên phố Pervomaiskaya ở trung tâm Syktyvkar, nhà hát là điểm hẹn văn hóa quen thuộc của người dân và là nơi du khách có thể cảm nhận nghệ thuật sân khấu độc đáo mang bản sắc phương Bắc. Nhà hát được phong danh hiệu 'hàn lâm' - sự ghi nhận cho bề dày và chất lượng nghệ thuật.",
    [
        "Nhà hát kịch lâu đời nhất Komi, lịch sử từ thập niên 1930",
        "Mang tên Viktor Savin - người sáng lập kịch nghệ dân tộc Komi",
        "Biểu diễn bằng cả tiếng Nga và tiếng Komi, gìn giữ ngôn ngữ bản địa",
    ],
    P(
        "Mở cửa theo lịch biểu diễn, chủ yếu buổi tối; phòng vé mở ban ngày.",
        "Vé theo suất diễn, giá phải chăng.",
        "Một buổi diễn khoảng 2-2,5 giờ.",
        "Mùa diễn thu - xuân.",
        "Đặt vé trước; nếu muốn trải nghiệm bản sắc, chọn vở diễn bằng tiếng Komi.",
    ),
    [
        {"title": "Wikipedia (RU) — Академический театр драмы имени В. Савина", "url": "https://ru.wikipedia.org/wiki/Академический_театр_драмы_имени_В._Савина"},
        {"title": "2ГИС — Театр драмы им. В. Савина", "url": "https://2gis.ru/syktyvkar"},
    ],
    ["theatre", "drama", "komi-language", "syktyvkar", "culture", "savin"],
    maps_text("Академический театр драмы имени В. Савина", "Сыктывкар", "Savin Drama Theatre", "Syktyvkar", 61.66990, 50.82490),
))

# 7) Стефановская площадь
RECORDS.append(rec(
    "stefanovskaya-square",
    "Quảng trường Stefanovskaya",
    "Стефановская площадь",
    "Stefanovskaya Square",
    ["square_street"],
    61.66861, 50.83556,
    "Trung tâm Syktyvkar, Cộng hòa Komi, Nga.",
    "Quảng trường Stefanovskaya là quảng trường trung tâm và trái tim của Syktyvkar, nơi diễn ra các sự kiện lớn, lễ hội và mít tinh. Xung quanh là tòa nhà chính quyền, đài tưởng niệm và Nhà thờ chính tòa Thánh Stefan.",
    "Nằm ngay giữa lòng Syktyvkar, Quảng trường Stefanovskaya là quảng trường chính và không gian công cộng quan trọng nhất của thủ phủ Komi. Quảng trường mang tên Thánh Stefan xứ Perm, thời Xô Viết từng được gọi là Quảng trường Lenin và về sau lấy lại tên lịch sử. Đây là nơi tọa lạc trụ sở chính quyền Cộng hòa Komi và các cơ quan hành chính, cùng đài tưởng niệm và không gian rộng thoáng cho những dịp trọng đại. Quảng trường là sân khấu của các sự kiện lớn trong năm: lễ duyệt binh và mít tinh mừng Ngày Chiến thắng, hội chợ, lễ hội thành phố, chợ Giáng sinh và cây thông năm mới rực rỡ vào mùa đông. Cạnh quảng trường là Nhà thờ chính tòa Thánh Stefan với những mái vòm dát vàng, tạo nên tổng thể trung tâm đô thị đặc trưng. Với du khách, Stefanovskaya là điểm khởi đầu tự nhiên để dạo bộ khám phá trung tâm lịch sử - văn hóa của Syktyvkar.",
    [
        "Quảng trường trung tâm, trái tim hành chính và lễ hội của Syktyvkar",
        "Nơi diễn ra duyệt binh Ngày Chiến thắng, lễ hội và chợ Giáng sinh",
        "Kề bên trụ sở chính quyền Komi và Nhà thờ chính tòa Thánh Stefan",
    ],
    P(
        "Không gian mở, tham quan tự do quanh năm cả ngày lẫn tối.",
        "Miễn phí.",
        "Khoảng 20-40 phút (lâu hơn khi có sự kiện).",
        "Mùa hè cho các lễ hội ngoài trời; dịp năm mới với cây thông và trang trí ánh sáng.",
        "Kết hợp tham quan Nhà thờ Thánh Stefan và các bảo tàng lân cận; canh dịp lễ để xem sự kiện đông vui.",
    ),
    [
        {"title": "Wikipedia (RU) — Стефановская площадь", "url": "https://ru.wikipedia.org/wiki/Стефановская_площадь"},
        {"title": "Wikipedia (RU) — Сыктывкар", "url": "https://ru.wikipedia.org/wiki/Сыктывкар"},
    ],
    ["square", "city-center", "syktyvkar", "landmark", "events"],
    maps_text("Стефановская площадь", "Сыктывкар", "Stefanovskaya Square", "Syktyvkar", 61.66861, 50.83556),
))

# 8) Свято-Казанский храм (Кочпон)
RECORDS.append(rec(
    "kochpon-kazan-church",
    "Nhà thờ Thánh Kazan ở Kochpon",
    "Свято-Казанский храм (Кочпон)",
    "St. Kazan Church (Kochpon)",
    ["church"],
    61.63718, 50.87053,
    "Khu Kochpon (Кочпон), ул. Набережная, Syktyvkar, Cộng hòa Komi, Nga.",
    "Nhà thờ Thánh Kazan ở khu Kochpon là một trong những nhà thờ cổ và quý giá nhất Syktyvkar - ngôi thánh đường hiếm hoi không đóng cửa suốt thời Xô Viết. Nơi đây lưu giữ nhiều thánh tích và biểu tượng thánh cổ.",
    "Nằm ở khu Kochpon bên bờ sông thuộc ngoại vi phía nam Syktyvkar, Nhà thờ Thánh Kazan (thờ Đức Mẹ Kazan) là một trong những ngôi thánh đường cổ kính và được trân trọng nhất của thành phố. Xây dựng vào cuối thế kỷ 19 - đầu thế kỷ 20, nhà thờ có số phận đặc biệt: đây là một trong rất ít nhà thờ ở Komi không bị đóng cửa hay phá hủy trong thời kỳ đàn áp tôn giáo của Liên Xô, nhờ vậy vẫn duy trì đời sống phụng vụ gần như liên tục. Chính vì thế, khi các nhà thờ khác bị phá, nhiều biểu tượng thánh (icon), thánh tích và đồ thờ quý giá đã được đưa về gìn giữ tại đây, khiến Kochpon trở thành một 'kho báu' tâm linh của Chính thống giáo xứ Komi. Ngôi nhà thờ với kiến trúc truyền thống, mái vòm và tháp chuông nằm trong khung cảnh yên tĩnh ven sông, là điểm hành hương quan trọng và là chứng nhân cho sức sống bền bỉ của đức tin nơi phương Bắc.",
    [
        "Một trong ít nhà thờ ở Komi không đóng cửa suốt thời Xô Viết",
        "Lưu giữ nhiều icon và thánh tích quý được cứu từ các nhà thờ bị phá",
        "Điểm hành hương cổ kính bên sông ở khu Kochpon, Syktyvkar",
    ],
    P(
        "Mở cửa cho tín hữu hằng ngày, thường ban ngày; giờ lễ theo lịch phụng vụ.",
        "Miễn phí; có thể quyên góp hoặc mua nến.",
        "Khoảng 30 phút.",
        "Quanh năm; sinh động vào các đại lễ và ngày lễ Đức Mẹ Kazan.",
        "Ăn mặc kín đáo, nữ giới trùm khăn; giữ trang nghiêm; nằm hơi xa trung tâm nên tính phương tiện di chuyển.",
    ),
    [
        {"title": "Sobory.ru — Церковь Казанской иконы Божией Матери в Кочпоне", "url": "https://sobory.ru/article/?object=10473"},
        {"title": "Wikipedia (RU) — Сыктывкар", "url": "https://ru.wikipedia.org/wiki/Сыктывкар"},
    ],
    ["church", "orthodox", "icons", "pilgrimage", "syktyvkar", "kochpon", "heritage"],
    maps_text("Свято-Казанский храм, Кочпон", "Сыктывкар", "St. Kazan Church Kochpon", "Syktyvkar", 61.63718, 50.87053),
))

# 9) Пожарная каланча (символ Сыктывкара)
RECORDS.append(rec(
    "fire-tower-syktyvkar",
    "Tháp cứu hỏa Syktyvkar (Pozharnaya Kalancha)",
    "Пожарная каланча (Сыктывкар)",
    "Fire Watchtower of Syktyvkar",
    ["monument"],
    61.6731, 50.8375,
    "Ул. Советская 9, Syktyvkar, Cộng hòa Komi, Nga.",
    "Tháp cứu hỏa cổ là biểu tượng không chính thức của Syktyvkar - một di tích kiến trúc đầu thế kỷ 20 với tháp bát giác đặc trưng. Đồng hồ trên tháp còn ngân nga giai điệu bài hát về thành phố.",
    "Được xây dựng trong những năm 1900-1907 theo thiết kế của kiến trúc sư Vologda I. I. Pavlov, Tháp cứu hỏa (Pozharnaya Kalancha) là di tích kiến trúc và biểu tượng không chính thức được yêu mến của Syktyvkar (thời đó là thị trấn Ust-Sysolsk). Công trình bằng gạch mang phong cách phương Bắc Nga cổ điển, nổi bật với ngọn tháp canh bát giác vươn cao - nơi xưa kia lính cứu hỏa quan sát toàn thành để phát hiện đám cháy. Sau đợt cải tạo năm 1975, tháp có thêm chóp nhọn cao với chú gà trống kim loại làm chong chóng gió đứng trên huy hiệu cổ của Ust-Sysolsk, còn mặt tiền được tôn thêm nét trang trí. Trên tháp gắn đồng hồ điện, mỗi khi điểm giờ lại ngân lên giai điệu bài hát của nhạc sĩ Yakov Perepelitsa viết về Syktyvkar - một chi tiết được người dân gìn giữ đầy tự hào. Ngày nay tòa nhà là trụ sở cơ quan phòng cháy chữa cháy, tầng ba có bảo tàng lịch sử cứu hỏa. Đây là mốc kiến trúc không thể bỏ qua khi dạo trung tâm thành phố.",
    [
        "Biểu tượng không chính thức của Syktyvkar, di tích kiến trúc 1900-1907",
        "Tháp canh bát giác đặc trưng, chóp có gà trống trên huy hiệu Ust-Sysolsk",
        "Đồng hồ ngân giai điệu bài hát về Syktyvkar mỗi khi điểm giờ; có bảo tàng cứu hỏa",
    ],
    P(
        "Ngắm bên ngoài tự do quanh năm; bảo tàng cứu hỏa bên trong mở theo hẹn/lịch riêng.",
        "Ngắm bên ngoài miễn phí; tham quan bảo tàng cứu hỏa cần liên hệ trước.",
        "Khoảng 15-30 phút.",
        "Quanh năm; đẹp cả khi có tuyết.",
        "Chụp ảnh tháp từ phố Sovetskaya; nghe đồng hồ điểm giờ; kết hợp tuyến dạo bộ trung tâm.",
    ),
    [
        {"title": "Wikipedia (RU) — Пожарная каланча (Сыктывкар)", "url": "https://ru.wikipedia.org/wiki/Пожарная_каланча_(Сыктывкар)"},
        {"title": "Национальная библиотека РК — Пожарная каланча", "url": "https://ru.wikipedia.org/wiki/Сыктывкар"},
    ],
    ["monument", "architecture", "landmark", "symbol", "syktyvkar", "fire-tower"],
    maps_text("Пожарная каланча", "Сыктывкар", "Fire Watchtower", "Syktyvkar", 61.6731, 50.8375),
))

# 10) Литературно-мемориальный музей И. А. Куратова
RECORDS.append(rec(
    "kuratov-museum",
    "Bảo tàng Văn học tưởng niệm I. A. Kuratov",
    "Литературно-мемориальный музей И. А. Куратова",
    "I. A. Kuratov Literary Memorial Museum",
    ["museum"],
    61.67350, 50.83924,
    "Ул. Орджоникидзе 2, Syktyvkar, Cộng hòa Komi, Nga.",
    "Bảo tàng tưởng niệm nhà thơ Ivan Kuratov - người khai sinh nền văn học viết Komi. Bảo tàng nằm trong một ngôi nhà gỗ cổ, giới thiệu cuộc đời, sự nghiệp và di sản của thi hào dân tộc.",
    "Nằm trong một ngôi nhà gỗ lịch sử ở trung tâm Syktyvkar, Bảo tàng Văn học tưởng niệm dành để tôn vinh Ivan Alekseevich Kuratov (1839-1875) - nhà thơ, nhà ngôn ngữ học và người sáng lập nền văn học viết của dân tộc Komi. Là một chi nhánh của Bảo tàng Quốc gia Cộng hòa Komi, nơi đây trưng bày các bản thảo, thư từ, sách vở, đồ dùng cá nhân và tư liệu tái hiện cuộc đời cùng hành trình sáng tạo của Kuratov - người đã viết những vần thơ đầu tiên bằng tiếng Komi và đặt nền móng cho ngôn ngữ văn chương của cả dân tộc. Không gian bảo tàng còn phản ánh đời sống văn hóa, xã hội của xứ Komi thế kỷ 19. Với những ai quan tâm đến văn học và ngôn ngữ Finno-Ugric, đây là điểm đến đặc biệt để hiểu về cội nguồn tiếng nói và tâm hồn Komi. Bảo tàng cũng tổ chức các buổi đọc thơ, sinh hoạt văn học và chương trình giáo dục.",
    [
        "Tưởng niệm Ivan Kuratov - người khai sinh văn học viết Komi",
        "Trưng bày bản thảo, thư từ và đồ dùng của thi hào trong ngôi nhà gỗ cổ",
        "Chi nhánh của Bảo tàng Quốc gia Komi, gắn với ngôn ngữ và văn chương dân tộc",
    ],
    P(
        "Thường mở 10:00-17:00/18:00, nghỉ một ngày đầu tuần; nên kiểm tra lịch.",
        "Vé vào cửa ở mức thấp.",
        "Khoảng 45 phút.",
        "Quanh năm; điểm đến trong nhà tốt cho mùa đông.",
        "Kết hợp với Bảo tàng Quốc gia Komi gần đó; hỏi về các buổi đọc thơ nếu quan tâm văn học.",
    ),
    [
        {"title": "Национальный музей РК — Музей И. А. Куратова", "url": "https://museumkomi.ru/"},
        {"title": "Wikipedia (RU) — Куратов, Иван Алексеевич", "url": "https://ru.wikipedia.org/wiki/Куратов,_Иван_Алексеевич"},
    ],
    ["museum", "literature", "kuratov", "komi-language", "syktyvkar", "memorial"],
    maps_text("Литературно-мемориальный музей И. А. Куратова", "Сыктывкар", "Kuratov Literary Museum", "Syktyvkar", 61.67350, 50.83924),
))

# 11) Геологический музей имени А. А. Чернова
RECORDS.append(rec(
    "chernov-geology-museum",
    "Bảo tàng Địa chất mang tên A. A. Chernov",
    "Геологический музей имени А. А. Чернова",
    "A. A. Chernov Geological Museum",
    ["museum"],
    61.67086, 50.82477,
    "Ул. Первомайская 54, Viện Địa chất (Институт геологии Коми НЦ), Syktyvkar, Cộng hòa Komi, Nga.",
    "Bảo tàng Địa chất mang tên nhà địa chất A. A. Chernov trưng bày khoáng vật, đá, hóa thạch và tài nguyên phong phú của vùng Komi và dãy Ural. Đây là bảo tàng khoa học thuộc Viện Địa chất Komi.",
    "Thuộc Viện Địa chất của Trung tâm Khoa học Komi trên phố Pervomaiskaya, Bảo tàng Địa chất mang tên A. A. Chernov là một bảo tàng khoa học chuyên đề độc đáo của Syktyvkar. Bảo tàng mang tên Aleksandr Aleksandrovich Chernov - nhà địa chất kiệt xuất, người có công lớn trong việc phát hiện và nghiên cứu bể than Pechora khổng lồ cùng tài nguyên khoáng sản của phương Bắc. Bộ sưu tập trưng bày hàng nghìn mẫu vật: khoáng vật đủ sắc màu, các loại đá, quặng, hóa thạch cổ sinh và mẫu tài nguyên đặc trưng của Cộng hòa Komi và dãy Ural - từ than, dầu, muối đến vàng, đá quý và những hóa thạch triệu năm tuổi. Đây là nơi lý tưởng để hiểu về sự giàu có địa chất đã định hình lịch sử khai thác và kinh tế của vùng, đồng thời khám phá vẻ đẹp kỳ thú của thế giới khoáng vật. Bảo tàng phục vụ cả mục đích nghiên cứu, giáo dục và tham quan, đặc biệt hấp dẫn với những ai yêu khoa học tự nhiên.",
    [
        "Bảo tàng địa chất khoa học thuộc Viện Địa chất Komi",
        "Mang tên A. A. Chernov - người nghiên cứu bể than Pechora",
        "Trưng bày khoáng vật, đá, quặng và hóa thạch của Komi và dãy Ural",
    ],
    P(
        "Mở cửa theo lịch của viện, thường trong giờ hành chính; nên hẹn/liên hệ trước, có thể cần đăng ký.",
        "Vé/phí tham quan ở mức thấp; một số buổi cần đặt trước.",
        "Khoảng 45-60 phút.",
        "Quanh năm; là điểm tham quan trong nhà.",
        "Liên hệ Viện Địa chất trước khi đến; phù hợp cho người yêu khoáng vật và học sinh, sinh viên.",
    ),
    [
        {"title": "Институт геологии Коми НЦ — Геологический музей им. А. А. Чернова", "url": "https://geo.komisc.ru/"},
        {"title": "Wikipedia (RU) — Чернов, Александр Александрович (геолог)", "url": "https://ru.wikipedia.org/wiki/Чернов,_Александр_Александрович_(геолог)"},
    ],
    ["museum", "geology", "minerals", "science", "syktyvkar", "chernov", "ural"],
    maps_text("Геологический музей имени А. А. Чернова", "Сыктывкар", "Chernov Geological Museum", "Syktyvkar", 61.67086, 50.82477),
))

# ==================== THIÊN NHIÊN / NÚI URAL / SÔNG / HANG ====================

# 12) Гора Народная
RECORDS.append(rec(
    "narodnaya-mountain",
    "Núi Narodnaya (đỉnh cao nhất dãy Ural)",
    "Гора Народная",
    "Mount Narodnaya",
    ["park_garden"],
    65.0333, 60.1167,
    "Dãy Ural Cận Cực, biên giới Cộng hòa Komi và Khu tự trị Khanty-Mansi, trong Vườn quốc gia Yugyd Va, Nga.",
    "Núi Narodnaya cao 1.895 m là đỉnh cao nhất của toàn dãy Ural. Nằm trên vùng Ural Cận Cực hoang vu trong Vườn quốc gia Yugyd Va, đây là mục tiêu chinh phục danh giá của dân leo núi khắp nước Nga.",
    "Với độ cao 1.895 mét, Narodnaya là đỉnh núi cao nhất của cả dãy Ural trải dài, nằm trên vùng Ural Cận Cực nơi ranh giới Cộng hòa Komi và Khu tự trị Khanty-Mansi, thuộc phạm vi Vườn quốc gia Yugyd Va (Di sản UNESCO 'Rừng nguyên sinh Komi'). Đỉnh núi được đặt tên vào năm 1927 trong một cuộc thám hiểm; tên gọi vừa gợi đến sông Naroda gần đó, vừa mang nghĩa 'của nhân dân' theo tinh thần thời đại. Xung quanh Narodnaya là khung cảnh núi non hùng vĩ với những hồ băng trong vắt (kar), thung lũng đá, tuyết vĩnh cửu và tàn tích sông băng. Chinh phục Narodnaya là ước mơ của nhiều nhà leo núi và đi bộ đường dài, dù hành trình đòi hỏi nhiều ngày băng qua vùng hoang dã khắc nghiệt, không đường sá, thường xuất phát từ thị trấn Inta. Đây không phải đỉnh quá hiểm về kỹ thuật nhưng thử thách bởi sự xa xôi, thời tiết thất thường và địa hình gian nan. Vẻ đẹp nguyên thủy và ý nghĩa biểu tượng khiến Narodnaya trở thành điểm đến để đời của dân phượt núi Nga.",
    [
        "Đỉnh cao nhất toàn dãy Ural, cao 1.895 mét",
        "Nằm trên Ural Cận Cực trong Vườn quốc gia Yugyd Va (Di sản UNESCO)",
        "Mục tiêu chinh phục danh giá, hành trình nhiều ngày từ Inta",
    ],
    nature_P(
        "Chuyến leo núi nhiều ngày (thường 7-12 ngày cả đi lẫn về từ Inta).",
        "Cuối tháng 7 - tháng 8 cho mùa leo núi; cuối đông - đầu xuân cho tuyến trượt tuyết.",
        "Bắt buộc đi cùng nhóm/hướng dẫn viên có kinh nghiệm và xin phép Vườn quốc gia Yugyd Va; chuẩn bị thể lực, đồ chống lạnh và định vị vì hoàn toàn không có hạ tầng.",
    ),
    [
        {"title": "Wikipedia (RU) — Народная (гора)", "url": "https://ru.wikipedia.org/wiki/Народная_(гора)"},
        {"title": "Национальный парк «Югыд ва»", "url": "https://yugyd-va.ru/"},
    ],
    ["mountain", "highest-peak", "ural", "subpolar-ural", "hiking", "yugyd-va", "nature", "remote"],
    maps_text("Гора Народная", "Республика Коми", "Mount Narodnaya", "Komi", 65.0333, 60.1167),
))

# 13) Гора Манарага
RECORDS.append(rec(
    "manaraga-mountain",
    "Núi Manaraga ('chân gấu')",
    "Гора Манарага",
    "Mount Manaraga",
    ["park_garden"],
    65.0478, 59.7628,
    "Dãy Ural Cận Cực, Cộng hòa Komi, trong Vườn quốc gia Yugyd Va, Nga.",
    "Núi Manaraga cao 1.662 m nổi tiếng với đỉnh răng cưa độc đáo được ví như 'bàn chân gấu'. Dù không phải đỉnh cao nhất, Manaraga được xem là ngọn núi đẹp và mang tính biểu tượng nhất của Ural Cận Cực.",
    "Cao 1.662 mét, Manaraga có lẽ là ngọn núi nổi tiếng và được yêu thích nhất của vùng Ural Cận Cực, thuộc Vườn quốc gia Yugyd Va ở Cộng hòa Komi. Điều làm nên danh tiếng của nó là hình dáng đỉnh núi độc nhất vô nhị: một sống núi lởm chởm với nhiều mũi nhọn như răng cưa. Trong tiếng Nenets, 'Manaraga' nghĩa là 'bàn chân gấu' (giơ vuốt) - đúng như dáng núi khi nhìn từ xa. Dù thấp hơn đỉnh Narodnaya kề bên, Manaraga từ lâu được dân leo núi Nga tôn là 'nữ hoàng của núi non Ural' bởi vẻ đẹp kiêu hùng, thanh thoát. Ngọn núi nằm giữa cảnh quan hoang sơ tuyệt mỹ với sông băng, thung lũng đá và những dòng sông trong vắt. Chinh phục sống núi răng cưa của Manaraga đòi hỏi kỹ thuật leo nhất định và là niềm tự hào của nhiều nhà leo núi. Hành trình tới đây thường kéo dài nhiều ngày băng qua vùng taiga và núi non không dấu chân người, khiến Manaraga trở thành biểu tượng của thiên nhiên hoang dã phương Bắc.",
    [
        "Đỉnh răng cưa độc đáo cao 1.662 m, được ví như 'bàn chân gấu' (tiếng Nenets)",
        "Được tôn là 'nữ hoàng của núi non Ural', biểu tượng của Ural Cận Cực",
        "Nằm trong Vườn quốc gia Yugyd Va giữa cảnh quan sông băng hoang sơ",
    ],
    nature_P(
        "Chuyến đi nhiều ngày (thường trên một tuần cả đi lẫn về).",
        "Cuối tháng 7 - tháng 8 cho leo núi; mùa đông cho tuyến trượt tuyết.",
        "Cần nhóm/hướng dẫn viên giàu kinh nghiệm và giấy phép Vườn quốc gia Yugyd Va; sống núi đòi hỏi kỹ thuật leo, chuẩn bị kỹ thiết bị và thể lực.",
    ),
    [
        {"title": "Wikipedia (RU) — Манарага", "url": "https://ru.wikipedia.org/wiki/Манарага"},
        {"title": "Национальный парк «Югыд ва»", "url": "https://yugyd-va.ru/"},
    ],
    ["mountain", "ural", "subpolar-ural", "climbing", "hiking", "yugyd-va", "nature", "remote"],
    maps_text("Гора Манарага", "Республика Коми", "Mount Manaraga", "Komi", 65.0478, 59.7628),
))

# 14) Гора Сабля
RECORDS.append(rec(
    "sablya-mountain",
    "Núi Sablya (Lưỡi kiếm)",
    "Гора Сабля",
    "Mount Sablya",
    ["park_garden"],
    64.77672, 58.88796,
    "Dãy Ural Cận Cực, huyện Pechora, Cộng hòa Komi, trong Vườn quốc gia Yugyd Va, Nga.",
    "Núi Sablya ('Lưỡi kiếm') là dãy núi răng cưa sắc nhọn cao khoảng 1.497 m, một trong những rặng núi ngoạn mục và dễ nhận biết nhất Ural Cận Cực. Hình dáng lởm chởm như lưỡi kiếm khiến nó trở thành điểm đến hấp dẫn của dân leo núi.",
    "Sablya - trong tiếng Nga nghĩa là 'lưỡi kiếm', là một rặng núi ngoạn mục ở vùng Ural Cận Cực thuộc huyện Pechora, Cộng hòa Komi, nằm trong Vườn quốc gia Yugyd Va. Đỉnh cao nhất của rặng đạt khoảng 1.497 mét. Cái tên bắt nguồn từ hình dáng đặc trưng: một sống núi dài, sắc nhọn với những mũi đá lởm chởm nhô lên như lưỡi kiếm cong hướng lên trời, tạo nên bóng dáng kịch tính khó lẫn khi nhìn từ đồng bằng Pechora. Rặng Sablya nổi tiếng với những vách đá dựng đứng, sông băng nhỏ (một trong những sông băng ở cực nam của Ural) và các hồ băng trong veo dưới chân. Đây là điểm đến quen thuộc của dân leo núi và đi bộ đường dài, vừa để chiêm ngưỡng vẻ đẹp hùng vĩ vừa thử thách bản thân trên những sườn dốc hiểm trở. Nằm gần thị trấn Pechora hơn so với các đỉnh sâu trong dãy, Sablya tương đối dễ tiếp cận hơn nhưng vẫn giữ nguyên sự hoang sơ và khắc nghiệt đặc trưng của núi non phương Bắc.",
    [
        "Rặng núi răng cưa sắc nhọn như 'lưỡi kiếm', cao khoảng 1.497 m",
        "Một trong những rặng núi ngoạn mục nhất Ural Cận Cực, thuộc Yugyd Va",
        "Có vách đá dựng đứng, sông băng nhỏ và hồ băng dưới chân",
    ],
    nature_P(
        "Chuyến đi bộ/leo núi nhiều ngày từ vùng Pechora.",
        "Cuối tháng 7 - tháng 8 cho mùa leo núi.",
        "Cần giấy phép Vườn quốc gia Yugyd Va và chuẩn bị kỹ; các vách dốc đòi hỏi kinh nghiệm leo núi.",
    ),
    [
        {"title": "Wikipedia (RU) — Сабля (гора)", "url": "https://ru.wikipedia.org/wiki/Сабля_(гора)"},
        {"title": "Национальный парк «Югыд ва»", "url": "https://yugyd-va.ru/"},
    ],
    ["mountain", "ural", "subpolar-ural", "ridge", "hiking", "yugyd-va", "nature", "glacier"],
    maps_text("Гора Сабля", "Республика Коми", "Mount Sablya", "Komi", 64.77672, 58.88796),
))

# 15) Река Щугор
RECORDS.append(rec(
    "shchugor-river",
    "Sông Shchugor (Shchugor)",
    "Река Щугор",
    "Shchugor River",
    ["park_garden"],
    64.2533, 57.5903,
    "Phụ lưu phải sông Pechora, chảy qua Vườn quốc gia Yugyd Va, huyện Vuktyl, Cộng hòa Komi, Nga (toạ độ cửa sông).",
    "Sông Shchugor là một trong những dòng sông đẹp và trong vắt nhất Ural, chảy qua Vườn quốc gia Yugyd Va trước khi đổ vào Pechora. Nổi tiếng với nước trong như pha lê, các 'cổng đá' hùng vĩ và những chuyến chèo bè, câu cá lý tưởng.",
    "Bắt nguồn từ sườn tây dãy Ural Bắc và chảy khoảng 300 km để đổ vào sông Pechora, Shchugor là một trong những con sông núi đẹp và tinh khiết nhất của Cộng hòa Komi, phần lớn nằm trong Vườn quốc gia Yugyd Va (Di sản UNESCO). Nước sông trong đến mức có thể nhìn thấu đáy ở độ sâu nhiều mét, mang màu xanh lục ngọc bích tuyệt đẹp. Điểm đặc sắc nhất của Shchugor là ba 'Cổng đá' (Ворота) - những đoạn sông len giữa các vách đá vôi cao dựng đứng gọi là Cổng Dưới, Cổng Giữa và Cổng Trên, tạo nên khung cảnh hẻm núi hùng vĩ. Dọc sông còn có các mó nước khoáng, thác nhỏ, rừng taiga nguyên sinh và hang động. Shchugor là tuyến chèo bè, kayak và câu cá (cá hồi trắng, cá xám) nổi tiếng, thu hút du khách ưa mạo hiểm và yêu thiên nhiên. Sông cũng là hành lang sinh thái quan trọng cho nhiều loài cá và động vật hoang dã. Vẻ đẹp nguyên sơ, làn nước trong vắt và những vách đá kỳ vĩ khiến Shchugor trở thành viên ngọc của thiên nhiên Komi.",
    [
        "Một trong những dòng sông trong vắt và đẹp nhất Ural, nước xanh ngọc bích",
        "Ba 'Cổng đá' (Ворота) - hẻm sông giữa vách đá vôi cao dựng đứng",
        "Tuyến chèo bè, kayak và câu cá nổi tiếng trong Vườn quốc gia Yugyd Va",
    ],
    nature_P(
        "Chuyến đi bè/kayak nhiều ngày dọc sông, hoặc tham quan các Cổng đá theo tour.",
        "Tháng 6 - đầu tháng 9 cho mùa nước và chèo bè; câu cá theo mùa và quy định.",
        "Cần giấy phép Vườn quốc gia Yugyd Va và đăng ký tuyến; đi cùng hướng dẫn viên có kinh nghiệm; chuẩn bị đồ chống côn trùng vào mùa hè.",
    ),
    [
        {"title": "Wikipedia (RU) — Щугор", "url": "https://ru.wikipedia.org/wiki/Щугор"},
        {"title": "Национальный парк «Югыд ва»", "url": "https://yugyd-va.ru/"},
    ],
    ["river", "clear-water", "canyon", "rafting", "fishing", "yugyd-va", "nature", "ural"],
    maps_text("Река Щугор", "Республика Коми", "Shchugor River", "Komi", 64.2533, 57.5903),
))

# 16) Уньинская пещера
RECORDS.append(rec(
    "unyinskaya-cave",
    "Hang Unyinskaya",
    "Уньинская пещера",
    "Unyinskaya Cave",
    ["park_garden"],
    61.781, 58.524,
    "Bên sông Unya, huyện Troitsko-Pechorsky, Cộng hòa Komi, gần Khu bảo tồn Pechoro-Ilych, Nga.",
    "Hang Unyinskaya là một trong những hang động lớn và nổi tiếng nhất Cộng hòa Komi, nằm bên sông Unya. Hang gắn với các di chỉ khảo cổ cổ xưa, từng là nơi trú ẩn và cúng tế của người thời tiền sử.",
    "Nằm bên bờ sông Unya (phụ lưu của Pechora) ở huyện Troitsko-Pechorsky vùng đông nam Komi, Uyinskaya (Unyinskaya) là một trong những hang động karst được biết đến nhiều nhất của nước cộng hòa. Hang hình thành trong khối đá vôi, có cửa hang và hệ thống ngách, hành lang khá dài. Điều làm nên giá trị đặc biệt của hang là các phát hiện khảo cổ: những cuộc khai quật cho thấy hang từng được con người sử dụng từ thời cổ đại - làm nơi trú ẩn của thợ săn và có thể là nơi cúng tế, với dấu tích xương động vật (kể cả động vật thời băng hà), công cụ và di vật. Vì thế Unyinskaya vừa là một di tích tự nhiên vừa là di chỉ khảo cổ - lịch sử quý giá của phương Bắc. Nằm ở vùng hoang vu gần Khu bảo tồn Pechoro-Ilych, hang không dễ tiếp cận và chủ yếu thu hút các nhà nghiên cứu, dân thám hiểm hang động (speleology) và du khách ưa khám phá thiên nhiên hoang dã dọc sông Unya.",
    [
        "Một trong những hang karst lớn và nổi tiếng nhất Komi, bên sông Unya",
        "Di chỉ khảo cổ: nơi trú ẩn, cúng tế của người tiền sử với xương động vật thời băng hà",
        "Nằm ở vùng hoang vu gần Khu bảo tồn Pechoro-Ilych, hấp dẫn dân thám hiểm",
    ],
    nature_P(
        "Tham quan theo chuyến thám hiểm/tour dọc sông Unya, thường nhiều ngày.",
        "Mùa hè (tháng 6-9) khi việc di chuyển trên sông thuận lợi.",
        "Vùng rất xa xôi, cần đi cùng hướng dẫn viên; mang đèn, mũ bảo hộ khi vào hang; tôn trọng giá trị khảo cổ, không lấy hiện vật.",
    ),
    [
        {"title": "Геологические памятники — Уньинская пещера", "url": "https://geomem.ru/"},
        {"title": "Outdoors.ru — Уньинская пещера (Республика Коми)", "url": "https://www.outdoors.ru/region/komi/kr184.php"},
    ],
    ["cave", "karst", "archaeology", "speleology", "nature", "unya", "remote"],
    maps_text("Уньинская пещера", "Республика Коми", "Unyinskaya Cave", "Komi", 61.781, 58.524),
))

# ==================== THÀNH PHỐ PHƯƠNG BẮC / BẮC CỰC ====================

# 17) Воркута
RECORDS.append(rec(
    "vorkuta",
    "Thành phố Vorkuta (Bắc Cực)",
    "Воркута",
    "Vorkuta",
    ["square_street", "monument"],
    67.5, 64.0333,
    "Thành phố Vorkuta, phía bắc Vòng Bắc Cực, đông bắc Cộng hòa Komi, Nga.",
    "Vorkuta là thành phố phương Bắc nằm trên Vòng Bắc Cực, mọc lên từ các mỏ than và trại lao động Gulag thời Xô Viết. Ngày nay đây là 'thành phố đang lụi tàn' đầy ám ảnh giữa tundra, chứng nhân của lịch sử bi tráng.",
    "Nằm phía bắc Vòng Bắc Cực ở góc đông bắc Cộng hòa Komi, giữa vùng tundra lạnh giá và bể than Pechora, Vorkuta là một trong những thành phố cực bắc của châu Âu. Thành phố ra đời trong thập niên 1930 gắn liền với việc khai thác than và hệ thống trại lao động khổ sai 'Vorkutlag' - một mắt xích lớn của Gulag, nơi hàng trăm nghìn tù nhân chính trị và thường phạm bị đày ải trong điều kiện khắc nghiệt. Sau chiến tranh, Vorkuta phát triển thành trung tâm khai thác than lớn với hàng loạt khu mỏ nối nhau theo 'vòng Vorkuta'. Từ khi Liên Xô tan rã, nhiều mỏ đóng cửa và dân số suy giảm mạnh, để lại những khu phố, làng mỏ bỏ hoang phủ tuyết - khiến Vorkuta được gọi là 'thành phố ma' hay thành phố đang lụi tàn, mang vẻ đẹp hoang tàn ám ảnh. Với du khách, Vorkuta là điểm đến độc đáo để cảm nhận cuộc sống Bắc Cực, chiêm nghiệm lịch sử Gulag qua các đài tưởng niệm và nghĩa trang, ngắm cực quang mùa đông và làm bàn đạp khám phá tundra cùng dãy Ural Cực.",
    [
        "Thành phố nằm trên Vòng Bắc Cực, một trong những đô thị cực bắc châu Âu",
        "Gắn với lịch sử khai thác than và hệ thống trại Gulag 'Vorkutlag'",
        "Cảnh quan tundra, khu mỏ bỏ hoang và cơ hội ngắm cực quang mùa đông",
    ],
    P(
        "Là thành phố nên tham quan tự do; các bảo tàng, đài tưởng niệm mở theo giờ riêng.",
        "Dạo thành phố miễn phí; bảo tàng địa phương thu vé nhỏ; một số khu vực cần lưu ý quy định.",
        "1-2 ngày cho thành phố và vùng phụ cận.",
        "Mùa đông cho cực quang và trải nghiệm Bắc Cực (rất lạnh); mùa hè ngắn cho tundra.",
        "Đến bằng máy bay hoặc tàu hỏa; chuẩn bị đồ chống lạnh cực độ vào mùa đông; đi cùng hướng dẫn viên nếu muốn thăm các khu mỏ/làng bỏ hoang.",
    ),
    [
        {"title": "Wikipedia (RU) — Воркута", "url": "https://ru.wikipedia.org/wiki/Воркута"},
        {"title": "Wikipedia (EN) — Vorkuta", "url": "https://en.wikipedia.org/wiki/Vorkuta"},
    ],
    ["city", "arctic", "gulag-history", "tundra", "coal", "aurora", "remote", "komi"],
    maps_text("Воркута", "Республика Коми", "Vorkuta", "Komi", 67.5, 64.0333),
))

# 18) Печора
RECORDS.append(rec(
    "pechora-town",
    "Thành phố Pechora",
    "Печора",
    "Pechora",
    ["square_street", "park_garden"],
    65.11667, 57.11667,
    "Thành phố Pechora, bên sông Pechora, trung - bắc Cộng hòa Komi, Nga.",
    "Pechora là thành phố cảng sông bên dòng Pechora hùng vĩ, một cửa ngõ chính để vào Vườn quốc gia Yugyd Va và dãy Ural. Thành phố trẻ gắn với tuyến đường sắt Pechora và giao thông đường sông phương Bắc.",
    "Nằm bên bờ con sông Pechora rộng lớn ở vùng trung - bắc Cộng hòa Komi, thành phố Pechora là một trung tâm giao thông và là cửa ngõ quan trọng để tiếp cận thiên nhiên hoang dã của vùng. Thành phố hình thành vào cuối thập niên 1940 gắn với việc xây dựng tuyến đường sắt phương Bắc (Pechora) và cảng sông, ban đầu cũng liên quan đến lao động cưỡng bức thời Xô Viết. Ngày nay Pechora là điểm trung chuyển chính cho những chuyến thám hiểm vào Vườn quốc gia Yugyd Va (Di sản UNESCO), lên vùng núi Ural Bắc như rặng Sablya, hay xuôi ngược dòng Pechora hùng vĩ. Thành phố có cảng sông nhộn nhịp, các đài tưởng niệm, nhà thờ, bảo tàng địa phương và không khí đặc trưng của một đô thị phương Bắc. Dòng sông Pechora - một trong những con sông lớn và sạch nhất châu Âu - là điểm nhấn cảnh quan, nơi du khách có thể đi thuyền, câu cá và ngắm hoàng hôn trắng mùa hè. Với vai trò bàn đạp khám phá Ural và Yugyd Va, Pechora là mắt xích không thể thiếu trong hành trình thiên nhiên Komi.",
    [
        "Thành phố cảng sông bên dòng Pechora - một trong những sông lớn, sạch nhất châu Âu",
        "Cửa ngõ chính vào Vườn quốc gia Yugyd Va và dãy Ural Bắc",
        "Gắn với tuyến đường sắt phương Bắc và giao thông đường sông",
    ],
    P(
        "Là thành phố, tham quan tự do; bảo tàng và điểm tham quan mở theo giờ riêng.",
        "Dạo thành phố miễn phí; bảo tàng thu vé nhỏ; tour sông/thiên nhiên tính phí.",
        "Khoảng 1 ngày (lâu hơn nếu dùng làm điểm khởi hành đi Yugyd Va).",
        "Mùa hè (tháng 6-9) cho đi thuyền và khởi hành các chuyến thiên nhiên.",
        "Đến bằng tàu hỏa hoặc máy bay; sắp xếp tour Yugyd Va/Sablya từ đây; tận hưởng đêm trắng mùa hè bên sông.",
    ),
    [
        {"title": "Wikipedia (RU) — Печора (город)", "url": "https://ru.wikipedia.org/wiki/Печора_(город)"},
        {"title": "Национальный парк «Югыд ва»", "url": "https://yugyd-va.ru/"},
    ],
    ["city", "river-port", "pechora-river", "gateway", "yugyd-va", "komi", "north"],
    maps_text("Печора", "Республика Коми", "Pechora", "Komi", 65.11667, 57.11667),
))

# 19) Инта
RECORDS.append(rec(
    "inta-town",
    "Thành phố Inta",
    "Инта",
    "Inta",
    ["square_street"],
    66.03981, 60.13152,
    "Thành phố Inta, gần Vòng Bắc Cực, đông bắc Cộng hòa Komi, Nga.",
    "Inta là thành phố mỏ than nhỏ ở phương bắc, gần Vòng Bắc Cực, nổi tiếng là cửa ngõ để chinh phục đỉnh Narodnaya và các ngọn núi cao nhất Ural. Thành phố có tháp nước độc đáo được xem là biểu tượng địa phương.",
    "Nằm ở vùng cận Bắc Cực đông bắc Cộng hòa Komi, không xa Vòng Bắc Cực, Inta là một thành phố mỏ than nhỏ hình thành vào giữa thế kỷ 20, cũng có nguồn gốc gắn với lao động cưỡng bức thời Xô Viết và bể than Pechora. Ngày nay dân số Inta khiêm tốn, nhưng thành phố có vai trò đặc biệt quan trọng với du lịch thiên nhiên: đây là điểm xuất phát chính cho các chuyến thám hiểm vào vùng Ural Cận Cực và Vườn quốc gia Yugyd Va, đặc biệt để chinh phục đỉnh Narodnaya (cao nhất Ural) và Manaraga. Từ Inta, du khách di chuyển bằng xe địa hình vào sâu trong vùng núi hoang vu. Một điểm nhấn kiến trúc thú vị của thành phố là tháp nước cũ xây bằng gạch với kiểu dáng độc đáo, được coi là biểu tượng và niềm tự hào của Inta. Thành phố mang không khí đặc trưng của đô thị phương Bắc khắc khổ, là nơi dừng chân tiếp tế và tổ chức hậu cần trước khi bước vào hành trình núi non khắc nghiệt.",
    [
        "Cửa ngõ chính chinh phục đỉnh Narodnaya và Manaraga của Ural Cận Cực",
        "Thành phố mỏ than nhỏ gần Vòng Bắc Cực, gắn với bể than Pechora",
        "Tháp nước gạch độc đáo - biểu tượng kiến trúc của thành phố",
    ],
    P(
        "Là thành phố, tham quan tự do; dịch vụ du lịch/hậu cần liên hệ trước.",
        "Dạo thành phố miễn phí; tour xe địa hình và chuyến núi tính phí.",
        "Nửa ngày cho thành phố; là điểm khởi hành các chuyến núi nhiều ngày.",
        "Cuối tháng 7 - tháng 8 cho mùa leo núi Narodnaya/Manaraga.",
        "Đến bằng tàu hỏa; đặt trước xe địa hình và hướng dẫn viên vào Yugyd Va; chuẩn bị hậu cần đầy đủ vì phía trước không còn hạ tầng.",
    ),
    [
        {"title": "Wikipedia (RU) — Инта", "url": "https://ru.wikipedia.org/wiki/Инта"},
        {"title": "Национальный парк «Югыд ва»", "url": "https://yugyd-va.ru/"},
    ],
    ["city", "coal", "gateway", "subpolar-ural", "narodnaya", "hiking", "komi", "north"],
    maps_text("Инта", "Республика Коми", "Inta", "Komi", 66.03981, 60.13152),
))

# 20) Ухта
RECORDS.append(rec(
    "ukhta-town",
    "Thành phố Ukhta",
    "Ухта",
    "Ukhta",
    ["square_street"],
    63.56667, 53.70000,
    "Thành phố Ukhta, trung Cộng hòa Komi, Nga.",
    "Ukhta là 'thủ đô dầu mỏ' của Komi - nơi khai thác dầu công nghiệp đầu tiên của nước Nga từ thế kỷ 18. Thành phố hiện đại, được quy hoạch đẹp, còn nổi tiếng với chân dung Lenin khổng lồ trên đồi Vetlosyan.",
    "Nằm ở trung tâm Cộng hòa Komi, Ukhta là thành phố lớn thứ hai của vùng và là trung tâm công nghiệp dầu khí quan trọng - được mệnh danh là 'thủ đô dầu mỏ' của Komi. Vùng Ukhta có lịch sử dầu mỏ lâu đời: ngay từ thế kỷ 18, đây là một trong những nơi khai thác dầu đầu tiên ở Nga, và mỏ dầu công nghiệp đầu tiên của nước Nga được khoan tại vùng này. Thành phố hiện đại phần lớn được xây dựng vào giữa thế kỷ 20, ban đầu cũng gắn với lao động cưỡng bức, sau phát triển mạnh nhờ dầu khí. Ukhta được đánh giá là một trong những đô thị được quy hoạch đẹp và ngăn nắp của phương Bắc, với trung tâm mang kiến trúc tân cổ điển Stalin, quảng trường, công viên và các công trình văn hóa. Biểu tượng nổi tiếng nhất của thành phố là chân dung nghiêng khổng lồ của Lenin trên sườn đồi Vetlosyan - một trong những bức chân dung Lenin lớn nhất thế giới, rực sáng về đêm. Ukhta cũng có bảo tàng lịch sử, nhà thờ và là điểm dừng chân tiện lợi trên hành trình khám phá miền trung Komi.",
    [
        "'Thủ đô dầu mỏ' của Komi, nơi khai thác dầu công nghiệp đầu tiên của Nga",
        "Trung tâm quy hoạch đẹp với kiến trúc tân cổ điển Stalin",
        "Chân dung Lenin khổng lồ trên đồi Vetlosyan - biểu tượng của thành phố",
    ],
    P(
        "Là thành phố, tham quan tự do; bảo tàng và điểm tham quan mở theo giờ riêng.",
        "Dạo thành phố miễn phí; bảo tàng thu vé nhỏ.",
        "Khoảng 1 ngày.",
        "Cuối xuân đến đầu thu dễ chịu; mùa đông lạnh nhưng chân dung Lenin sáng đèn ấn tượng.",
        "Ghé đồi Vetlosyan ngắm chân dung Lenin (đẹp nhất lúc lên đèn); dạo trung tâm tân cổ điển; là điểm dừng thuận tiện đường sắt/đường bộ.",
    ),
    [
        {"title": "Wikipedia (RU) — Ухта", "url": "https://ru.wikipedia.org/wiki/Ухта"},
        {"title": "Wikipedia (EN) — Ukhta", "url": "https://en.wikipedia.org/wiki/Ukhta"},
    ],
    ["city", "oil", "industry", "architecture", "komi", "lenin", "north"],
    maps_text("Ухта", "Республика Коми", "Ukhta", "Komi", 63.56667, 53.70000),
))

# 21) Профиль Ленина на горе Ветлосян (Ухта)
RECORDS.append(rec(
    "lenin-profile-vetlosyan",
    "Chân dung Lenin trên đồi Vetlosyan",
    "Профиль Ленина на горе Ветлосян",
    "Lenin Profile on Vetlosyan Hill",
    ["monument"],
    63.55884, 53.75297,
    "Sườn đồi Vetlosyan (Ветлосян), thành phố Ukhta, Cộng hòa Komi, Nga.",
    "Chân dung nghiêng khổng lồ của Lenin trên sườn đồi Vetlosyan ở Ukhta được coi là một trong những bức chân dung Lenin lớn nhất thế giới. Bức phù điêu bằng kim loại rực sáng về đêm, là biểu tượng độc đáo của thành phố.",
    "Trên sườn đồi Vetlosyan nhìn xuống thành phố Ukhta là một trong những công trình độc đáo và gây ấn tượng nhất Cộng hòa Komi: bức chân dung nghiêng khổng lồ của Vladimir Lenin. Được dựng vào năm 1970 nhân kỷ niệm 100 năm ngày sinh của Lenin, tác phẩm là một khung phù điêu bằng kim loại phác họa gương mặt nhìn nghiêng của nhà lãnh đạo Xô Viết, với kích thước cực lớn - chiều dài lên tới hàng chục mét - và được xem là một trong những chân dung Lenin lớn nhất thế giới. Vào ban đêm, đường viền chân dung được thắp sáng bằng đèn, nổi bật trên nền đồi tối và có thể nhìn thấy từ nhiều nơi trong thành phố, tạo nên hình ảnh vừa hoài niệm vừa siêu thực. Công trình là chứng tích của thời kỳ Xô Viết và đã trở thành một biểu tượng, điểm nhận diện gắn bó với bản sắc của Ukhta. Du khách thường lên đồi Vetlosyan để ngắm bức chân dung ở cự ly gần và phóng tầm mắt bao quát toàn cảnh thành phố dầu mỏ phía dưới.",
    [
        "Một trong những chân dung Lenin lớn nhất thế giới, dựng năm 1970",
        "Phù điêu kim loại khổng lồ trên sườn đồi, rực sáng đèn về đêm",
        "Biểu tượng độc đáo của Ukhta, điểm ngắm toàn cảnh thành phố",
    ],
    P(
        "Ngoài trời, tham quan tự do quanh năm; đẹp nhất khi lên đèn buổi tối.",
        "Miễn phí.",
        "Khoảng 30-45 phút (gồm leo lên đồi và ngắm cảnh).",
        "Quanh năm; buổi tối để thấy chân dung sáng đèn; ban ngày để ngắm toàn cảnh thành phố.",
        "Đi giày phù hợp để lên đồi; kết hợp tham quan trung tâm Ukhta; mang máy ảnh cho cảnh đêm.",
    ),
    [
        {"title": "RussPass — Профиль Ленина, Ухта", "url": "https://russpass.ru/"},
        {"title": "Wikipedia (RU) — Ухта", "url": "https://ru.wikipedia.org/wiki/Ухта"},
    ],
    ["monument", "lenin", "soviet-heritage", "landmark", "ukhta", "komi"],
    maps_text("Профиль Ленина на горе Ветлосян", "Ухта", "Lenin Profile Vetlosyan", "Ukhta", 63.55884, 53.75297),
))

# ==================== DI SẢN TÔN GIÁO / KHÁC ====================

# 22) Кылтовский Крестовоздвиженский женский монастырь
RECORDS.append(rec(
    "kyltovo-convent",
    "Tu viện nữ Kyltovo (Suy tôn Thánh giá)",
    "Кылтовский Крестовоздвиженский женский монастырь",
    "Kyltovo Exaltation of the Cross Convent",
    ["church"],
    62.32052, 50.99436,
    "Gần làng Kyltovo (Кылтово), huyện Knyazhpogostsky, Cộng hòa Komi, Nga.",
    "Tu viện nữ Kyltovo là tu viện nữ duy nhất và cổ kính của Cộng hòa Komi, thành lập cuối thế kỷ 19 giữa rừng taiga hẻo lánh. Sau thời gian bị đóng cửa, tu viện được khôi phục và là điểm hành hương thanh tịnh.",
    "Nằm giữa vùng rừng taiga yên tĩnh gần làng Kyltovo thuộc huyện Knyazhpogostsky, Tu viện nữ Kyltovo mang tên lễ Suy tôn Thánh giá là tu viện nữ cổ kính và quan trọng bậc nhất của Cộng hòa Komi. Tu viện được thành lập vào cuối thế kỷ 19 (những năm 1890) nhờ công của các nhà hảo tâm, trở thành trung tâm đời sống tu trì và từ thiện của phụ nữ Chính thống giáo ở phương Bắc, với nhà thờ đá, các dãy nhà tu và ruộng vườn tự cung tự cấp. Sau Cách mạng, tu viện bị đóng cửa và cơ sở từng bị dùng cho nhiều mục đích khác nhau, kể cả trại giam thời Xô Viết. Đến những năm 1990-2000, tu viện được phục hồi và trở lại đời sống tôn giáo với cộng đoàn nữ tu. Ngày nay Kyltovo là điểm hành hương thanh bình, nơi du khách và tín hữu tìm về sự tĩnh lặng giữa thiên nhiên phương Bắc, chiêm ngưỡng kiến trúc nhà thờ cổ và cảm nhận lịch sử thăng trầm của đức tin nơi đây.",
    [
        "Tu viện nữ cổ kính và quan trọng nhất Komi, thành lập cuối thế kỷ 19",
        "Nằm giữa rừng taiga hẻo lánh, từng bị đóng cửa rồi được khôi phục",
        "Điểm hành hương thanh tịnh với nhà thờ đá và cộng đoàn nữ tu",
    ],
    P(
        "Mở cửa cho khách hành hương ban ngày; nên tránh giờ cử hành phụng vụ nếu chỉ tham quan.",
        "Miễn phí; có thể quyên góp.",
        "Khoảng 1-1,5 giờ.",
        "Mùa hè thuận tiện di chuyển; các dịp lễ lớn Chính thống giáo nhộn nhịp hơn.",
        "Ăn mặc kín đáo, nữ giới trùm khăn; đường tới hơi xa nên tính phương tiện; giữ trang nghiêm nơi tu viện.",
    ),
    [
        {"title": "Wikipedia (RU) — Крестовоздвиженский Кылтовский монастырь", "url": "https://ru.wikipedia.org/wiki/Крестовоздвиженский_Кылтовский_монастырь"},
        {"title": "Sobory.ru — Кылтовский Крестовоздвиженский монастырь", "url": "https://sobory.ru/article/?object=16441"},
    ],
    ["monastery", "convent", "orthodox", "pilgrimage", "komi", "taiga", "heritage"],
    maps_text("Кылтовский Крестовоздвиженский женский монастырь", "Республика Коми", "Kyltovo Convent", "Komi", 62.32052, 50.99436),
))

# 23) Троице-Стефано-Ульяновский монастырь
RECORDS.append(rec(
    "ulyanovo-monastery",
    "Tu viện Trinity-Stefano-Ulyanovo",
    "Троице-Стефано-Ульяновский монастырь",
    "Trinity-Stephen-Ulyanovo Monastery",
    ["church"],
    61.82470, 53.55630,
    "Làng Ulyanovo (Ульяново), huyện Ust-Kulomsky, bên sông Vychegda thượng nguồn, Cộng hòa Komi, Nga.",
    "Tu viện Trinity-Stefano-Ulyanovo là một trong những tu viện nam lớn và đẹp nhất phương Bắc nước Nga, bên sông Vychegda. Tương truyền có nguồn gốc từ thời Thánh Stefan xứ Perm, quần thể hiện nay là kiệt tác kiến trúc thế kỷ 19.",
    "Nằm bên bờ sông Vychegda thượng nguồn tại làng Ulyanovo, huyện Ust-Kulomsky, Tu viện Trinity-Stefano-Ulyanovo là một trong những tu viện nam nổi bật và bề thế nhất của cả miền Bắc nước Nga. Theo truyền thuyết, tu viện có nguồn gốc từ thế kỷ 14 gắn với sứ mệnh truyền giáo của Thánh Stefan xứ Perm ở vùng thượng Vychegda. Quần thể tu viện đồ sộ như ngày nay chủ yếu được xây dựng vào nửa sau thế kỷ 19, khi các tu sĩ từ tu viện Solovetsky đến phục hưng nơi đây, tạo nên một tổ hợp kiến trúc tráng lệ với nhà thờ chính, tháp chuông cao, tường bao, tháp góc và các dãy nhà tu - được ví như một 'điện Kremlin' tôn giáo giữa rừng taiga. Thời Xô Viết tu viện bị đóng cửa và xuống cấp, sau được trả lại cho Giáo hội và khôi phục từ những năm 1990. Ngày nay đây là trung tâm hành hương quan trọng và là điểm đến cho những ai muốn chiêm ngưỡng vẻ đẹp kiến trúc Chính thống giáo phương Bắc trong khung cảnh thiên nhiên thanh bình bên dòng Vychegda.",
    [
        "Một trong những tu viện nam bề thế và đẹp nhất miền Bắc nước Nga",
        "Truyền thuyết gắn với Thánh Stefan xứ Perm; kiến trúc tráng lệ thế kỷ 19",
        "Quần thể như 'Kremlin tôn giáo' bên sông Vychegda, được khôi phục sau thời Xô Viết",
    ],
    P(
        "Mở cửa cho khách hành hương ban ngày; giờ lễ theo lịch phụng vụ.",
        "Miễn phí; có thể quyên góp; một số khu vực có thể cần xin phép.",
        "Khoảng 1-1,5 giờ.",
        "Mùa hè cho cảnh sông và di chuyển thuận tiện; các đại lễ Chính thống giáo.",
        "Ăn mặc kín đáo, nữ giới trùm khăn; đường tới khá xa từ Syktyvkar, nên tính lịch trình; giữ trang nghiêm.",
    ),
    [
        {"title": "Wikipedia (RU) — Троице-Стефано-Ульяновский монастырь", "url": "https://ru.wikipedia.org/wiki/Троице-Стефано-Ульяновский_монастырь"},
        {"title": "Sobory.ru — Троице-Стефано-Ульяновский монастырь", "url": "https://sobory.ru/article/?object=05237"},
    ],
    ["monastery", "orthodox", "pilgrimage", "architecture", "komi", "vychegda", "heritage"],
    maps_text("Троице-Стефано-Ульяновский монастырь", "Республика Коми", "Ulyanovo Monastery", "Komi", 61.82470, 53.55630),
))

# 24) Серёгово (соляной курорт)
RECORDS.append(rec(
    "seregovo",
    "Làng Seregovo và suối muối",
    "Серёгово",
    "Seregovo",
    ["other"],
    62.32601, 50.69849,
    "Làng Seregovo (Серёгово), huyện Knyazhpogostsky, bên sông Vym, Cộng hòa Komi, Nga.",
    "Seregovo là làng cổ nổi tiếng với các mỏ muối và suối nước muối khoáng, nơi có nghề nấu muối từ thế kỷ 16. Ngày nay đây là khu điều dưỡng nghỉ dưỡng dùng nước khoáng - bùn để chữa bệnh.",
    "Nằm bên sông Vym thuộc huyện Knyazhpogostsky, Seregovo là một trong những ngôi làng lịch sử độc đáo của Cộng hòa Komi nhờ nguồn nước muối ngầm phong phú. Từ thế kỷ 16-17, nơi đây đã hình thành nghề nấu muối (solevarenie): người ta bơm nước muối từ lòng đất lên rồi cô đặc để lấy muối - một ngành thủ công quan trọng cung cấp muối cho cả vùng phương Bắc suốt nhiều thế kỷ. Nguồn nước muối khoáng đậm đặc của Seregovo về sau được nhận ra có giá trị chữa bệnh, và một khu điều dưỡng (санаторий) đã ra đời tại đây từ thế kỷ 20, sử dụng nước khoáng và bùn trị liệu để chữa các bệnh về cơ - xương - khớp, thần kinh và tuần hoàn. Ngày nay khu nghỉ dưỡng Seregovo là một trong những cơ sở điều dưỡng chính của Komi, thu hút khách đến chữa bệnh và thư giãn giữa thiên nhiên yên tĩnh. Ngôi làng cũng giữ dấu ấn lịch sử nghề muối và kiến trúc gỗ phương Bắc, là điểm dừng chân thú vị cho ai muốn tìm hiểu di sản công nghiệp - thủ công truyền thống của vùng.",
    [
        "Làng cổ với nghề nấu muối từ thế kỷ 16-17, di sản thủ công phương Bắc",
        "Nguồn nước muối khoáng và bùn trị liệu quý giá",
        "Khu điều dưỡng (санаторий) chữa bệnh chính của Komi bên sông Vym",
    ],
    P(
        "Làng tham quan tự do; khu điều dưỡng nhận khách theo chương trình nghỉ dưỡng/liệu trình.",
        "Vào làng miễn phí; dịch vụ điều dưỡng, tắm khoáng - bùn tính phí theo gói.",
        "Nửa ngày tham quan; lâu hơn nếu nghỉ dưỡng.",
        "Quanh năm cho điều dưỡng; mùa hè thuận tiện tham quan làng.",
        "Đặt trước nếu muốn dùng dịch vụ điều dưỡng; kết hợp tìm hiểu lịch sử nghề muối; đường tới từ Syktyvkar khoảng vài giờ.",
    ),
    [
        {"title": "Wikipedia (RU) — Серёгово", "url": "https://ru.wikipedia.org/wiki/Серёгово"},
        {"title": "Санаторий «Серёгово»", "url": "https://sanseregovo.ru/"},
    ],
    ["village", "salt", "history", "spa", "sanatorium", "mineral-water", "komi", "vym"],
    maps_text("Серёгово санаторий", "Республика Коми", "Seregovo", "Komi", 62.32601, 50.69849),
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
