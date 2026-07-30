# -*- coding: utf-8 -*-
"""_add_places_altai-republic_20260729_020000.py — VÙNG: Cộng hoà Altai (Республика Алтай)
(lần chạy tự động bảo trì 2026-07-29).

Bối cảnh: altai-republic.json hiện có 8 địa điểm (Телецкое озеро, перевал Кату-Ярык,
Мультинские озёра, Белуха, остров Патмос/Чемал, Гейзерное озеро, Калбак-Таш, озеро Ая).
Bổ sung 23 danh lam THẬT SỰ nổi tiếng CÒN THIẾU → đưa vùng lên 31. TRÁNH trùng 8 điểm trên.

TOẠ ĐỘ — xác minh chủ yếu qua prop=coordinates của ru.wikipedia/en.wikipedia (2026-07-29),
một số điểm phố/khu nghỉ dùng toạ độ đã biết chắc (2GIS/Yandex). Phạm vi Altai: lat ~49.0–52.7,
lon ~83.9–89.8; lon LỚN HƠN lat, KHÔNG đảo. Nguồn toạ độ chính:
  Чике-Таман 50.6449,86.3123 (ruwiki); Семинский пер. 51.0453,85.6042 (ruwiki);
  Улаганский пер. 50.482449,87.629823 (ruwiki); вдп Корбу 51.7061,87.6842 (ruwiki);
  Учар/Б.Чульчинский 51.1179,88.0836 (ruwiki); Камышлинский вдп 51.6698,85.7562 (ruwiki);
  Аккемское оз. 49.9069,86.5467 (ruwiki); Кучерлинское оз. 49.8375,86.4247 (данные путеводителей);
  Каракольские оз. 51.4833,86.3833 (ruwiki); Манжерокское оз. 51.8236,85.8206 (2gis);
  Тавдинские пещеры 51.7687,85.7164 (ruwiki); плато Укок 49.3078,87.5947 (ruwiki);
  Уч-Энмек 50.760461,85.852058 (ruwiki); Чулышман 51.3639,87.7625 (ruwiki, устье);
  Курайская степь 50.211,87.905 (ruwiki); Северо-Чуйский хр. 50.067,87.583 (ruwiki);
  Чуй-Оозы 50.393,86.678 (ruwiki); Кызыл-Чин «Алтайский Марс» ~50.0197,88.3125 (долина, ruwiki);
  Чемальская ГЭС 51.39083,86.01056 (ruwiki); Бирюзовая Катунь 51.7897,85.7358 (2gis);
  ВТРК Манжерок 51.8130,85.8360 (2gis); Ороктойский мост 51.12306,86.16583 (ruwiki);
  Нацмузей им. Анохина 51.9585,85.9200 (Горно-Алтайск, ул. Чорос-Гуркина 46).

GHI CHÚ: BỎ Пазырыкские курганы vì toạ độ nguồn (49.5789,88.1531) mâu thuẫn rõ với vị trí thung lũng
Пазырык thực tế (~50.7) → tránh sai. Chủ đề khảo cổ đã có Укок + bảo tàng Анохин (Công chúa Ukok).
KHÔNG bịa toạ độ, KHÔNG nhồi. Nội dung tiếng Việt NGUYÊN GỐC (paraphrase), có ghi nguồn.

Chạy:  python3 tools/_add_places_altai-republic_20260729_020000.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "altai-republic"
REGION_NAME_VI = "Cộng hoà Altai"
FD = "Vùng Siberia"


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

# ============================ NHÓM 1: BẢO TÀNG & ĐÈO & THÁC ============================

# 1) Bảo tàng Quốc gia mang tên A. V. Anokhin ---------------------------------------
RECORDS.append(rec(
    "anokhin-national-museum",
    "Bảo tàng Quốc gia Cộng hoà Altai mang tên A. V. Anokhin",
    "Национальный музей Республики Алтай имени А. В. Анохина",
    "A. V. Anokhin National Museum of the Altai Republic",
    ["museum"],
    51.9585, 85.9200,
    "Phố Grigoria Choros-Gurkina 46, thành phố Gorno-Altaysk, Cộng hoà Altai, Nga",
    "Bảo tàng Quốc gia mang tên nhà dân tộc học A. V. Anokhin là bảo tàng lớn và lâu đời nhất Cộng hoà Altai, đặt tại thủ phủ Gorno-Altaysk. Nơi đây lưu giữ hàng chục nghìn hiện vật về thiên nhiên, khảo cổ và văn hoá các dân tộc Altai.",
    "Thành lập năm 1918, Bảo tàng Quốc gia Cộng hoà Altai mang tên A. V. Anokhin là kho tàng di sản trung tâm của cả vùng, toạ lạc trong toà nhà hiện đại ở lõi thành phố Gorno-Altaysk. Bộ sưu tập trải rộng từ mẫu vật địa chất, động thực vật taiga đến nghệ thuật dân gian, trang phục, nhạc cụ và đồ thủ công của người Altai bản địa. Điểm nhấn nổi tiếng nhất là gian trưng bày dành riêng cho 'Công chúa Ukok' - xác ướp người phụ nữ Pazyryk hơn 2.400 năm tuổi được khai quật trên cao nguyên Ukok, bảo quản trong phòng đặc biệt kiểm soát khí hậu. Du khách còn được xem các phát hiện từ những gò mộ scythia, tranh của hoạ sĩ G. Choros-Gurkin và tư liệu về nhà nghiên cứu Anokhin. Đây là điểm khởi đầu lý tưởng để hiểu chiều sâu lịch sử và tâm linh của vùng núi Altai trước khi lên đường.",
    [
        "Bảo tàng lớn và lâu đời nhất (1918) của Cộng hoà Altai, ngay trung tâm Gorno-Altaysk.",
        "Trưng bày 'Công chúa Ukok' - xác ướp Pazyryk 2.400 năm trong phòng kiểm soát khí hậu.",
        "Bộ sưu tập phong phú về thiên nhiên, khảo cổ scythia và văn hoá dân tộc Altai.",
    ],
    p("Thường mở cửa thứ Ba–Chủ nhật khoảng 10:00–18:00; thứ Hai nghỉ (nên kiểm tra lịch trước).",
      "Vé vào cửa phải thu phí, mức thường vài trăm rúp; gian Công chúa Ukok có thể tính vé riêng.",
      "Khoảng 1,5–2 giờ.",
      "Quanh năm; hợp làm điểm dừng đầu tiên khi mới đến Gorno-Altaysk.",
      "Việc mở phòng đặt xác ướp Ukok có lịch riêng theo tín ngưỡng bản địa - nên hỏi trước tại quầy vé."),
    [
        {"title": "Wikipedia (RU) — Национальный музей Республики Алтай", "url": "https://ru.wikipedia.org/wiki/Национальный_музей_Республики_Алтай_имени_А._В._Анохина"},
        {"title": "Culture.ru — музеи Республики Алтай", "url": "https://www.culture.ru/institutes/"},
    ],
    ["museum", "history", "archaeology", "ethnography", "ukok-princess", "gorno-altaysk"],
    maps_text("Национальный музей имени А. В. Анохина", "Горно-Алтайск", "Anokhin National Museum", "Gorno-Altaysk", 51.9585, 85.9200),
))

# 2) Đèo Chike-Taman -----------------------------------------------------------------
RECORDS.append(rec(
    "chike-taman-pass",
    "Đèo Chike-Taman",
    "Перевал Чике-Таман",
    "Chike-Taman Pass",
    ["park_garden"],
    50.6449, 86.3123,
    "Km 659 đường Chuysky Trakt, huyện Ongudaysky, Cộng hoà Altai, Nga",
    "Chike-Taman là con đèo ngoạn mục trên đại lộ huyền thoại Chuysky Trakt, cao khoảng 1.295 m, nổi tiếng với những khúc cua tay áo uốn lượn giữa vách đá dựng đứng. Từ đỉnh đèo có đài ngắm cảnh nhìn bao quát thung lũng và dãy núi Altai.",
    "Đèo Chike-Taman (tên tiếng Altai nghĩa là 'lòng bàn chân phẳng') là một trong những đoạn ấn tượng nhất của Chuysky Trakt - tuyến đường được xếp vào hàng đẹp nhất thế giới. Đường cũ men theo sườn núi bằng vô số khúc cua gấp, còn con đường mới cắt qua đá granite tạo nên khung cảnh đèo dốc hùng vĩ ở độ cao khoảng 1.295 m. Trên đỉnh đèo có khu quan sát với bậc thang, bảng chỉ dẫn và những quầy bán mật ong, thảo dược, đồ lưu niệm của người bản địa. Đứng đây, du khách thu vào tầm mắt toàn cảnh thung lũng sâu hun hút và các rặng núi trùng điệp, đặc biệt huyền ảo vào lúc bình minh hay hoàng hôn. Chike-Taman là cột mốc mà hầu như mọi hành trình xuyên Altai đều dừng lại chụp ảnh.",
    [
        "Đèo biểu tượng của Chuysky Trakt, cao ~1.295 m với những khúc cua tay áo ngoạn mục.",
        "Đài ngắm cảnh trên đỉnh nhìn bao quát thung lũng và dãy núi Altai.",
        "Điểm dừng chân mua mật ong, thảo dược và đồ lưu niệm bản địa.",
    ],
    p("Ngoài trời, tham quan tự do suốt ngày đêm; các quầy hàng hoạt động ban ngày.",
      "Miễn phí.",
      "Khoảng 20–40 phút dừng chân.",
      "Cuối xuân đến đầu thu; bình minh và hoàng hôn ánh sáng đẹp nhất.",
      "Đường đèo nhiều cua gấp - lái xe cẩn thận, đỗ đúng bãi trên đỉnh. Mang áo ấm vì trên cao gió lạnh."),
    [
        {"title": "Wikipedia (RU) — Чике-Таман", "url": "https://ru.wikipedia.org/wiki/Чике-Таман"},
    ],
    ["mountain-pass", "chuysky-trakt", "viewpoint", "scenic-road", "nature", "altai"],
    maps_text("Перевал Чике-Таман", "Республика Алтай", "Chike-Taman Pass", "Altai Republic", 50.6449, 86.3123),
))

# 3) Đèo Seminsky ---------------------------------------------------------------------
RECORDS.append(rec(
    "seminsky-pass",
    "Đèo Seminsky",
    "Семинский перевал",
    "Seminsky Pass",
    ["park_garden"],
    51.0453, 85.6042,
    "Đường Chuysky Trakt, huyện Ongudaysky, Cộng hoà Altai, Nga",
    "Seminsky là đèo cao nhất trên đường Chuysky Trakt, đỉnh khoảng 1.717 m, đánh dấu ranh giới tự nhiên giữa Bắc và Trung Altai. Đèo thoải rộng, phủ rừng tuyết tùng và đồng cỏ cao nguyên, là điểm dừng nghỉ và trượt tuyết mùa đông.",
    "Đèo Seminsky (tiếng Altai: Дьал-Менку - 'ngọn núi vĩnh cửu') là điểm cao nhất mà Chuysky Trakt vượt qua, ở độ cao khoảng 1.717 m so với mực nước biển. Khác với vẻ hiểm trở của Chike-Taman, Seminsky là con đèo dài và thoai thoải, hai bên là rừng tuyết tùng (kedr) cùng những trảng cỏ núi cao thoáng đãng. Trên đỉnh có đài kỷ niệm 200 năm Altai gia nhập nước Nga, một trung tâm huấn luyện thể thao vùng cao và các quầy bán mật ong, thảo dược, hạt tuyết tùng. Mùa đông nơi đây trở thành điểm trượt tuyết và nghỉ dưỡng, còn mùa hè là chốn hít thở không khí trong lành, ngắm hoa cỏ cao nguyên. Đèo đánh dấu ranh giới cảnh quan giữa Bắc và Trung Altai, nên qua đây thiên nhiên đổi khác rõ rệt.",
    [
        "Đèo CAO NHẤT trên Chuysky Trakt (~1.717 m), ranh giới Bắc – Trung Altai.",
        "Rừng tuyết tùng, đồng cỏ cao nguyên và đài kỷ niệm 200 năm Altai thuộc Nga.",
        "Điểm trượt tuyết mùa đông, mua mật ong và hạt tuyết tùng.",
    ],
    p("Ngoài trời, tự do suốt ngày đêm; quầy hàng và cơ sở thể thao hoạt động ban ngày.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Mùa hè ngắm hoa cỏ, mùa đông trượt tuyết.",
      "Trên cao gió lạnh và loãng khí - mang áo ấm. Có thể đi bộ nhẹ vào rừng tuyết tùng gần đỉnh."),
    [
        {"title": "Wikipedia (RU) — Семинский перевал", "url": "https://ru.wikipedia.org/wiki/Семинский_перевал"},
    ],
    ["mountain-pass", "chuysky-trakt", "cedar-forest", "skiing", "nature", "altai"],
    maps_text("Семинский перевал", "Республика Алтай", "Seminsky Pass", "Altai Republic", 51.0453, 85.6042),
))

# 4) Đèo Ulagan (đèo Krasnye Vorota gần đó) -------------------------------------------
RECORDS.append(rec(
    "ulagan-pass",
    "Đèo Ulagan",
    "Улаганский перевал",
    "Ulagan Pass",
    ["park_garden"],
    50.482449, 87.629823,
    "Huyện Ulagansky, Cộng hoà Altai, Nga (trên đường từ Aktash đi Balyktuyul)",
    "Đèo Ulagan là một trong những đèo cao nhất Altai, đỉnh khoảng 2.080 m, nằm giữa vùng cao nguyên hồ và rừng taiga khắc nghiệt. Cảnh quan quanh đèo là những hồ nước nhỏ, đầm lầy núi cao và rừng tuyết tùng thưa.",
    "Đèo Ulagan vượt qua cao nguyên Ulagan ở độ cao khoảng 2.080 m, thuộc hàng những con đèo ô tô cao nhất của Cộng hoà Altai. Con đường lên đèo đi qua vùng đất hoang sơ đặc trưng vùng cao: những hồ băng nhỏ lấp lánh, trảng đầm lầy núi và rừng tuyết tùng còi cọc chịu gió. Không xa đèo là danh thắng 'Cổng Đỏ' (Krasnye Vorota) - khe đá đỏ rực do quặng chu sa và cinnabar tạo màu, nơi con đường len giữa hai vách đá dựng đứng bên dòng sông Chibitka. Vùng Ulagan còn là cửa ngõ dẫn tới thung lũng Pazyryk khảo cổ và xuống thung lũng Chulyshman. Khí hậu ở đây lạnh và thay đổi nhanh, mang lại cảm giác hoang vắng, tách biệt của một Altai nguyên thuỷ ít người lui tới.",
    [
        "Một trong những đèo ô tô CAO NHẤT Altai (~2.080 m), cảnh quan cao nguyên hồ.",
        "Gần danh thắng 'Cổng Đỏ' (Krasnye Vorota) - khe đá đỏ do quặng chu sa.",
        "Cửa ngõ tới thung lũng khảo cổ Pazyryk và thung lũng Chulyshman.",
    ],
    p("Ngoài trời, tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 20–30 phút (kết hợp dừng ở Cổng Đỏ).",
      "Mùa hè (tháng 6–9); ngoài thời gian này đường có thể tuyết băng.",
      "Đường xa, ít trạm tiếp liệu - đổ đầy xăng ở Aktash. Thời tiết đổi nhanh, luôn mang áo ấm."),
    [
        {"title": "Wikipedia (RU) — Улаганский перевал", "url": "https://ru.wikipedia.org/wiki/Улаганский_перевал"},
    ],
    ["mountain-pass", "highland", "krasnye-vorota", "nature", "ulagan", "altai"],
    maps_text("Улаганский перевал", "Республика Алтай", "Ulagan Pass", "Altai Republic", 50.482449, 87.629823),
))

# 5) Thác Korbu -----------------------------------------------------------------------
RECORDS.append(rec(
    "korbu-waterfall",
    "Thác Korbu",
    "Водопад Корбу",
    "Korbu Waterfall",
    ["park_garden"],
    51.7061, 87.6842,
    "Bờ đông hồ Teletskoye, khu bảo tồn thiên nhiên Altaisky, huyện Turochaksky, Cộng hoà Altai, Nga",
    "Korbu là thác nước nổi tiếng nhất bên hồ Teletskoye, cao khoảng 12,8 m, đổ ầm ầm giữa rừng taiga trên bờ đông của hồ. Thác nằm trong khu bảo tồn thiên nhiên Altaisky và chỉ đến được bằng thuyền.",
    "Thác Korbu là điểm đến biểu tượng của hồ Teletskoye, cao khoảng 12,8 m, tung bọt trắng xoá giữa khung cảnh rừng taiga nguyên sinh trên bờ đông của hồ. Vì nằm trong khu bảo tồn thiên nhiên quốc gia Altaisky (Di sản Thế giới UNESCO), thác chỉ có thể tiếp cận bằng thuyền hoặc tàu cao tốc khởi hành từ làng Artybash ở đầu bắc hồ. Một sàn gỗ và lối đi lát ván dẫn du khách tới sát chân thác, nơi hơi nước mát lạnh bay mù mịt và tiếng nước gầm vang. Khu vực bến thác có các quầy bán cá hun khói, mật ong, trà thảo mộc và đồ lưu niệm bản địa. Chuyến đi thuyền tới Korbu thường kết hợp ngắm nhiều thác và vịnh khác, là trải nghiệm không thể bỏ qua khi tới Teletskoye.",
    [
        "Thác nổi tiếng nhất hồ Teletskoye (~12,8 m), nằm trong khu bảo tồn UNESCO Altaisky.",
        "Chỉ tới được bằng thuyền/tàu cao tốc từ làng Artybash - hành trình ngắm hồ tuyệt đẹp.",
        "Có sàn ngắm sát chân thác và quầy đặc sản (cá hun khói, mật ong) bản địa.",
    ],
    p("Tiếp cận theo tour thuyền ban ngày, thường mùa hè; cần xin phép vào khu bảo tồn (đã gồm trong tour).",
      "Có phí lên bờ vào khu bảo tồn (thường vài trăm rúp) cộng giá thuê thuyền.",
      "Khoảng 1–3 giờ (gồm thời gian đi thuyền).",
      "Mùa hè (tháng 6–9); sau mưa thác đầy nước và hùng vĩ nhất.",
      "Chọn tour thuyền uy tín ở Artybash; mang áo khoác chống nước vì hơi thác và gió hồ khá lạnh."),
    [
        {"title": "Wikipedia (RU) — Корбу (водопад)", "url": "https://ru.wikipedia.org/wiki/Корбу_(водопад)"},
    ],
    ["waterfall", "lake-teletskoye", "nature-reserve", "unesco", "boat-tour", "altai"],
    maps_text("Водопад Корбу", "Республика Алтай", "Korbu Waterfall", "Altai Republic", 51.7061, 87.6842),
))

# ============================ NHÓM 2: THÁC & HỒ NÚI CAO ============================

# 6) Thác Uchar (thác Bolshoy Chulchinsky) -------------------------------------------
RECORDS.append(rec(
    "uchar-waterfall",
    "Thác Uchar (thác Chulchinsky Lớn)",
    "Водопад Учар (Большой Чульчинский)",
    "Uchar Waterfall (Great Chulcha Waterfall)",
    ["park_garden"],
    51.1179, 88.0836,
    "Trên sông Chulcha, thung lũng Chulyshman, huyện Ulagansky, Cộng hoà Altai, Nga",
    "Uchar là thác nước tầng cao nhất Altai, cao khoảng 160 m, nằm sâu trong khu bảo tồn Altaisky bên nhánh sông Chulcha. Đến được thác phải đi bộ đường mòn hoang dã men vách núi, thưởng cho du khách một trong những cảnh tượng hùng vĩ nhất vùng.",
    "Thác Uchar - còn gọi là thác Chulchinsky Lớn - là dòng thác dạng ghềnh bậc thang cao nhất Cộng hoà Altai, đổ xuống khoảng 160 m qua vô số khối đá khổng lồ trên sông Chulcha, một nhánh của Chulyshman. Thác tương đối 'trẻ', hình thành sau một trận sạt lở núi cách đây vài thế kỷ, nên dòng nước cuộn xoáy dữ dội giữa ngổn ngang đá tảng. Để tới đây, du khách phải vượt sông Chulyshman rồi đi bộ khoảng 8–12 km đường mòn khó, băng qua sườn dốc, suối và những đoạn cheo leo - hành trình mất gần cả ngày. Thác nằm trong khu bảo tồn thiên nhiên Altaisky (Di sản Thế giới UNESCO) nên cần giấy phép và thường đi cùng hướng dẫn viên bản địa. Phần thưởng là khung cảnh nước trắng gào thét giữa núi non nguyên sơ, xứng đáng công sức bỏ ra.",
    [
        "Thác dạng ghềnh CAO NHẤT Altai (~160 m), trên sông Chulcha trong khu bảo tồn UNESCO.",
        "Chỉ đến được bằng đường mòn đi bộ 8–12 km khó, mất gần cả ngày.",
        "Cảnh nước cuộn giữa đá tảng khổng lồ, hoang sơ bậc nhất vùng Altai.",
    ],
    p("Đi trong ngày theo tuyến trek; cần giấy phép vào khu bảo tồn Altaisky và nên có hướng dẫn viên.",
      "Phí vào khu bảo tồn (vài trăm rúp) cộng chi phí hướng dẫn/đưa đò qua sông.",
      "Cả ngày (6–9 giờ cả đi lẫn về).",
      "Mùa hè (tháng 6–9), khi đường mòn khô ráo và an toàn hơn.",
      "Đường mòn nguy hiểm ở vài đoạn - đi giày trek, mang đủ nước, không đi một mình. Xuất phát sớm."),
    [
        {"title": "Wikipedia (RU) — Большой Чульчинский водопад", "url": "https://ru.wikipedia.org/wiki/Большой_Чульчинский_водопад"},
    ],
    ["waterfall", "chulyshman", "trekking", "nature-reserve", "unesco", "altai"],
    maps_text("Водопад Учар", "Республика Алтай", "Uchar Waterfall", "Altai Republic", 51.1179, 88.0836),
))

# 7) Thác Kamyshlinsky ---------------------------------------------------------------
RECORDS.append(rec(
    "kamyshlinsky-waterfall",
    "Thác Kamyshlinsky",
    "Камышлинский водопад",
    "Kamyshlinsky Waterfall",
    ["park_garden"],
    51.6698, 85.7562,
    "Trên sông Kamyshla gần làng Barangol / Ust-Sema, huyện Chemalsky, Cộng hoà Altai, Nga",
    "Kamyshlinsky là thác nước hai bậc dễ tiếp cận trên sông Kamyshla, gần đầu tuyến du lịch sông Katun. Thác cao khoảng 12 m, là điểm dạo bộ và chụp ảnh quen thuộc chỉ cách Chuysky Trakt một quãng ngắn.",
    "Thác Kamyshlinsky nằm trên con sông nhỏ Kamyshla, ngay trước khi nó đổ vào sông Katun, thuộc khu vực làng Barangol - Ust-Sema. Đây là một trong những thác dễ tới nhất Altai: từ các khu nghỉ ven Katun, du khách có thể đi bộ theo đường mòn ven sông vài km, hoặc đi thuyền/qua cầu treo rồi men theo lối rừng. Thác cao khoảng 12 m, đổ thành hai bậc qua vách đá, tạo hồ nước nhỏ trong vắt phía dưới nơi nhiều người thích chụp ảnh. Xung quanh là rừng lá kim và bạch dương mát rượi, có cầu treo bắc qua Katun và các quầy đặc sản. Nhờ khoảng cách gần và đường dễ đi, Kamyshlinsky phù hợp với gia đình, người lớn tuổi và những ai muốn ngắm thác Altai mà không phải trek đường dài.",
    [
        "Thác hai bậc cao ~12 m, DỄ tiếp cận nhất nhì Altai, gần Chuysky Trakt.",
        "Đi bộ ven sông vài km hoặc qua cầu treo Katun - hợp gia đình và người lớn tuổi.",
        "Hồ nước nhỏ dưới chân thác và rừng lá kim quanh năm mát mẻ.",
    ],
    p("Ngoài trời; đường mòn/cầu treo hoạt động ban ngày, mùa ấm.",
      "Có thể thu phí nhỏ qua cầu treo hoặc lối vào tư nhân (vài chục–trăm rúp).",
      "Khoảng 2–3 giờ cả đi bộ.",
      "Cuối xuân đến đầu thu; mùa nước lớn thác đẹp nhất.",
      "Đi giày bám tốt vì đá ven thác trơn. Kết hợp nghỉ tại các khu ven Katun gần Ust-Sema."),
    [
        {"title": "Wikipedia (RU) — Камышлинский водопад", "url": "https://ru.wikipedia.org/wiki/Камышлинский_водопад"},
    ],
    ["waterfall", "katun", "easy-hike", "suspension-bridge", "nature", "altai"],
    maps_text("Камышлинский водопад", "Республика Алтай", "Kamyshlinsky Waterfall", "Altai Republic", 51.6698, 85.7562),
))

# 8) Hồ Akkem --------------------------------------------------------------------------
RECORDS.append(rec(
    "akkem-lake",
    "Hồ Akkem",
    "Аккемское озеро",
    "Akkem Lake",
    ["park_garden"],
    49.9069, 86.5467,
    "Chân sườn bắc núi Belukha, huyện Ust-Koksinsky, Cộng hoà Altai, Nga",
    "Hồ Akkem nằm ngay dưới bức tường băng phía bắc của núi Belukha - đỉnh cao nhất Siberia. Mặt hồ màu xám sữa do bột băng, phản chiếu khối núi tuyết Belukha, là điểm đến trong mơ của dân leo núi và trekking.",
    "Hồ Akkem trải mình ở độ cao khoảng 2.050 m dưới chân bức tường băng Akkem hùng vĩ của núi Belukha (4.506 m) - đỉnh cao nhất dãy Altai và cả Siberia. Nước hồ mang màu trắng xám đặc trưng do chứa bột đá mịn từ sông băng, và trong những ngày lặng gió, mặt hồ phản chiếu khối núi tuyết đôi Belukha tạo nên một trong những khung cảnh nổi tiếng nhất nước Nga. Đây là điểm hội tụ của các cung trekking và leo núi: quanh hồ có trạm cứu hộ, lều trại, chùa và nhà nghỉ đơn sơ. Từ Akkem, du khách có thể đi tiếp tới Thung lũng Bảy Hồ, sông băng Akkem hay hồ Kucherla lân cận. Để đến hồ thường phải đi bộ nhiều ngày từ làng Tyungur hoặc kết hợp trực thăng, giữa khung cảnh núi non thiêng liêng mà người Altai coi là chốn linh khí.",
    [
        "Nằm dưới bức tường băng phía bắc núi Belukha (4.506 m) - đỉnh cao nhất Siberia.",
        "Nước hồ màu trắng xám do bột băng, phản chiếu khối núi tuyết Belukha.",
        "Điểm tập kết của dân trekking/leo núi, cửa ngõ tới Thung lũng Bảy Hồ và sông băng Akkem.",
    ],
    p("Ngoài trời, mùa trek từ khoảng tháng 6 đến tháng 9.",
      "Miễn phí (chi phí chủ yếu là dẫn đường, ngựa thồ hoặc trực thăng).",
      "Thường 2–4 ngày trek khứ hồi từ Tyungur (hoặc ~20 phút bay trực thăng).",
      "Giữa mùa hè, khi đường mòn khô và Belukha ít mây.",
      "Độ cao lớn, thời tiết đổi nhanh - chuẩn bị đồ trek chuyên dụng, đi cùng hướng dẫn viên có kinh nghiệm."),
    [
        {"title": "Wikipedia (RU) — Аккемское озеро", "url": "https://ru.wikipedia.org/wiki/Аккемское_озеро"},
    ],
    ["mountain-lake", "belukha", "glacier", "trekking", "unesco", "altai"],
    maps_text("Аккемское озеро", "Республика Алтай", "Akkem Lake", "Altai Republic", 49.9069, 86.5467),
))

# 9) Hồ Kucherla ----------------------------------------------------------------------
RECORDS.append(rec(
    "kucherla-lake",
    "Hồ Kucherla",
    "Кучерлинское озеро",
    "Kucherla Lake",
    ["park_garden"],
    49.8375, 86.4247,
    "Thung lũng sông Kucherla, sườn bắc dãy Katunsky, huyện Ust-Koksinsky, Cộng hoà Altai, Nga",
    "Hồ Kucherla là hồ băng tuyệt đẹp nằm ở thung lũng bên cạnh hồ Akkem, dưới chân dãy Katunsky. Nước hồ mang màu ngọc lam sữa đặc trưng, được rừng tuyết tùng và các đỉnh tuyết bao quanh.",
    "Hồ Kucherla dài khoảng 5 km nằm ở độ cao chừng 1.790 m trong thung lũng sông Kucherla, phía tây khối núi Belukha. Được tạo thành do băng hà, hồ khoác màu ngọc lam pha trắng sữa nhờ bột đá lơ lửng, đổi sắc theo ánh nắng từ xanh ngọc tới xanh lam thẫm. Bao quanh hồ là rừng tuyết tùng cổ thụ, đồng cỏ hoa và những vách núi tuyết phản chiếu xuống mặt nước phẳng lặng. Cùng với hồ Akkem, Kucherla là một trong hai viên ngọc của vùng Belukha và thường nằm trên cùng cung trekking vòng quanh đỉnh núi thiêng. Đường tới hồ đi qua thung lũng Kucherla với các bãi đá khắc cổ (petroglyph) ở Kuylyu, băng qua rừng taiga hoang sơ. Đây là chốn cắm trại lý tưởng cho những ai muốn tận hưởng vẻ đẹp tinh khôi và tĩnh lặng của Altai thượng nguồn.",
    [
        "Hồ băng dài ~5 km ở độ cao ~1.790 m, nước ngọc lam sữa đổi màu theo nắng.",
        "Nằm ở thung lũng sông Kucherla phía tây núi Belukha, cùng cung trek với hồ Akkem.",
        "Đường tới hồ qua rừng tuyết tùng và bãi đá khắc cổ Kuyulu.",
    ],
    p("Ngoài trời, mùa trek khoảng tháng 6 đến tháng 9.",
      "Miễn phí (chi phí dẫn đường, ngựa thồ).",
      "Thường 2–3 ngày trek khứ hồi từ Tyungur.",
      "Giữa mùa hè, trời quang để hồ lên màu đẹp nhất.",
      "Trek đường dài vùng cao - cần thể lực, đồ ấm và hướng dẫn viên. Kết hợp thăm hồ Akkem cùng chuyến."),
    [
        {"title": "Wikipedia (RU) — Кучерлинское озеро", "url": "https://ru.wikipedia.org/wiki/Кучерлинское_озеро"},
    ],
    ["mountain-lake", "belukha", "glacier", "trekking", "cedar-forest", "altai"],
    maps_text("Кучерлинское озеро", "Республика Алтай", "Kucherla Lake", "Altai Republic", 49.8375, 86.4247),
))

# 10) Cụm hồ Karakol -----------------------------------------------------------------
RECORDS.append(rec(
    "karakol-lakes",
    "Cụm hồ Karakol",
    "Каракольские озёра",
    "Karakol Lakes",
    ["park_garden"],
    51.4833, 86.3833,
    "Sườn tây dãy Iolgo, huyện Chemalsky, Cộng hoà Altai, Nga",
    "Cụm hồ Karakol là chuỗi bảy hồ băng xếp bậc thang trên sườn núi Iolgo, mỗi hồ một độ cao và sắc nước khác nhau. Đây là điểm trekking được yêu thích ở Trung Altai, nằm trong khu danh thắng thiên nhiên được bảo vệ.",
    "Cụm hồ Karakol gồm bảy hồ băng nối tiếp nhau theo bậc thang trên sườn tây dãy Iolgo, trải từ độ cao khoảng 1.820 m đến hơn 2.000 m. Các hồ được nối bằng những dòng suối nhỏ, và điều thú vị là mỗi hồ mang sắc nước cùng hệ thực vật hơi khác nhau tuỳ độ cao - từ hồ dưới thấp viền rừng tuyết tùng đến hồ trên cao trơ trọi giữa đá và đồng rêu núi. Toàn khu vực là một đài quan sát tự nhiên về sự chuyển tiếp các đới cảnh quan, đồng thời là điểm dã ngoại, cưỡi ngựa và trekking phổ biến từ vùng Elekmonar - Chemal. Khu vực được công nhận là di tích thiên nhiên và nằm trong vùng đệm sinh thái nên cần giữ gìn cẩn thận. Đường lên hồ thường đi bằng xe địa hình một đoạn rồi đi bộ hoặc cưỡi ngựa, phù hợp cho chuyến 1–2 ngày khám phá thiên nhiên Trung Altai.",
    [
        "Chuỗi BẢY hồ băng xếp bậc thang, mỗi hồ một độ cao và sắc nước riêng.",
        "Đài quan sát tự nhiên về các đới cảnh quan trên sườn dãy Iolgo.",
        "Điểm trekking, cưỡi ngựa quen thuộc từ vùng Elekmonar – Chemal.",
    ],
    p("Ngoài trời, mùa ấm khoảng tháng 6 đến tháng 9.",
      "Có thể thu phí vào khu di tích thiên nhiên và phí dịch vụ xe/ngựa.",
      "1–2 ngày (đi xe địa hình kết hợp đi bộ/cưỡi ngựa).",
      "Giữa mùa hè, khi hoa núi nở và đường khô ráo.",
      "Đường lên gồ ghề, nên đi tour có xe địa hình và người dẫn. Mang áo mưa vì thời tiết núi thất thường."),
    [
        {"title": "Wikipedia (RU) — Каракольские озёра", "url": "https://ru.wikipedia.org/wiki/Каракольские_озёра"},
    ],
    ["mountain-lakes", "iolgo-range", "trekking", "horse-riding", "nature", "altai"],
    maps_text("Каракольские озёра", "Республика Алтай", "Karakol Lakes", "Altai Republic", 51.4833, 86.3833),
))

# ============================ NHÓM 3: HANG, CAO NGUYÊN, CÔNG VIÊN, THUNG LŨNG ============================

# 11) Hồ Manzherok --------------------------------------------------------------------
RECORDS.append(rec(
    "manzherok-lake",
    "Hồ Manzherok",
    "Манжерокское озеро",
    "Manzherok Lake",
    ["park_garden"],
    51.8236, 85.8206,
    "Gần làng Manzherok, huyện Maiminsky, Cộng hoà Altai, Nga",
    "Hồ Manzherok là hồ nước ấm nông nằm gần làng Manzherok, được coi là di tích thiên nhiên với loài củ ấu quý hiếm mọc trên mặt nước. Hồ nằm ngay dưới chân núi Sinyukha và khu nghỉ cáp treo Manzherok.",
    "Hồ Manzherok là một hồ nhỏ, nông và ấm nằm trong thung lũng sông Katun gần làng Manzherok, ở độ cao khoảng 400 m. Khác với những hồ băng lạnh giá trên núi cao, Manzherok là hồ đồng bằng được sưởi ấm tốt vào mùa hè, quanh bờ mọc lau sậy và đặc biệt là loài củ ấu nổi (chilim) - thực vật thuỷ sinh cổ được đưa vào Sách Đỏ. Nhờ vẻ đẹp yên bình và giá trị sinh thái, hồ được công nhận là di tích thiên nhiên của Cộng hoà Altai. Hồ nằm ngay dưới chân núi Sinyukha, nơi có khu nghỉ dưỡng và tuyến cáp treo Manzherok hiện đại, nên khu vực này trở thành một trong những cụm du lịch nhộn nhịp nhất Bắc Altai. Du khách có thể dạo quanh hồ, chèo thuyền, câu cá và kết hợp lên cáp treo ngắm toàn cảnh thung lũng Katun.",
    [
        "Hồ đồng bằng nông, ấm, là di tích thiên nhiên với loài củ ấu nổi trong Sách Đỏ.",
        "Nằm dưới chân núi Sinyukha, cạnh khu nghỉ và cáp treo Manzherok.",
        "Điểm dạo bộ, chèo thuyền, câu cá dễ chịu ở Bắc Altai.",
    ],
    p("Ngoài trời, quanh năm; các dịch vụ thuyền hoạt động mùa ấm.",
      "Vào hồ thường miễn phí; thuê thuyền/dịch vụ tính phí riêng.",
      "Khoảng 1–2 giờ.",
      "Mùa hè, khi nước ấm và củ ấu nở kín mặt hồ.",
      "Không hái củ ấu (loài được bảo vệ). Kết hợp lên cáp treo Manzherok gần đó để ngắm toàn cảnh."),
    [
        {"title": "Wikipedia (RU) — Манжерокское озеро", "url": "https://ru.wikipedia.org/wiki/Манжерокское_озеро"},
    ],
    ["lake", "nature-monument", "manzherok", "katun-valley", "family", "altai"],
    maps_text("Манжерокское озеро", "Республика Алтай", "Manzherok Lake", "Altai Republic", 51.8236, 85.8206),
))

# 12) Hang động Tavda (Tavdinskie peschery) ------------------------------------------
RECORDS.append(rec(
    "tavda-caves",
    "Hệ hang động Tavda",
    "Тавдинские пещеры",
    "Tavda (Tavdinskie) Caves",
    ["park_garden"],
    51.7687, 85.7164,
    "Khu du lịch Biryuzovaya Katun, bờ trái sông Katun, huyện Altaisky/Maiminsky, Cộng hoà Altai, Nga",
    "Hệ hang Tavda là quần thể hàng chục hang động đá vôi trên vách núi bên bờ sông Katun, thuộc khu du lịch Biryuzovaya Katun. Đây là điểm khảo cổ và tham quan hang dễ tiếp cận, nổi bật với 'Cổng Trời' Tavda.",
    "Hệ hang động Tavda (Tavdinskie peschery) là một dải gồm khoảng 30 hang đá vôi karst nằm trên sườn núi bên bờ trái sông Katun, ngay trong khu du lịch Biryuzovaya Katun. Các hang thông nhau bằng lối đi và ngách, đã được lắp bậc thang, lan can và chiếu sáng để du khách tham quan an toàn. Giới khảo cổ từng tìm thấy dấu tích cư trú của người cổ đại từ thời đồ đồng và đồ sắt trong các hang này, cho thấy nơi đây đã có người sinh sống từ hàng nghìn năm trước. Điểm nhấn nổi tiếng là 'Cổng Trời Tavda' (Tavdinskaya arka) - một vòm đá tự nhiên trên đỉnh vách, nơi có thể phóng tầm mắt ngắm thung lũng Katun uốn lượn. Nhờ nằm sát khu nghỉ dưỡng và đường lớn, Tavda là một trong những hang động dễ thăm nhất Altai, phù hợp cho cả gia đình.",
    [
        "Quần thể ~30 hang đá vôi karst bên sông Katun, có bậc thang và chiếu sáng.",
        "Di chỉ cư trú của người cổ đại (đồ đồng, đồ sắt) - giá trị khảo cổ.",
        "'Cổng Trời Tavda' - vòm đá tự nhiên ngắm toàn cảnh thung lũng Katun.",
    ],
    p("Thường mở cửa ban ngày, mùa ấm (khoảng 9:00–19:00); mùa đông hạn chế.",
      "Có phí tham quan hang (thường vài trăm rúp).",
      "Khoảng 1–1,5 giờ.",
      "Cuối xuân đến đầu thu; ngày khô ráo để leo bậc an toàn.",
      "Đi giày bám tốt, mang đèn pin. Có tuyến zipline và cầu treo qua Katun gần đó để kết hợp."),
    [
        {"title": "Wikipedia (RU) — Тавдинские пещеры", "url": "https://ru.wikipedia.org/wiki/Тавдинские_пещеры"},
    ],
    ["cave", "karst", "archaeology", "biryuzovaya-katun", "family", "altai"],
    maps_text("Тавдинские пещеры", "Республика Алтай", "Tavda Caves", "Altai Republic", 51.7687, 85.7164),
))

# 13) Cao nguyên Ukok -----------------------------------------------------------------
RECORDS.append(rec(
    "ukok-plateau",
    "Cao nguyên Ukok",
    "Плоскогорье Укок",
    "Ukok Plateau",
    ["park_garden"],
    49.3078, 87.5947,
    "Huyện Kosh-Agachsky, cực nam Cộng hoà Altai, giáp Kazakhstan, Trung Quốc và Mông Cổ",
    "Ukok là cao nguyên hoang vắng ở độ cao hơn 2.200 m nơi bốn quốc gia giao nhau, thuộc Di sản Thế giới 'Núi Vàng Altai'. Đây là vùng đất thiêng của khảo cổ Pazyryk, nơi phát hiện xác ướp 'Công chúa Ukok'.",
    "Cao nguyên Ukok trải rộng ở độ cao trên 2.200 m tại cực nam Cộng hoà Altai, nơi biên giới Nga gặp Kazakhstan, Trung Quốc và Mông Cổ. Đây là vùng thảo nguyên - đài nguyên núi cao lộng gió, với hồ băng, đầm lầy và đàn gia súc du mục, được UNESCO ghi danh trong quần thể 'Núi Vàng Altai' (Zone of Peace). Ukok có ý nghĩa tâm linh và khảo cổ đặc biệt: dưới lớp băng vĩnh cửu, các nhà khoa học đã khai quật những gò mộ Pazyryk còn nguyên vẹn, trong đó nổi tiếng nhất là xác ướp 'Công chúa Ukok' (thế kỷ 5 TCN) với hình xăm và trang phục được bảo tồn kỳ diệu. Người Altai coi đây là chốn linh thiêng, hạn chế xâm phạm. Cảnh quan Ukok hoang sơ, tách biệt và khó tiếp cận - cần giấy phép vùng biên giới - nên chỉ dành cho những chuyến đi có tổ chức, thưởng cho lữ khách một trong những vùng đất nguyên thuỷ nhất châu Á.",
    [
        "Cao nguyên >2.200 m nơi bốn nước giao nhau, thuộc Di sản UNESCO 'Núi Vàng Altai'.",
        "Vùng đất thiêng khảo cổ Pazyryk - nơi tìm thấy xác ướp 'Công chúa Ukok'.",
        "Cảnh quan thảo nguyên - đài nguyên núi cao hoang vắng, du mục và hồ băng.",
    ],
    p("Ngoài trời, mùa hè ngắn (tháng 6–9); cần giấy phép vào vùng biên giới.",
      "Miễn phí tham quan nhưng phải làm giấy phép biên giới và trả chi phí tour/xe địa hình.",
      "Thường 2–4 ngày cả hành trình.",
      "Giữa mùa hè, khi đèo và đường đất thông.",
      "Xin giấy phép biên giới trước nhiều ngày. Đi xe địa hình cùng công ty tour; tôn trọng địa điểm linh thiêng của người bản địa."),
    [
        {"title": "Wikipedia (RU) — Укок", "url": "https://ru.wikipedia.org/wiki/Укок"},
        {"title": "UNESCO — Golden Mountains of Altai", "url": "https://whc.unesco.org/en/list/768/"},
    ],
    ["plateau", "unesco", "pazyryk", "ukok-princess", "border-zone", "altai"],
    maps_text("Плоскогорье Укок", "Республика Алтай", "Ukok Plateau", "Altai Republic", 49.3078, 87.5947),
))

# 14) Công viên tự nhiên Uch-Enmek ---------------------------------------------------
RECORDS.append(rec(
    "uch-enmek-nature-park",
    "Công viên tự nhiên Uch-Enmek (thung lũng Karakol)",
    "Природный парк Уч-Энмек",
    "Uch-Enmek Nature Park",
    ["park_garden"],
    50.760461, 85.852058,
    "Thung lũng Karakol gần làng Karakol/Kulada, huyện Ongudaysky, Cộng hoà Altai, Nga",
    "Uch-Enmek là công viên tự nhiên - văn hoá bảo vệ thung lũng thiêng Karakol, nơi tập trung dày đặc gò mộ, bia đá và tranh khắc cổ. Ngọn núi thiêng Uch-Enmek ba đỉnh được người Altai coi là trục tâm linh của vùng.",
    "Công viên tự nhiên Uch-Enmek được lập để gìn giữ thung lũng Karakol - một trong những cảnh quan linh thiêng và giàu di sản khảo cổ bậc nhất Altai. Trên nền thảo nguyên núi rộng lớn là hàng loạt di tích trải dài nhiều thiên niên kỷ: gò mộ scythia (kurgan), bia đá khắc hình (bãi mộ Bashadar nổi tiếng), các phiến đá dựng và tranh khắc trên đá. Ngọn núi ba đỉnh Uch-Enmek phủ tuyết được cư dân bản địa tôn kính như trung tâm năng lượng, trục nối trời - đất. Công viên vận hành theo mô hình kết hợp bảo tồn thiên nhiên với văn hoá tinh thần của người Altai: du khách được nghe truyền thuyết, tìm hiểu tín ngưỡng shaman và tôn trọng các khu vực cấm. Đây là điểm đến cho những ai muốn cảm nhận chiều sâu tâm linh và lịch sử của Altai, thay vì chỉ ngắm phong cảnh.",
    [
        "Bảo vệ thung lũng thiêng Karakol với gò mộ scythia, bia đá và bãi mộ Bashadar.",
        "Núi ba đỉnh Uch-Enmek được người Altai coi là trục tâm linh của vùng.",
        "Mô hình kết hợp bảo tồn thiên nhiên với văn hoá, tín ngưỡng bản địa.",
    ],
    p("Ngoài trời; nên liên hệ ban quản lý công viên hoặc trung tâm dân tộc trước khi vào.",
      "Có phí vào công viên và phí hướng dẫn văn hoá.",
      "Nửa ngày đến một ngày.",
      "Mùa hè (tháng 6–9) khi thảo nguyên xanh và đường khô.",
      "Tôn trọng khu vực thiêng, không trèo lên hay chạm gò mộ. Nên đi cùng hướng dẫn viên bản địa để hiểu ý nghĩa di tích."),
    [
        {"title": "Wikipedia (RU) — Уч-Энмек", "url": "https://ru.wikipedia.org/wiki/Уч-Энмек"},
    ],
    ["nature-park", "karakol-valley", "kurgan", "sacred-site", "ethnography", "altai"],
    maps_text("Природный парк Уч-Энмек", "Республика Алтай", "Uch-Enmek Nature Park", "Altai Republic", 50.760461, 85.852058),
))

# 15) Thung lũng Chulyshman ----------------------------------------------------------
RECORDS.append(rec(
    "chulyshman-valley",
    "Thung lũng Chulyshman",
    "Долина реки Чулышман",
    "Chulyshman Valley",
    ["park_garden"],
    51.3639, 87.7625,
    "Huyện Ulagansky, dọc sông Chulyshman từ đèo Katu-Yaryk tới hồ Teletskoye, Cộng hoà Altai, Nga",
    "Thung lũng Chulyshman là hẻm núi sâu và hùng vĩ chạy dọc sông Chulyshman, từ đèo Katu-Yaryk xuống tới đầu nam hồ Teletskoye. Hai bên là vách đá dựng đứng cao hàng trăm mét, ẩn chứa thác nước, đá nấm và bãi cắm trại hoang sơ.",
    "Thung lũng Chulyshman là một trong những cảnh quan choáng ngợp nhất Altai: dòng sông Chulyshman cuộn chảy dưới đáy hẻm núi sâu, hai bên là những vách đá thẳng đứng cao 500–800 m kéo dài hàng chục km từ đèo Katu-Yaryk xuống đầu nam hồ Teletskoye. Con đường độc đạo đổ xuống thung lũng qua các khúc cua serpentine dốc đứng của Katu-Yaryk, mở ra một thế giới tách biệt với bãi bồi xanh mướt, đàn gia súc và những khu trại ven sông. Dọc thung lũng ẩn chứa nhiều kỳ quan: thác Uchar cao nhất Altai, cụm đá nấm Akkurum (Kamennye griby) kỳ dị, các thác nước nhỏ và bãi tắm sông. Vẻ hoang vu, tĩnh lặng và hùng vĩ khiến Chulyshman trở thành thiên đường cho dân phượt, cắm trại và nhiếp ảnh, dù đường vào gian nan và ít tiện nghi.",
    [
        "Hẻm núi sâu với vách đá dựng đứng 500–800 m dọc sông Chulyshman.",
        "Đường độc đạo xuống thung lũng qua đèo serpentine Katu-Yaryk ngoạn mục.",
        "Ẩn chứa thác Uchar, đá nấm Akkurum và nhiều bãi trại ven sông hoang sơ.",
    ],
    p("Ngoài trời, tự do; mùa hè là thời điểm khả thi để vào thung lũng.",
      "Miễn phí (chi phí xăng xe, trại, đưa đò qua sông).",
      "Thường 1–3 ngày khám phá.",
      "Mùa hè (tháng 6–9); mùa khác đường xuống Katu-Yaryk rất nguy hiểm.",
      "Cần xe gầm cao/4x4 vững; đổ xăng đầy ở Aktash. Ít sóng điện thoại và cửa hàng - chuẩn bị đồ tự túc."),
    [
        {"title": "Wikipedia (RU) — Чулышман", "url": "https://ru.wikipedia.org/wiki/Чулышман"},
    ],
    ["valley", "canyon", "chulyshman", "katu-yaryk", "camping", "altai"],
    maps_text("Долина Чулышмана", "Республика Алтай", "Chulyshman Valley", "Altai Republic", 51.3639, 87.7625),
))

# ============================ NHÓM 4: THẢO NGUYÊN, DÃY NÚI, NGÃ BA, SAO HỎA ============================

# 16) Thảo nguyên Kuray ---------------------------------------------------------------
RECORDS.append(rec(
    "kuray-steppe",
    "Thảo nguyên Kuray",
    "Курайская степь",
    "Kuray Steppe",
    ["park_garden"],
    50.211, 87.905,
    "Huyện Kosh-Agachsky, dọc Chuysky Trakt gần làng Kuray, Cộng hoà Altai, Nga",
    "Thảo nguyên Kuray là vùng bồn địa núi cao khô cằn ở độ cao ~1.500 m, nổi tiếng với phông nền là các đỉnh tuyết của dãy Bắc Chuysky. Đây cũng là nơi có 'ruộng bậc thang khổng lồ' - dấu tích gợn sóng do lũ băng cổ đại tạo thành.",
    "Thảo nguyên Kuray là một bồn địa liên núi rộng lớn nằm ở độ cao khoảng 1.500 m dọc Chuysky Trakt, được bao quanh bởi những dãy núi cao. Cảnh tượng biểu tượng nơi đây là dải thảo nguyên vàng nâu trải phẳng, phía sau vươn lên bức tường các đỉnh phủ tuyết quanh năm của dãy Bắc Chuysky (Severo-Chuysky) với những sông băng lấp lánh - một trong những khung hình đẹp và được chụp nhiều nhất Altai. Kuray còn nổi tiếng trong giới khoa học nhờ hệ 'giant current ripples' - những gợn sóng khổng lồ in trên mặt đất, dấu vết của các trận lũ vỡ hồ băng thời tiền sử từng quét qua thung lũng. Vùng đất khô, gió và khoáng đạt này là điểm dừng lý tưởng để ngắm núi, cắm trại, ngắm sao và làm bàn đạp tới thung lũng Aktru dưới chân các đỉnh cao. Không khí trong veo và tầm nhìn rộng khiến Kuray mang vẻ đẹp hùng vĩ, gần như siêu thực.",
    [
        "Bồn địa thảo nguyên ~1.500 m với phông nền đỉnh tuyết dãy Bắc Chuysky.",
        "Nơi có 'gợn sóng khổng lồ' - dấu tích lũ vỡ hồ băng thời tiền sử.",
        "Điểm ngắm núi, cắm trại, ngắm sao và bàn đạp tới thung lũng Aktru.",
    ],
    p("Ngoài trời, tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 1–2 giờ dừng ngắm (hoặc cắm trại qua đêm).",
      "Cuối hè - đầu thu trời quang để thấy rõ đỉnh tuyết; đêm quang ngắm sao.",
      "Ban đêm rất lạnh dù mùa hè - mang đồ ấm. Điểm ngắm đẹp nhất nằm ở rìa nam thảo nguyên nhìn về dãy Chuysky."),
    [
        {"title": "Wikipedia (RU) — Курайская степь", "url": "https://ru.wikipedia.org/wiki/Курайская_степь"},
    ],
    ["steppe", "chuysky-trakt", "north-chuysky-ridge", "stargazing", "nature", "altai"],
    maps_text("Курайская степь", "Республика Алтай", "Kuray Steppe", "Altai Republic", 50.211, 87.905),
))

# 17) Dãy Bắc Chuysky -----------------------------------------------------------------
RECORDS.append(rec(
    "north-chuysky-ridge",
    "Dãy núi Bắc Chuysky",
    "Северо-Чуйский хребет",
    "North Chuysky Ridge",
    ["park_garden"],
    50.067, 87.583,
    "Ranh giới huyện Kosh-Agachsky và Ulagansky, Cộng hoà Altai, Nga",
    "Dãy Bắc Chuysky là một trong những rặng núi tuyết đồ sộ nhất Altai, với đỉnh cao nhất Maashey-Bash ~4.177 m và nhiều sông băng. Đây là thánh địa của dân leo núi, trekking và điểm nhìn biểu tượng phía trên thảo nguyên Kuray.",
    "Dãy Bắc Chuysky (Severo-Chuysky) là bức tường núi tuyết trải dài giữa thảo nguyên Kuray và Chuya, một trong những rặng núi cao và hiểm trở nhất Cộng hoà Altai. Đỉnh cao nhất là Maashey-Bash (~4.177 m), cùng cụm 'Aktru' và 'Bish-Iirdu' phủ băng vĩnh cửu với hàng chục sông băng nuôi các dòng suối ngọc lam. Đây là địa bàn kinh điển của giới leo núi và trekking Nga: từ làng Kuray hoặc Chibit, các cung đường dẫn tới thung lũng Aktru (có trạm khí tượng - alpine camp lâu đời), hồ Shavlinskiye tuyệt đẹp và những sông băng cheo leo. Nhìn từ thảo nguyên Kuray, hàng loạt đỉnh trắng xoá của dãy Bắc Chuysky tạo nên khung cảnh hùng vĩ biểu tượng của Altai. Với cảnh quan băng hà, hồ núi và đỉnh cao, đây là điểm đến cho những ai đam mê núi non thực thụ.",
    [
        "Rặng núi tuyết đồ sộ, đỉnh Maashey-Bash ~4.177 m với hàng chục sông băng.",
        "Thánh địa leo núi/trekking: thung lũng Aktru, hồ Shavlinskiye.",
        "Phông nền biểu tượng của Altai nhìn từ thảo nguyên Kuray.",
    ],
    p("Ngoài trời, mùa trek/leo núi khoảng tháng 6 đến tháng 9.",
      "Miễn phí ngắm từ xa; các cung trek cần chi phí dẫn đường, xe địa hình.",
      "Từ nửa ngày (ngắm cảnh) đến nhiều ngày (trekking).",
      "Giữa - cuối hè, khi đường mòn thông và trời quang.",
      "Địa hình núi cao khắc nghiệt - chỉ trek/leo với hướng dẫn viên và trang bị chuyên dụng. Từ Kuray có tour xe địa hình lên gần chân núi."),
    [
        {"title": "Wikipedia (RU) — Северо-Чуйский хребет", "url": "https://ru.wikipedia.org/wiki/Северо-Чуйский_хребет"},
    ],
    ["mountain-range", "glacier", "aktru", "mountaineering", "trekking", "altai"],
    maps_text("Северо-Чуйский хребет", "Республика Алтай", "North Chuysky Ridge", "Altai Republic", 50.067, 87.583),
))

# 18) Ngã ba Chuya - Katun (Chuy-Oozy) -----------------------------------------------
RECORDS.append(rec(
    "chuya-katun-confluence",
    "Ngã ba sông Chuya - Katun (Chuy-Oozy)",
    "Слияние Чуи и Катуни (Чуй-Оозы)",
    "Chuya-Katun Confluence (Chuy-Oozy)",
    ["park_garden"],
    50.393, 86.678,
    "Gần làng Inya, huyện Ongudaysky, Chuysky Trakt km ~712, Cộng hoà Altai, Nga",
    "Chuy-Oozy là nơi hai dòng sông Chuya và Katun gặp nhau, tạo cảnh tượng hai màu nước - xanh ngọc và xám đục - chảy song song trước khi hoà làm một. Đây là điểm ngắm cảnh thiêng và ngoạn mục trên Chuysky Trakt.",
    "Ngã ba Chuy-Oozy là nơi sông Chuya mang màu xám đục nhập vào dòng Katun màu xanh ngọc, và trong nhiều thời điểm trong năm, hai màu nước chảy song song một quãng dài trước khi trộn lẫn - một hiện tượng khiến ai cũng phải dừng chân. Điểm nhìn nằm trên vách cao bên Chuysky Trakt gần làng Inya, có bãi đỗ và đài quan sát nhìn xuống hợp lưu giữa khung cảnh núi non khô cằn hùng vĩ. Đây không chỉ là kỳ quan thị giác mà còn là địa điểm được người Altai coi là linh thiêng: quanh khu vực có những cây buộc dải vải nghi lễ (kyira) và gần đó là các di tích khảo cổ như bãi đá khắc và những cột đá cổ. Chuy-Oozy thường được kết hợp trong hành trình cùng bãi petroglyph Kalbak-Tash và đèo Chike-Taman gần kề, tạo thành cụm điểm đến đặc sắc của Trung Altai.",
    [
        "Nơi hợp lưu Chuya (xám) và Katun (xanh ngọc) - cảnh hai màu nước độc đáo.",
        "Đài ngắm trên vách cao bên Chuysky Trakt gần làng Inya.",
        "Địa điểm linh thiêng của người Altai, gần petroglyph và di tích cổ.",
    ],
    p("Ngoài trời, tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Cuối xuân - đầu hè khi tương phản hai màu nước rõ nhất; nắng để lên màu đẹp.",
      "Đỗ đúng bãi ven đường, cẩn thận mép vực. Tôn trọng cây nghi lễ - không giật dải vải. Kết hợp thăm Kalbak-Tash gần đó."),
    [
        {"title": "Wikipedia (RU) — Чуй-Оозы", "url": "https://ru.wikipedia.org/wiki/Чуй-Оозы"},
    ],
    ["river-confluence", "chuysky-trakt", "viewpoint", "sacred-site", "nature", "altai"],
    maps_text("Слияние Чуи и Катуни", "Республика Алтай", "Chuya Katun Confluence", "Altai Republic", 50.393, 86.678),
))

# 19) Kyzyl-Chin ("Sao Hỏa Altai") ---------------------------------------------------
RECORDS.append(rec(
    "kyzyl-chin-altai-mars",
    "Thung lũng Kyzyl-Chin ('Sao Hỏa Altai')",
    "Кызыл-Чин («Алтайский Марс»)",
    "Kyzyl-Chin Valley (Altai Mars)",
    ["park_garden"],
    50.0197, 88.3125,
    "Thung lũng sông Kyzyl-Chin, cách làng Chagan-Uzun ~7,5 km, huyện Kosh-Agachsky, Cộng hoà Altai, Nga",
    "Kyzyl-Chin, quen gọi là 'Sao Hỏa Altai', là thung lũng có những dãy đồi đất nhiều màu đỏ, cam, vàng, tím do khoáng chất tạo nên. Cảnh quan siêu thực này gợi liên tưởng bề mặt hành tinh Đỏ, thu hút đông đảo du khách và nhiếp ảnh gia.",
    "Thung lũng Kyzyl-Chin, được đặt biệt danh 'Sao Hỏa Altai', nằm cách làng Chagan-Uzun khoảng 7,5 km dọc con sông cùng tên ở vùng khô hạn Kosh-Agach. Điều làm nên danh tiếng của nơi đây là những sườn đồi đất sét rực rỡ sắc màu - đỏ, cam, vàng, nâu, tím và cả xanh lục - do đất chứa nhiều loại khoáng đa kim và ôxít sắt lắng đọng qua hàng triệu năm. Dưới ánh nắng, các dải màu nổi bật đến mức khung cảnh trông như bề mặt Sao Hỏa, khiến du khách gọi các khu vực tham quan là 'Mars-1' và 'Mars-2'. Đây là vùng bán hoang mạc núi cao, khí hậu khắc nghiệt, gần như không cây cối, càng tô đậm vẻ ngoài hành tinh khác. Du khách có thể đi bộ dạo giữa các đồi màu, leo lên điểm cao ngắm toàn cảnh và chụp những bức ảnh ấn tượng. Kyzyl-Chin thường được ghép cùng hành trình khám phá vùng Chuya - Kosh-Agach xa xôi.",
    [
        "Đồi đất nhiều màu đỏ - cam - vàng - tím do khoáng đa kim, tựa bề mặt Sao Hỏa.",
        "Hai khu tham quan quen gọi 'Mars-1' và 'Mars-2' gần làng Chagan-Uzun.",
        "Cảnh quan bán hoang mạc núi cao siêu thực, thiên đường của nhiếp ảnh.",
    ],
    p("Ngoài trời, tự do; ban ngày mùa ấm là thời điểm tham quan.",
      "Có thể thu phí nhỏ vào khu hoặc phí gửi xe của người địa phương.",
      "Khoảng 1,5–3 giờ.",
      "Cuối hè - đầu thu, nắng nghiêng làm màu đất rực rỡ nhất.",
      "Xe con có thể tới gần Mars-1; tới Mars-2 nên đi xe gầm cao. Mang nước và mũ vì nắng gắt, ít bóng râm."),
    [
        {"title": "Wikipedia (RU) — Кызылчин (Кызыл-Чин)", "url": "https://ru.wikipedia.org/wiki/Кызылчин"},
    ],
    ["colored-hills", "altai-mars", "badlands", "chagan-uzun", "photography", "altai"],
    maps_text("Кызыл-Чин Алтайский Марс", "Республика Алтай", "Kyzyl-Chin Altai Mars", "Altai Republic", 50.0197, 88.3125),
))

# 20) Nhà máy thuỷ điện Chemal (Chemalskaya GES) -------------------------------------
RECORDS.append(rec(
    "chemal-hydro-station",
    "Nhà máy thuỷ điện Chemal (di tích)",
    "Чемальская ГЭС",
    "Chemal Hydroelectric Station",
    ["other"],
    51.39083, 86.01056,
    "Cửa sông Chemal đổ vào Katun, làng Chemal, huyện Chemalsky, Cộng hoà Altai, Nga",
    "Nhà máy thuỷ điện Chemal xây năm 1935 là một trong những công trình thuỷ điện nhỏ đầu tiên vùng Altai, nay thành điểm tham quan lịch sử bên hồ chứa nhỏ. Khu vực có đập nước, bảo tàng nhỏ và các trò giải trí ven sông Katun.",
    "Nhà máy thuỷ điện Chemal (Chemalskaya GES) được xây dựng năm 1935 bằng sức lao động của các trại viên, là một trong những nhà máy thuỷ điện đầu tiên và nhỏ của vùng Altai, đặt nơi sông Chemal đổ vào Katun. Sau nhiều thập niên vận hành và bị hư hại do lũ, nhà máy ngừng phát điện và được chuyển thành điểm du lịch - di tích kỹ thuật. Du khách tới đây để xem con đập, hồ chứa nhỏ và tìm hiểu lịch sử điện khí hoá vùng núi qua khu trưng bày. Quanh nhà máy hình thành một cụm giải trí nhộn nhịp với zipline vượt sông, tarzanka, chợ lưu niệm và quán ăn. Điểm này thường được ghép cùng đảo Patmos và tu viện gần đó trong tuyến tham quan làng Chemal - một trong những trung tâm du lịch quen thuộc nhất của vùng ven Katun.",
    [
        "Nhà máy thuỷ điện nhỏ xây 1935 - di tích lịch sử điện khí hoá vùng Altai.",
        "Có đập, hồ chứa và khu trưng bày; xung quanh là cụm giải trí ven Katun.",
        "Thường kết hợp tham quan cùng đảo Patmos và tu viện ở làng Chemal.",
    ],
    p("Thường mở cửa ban ngày, đông khách vào mùa hè.",
      "Có phí vào khu di tích và phí riêng cho các trò giải trí (zipline, tarzanka).",
      "Khoảng 1–1,5 giờ.",
      "Mùa hè khi các dịch vụ giải trí hoạt động đầy đủ.",
      "Khu vực có thể đông và thương mại hoá - đi sớm để tránh đông. Kết hợp đi bộ sang đảo Patmos gần đó."),
    [
        {"title": "Wikipedia (RU) — Чемальская ГЭС", "url": "https://ru.wikipedia.org/wiki/Чемальская_ГЭС"},
    ],
    ["hydroelectric", "historic", "chemal", "katun", "family", "altai"],
    maps_text("Чемальская ГЭС", "Республика Алтай", "Chemal Hydroelectric Station", "Altai Republic", 51.39083, 86.01056),
))

# ============================ NHÓM 5: KHU NGHỈ, CÁP TREO, CẦU TREO ============================

# 21) Khu du lịch Biryuzovaya Katun ---------------------------------------------------
RECORDS.append(rec(
    "turquoise-katun",
    "Khu du lịch Biryuzovaya Katun (Katun Ngọc Lam)",
    "Особая экономическая зона «Бирюзовая Катунь»",
    "Biryuzovaya Katun Resort",
    ["other"],
    51.7897, 85.7358,
    "Bờ trái sông Katun, huyện Altaisky, gần Manzherok, Cộng hoà Altai, Nga",
    "Biryuzovaya Katun ('Katun Ngọc Lam') là khu du lịch - nghỉ dưỡng lớn bên bờ trái sông Katun, lấy tên từ màu nước ngọc lam của sông vào mùa thu đông. Nơi đây có hồ tắm nhân tạo, hệ hang Tavda, bãi biển và nhiều hoạt động ngoài trời.",
    "Biryuzovaya Katun là một trong những khu du lịch tổng hợp lớn và phát triển nhất Bắc Altai, trải rộng trên bờ trái sông Katun đối diện làng Manzherok. Tên gọi bắt nguồn từ sắc nước ngọc lam đặc trưng của sông Katun khi mực nước xuống và trong vào mùa thu - đông. Khu vực có một hồ tắm nhân tạo được sưởi bằng nắng với bãi cát nhân tạo an toàn cho trẻ em, cùng vô số dịch vụ: hệ hang động Tavda ngay trong khu, tuyến zipline và cầu treo vượt sông Katun, cho thuê xe đạp, cưỡi ngựa, khinh khí cầu, khu cắm trại và khách sạn. Vào mùa hè nơi đây tổ chức các lễ hội, sự kiện thể thao và âm nhạc ngoài trời. Nhờ hạ tầng tốt và nằm gần đường lớn, Biryuzovaya Katun là điểm đến thuận tiện cho gia đình và những ai muốn kết hợp nghỉ dưỡng với khám phá thiên nhiên Altai.",
    [
        "Khu du lịch tổng hợp lớn bên bờ Katun, tên từ màu nước ngọc lam mùa thu - đông.",
        "Có hồ tắm bãi cát nhân tạo, hệ hang Tavda, zipline và cầu treo qua sông.",
        "Nhiều dịch vụ: cưỡi ngựa, xe đạp, cắm trại, khách sạn và lễ hội mùa hè.",
    ],
    p("Mở cửa quanh năm; sôi động và đầy đủ dịch vụ nhất vào mùa hè.",
      "Vào khu và bãi tắm có thu phí; mỗi dịch vụ (hang, zipline...) tính vé riêng.",
      "Nửa ngày đến vài ngày (nếu lưu trú).",
      "Mùa hè để tắm hồ và dự lễ hội; mùa thu ngắm Katun lên màu ngọc lam.",
      "Cuối tuần hè rất đông - đặt chỗ trước. Kết hợp thăm hang Tavda ngay trong khu."),
    [
        {"title": "Wikipedia (RU) — Бирюзовая Катунь", "url": "https://ru.wikipedia.org/wiki/Бирюзовая_Катунь"},
    ],
    ["resort", "katun", "beach", "zipline", "family", "altai"],
    maps_text("Бирюзовая Катунь", "Республика Алтай", "Biryuzovaya Katun", "Altai Republic", 51.7897, 85.7358),
))

# 22) Khu nghỉ dưỡng & cáp treo Manzherok (núi Sinyukha) -----------------------------
RECORDS.append(rec(
    "manzherok-resort",
    "Khu nghỉ dưỡng & cáp treo Manzherok (núi Sinyukha)",
    "Всесезонный курорт «Манжерок» (гора Синюха)",
    "Manzherok Resort and Cable Car (Mount Sinyukha)",
    ["other"],
    51.8130, 85.8360,
    "Sườn núi Malaya Sinyukha gần làng Manzherok, huyện Maiminsky, Cộng hoà Altai, Nga",
    "Manzherok là khu nghỉ dưỡng bốn mùa hiện đại với tuyến cáp treo lên núi Malaya Sinyukha (~1.012 m). Mùa đông là điểm trượt tuyết, mùa hè cáp treo đưa du khách lên đỉnh ngắm toàn cảnh thung lũng Katun và hồ Manzherok.",
    "Khu nghỉ dưỡng bốn mùa Manzherok là một trong những tổ hợp du lịch được đầu tư quy mô nhất Bắc Altai, nằm trên sườn núi Malaya Sinyukha ngay cạnh làng Manzherok và hồ cùng tên. Trái tim của khu là tuyến cáp treo cabin hiện đại đưa du khách từ chân núi lên gần đỉnh Sinyukha ở độ cao khoảng 1.012 m. Mùa đông, các sườn dốc biến thành khu trượt tuyết với nhiều đường trượt và dịch vụ cho thuê trang bị. Mùa hè, cáp treo trở thành phương tiện ngắm cảnh: từ đỉnh núi, tầm mắt trải khắp thung lũng sông Katun uốn lượn, hồ Manzherok và các rặng núi Bắc Altai. Trên đỉnh có đài quan sát, quán cà phê, khu chụp ảnh và những vườn đá xếp cầu may theo phong tục. Với hạ tầng khách sạn, nhà hàng và giải trí đồng bộ, Manzherok phù hợp cho gia đình và du lịch nghỉ dưỡng quanh năm.",
    [
        "Khu nghỉ bốn mùa với cáp treo cabin lên núi Malaya Sinyukha (~1.012 m).",
        "Mùa đông trượt tuyết, mùa hè lên đỉnh ngắm thung lũng Katun và hồ Manzherok.",
        "Đài quan sát, quán cà phê và hạ tầng nghỉ dưỡng đồng bộ trên đỉnh.",
    ],
    p("Cáp treo hoạt động quanh năm theo khung giờ (thường khoảng 9:00–18:00); kiểm tra lịch mùa.",
      "Vé cáp treo khứ hồi thu phí (thường vài trăm–hơn nghìn rúp); mùa trượt tuyết có vé riêng.",
      "Khoảng 2–3 giờ (gồm lên đỉnh và ngắm cảnh).",
      "Mùa đông trượt tuyết; mùa hè - thu ngắm cảnh và leo núi nhẹ.",
      "Trên đỉnh gió lạnh hơn dưới chân - mang áo khoác. Cuối tuần đông khách, nên mua vé cáp treo sớm."),
    [
        {"title": "Wikipedia (RU) — Манжерок (курорт)", "url": "https://ru.wikipedia.org/wiki/Манжерок"},
    ],
    ["resort", "cable-car", "skiing", "mount-sinyukha", "viewpoint", "altai"],
    maps_text("Курорт Манжерок канатная дорога", "Республика Алтай", "Manzherok Resort", "Altai Republic", 51.8130, 85.8360),
))

# 23) Cầu treo Oroktoy (qua ghềnh Teldekpen) -----------------------------------------
RECORDS.append(rec(
    "oroktoy-bridge",
    "Cầu treo Oroktoy (qua ghềnh Teldekpen)",
    "Ороктойский мост",
    "Oroktoy Bridge",
    ["bridge"],
    51.12306, 86.16583,
    "Trên sông Katun gần làng Oroktoy, huyện Chemalsky, Cộng hoà Altai, Nga",
    "Cầu treo Oroktoy bắc qua sông Katun tại đoạn hẻm hẹp và sâu nhất - ghềnh Teldekpen, nơi dòng sông bị ép giữa hai vách đá. Đứng trên cầu có thể nhìn xuống dòng nước xoáy màu ngọc lam cuộn chảy dưới vực sâu.",
    "Cầu treo Oroktoy là một cây cầu dây văng cho xe nhỏ và người đi bộ, bắc qua sông Katun gần làng Oroktoy. Điểm đặc biệt là cầu vắt ngang đúng đoạn ghềnh Teldekpen (Teldekpenskiye porogi) - nơi lòng Katun bị thu hẹp còn vài chục mét và khoét sâu giữa hai bức vách đá dựng đứng, tạo thành một trong những chỗ sâu nhất của con sông. Từ mặt cầu, du khách nhìn xuống dòng nước ngọc lam đặc quánh xoáy cuộn qua khe đá hẹp - cảnh tượng vừa đẹp vừa gai người. Khu vực quanh cầu có những vách đá, hang nhỏ và là điểm quen thuộc để chụp ảnh, ngắm sông. Cầu Oroktoy thường nằm trong cung đường vòng qua các làng Chemal - Kuyus dọc hữu ngạn Katun, hoặc trên đường tới các bãi đá khắc cổ và danh thắng lân cận.",
    [
        "Cầu treo vắt qua ghềnh Teldekpen - đoạn hẹp và sâu nhất của sông Katun.",
        "Ngắm dòng nước ngọc lam xoáy cuộn giữa hai vách đá dựng đứng.",
        "Nằm trên cung đường Chemal – Kuyus dọc hữu ngạn Katun.",
    ],
    p("Ngoài trời, tự do suốt ngày đêm.",
      "Miễn phí (đôi khi có phí nhỏ qua các điểm tư nhân lân cận).",
      "Khoảng 20–30 phút.",
      "Mùa hè - thu; mùa thu Katun lên màu ngọc lam đẹp nhất.",
      "Cầu tải trọng hạn chế - xe lớn không qua được. Đứng ngắm cẩn thận, giữ khoảng cách mép vực."),
    [
        {"title": "Wikipedia (RU) — Ороктойский мост", "url": "https://ru.wikipedia.org/wiki/Ороктойский_мост"},
    ],
    ["bridge", "suspension-bridge", "katun", "teldekpen", "viewpoint", "altai"],
    maps_text("Ороктойский мост", "Республика Алтай", "Oroktoy Bridge", "Altai Republic", 51.12306, 86.16583),
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
