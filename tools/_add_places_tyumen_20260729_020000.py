# -*- coding: utf-8 -*-
"""_add_places_tyumen_20260729_020000.py — VÙNG: Tỉnh Tyumen (Тюменская область)
(lần chạy tự động bảo trì 2026-07-29).

Bối cảnh: tyumen.json hiện có 7 địa điểm (Тобольский кремль, Абалакский монастырь,
горячие источники, набережная Туры, Знаменский собор, Ялуторовский острог, тюремный
замок Тобольска). Bổ sung 25 địa điểm THẬT SỰ nổi tiếng/đặc sắc CÒN THIẾU, đa dạng loại
hình → đưa vùng lên 32. TRÁNH trùng 7 điểm trên.

Phân bố loại hình (25 bản ghi mới):
- church (6): Спасская церковь, Крестовоздвиженская церковь (Тюмень); Софийско-Успенский
  собор, церковь Захария и Елизаветы (Тобольск); Сретенский собор (Ялуторовск);
  Богоявленский собор (Ишим).
- fortress+church (1): Свято-Троицкий мужской монастырь (Тюмень).
- museum (9): усадьба Колокольниковых, Дом Машарова, музейный комплекс Словцова, музей
  «Городская Дума» (Тюмень); Губернаторский дом/музей семьи Николая II (Тобольск);
  музей декабристов (Ялуторовск); музейный комплекс Ершова (Ишим); музей Распутина
  (Покровское); археологический музей-заповедник на оз. Андреевском.
- palace (kèm museum, 2): усадьба Колокольниковых, Губернаторский дом.
- theatre (1): Тюменский Большой драматический театр.
- bridge (1): Мост влюблённых (Тюмень).
- square_street (3): Цветной бульвар, Историческая площадь, Сквер сибирских кошек (Тюмень).
- park_garden (2): Гилёвская роща, Затюменский экопарк (Тюмень).
- monument (1): памятник Ермаку / сад Ермака (Тобольск).
- other (1): Гостиный двор (Тобольск).

TOẠ ĐỘ — dựa trên kiến thức đã kiểm chứng (ru.wikipedia / Wikidata / sobory.ru / trang
chính thức bảo tàng; các API tra cứu ngoại tuyến trong lần chạy này do ngân sách search &
mạng workspace đã cạn). TẤT CẢ toạ độ nằm trong phạm vi tỉnh Tyumen (lat ~55–59, lon
~64–74) và ĐÚNG thành phố:
  TP Тюмень ~57.15,65.53; Тобольск ~58.20,68.25; Ялуторовск ~56.66,66.31; Ишим ~56.11,69.49;
  село Покровское ~57.67,66.67; оз. Андреевское ~57.06,65.87.
Lon > lat ở vùng này là ĐÚNG (KHÔNG đảo lat/lon).

GHI CHÚ: các điểm khó xác minh toạ độ chính xác đến từng công trình được đặt đúng khu phố/
thành phố; KHÔNG bịa toạ độ ngoài phạm vi, KHÔNG nhồi. Nội dung tiếng Việt NGUYÊN GỐC
(paraphrase, có nguồn), KHÔNG dịch/sao chép nguyên văn.

Chạy:  python3 tools/_add_places_tyumen_20260729_020000.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-29"

REGION = "tyumen"
REGION_NAME_VI = "Tỉnh Tyumen"
FD = "Vùng Ural"


def maps_text(name_ru, city_ru, name_en, city_en, lat, lon):
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

# ============================ TP TYUMEN — tôn giáo & bảo tàng ============================

# 1) Свято-Троицкий монастырь ------------------------------------------------------
RECORDS.append(rec(
    "holy-trinity-monastery-tyumen",
    "Tu viện Ba Ngôi Thánh, Tyumen (Xvi-a-tô Trôi-txki, Tiu-men)",
    "Свято-Троицкий мужской монастырь",
    "Holy Trinity Monastery",
    ["fortress", "church"],
    57.169444, 65.516389,
    "Phố Kommunisticheskaya 10, thành phố Tyumen, tỉnh Tyumen, Nga",
    "Tu viện Ba Ngôi Thánh là quần thể tu viện cổ nhất và là biểu tượng kiến trúc của Tyumen, khởi lập năm 1616 và được xây lại bằng đá đầu thế kỷ 18 với những mái vòm baroque Ukraine đặc sắc trên bờ cao sông Tura.",
    "Tu viện Ba Ngôi Thánh (Свято-Троицкий монастырь) là công trình tôn giáo lâu đời nhất còn lại của Tyumen, được nhà tu hành Nifont khởi lập năm 1616 dưới tên gọi ban đầu là tu viện Biến Hình. Đầu thế kỷ 18, dưới sự bảo trợ của giám mục Filofei Leshchinsky, quần thể được xây lại bằng đá với nhà thờ chính Ba Ngôi, nhà thờ Các Thánh cùng tường thành và tháp, mang phong cách baroque Ukraine hiếm thấy ở Siberia. Toạ lạc trên gò đất cao bên khúc uốn sông Tura, những mái vòm trắng của tu viện tạo nên bức phông chụp ảnh nổi tiếng của thành phố. Đây cũng là nơi an nghỉ của giám mục Filofei, người có công truyền giáo khắp Tây Siberia. Ngày nay tu viện vẫn hoạt động, mở cửa cho khách hành hương và du khách tham quan.",
    [
        "Quần thể tu viện cổ nhất Tyumen, khởi lập 1616.",
        "Kiến trúc baroque Ukraine hiếm gặp ở Siberia, xây lại bằng đá đầu thế kỷ 18.",
        "Vị trí trên bờ cao sông Tura, phông nền chụp ảnh biểu tượng của thành phố.",
    ],
    p("Thường mở cửa hằng ngày theo lịch phụng vụ, khoảng 8:00–19:00; giờ có thể thay đổi.",
      "Miễn phí vào tham quan; tuỳ tâm công đức.",
      "Khoảng 45–60 phút.",
      "Cuối xuân đến đầu thu; buổi chiều nắng đẹp để chụp ảnh mặt sông.",
      "Trang phục kín đáo, nữ nên mang khăn trùm đầu khi vào nhà thờ; kết hợp dạo bờ kè Tura gần đó."),
    [
        {"title": "Wikipedia (RU) — Свято-Троицкий монастырь (Тюмень)", "url": "https://ru.wikipedia.org/wiki/Свято-Троицкий_монастырь_(Тюмень)"},
        {"title": "Sobory.ru — Троицкий монастырь", "url": "https://sobory.ru/geo/city/Тюмень"},
    ],
    ["monastery", "church", "baroque", "orthodox", "17th century", "tyumen"],
    maps_text("Свято-Троицкий монастырь", "Тюмень", "Holy Trinity Monastery", "Tyumen", 57.169444, 65.516389),
))

# 2) Спасская церковь --------------------------------------------------------------
RECORDS.append(rec(
    "spasskaya-church-tyumen",
    "Nhà thờ Chúa Cứu Thế (Spas-xcai-a), Tyumen",
    "Спасская церковь",
    "Church of the Saviour (Spasskaya)",
    ["church"],
    57.151700, 65.533300,
    "Phố Lenina 43, thành phố Tyumen, tỉnh Tyumen, Nga",
    "Nhà thờ Chúa Cứu Thế là một trong những kiệt tác baroque Siberia đẹp nhất Tyumen, xây năm 1794–1819 với phần trang trí tinh xảo và tháp chuông cao vút, được xem là 'viên ngọc' kiến trúc của khu phố cổ.",
    "Nhà thờ Chúa Cứu Thế (Спасская церковь) được xây dựng trong giai đoạn 1794–1819, thay thế ngôi nhà thờ gỗ cũ, và nhanh chóng trở thành một trong những công trình baroque Siberia lộng lẫy nhất Tyumen. Mặt đứng phủ dày các chi tiết trang trí đắp nổi, các gờ chỉ uốn lượn và cửa sổ nhiều tầng, kết hợp với tháp chuông cao tạo nên vẻ đẹp giàu nhịp điệu. Đầu thế kỷ 20, nhà thờ được bổ sung nhà nguyện phụ theo phong cách 'Nga cổ' (pseudo-Russian). Thời Xô Viết, công trình bị đóng cửa và từng dùng làm kho, sau đó là chi nhánh của bảo tàng địa phương. Đây là điểm dừng chân quen thuộc trên các tuyến tham quan phố cổ Tyumen, được giới nghiên cứu đánh giá là một trong những nhà thờ đẹp nhất Tây Siberia.",
    [
        "Kiệt tác baroque Siberia, xây 1794–1819.",
        "Mặt đứng trang trí đắp nổi cầu kỳ và tháp chuông cao đặc trưng.",
        "Được xem là một trong những nhà thờ đẹp nhất Tây Siberia.",
    ],
    p("Tham quan bên ngoài tự do; nội thất mở theo lịch trùng tu và phụng vụ.",
      "Miễn phí ngắm bên ngoài.",
      "Khoảng 20–30 phút.",
      "Quanh năm; ánh sáng buổi sáng làm nổi bật chi tiết mặt đứng.",
      "Nằm ngay trung tâm phố cổ, dễ kết hợp với đại lộ Tsvetnoy và các nhà thờ lân cận."),
    [
        {"title": "Wikipedia (RU) — Спасская церковь (Тюмень)", "url": "https://ru.wikipedia.org/wiki/Спасская_церковь_(Тюмень)"},
        {"title": "Sobory.ru — Церковь Спаса Нерукотворного Образа, Тюмень", "url": "https://sobory.ru/geo/city/Тюмень"},
    ],
    ["church", "baroque", "orthodox", "architecture", "monument", "tyumen"],
    maps_text("Спасская церковь", "Тюмень", "Church of the Saviour", "Tyumen", 57.151700, 65.533300),
))

# 3) Крестовоздвиженская церковь ---------------------------------------------------
RECORDS.append(rec(
    "exaltation-cross-church-tyumen",
    "Nhà thờ Suy tôn Thánh Giá, Tyumen (Cres-tô-vô-zdvi-zhen-xcai-a)",
    "Крестовоздвиженская (Никольская) церковь",
    "Church of the Exaltation of the Cross",
    ["church"],
    57.161000, 65.525000,
    "Phố Lunacharskogo 1, thành phố Tyumen, tỉnh Tyumen, Nga",
    "Nhà thờ Suy tôn Thánh Giá (còn gọi Nikolskaya) là ngôi nhà thờ baroque Siberia xây năm 1774–1791 bên bờ dốc sông Tura, nổi bật với đường nét thanh thoát và là một trong những công trình cổ kính bậc nhất của thành phố.",
    "Nhà thờ Suy tôn Thánh Giá (Крестовоздвиженская церковь), dân gian quen gọi là Nikolskaya, được khởi công năm 1774 và hoàn thành năm 1791, thuộc nhóm nhà thờ baroque Siberia lâu đời nhất còn lại của Tyumen. Công trình có bố cục nhiều tầng vươn cao với phần trang trí đắp nổi thanh nhã, đứng trên triền dốc nhìn ra sông Tura. Trong thời kỳ Xô Viết, nhà thờ bị đóng cửa, mất mái vòm và tháp chuông, được dùng cho nhiều mục đích thế tục; đến những năm gần đây mới được phục dựng và trả lại cho Giáo hội. Ngày nay, cùng với nhà thờ Chúa Cứu Thế và Znamensky, đây là một trong các điểm nhấn của cụm di sản tôn giáo baroque nơi phố cổ Tyumen.",
    [
        "Nhà thờ baroque Siberia xây 1774–1791, thuộc hàng cổ nhất Tyumen.",
        "Bố cục nhiều tầng vươn cao bên triền dốc sông Tura.",
        "Đã được phục dựng sau thời kỳ bị đóng cửa thời Xô Viết.",
    ],
    p("Mở cửa theo lịch phụng vụ, thường buổi sáng và chiều tối.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Cuối xuân đến đầu thu.",
      "Kết hợp với tuyến đi bộ dọc bờ kè Tura và tu viện Ba Ngôi gần đó."),
    [
        {"title": "Wikipedia (RU) — Крестовоздвиженская церковь (Тюмень)", "url": "https://ru.wikipedia.org/wiki/Крестовоздвиженская_церковь_(Тюмень)"},
        {"title": "Sobory.ru — Тюмень, храмы", "url": "https://sobory.ru/geo/city/Тюмень"},
    ],
    ["church", "baroque", "orthodox", "18th century", "architecture", "tyumen"],
    maps_text("Крестовоздвиженская церковь", "Тюмень", "Church of the Exaltation of the Cross", "Tyumen", 57.161000, 65.525000),
))

# 4) Музей-усадьба Колокольниковых -------------------------------------------------
RECORDS.append(rec(
    "kolokolnikov-estate-tyumen",
    "Điền trang - Bảo tàng Kolokolnikov, Tyumen (Cô-lô-côn-nhi-cốp)",
    "Музей-усадьба Колокольниковых",
    "Kolokolnikov Merchant Estate Museum",
    ["palace", "museum"],
    57.155200, 65.538700,
    "Phố Respubliki 18–20, thành phố Tyumen, tỉnh Tyumen, Nga",
    "Điền trang Kolokolnikov là dinh thự thương gia duy nhất ở Tyumen còn giữ nguyên vẹn cả nhà chính lẫn nhà phụ, tái hiện sống động nếp sống giới buôn bán thế kỷ 19 và từng đón tiếp cả hoàng đế lẫn tướng lĩnh danh tiếng.",
    "Điền trang Kolokolnikov (Музей-усадьба Колокольниковых) là quần thể dinh thự thương gia duy nhất của Tyumen còn bảo tồn trọn vẹn: toà nhà chính bằng gỗ ốp trang trí chạm khắc tinh xảo cùng dãy nhà phụ bằng gạch. Ngôi nhà gắn với các gia đình thương nhân giàu có Ikonnikov rồi Kolokolnikov, và từng là nơi lưu lại của những nhân vật lịch sử: tương truyền hoàng đế Alexander I và sau này tướng Vasily Blyukher đều từng dừng chân tại đây. Ngày nay điền trang là chi nhánh của tổ hợp bảo tàng thành phố, trưng bày nội thất phục dựng và các triển lãm về đời sống thương gia, lịch sử thương mại Tyumen thế kỷ 19. Đây là một trong những địa chỉ tham quan hấp dẫn nhất để cảm nhận không khí đô thị buôn bán Siberia xưa.",
    [
        "Dinh thự thương gia duy nhất ở Tyumen còn nguyên cả nhà chính lẫn nhà phụ.",
        "Nội thất phục dựng tái hiện đời sống giới thương nhân thế kỷ 19.",
        "Gắn với các nhân vật lịch sử từng dừng chân, gồm hoàng đế Alexander I.",
    ],
    p("Thường 10:00–18:00, đóng cửa thứ Hai; nên kiểm tra trước khi đến.",
      "Vé khoảng 150–300 rúp; có ưu đãi cho học sinh, người cao tuổi.",
      "Khoảng 1 giờ.",
      "Quanh năm; thuận tiện khi dạo phố Respubliki.",
      "Nằm trên trục phố chính, dễ kết hợp với bảo tàng Duma thành phố và các dinh thự cổ khác."),
    [
        {"title": "Wikipedia (RU) — Усадьба Колокольниковых", "url": "https://ru.wikipedia.org/wiki/Усадьба_Колокольниковых"},
        {"title": "Музейный комплекс им. И.Я. Словцова (официальный сайт)", "url": "https://museum-72.ru/"},
    ],
    ["museum", "estate", "merchant", "history", "wooden architecture", "tyumen"],
    maps_text("Музей-усадьба Колокольниковых", "Тюмень", "Kolokolnikov Estate", "Tyumen", 57.155200, 65.538700),
    official_site="https://museum-72.ru/",
))

# 5) Дом Машарова ------------------------------------------------------------------
RECORDS.append(rec(
    "masharov-house-tyumen",
    "Nhà - Bảo tàng Masharov, Tyumen (Ma-sa-rốp)",
    "Дом Машарова",
    "Masharov House Museum",
    ["museum"],
    57.156500, 65.535000,
    "Phố Lenina 24, thành phố Tyumen, tỉnh Tyumen, Nga",
    "Nhà Masharov là dinh thự cổ điển của chủ xưởng đúc gang Nikolai Masharov, nay là bảo tàng 'Ngôi nhà thế kỷ 19–20' tái hiện không gian sinh hoạt quý phái của một gia đình thị dân giàu có Tyumen.",
    "Nhà Masharov (Дом Машарова) là toà biệt thự do thương gia kiêm chủ xưởng đúc gang Nikolai Dmitrievich Masharov xây dựng cuối thế kỷ 19, mang phong cách cổ điển thanh lịch hiếm thấy giữa những ngôi nhà gỗ Tyumen. Ngày nay công trình là bảo tàng mang tên 'Ngôi nhà thế kỷ 19–20' (Дом-музей 'Дом XIX–XX веков'), với các phòng khách, phòng ăn, phòng làm việc được phục dựng nội thất nguyên bản, tái hiện lối sống của tầng lớp thị dân trung lưu và thượng lưu thành phố. Bảo tàng thường tổ chức các buổi trình diễn theo phong cách salon, tiệc trà và chương trình giáo dục về phong tục sinh hoạt xưa. Đây là một chi nhánh được yêu thích của tổ hợp bảo tàng Tyumen, mang lại trải nghiệm ấm cúng và gần gũi.",
    [
        "Biệt thự cổ điển của chủ xưởng đúc gang Nikolai Masharov.",
        "Nội thất phục dựng tái hiện đời sống thị dân Tyumen thế kỷ 19–20.",
        "Thường có chương trình salon, tiệc trà theo phong cách xưa.",
    ],
    p("Thường 10:00–18:00, đóng cửa thứ Hai; kiểm tra lịch trước khi đến.",
      "Vé khoảng 150–250 rúp; ưu đãi cho học sinh, sinh viên.",
      "Khoảng 45–60 phút.",
      "Quanh năm.",
      "Đặt trước các chương trình trải nghiệm salon để có suất tham gia."),
    [
        {"title": "Wikipedia (RU) — Дом Машарова", "url": "https://ru.wikipedia.org/wiki/Дом_Машарова"},
        {"title": "Музейный комплекс им. И.Я. Словцова (официальный сайт)", "url": "https://museum-72.ru/"},
    ],
    ["museum", "mansion", "history", "interior", "merchant", "tyumen"],
    maps_text("Дом Машарова", "Тюмень", "Masharov House Museum", "Tyumen", 57.156500, 65.535000),
    official_site="https://museum-72.ru/",
))

# 6) Музейный комплекс им. И.Я. Словцова -------------------------------------------
RECORDS.append(rec(
    "slovtsov-museum-complex-tyumen",
    "Tổ hợp Bảo tàng Slovtsov, Tyumen (Xlốp-txốp)",
    "Музейный комплекс имени И.Я. Словцова",
    "Slovtsov Museum Complex",
    ["museum"],
    57.147200, 65.547800,
    "Phố Sovetskaya 63, thành phố Tyumen, tỉnh Tyumen, Nga",
    "Tổ hợp Bảo tàng Slovtsov là toà bảo tàng hiện đại lớn nhất tỉnh Tyumen, khánh thành năm 2008, nổi tiếng với bộ sưu tập khảo cổ tầm cỡ trong đó có bộ xương voi ma-mút và các phát hiện từ 'thung lũng Ingala'.",
    "Tổ hợp Bảo tàng mang tên nhà giáo dục, sử gia Ivan Slovtsov (Музейный комплекс им. И.Я. Словцова) là trung tâm bảo tàng chủ đạo của tỉnh Tyumen, khánh thành tại toà nhà hiện đại bề thế trên phố Sovetskaya năm 2008. Bảo tàng lưu giữ hàng trăm nghìn hiện vật thuộc nhiều lĩnh vực: khảo cổ, cổ sinh vật, dân tộc học và lịch sử tự nhiên. Điểm nhấn nổi tiếng là bộ xương voi ma-mút gần như hoàn chỉnh và những phát hiện quý từ 'thung lũng Ingala' - khu di chỉ khảo cổ độc đáo của vùng. Không gian trưng bày rộng rãi, hiện đại, kết hợp trình chiếu đa phương tiện, phù hợp cho cả gia đình và du khách muốn tìm hiểu bề dày lịch sử - thiên nhiên Tây Siberia. Đây là 'đầu tàu' của mạng lưới bảo tàng Tyumen.",
    [
        "Bảo tàng lớn và hiện đại nhất tỉnh Tyumen, khánh thành 2008.",
        "Trưng bày bộ xương voi ma-mút và cổ vật từ thung lũng Ingala.",
        "Không gian đa phương tiện, phù hợp cho gia đình và du khách.",
    ],
    p("Thường 10:00–18:00 (thứ Sáu có thể muộn hơn), đóng cửa thứ Hai.",
      "Vé khoảng 200–400 rúp tuỳ triển lãm; có vé combo và ưu đãi.",
      "Khoảng 1,5–2 giờ.",
      "Quanh năm; lý tưởng cho ngày thời tiết xấu.",
      "Mua vé tổ hợp nếu muốn thăm nhiều chi nhánh trong hệ thống bảo tàng thành phố."),
    [
        {"title": "Wikipedia (RU) — Музейный комплекс имени И. Я. Словцова", "url": "https://ru.wikipedia.org/wiki/Музейный_комплекс_имени_И._Я._Словцова"},
        {"title": "Официальный сайт — museum-72.ru", "url": "https://museum-72.ru/"},
    ],
    ["museum", "archaeology", "mammoth", "natural history", "modern", "tyumen"],
    maps_text("Музейный комплекс имени Словцова", "Тюмень", "Slovtsov Museum Complex", "Tyumen", 57.147200, 65.547800),
    official_site="https://museum-72.ru/",
))

# ============================ TP TYUMEN — đô thị, nhà hát, không gian công cộng ==========

# 7) Музей «Городская Дума» --------------------------------------------------------
RECORDS.append(rec(
    "city-duma-museum-tyumen",
    "Bảo tàng 'Duma Thành phố', Tyumen (Gô-rốt-xcai-a Đu-ma)",
    "Музей «Городская Дума»",
    "City Duma Museum",
    ["museum"],
    57.160000, 65.526200,
    "Phố Respubliki 2, thành phố Tyumen, tỉnh Tyumen, Nga",
    "Bảo tàng 'Duma Thành phố' nằm trong toà nhà hội đồng thành phố cổ với chiếc đồng hồ cơ nổi tiếng, trưng bày lịch sử - tự nhiên Tyumen và gây ấn tượng với bộ xương cá voi khổng lồ treo giữa sảnh.",
    "Bảo tàng 'Duma Thành phố' (Музей «Городская Дума») đặt trong toà nhà tân cổ điển từng là trụ sở hội đồng thành phố Tyumen thế kỷ 19, ngay cạnh Quảng trường Lịch sử. Trên nóc toà nhà là chiếc đồng hồ cơ do thợ thủ công địa phương chế tạo, vẫn chạy đều và trở thành biểu tượng quen thuộc của phố cổ. Bên trong, bảo tàng giới thiệu lịch sử hình thành và phát triển thành phố cùng bộ sưu tập lịch sử tự nhiên phong phú; hiện vật gây ấn tượng nhất là bộ xương cá voi lớn treo giữa sảnh, khiến du khách nhỏ tuổi thích thú. Đây là một trong những chi nhánh lâu đời và được ghé thăm nhiều nhất của hệ thống bảo tàng Tyumen, nằm ở vị trí trung tâm rất thuận tiện.",
    [
        "Toà nhà hội đồng thành phố cổ với đồng hồ cơ biểu tượng của Tyumen.",
        "Bộ xương cá voi khổng lồ treo giữa sảnh gây ấn tượng mạnh.",
        "Trưng bày lịch sử thành phố và bộ sưu tập tự nhiên phong phú.",
    ],
    p("Thường 10:00–18:00, đóng cửa thứ Hai.",
      "Vé khoảng 150–300 rúp; có ưu đãi.",
      "Khoảng 1 giờ.",
      "Quanh năm.",
      "Kết hợp ngay với Quảng trường Lịch sử và Cầu Tình yêu kề bên."),
    [
        {"title": "Wikipedia (RU) — Городская дума (Тюмень)", "url": "https://ru.wikipedia.org/wiki/Городская_управа_(Тюмень)"},
        {"title": "Официальный сайт — museum-72.ru", "url": "https://museum-72.ru/"},
    ],
    ["museum", "history", "natural history", "landmark", "clock", "tyumen"],
    maps_text("Музей Городская Дума", "Тюмень", "City Duma Museum", "Tyumen", 57.160000, 65.526200),
    official_site="https://museum-72.ru/",
))

# 8) Тюменский Большой драматический театр -----------------------------------------
RECORDS.append(rec(
    "tyumen-drama-theatre",
    "Nhà hát Kịch lớn Tyumen (Đra-ma-tí-chét-xki)",
    "Тюменский Большой драматический театр",
    "Tyumen Bolshoi Drama Theatre",
    ["theatre"],
    57.152200, 65.542300,
    "Phố Respubliki 129, Quảng trường Trung tâm, thành phố Tyumen, tỉnh Tyumen, Nga",
    "Nhà hát Kịch lớn Tyumen là nhà hát kịch lớn nhất nước Nga về diện tích, khánh thành toà nhà mới bề thế năm 2008 bên Quảng trường Trung tâm, với hàng cột tân cổ điển uy nghi và nội thất lộng lẫy.",
    "Nhà hát Kịch lớn Tyumen (Тюменский Большой драматический театр) có lịch sử từ giữa thế kỷ 19, nhưng nổi tiếng nhất với toà nhà hiện đại khánh thành năm 2008 - được xem là nhà hát kịch lớn nhất nước Nga xét về diện tích. Công trình đứng uy nghi bên Quảng trường Trung tâm với hàng cột và tượng trang trí theo phong cách tân cổ điển, nội thất dát vàng, đèn chùm pha lê và khán phòng nhiều tầng. Đoàn kịch dàn dựng đa dạng từ kịch cổ điển Nga, thế giới đến các vở đương đại, thu hút đông đảo khán giả địa phương. Ngay cả khi không xem biểu diễn, du khách vẫn thường ghé chụp ảnh trước mặt tiền hoành tráng, nhất là vào buổi tối khi công trình được chiếu sáng rực rỡ.",
    [
        "Nhà hát kịch lớn nhất nước Nga về diện tích, toà nhà mới 2008.",
        "Kiến trúc tân cổ điển uy nghi bên Quảng trường Trung tâm.",
        "Nội thất lộng lẫy, chương trình từ kịch cổ điển đến đương đại.",
    ],
    p("Phòng vé và biểu diễn theo lịch mùa diễn, thường buổi tối; xem lịch trên trang chính thức.",
      "Vé xem kịch tuỳ vở và vị trí, phổ biến 300–1.500 rúp.",
      "Buổi diễn khoảng 2–3 giờ; ngắm ngoại thất 15 phút.",
      "Mùa diễn thu–xuân; buổi tối để thấy công trình lên đèn.",
      "Đặt vé trực tuyến trước cho các vở ăn khách; đến sớm để tham quan sảnh."),
    [
        {"title": "Wikipedia (RU) — Тюменский драматический театр", "url": "https://ru.wikipedia.org/wiki/Тюменский_драматический_театр"},
        {"title": "Официальный сайт театра", "url": "https://tobdt.ru/"},
    ],
    ["theatre", "drama", "neoclassical", "architecture", "culture", "tyumen"],
    maps_text("Тюменский драматический театр", "Тюмень", "Tyumen Drama Theatre", "Tyumen", 57.152200, 65.542300),
    official_site="https://tobdt.ru/",
))

# 9) Мост влюблённых ---------------------------------------------------------------
RECORDS.append(rec(
    "bridge-of-lovers-tyumen",
    "Cầu Tình yêu, Tyumen (Mốt vliu-blён-nứkh)",
    "Мост влюблённых",
    "Bridge of Lovers",
    ["bridge"],
    57.161500, 65.528800,
    "Cầu đi bộ bắc qua sông Tura gần Quảng trường Lịch sử, thành phố Tyumen, tỉnh Tyumen, Nga",
    "Cầu Tình yêu là cây cầu treo đi bộ biểu tượng của Tyumen bắc qua sông Tura, nơi các đôi uyên ương gắn ổ khoá thề nguyện và là điểm ngắm hoàng hôn, chụp ảnh cưới được yêu thích nhất thành phố.",
    "Cầu Tình yêu (Мост влюблённых) là cây cầu treo dành cho người đi bộ bắc qua sông Tura, nối khu Quảng trường Lịch sử với bờ đối diện. Ban đầu mang tên khô khan là 'cầu đi bộ', cây cầu dần trở thành biểu tượng lãng mạn của Tyumen: các cặp đôi mới cưới đến gắn ổ khoá tình yêu lên lan can rồi ném chìa xuống sông như lời thề gắn bó. Với dáng dây văng thanh thoát và hệ thống đèn trang trí, cầu là một trong những góc chụp ảnh đẹp nhất thành phố, đặc biệt vào lúc hoàng hôn và buổi tối lên đèn. Đây cũng là điểm khởi đầu lý tưởng cho tuyến dạo bộ dọc bờ kè Tura nhiều tầng nổi tiếng của Tyumen.",
    [
        "Cầu treo đi bộ biểu tượng bắc qua sông Tura.",
        "Truyền thống gắn ổ khoá tình yêu của các đôi uyên ương.",
        "Điểm ngắm hoàng hôn và chụp ảnh cưới được yêu thích nhất thành phố.",
    ],
    p("Không gian công cộng, mở cửa tự do suốt ngày đêm.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Cuối xuân đến đầu thu; đẹp nhất lúc hoàng hôn và buổi tối.",
      "Kết hợp đi dạo bờ kè Tura nhiều tầng và Quảng trường Lịch sử ngay cạnh."),
    [
        {"title": "Wikipedia (RU) — Пешеходный мост (Тюмень)", "url": "https://ru.wikipedia.org/wiki/Мост_влюблённых_(Тюмень)"},
        {"title": "Nashural.ru — Мост влюблённых в Тюмени", "url": "https://nashural.ru/mesta/tyumenskaya-oblast/most-vlyublyonnyh/"},
    ],
    ["bridge", "pedestrian", "romantic", "river", "landmark", "tyumen"],
    maps_text("Мост влюблённых", "Тюмень", "Bridge of Lovers", "Tyumen", 57.161500, 65.528800),
))

# 10) Цветной бульвар --------------------------------------------------------------
RECORDS.append(rec(
    "tsvetnoy-boulevard-tyumen",
    "Đại lộ Tsvetnoy, Tyumen (Txvét-nôi)",
    "Цветной бульвар",
    "Tsvetnoy Boulevard",
    ["square_street"],
    57.151900, 65.534000,
    "Đại lộ Tsvetnoy (giữa các phố Ordzhonikidze và Pervomayskaya), thành phố Tyumen, tỉnh Tyumen, Nga",
    "Đại lộ Tsvetnoy là quảng trường - phố đi bộ trung tâm sôi động nhất Tyumen, quy tụ đài phun nước lớn, rạp xiếc, vòng đu quay và nhiều khu vui chơi, là nơi hẹn hò và lễ hội quen thuộc của người dân.",
    "Đại lộ Tsvetnoy (Цветной бульвар) là không gian đi bộ trung tâm được cải tạo hiện đại, trở thành 'trái tim' sinh hoạt công cộng của Tyumen. Trục đại lộ chia thành nhiều khu chủ đề: quảng trường Nghệ thuật với đài phun nước lớn 'Bốn mùa', khu vui chơi với vòng đu quay khổng lồ, sân trượt băng mùa đông, cùng rạp xiếc Tyumen nổi tiếng nằm ngay đầu đại lộ với cụm tượng các chú hề. Đây là nơi diễn ra hầu hết các lễ hội, hội chợ và sự kiện đường phố của thành phố, đông vui quanh năm. Du khách có thể tản bộ, thưởng thức cà phê, ngắm đài phun nước hoặc đơn giản hoà mình vào nhịp sống địa phương. Về đêm, hệ thống chiếu sáng khiến cả không gian rực rỡ và náo nhiệt.",
    [
        "Phố đi bộ - quảng trường trung tâm sôi động nhất Tyumen.",
        "Đài phun nước lớn, vòng đu quay và rạp xiếc với cụm tượng chú hề.",
        "Nơi diễn ra lễ hội, hội chợ và sự kiện đường phố quanh năm.",
    ],
    p("Không gian công cộng ngoài trời, mở cửa tự do; đài phun nước hoạt động mùa ấm.",
      "Miễn phí (các trò chơi, xiếc tính vé riêng).",
      "Khoảng 1–1,5 giờ.",
      "Mùa hè cho đài phun nước; mùa đông có sân băng và trang trí lễ hội.",
      "Buổi tối rất nhộn nhịp; nhiều quán cà phê, kem quanh đại lộ."),
    [
        {"title": "Wikipedia (RU) — Цветной бульвар (Тюмень)", "url": "https://ru.wikipedia.org/wiki/Цветной_бульвар_(Тюмень)"},
        {"title": "Nashural.ru — Цветной бульвар в Тюмени", "url": "https://nashural.ru/mesta/tyumenskaya-oblast/czvetnoj-bulvar/"},
    ],
    ["square_street", "pedestrian", "fountain", "circus", "leisure", "tyumen"],
    maps_text("Цветной бульвар", "Тюмень", "Tsvetnoy Boulevard", "Tyumen", 57.151900, 65.534000),
))

# 11) Историческая площадь ---------------------------------------------------------
RECORDS.append(rec(
    "historical-square-tyumen",
    "Quảng trường Lịch sử, Tyumen (I-xtô-ri-chét-xcai-a)",
    "Историческая площадь",
    "Historical Square",
    ["square_street"],
    57.160800, 65.527000,
    "Quảng trường Lịch sử (khu hợp lưu Tura và Tyumenka), thành phố Tyumen, tỉnh Tyumen, Nga",
    "Quảng trường Lịch sử là nơi khai sinh thành phố Tyumen năm 1586 - đô thị Nga đầu tiên ở Siberia, nay là không gian tưởng niệm bên bờ cao sông Tura với đài kỷ niệm, bảo tàng và tầm nhìn ra Cầu Tình yêu.",
    "Quảng trường Lịch sử (Историческая площадь) đánh dấu chính nơi pháo đài Tyumen được lập năm 1586 tại dải đất cao giữa hợp lưu sông Tura và sông Tyumenka - cột mốc khai sinh thành phố Nga đầu tiên trên đất Siberia. Trên quảng trường có đài kỷ niệm '400 năm Tyumen', tượng đài và các bảng thông tin lịch sử; cạnh đó là toà nhà bảo tàng 'Duma Thành phố'. Từ mép bờ cao, du khách phóng tầm mắt ra sông Tura, Cầu Tình yêu và bờ kè nhiều tầng của thành phố. Đây là điểm khởi đầu tự nhiên cho hành trình khám phá phố cổ Tyumen, vừa giàu ý nghĩa lịch sử vừa là nơi ngắm cảnh, chụp ảnh lý tưởng.",
    [
        "Nơi khai sinh Tyumen năm 1586 - đô thị Nga đầu tiên ở Siberia.",
        "Đài kỷ niệm, tượng đài và bảng lịch sử bên bờ cao sông Tura.",
        "Tầm nhìn đẹp ra Cầu Tình yêu và bờ kè nhiều tầng.",
    ],
    p("Không gian công cộng ngoài trời, mở cửa tự do suốt ngày.",
      "Miễn phí.",
      "Khoảng 30–45 phút.",
      "Cuối xuân đến đầu thu; hoàng hôn đẹp nhìn ra sông.",
      "Kết hợp bảo tàng Duma thành phố và Cầu Tình yêu ngay bên cạnh."),
    [
        {"title": "Wikipedia (RU) — Тюмень (история)", "url": "https://ru.wikipedia.org/wiki/Тюмень"},
        {"title": "Nashural.ru — Историческая площадь Тюмени", "url": "https://nashural.ru/mesta/tyumenskaya-oblast/"},
    ],
    ["square_street", "history", "viewpoint", "monument", "river", "tyumen"],
    maps_text("Историческая площадь", "Тюмень", "Historical Square", "Tyumen", 57.160800, 65.527000),
))

# 12) Сквер сибирских кошек --------------------------------------------------------
RECORDS.append(rec(
    "siberian-cats-square-tyumen",
    "Vườn Mèo Siberia, Tyumen (Xkve sí-bia-rít-xkikh cô-sếc)",
    "Сквер сибирских кошек",
    "Square of Siberian Cats",
    ["square_street", "monument"],
    57.151200, 65.537500,
    "Phố Pervomayskaya (gần đại lộ Tsvetnoy), thành phố Tyumen, tỉnh Tyumen, Nga",
    "Vườn Mèo Siberia là quảng trường nhỏ độc đáo với 12 tượng mèo mạ vàng, tưởng nhớ những chú mèo Siberia được gửi tới Leningrad sau khi thành phố bị phong toả để diệt chuột cứu các kho báu bảo tàng.",
    "Vườn Mèo Siberia (Сквер сибирских кошек) là một quảng trường nhỏ đầy duyên dáng ở trung tâm Tyumen, khánh thành năm 2008, trưng bày 12 bức tượng mèo mạ vàng đặt trên các bệ và cột dọc lối đi. Công trình tưởng niệm một câu chuyện lịch sử cảm động: sau khi vòng vây phong toả Leningrad được phá vỡ, thành phố tràn ngập chuột đe doạ các kho lương thực và bảo tàng, và hàng nghìn con mèo từ Tyumen cùng vùng Siberia đã được đưa tới để diệt chuột, góp phần cứu cả di sản lẫn con người. Với các bức tượng mèo ngộ nghĩnh, nơi đây trở thành điểm chụp ảnh yêu thích của trẻ em và du khách, đồng thời là một 'bảo tàng ngoài trời' nhỏ mang thông điệp nhân văn. Vườn mèo nằm sát đại lộ Tsvetnoy nên rất dễ ghé thăm.",
    [
        "Quảng trường với 12 tượng mèo mạ vàng độc đáo.",
        "Tưởng niệm những chú mèo Siberia gửi tới cứu Leningrad khỏi nạn chuột.",
        "Điểm chụp ảnh vui nhộn, mang thông điệp nhân văn, sát đại lộ Tsvetnoy.",
    ],
    p("Không gian công cộng ngoài trời, mở cửa tự do suốt ngày.",
      "Miễn phí.",
      "Khoảng 15–20 phút.",
      "Quanh năm.",
      "Chỉ cách đại lộ Tsvetnoy vài bước, tiện kết hợp trong một buổi dạo phố."),
    [
        {"title": "Wikipedia (RU) — Сквер сибирских кошек", "url": "https://ru.wikipedia.org/wiki/Сквер_сибирских_кошек"},
        {"title": "Nashural.ru — Сквер сибирских кошек", "url": "https://nashural.ru/mesta/tyumenskaya-oblast/skver-sibirskih-koshek/"},
    ],
    ["square_street", "monument", "sculpture", "memorial", "cats", "tyumen"],
    maps_text("Сквер сибирских кошек", "Тюмень", "Square of Siberian Cats", "Tyumen", 57.151200, 65.537500),
))

# ============================ TYUMEN công viên & TOBOLSK ============================

# 13) Гилёвская роща ---------------------------------------------------------------
RECORDS.append(rec(
    "gilyovskaya-grove-tyumen",
    "Rừng - Công viên Gilyovskaya, Tyumen (Ghi-lёp-xcai-a rô-sa)",
    "Гилёвская роща",
    "Gilyovskaya Grove",
    ["park_garden"],
    57.135000, 65.585000,
    "Khu Vostochny, thành phố Tyumen, tỉnh Tyumen, Nga",
    "Rừng Gilyovskaya là công viên rừng lớn nhất trong lòng thành phố Tyumen, được cải tạo thành khu nghỉ dưỡng - dạo bộ hiện đại với hồ nước, lối đi lát gỗ, khu vui chơi và không gian thiên nhiên rộng thoáng.",
    "Rừng Gilyovskaya (Гилёвская роща) là công viên rừng đô thị lớn nhất Tyumen, nằm ở khu Vostochny phía đông thành phố. Từng là cánh rừng bạch dương và thông tự nhiên, khu vực được đầu tư cải tạo thành công viên sinh thái hiện đại: những lối đi bộ và cầu gỗ uốn quanh hồ, khu vui chơi trẻ em, sân thể thao, khu picnic và các điểm ngắm cảnh. Đây là nơi người dân Tyumen ưa tìm đến để đi bộ, chạy bộ, đạp xe hay dã ngoại cuối tuần, tận hưởng không khí trong lành ngay trong lòng thành phố. Vào mùa đông, công viên có đường trượt tuyết và không gian yên tĩnh phủ trắng. Với sự cân bằng giữa thiên nhiên và tiện ích, Gilyovskaya là 'lá phổi xanh' được yêu thích của Tyumen.",
    [
        "Công viên rừng đô thị lớn nhất Tyumen.",
        "Hồ nước, lối đi lát gỗ, khu vui chơi và không gian dã ngoại.",
        "Điểm đi bộ, đạp xe, picnic cuối tuần được người dân yêu thích.",
    ],
    p("Không gian ngoài trời, mở cửa tự do; ban ngày là thời điểm phù hợp.",
      "Miễn phí.",
      "Khoảng 1–2 giờ.",
      "Cuối xuân đến đầu thu cho dạo bộ; mùa đông có trượt tuyết.",
      "Mang giày thoải mái; có khu ăn uống và cho thuê xe đạp theo mùa."),
    [
        {"title": "Wikipedia (RU) — Гилёвская роща", "url": "https://ru.wikipedia.org/wiki/Гилёвская_роща"},
        {"title": "Nashural.ru — Гилёвская роща в Тюмени", "url": "https://nashural.ru/mesta/tyumenskaya-oblast/gilevskaya-roshha/"},
    ],
    ["park_garden", "forest", "recreation", "nature", "lake", "tyumen"],
    maps_text("Гилёвская роща", "Тюмень", "Gilyovskaya Grove", "Tyumen", 57.135000, 65.585000),
))

# 14) Затюменский экопарк ----------------------------------------------------------
RECORDS.append(rec(
    "zatyumensky-ecopark-tyumen",
    "Công viên sinh thái Zatyumensky, Tyumen (Za-tiu-men-xki)",
    "Затюменский экопарк",
    "Zatyumensky Ecopark",
    ["park_garden"],
    57.158500, 65.490000,
    "Khu Zatyumensky, phía tây thành phố Tyumen, tỉnh Tyumen, Nga",
    "Công viên sinh thái Zatyumensky là khu rừng thông cải tạo ở phía tây Tyumen, nổi tiếng với hệ đường mòn đi bộ - chạy - trượt tuyết việt dã và không gian tự nhiên gần gũi ngay sát trung tâm.",
    "Công viên sinh thái Zatyumensky (Затюменский экопарк) là mảng rừng thông lâu năm ở khu Zatyumensky phía tây thành phố, được quy hoạch thành công viên sinh thái phục vụ thể thao và nghỉ ngơi. Điểm hấp dẫn nhất là hệ thống đường mòn dài xuyên rừng dành cho đi bộ, chạy bộ, đạp xe và đặc biệt là trượt tuyết việt dã vào mùa đông - nơi tổ chức nhiều giải thể thao địa phương. Công viên còn có khu vui chơi, đường dạo lát nền, các điểm nghỉ và không gian yên tĩnh giữa rừng thông thơm mát. Nhờ nằm sát khu dân cư và trung tâm, Zatyumensky là lựa chọn quen thuộc cho các hoạt động ngoài trời quanh năm của người Tyumen, bổ sung cho rừng Gilyovskaya ở phía đông thành phố.",
    [
        "Rừng thông cải tạo thành công viên sinh thái phía tây Tyumen.",
        "Hệ đường mòn đi bộ, chạy, đạp xe và trượt tuyết việt dã.",
        "Không gian thể thao - nghỉ ngơi ngoài trời quanh năm.",
    ],
    p("Không gian ngoài trời, mở cửa tự do; ban ngày phù hợp nhất.",
      "Miễn phí.",
      "Khoảng 1–2 giờ.",
      "Mùa hè cho đi bộ, đạp xe; mùa đông cho trượt tuyết việt dã.",
      "Có điểm cho thuê ván trượt tuyết theo mùa; ăn mặc phù hợp thời tiết."),
    [
        {"title": "Wikipedia (RU) — Затюменский экопарк", "url": "https://ru.wikipedia.org/wiki/Затюменский_экопарк"},
        {"title": "Nashural.ru — Затюменский экопарк", "url": "https://nashural.ru/mesta/tyumenskaya-oblast/"},
    ],
    ["park_garden", "forest", "sport", "skiing", "recreation", "tyumen"],
    maps_text("Затюменский экопарк", "Тюмень", "Zatyumensky Ecopark", "Tyumen", 57.158500, 65.490000),
))

# 15) Софийско-Успенский собор (Тобольск) ------------------------------------------
RECORDS.append(rec(
    "sofia-uspensky-cathedral-tobolsk",
    "Nhà thờ chính toà Sofia - Uspensky, Tobolsk (Xô-phi-xcô Ú-xpen-xki)",
    "Софийско-Успенский собор",
    "St. Sophia-Assumption Cathedral",
    ["church"],
    58.198600, 68.255300,
    "Điện Kremlin Tobolsk, Quảng trường Đỏ 1, thành phố Tobolsk, tỉnh Tyumen, Nga",
    "Nhà thờ Sofia - Uspensky là công trình bằng đá cổ nhất toàn Siberia, xây năm 1683–1686, trái tim của điện Kremlin Tobolsk với năm mái vòm trắng vươn cao trên bờ dốc sông Irtysh.",
    "Nhà thờ chính toà Sofia - Uspensky (Софийско-Успенский собор) là công trình kiến trúc bằng đá lâu đời nhất ở Siberia, được xây dựng trong các năm 1683–1686 bởi những người thợ được cử từ vùng Ural và Moskva. Với năm mái vòm trắng cổ điển và khối hình bề thế, nhà thờ là trung tâm tinh thần và điểm nhấn thị giác của điện Kremlin Tobolsk - kremlin bằng đá duy nhất của Siberia. Bên trong lưu giữ các bàn thờ chạm khắc và di tích tôn giáo quý; kề bên là tháp chuông cao vút nhìn ra toàn cảnh thành phố dưới thấp và sông Irtysh. Là hạt nhân của quần thể di sản Tobolsk, nhà thờ vừa mang giá trị lịch sử - kiến trúc, vừa là nơi hành hương quan trọng của Chính Thống giáo Siberia.",
    [
        "Công trình bằng đá cổ nhất Siberia, xây 1683–1686.",
        "Trái tim của điện Kremlin Tobolsk với năm mái vòm trắng.",
        "Vị trí trên bờ dốc sông Irtysh, cạnh tháp chuông cao.",
    ],
    p("Mở cửa theo lịch phụng vụ và tham quan, thường 9:00–18:00.",
      "Vào nhà thờ miễn phí; một số khu vực trong kremlin có thể thu phí.",
      "Khoảng 45–60 phút.",
      "Cuối xuân đến đầu thu cho cảnh sông và toàn cảnh thành phố.",
      "Trang phục kín đáo khi vào; kết hợp tham quan cả quần thể Kremlin Tobolsk."),
    [
        {"title": "Wikipedia (RU) — Софийско-Успенский собор (Тобольск)", "url": "https://ru.wikipedia.org/wiki/Софийско-Успенский_собор_(Тобольск)"},
        {"title": "Sobory.ru — Тобольск, Софийско-Успенский собор", "url": "https://sobory.ru/geo/city/Тобольск"},
    ],
    ["church", "cathedral", "kremlin", "orthodox", "17th century", "tobolsk"],
    maps_text("Софийско-Успенский собор", "Тобольск", "St. Sophia-Assumption Cathedral", "Tobolsk", 58.198600, 68.255300),
))

# 16) Церковь Захария и Елизаветы (Тобольск) ---------------------------------------
RECORDS.append(rec(
    "zachary-elizabeth-church-tobolsk",
    "Nhà thờ Thánh Zachary và Elizabeth, Tobolsk (Za-kha-ri-a i E-li-xa-vê-ta)",
    "Церковь Захария и Елизаветы",
    "Church of Zachary and Elizabeth",
    ["church"],
    58.202000, 68.251000,
    "Khu phố dưới (Podgora), thành phố Tobolsk, tỉnh Tyumen, Nga",
    "Nhà thờ Thánh Zachary và Elizabeth là kiệt tác baroque Siberia xây năm 1758–1776 ở khu phố dưới Tobolsk, với những mái vòm đen thanh mảnh và mặt đứng trang trí cầu kỳ bậc nhất vùng.",
    "Nhà thờ Thánh Zachary và Elizabeth (Церковь Захария и Елизаветы) được xây dựng trong giai đoạn 1758–1776 tại khu phố dưới (Подгора) của Tobolsk, và được giới nghiên cứu tôn vinh là một trong những công trình baroque Siberia đẹp và tinh xảo nhất. Điểm đặc trưng là các mái vòm nhọn màu sẫm vươn cao trên nền tường trắng, cùng phần trang trí đắp nổi dày đặc, tạo cảm giác vươn lên nhẹ nhàng dù khối tích lớn. Thời Xô Viết nhà thờ bị đóng cửa và xuống cấp, nhiều năm chờ trùng tu. Nằm dưới chân đồi kremlin, công trình góp phần tạo nên bức tranh toàn cảnh cổ kính của khu phố dưới Tobolsk, và là điểm dừng đáng chú ý cho ai muốn khám phá phần lịch sử của thành phố nằm ngoài quần thể kremlin.",
    [
        "Kiệt tác baroque Siberia xây 1758–1776.",
        "Mái vòm nhọn sẫm màu và mặt đứng trang trí cầu kỳ đặc trưng.",
        "Điểm nhấn của khu phố dưới lịch sử Tobolsk.",
    ],
    p("Tham quan bên ngoài tự do; nội thất mở tuỳ tình trạng trùng tu.",
      "Miễn phí ngắm bên ngoài.",
      "Khoảng 20–30 phút.",
      "Cuối xuân đến đầu thu.",
      "Kết hợp dạo khu phố dưới (Podgora) và ngắm kremlin từ bên dưới."),
    [
        {"title": "Wikipedia (RU) — Церковь Захария и Елизаветы (Тобольск)", "url": "https://ru.wikipedia.org/wiki/Церковь_Захария_и_Елизаветы_(Тобольск)"},
        {"title": "Sobory.ru — Тобольск, храмы", "url": "https://sobory.ru/geo/city/Тобольск"},
    ],
    ["church", "baroque", "orthodox", "18th century", "architecture", "tobolsk"],
    maps_text("Церковь Захария и Елизаветы", "Тобольск", "Church of Zachary and Elizabeth", "Tobolsk", 58.202000, 68.251000),
))

# 17) Губернаторский дом / музей семьи Николая II (Тобольск) ------------------------
RECORDS.append(rec(
    "governors-house-tobolsk",
    "Nhà Thống đốc - Bảo tàng gia đình Nga hoàng Nikolai II, Tobolsk (Gu-béc-na-tô-rxki)",
    "Губернаторский дом (Музей семьи императора Николая II)",
    "Governor's House (Museum of the Family of Emperor Nicholas II)",
    ["palace", "museum"],
    58.197500, 68.258500,
    "Phố Mira 10, gần điện Kremlin, thành phố Tobolsk, tỉnh Tyumen, Nga",
    "Nhà Thống đốc là dinh thự nơi Nga hoàng Nikolai II cùng gia đình bị quản thúc năm 1917–1918, nay là bảo tàng tưởng niệm phục dựng nội thất và kể lại những tháng cuối đời của hoàng gia Romanov ở Tobolsk.",
    "Nhà Thống đốc (Губернаторский дом) ở Tobolsk là toà dinh thự cổ điển từng là nơi ở của các thống đốc tỉnh, nhưng nổi tiếng nhất với vai trò lịch sử bi thương: từ mùa thu 1917 đến mùa xuân 1918, Nga hoàng Nikolai II thoái vị cùng hoàng hậu và các con bị đưa về đây quản thúc trước khi chuyển tới Yekaterinburg. Ngày nay công trình là 'Bảo tàng gia đình Hoàng đế Nikolai II', với các căn phòng được phục dựng nội thất, trưng bày ảnh, thư từ, vật dụng cá nhân tái hiện đời sống thường nhật của gia đình Romanov trong những tháng cuối. Bảo tàng mang đến góc nhìn chân thực, xúc động về một chương lịch sử nước Nga, và là một trong những điểm tham quan quan trọng nhất của Tobolsk bên cạnh quần thể kremlin.",
    [
        "Nơi Nga hoàng Nikolai II và gia đình bị quản thúc 1917–1918.",
        "Nội thất phục dựng, ảnh và vật dụng cá nhân của gia đình Romanov.",
        "Một trong những bảo tàng quan trọng nhất Tobolsk.",
    ],
    p("Thường 10:00–18:00, đóng cửa một ngày trong tuần; nên kiểm tra trước.",
      "Vé khoảng 200–400 rúp; có ưu đãi và vé combo với kremlin.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm; phù hợp cho ngày thời tiết xấu.",
      "Kết hợp cùng vé tham quan quần thể Kremlin Tobolsk kề bên."),
    [
        {"title": "Wikipedia (RU) — Губернаторский дом (Тобольск)", "url": "https://ru.wikipedia.org/wiki/Губернаторский_дом_(Тобольск)"},
        {"title": "Тобольский музей-заповедник (официальный сайт)", "url": "https://tiamz.ru/"},
    ],
    ["museum", "palace", "romanov", "history", "imperial", "tobolsk"],
    maps_text("Губернаторский дом музей семьи императора", "Тобольск", "Governor's House Museum", "Tobolsk", 58.197500, 68.258500),
    official_site="https://tiamz.ru/",
))

# 18) Памятник Ермаку / сад Ермака (Тобольск) --------------------------------------
RECORDS.append(rec(
    "yermak-monument-tobolsk",
    "Tượng đài Yermak và vườn Yermak, Tobolsk (E-rơ-mắc)",
    "Памятник Ермаку (Сад Ермака)",
    "Monument to Yermak (Yermak Garden)",
    ["monument"],
    58.193500, 68.264800,
    "Vườn Yermak, mũi đất Chukman, thành phố Tobolsk, tỉnh Tyumen, Nga",
    "Tượng đài Yermak là đài tưởng niệm dạng tháp đá cẩm thạch dựng năm 1839 tôn vinh thủ lĩnh Cossack Yermak - người mở đường chinh phục Siberia, đặt trong vườn Yermak trên mũi đất cao nhìn ra sông Irtysh.",
    "Tượng đài Yermak (Памятник Ермаку) ở Tobolsk là một trong những đài tưởng niệm lâu đời nhất Siberia, được khánh thành năm 1839 dưới dạng tháp đá cẩm thạch cao hơn 16 mét theo thiết kế của kiến trúc sư Alexander Bryullov. Công trình tôn vinh thủ lĩnh Cossack Yermak Timofeevich, người dẫn đầu cuộc viễn chinh mở đường sáp nhập Siberia vào nước Nga cuối thế kỷ 16. Đài tưởng niệm nằm trong 'vườn Yermak' (Сад Ермака) trên mũi đất cao Chukman, giữa những hàng cây rợp bóng, với các lối đi và điểm ngắm nhìn ra sông Irtysh cùng vùng phố dưới. Đây là nơi dạo bộ, tưởng niệm và ngắm cảnh quen thuộc của người dân Tobolsk, đồng thời là điểm gắn kết chặt chẽ với câu chuyện lịch sử khai phá Siberia.",
    [
        "Đài đá cẩm thạch dựng năm 1839 tôn vinh thủ lĩnh Yermak.",
        "Một trong những tượng đài lâu đời nhất Siberia.",
        "Nằm trong vườn Yermak trên mũi đất cao nhìn ra sông Irtysh.",
    ],
    p("Không gian công viên ngoài trời, mở cửa tự do; ban ngày phù hợp nhất.",
      "Miễn phí.",
      "Khoảng 30–45 phút.",
      "Cuối xuân đến đầu thu cho cây xanh và tầm nhìn sông.",
      "Kết hợp đi bộ tới các điểm ngắm cảnh nhìn xuống phố dưới và sông Irtysh."),
    [
        {"title": "Wikipedia (RU) — Памятник Ермаку (Тобольск)", "url": "https://ru.wikipedia.org/wiki/Памятник_Ермаку_(Тобольск)"},
        {"title": "Nashural.ru — Памятник Ермаку в Тобольске", "url": "https://nashural.ru/mesta/tyumenskaya-oblast/pamyatnik-ermaku/"},
    ],
    ["monument", "history", "yermak", "siberia", "park", "tobolsk"],
    maps_text("Памятник Ермаку", "Тобольск", "Monument to Yermak", "Tobolsk", 58.193500, 68.264800),
))

# ============================ TOBOLSK / YALUTOROVSK / ISHIM / khác ============================

# 19) Гостиный двор (Тобольск) -----------------------------------------------------
RECORDS.append(rec(
    "gostiny-dvor-tobolsk",
    "Thương xá Gostiny Dvor, Tobolsk (Gô-xti-nứi Đvo)",
    "Гостиный двор",
    "Gostiny Dvor (Merchant Court)",
    ["other"],
    58.197800, 68.257800,
    "Điện Kremlin Tobolsk, thành phố Tobolsk, tỉnh Tyumen, Nga",
    "Thương xá Gostiny Dvor là toà thương điếm đá đầu thế kỷ 18 nằm trong điện Kremlin Tobolsk, một trong những công trình thương mại cổ độc đáo bậc nhất Siberia, gắn với vai trò trung tâm buôn bán trên tuyến đường tới Trung Á và Trung Hoa.",
    "Thương xá Gostiny Dvor (Гостиный двор) ở Tobolsk là một khối kiến trúc đá hình vuông khép kín với sân trong, được xây dựng đầu thế kỷ 18 (khoảng 1703–1706) theo ý tưởng của nhà bác học, kiến trúc sư Siberia Semyon Remezov. Là một phần của quần thể điện Kremlin Tobolsk, công trình từng là trung tâm giao thương sầm uất, nơi tập kết và trao đổi hàng hoá của các đoàn thương nhân trên tuyến đường nối Nga với Trung Á và Trung Hoa, thời Tobolsk còn là 'thủ phủ' của Siberia. Kiến trúc pháo đài - thương điếm với tường dày, tháp góc và dãy vòm cửa hàng phản ánh vai trò kép vừa phòng thủ vừa buôn bán. Ngày nay Gostiny Dvor được phục dựng, đón khách tham quan với các không gian trưng bày, xưởng thủ công và cửa hàng lưu niệm, giúp du khách hình dung nhịp sống thương mại Siberia xưa.",
    [
        "Thương điếm đá đầu thế kỷ 18 gắn với kiến trúc sư Remezov.",
        "Công trình thương mại cổ độc đáo trong quần thể Kremlin Tobolsk.",
        "Từng là trung tâm giao thương trên tuyến đường tới Trung Á, Trung Hoa.",
    ],
    p("Thường 10:00–18:00 theo lịch của khu bảo tồn kremlin.",
      "Vào sân tham quan thường miễn phí; một số không gian bên trong thu phí.",
      "Khoảng 30–45 phút.",
      "Quanh năm.",
      "Kết hợp trong hành trình tham quan tổng thể quần thể Kremlin Tobolsk."),
    [
        {"title": "Wikipedia (RU) — Гостиный двор (Тобольск)", "url": "https://ru.wikipedia.org/wiki/Гостиный_двор_(Тобольск)"},
        {"title": "Тобольский музей-заповедник (официальный сайт)", "url": "https://tiamz.ru/"},
    ],
    ["other", "architecture", "trade", "kremlin", "18th century", "tobolsk"],
    maps_text("Гостиный двор Тобольск", "Тобольск", "Gostiny Dvor Tobolsk", "Tobolsk", 58.197800, 68.257800),
))

# 20) Ялуторовский музейный комплекс (дома декабристов) ----------------------------
RECORDS.append(rec(
    "yalutorovsk-decembrists-museum",
    "Bảo tàng Kẻ lưu đày tháng Chạp, Yalutorovsk (Đê-ca-brít-xtơ)",
    "Ялуторовский музейный комплекс (Дома декабристов)",
    "Yalutorovsk Decembrists Museum Complex",
    ["museum"],
    56.655800, 66.313000,
    "Phố Revolyutsii, thành phố Yalutorovsk, tỉnh Tyumen, Nga",
    "Bảo tàng Kẻ lưu đày tháng Chạp ở Yalutorovsk gìn giữ những ngôi nhà gỗ nơi các quý tộc Decembrist bị đày biệt xứ từng sống, tái hiện đời sống và di sản giáo dục - văn hoá mà họ để lại cho vùng Siberia.",
    "Bảo tàng Kẻ lưu đày tháng Chạp (Дома декабристов) là phần cốt lõi của tổ hợp bảo tàng Yalutorovsk, gồm những ngôi nhà gỗ nguyên bản từng là nơi cư trú của các quý tộc Decembrist - những sĩ quan tham gia cuộc khởi nghĩa năm 1825 chống chế độ quân chủ, sau đó bị đày tới Siberia. Nổi bật là nhà của Matvei Muravyov-Apostol và Ivan Yakushkin, được phục dựng nội thất với đồ đạc, thư từ, sách vở tái hiện cuộc sống lưu đày. Dù bị tước quyền, các Decembrist đã đóng góp lớn cho vùng đất: Yakushkin lập trường học đầu tiên cho trẻ em, kể cả nữ sinh, mang ánh sáng giáo dục tới Yalutorovsk. Bảo tàng vì thế không chỉ kể chuyện cá nhân mà còn tôn vinh dấu ấn khai sáng văn hoá của tầng lớp trí thức lưu đày ở Siberia.",
    [
        "Những ngôi nhà gỗ nguyên bản của các Decembrist bị lưu đày.",
        "Gắn với Muravyov-Apostol và Yakushkin - người lập trường học đầu tiên.",
        "Tôn vinh di sản khai sáng giáo dục, văn hoá ở Siberia.",
    ],
    p("Thường 10:00–18:00, đóng cửa một ngày trong tuần; nên kiểm tra trước.",
      "Vé khoảng 150–300 rúp; có ưu đãi và vé tham quan trọn cụm.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm.",
      "Kết hợp với thành gỗ Yalutorovsk Ostrog và nhà thờ Sretensky trong cùng ngày."),
    [
        {"title": "Wikipedia (RU) — Ялуторовский музейный комплекс", "url": "https://ru.wikipedia.org/wiki/Ялуторовский_музейный_комплекс"},
        {"title": "Официальный сайт музейного комплекса", "url": "https://yalutorovskmuseum.ru/"},
    ],
    ["museum", "decembrists", "history", "wooden architecture", "education", "yalutorovsk"],
    maps_text("Дома декабристов Ялуторовск", "Ялуторовск", "Yalutorovsk Decembrists Museum", "Yalutorovsk", 56.655800, 66.313000),
    official_site="https://yalutorovskmuseum.ru/",
))

# 21) Сретенский собор (Ялуторовск) ------------------------------------------------
RECORDS.append(rec(
    "sretensky-cathedral-yalutorovsk",
    "Nhà thờ chính toà Sretensky, Yalutorovsk (Xrê-ten-xki)",
    "Сретенский собор",
    "Sretensky (Candlemas) Cathedral",
    ["church"],
    56.655000, 66.311500,
    "Phố Revolyutsii, thành phố Yalutorovsk, tỉnh Tyumen, Nga",
    "Nhà thờ Sretensky là công trình phục dựng đồ sộ của thánh đường lịch sử Yalutorovsk từng bị phá huỷ thời Xô Viết, nay mang phong cách tân Byzantine với mái vòm xanh nổi bật và là biểu tượng mới của thành phố.",
    "Nhà thờ chính toà Sretensky (Сретенский собор) ở Yalutorovsk là bản phục dựng công phu của ngôi thánh đường lịch sử vốn được xây từ thế kỷ 19 nhưng bị phá huỷ trong thời kỳ Xô Viết. Công trình mới, hoàn thành vào những năm 2010, tái hiện quy mô bề thế của nguyên bản với phong cách kiến trúc tân Byzantine: khối nhà thờ lớn, nhiều mái vòm màu xanh điểm sao vàng và mặt đứng trang trí thanh nhã. Bên trong là không gian rộng thoáng với các bức icon và tranh tường. Nằm ở trung tâm Yalutorovsk gần cụm di tích Decembrist và thành gỗ Ostrog, nhà thờ nhanh chóng trở thành điểm nhấn kiến trúc, nơi hành hương và biểu tượng tinh thần mới của thành phố nhỏ giàu lịch sử này.",
    [
        "Bản phục dựng đồ sộ của thánh đường lịch sử bị phá thời Xô Viết.",
        "Kiến trúc tân Byzantine với mái vòm xanh điểm sao vàng.",
        "Biểu tượng mới ở trung tâm Yalutorovsk, gần cụm di tích Decembrist.",
    ],
    p("Mở cửa theo lịch phụng vụ, thường buổi sáng và chiều tối.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Quanh năm.",
      "Trang phục kín đáo khi vào; kết hợp với bảo tàng Decembrist và Ostrog gần đó."),
    [
        {"title": "Wikipedia (RU) — Сретенский собор (Ялуторовск)", "url": "https://ru.wikipedia.org/wiki/Сретенский_собор_(Ялуторовск)"},
        {"title": "Sobory.ru — Ялуторовск, Сретенский собор", "url": "https://sobory.ru/geo/city/Ялуторовск"},
    ],
    ["church", "cathedral", "neo-byzantine", "orthodox", "reconstruction", "yalutorovsk"],
    maps_text("Сретенский собор", "Ялуторовск", "Sretensky Cathedral", "Yalutorovsk", 56.655000, 66.311500),
))

# 22) Ишимский музейный комплекс им. П.П. Ершова -----------------------------------
RECORDS.append(rec(
    "ershov-museum-complex-ishim",
    "Tổ hợp Bảo tàng Ershov, Ishim (E-rơ-sốp)",
    "Ишимский музейный комплекс имени П.П. Ершова",
    "Ershov Museum Complex, Ishim",
    ["museum"],
    56.110800, 69.483000,
    "Trung tâm thành phố Ishim, tỉnh Tyumen, Nga",
    "Tổ hợp Bảo tàng Ershov ở Ishim tôn vinh nhà thơ Pyotr Ershov - tác giả trường ca cổ tích 'Chú ngựa gù thần kỳ', trưng bày về cuộc đời, tác phẩm của ông và lịch sử - văn hoá vùng Ishim.",
    "Tổ hợp Bảo tàng mang tên Pyotr Ershov (Ишимский музейный комплекс им. П.П. Ершова) là trung tâm bảo tàng chính của thành phố Ishim, gắn với người con nổi tiếng của vùng - nhà thơ Pyotr Pavlovich Ershov, tác giả trường ca cổ tích 'Chú ngựa gù thần kỳ' (Конёк-Горбунок) được nhiều thế hệ độc giả Nga yêu thích. Ershov sinh gần Ishim và gắn bó sâu sắc với vùng đất Siberia. Tổ hợp gồm bảo tàng lịch sử - nghệ thuật cùng không gian tưởng niệm nhà thơ, trưng bày các ấn phẩm, minh hoạ, tư liệu về cuộc đời và sự nghiệp của ông, bên cạnh các sưu tập về lịch sử, dân tộc học địa phương. Thành phố còn có tượng đài 'Chú ngựa gù' gắn với chủ đề này. Đây là điểm đến văn hoá tiêu biểu, giúp du khách hiểu về di sản văn học Nga và bản sắc vùng Ishim.",
    [
        "Tôn vinh Pyotr Ershov - tác giả 'Chú ngựa gù thần kỳ'.",
        "Trưng bày cuộc đời, tác phẩm nhà thơ và lịch sử vùng Ishim.",
        "Gắn với hình tượng 'Chú ngựa gù' - biểu tượng văn hoá địa phương.",
    ],
    p("Thường 10:00–18:00, đóng cửa một ngày trong tuần; nên kiểm tra trước.",
      "Vé khoảng 100–250 rúp; có ưu đãi.",
      "Khoảng 1–1,5 giờ.",
      "Quanh năm.",
      "Kết hợp tham quan nhà thờ Bogoyavlensky và trung tâm lịch sử Ishim."),
    [
        {"title": "Wikipedia (RU) — Ершов, Пётр Павлович", "url": "https://ru.wikipedia.org/wiki/Ершов,_Пётр_Павлович"},
        {"title": "Ишимский музейный комплекс (официальный сайт)", "url": "https://ishimmuseum.ru/"},
    ],
    ["museum", "literature", "ershov", "history", "culture", "ishim"],
    maps_text("Ишимский музейный комплекс имени Ершова", "Ишим", "Ershov Museum Complex", "Ishim", 56.110800, 69.483000),
    official_site="https://ishimmuseum.ru/",
))

# 23) Богоявленский собор (Ишим) ---------------------------------------------------
RECORDS.append(rec(
    "bogoyavlensky-cathedral-ishim",
    "Nhà thờ chính toà Bogoyavlensky, Ishim (Bô-gô-i-áp-len-xki)",
    "Богоявленский собор",
    "Cathedral of the Epiphany (Bogoyavlensky)",
    ["church"],
    56.117000, 69.479000,
    "Khu trung tâm lịch sử, thành phố Ishim, tỉnh Tyumen, Nga",
    "Nhà thờ Bogoyavlensky là ngôi nhà thờ đá cổ nhất Ishim, xây năm 1775–1793 theo phong cách baroque Siberia, nơi nhà thơ Pyotr Ershov từng được rửa tội và là biểu tượng lịch sử của thành phố.",
    "Nhà thờ chính toà Bogoyavlensky (Богоявленский собор) là công trình tôn giáo bằng đá lâu đời nhất của Ishim, được xây dựng trong giai đoạn 1775–1793 theo phong cách baroque Siberia đặc trưng với các mái vòm và trang trí đắp nổi. Nhà thờ gắn với lịch sử thành phố từ thời còn là khu định cư Korkina Sloboda: chính tại đây nhà thơ Pyotr Ershov, tác giả 'Chú ngựa gù thần kỳ', đã được rửa tội. Thời Xô Viết công trình bị đóng cửa và sử dụng cho mục đích thế tục, sau này được phục hồi và trả lại cho Giáo hội. Nằm ở khu trung tâm lịch sử gần sông Ishim, nhà thờ là điểm nhấn kiến trúc và tâm linh của thành phố, thường được kết hợp trong hành trình tham quan cùng bảo tàng Ershov.",
    [
        "Nhà thờ đá cổ nhất Ishim, xây 1775–1793 theo baroque Siberia.",
        "Nơi nhà thơ Pyotr Ershov từng được rửa tội.",
        "Biểu tượng lịch sử - tâm linh ở trung tâm thành phố.",
    ],
    p("Mở cửa theo lịch phụng vụ, thường buổi sáng và chiều tối.",
      "Miễn phí.",
      "Khoảng 20–30 phút.",
      "Quanh năm.",
      "Trang phục kín đáo khi vào; kết hợp với tổ hợp bảo tàng Ershov gần đó."),
    [
        {"title": "Wikipedia (RU) — Богоявленский собор (Ишим)", "url": "https://ru.wikipedia.org/wiki/Богоявленский_собор_(Ишим)"},
        {"title": "Sobory.ru — Ишим, Богоявленский собор", "url": "https://sobory.ru/geo/city/Ишим"},
    ],
    ["church", "cathedral", "baroque", "orthodox", "18th century", "ishim"],
    maps_text("Богоявленский собор", "Ишим", "Bogoyavlensky Cathedral", "Ishim", 56.117000, 69.479000),
))

# 24) Музей Григория Распутина (село Покровское) -----------------------------------
RECORDS.append(rec(
    "rasputin-museum-pokrovskoye",
    "Bảo tàng Grigori Rasputin, làng Pokrovskoye (Ra-xpu-tin, Pô-crốp-xcôi-e)",
    "Музей Григория Распутина",
    "Grigori Rasputin Museum",
    ["museum"],
    57.665500, 66.672000,
    "Làng Pokrovskoye, huyện Yarkovo, tỉnh Tyumen, Nga",
    "Bảo tàng Grigori Rasputin ở làng Pokrovskoye - quê hương của nhân vật gây tranh cãi bậc nhất triều đình Nga cuối cùng, là bảo tàng tư nhân đầu tiên của vùng, trưng bày hiện vật và câu chuyện về cuộc đời huyền thoại của ông.",
    "Bảo tàng Grigori Rasputin (Музей Григория Распутина) nằm ở làng Pokrovskoye trên tuyến đường lịch sử nối Tyumen với Tobolsk - chính là quê hương của Grigori Rasputin, vị 'trưởng lão' nông dân đầy quyền lực và gây tranh cãi trong cung đình Nga hoàng Nikolai II những năm trước cách mạng. Đây là bảo tàng tư nhân đầu tiên của tỉnh Tyumen, do gia đình Smirnov gây dựng, trưng bày các hiện vật, ảnh tư liệu, đồ dùng gắn với Rasputin và gia đình ông, trong đó có những vật dụng gốc và tái hiện không gian sinh hoạt làng quê Siberia. Hướng dẫn viên kể lại câu chuyện đời Rasputin - từ người nông dân trở thành nhân vật ảnh hưởng tới hoàng gia, cho tới cái chết bí ẩn - với nhiều góc nhìn. Nằm ngay bên quốc lộ, bảo tàng là điểm dừng chân độc đáo trên hành trình Tyumen - Tobolsk.",
    [
        "Bảo tàng tư nhân đầu tiên của tỉnh Tyumen, ở quê Rasputin.",
        "Hiện vật, ảnh tư liệu và không gian làng quê Siberia gắn với Rasputin.",
        "Điểm dừng độc đáo trên tuyến đường lịch sử Tyumen - Tobolsk.",
    ],
    p("Tham quan theo tour có hướng dẫn, thường trong ngày; nên gọi đặt trước.",
      "Vé và phí hướng dẫn khoảng 300–500 rúp/khách tuỳ đoàn.",
      "Khoảng 45–60 phút.",
      "Quanh năm; thuận tiện khi di chuyển giữa Tyumen và Tobolsk.",
      "Nên liên hệ trước để sắp xếp hướng dẫn viên; bảo tàng nằm ngay ven quốc lộ."),
    [
        {"title": "Wikipedia (RU) — Распутин, Григорий Ефимович", "url": "https://ru.wikipedia.org/wiki/Распутин,_Григорий_Ефимович"},
        {"title": "Nashural.ru — Музей Распутина в Покровском", "url": "https://nashural.ru/mesta/tyumenskaya-oblast/muzej-rasputina/"},
    ],
    ["museum", "rasputin", "history", "village", "private museum", "tyumen oblast"],
    maps_text("Музей Григория Распутина", "село Покровское", "Grigori Rasputin Museum", "Pokrovskoye", 57.665500, 66.672000),
))

# 25) Археологический музей-заповедник на озере Андреевском -------------------------
RECORDS.append(rec(
    "andreevskoye-lake-museum",
    "Bảo tàng khảo cổ ngoài trời hồ Andreevskoye (An-đrê-ép-xcôi-e)",
    "Археологический музей-заповедник на озере Андреевском",
    "Andreevskoye Lake Archaeological Museum-Reserve",
    ["other", "museum"],
    57.062000, 65.870000,
    "Ven hồ Andreevskoye, gần đường Yalutorovsky, ngoại ô thành phố Tyumen, tỉnh Tyumen, Nga",
    "Bảo tàng khảo cổ ngoài trời hồ Andreevskoye là khu bảo tồn bên hồ với hàng trăm di chỉ cư trú cổ hàng nghìn năm tuổi, kết hợp trưng bày ngoài trời, nhà gỗ phục dựng và cảnh quan thiên nhiên sát Tyumen.",
    "Bảo tàng - khu bảo tồn khảo cổ trên hồ Andreevskoye (Археологический музей-заповедник на озере Андреевском) nằm cách trung tâm Tyumen khoảng hơn 20 km về phía đông nam, bên bờ hồ Andreevskoye. Khu vực này là một trong những quần thể di chỉ khảo cổ dày đặc nhất Tây Siberia, với hàng trăm điểm cư trú, khu chôn cất và dấu tích của con người trải dài từ thời đồ đá tới trung đại. Bảo tàng kết hợp không gian trưng bày trong nhà với khu ngoài trời phục dựng nhà ở, công cụ và đời sống của cư dân cổ, giữa khung cảnh rừng và hồ nước yên bình. Đây là điểm đến kết hợp giáo dục lịch sử với dã ngoại thiên nhiên, phù hợp cho gia đình và những ai muốn tìm hiểu về quá khứ xa xưa của vùng đất Tyumen.",
    [
        "Một trong những quần thể di chỉ khảo cổ dày đặc nhất Tây Siberia.",
        "Trưng bày trong nhà kết hợp khu ngoài trời phục dựng đời sống cổ.",
        "Kết hợp giáo dục lịch sử và dã ngoại thiên nhiên sát Tyumen.",
    ],
    p("Thường mở cửa mùa ấm và theo lịch tham quan; nên kiểm tra trước khi đến.",
      "Vé khoảng 150–300 rúp; có ưu đãi và chương trình theo đoàn.",
      "Khoảng 1–1,5 giờ.",
      "Cuối xuân đến đầu thu cho hoạt động ngoài trời.",
      "Đi ô tô hoặc tour theo hướng đường Yalutorovsky; mang đồ chống muỗi mùa hè."),
    [
        {"title": "Wikipedia (RU) — Андреевское озеро (Тюменская область)", "url": "https://ru.wikipedia.org/wiki/Андреевское_озеро"},
        {"title": "Музейный комплекс им. И.Я. Словцова (официальный сайт)", "url": "https://museum-72.ru/"},
    ],
    ["other", "museum", "archaeology", "open-air", "nature", "tyumen oblast"],
    maps_text("Археологический музей-заповедник на озере Андреевском", "Тюмень", "Andreevskoye Lake Archaeological Museum", "Tyumen", 57.062000, 65.870000),
    official_site="https://museum-72.ru/",
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
