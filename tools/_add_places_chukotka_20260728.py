# -*- coding: utf-8 -*-
"""_add_places_chukotka_20260728.py — VÙNG: Khu tự trị Chukotka (Chukotka AO).

Bối cảnh: chukotka.json hiện có 6 địa điểm (whale-bone-alley-yttygran, cape-dezhnev,
wrangel-island-reserve, anadyr-transfiguration-cathedral, egvekinot-arctic-circle,
meynypilgyno-birds). Mục tiêu nâng lên >=30. Chukotka là vùng CỰC ĐÔNG BẮC RẤT THƯA,
danh lam chủ yếu là thiên nhiên hoang dã, làng bản bản địa và di sản Bắc Cực độc đáo —
nên nhiều bản ghi thuộc nhóm "other" (đúng thực tế địa lý, KHÔNG nhồi/bịa).

Đợt này thêm 25 địa điểm THẬT SỰ tồn tại & đặc sắc, đa dạng:
- Anadyr (thủ phủ): Bảo tàng "Наследие Чукотки", tượng Thánh Nikolay, tượng nhà văn
  Yuri Rytkheu, đài kỷ niệm Ban Cách mạng đầu tiên Chukotka, tranh tường/muralы phố,
  cửa vịnh Anadyr (ngắm cá voi trắng beluga).
- Di sản/thiên nhiên độc đáo: hồ thiên thạch Elgygytgyn, VQG Beringia, đảo Kolyuchin
  (trạm cực bỏ hoang & gấu Bắc Cực), làng Yupik bỏ hoang Naukan, Uelen (xưởng chạm ngà),
  Lorino (săn cá voi truyền thống), Sireniki (làng cổ), đảo Ratmanov/Diomede Lớn (cực
  đông nước Nga), mũi Navarin, núi lửa Anyuisky, mũi Chaplina, mũi Shmidta, suối nước
  nóng Chaplino, bãi hải mã đảo Arakamchechen.
- Thị trấn/công trình: Provideniya, Pevek (cực bắc Nga) + nhà máy điện hạt nhân nổi
  "Akademik Lomonosov", Bilibino (NM điện hạt nhân Bắc Cực đầu tiên), Lavrentiya.

TOẠ ĐỘ — xác minh chéo qua Wikipedia (EN/RU), Wikidata, GeoHack (2026-07). Chukotka nằm
HAI BÊN đường đổi ngày (kinh tuyến 180): các điểm phía TÂY có lon DƯƠNG (~166–180), các
điểm phía ĐÔNG (gần Alaska) có lon ÂM (~ -180 đến -169). Quy ước này khớp dữ liệu sẵn có
(cape-dezhnev -169.65, egvekinot -179.12, wrangel -179.42 đều ÂM; anadyr +177.52 DƯƠNG).
Đã kiểm thứ tự lat/lon và dấu âm cho các điểm bên kia đường đổi ngày.

Ghi chú độ chính xác: một số tượng đài/bảo tàng ở Anadyr chưa có toạ độ toà nhà công bố
trên Wikidata; các điểm này neo trong trung tâm Anadyr (đã kiểm chứng) và link bản đồ
dùng TÌM-THEO-TÊN tiếng Nga nên ghim vẫn trỏ đúng đối tượng. Toạ độ suối nóng Chaplino
neo tại làng Novoye Chaplino kề bên.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_chukotka_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "chukotka"
REGION_NAME_VI = "Khu tự trị Chukotka"
FD = "Vùng Viễn Đông"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
    """Link bản đồ TRỎ-ĐỊA-ĐIỂM bằng text-search + canh giữa theo toạ độ đã kiểm chứng."""
    yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    return {
        "yandex": f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=13",
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

# 1) Bảo tàng "Di sản Chukotka" (Anadyr) --------------------------------------
RECORDS.append(rec(
    "chukotka-heritage-museum-anadyr",
    "Trung tâm Bảo tàng “Di sản Chukotka” (Muzeyny tsentr «Nasledie Chukotki»)",
    "Музейный центр «Наследие Чукотки»",
    "Museum Center “Chukotka Heritage” (Anadyr)",
    ["museum"],
    64.7337, 177.5093,
    "Trung tâm thành phố Anadyr, Khu tự trị Chukotka, Nga.",
    "Bảo tàng lớn nhất và hiện đại nhất vùng Chukotka, nơi kể trọn câu chuyện của miền cực đông nước Nga: văn hoá người Chukchi và Eskimo, nghệ thuật chạm ngà – xương, thiên nhiên Bắc Cực và lịch sử khai phá vùng đất băng giá.",
    "Trung tâm Bảo tàng “Di sản Chukotka” ở thủ phủ Anadyr là điểm khởi đầu lý tưởng để hiểu cả một vùng đất rộng lớn nhưng thưa vắng bậc nhất hành tinh. Sưu tập của bảo tàng trải rộng từ khảo cổ và dân tộc học của các dân tộc bản địa (Chukchi, Eskimo/Yupik, Even, Chuvan) đến bộ sưu tập nghệ thuật chạm khắc ngà hải mã và xương cá voi nổi tiếng thế giới của Chukotka. Khách tham quan còn gặp các trưng bày về thiên nhiên đài nguyên và biển Bắc Cực, về lịch sử tuyến Đường Biển Phương Bắc, về đời sống của người chăn tuần lộc và thợ săn thú biển. Bảo tàng được đầu tư bài bản với không gian trưng bày đa phương tiện, được xem là một trong những bảo tàng “sáng” và tiện nghi nhất ở vùng Viễn Đông Bắc Cực. Đây là nơi giúp du khách hình dung bức tranh tổng thể trước khi lên đường tới các làng bản và điểm hoang dã xa xôi của Chukotka.",
    [
        "Bảo tàng đầu ngành của Chukotka về văn hoá bản địa và thiên nhiên Bắc Cực.",
        "Sưu tập nghệ thuật chạm ngà hải mã và xương cá voi đặc sắc.",
        "Trưng bày đa phương tiện hiện đại, điểm định hướng trước khi khám phá vùng.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ hành chính, thường nghỉ thứ Hai; nên kiểm tra lịch trước khi đến.",
        "ticket_vi": "Vé vào cửa mức thấp; có thể có tour hướng dẫn tính phí thêm.",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Quanh năm; thuận tiện kết hợp khi ghé Anadyr mùa hè (tháng 7–8).",
        "tips_vi": "Điểm dừng đầu tiên rất đáng giá để hiểu văn hoá Chukchi/Eskimo trước khi đi các làng xa.",
    },
    [
        {"title": "Wikipedia (RU) — Анадырь", "url": "https://ru.wikipedia.org/wiki/Анадырь"},
        {"title": "Museu.ms — Chukotka Heritage Museum Center", "url": "http://museu.ms/museum/details/13485"},
    ],
    ["chukotka", "anadyr", "museum", "chukchi", "eskimo", "ivory-carving"],
    maps_text("Музейный центр Наследие Чукотки", "Анадырь", "Chukotka Heritage Museum", "Anadyr", 64.7337, 177.5093),
))

# 2) Tượng đài Thánh Nikolay (Anadyr) ----------------------------------------
RECORDS.append(rec(
    "anadyr-st-nicholas-monument",
    "Tượng đài Thánh Nikolay Kỳ Diệu (Pamyatnik Nikolayu Chudotvortsu)",
    "Памятник Николаю Чудотворцу",
    "Monument to St. Nicholas the Wonderworker (Anadyr)",
    ["monument"],
    64.7351, 177.5165,
    "Trên gò cao nhìn ra cửa vịnh Anadyr, gần Nhà thờ Chính tòa Chúa Ba Ngôi, thành phố Anadyr, Chukotka, Nga.",
    "Bức tượng đồng khổng lồ Thánh Nikolay – vị thánh bảo trợ của người đi biển và lữ khách – đứng trên gò cao đón gió biển, dang tay che chở cho thành phố cực đông nước Nga. Đây là một trong những tượng đài Thánh Nikolay lớn nhất thế giới.",
    "Vươn lên trên gò đất nhìn thẳng ra cửa vịnh Anadyr, tượng đài Thánh Nikolay Kỳ Diệu (Nikolay Chudotvorets) là một trong những biểu tượng dễ nhận ra nhất của thủ phủ Chukotka. Bức tượng bằng đồng cao lớn khắc hoạ vị thánh – người được tín đồ Chính Thống giáo tôn là đấng bảo trợ của thuỷ thủ, ngư dân và những người đi đường xa – trong tư thế ban phước, hướng ra biển như đang canh giữ cho những con tàu ra vào cảng và cho cả thành phố quanh năm gió tuyết. Công trình được dựng đầu những năm 2000, cùng thời với việc xây Nhà thờ Chính tòa Chúa Ba Ngôi bằng gỗ gần đó, tạo thành cụm điểm nhấn tâm linh của Anadyr. Từ chân tượng, du khách có tầm nhìn đẹp bao quát cửa vịnh, khu cảng và những dãy nhà nhiều màu của thành phố – một điểm chụp ảnh và ngắm cảnh quen thuộc.",
    [
        "Một trong những tượng đài Thánh Nikolay lớn nhất thế giới.",
        "Vị trí trên gò cao, tầm nhìn đẹp bao quát cửa vịnh và cảng Anadyr.",
        "Tạo thành cụm điểm nhấn cùng Nhà thờ Chính tòa Chúa Ba Ngôi bằng gỗ.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–30 phút.",
        "best_time_vi": "Mùa hè (tháng 6–8) trời sáng dài, dễ đi bộ và ngắm cảnh.",
        "tips_vi": "Kết hợp tham quan cùng Nhà thờ Chúa Ba Ngôi kề bên; mang áo chắn gió vì trên gò lộng gió biển.",
    },
    [
        {"title": "Wikipedia (RU) — Анадырь", "url": "https://ru.wikipedia.org/wiki/Анадырь"},
        {"title": "Wikipedia (EN) — Anadyr (search)", "url": "https://en.wikipedia.org/wiki/Special:Search?search=Anadyr%20Saint%20Nicholas%20monument"},
    ],
    ["chukotka", "anadyr", "monument", "orthodox", "saint-nicholas", "viewpoint"],
    maps_text("Памятник Николаю Чудотворцу", "Анадырь", "Monument to St Nicholas", "Anadyr", 64.7351, 177.5165),
))

# 3) Tượng đài nhà văn Yuri Rytkheu (Anadyr) ---------------------------------
RECORDS.append(rec(
    "anadyr-rytkheu-monument",
    "Tượng đài nhà văn Yuri Rytkheu (Pamyatnik Yuriyu Rytkheu)",
    "Памятник Юрию Рытхэу",
    "Monument to Yuri Rytkheu (Anadyr)",
    ["monument"],
    64.7322, 177.5075,
    "Khu trung tâm ven vịnh, thành phố Anadyr, Khu tự trị Chukotka, Nga.",
    "Tượng đài tưởng niệm Yuri Rytkheu (1930–2008) – nhà văn Chukchi lừng danh, người đưa cuộc sống, huyền thoại và tâm hồn của dân tộc mình vào văn học thế giới. Ông sinh ra ở làng Uelen bên bờ eo biển Bering.",
    "Ở trung tâm Anadyr có tượng đài dành cho Yuri Rytkheu – nhà văn nổi tiếng nhất mà vùng Chukotka từng sinh ra. Sinh năm 1930 trong một gia đình thợ săn ở làng Uelen cực đông, Rytkheu viết bằng cả tiếng Chukchi và tiếng Nga, và qua hàng loạt tiểu thuyết, truyện ngắn ông đã kể cho thế giới nghe về đời sống, tín ngưỡng, huyền thoại và những biến động của người Chukchi giữa thế kỷ 20. Tác phẩm của ông được dịch ra nhiều thứ tiếng, giúp một dân tộc nhỏ nơi tận cùng Á – Âu có tiếng nói trong văn chương toàn cầu. Tượng đài ở Anadyr là nơi người dân và du khách bày tỏ lòng trân trọng với “người kể chuyện của vùng đài nguyên”, đồng thời là dịp để hiểu thêm về văn hoá bản địa Chukotka qua lăng kính văn học.",
    [
        "Tưởng niệm Yuri Rytkheu – nhà văn Chukchi được dịch ra nhiều thứ tiếng.",
        "Gợi nhắc di sản văn học và văn hoá của các dân tộc bản địa Chukotka.",
        "Nằm ở khu trung tâm Anadyr, dễ kết hợp dạo phố ven vịnh.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–20 phút.",
        "best_time_vi": "Mùa hè, khi dạo bộ trong thành phố dễ chịu.",
        "tips_vi": "Đọc trước một tác phẩm của Rytkheu (ví dụ “Khi cá voi ra đi”) sẽ khiến chuyến thăm ý nghĩa hơn.",
    },
    [
        {"title": "Wikipedia (EN) — Yuri Rytkheu", "url": "https://en.wikipedia.org/wiki/Yuri_Rytkheu"},
        {"title": "Wikipedia (RU) — Рытхэу, Юрий Сергеевич", "url": "https://ru.wikipedia.org/wiki/Рытхэу,_Юрий_Сергеевич"},
    ],
    ["chukotka", "anadyr", "monument", "literature", "chukchi", "rytkheu"],
    maps_text("Памятник Юрию Рытхэу", "Анадырь", "Monument to Yuri Rytkheu", "Anadyr", 64.7322, 177.5075),
))

# 4) Đài kỷ niệm Ban Cách mạng đầu tiên Chukotka (Anadyr) --------------------
RECORDS.append(rec(
    "anadyr-first-revkom-monument",
    "Đài kỷ niệm Ban Cách mạng đầu tiên Chukotka (Pamyatnik Pervomu revkomu Chukotki)",
    "Памятник Первому ревкому Чукотки",
    "Monument to the First Revolutionary Committee of Chukotka (Anadyr)",
    ["monument"],
    64.7345, 177.5085,
    "Khu trung tâm ven vịnh, thành phố Anadyr, Khu tự trị Chukotka, Nga.",
    "Đài tưởng niệm những thành viên Ban Cách mạng (revkom) đầu tiên của Chukotka bị sát hại năm 1920. Đây là một trong những tượng đài lịch sử lâu đời và mang tính biểu tượng của Anadyr thời Xô-viết.",
    "Giữa trung tâm Anadyr là đài kỷ niệm dành cho Ban Cách mạng đầu tiên của Chukotka – nhóm những người thành lập chính quyền Xô-viết non trẻ ở vùng cực đông năm 1919–1920, do Mikhail Mandrikov đứng đầu, và bị bắn chết trong cuộc phản loạn đầu năm 1920. Công trình là một trong những đài tưởng niệm lâu đời của thành phố, gắn với giai đoạn lịch sử đầy biến động khi Chukotka bước vào thời kỳ hiện đại. Với người dân địa phương, đây là một địa chỉ đỏ quen thuộc, nơi diễn ra các nghi lễ tưởng niệm; với du khách, đó là dịp tìm hiểu lịch sử thế kỷ 20 của vùng đất xa xôi này. Đài nằm ở khu vực dễ tiếp cận trong thành phố, có thể ghé qua khi dạo bộ giữa các điểm tham quan của Anadyr.",
    [
        "Tưởng niệm nhóm cách mạng đầu tiên của Chukotka bị sát hại năm 1920.",
        "Một trong những tượng đài lịch sử lâu đời của Anadyr.",
        "Gắn với trang sử thế kỷ 20 của miền cực đông nước Nga.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–15 phút.",
        "best_time_vi": "Quanh năm; mùa hè thuận tiện đi bộ.",
        "tips_vi": "Dễ kết hợp trong lịch dạo phố Anadyr cùng bảo tàng và các tượng đài khác.",
    },
    [
        {"title": "Wikipedia (RU) — Первый ревком Чукотки", "url": "https://ru.wikipedia.org/wiki/Первый_ревком_Чукотки"},
        {"title": "Wikipedia (RU) — Анадырь", "url": "https://ru.wikipedia.org/wiki/Анадырь"},
    ],
    ["chukotka", "anadyr", "monument", "history", "soviet", "memorial"],
    maps_text("Памятник Первому ревкому Чукотки", "Анадырь", "First Revkom Monument", "Anadyr", 64.7345, 177.5085),
))

# 5) Tranh tường/muralы phố Anadyr -------------------------------------------
RECORDS.append(rec(
    "anadyr-murals",
    "Tranh tường phố phường Anadyr (Muraly / graffiti Anadyrya)",
    "Муралы и граффити Анадыря",
    "Anadyr Street Murals",
    ["other"],
    64.7337, 177.5140,
    "Trên các mặt tường chung cư khắp thành phố Anadyr, Khu tự trị Chukotka, Nga.",
    "Anadyr được mệnh danh là một trong những thành phố “sặc sỡ” nhất nước Nga: những khối chung cư bê tông thời Xô-viết được sơn màu rực rỡ và phủ tranh tường khổng lồ – gấu Bắc Cực, cá voi, người Chukchi, cảnh đài nguyên – để xua đi cái ảm đạm của mùa cực đêm.",
    "Giữa một vùng đất quanh năm tuyết trắng, xám xịt và nhiều tháng chìm trong bóng tối cực đêm, Anadyr chọn cách “phản công” bằng màu sắc. Các dãy chung cư bê tông kiểu Liên Xô được sơn phủ những gam màu tươi và trang trí bằng hàng loạt bức tranh tường (mural) cỡ lớn: gấu trắng, cá voi, hải mã, chân dung người bản địa, cảnh săn bắt và huyền thoại Chukchi, những dòng chữ cổ vũ tinh thần. Nhờ vậy, thủ phủ Chukotka thường được nhắc tới như một trong những thành phố nhiều màu sắc và “vui mắt” nhất nước Nga, dù nằm ở nơi khắc nghiệt bậc nhất. Với du khách, dạo bộ giữa các khu nhà để “săn” tranh tường là một cách thú vị và miễn phí để cảm nhận tinh thần lạc quan cùng bản sắc văn hoá của người dân nơi đây.",
    [
        "Anadyr nổi tiếng là một trong những thành phố nhiều màu sắc nhất nước Nga.",
        "Tranh tường chủ đề Bắc Cực và văn hoá Chukchi phủ khắp các khối chung cư.",
        "Điểm dạo bộ, chụp ảnh miễn phí và độc đáo ngay trong thành phố.",
    ],
    {
        "hours_vi": "Ngoài trời, tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 1 giờ dạo bộ ngắm tranh.",
        "best_time_vi": "Mùa hè có ánh sáng ban ngày dài, màu tranh lên rực rỡ nhất.",
        "tips_vi": "Kết hợp lộ trình đi bộ giữa bảo tàng, nhà thờ và tượng đài để ngắm nhiều bức tranh nhất.",
    },
    [
        {"title": "Wikipedia (RU) — Анадырь", "url": "https://ru.wikipedia.org/wiki/Анадырь"},
        {"title": "Wikipedia (EN) — Anadyr (town)", "url": "https://en.wikipedia.org/wiki/Anadyr_(town)"},
    ],
    ["chukotka", "anadyr", "street-art", "murals", "city-walk"],
    maps_text("Анадырь", "Чукотка", "Anadyr", "Chukotka", 64.7337, 177.5140),
))

# 6) Cửa vịnh Anadyr – ngắm cá voi trắng beluga ------------------------------
RECORDS.append(rec(
    "anadyr-estuary-beluga",
    "Cửa vịnh Anadyr – nơi ngắm cá voi trắng beluga (Anadyrsky liman)",
    "Анадырский лиман",
    "Anadyr Estuary (Anadyrsky Liman)",
    ["other"],
    64.7180, 177.4700,
    "Cửa sông – vụng nước lợ nơi các sông Anadyr, Kanchalan, Velikaya đổ ra vịnh Anadyr, cạnh thành phố Anadyr, Chukotka, Nga.",
    "Vùng cửa sông rộng lớn ôm lấy thành phố Anadyr, nơi mùa hè đàn cá voi trắng beluga và cả cá voi xám kéo vào săn cá hồi ngay trước mặt thành phố – một cảnh tượng thiên nhiên hiếm có ngay cạnh khu dân cư.",
    "Anadyr nằm bên bờ một cửa sông – vụng nước lợ mênh mông (liman), nơi ba con sông Anadyr, Kanchalan và Velikaya cùng đổ nước ra vịnh Anadyr thuộc biển Bering. Vào mùa hè, khi từng đàn cá hồi ngược dòng, vùng nước này trở thành “bàn tiệc” thu hút cá voi trắng beluga bơi thành đàn ngay sát thành phố; đôi khi cả cá voi xám cũng xuất hiện. Từ bờ kè hoặc trên chuyến phà/tàu nhỏ nối thành phố với sân bay Ugolny bên kia cửa vịnh, du khách có thể bắt gặp những tấm lưng trắng nhấp nhô – một trong những trải nghiệm ngắm cá voi dễ tiếp cận nhất Bắc Cực Nga. Cửa vịnh cũng là nơi trú ngụ của hải cẩu và vô số loài chim biển, đồng thời đóng khung nên khung cảnh đặc trưng của Anadyr với mặt nước rộng, con tàu và những dãy nhà nhiều màu.",
    [
        "Cá voi trắng beluga (và đôi khi cá voi xám) kéo vào săn cá hồi ngay cạnh thành phố mỗi mùa hè.",
        "Một trong những nơi ngắm cá voi dễ tiếp cận nhất ở Bắc Cực Nga.",
        "Cảnh quan cửa vịnh đặc trưng: mặt nước rộng, phà, chim biển và hải cẩu.",
    ],
    {
        "hours_vi": "Tự do; ngắm cá voi phụ thuộc mùa và thuỷ triều.",
        "ticket_vi": "Miễn phí từ bờ; tour thuyền/phà tính phí riêng.",
        "duration_vi": "Từ 30 phút ngắm cảnh đến vài giờ nếu đi thuyền.",
        "best_time_vi": "Giữa hè (tháng 7–8) khi cá hồi về và cá voi vào cửa vịnh.",
        "tips_vi": "Mang ống nhòm; hỏi người địa phương về thời điểm cá voi hay xuất hiện trong ngày.",
    },
    [
        {"title": "Wikipedia (EN) — Gulf of Anadyr", "url": "https://en.wikipedia.org/wiki/Gulf_of_Anadyr"},
        {"title": "Wikipedia (RU) — Анадырский лиман", "url": "https://ru.wikipedia.org/wiki/Анадырский_лиман"},
    ],
    ["chukotka", "anadyr", "nature", "beluga", "whale-watching", "estuary"],
    maps_text("Анадырский лиман", "Анадырь", "Anadyr Estuary", "Anadyr", 64.7180, 177.4700),
))

# 7) Hồ thiên thạch Elgygytgyn -----------------------------------------------
RECORDS.append(rec(
    "lake-elgygytgyn",
    "Hồ Elgygytgyn – hồ miệng thiên thạch (Ozero Elgygytgyn)",
    "Озеро Эльгыгытгын",
    "Lake Elgygytgyn",
    ["other"],
    67.5000, 172.0900,
    "Vùng cao nguyên trung tâm Chukotka, huyện Anadyrsky (xa các khu dân cư), Khu tự trị Chukotka, Nga.",
    "Một hồ nước tròn gần như hoàn hảo nằm trong lòng chảo miệng va chạm thiên thạch khoảng 3,6 triệu năm tuổi. Lớp trầm tích đáy hồ chưa từng bị băng hà xáo trộn, trở thành “cuốn nhật ký” khí hậu quý giá bậc nhất Bắc Cực.",
    "Ẩn giữa cao nguyên hoang vắng ở trung tâm Chukotka, hồ Elgygytgyn có hình gần tròn với đường kính khoảng 12 km, hình thành khi một thiên thạch lao xuống Trái Đất chừng 3,6 triệu năm trước (kỷ Pliocene). Điều khiến giới khoa học say mê là suốt hàng triệu năm ấy, lòng chảo này chưa bao giờ bị các dòng sông băng lục địa cày xới, nên lớp trầm tích dưới đáy sâu (hơn 170 m nước) lưu giữ liên tục dấu vết biến đổi khí hậu của cả vùng Bắc Cực – một kho tư liệu cổ khí hậu hiếm có mà nhiều đoàn khoan quốc tế đã tìm đến. Cái tên trong tiếng Chukchi mang nghĩa “hồ trắng” (nước lạnh trong veo). Hồ và vùng quanh nó nằm trong khu bảo tồn, là môi trường sống của loài cá hồi than vây dài đặc hữu và điểm dừng của tuần lộc, chim di cư. Đây là điểm đến cực kỳ xa xôi, chỉ tiếp cận được bằng trực thăng hoặc chuyến đi hoang dã có tổ chức.",
    [
        "Hồ nằm trong miệng va chạm thiên thạch ~3,6 triệu năm tuổi, hình gần tròn hoàn hảo.",
        "Trầm tích đáy hồ là kho lưu trữ cổ khí hậu Bắc Cực quý giá cho khoa học.",
        "Sinh cảnh của cá hồi than vây dài đặc hữu, cực kỳ hoang sơ và biệt lập.",
    ],
    {
        "hours_vi": "Vùng hoang dã, không có cơ sở dịch vụ; tiếp cận theo đoàn.",
        "ticket_vi": "Không bán vé; cần tự tổ chức/thuê dịch vụ chuyên biệt (rất tốn kém).",
        "duration_vi": "Chuyến đi nhiều ngày (thường bằng trực thăng).",
        "best_time_vi": "Mùa hè ngắn ngủi (tháng 7–8) khi băng tan và thời tiết tương đối ổn.",
        "tips_vi": "Chỉ đi cùng đơn vị chuyên nghiệp; cần giấy phép, thiết bị và kế hoạch hậu cần cho vùng cực xa.",
    },
    [
        {"title": "Wikipedia (EN) — Lake Elgygytgyn", "url": "https://en.wikipedia.org/wiki/Lake_Elgygytgyn"},
        {"title": "Wikipedia (RU) — Эльгыгытгын", "url": "https://ru.wikipedia.org/wiki/Эльгыгытгын"},
    ],
    ["chukotka", "nature", "impact-crater", "lake", "science", "remote"],
    maps_text("Озеро Эльгыгытгын", "Чукотка", "Lake Elgygytgyn", "Chukotka", 67.5000, 172.0900),
))

# 8) Vườn quốc gia Beringia --------------------------------------------------
RECORDS.append(rec(
    "beringia-national-park",
    "Vườn quốc gia Beringia (Natsionalny park Beringiya)",
    "Национальный парк «Берингия»",
    "Beringia National Park",
    ["park_garden"],
    64.4229, -173.2264,
    "Trải rộng trên bán đảo Chukchi phía đông Chukotka (huyện Providensky và Chukotsky); trụ sở đặt tại thị trấn Provideniya, Nga.",
    "Vườn quốc gia lớn nằm ở nơi tận cùng phía đông nước Nga, nhìn sang Alaska – bảo tồn đài nguyên Beringia, các di chỉ Eskimo cổ, đàn hải mã, cá voi và cả “Hẻm Xương Cá voi” huyền thoại. Đây là phần Nga của di sản chung Beringia hai bên eo biển Bering.",
    "Được thành lập năm 2013, Vườn quốc gia Beringia bảo vệ một vùng rộng lớn trên bán đảo Chukchi – dải đất từng là cầu nối lục địa Beringia nối châu Á với châu Mỹ trong kỷ Băng hà. Công viên gồm nhiều cụm bảo tồn ôm lấy các vịnh và mũi đất hướng ra biển Bering và eo biển Bering, che chở cho đài nguyên vùng cực, các đàn hải mã trên bãi đá, cá voi xám và cá voi đầu cong, cùng vô số chim biển. Nhưng Beringia còn là một công viên “văn hoá”: trong ranh giới của nó có những di chỉ khảo cổ và làng Eskimo/Yupik cổ, có “Hẻm Xương Cá voi” trên đảo Yttygran, có làng bỏ hoang Naukan gần mũi Dezhnev. Vườn quốc gia được xem là phần Nga của “di sản chung Beringia”, kết nối về ý tưởng với Khu bảo tồn Cầu Đất Bering (Bering Land Bridge) bên phía Alaska, Hoa Kỳ. Đây là điểm đến cho du khách ưa mạo hiểm, thường tiếp cận từ Provideniya bằng thuyền hoặc tour chuyên biệt.",
    [
        "Bảo tồn đài nguyên Beringia – “cầu đất” cổ nối châu Á với châu Mỹ.",
        "Bao gồm di chỉ Eskimo cổ, Hẻm Xương Cá voi (Yttygran) và làng bỏ hoang Naukan.",
        "Phần Nga của di sản chung Beringia, gắn với Khu bảo tồn bên phía Alaska.",
    ],
    {
        "hours_vi": "Vùng bảo tồn hoang dã; tham quan theo tour và cần giấy phép vào công viên.",
        "ticket_vi": "Có phí vào công viên và thủ tục đăng ký; liên hệ ban quản lý ở Provideniya.",
        "duration_vi": "Thường là các tour nhiều ngày bằng thuyền.",
        "best_time_vi": "Mùa hè (tháng 7–9) khi biển bớt băng, thuận tiện đi thuyền.",
        "tips_vi": "Đăng ký trước với ban quản lý; nhiều khu thuộc vùng biên giới nên cần giấy phép đặc biệt.",
    },
    [
        {"title": "Wikipedia (EN) — Beringia National Park", "url": "https://en.wikipedia.org/wiki/Beringia_(national_park)"},
        {"title": "Wikipedia (RU) — Берингия (национальный парк)", "url": "https://ru.wikipedia.org/wiki/Берингия_(национальный_парк)"},
    ],
    ["chukotka", "national-park", "beringia", "tundra", "walrus", "unesco-tentative"],
    maps_text("Национальный парк Берингия", "Провидения", "Beringia National Park", "Provideniya", 64.4229, -173.2264),
))

# 9) Đảo Kolyuchin – trạm cực bỏ hoang & gấu Bắc Cực -------------------------
RECORDS.append(rec(
    "kolyuchin-island",
    "Đảo Kolyuchin – trạm cực bỏ hoang & gấu Bắc Cực (Ostrov Kolyuchin)",
    "Остров Колючин",
    "Kolyuchin Island",
    ["other"],
    67.4667, -174.6167,
    "Đảo nhỏ ngoài khơi bờ bắc Chukotka, biển Chukchi, gần vịnh Kolyuchinskaya, Nga.",
    "Hòn đảo đá nhỏ giữa biển Chukchi với trạm nghiên cứu cực bị bỏ hoang – nơi từng gây chấn động khi những chú gấu Bắc Cực chiếm ngụ các toà nhà đổ nát, tạo nên loạt ảnh nổi tiếng thế giới. Đảo còn là “chung cư” của hàng vạn chim biển.",
    "Đảo Kolyuchin là một mỏm đá nhỏ nhô lên giữa biển Chukchi, ngoài khơi bờ bắc Chukotka. Trên đảo từng có một trạm khí tượng – nghiên cứu địa cực hoạt động thời Xô-viết, nay đã bị bỏ hoang, chỉ còn lại những ngôi nhà gỗ mục nát và thiết bị han gỉ. Đảo bất ngờ nổi tiếng khắp thế giới vào năm 2021, khi một nhiếp ảnh gia ghi lại cảnh những con gấu Bắc Cực thong dong “dọn vào ở” trong các ô cửa sổ và căn phòng đổ nát của trạm cũ – bộ ảnh giành nhiều giải thưởng và trở thành biểu tượng cho sự giao thoa kỳ lạ giữa thiên nhiên hoang dã và tàn tích của con người ở Bắc Cực. Vách đá của đảo còn là nơi làm tổ của hàng chục nghìn con chim biển (chim anca, chim uống nước, hải âu cổ rụt…), biến Kolyuchin thành một điểm quan sát động vật hoang dã ấn tượng cho các tour thám hiểm bằng thuyền dọc bờ biển Chukchi.",
    [
        "Trạm nghiên cứu địa cực bỏ hoang – bối cảnh loạt ảnh gấu Bắc Cực nổi tiếng năm 2021.",
        "Vách đá là nơi làm tổ của hàng chục nghìn chim biển.",
        "Điểm quan sát động vật hoang dã trên các tour thuyền dọc biển Chukchi.",
    ],
    {
        "hours_vi": "Đảo hoang; chỉ ghé qua trên tour thuyền/du thuyền thám hiểm.",
        "ticket_vi": "Không bán vé; chi phí nằm trong tour.",
        "duration_vi": "Thường là điểm dừng vài giờ trong hành trình dài ngày.",
        "best_time_vi": "Cuối hè (tháng 8–9) khi biển ít băng và động vật hoạt động.",
        "tips_vi": "Không lên bờ khi có gấu; luôn giữ khoảng cách an toàn và tuân theo hướng dẫn viên.",
    },
    [
        {"title": "Wikipedia (EN) — Kolyuchin", "url": "https://en.wikipedia.org/wiki/Kolyuchin"},
        {"title": "Wikipedia (RU) — Колючин", "url": "https://ru.wikipedia.org/wiki/Колючин_(остров)"},
    ],
    ["chukotka", "island", "polar-bear", "abandoned", "birds", "chukchi-sea"],
    maps_text("Остров Колючин", "Чукотка", "Kolyuchin Island", "Chukotka", 67.4667, -174.6167),
))

# 10) Làng Yupik bỏ hoang Naukan ---------------------------------------------
RECORDS.append(rec(
    "naukan-abandoned-village",
    "Naukan – làng Eskimo bỏ hoang gần mũi Dezhnev (Naukan)",
    "Наукан",
    "Naukan (abandoned Yupik village)",
    ["other"],
    66.0272, -169.7078,
    "Trên sườn mũi Dezhnev, bán đảo Chukchi, huyện Chukotsky, Khu tự trị Chukotka, Nga.",
    "Ngôi làng Eskimo (Yupik Naukan) từng là khu định cư ở cực đông nhất lục địa Á – Âu, có người ở suốt gần 2.000 năm trước khi bị di dời năm 1958. Nay chỉ còn nền nhà đá và xương cá voi, lặng lẽ nhìn sang Alaska bên kia eo biển Bering.",
    "Bám vào sườn dốc của mũi Dezhnev – điểm cực đông của lục địa Á – Âu – Naukan từng là ngôi làng của người Eskimo Naukan (một nhánh Yupik), có người sinh sống liên tục gần hai thiên niên kỷ. Ở vị trí đắc địa nhìn thẳng ra eo biển Bering và hai đảo Diomede, dân làng sống bằng nghề săn cá voi, hải mã và hải cẩu, phát triển một thứ tiếng Yupik riêng biệt. Năm 1958, chính quyền Xô-viết buộc dân Naukan phải rời đi và phân tán về các làng khác, khép lại lịch sử của một trong những cộng đồng cổ xưa nhất Bắc Cực. Ngày nay Naukan là một di chỉ hoang phế đầy ám ảnh: những vòng nền nhà bán âm bằng đá, hàm xương cá voi, khung nhà mục và các bậc đá rêu phong nằm rải trên sườn núi. Là một phần của Vườn quốc gia Beringia, nơi này thường được ghép cùng chuyến thăm mũi Dezhnev, cho du khách cảm nhận sâu sắc về đời sống bản địa và sự khắc nghiệt của vùng cực.",
    [
        "Từng là khu định cư ở cực đông nhất lục địa Á – Âu, có người ở gần 2.000 năm.",
        "Bị di dời năm 1958; nay là di chỉ hoang phế với nền nhà đá và xương cá voi.",
        "Nằm trên mũi Dezhnev, nhìn sang Alaska; thuộc Vườn quốc gia Beringia.",
    ],
    {
        "hours_vi": "Di chỉ ngoài trời hoang vắng; tiếp cận theo tour cùng mũi Dezhnev.",
        "ticket_vi": "Không bán vé; chi phí và giấy phép vùng biên nằm trong tour.",
        "duration_vi": "Khoảng 1–2 giờ tham quan di chỉ.",
        "best_time_vi": "Mùa hè (tháng 7–8) khi biển đi lại được và sương mù ít.",
        "tips_vi": "Cần giấy phép vùng biên giới; giữ nguyên hiện trạng di chỉ, không lấy hiện vật.",
    },
    [
        {"title": "Wikipedia (EN) — Naukan", "url": "https://en.wikipedia.org/wiki/Naukan"},
        {"title": "Wikipedia (RU) — Наукан", "url": "https://ru.wikipedia.org/wiki/Наукан"},
    ],
    ["chukotka", "eskimo", "yupik", "abandoned", "archaeology", "beringia"],
    maps_text("Наукан", "Чукотка", "Naukan", "Chukotka", 66.0272, -169.7078),
))

# 11) Uelen – làng cực đông & xưởng chạm ngà ---------------------------------
RECORDS.append(rec(
    "uelen-ivory-carving",
    "Uelen – làng cực đông & xưởng chạm ngà (Uelen)",
    "Уэлен",
    "Uelen (easternmost village & bone-carving workshop)",
    ["other", "museum"],
    66.1594, -169.8092,
    "Trên dải cát hẹp giữa đầm phá và biển Chukchi, gần mũi Dezhnev, huyện Chukotsky, Chukotka, Nga.",
    "Ngôi làng có người ở nằm ở cực đông nhất nước Nga và cả lục địa Á – Âu, quê hương của xưởng chạm ngà – xương lừng danh và của nhà văn Yuri Rytkheu. Một điểm đến biểu tượng cho nghệ thuật và văn hoá bản địa Chukotka.",
    "Uelen nằm trên một dải cát hẹp kẹp giữa đầm phá và biển Chukchi, ngay gần mũi Dezhnev – khiến nơi đây là khu dân cư ở cực đông nhất của cả nước Nga lẫn lục địa Á – Âu, chỉ cách đường đổi ngày và Alaska một tầm nhìn. Làng nổi tiếng khắp thế giới nhờ Xưởng Chạm khắc Xương Uelen, thành lập năm 1931, nơi các nghệ nhân Chukchi và Eskimo tiếp nối truyền thống chạm ngà hải mã, xương cá voi và khắc tranh trên ngà (kỹ thuật khắc – tô màu độc đáo). Những tác phẩm tinh xảo kể lại cảnh săn bắt, huyền thoại và đời sống đài nguyên; xưởng có phòng trưng bày như một bảo tàng nhỏ, được xem là cái nôi của nghệ thuật tạo hình bản địa vùng cực đông. Uelen cũng là nơi sinh của nhà văn Yuri Rytkheu. Với du khách, ghé Uelen là dịp hiếm hoi để tận mắt thấy nghề thủ công cổ truyền vẫn sống động nơi tận cùng nước Nga.",
    [
        "Khu dân cư ở cực đông nhất nước Nga và lục địa Á – Âu.",
        "Xưởng chạm khắc xương Uelen (1931) – cái nôi nghệ thuật chạm ngà Chukchi/Eskimo.",
        "Quê hương nhà văn Yuri Rytkheu; có phòng trưng bày như bảo tàng nhỏ.",
    ],
    {
        "hours_vi": "Xưởng/phòng trưng bày mở theo giờ làm việc; nên báo trước qua tour.",
        "ticket_vi": "Có thể mua tác phẩm tại chỗ; tham quan thường trong khuôn khổ tour.",
        "duration_vi": "Khoảng 1–2 giờ ở làng và xưởng.",
        "best_time_vi": "Mùa hè (tháng 7–8) khi có thể tiếp cận bằng thuyền/trực thăng.",
        "tips_vi": "Cần giấy phép vùng biên; mua đồ chạm ngà cần lưu ý quy định xuất khẩu sản phẩm từ ngà.",
    },
    [
        {"title": "Wikipedia (EN) — Uelen", "url": "https://en.wikipedia.org/wiki/Uelen"},
        {"title": "Wikipedia (RU) — Уэлен", "url": "https://ru.wikipedia.org/wiki/Уэлен"},
    ],
    ["chukotka", "uelen", "ivory-carving", "chukchi", "easternmost", "craft"],
    maps_text("Уэлен", "Чукотка", "Uelen", "Chukotka", 66.1594, -169.8092),
))

# 12) Lorino – làng săn cá voi truyền thống ----------------------------------
RECORDS.append(rec(
    "lorino-whaling-village",
    "Lorino – làng săn cá voi truyền thống (Lorino)",
    "Лорино",
    "Lorino",
    ["other"],
    65.5042, -171.7042,
    "Bên vịnh Mechigmen, huyện Chukotsky, Khu tự trị Chukotka, Nga.",
    "Làng ven biển đông dân người Chukchi nhất Chukotka, nơi vẫn duy trì nghề săn cá voi và hải mã truyền thống của thợ săn thú biển bản địa. Gần làng có những suối nước nóng phun giữa đài nguyên lạnh giá.",
    "Nằm bên vịnh Mechigmen nhìn ra biển Bering, Lorino là ngôi làng ven biển có đông người Chukchi sinh sống bậc nhất vùng. Đời sống nơi đây gắn chặt với biển: cộng đồng thợ săn thú biển bản địa vẫn được phép duy trì nghề săn cá voi xám và hải mã theo hạn ngạch truyền thống, một tập tục hàng nghìn năm nay đóng vai trò sống còn cả về lương thực lẫn văn hoá. Du khách đến Lorino có thể tìm hiểu cách người dân xẻ thịt, chia phần và bảo quản chiến lợi phẩm theo tập quán, xem những chiếc thuyền da hải mã và nghe các câu chuyện săn bắt. Cách làng không xa là những suối nước nóng tự nhiên (nguồn nóng Lorino) phun lên giữa đài nguyên – nơi người dân và du khách ngâm mình thư giãn giữa khung cảnh hoang vu. Lorino cho thấy một Chukotka “sống”, nơi truyền thống bản địa vẫn tiếp diễn trong đời sống thường nhật.",
    [
        "Một trong những làng người Chukchi đông dân nhất, giữ nghề săn thú biển truyền thống.",
        "Cơ hội tìm hiểu văn hoá săn cá voi – hải mã của người bản địa Bắc Cực.",
        "Gần làng có suối nước nóng tự nhiên để ngâm mình giữa đài nguyên.",
    ],
    {
        "hours_vi": "Làng dân cư; tham quan nên đi cùng hướng dẫn viên địa phương.",
        "ticket_vi": "Không có vé; chi phí theo tour và dịch vụ tại chỗ.",
        "duration_vi": "Nửa ngày đến một ngày (kể cả suối nước nóng).",
        "best_time_vi": "Mùa hè – thu, mùa săn thú biển và biển đi lại thuận tiện.",
        "tips_vi": "Tôn trọng tập quán bản địa; xin phép trước khi chụp ảnh cảnh săn bắt và người dân.",
    },
    [
        {"title": "Wikipedia (EN) — Lorino", "url": "https://en.wikipedia.org/wiki/Lorino,_Chukotka_Autonomous_Okrug"},
        {"title": "Wikipedia (RU) — Лорино", "url": "https://ru.wikipedia.org/wiki/Лорино"},
    ],
    ["chukotka", "chukchi", "whaling", "indigenous", "hot-springs", "mechigmen"],
    maps_text("Лорино", "Чукотка", "Lorino", "Chukotka", 65.5042, -171.7042),
))

# 13) Sireniki – làng cổ Bắc Cực ---------------------------------------------
RECORDS.append(rec(
    "sireniki-ancient-village",
    "Sireniki – làng cổ bên biển Bering (Sireniki)",
    "Сиреники",
    "Sireniki",
    ["other"],
    64.4167, -173.9500,
    "Trên bờ biển Bering, huyện Providensky, Khu tự trị Chukotka, Nga.",
    "Một trong những khu định cư có người ở liên tục lâu đời nhất Bắc Cực – khoảng 2.500 đến 3.000 năm. Làng ven biển của người Yupik và Chukchi này còn gắn với thứ tiếng Eskimo Sirenik nay đã thất truyền.",
    "Sireniki nằm nép bên bờ biển Bering, dưới chân những vách đá và đồi đài nguyên, và được xem là một trong những nơi có người ở liên tục lâu đời nhất vùng Bắc Cực – các di chỉ khảo cổ cho thấy con người đã sinh sống ở đây khoảng 2.500–3.000 năm. Cộng đồng làng gồm người Yupik và Chukchi, sống nhờ săn hải mã, hải cẩu và cá voi. Sireniki đặc biệt nổi tiếng trong giới ngôn ngữ học vì từng là quê hương của tiếng Eskimo Sirenik – một ngôn ngữ khác biệt tới mức được coi là nhánh riêng, nay đã tuyệt tích khi người nói cuối cùng qua đời. Với du khách ưa khám phá, làng mang đến cái nhìn về một cộng đồng bản địa bền bỉ bám trụ nơi biển và băng, giữa cảnh quan bờ biển hoang sơ với đá, sóng và những đàn chim, hải mã. Sireniki thường được ghé thăm trong các hành trình dọc bờ nam bán đảo Chukchi.",
    [
        "Một trong những khu định cư có người ở liên tục lâu đời nhất Bắc Cực (~2.500–3.000 năm).",
        "Làng của người Yupik và Chukchi, sống bằng nghề săn thú biển.",
        "Quê hương của tiếng Eskimo Sirenik đặc biệt, nay đã thất truyền.",
    ],
    {
        "hours_vi": "Làng dân cư ven biển; tham quan theo tour dọc bờ nam Chukchi.",
        "ticket_vi": "Không có vé; chi phí theo tour.",
        "duration_vi": "Khoảng 1–2 giờ trong hành trình dài hơn.",
        "best_time_vi": "Mùa hè (tháng 7–9) khi biển thông thoáng.",
        "tips_vi": "Cần giấy phép vùng biên; tôn trọng cộng đồng và di chỉ khảo cổ.",
    },
    [
        {"title": "Wikipedia (EN) — Sireniki", "url": "https://en.wikipedia.org/wiki/Sireniki"},
        {"title": "Wikipedia (RU) — Сиреники", "url": "https://ru.wikipedia.org/wiki/Сиреники"},
    ],
    ["chukotka", "eskimo", "yupik", "ancient-settlement", "bering-sea", "language"],
    maps_text("Сиреники", "Чукотка", "Sireniki", "Chukotka", 64.4167, -173.9500),
))

# 14) Đảo Ratmanov (Diomede Lớn) – cực đông nước Nga -------------------------
RECORDS.append(rec(
    "ratmanov-big-diomede-island",
    "Đảo Ratmanov (Diomede Lớn) – điểm cực đông nước Nga (Ostrov Ratmanova)",
    "Остров Ратманова (Большой Диомид)",
    "Ratmanov Island (Big Diomede)",
    ["other"],
    65.7811, -169.0569,
    "Giữa eo biển Bering, huyện Chukotsky, Khu tự trị Chukotka, Nga (cực đông của nước Nga).",
    "Hòn đảo đá nằm chính giữa eo biển Bering là điểm cực đông của nước Nga. Chỉ cách đảo Diomede Nhỏ của Mỹ khoảng 4 km, với Đường Đổi Ngày Quốc tế chạy giữa hai đảo – nên có biệt danh “hòn đảo của ngày mai”.",
    "Đảo Ratmanov, người Eskimo gọi là Imaqliq và phương Tây gọi là Diomede Lớn, là một khối đá cao nằm giữa eo biển Bering và đánh dấu điểm cực đông của lãnh thổ Nga. Điều kỳ thú là chỉ cách đó khoảng 4 km về phía đông là đảo Diomede Nhỏ thuộc bang Alaska, Hoa Kỳ – và Đường Đổi Ngày Quốc tế chạy đúng giữa khe nước hẹp giữa hai đảo. Vì thế khi đứng ở Diomede Lớn nhìn sang Diomede Nhỏ, người ta thực sự “nhìn từ ngày mai sang ngày hôm qua”: hai đảo lệch nhau gần 21 giờ đồng hồ, khiến Ratmanov mang biệt danh “hòn đảo của ngày mai”. Đảo không có dân thường sinh sống, chỉ có một trạm biên phòng Nga; vách đá là nơi làm tổ của hàng loạt chim biển, quanh đảo có hải mã và cá voi. Đây là biểu tượng địa lý đặc biệt của Chukotka, tuy rất khó tiếp cận do nằm trong vùng biên giới nhạy cảm.",
    [
        "Điểm cực đông của nước Nga, nằm giữa eo biển Bering.",
        "Cách đảo Diomede Nhỏ (Mỹ) chỉ ~4 km, Đường Đổi Ngày chạy giữa hai đảo.",
        "“Hòn đảo của ngày mai” – lệch gần 21 giờ so với đảo láng giềng của Mỹ.",
    ],
    {
        "hours_vi": "Vùng biên giới quân sự; không mở cho tham quan tự do.",
        "ticket_vi": "Không có dịch vụ du lịch thông thường; chỉ ngắm từ xa trên tour biển (nếu được phép).",
        "duration_vi": "Tùy hành trình; thường chỉ quan sát từ tàu.",
        "best_time_vi": "Mùa hè khi biển bớt băng.",
        "tips_vi": "Khu vực biên giới rất nhạy cảm – tuyệt đối tuân thủ quy định và không tự ý tiếp cận.",
    },
    [
        {"title": "Wikipedia (EN) — Big Diomede", "url": "https://en.wikipedia.org/wiki/Big_Diomede"},
        {"title": "Wikipedia (RU) — Ратманова (остров)", "url": "https://ru.wikipedia.org/wiki/Ратманова_(остров)"},
    ],
    ["chukotka", "island", "bering-strait", "easternmost", "date-line", "border"],
    maps_text("Остров Ратманова", "Чукотка", "Big Diomede Island", "Chukotka", 65.7811, -169.0569),
))

# 15) Mũi Navarin ------------------------------------------------------------
RECORDS.append(rec(
    "cape-navarin",
    "Mũi Navarin (Mys Navarin)",
    "Мыс Наварин",
    "Cape Navarin",
    ["other"],
    62.2753, 179.0989,
    "Mỏm đất phía nam vịnh Anadyr, bờ biển Bering, huyện Anadyrsky, Chukotka, Nga.",
    "Mũi đất núi non hiểm trở nhô ra biển Bering ở rìa nam vịnh Anadyr, nổi tiếng với vách đá dựng đứng, hải đăng cô độc, đàn chim biển và những cơn bão dữ dội – một trong những mốc hàng hải khắc nghiệt của vùng Viễn Đông.",
    "Mũi Navarin là một mỏm đất núi non gồ ghề nhô ra biển Bering ở rìa phía nam vịnh Anadyr, gần như chạm tới kinh tuyến 180. Đây là một trong những điểm mốc hàng hải nổi tiếng và đáng gờm của vùng biển Viễn Đông: vách đá dốc đứng cao hàng trăm mét đổ thẳng xuống mặt nước, quanh năm hứng gió mạnh và những cơn bão dữ, khiến thuỷ thủ xưa nay đều dè chừng khi đi ngang. Trên mũi có một hải đăng đơn độc; các vách đá là nơi trú ngụ của những đàn chim biển đông đúc, còn vùng nước quanh đó thu hút hải mã, hải cẩu và cá voi. Với đặc thù hoang vu và hiểm trở, Cape Navarin chủ yếu được biết đến như một cột mốc địa lý và điểm quan sát thiên nhiên từ tàu biển, hơn là nơi du khách có thể dễ dàng đặt chân lên.",
    [
        "Mũi đất núi non hiểm trở nhô ra biển Bering, gần kinh tuyến 180.",
        "Vách đá dựng đứng, hải đăng cô độc và những đàn chim biển.",
        "Điểm mốc hàng hải khét tiếng vì gió bão dữ dội của vùng Viễn Đông.",
    ],
    {
        "hours_vi": "Vùng hoang dã ngoài khơi; chủ yếu quan sát từ tàu biển.",
        "ticket_vi": "Không có dịch vụ; nằm trong hành trình tàu/tour biển.",
        "duration_vi": "Điểm dừng quan sát trong hành trình dài.",
        "best_time_vi": "Mùa hè khi biển tương đối yên và ít băng.",
        "tips_vi": "Thời tiết đổi nhanh và biển động mạnh – theo sát lịch trình và hướng dẫn của thuyền.",
    },
    [
        {"title": "Wikipedia (EN) — Cape Navarin", "url": "https://en.wikipedia.org/wiki/Cape_Navarin"},
        {"title": "Wikidata — Cape Navarin (Q3562501)", "url": "https://www.wikidata.org/wiki/Q3562501"},
    ],
    ["chukotka", "cape", "bering-sea", "lighthouse", "seabirds", "nature"],
    maps_text("Мыс Наварин", "Чукотка", "Cape Navarin", "Chukotka", 62.2753, 179.0989),
))

# 16) Núi lửa Anyuisky -------------------------------------------------------
RECORDS.append(rec(
    "anyuysky-volcano",
    "Núi lửa Anyuisky (Anyuysky vulkan)",
    "Анюйский вулкан",
    "Anyuysky Volcano",
    ["other"],
    67.1742, 165.8356,
    "Vùng cao nguyên Anyuy, huyện Bilibinsky (tây Chukotka), Khu tự trị Chukotka, Nga.",
    "Núi lửa trẻ nhất vùng đông bắc Á – một nón xỉ đã tắt vươn lên giữa cao nguyên Anyuy, để lại dòng dung nham dài hàng chục cây số đông cứng giữa đài nguyên, dấu tích của những đợt phun trào cách nay chỉ vài thế kỷ đến vài nghìn năm.",
    "Ẩn sâu trong vùng cao nguyên Anyuy hoang vắng ở phía tây Chukotka, gần thị trấn Bilibino, núi lửa Anyuisky là một hiện tượng địa chất hiếm có: được xem là ngọn núi lửa trẻ nhất ở vùng đông bắc châu Á. Đây là một nón xỉ (cinder cone) nay đã tắt, cao vài trăm mét, phun trào tương đối gần đây theo thang thời gian địa chất – chỉ vài thế kỷ đến vài nghìn năm trước – và để lại một dòng dung nham đen chảy dài hàng chục kilomet, nay đông cứng thành dải đá bazan gồ ghề vắt ngang thung lũng và làm nghẽn dòng chảy tạo nên các hồ nhỏ. Giữa một Chukotka phần lớn là đài nguyên và núi trầm tích, cảnh quan dung nham nguyên sơ này trông như đến từ hành tinh khác. Vị trí cực kỳ hẻo lánh khiến Anyuisky chủ yếu là điểm đến của các nhà địa chất và số ít đoàn thám hiểm hoang dã, đi tới bằng trực thăng hoặc hành trình dài băng qua đài nguyên.",
    [
        "Được xem là núi lửa trẻ nhất vùng đông bắc châu Á.",
        "Dòng dung nham dài hàng chục km đông cứng giữa đài nguyên, tạo hồ chặn dòng.",
        "Cảnh quan bazan nguyên sơ, cực kỳ hẻo lánh, hấp dẫn giới địa chất và thám hiểm.",
    ],
    {
        "hours_vi": "Vùng hoang dã không dịch vụ; đi theo đoàn chuyên biệt.",
        "ticket_vi": "Không bán vé; chi phí hậu cần cao (trực thăng/đoàn thám hiểm).",
        "duration_vi": "Chuyến đi nhiều ngày.",
        "best_time_vi": "Mùa hè ngắn (tháng 7–8) khi tuyết tan và thời tiết ổn định hơn.",
        "tips_vi": "Chỉ đi cùng đơn vị chuyên nghiệp, chuẩn bị hậu cần kỹ cho vùng cực xa.",
    },
    [
        {"title": "Wikipedia (EN) — Anyuyskiy", "url": "https://en.wikipedia.org/wiki/Anyuyskiy"},
        {"title": "Wikipedia (RU) — Анюйский (вулкан)", "url": "https://ru.wikipedia.org/wiki/Анюйский_(вулкан)"},
    ],
    ["chukotka", "volcano", "lava-flow", "geology", "bilibino", "remote"],
    maps_text("Анюйский вулкан", "Чукотка", "Anyuysky Volcano", "Chukotka", 67.1742, 165.8356),
))

# 17) Lavrentiya -------------------------------------------------------------
RECORDS.append(rec(
    "lavrentiya-village",
    "Lavrentiya – cửa ngõ vùng cực đông (Lavrentiya)",
    "Лаврентия",
    "Lavrentiya",
    ["other"],
    65.5842, -170.9889,
    "Bên vịnh Lavrentiya (Zaliv Lavrentiya), trung tâm huyện Chukotsky, Khu tự trị Chukotka, Nga.",
    "Trung tâm hành chính của huyện Chukotsky bên bờ vịnh Lavrentiya, là cửa ngõ để đến mũi Dezhnev, làng Uelen và các điểm cực đông. Vịnh mang tên Thánh Lavrenti được nhà thám hiểm James Cook đặt năm 1778.",
    "Lavrentiya là trung tâm hành chính của huyện Chukotsky, nằm bên bờ vịnh cùng tên nhìn ra biển Bering. Đây là điểm trung chuyển quan trọng và là cửa ngõ để du khách tiếp cận những địa danh biểu tượng ở cực đông Chukotka: mũi Dezhnev, làng chạm ngà Uelen, làng bỏ hoang Naukan. Cái tên Lavrentiya bắt nguồn từ vịnh Thánh Lavrenti (St Lawrence Bay) mà nhà hàng hải người Anh James Cook đặt khi đi ngang đây năm 1778, đúng dịp lễ vị thánh này. Thị trấn nhỏ có sân bay địa phương, bảo tàng vùng và là nơi cư trú của cộng đồng Chukchi, Eskimo cùng cư dân đến từ khắp nước Nga. Với khách du lịch, Lavrentiya thường là chặng dừng chân hậu cần – nghỉ ngơi, chuẩn bị và làm thủ tục vùng biên – trước khi lên đường tới các điểm hoang dã lân cận.",
    [
        "Trung tâm huyện Chukotsky, cửa ngõ tới mũi Dezhnev, Uelen và Naukan.",
        "Vịnh mang tên Thánh Lavrenti do James Cook đặt năm 1778.",
        "Điểm trung chuyển hậu cần với sân bay địa phương và bảo tàng vùng.",
    ],
    {
        "hours_vi": "Thị trấn dân cư; dịch vụ theo giờ địa phương.",
        "ticket_vi": "Không có vé tham quan chung; bảo tàng vùng có thể thu phí nhỏ.",
        "duration_vi": "Thường là điểm dừng chân 1 ngày hoặc qua đêm.",
        "best_time_vi": "Mùa hè, khi giao thông tới các điểm cực đông thuận lợi.",
        "tips_vi": "Làm thủ tục giấy phép vùng biên tại đây trước khi đi Dezhnev/Uelen/Naukan.",
    },
    [
        {"title": "Wikipedia (EN) — Lavrentiya", "url": "https://en.wikipedia.org/wiki/Lavrentiya"},
        {"title": "Wikipedia (RU) — Лаврентия", "url": "https://ru.wikipedia.org/wiki/Лаврентия_(село)"},
    ],
    ["chukotka", "chukotsky", "gateway", "bering", "james-cook", "village"],
    maps_text("Лаврентия", "Чукотка", "Lavrentiya", "Chukotka", 65.5842, -170.9889),
))

# 18) Provideniya – thị trấn cảng & cửa ngõ Beringia -------------------------
RECORDS.append(rec(
    "provideniya-bay-town",
    "Provideniya – thị trấn cảng bên vịnh Provideniya (Provideniya)",
    "Провидения",
    "Provideniya",
    ["other"],
    64.4229, -173.2264,
    "Bên vịnh Provideniya (Komsomolskaya), huyện Providensky, Khu tự trị Chukotka, Nga.",
    "Thị trấn cảng nằm sâu trong một vịnh kín gió tuyệt đẹp, là cửa ngõ chính vào Vườn quốc gia Beringia và là điểm cập bến của các chuyến tàu thám hiểm Bắc Cực. Nơi đây có bảo tàng di sản Beringia và bề dày lịch sử Đường Biển Phương Bắc.",
    "Provideniya nằm nép trong một vịnh biển sâu và kín gió – được các nhà hàng hải xưa đặt tên là “Thiên Hựu” (Provideniya, nghĩa là “sự quan phòng của Chúa”) vì đây là chốn trú bão an toàn hiếm có trên tuyến đường biển gian nan. Thị trấn phát triển mạnh thời Xô-viết như một cảng quan trọng trên Đường Biển Phương Bắc và là điểm gần Alaska; ngày nay dân số đã giảm nhiều nhưng Provideniya vẫn là trung tâm hành chính huyện và cửa ngõ chính để vào Vườn quốc gia Beringia. Từ đây, các tour thuyền toả đi thăm Hẻm Xương Cá voi, đảo hải mã, làng bản Eskimo và bờ biển hoang dã. Thị trấn có bảo tàng di sản Beringia giới thiệu văn hoá bản địa và lịch sử vùng. Với các chuyến tàu du lịch thám hiểm vòng quanh Chukotka, Provideniya thường là cảng cập bến, nơi khung cảnh vịnh núi bao quanh những dãy nhà nhiều màu tạo nên một trong những bức tranh Bắc Cực đẹp và đặc trưng nhất.",
    [
        "Thị trấn cảng trong vịnh kín gió, cửa ngõ chính vào Vườn quốc gia Beringia.",
        "Cảng lịch sử trên Đường Biển Phương Bắc, gần Alaska; điểm cập bến tàu thám hiểm.",
        "Có bảo tàng di sản Beringia và khung cảnh vịnh núi rất đặc trưng.",
    ],
    {
        "hours_vi": "Thị trấn dân cư; dịch vụ và bảo tàng theo giờ địa phương.",
        "ticket_vi": "Bảo tàng thu phí nhỏ; tour thuyền đi Beringia tính phí riêng.",
        "duration_vi": "1 ngày trở lên, hoặc làm căn cứ cho các tour biển.",
        "best_time_vi": "Mùa hè (tháng 7–9) khi biển thông và tàu du lịch hoạt động.",
        "tips_vi": "Là vùng biên giới – cần giấy phép; dùng làm điểm xuất phát đi Hẻm Xương Cá voi và các đảo.",
    },
    [
        {"title": "Wikipedia (EN) — Provideniya", "url": "https://en.wikipedia.org/wiki/Provideniya"},
        {"title": "Wikipedia (RU) — Провидения (посёлок)", "url": "https://ru.wikipedia.org/wiki/Провидения_(посёлок)"},
    ],
    ["chukotka", "provideniya", "port", "beringia-gateway", "northern-sea-route", "bay"],
    maps_text("Провидения", "Чукотка", "Provideniya", "Chukotka", 64.4229, -173.2264),
))

# 19) Pevek – thành phố cực bắc nước Nga -------------------------------------
RECORDS.append(rec(
    "pevek-northernmost-city",
    "Pevek – thành phố cực bắc nước Nga (Pevek)",
    "Певек",
    "Pevek",
    ["other"],
    69.7003, 170.2833,
    "Bên vịnh Chaunskaya, biển Đông Siberia, huyện Chaunsky, Khu tự trị Chukotka, Nga.",
    "Thành phố nằm ở cực bắc nhất của nước Nga, một cảng biển trên Đường Biển Phương Bắc bên vịnh Chaunskaya. Nơi đây nổi tiếng với gió “yuzhak” dữ dội và là bến đỗ của nhà máy điện hạt nhân nổi đầu tiên thế giới.",
    "Pevek là thành phố nằm ở vĩ độ cao nhất trong tất cả các thành phố của nước Nga, bên bờ vịnh Chaunskaya thuộc biển Đông Siberia. Là một cảng quan trọng trên Đường Biển Phương Bắc, thành phố hình thành và lớn lên nhờ khai khoáng (thiếc, vàng) và vận tải biển vùng cực. Pevek nổi tiếng với “yuzhak” – những cơn gió nam đổ từ trên núi xuống với sức mạnh khủng khiếp, có thể quật ngã người và làm tê liệt cả thành phố trong nhiều ngày. Dù khắc nghiệt, Pevek lại là điểm đến của khách ưa “sưu tầm” cực điểm địa lý và tò mò về đời sống nơi tận cùng phương bắc: những dãy nhà chịu gió, bến cảng nhìn ra biển băng, và đặc biệt là nhà máy điện hạt nhân nổi “Akademik Lomonosov” neo ngay tại cảng, cung cấp điện và nhiệt cho vùng. Từ Pevek, du khách có thể tiếp cận những vùng đài nguyên và di sản khai khoáng của tây bắc Chukotka.",
    [
        "Thành phố ở cực bắc nhất của nước Nga, bên vịnh Chaunskaya.",
        "Nổi tiếng với gió “yuzhak” cực mạnh đổ từ núi xuống.",
        "Bến đỗ của nhà máy điện hạt nhân nổi đầu tiên thế giới “Akademik Lomonosov”.",
    ],
    {
        "hours_vi": "Thành phố dân cư; dịch vụ theo giờ địa phương.",
        "ticket_vi": "Không có vé tham quan chung.",
        "duration_vi": "1–2 ngày kết hợp khám phá vùng.",
        "best_time_vi": "Mùa hè (tháng 7–8); mùa đông cực kỳ khắc nghiệt và nhiều gió.",
        "tips_vi": "Theo dõi dự báo gió “yuzhak”; chuyến bay tới Pevek dễ bị hoãn vì thời tiết.",
    },
    [
        {"title": "Wikipedia (EN) — Pevek", "url": "https://en.wikipedia.org/wiki/Pevek"},
        {"title": "Wikipedia (RU) — Певек", "url": "https://ru.wikipedia.org/wiki/Певек"},
    ],
    ["chukotka", "pevek", "northernmost-city", "port", "northern-sea-route", "arctic"],
    maps_text("Певек", "Чукотка", "Pevek", "Chukotka", 69.7003, 170.2833),
))

# 20) Nhà máy điện hạt nhân nổi Akademik Lomonosov (Pevek) -------------------
RECORDS.append(rec(
    "akademik-lomonosov-fnpp",
    "Nhà máy điện hạt nhân nổi “Akademik Lomonosov” (Plavuchaya AES)",
    "Плавучая АЭС «Академик Ломоносов»",
    "Akademik Lomonosov Floating Nuclear Power Plant",
    ["other"],
    69.7003, 170.2999,
    "Neo tại cảng Pevek, vịnh Chaunskaya, huyện Chaunsky, Khu tự trị Chukotka, Nga.",
    "Nhà máy điện hạt nhân nổi đầu tiên và duy nhất trên thế giới đang vận hành, neo ngay tại cảng Pevek. Con “tàu điện” với hai lò phản ứng cung cấp điện và nhiệt cho thành phố cực bắc nước Nga, thay thế các nhà máy cũ trong vùng.",
    "Neo cố định tại cảng Pevek, “Akademik Lomonosov” là nhà máy điện hạt nhân nổi đầu tiên trên thế giới đi vào vận hành thương mại. Về bản chất, đây là một sà lan lớn không tự hành, trên đó lắp hai lò phản ứng kiểu tàu phá băng (KLT-40S) cho tổng công suất điện khoảng 70 MW cùng lượng nhiệt sưởi đáng kể. Được đóng ở nhà máy tại Saint Petersburg rồi kéo vòng qua Bắc Băng Dương tới Chukotka, nhà máy bắt đầu hoà lưới cuối năm 2019 và cấp điện – nhiệt cho Pevek cùng khu công nghiệp – khai khoáng lân cận, thay thế dần nhà máy điện hạt nhân Bilibino cũ và nhà máy nhiệt điện địa phương. Ý tưởng “nhà máy điện di động” này được thiết kế riêng cho những vùng cực xa xôi khó kéo đường dây, và Pevek trở thành nơi kiểm chứng công nghệ đó trong điều kiện Bắc Cực thực tế. Dù không phải điểm cho khách vào tham quan (là công trình hạt nhân canh phòng nghiêm ngặt), “con tàu nguyên tử” neo bên bến cảng vẫn là một biểu tượng công nghệ độc đáo có thể ngắm từ xa và là câu chuyện hấp dẫn của Pevek.",
    [
        "Nhà máy điện hạt nhân nổi đầu tiên trên thế giới đi vào vận hành.",
        "Hai lò phản ứng KLT-40S (~70 MW điện) cấp điện – nhiệt cho Pevek từ cuối 2019.",
        "Được kéo từ Saint Petersburg qua Bắc Băng Dương; thay thế các nhà máy cũ trong vùng.",
    ],
    {
        "hours_vi": "Công trình hạt nhân canh phòng nghiêm; không mở cửa tham quan bên trong.",
        "ticket_vi": "Không có; chỉ có thể ngắm/chụp từ xa ở khu vực cho phép.",
        "duration_vi": "Ngắm ngoài từ bến cảng: vài chục phút.",
        "best_time_vi": "Mùa hè khi ra bến cảng dễ chịu hơn.",
        "tips_vi": "Không chụp ảnh ở khu vực cấm; tuân thủ quy định an ninh của cảng và nhà máy.",
    },
    [
        {"title": "Wikipedia (EN) — Akademik Lomonosov", "url": "https://en.wikipedia.org/wiki/Akademik_Lomonosov"},
        {"title": "Wikipedia (RU) — Академик Ломоносов (ПАТЭС)", "url": "https://ru.wikipedia.org/wiki/Академик_Ломоносов_(плавучая_атомная_электростанция)"},
    ],
    ["chukotka", "pevek", "floating-npp", "nuclear", "technology", "arctic"],
    maps_text("Плавучая АЭС Академик Ломоносов", "Певек", "Akademik Lomonosov FNPP", "Pevek", 69.7003, 170.2999),
))

# 21) Bilibino & nhà máy điện hạt nhân Bilibino ------------------------------
RECORDS.append(rec(
    "bilibino-npp-town",
    "Bilibino – thị trấn vàng & nhà máy điện hạt nhân Bắc Cực (Bilibino)",
    "Билибино",
    "Bilibino (town & nuclear power plant)",
    ["other"],
    68.0500, 166.4500,
    "Tây Chukotka, trung tâm huyện Bilibinsky, Khu tự trị Chukotka, Nga.",
    "Thị trấn khai thác vàng ở vùng đài nguyên tây Chukotka, nơi có nhà máy điện hạt nhân Bilibino – từng là nhà máy điện hạt nhân nằm ở vị trí cực bắc nhất thế giới và là nhà máy hạt nhân đầu tiên vận hành trên nền băng vĩnh cửu Bắc Cực.",
    "Bilibino là một thị trấn nhỏ giữa đài nguyên tây Chukotka, hình thành từ thập niên 1950 nhờ các mỏ vàng của vùng thượng nguồn sông Anyuy – tên thị trấn đặt theo nhà địa chất Yuri Bilibin, người khai mở vàng vùng Kolyma – Chukotka. Điều khiến Bilibino có tên trên bản đồ công nghệ là Nhà máy điện hạt nhân Bilibino, vận hành từ năm 1974 để cấp điện và nhiệt cho các mỏ và cộng đồng biệt lập nơi đây. Trong nhiều thập niên, đây là nhà máy điện hạt nhân nằm ở vĩ độ cao nhất thế giới và là một trong những nhà máy hạt nhân đầu tiên được xây dựng, vận hành thành công trên nền băng vĩnh cửu Bắc Cực – một kỳ tích kỹ thuật thời bấy giờ. Khi đã lớn tuổi, nhà máy dần được cho ngừng hoạt động và thay thế bằng nguồn điện từ nhà máy nổi “Akademik Lomonosov” ở Pevek. Với du khách, Bilibino là cửa sổ nhìn vào lịch sử khai khoáng và năng lượng nơi vùng cực, cũng là điểm xuất phát để tới các vùng hoang dã tây Chukotka như núi lửa Anyuisky.",
    [
        "Thị trấn khai thác vàng ở đài nguyên tây Chukotka, mang tên nhà địa chất Yuri Bilibin.",
        "Nhà máy điện hạt nhân Bilibino – từng ở vị trí cực bắc nhất thế giới.",
        "Một trong những nhà máy hạt nhân đầu tiên vận hành trên nền băng vĩnh cửu.",
    ],
    {
        "hours_vi": "Thị trấn dân cư; nhà máy hạt nhân không mở cửa tham quan.",
        "ticket_vi": "Không có vé tham quan chung.",
        "duration_vi": "1 ngày, hoặc làm điểm xuất phát đi vùng hoang dã lân cận.",
        "best_time_vi": "Mùa hè (tháng 7–8).",
        "tips_vi": "Tiếp cận chủ yếu bằng máy bay; chuẩn bị cho hạ tầng và dịch vụ hạn chế.",
    },
    [
        {"title": "Wikipedia (EN) — Bilibino", "url": "https://en.wikipedia.org/wiki/Bilibino"},
        {"title": "Wikipedia (EN) — Bilibino Nuclear Power Plant", "url": "https://en.wikipedia.org/wiki/Bilibino_Nuclear_Power_Plant"},
    ],
    ["chukotka", "bilibino", "gold-mining", "nuclear", "permafrost", "history"],
    maps_text("Билибино", "Чукотка", "Bilibino", "Chukotka", 68.0500, 166.4500),
))

# 22) Suối nước nóng Chaplino (Novoye Chaplino) ------------------------------
RECORDS.append(rec(
    "chaplino-hot-springs",
    "Suối nước nóng Chaplino (Chaplinskiye goryachiye klyuchi)",
    "Чаплинские горячие ключи",
    "Chaplino Hot Springs",
    ["other"],
    64.4983, -172.8617,
    "Gần làng Novoye Chaplino, bên vịnh Tkachen, huyện Providensky, Khu tự trị Chukotka, Nga.",
    "Những dòng suối khoáng nóng bốc hơi nghi ngút giữa đài nguyên lạnh giá gần làng Novoye Chaplino – nơi người dân và du khách ngâm mình thư giãn trong làn nước ấm, ngắm cảnh biển và núi hoang sơ của bán đảo Chukchi.",
    "Không xa làng Yupik Novoye Chaplino bên vịnh Tkachen là một cụm suối nước nóng tự nhiên phun lên giữa đài nguyên – hiện tượng địa nhiệt hiếm hoi mang lại chút ấm áp giữa vùng đất quanh năm giá lạnh. Dòng nước khoáng ấm nóng được người dân địa phương dẫn vào những bồn tắm lộ thiên đơn sơ, nơi có thể ngâm mình thư giãn ngay giữa khung cảnh núi non, biển và đài nguyên bốn bề vắng lặng. Cảnh tượng làn hơi nước bốc lên trong không khí băng giá, xung quanh là tuyết hoặc thảm cỏ đài nguyên và những đàn chim, tạo nên trải nghiệm rất đặc trưng của Chukotka. Suối nước nóng Chaplino là một trong những điểm tham quan yêu thích trong các tour ngắn khởi hành từ Provideniya, thường kết hợp với thăm làng bản Eskimo và ngắm động vật hoang dã ven biển.",
    [
        "Suối khoáng nóng tự nhiên phun giữa đài nguyên gần làng Novoye Chaplino.",
        "Ngâm mình thư giãn trong bồn lộ thiên giữa khung cảnh biển – núi hoang sơ.",
        "Điểm ưa thích trong các tour ngắn khởi hành từ Provideniya.",
    ],
    {
        "hours_vi": "Ngoài trời, tự do; thường ghé theo tour từ Provideniya.",
        "ticket_vi": "Bồn tắm tự nhiên miễn phí; chi phí đi lại theo tour.",
        "duration_vi": "Khoảng 1–2 giờ ngâm và ngắm cảnh.",
        "best_time_vi": "Quanh năm; ngâm nước nóng giữa tiết trời lạnh càng thú vị.",
        "tips_vi": "Mang đồ bơi và khăn; đi cùng người địa phương để biết bồn nào an toàn, nhiệt độ phù hợp.",
    },
    [
        {"title": "Wikipedia (EN) — Novoye Chaplino", "url": "https://en.wikipedia.org/wiki/Novoye_Chaplino"},
        {"title": "Wikipedia (RU) — Новое Чаплино", "url": "https://ru.wikipedia.org/wiki/Новое_Чаплино"},
    ],
    ["chukotka", "hot-springs", "geothermal", "providensky", "tundra", "wellness"],
    maps_text("Чаплинские горячие ключи", "Новое Чаплино", "Chaplino Hot Springs", "Novoye Chaplino", 64.4983, -172.8617),
))

# 23) Mũi Chaplina -----------------------------------------------------------
RECORDS.append(rec(
    "cape-chaplina",
    "Mũi Chaplina (Mys Chaplina)",
    "Мыс Чаплина",
    "Cape Chaplino",
    ["other"],
    64.4048, -172.2276,
    "Mỏm đông nam bán đảo Chukchi, ra biển Bering, huyện Providensky, Khu tự trị Chukotka, Nga.",
    "Mũi đất ở góc đông nam bán đảo Chukchi, gần di chỉ làng Eskimo cổ Ungazik (Chaplino cũ). Nơi đây có hải đăng, bãi hải mã, xương cá voi và những đàn chim biển – một cột mốc và điểm quan sát động vật hoang dã ven bờ Bering.",
    "Mũi Chaplina là một mỏm đất nhô ra biển Bering ở góc đông nam bán đảo Chukchi. Gần mũi từng có làng Eskimo cổ Ungazik (còn gọi là Chaplino cũ) – một trong những khu định cư săn thú biển quan trọng, nay đã bị bỏ và cư dân chuyển về Novoye Chaplino. Mũi đất là một mốc hàng hải với ngọn hải đăng, đồng thời là nơi tụ họp của thiên nhiên hoang dã vùng cực: các bãi đá là chỗ hải mã lên nghỉ, ven bờ rải rác xương cá voi, còn vách đá và triền cỏ đài nguyên là nơi làm tổ của chim biển. Vùng nước quanh mũi giàu sinh vật nên thu hút cả cá voi. Với du khách đi thuyền dọc bờ nam Chukchi, Cape Chaplino là điểm quan sát động vật và cảnh quan hoang sơ, đồng thời gợi nhớ lịch sử lâu đời của các cộng đồng Eskimo bản địa nơi đây.",
    [
        "Mỏm đông nam bán đảo Chukchi, gần di chỉ làng Eskimo cổ Ungazik.",
        "Có hải đăng, bãi hải mã, xương cá voi và các đàn chim biển.",
        "Điểm quan sát động vật hoang dã trên các tour thuyền dọc bờ Bering.",
    ],
    {
        "hours_vi": "Vùng hoang dã ven biển; ghé qua trên tour thuyền.",
        "ticket_vi": "Không có vé; chi phí theo tour.",
        "duration_vi": "Điểm dừng khoảng 1 giờ trong hành trình.",
        "best_time_vi": "Mùa hè (tháng 7–9) khi có thể đi thuyền và động vật hoạt động.",
        "tips_vi": "Giữ khoảng cách với bãi hải mã; tuân thủ hướng dẫn để không làm chúng hoảng loạn.",
    },
    [
        {"title": "Wikipedia (EN) — Cape Chaplino", "url": "https://en.wikipedia.org/wiki/Cape_Chaplino"},
        {"title": "Wikipedia (RU) — Мыс Чаплина", "url": "https://ru.wikipedia.org/wiki/Мыс_Чаплина"},
    ],
    ["chukotka", "cape", "walrus", "lighthouse", "eskimo", "bering-sea"],
    maps_text("Мыс Чаплина", "Чукотка", "Cape Chaplino", "Chukotka", 64.4048, -172.2276),
))

# 24) Mũi Shmidta ------------------------------------------------------------
RECORDS.append(rec(
    "cape-schmidt",
    "Mũi Shmidta (Mys Shmidta)",
    "Мыс Шмидта",
    "Cape Schmidt",
    ["other"],
    68.9067, -179.3667,
    "Bờ biển Chukchi, tây bắc Chukotka, huyện Iultinsky, Khu tự trị Chukotka, Nga.",
    "Mũi đất và khu dân cư trên bờ biển Chukchi mang tên nhà thám hiểm Bắc Cực Otto Schmidt, gắn liền với lịch sử hàng không địa cực và Đường Biển Phương Bắc. Vùng bờ biển này còn nổi tiếng là nơi gấu Bắc Cực thường lai vãng.",
    "Mũi Shmidta là một mỏm đất trên bờ biển Chukchi ở tây bắc Chukotka, cùng khu dân cư nhỏ mang tên nhà toán học – thám hiểm địa cực nổi tiếng Otto Schmidt. Trong thời kỳ khai phá Bắc Cực và vận hành Đường Biển Phương Bắc, đây là một điểm tựa quan trọng: có trạm khí tượng, sân bay phục vụ hàng không địa cực và là mắt xích trên tuyến hải trình băng giá. Vùng bờ biển quanh mũi Shmidta khét tiếng với băng dày, sương mù và thời tiết khắc nghiệt, đồng thời là nơi gấu Bắc Cực thường xuyên lang thang kiếm ăn ven bờ, nhất là vào mùa băng. Ngày nay khu dân cư đã thu nhỏ nhiều, nhưng địa danh vẫn gợi lại một chương sử hào hùng và gian khó của công cuộc chinh phục Bắc Cực Xô-viết. Đây là điểm đến của những ai muốn chạm tới một mốc địa lý xa xôi trên bờ biển băng của Chukotka.",
    [
        "Mũi đất và khu dân cư mang tên nhà thám hiểm địa cực Otto Schmidt.",
        "Gắn với lịch sử hàng không địa cực và Đường Biển Phương Bắc.",
        "Bờ biển băng giá nổi tiếng là nơi gấu Bắc Cực thường lui tới.",
    ],
    {
        "hours_vi": "Khu dân cư nhỏ vùng xa; không có dịch vụ du lịch chuyên biệt.",
        "ticket_vi": "Không có vé.",
        "duration_vi": "Điểm dừng ngắn tùy hành trình.",
        "best_time_vi": "Mùa hè khi tiếp cận thuận lợi hơn.",
        "tips_vi": "Cảnh giác gấu Bắc Cực ven bờ; thời tiết xấu thường làm gián đoạn chuyến bay.",
    },
    [
        {"title": "Wikipedia (EN) — Cape Schmidt", "url": "https://en.wikipedia.org/wiki/Cape_Schmidt"},
        {"title": "Wikipedia (RU) — Мыс Шмидта (село)", "url": "https://ru.wikipedia.org/wiki/Мыс_Шмидта_(село)"},
    ],
    ["chukotka", "cape", "otto-schmidt", "polar-aviation", "polar-bear", "chukchi-sea"],
    maps_text("Мыс Шмидта", "Чукотка", "Cape Schmidt", "Chukotka", 68.9067, -179.3667),
))

# 25) Bãi hải mã đảo Arakamchechen -------------------------------------------
RECORDS.append(rec(
    "arakamchechen-walrus-rookery",
    "Bãi hải mã đảo Arakamchechen (Ostrov Arakamchechen)",
    "Остров Аракамчечен",
    "Arakamchechen Island (walrus rookery)",
    ["other"],
    64.7000, -172.4500,
    "Trong eo biển Senyavin, gần đảo Yttygran, huyện Providensky, Khu tự trị Chukotka, Nga.",
    "Hòn đảo trong eo biển Senyavin nổi tiếng với một trong những bãi lên bờ (rookery) đông đúc nhất của hải mã Thái Bình Dương. Hàng nghìn con hải mã chen chúc trên bãi đá, cùng cá voi lượn quanh vùng nước – một điểm nhấn của Vườn quốc gia Beringia.",
    "Đảo Arakamchechen nằm trong eo biển Senyavin, ngay cạnh đảo Yttygran nơi có “Hẻm Xương Cá voi” nổi tiếng. Đảo được biết đến nhiều nhất nhờ bãi hải mã (walrus haulout/rookery) khổng lồ ở mũi phía đông: vào cuối hè và mùa thu, hàng nghìn con hải mã Thái Bình Dương kéo lên nằm chen chúc trên bãi đá và triền dốc ven biển, tạo nên một trong những cảnh tượng tập trung động vật hoang dã ấn tượng nhất Bắc Cực. Vùng nước quanh đảo, giàu nhuyễn thể và cá, cũng là nơi cá voi xám tìm đến kiếm ăn, nên các tour thuyền thường kết hợp ngắm hải mã trên bãi và cá voi dưới nước. Là một phần của Vườn quốc gia Beringia, Arakamchechen thường được ghép cùng chuyến thăm Hẻm Xương Cá voi ở Yttygran, cho du khách một ngày trọn vẹn giữa thiên nhiên và di sản của eo biển Senyavin.",
    [
        "Một trong những bãi lên bờ đông đúc nhất của hải mã Thái Bình Dương.",
        "Hàng nghìn con hải mã chen chúc trên bãi đá vào cuối hè – thu.",
        "Thường ghép tour cùng Hẻm Xương Cá voi (đảo Yttygran) trong Vườn quốc gia Beringia.",
    ],
    {
        "hours_vi": "Đảo hoang; ghé qua trên tour thuyền từ Provideniya.",
        "ticket_vi": "Không có vé; chi phí và giấy phép công viên nằm trong tour.",
        "duration_vi": "Điểm dừng 1–2 giờ, thường trong ngày cùng Yttygran.",
        "best_time_vi": "Cuối hè đến đầu thu (tháng 8–9) khi hải mã tụ đông trên bãi.",
        "tips_vi": "Tuyệt đối giữ khoảng cách và im lặng: hải mã dễ hoảng loạn giẫm đạp nhau khi bị quấy rầy.",
    },
    [
        {"title": "Wikipedia (EN) — Arakamchechen Island", "url": "https://en.wikipedia.org/wiki/Arakamchechen_Island"},
        {"title": "Wikipedia (RU) — Аракамчечен", "url": "https://ru.wikipedia.org/wiki/Аракамчечен"},
    ],
    ["chukotka", "island", "walrus", "beringia", "senyavin-strait", "wildlife"],
    maps_text("Остров Аракамчечен", "Чукотка", "Arakamchechen Island", "Chukotka", 64.7000, -172.4500),
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
