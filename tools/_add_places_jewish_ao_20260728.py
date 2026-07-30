# -*- coding: utf-8 -*-
"""_add_places_jewish_ao_20260728.py — VÙNG: Tỉnh tự trị Do Thái (Jewish AO / EAO)
(lần chạy tự động 2026-07-28).

Bối cảnh: jewish-ao.json hiện có 5 địa điểm. Đây là vùng NHỎ, THƯA danh lam. Đợt này
bổ sung 25 địa điểm THẬT SỰ hợp lệ, đa dạng loại hình, để đạt ≥30:
- Birobidzhan (15): Nhà thờ chính toà Благовещенский, nhà thờ gỗ Николая Чудотворца,
  Филармония, Nhà hát rối «Кудесник», Bảo tàng địa phương (краеведческий), Bảo tàng nghệ
  thuật hiện đại, Đài «первым переселенцам», Tượng «Скрипач», Мемориал «Вечный огонь» /
  сквер Победы, Công viên thành phố + hồ, Thư viện Шолом-Алейхема, Площадь Ленина,
  Театральная площадь, Биробиджанский Арбат, Sông Бира & kè dạo bộ.
- Ngoài thành phố (10): Đài-bảo tàng trận Волочаевка (сопка Июнь-Корань), khu nghỉ suối
  nóng Кульдур, thị trấn Облучье, làng Амурзет (bờ Amur), làng Ленинское (bờ Amur),
  hồ Забеловское (cụm Забеловский của заповедник Бастак), hang Лондоковская, đô thị
  Смидович, sông Биджан, làng Николаевка.

TOẠ ĐỘ — xác minh chéo (sobory.ru, Yandex Maps org/geo, fesk.ru, museum.ru, idilesom.com,
ruwiki.ru, waterresources.ru; 2026-07). Kiểm tra phạm vi EAO: lat 47,3–49,4; lon 130–135;
KHÔNG đảo lat/lon; tất cả nằm trong tỉnh. Một số điểm phi-toà-nhà (kè sông, quảng trường,
sông, hồ) dùng toạ độ ĐIỂM MỐC/ĐẠI DIỆN đã ghi rõ. Link bản đồ TRỎ-ĐỊA-ĐIỂM: ưu tiên URL
trang tổ chức Яндекс (maps_org) cho các đối tượng có; còn lại dùng text-search theo tên_ru
+ thành phố, canh giữa theo toạ độ đã kiểm.

Nội dung tiếng Việt NGUYÊN GỐC (paraphrase, KHÔNG dịch/sao chép nguyên văn), có ghi nguồn.

Chạy:  python3 tools/_add_places_jewish_ao_20260728.py
"""
import json, os, datetime, shutil, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY = "2026-07-28"

REGION = "jewish-ao"
REGION_NAME_VI = "Tỉnh tự trị Do Thái"
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
    """Ưu tiên URL trang tổ chức/địa điểm Яндекс (chính xác nhất) + Google text-search."""
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

# 1) Благовещенский кафедральный собор -----------------------------------------
RECORDS.append(rec(
    "blagoveshchensky-cathedral-birobidzhan",
    "Nhà thờ chính toà Truyền Tin (Blagoveshchensky sobor)",
    "Благовещенский кафедральный собор",
    "Annunciation Cathedral (Birobidzhan)",
    ["church"],
    48.794353, 132.927854,
    "Ул. Ленина, 34, thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Nhà thờ chính toà của giáo phận Birobidzhan – ngôi nhà thờ Chính thống bằng đá đầu tiên của Tỉnh tự trị Do Thái, xây năm 2003–2005.",
    "Благовещенский кафедральный собор là ngôi thánh đường Chính thống giáo bằng đá đầu tiên được dựng lên ở Tỉnh tự trị Do Thái – một vùng đất mà lịch sử thế kỷ 20 gắn với người Do Thái nhiều hơn là với Chính thống giáo. Công trình khởi công tháng 4/2003 và được thánh hiến ngày 21/9/2005 bởi vị giám mục đầu tiên của giáo phận Birobidzhan là Iosif. Nhà thờ có hai tầng: hạ đường cung hiến thánh Tông đồ Iakov, còn thượng đường mang tước hiệu Truyền Tin của Đức Mẹ. Với năm mái vòm hành hương màu vàng nổi bật trên nền trời, nội thất được các hoạ sĩ phục chế từ Serpukhov trang trí bích hoạ, đây là điểm nhấn kiến trúc tôn giáo trung tâm của thành phố và là trung tâm đời sống Chính thống giáo của cả tỉnh. Kế bên là toà nhà Quản trị giáo phận và trung tâm xã hội – giáo dục.",
    [
        "Nhà thờ Chính thống bằng đá đầu tiên của Tỉnh tự trị Do Thái.",
        "Kiến trúc hai tầng, năm mái vòm vàng, bích hoạ nội thất.",
        "Trung tâm giáo phận Birobidzhan, thánh hiến năm 2005.",
    ],
    {
        "hours_vi": "Mở cửa hằng ngày theo giờ lễ (thường sáng sớm đến chiều tối); giờ thánh lễ dày hơn vào cuối tuần và ngày lễ.",
        "ticket_vi": "Miễn phí (nhà thờ đang hoạt động).",
        "duration_vi": "Khoảng 20–40 phút.",
        "best_time_vi": "Quanh năm; đẹp nhất vào các dịp lễ lớn của Chính thống giáo.",
        "tips_vi": "Ăn mặc kín đáo; nữ nên mang khăn trùm đầu. Giữ yên lặng, xin phép trước khi chụp ảnh bên trong.",
    },
    [
        {"title": "Соборы.ру — Кафедральный собор Благовещения Пресвятой Богородицы (Биробиджан)", "url": "https://sobory.ru/article/?object=22277"},
        {"title": "РИА Биробиджан — Благовещенский кафедральный собор", "url": "https://riabir.ru/putevod/blagoveshhenskiy-kafedralnyiy-sobor/"},
    ],
    ["cathedral", "orthodox", "birobidzhan", "landmark"],
    maps_text("Благовещенский кафедральный собор", "Биробиджан", "Annunciation Cathedral", "Birobidzhan", 48.794353, 132.927854),
))

# 2) Церковь Николая Чудотворца ------------------------------------------------
RECORDS.append(rec(
    "nikolskaya-church-birobidzhan",
    "Nhà thờ gỗ Thánh Nicholas (Tserkov Nikolaya Chudotvortsa)",
    "Церковь Николая Чудотворца",
    "Church of St. Nicholas the Wonderworker (Birobidzhan)",
    ["church"],
    48.797718, 132.915168,
    "Ул. Шолом-Алейхема, 52, thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Ngôi nhà thờ gỗ nhỏ dựng năm 1998–1999, từng giữ vai trò nhà thờ chính của Birobidzhan trước khi nhà thờ đá Truyền Tin ra đời.",
    "Церковь Николая Чудотворца là một nhà thờ Chính thống bằng gỗ được xây dựng trong hai năm 1998–1999 và thánh hiến ngày 19/12/1999 – đúng ngày lễ Thánh Nikolay. Trong giai đoạn giáo phận Birobidzhan mới thành lập, ngôi nhà thờ gỗ khiêm nhường này từng đóng vai trò nhà thờ chính (собор) của thành phố cho đến khi nhà thờ đá Благовещенский được khánh thành tháng 9/2005. Nằm trên trục phố trung tâm mang tên nhà văn Sholom-Aleichem, với lối kiến trúc gỗ truyền thống Nga cùng mái vòm nhỏ, công trình là một điểm dừng chân yên tĩnh và là chứng nhân cho những bước đầu của đời sống Chính thống giáo tại vùng đất vốn nổi tiếng về văn hoá Do Thái.",
    [
        "Nhà thờ gỗ truyền thống Nga, thánh hiến năm 1999.",
        "Từng là nhà thờ chính của Birobidzhan tới năm 2005.",
        "Nằm trên phố trung tâm Sholom-Aleichem.",
    ],
    {
        "hours_vi": "Mở theo giờ lễ hằng ngày; đông tín hữu hơn vào cuối tuần.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–30 phút.",
        "best_time_vi": "Quanh năm; đặc biệt dịp lễ Thánh Nikolay (19/12).",
        "tips_vi": "Trang phục kín đáo, giữ yên tĩnh; kết hợp dạo bộ dọc phố Sholom-Aleichem gần đó.",
    },
    [
        {"title": "Соборы.ру — Церковь Николая Чудотворца (Биробиджан)", "url": "https://sobory.ru/article/?object=22276"},
    ],
    ["church", "wooden-church", "orthodox", "birobidzhan"],
    maps_text("Церковь Николая Чудотворца", "Биробиджан", "Church of St Nicholas", "Birobidzhan", 48.797718, 132.915168),
))

# 3) Биробиджанская областная филармония ---------------------------------------
RECORDS.append(rec(
    "birobidzhan-philharmonic",
    "Nhạc viện – Nhà hát giao hưởng tỉnh Birobidzhan (Filarmoniya)",
    "Биробиджанская областная филармония",
    "Birobidzhan Regional Philharmonic",
    ["theatre"],
    48.786869, 132.929777,
    "Пр. 60-летия СССР, 14 (Quảng trường Nhà hát), thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Trung tâm âm nhạc chính của tỉnh, thành lập năm 1977, với phòng hoà nhạc 674 chỗ ngay trên Quảng trường Nhà hát.",
    "Биробиджанская областная филармония là thiết chế biểu diễn âm nhạc trung tâm của Tỉnh tự trị Do Thái. Được thành lập năm 1977, đến năm 1984 nhạc viện dời về toà nhà hiện tại trên Quảng trường Nhà hát (Театральная площадь), sở hữu phòng hoà nhạc khoảng 674 ghế. Chương trình ở đây trải rộng từ nhạc hàn lâm, hoà tấu dân gian đến các đêm nhạc Do Thái (klezmer) và những sự kiện văn hoá – lễ hội mang bản sắc riêng của vùng. Nằm giữa quảng trường có đài phun nước và bồn hoa trang trí, cùng tượng «Nghệ sĩ vĩ cầm» kế bên, filармония là hạt nhân của không gian văn hoá – giải trí công cộng ở trung tâm Birobidzhan.",
    [
        "Trung tâm âm nhạc của tỉnh, thành lập 1977, hội trường ~674 chỗ.",
        "Chương trình đa dạng: hàn lâm, dân gian, nhạc Do Thái klezmer.",
        "Toạ lạc trên Quảng trường Nhà hát trung tâm thành phố.",
    ],
    {
        "hours_vi": "Phòng vé thường mở thứ Ba–thứ Sáu 12:00–19:00 (nghỉ trưa); biểu diễn theo lịch mùa.",
        "ticket_vi": "Có phí theo từng chương trình; xem lịch và giá trên trang chính thức.",
        "duration_vi": "Một buổi diễn khoảng 1,5–2 giờ.",
        "best_time_vi": "Mùa diễn thu – xuân; kiểm tra áp phích trước khi tới.",
        "tips_vi": "Đặt vé trước cho các đêm nhạc lớn; kết hợp dạo Quảng trường Nhà hát và chụp ảnh tượng «Nghệ sĩ vĩ cầm».",
    },
    [
        {"title": "Культура.РФ — Биробиджанская областная филармония", "url": "https://www.culture.ru/institutes/53698/birobidzhanskaya-oblastnaya-filarmoniya"},
        {"title": "Яндекс Карты — Биробиджанская областная филармония", "url": "https://yandex.ru/maps/org/birobidzhanskaya_oblastnaya_filarmoniya/1043542327/"},
    ],
    ["philharmonic", "concert-hall", "music", "birobidzhan"],
    maps_org("https://yandex.ru/maps/org/birobidzhanskaya_oblastnaya_filarmoniya/1043542327/", "Birobidzhan Regional Philharmonic", "Birobidzhan"),
    official_site="https://www.birfil.ru/",
))

# 4) Театр кукол «Кудесник» ----------------------------------------------------
RECORDS.append(rec(
    "kudesnik-puppet-theatre-birobidzhan",
    "Nhà hát múa rối «Kudesnik» (Teatr kukol Kudesnik)",
    "Театр кукол «Кудесник»",
    "Kudesnik Puppet Theatre",
    ["theatre"],
    48.798508, 132.917622,
    "Швейный переулок, 6Б, thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Nhà hát múa rối duy nhất của tỉnh, điểm giải trí quen thuộc cho gia đình và trẻ em ở Birobidzhan.",
    "Театр кукол «Кудесник» là nhà hát múa rối duy nhất của Tỉnh tự trị Do Thái, chuyên dàn dựng các vở diễn dành cho thiếu nhi và gia đình dựa trên truyện cổ tích Nga, dân gian thế giới và những câu chuyện mang màu sắc địa phương. Sân khấu rối nhỏ ấm cúng đặt trong một toà nhà ở Швейный переулок, là nơi thường xuyên tổ chức các buổi diễn cuối tuần, chương trình dịp lễ và hoạt động giáo dục nghệ thuật cho trẻ. Với một thành phố nhỏ như Birobidzhan, «Kudesnik» là địa chỉ văn hoá thân thuộc, giúp du khách đi cùng con nhỏ có thêm lựa chọn trải nghiệm.",
    [
        "Nhà hát múa rối duy nhất của Tỉnh tự trị Do Thái.",
        "Chương trình hướng tới thiếu nhi và gia đình.",
        "Không gian sân khấu rối ấm cúng, thân thiện.",
    ],
    {
        "hours_vi": "Biểu diễn theo lịch (thường cuối tuần và dịp lễ); phòng vé mở theo giờ hành chính.",
        "ticket_vi": "Vé giá bình dân theo suất diễn.",
        "duration_vi": "Một vở khoảng 40–60 phút.",
        "best_time_vi": "Cuối tuần, kỳ nghỉ học và dịp lễ thiếu nhi.",
        "tips_vi": "Phù hợp cho gia đình có trẻ nhỏ; nên hỏi lịch diễn trước vì suất diễn thay đổi theo tuần.",
    },
    [
        {"title": "Яндекс Карты — Театр кукол «Кудесник» (Биробиджан)", "url": "https://yandex.ru/maps/org/kudesnik/1094333710/"},
    ],
    ["puppet-theatre", "family", "kids", "birobidzhan"],
    maps_org("https://yandex.ru/maps/org/kudesnik/1094333710/", "Kudesnik Puppet Theatre", "Birobidzhan"),
))

# 5) Областной краеведческий музей ---------------------------------------------
RECORDS.append(rec(
    "regional-lore-museum-birobidzhan",
    "Bảo tàng địa phương tỉnh Birobidzhan (Kraevedcheskiy muzey)",
    "Областной краеведческий музей г. Биробиджана",
    "Regional Museum of Local Lore (Birobidzhan)",
    ["museum"],
    48.793176, 132.928569,
    "Ул. Ленина, 25, thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Bảo tàng lịch sử – thiên nhiên chủ lực của tỉnh, mở cửa từ năm 1945, giới thiệu quá trình khai phá vùng Amur và lịch sử người Do Thái tới định cư.",
    "Областной краеведческий музей là bảo tàng tổng hợp chủ lực của Tỉnh tự trị Do Thái. Được quyết định thành lập năm 1944 và đón khách lần đầu tháng 6/1945, bảo tàng tập hợp các gian trưng bày về thiên nhiên vùng đất (động – thực vật, khoáng vật của rặng Tiểu Hưng An), về quá khứ khảo cổ, về lịch sử người Nga khai phá lưu vực Amur, và đặc biệt là câu chuyện những đoàn di dân Do Thái đến lập nghiệp từ cuối thập niên 1920 tạo nên vùng tự trị độc nhất vô nhị này. Bộ sưu tập gồm hiện vật dân tộc học, tài liệu, ảnh tư liệu và các phục dựng sinh động, giúp du khách hiểu bối cảnh hình thành «Birobidzhan» – một thử nghiệm lịch sử về quê hương của người Do Thái ở Viễn Đông Xô-viết.",
    [
        "Bảo tàng tổng hợp lâu đời nhất tỉnh, mở cửa từ 1945.",
        "Trưng bày thiên nhiên, khảo cổ, khai phá Amur và lịch sử di dân Do Thái.",
        "Điểm khởi đầu lý tưởng để hiểu vùng tự trị độc đáo này.",
    ],
    {
        "hours_vi": "Mở cửa các ngày trong tuần theo giờ hành chính (thường nghỉ đầu tuần); nên kiểm tra trước.",
        "ticket_vi": "Vé vào cửa mức bình dân; có thể phụ phí cho triển lãm đặc biệt.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Quanh năm; tiện ghép với các điểm trung tâm trên phố Lenin.",
        "tips_vi": "Cùng toà nhà (Ленина 25) còn có Thư viện khoa học tỉnh Sholom-Aleichem – có thể tham quan liền mạch.",
    },
    [
        {"title": "Культура.РФ — Областной краеведческий музей г. Биробиджана", "url": "https://www.culture.ru/institutes/12091/oblastnoi-kraevedcheskii-muzei-g-birobidzhana"},
        {"title": "Trang chính thức bảo tàng (okm79.ru)", "url": "https://okm79.ru/"},
    ],
    ["museum", "local-history", "ethnography", "birobidzhan"],
    maps_org("https://yandex.ru/maps/org/krayevedcheskiy_muzey/1003884734/", "Regional Museum of Local Lore", "Birobidzhan"),
    official_site="https://okm79.ru/",
))

# 6) Музей современного искусства ЕАО ------------------------------------------
RECORDS.append(rec(
    "contemporary-art-museum-eao",
    "Bảo tàng Nghệ thuật Đương đại tỉnh (Muzey sovremennogo iskusstva)",
    "Музей современного искусства Еврейской автономной области",
    "Museum of Contemporary Art of the Jewish AO",
    ["museum"],
    48.789534, 132.931120,
    "Ул. Шолом-Алейхема, 11 (Cung Văn hoá thành phố – GDK), thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Bảo tàng nghệ thuật hiện đại của tỉnh, nổi tiếng với bộ sưu tập tranh chủ đề Cựu Ước độc đáo.",
    "Музей современного искусства của Tỉnh tự trị Do Thái là điểm đến nghệ thuật đặc sắc đặt trong Cung Văn hoá thành phố (ГДК) trên phố Sholom-Aleichem. Bảo tàng lưu giữ một bộ sưu tập tranh lấy cảm hứng từ các mô-típ và câu chuyện trong Kinh Cựu Ước – một chủ đề gắn bó mật thiết với bản sắc Do Thái của vùng đất, được xem là độc nhất trong hệ thống bảo tàng Nga. Bên cạnh đó là các tác phẩm hội hoạ, đồ hoạ và điêu khắc của nghệ sĩ đương đại vùng Viễn Đông cùng những triển lãm luân phiên. Đây là nơi giao thoa giữa nghệ thuật hiện đại và di sản văn hoá – tôn giáo Do Thái, mang lại một góc nhìn khác biệt so với các bảo tàng lịch sử truyền thống.",
    [
        "Bộ sưu tập tranh chủ đề Cựu Ước được xem là độc nhất ở Nga.",
        "Trưng bày nghệ thuật đương đại vùng Viễn Đông.",
        "Đặt trong Cung Văn hoá thành phố trên phố Sholom-Aleichem.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ hành chính các ngày trong tuần; nên kiểm tra trước khi tới.",
        "ticket_vi": "Vé vào cửa mức bình dân.",
        "duration_vi": "Khoảng 45–60 phút.",
        "best_time_vi": "Quanh năm; hỏi lịch triển lãm chuyên đề đang diễn ra.",
        "tips_vi": "Nằm ngay trung tâm, dễ ghép với phố đi bộ Arbat và Quảng trường Nhà hát.",
    },
    [
        {"title": "Яндекс Карты — Музей современного искусства (Биробиджан)", "url": "https://yandex.ru/maps/org/muzey_sovremennogo_iskusstva/1380266398/"},
    ],
    ["museum", "contemporary-art", "jewish-culture", "birobidzhan"],
    maps_org("https://yandex.ru/maps/org/muzey_sovremennogo_iskusstva/1380266398/", "Museum of Contemporary Art", "Birobidzhan"),
))

# 7) Памятник первым переселенцам ----------------------------------------------
RECORDS.append(rec(
    "first-settlers-monument-birobidzhan",
    "Đài tưởng niệm những di dân đầu tiên (Pamyatnik pervym pereselentsam)",
    "Памятник первым переселенцам",
    "Monument to the First Settlers",
    ["monument"],
    48.792943, 132.933577,
    "Привокзальная площадь (cạnh ga đường sắt), thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Tượng đồng khắc hoạ một gia đình di dân Do Thái ngồi trên xe ngựa, đặt ngay quảng trường trước nhà ga – biểu tượng cho những người đầu tiên đến khai phá vùng đất.",
    "Памятник первым переселенцам là một trong những biểu tượng cảm động nhất của Birobidzhan. Nhóm tượng đồng khắc hoạ hình ảnh một gia đình di dân trên chiếc xe ngựa chất đầy hành lý – bao tải, đồ đạc và cả ấm samovar – gợi lại làn sóng người Do Thái từ nhiều nơi đổ về lập nghiệp ở vùng Viễn Đông từ cuối thập niên 1920. Tác phẩm được đặt ở Quảng trường Nhà ga, ngay nơi những đoàn tàu năm xưa đưa các gia đình tới miền đất mới. Đây là điểm chụp ảnh và tưởng niệm gắn liền với câu chuyện hình thành Tỉnh tự trị Do Thái, thường được ghé thăm cùng đài Menorah và tượng nhà văn Sholom-Aleichem gần đó.",
    [
        "Tượng đồng gia đình di dân trên xe ngựa với hành lý, samovar.",
        "Đặt tại Quảng trường Nhà ga – nơi các đoàn di dân từng tới.",
        "Biểu tượng của làn sóng lập nghiệp hình thành vùng tự trị.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–15 phút.",
        "best_time_vi": "Ban ngày để chụp ảnh; đẹp cả khi có ánh đèn buổi tối.",
        "tips_vi": "Kết hợp tham quan đài Menorah và ga Birobidzhan I liền kề.",
    },
    [
        {"title": "Яндекс Карты — Памятник первым переселенцам (Биробиджан)", "url": "https://yandex.ru/maps/org/pervym_pereselentsam/219319683200/"},
    ],
    ["monument", "settlers", "history", "birobidzhan"],
    maps_org("https://yandex.ru/maps/org/pervym_pereselentsam/219319683200/", "Monument to the First Settlers", "Birobidzhan"),
))

# 8) Скульптура «Скрипач» ------------------------------------------------------
RECORDS.append(rec(
    "fiddler-sculpture-birobidzhan",
    "Tượng «Nghệ sĩ vĩ cầm» (Skulptura Skripach)",
    "Скульптура «Скрипач»",
    "The Fiddler Sculpture",
    ["monument"],
    48.787825, 132.930041,
    "Театральная площадь (trước Nhạc viện tỉnh), thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Tượng đồng người nghệ sĩ kéo vĩ cầm trên Quảng trường Nhà hát – hình ảnh gợi nhắc «Người kéo vĩ cầm trên mái nhà» và di sản âm nhạc Do Thái.",
    "Скульптура «Скрипач» là bức tượng đồng khắc hoạ một nghệ sĩ đang say sưa kéo vĩ cầm, đặt trên Quảng trường Nhà hát ngay trước toà nhà Nhạc viện tỉnh Birobidzhan. Hình tượng gợi liên tưởng tới «Fiddler on the Roof» (Người kéo vĩ cầm trên mái nhà) – biểu tượng quen thuộc của văn hoá và âm nhạc Do Thái Đông Âu, đồng thời tôn vinh truyền thống klezmer gắn với cộng đồng đã tạo nên vùng đất này. Xung quanh tượng là các nàng thơ, đài phun nước và bồn hoa trang trí, tạo nên một góc quảng trường sống động, được người dân và du khách yêu thích để dạo chơi, chụp ảnh.",
    [
        "Tượng đồng nghệ sĩ vĩ cầm gợi nhắc «Fiddler on the Roof».",
        "Biểu tượng âm nhạc klezmer và văn hoá Do Thái của vùng.",
        "Nằm trên Quảng trường Nhà hát với đài phun nước, bồn hoa.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 10–15 phút.",
        "best_time_vi": "Mùa ấm khi đài phun nước hoạt động; buổi tối có đèn.",
        "tips_vi": "Ghép cùng buổi diễn ở Nhạc viện tỉnh ngay bên cạnh.",
    },
    [
        {"title": "Яндекс Карты — Скульптура «Скрипач» (Биробиджан)", "url": "https://yandex.ru/maps/org/skripach/209137397571/"},
    ],
    ["monument", "sculpture", "music", "jewish-culture", "birobidzhan"],
    maps_org("https://yandex.ru/maps/org/skripach/209137397571/", "The Fiddler Sculpture", "Birobidzhan"),
))

# 9) Мемориал «Вечный огонь» / сквер Победы ------------------------------------
RECORDS.append(rec(
    "eternal-flame-victory-square-birobidzhan",
    "Đài Ngọn lửa Vĩnh cửu – Vườn hoa Chiến thắng (Vechny ogon)",
    "Мемориал «Вечный огонь» / сквер Победы",
    "Eternal Flame Memorial / Victory Square",
    ["monument"],
    48.791508, 132.932787,
    "Сквер Победы (gần Quảng trường Nhà ga), thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Đài tưởng niệm Chiến tranh Vệ quốc Vĩ đại với Ngọn lửa Vĩnh cửu, đặt trong Vườn hoa Chiến thắng ở trung tâm Birobidzhan.",
    "Мемориал «Вечный огонь» nằm trong сквер Победы (Vườn hoa Chiến thắng) là đài tưởng niệm chính của Birobidzhan dành cho những người con của vùng đất đã ngã xuống trong Chiến tranh Vệ quốc Vĩ đại 1941–1945. Vườn hoa được khánh thành ngày 8/5/1975 nhân 30 năm Chiến thắng, và Ngọn lửa Vĩnh cửu được thắp lên cạnh bia tưởng niệm cùng «Con đường các Anh hùng» (Аллея героев). Đây là nơi diễn ra các nghi lễ đặt hoa vào Ngày Chiến thắng 9/5 và những dịp trọng thể khác, đồng thời là một không gian xanh trang nghiêm giữa lòng thành phố. Khu tưởng niệm đã được tu bổ và thắp lại ngọn lửa sau cải tạo cuối năm 2025.",
    [
        "Ngọn lửa Vĩnh cửu tưởng niệm liệt sĩ Chiến tranh Vệ quốc.",
        "Vườn hoa Chiến thắng khánh thành năm 1975, có Аллея героев.",
        "Nơi tổ chức nghi lễ Ngày Chiến thắng 9/5.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–20 phút.",
        "best_time_vi": "Quanh năm; trang trọng nhất dịp 9/5 (Ngày Chiến thắng).",
        "tips_vi": "Giữ thái độ trang nghiêm; gần Quảng trường Nhà ga nên dễ kết hợp tham quan.",
    },
    [
        {"title": "Яндекс Карты — Вечный огонь / сквер Победы (Биробиджан)", "url": "https://yandex.ru/maps/org/vechny_ogon/165913077776/"},
    ],
    ["memorial", "eternal-flame", "wwii", "birobidzhan"],
    maps_org("https://yandex.ru/maps/org/vechny_ogon/165913077776/", "Eternal Flame Memorial Victory Square", "Birobidzhan"),
))

# 10) Городской парк культуры и отдыха + Комсомольское озеро --------------------
RECORDS.append(rec(
    "birobidzhan-city-park",
    "Công viên Văn hoá – Nghỉ ngơi thành phố & hồ Komsomol (Gorodskoy park)",
    "Городской парк культуры и отдыха и Комсомольское озеро",
    "Birobidzhan City Park & Komsomol Lake",
    ["park_garden"],
    48.784107, 132.931566,
    "Ул. Советская, ven sông Bira, thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Công viên trung tâm bên sông Bira với khu vui chơi và hồ – bãi tắm liền kề, là nơi nghỉ ngơi quen thuộc của người dân thành phố.",
    "Городской парк культуры и отдыха là công viên trung tâm của Birobidzhan, trải dọc bờ sông Bira. Đây là không gian nghỉ ngơi, dạo chơi và giải trí quen thuộc của người dân với các lối đi rợp cây, khu trò chơi thiếu nhi, sân khấu ngoài trời và những sự kiện văn hoá theo mùa. Sát cạnh công viên là hồ nước cùng bãi tắm – điểm hạ nhiệt được ưa chuộng trong những ngày hè oi ả của vùng Viễn Đông. Kết hợp giữa mảng xanh, mặt nước và không khí sinh hoạt cộng đồng, đây là nơi lý tưởng để du khách cảm nhận nhịp sống thường nhật của thủ phủ tỉnh nhỏ nhất về dân số này.",
    [
        "Công viên trung tâm bên bờ sông Bira.",
        "Khu vui chơi, sân khấu ngoài trời, sự kiện theo mùa.",
        "Có hồ và bãi tắm liền kề cho mùa hè.",
    ],
    {
        "hours_vi": "Ngoài trời, mở cửa tự do; các trò chơi/dịch vụ hoạt động chủ yếu mùa ấm.",
        "ticket_vi": "Vào cửa miễn phí; một số trò chơi và dịch vụ tính phí riêng.",
        "duration_vi": "Khoảng 1–2 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu; mùa hè cho tắm hồ.",
        "tips_vi": "Mang đồ chống muỗi vào mùa hè; kết hợp dạo bộ ven sông Bira.",
    },
    [
        {"title": "Яндекс Карты — Городской парк (Биробиджан)", "url": "https://yandex.ru/maps/11393/birobidgan/search/%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%BE%D0%B9%20%D0%BF%D0%B0%D1%80%D0%BA/"},
    ],
    ["park", "recreation", "lake", "bira-river", "birobidzhan"],
    maps_text("Городской парк культуры и отдыха", "Биробиджан", "City Park", "Birobidzhan", 48.784107, 132.931566),
))

# 11) Областная научная библиотека им. Шолом-Алейхема --------------------------
RECORDS.append(rec(
    "sholom-aleichem-library-birobidzhan",
    "Thư viện khoa học tỉnh mang tên Sholom-Aleichem (Biblioteka im. Sholom-Aleykhema)",
    "Областная научная библиотека им. Шолом-Алейхема",
    "Sholom-Aleichem Regional Scientific Library",
    ["other"],
    48.792979, 132.928952,
    "Ул. Ленина, 25, thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Thư viện lớn nhất tỉnh mang tên đại văn hào Do Thái Sholom-Aleichem, cũng là trung tâm lưu giữ tư liệu và văn hoá của vùng.",
    "Областная научная библиотека имени Шолом-Алейхема là thư viện tổng hợp lớn nhất Tỉnh tự trị Do Thái, mang tên nhà văn kinh điển viết bằng tiếng Yiddish – người đã trở thành biểu tượng văn hoá của vùng đất. Bên cạnh chức năng thư viện với kho sách phong phú, nơi đây còn là trung tâm lưu giữ tư liệu địa phương, tổ chức triển lãm, gặp gỡ văn học và các hoạt động gìn giữ di sản văn hoá – ngôn ngữ Do Thái (Yiddish). Toà nhà nằm ngay trung tâm trên phố Lenin, cùng địa chỉ với Bảo tàng địa phương, tạo thành một cụm văn hoá tiện lợi cho du khách muốn tìm hiểu sâu về Birobidzhan.",
    [
        "Thư viện lớn nhất tỉnh, mang tên đại văn hào Sholom-Aleichem.",
        "Trung tâm lưu giữ tư liệu và di sản văn hoá Yiddish.",
        "Cùng toà nhà với Bảo tàng địa phương trên phố Lenin.",
    ],
    {
        "hours_vi": "Mở cửa theo giờ hành chính các ngày trong tuần; thường nghỉ một ngày cố định.",
        "ticket_vi": "Vào tham quan/đọc miễn phí.",
        "duration_vi": "Khoảng 20–40 phút nếu tham quan.",
        "best_time_vi": "Quanh năm; chú ý các sự kiện văn học – triển lãm.",
        "tips_vi": "Kết hợp với Bảo tàng địa phương cùng toà nhà (Ленина 25).",
    },
    [
        {"title": "Trang chính thức thư viện (bounb.ru)", "url": "https://bounb.ru/"},
        {"title": "Яндекс Карты — Научная библиотека им. Шолом-Алейхема", "url": "https://yandex.ru/maps/org/nauchnaya_biblioteka_im_sholom_aleykhema/1340875030/"},
    ],
    ["library", "culture", "yiddish", "birobidzhan"],
    maps_org("https://yandex.ru/maps/org/nauchnaya_biblioteka_im_sholom_aleykhema/1340875030/", "Sholom-Aleichem Regional Library", "Birobidzhan"),
    official_site="https://bounb.ru/",
))

# 12) Площадь Ленина -----------------------------------------------------------
RECORDS.append(rec(
    "lenin-square-birobidzhan",
    "Quảng trường Lenin (Ploshchad Lenina)",
    "Площадь имени Ленина",
    "Lenin Square (Birobidzhan)",
    ["square_street"],
    48.790149, 132.925047,
    "Trung tâm hành chính thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Quảng trường trung tâm và là nơi tổ chức các sự kiện lớn của thành phố, với tượng đài Lenin dựng năm 1978.",
    "Площадь имени Ленина là quảng trường trung tâm của Birobidzhan – không gian công cộng chính, nơi bao quanh là các toà nhà chính quyền tỉnh và thành phố. Tượng đài Vladimir Lenin tại đây được khánh thành ngày 7/10/1978. Quảng trường là địa điểm diễn ra những sự kiện quan trọng: mít-tinh, lễ hội thành phố, hội chợ, chương trình đón năm mới với cây thông và sân trượt băng vào mùa đông. Rộng rãi và nằm ở vị trí trung tâm, đây là điểm khởi đầu thuận tiện để dạo bộ khám phá khu lõi lịch sử – hành chính của thủ phủ tỉnh.",
    [
        "Quảng trường trung tâm hành chính của thành phố.",
        "Tượng đài Lenin khánh thành năm 1978.",
        "Nơi tổ chức lễ hội, mít-tinh và sự kiện năm mới.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–20 phút.",
        "best_time_vi": "Quanh năm; sôi động nhất vào dịp lễ và mùa đông (chợ năm mới).",
        "tips_vi": "Điểm trung tâm dễ định vị; từ đây đi bộ tới các bảo tàng, nhà thờ và phố đi bộ.",
    },
    [
        {"title": "Яндекс Карты — Площадь имени Ленина (Биробиджан)", "url": "https://yandex.ru/maps/11393/birobidgan/geo/ploshchad_imeni_lenina/1520635919/"},
    ],
    ["square", "city-center", "lenin", "birobidzhan"],
    maps_text("Площадь Ленина", "Биробиджан", "Lenin Square", "Birobidzhan", 48.790149, 132.925047),
))

# 13) Театральная площадь ------------------------------------------------------
RECORDS.append(rec(
    "theatre-square-birobidzhan",
    "Quảng trường Nhà hát (Teatralnaya ploshchad)",
    "Театральная площадь",
    "Theatre Square (Birobidzhan)",
    ["square_street"],
    48.787250, 132.929900,
    "Trước Nhạc viện tỉnh, pr. 60-letiya SSSR, thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Quảng trường văn hoá của thành phố trước Nhạc viện tỉnh, với đài phun nước, bồn hoa và tượng «Nghệ sĩ vĩ cầm».",
    "Театральная площадь là quảng trường văn hoá trung tâm của Birobidzhan, trải rộng trước toà nhà Nhạc viện tỉnh. Đây là không gian dạo chơi sinh động với đài phun nước, các bồn hoa được tạo hình trang trí và bức tượng «Nghệ sĩ vĩ cầm» nổi tiếng. Vào mùa ấm, quảng trường là nơi hò hẹn, đi dạo buổi tối, tổ chức các buổi biểu diễn ngoài trời và lễ hội thành phố; mùa đông lại khoác lên mình khung cảnh trang trí băng tuyết. Kết nối liền mạch với Nhạc viện, quảng trường tạo thành trái tim văn hoá – giải trí của thủ phủ tỉnh.",
    [
        "Quảng trường văn hoá trước Nhạc viện tỉnh.",
        "Đài phun nước, bồn hoa và tượng «Nghệ sĩ vĩ cầm».",
        "Nơi diễn ra biểu diễn ngoài trời và lễ hội thành phố.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 15–30 phút.",
        "best_time_vi": "Mùa ấm khi đài phun nước hoạt động; buổi tối lên đèn.",
        "tips_vi": "Ghép cùng Nhạc viện tỉnh và tượng «Nghệ sĩ vĩ cầm» ngay tại quảng trường.",
    },
    [
        {"title": "Яндекс Карты — Театральная площадь (Биробиджан)", "url": "https://yandex.ru/maps/11393/birobidgan/search/%D0%A2%D0%B5%D0%B0%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%BF%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D1%8C/"},
    ],
    ["square", "fountain", "city-center", "birobidzhan"],
    maps_text("Театральная площадь", "Биробиджан", "Theatre Square", "Birobidzhan", 48.787250, 132.929900),
))

# 14) Биробиджанский Арбат -----------------------------------------------------
RECORDS.append(rec(
    "birobidzhan-arbat",
    "Phố đi bộ Arbat Birobidzhan (Birobidzhanskiy Arbat)",
    "Биробиджанский Арбат (пешеходная зона ул. Шолом-Алейхема)",
    "Birobidzhan Arbat (pedestrian street)",
    ["square_street"],
    48.788750, 132.934243,
    "Đoạn đi bộ phố Шолом-Алейхема (khu vực nhà số 1–11), thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga.",
    "Đoạn phố đi bộ trung tâm mang tên nhà văn Sholom-Aleichem, với quán xá, cửa hàng và không khí thư giãn.",
    "Биробиджанский Арбат là tên gọi thân mật cho đoạn phố đi bộ trên trục ул. Шолом-Алейхема ở trung tâm thành phố – tương tự phố Arbat nổi tiếng ở Moskva. Đây là nơi tập trung cửa hàng, quán cà phê, ghế nghỉ và cây xanh, là không gian dạo bộ, mua sắm và gặp gỡ được người dân yêu thích. Trên và quanh phố còn có các chi tiết trang trí, tiểu cảnh gợi nhắc bản sắc Do Thái của thành phố. Với những du khách muốn cảm nhận nhịp sống đời thường của Birobidzhan, đây là đoạn phố đáng để tản bộ, thưởng thức đồ uống và quan sát sinh hoạt địa phương.",
    [
        "Phố đi bộ trung tâm mang tên nhà văn Sholom-Aleichem.",
        "Nhiều quán cà phê, cửa hàng, ghế nghỉ và cây xanh.",
        "Không gian dạo bộ, mua sắm quen thuộc của người dân.",
    ],
    {
        "hours_vi": "Ngoài trời, dạo bộ tự do mọi lúc; quán xá theo giờ riêng.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–60 phút.",
        "best_time_vi": "Mùa ấm và buổi chiều tối; mùa đông khá lạnh.",
        "tips_vi": "Kết hợp với Bảo tàng nghệ thuật hiện đại và Quảng trường Nhà hát gần đó.",
    },
    [
        {"title": "Яндекс Карты — пешеходная зона ул. Шолом-Алейхема (Биробиджан)", "url": "https://yandex.ru/maps/org/arbat/157498424964/"},
    ],
    ["pedestrian-street", "shopping", "walk", "birobidzhan"],
    maps_text("улица Шолом-Алейхема пешеходная зона Арбат", "Биробиджан", "Birobidzhan Arbat pedestrian street", "Birobidzhan", 48.788750, 132.934243),
))

# 15) Река Бира и набережная ---------------------------------------------------
RECORDS.append(rec(
    "bira-river-embankment-birobidzhan",
    "Sông Bira và kè dạo bộ (Reka Bira / naberezhnaya)",
    "Река Бира и набережная",
    "Bira River and Embankment",
    ["park_garden"],
    48.785500, 132.929500,
    "Bờ sông Bira, khu trung tâm thành phố Birobidzhan, Tỉnh tự trị Do Thái, Nga. (toạ độ điểm mốc trên bờ sông ở trung tâm)",
    "Con sông đặt tên cho thành phố (Biro-Bidzhan) cùng đoạn kè dạo bộ ở trung tâm – điểm thư giãn ven nước của Birobidzhan.",
    "Река Бира là con sông chảy qua trung tâm Birobidzhan và cùng với sông Bidzhan đã đặt tên cho thành phố (Biro-Bidzhan). Là nhánh trái của sông Amur, Bira dài khoảng 424 km, hình thành từ hợp lưu của các dòng Sutara và Kuldur ở rặng Tiểu Hưng An. Đoạn chảy qua thành phố với đoạn kè dạo bộ ở trung tâm là nơi người dân đi bộ, ngắm cảnh và câu cá; hai bờ sông gắn với công viên thành phố và các không gian xanh. Dòng Bira không chỉ là cảnh quan mà còn là một phần bản sắc – cái tên và cả nhịp sống của Birobidzhan đều gắn với con sông này. (Toạ độ ghi ở đây là điểm mốc trên bờ sông khu trung tâm.)",
    [
        "Con sông đặt tên cho thành phố Biro-Bidzhan.",
        "Nhánh trái của Amur, dài khoảng 424 km.",
        "Đoạn kè trung tâm là nơi dạo bộ, ngắm cảnh, câu cá.",
    ],
    {
        "hours_vi": "Ngoài trời, tham quan tự do mọi lúc.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30–45 phút dạo bộ ven sông.",
        "best_time_vi": "Cuối xuân đến đầu thu; mùa hè có thể câu cá, dạo mát.",
        "tips_vi": "Mang đồ chống muỗi mùa hè; kết hợp công viên thành phố liền kề.",
    },
    [
        {"title": "Циклопедия — Бира (река)", "url": "https://cyclowiki.org/wiki/%D0%91%D0%B8%D1%80%D0%B0_(%D1%80%D0%B5%D0%BA%D0%B0)"},
    ],
    ["river", "embankment", "nature", "bira-river", "birobidzhan"],
    maps_text("Набережная реки Бира", "Биробиджан", "Bira River embankment", "Birobidzhan", 48.785500, 132.929500),
))

# 16) Волочаевский мемориальный музей-памятник (сопка Июнь-Корань) --------------
RECORDS.append(rec(
    "volochaevka-battle-memorial",
    "Đài – bảo tàng trận Volochaevka trên đồi Iyun-Koran (Volochaevskiy memorial)",
    "Волочаевский мемориальный музей-памятник (сопка Июнь-Корань)",
    "Volochaevka Battle Memorial-Museum (Iyun-Koran Hill)",
    ["monument", "museum"],
    48.564700, 134.498800,
    "Đỉnh đồi Iyun-Koran, cạnh làng Volochaevka-1, huyện Smidovichsky, Tỉnh tự trị Do Thái, Nga (cách Birobidzhan ~76 km về phía đông).",
    "Khu tưởng niệm trên đồi Iyun-Koran – nơi diễn ra trận Volochaevka 1922, một trong những trận đánh lớn cuối Nội chiến ở Viễn Đông.",
    "Волочаевский мемориальный музей-памятник nằm trên đỉnh đồi Iyun-Koran (сопка Июнь-Корань) bên cạnh làng Volochaevka-1, tưởng niệm trận Volochaevka diễn ra ngày 5–14/2/1922 – một trong những trận đánh quyết định của giai đoạn cuối Nội chiến Nga ở vùng Viễn Đông. Năm 1928, trên đỉnh đồi, cạnh ngôi mộ tập thể của 118 chiến sĩ hồng quân đã hy sinh, người ta dựng lên toà nhà bảo tàng với tượng người lính Hồng quân Nhân dân trên mái. Bên trong từng trưng bày các hiện vật và một bức tranh toàn cảnh (diorama) về trận đánh. Ngày 14/6/2022, đúng dịp kỷ niệm, quần thể tưởng niệm được mở cửa trở lại sau đợt trùng tu lớn. Đây là di tích lịch sử – quân sự nổi bật nhất của tỉnh, gắn với bài hát «Trên những ngọn đồi Mãn Châu» và ký ức về «những ngày Volochaevka».",
    [
        "Di tích trận Volochaevka 1922 – bước ngoặt cuối Nội chiến ở Viễn Đông.",
        "Bảo tàng trên đồi (1928) với tượng lính Hồng quân trên mái, mộ tập thể 118 chiến sĩ.",
        "Quần thể tưởng niệm được trùng tu, mở lại năm 2022.",
    ],
    {
        "hours_vi": "Bảo tàng mở theo lịch (nên hỏi trước); khu đồi và đài tưởng niệm ngoài trời thăm tự do.",
        "ticket_vi": "Đồi và đài tưởng niệm miễn phí; phần bảo tàng có thể thu phí nhỏ.",
        "duration_vi": "Khoảng 1–1,5 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu; trang trọng dịp kỷ niệm tháng 2 và tháng 6.",
        "tips_vi": "Đi ô tô theo quốc lộ Chita–Khabarovsk là thuận tiện nhất; leo lên đỉnh đồi để ngắm toàn cảnh.",
    },
    [
        {"title": "Музеи России — Волочаевский мемориальный музей-памятник (M1442)", "url": "http://www.museum.ru/M1442"},
        {"title": "Культурный туризм — Волочаевская сопка", "url": "https://culttourism.ru/evreyskaya/volochaevskaya_sopka.html"},
    ],
    ["memorial", "civil-war", "battle", "museum", "volochaevka"],
    maps_org("https://yandex.com/maps/org/sopka_iyun_koran/213164902544/", "Volochaevka Battle Memorial Iyun-Koran Hill", "Volochaevka"),
))

# 17) Курорт Кульдур -----------------------------------------------------------
RECORDS.append(rec(
    "kuldur-resort",
    "Khu nghỉ dưỡng suối khoáng nóng Kuldur (Kurort Kuldur)",
    "Курорт Кульдур",
    "Kuldur Balneological Resort",
    ["other"],
    49.203900, 131.631900,
    "Thị trấn Kuldur, huyện Obluchensky, Tỉnh tự trị Do Thái, Nga (cách Birobidzhan ~135 km).",
    "Khu nghỉ dưỡng suối khoáng nóng lâu đời nhất vùng Viễn Đông, nằm trong thung lũng sông Kuldur giữa rặng Tiểu Hưng An.",
    "Курорт Кульдур là khu nghỉ dưỡng chữa bệnh bằng suối khoáng nóng (balneological) lâu đời và nổi tiếng nhất vùng Viễn Đông, hoạt động từ năm 1924. Khu nghỉ nằm trong thung lũng sông Kuldur, giữa rừng taiga của rặng núi Tiểu Hưng An, sử dụng nguồn nước khoáng nóng chứa silic và các thành phần khoáng có tác dụng hỗ trợ điều trị bệnh cơ – xương – khớp, thần kinh và da. Không khí trong lành, cảnh quan núi rừng cùng hệ thống các nhà điều dưỡng khiến Kuldur trở thành điểm đến kết hợp nghỉ dưỡng và phục hồi sức khoẻ được ưa chuộng suốt bốn mùa. Đây cũng là địa danh gắn với tước hiệu của giám mục Birobidzhan «và Kuldur».",
    [
        "Khu suối khoáng nóng lâu đời nhất Viễn Đông (từ 1924).",
        "Nước khoáng nóng silic hỗ trợ trị bệnh xương khớp, thần kinh, da.",
        "Nằm giữa thung lũng và rừng taiga rặng Tiểu Hưng An.",
    ],
    {
        "hours_vi": "Theo lịch của các nhà điều dưỡng (санаторий); nhận khách quanh năm.",
        "ticket_vi": "Trả phí theo gói lưu trú/điều trị của cơ sở điều dưỡng.",
        "duration_vi": "Thường lưu trú vài ngày đến vài tuần theo liệu trình.",
        "best_time_vi": "Quanh năm; mùa đông tuyết đẹp, mùa hè mát mẻ.",
        "tips_vi": "Nên đặt gói điều dưỡng trước; đi tàu tới ga gần rồi trung chuyển, hoặc đi ô tô.",
    },
    [
        {"title": "Рувики — Кульдур", "url": "https://ru.ruwiki.ru/wiki/%D0%9A%D1%83%D0%BB%D1%8C%D0%B4%D1%83%D1%80"},
    ],
    ["resort", "hot-springs", "spa", "health", "kuldur"],
    maps_text("Курорт Кульдур санаторий", "Кульдур", "Kuldur resort", "Kuldur", 49.203900, 131.631900),
))

# 18) Город Облучье ------------------------------------------------------------
RECORDS.append(rec(
    "obluchye-town",
    "Thị trấn Obluchye (Gorod Obluchye)",
    "Город Облучье",
    "Obluchye Town",
    ["other"],
    49.018000, 131.050000,
    "Trung tâm huyện Obluchensky, Tỉnh tự trị Do Thái, Nga (cách Birobidzhan ~159 km về phía tây).",
    "Thị trấn miền núi trên tuyến đường sắt Xuyên Siberia, cửa ngõ phía tây của tỉnh, ra đời từ việc xây dựng tuyến đường sắt Amur.",
    "Город Облучье là thị trấn cực tây của Tỉnh tự trị Do Thái, trung tâm hành chính của huyện Obluchensky, nằm giữa vùng núi Tiểu Hưng An sát ranh giới với tỉnh Amur. Thị trấn hình thành đầu thế kỷ 20 gắn với việc xây dựng tuyến đường sắt Amur – một đoạn của Đường sắt Xuyên Siberia – và được nâng cấp thành thành phố năm 1938. Đây là một đầu mối đường sắt quan trọng, đồng thời nổi tiếng là một trong những nơi có khí hậu khắc nghiệt, mùa đông rất lạnh của vùng. Với du khách yêu thích hành trình bằng tàu hoả và cảnh quan núi rừng taiga, Obluchye là điểm dừng đặc trưng cho miền tây của tỉnh.",
    [
        "Thị trấn cực tây của tỉnh, giáp tỉnh Amur.",
        "Ra đời cùng tuyến đường sắt Amur (Xuyên Siberia), thành phố từ 1938.",
        "Đầu mối đường sắt giữa vùng núi Tiểu Hưng An.",
    ],
    {
        "hours_vi": "Thị trấn – tham quan tự do; dịch vụ theo giờ địa phương.",
        "ticket_vi": "Miễn phí (đi lại, lưu trú tự túc).",
        "duration_vi": "Nửa ngày nếu ghé qua.",
        "best_time_vi": "Mùa hè và đầu thu dễ chịu hơn; mùa đông rất lạnh.",
        "tips_vi": "Tiện nhất khi đi tàu trên tuyến Xuyên Siberia; chuẩn bị đồ ấm nếu tới vào mùa đông.",
    },
    [
        {"title": "Рувики — Облучье", "url": "https://ru.ruwiki.ru/wiki/%D0%9E%D0%B1%D0%BB%D1%83%D1%87%D1%8C%D0%B5"},
    ],
    ["town", "railway", "trans-siberian", "obluchye"],
    maps_text("Город Облучье", "Облучье", "Obluchye", "Obluchye", 49.018000, 131.050000),
))

# 19) Село Амурзет -------------------------------------------------------------
RECORDS.append(rec(
    "amurzet-village",
    "Làng Amurzet bên sông Amur (Selo Amurzet)",
    "Село Амурзет",
    "Amurzet Village",
    ["other"],
    47.696700, 131.098100,
    "Trung tâm huyện Oktyabrsky, bên bờ trái sông Amur, Tỉnh tự trị Do Thái, Nga (cách Birobidzhan ~180 km về tây-nam).",
    "Làng trung tâm huyện Oktyabrsky bên bờ sông Amur, do người Do Thái di cư lập nên cuối thập niên 1920, đối diện Trung Quốc qua sông.",
    "Село Амурзет là trung tâm hành chính của huyện Oktyabrsky, nằm ở cực nam Tỉnh tự trị Do Thái, ngay bên bờ trái sông Amur – dòng sông biên giới ngăn cách Nga với Trung Quốc. Ngôi làng được lập năm 1929 bởi những người Do Thái di cư tới khai phá vùng đất; chính cái tên «Amurzet» là chữ viết tắt của cụm từ Nga «Hội hợp tác ruộng đất của người Do Thái trên sông Amur» (Амурское земельное еврейское товарищество). Ngày nay Amurzet là một làng nông nghiệp yên bình, điểm quan sát dòng Amur rộng lớn và cảnh quan đồng bằng ven sông, đồng thời là chứng tích cho công cuộc định cư nông nghiệp của người Do Thái ở Viễn Đông.",
    [
        "Làng trung tâm huyện Oktyabrsky, bên bờ sông Amur.",
        "Do người Do Thái di cư lập năm 1929; tên là chữ viết tắt.",
        "Điểm ngắm sông Amur và vùng biên giới Nga – Trung.",
    ],
    {
        "hours_vi": "Làng – tham quan tự do; dịch vụ theo giờ địa phương.",
        "ticket_vi": "Miễn phí (đi lại, lưu trú tự túc).",
        "duration_vi": "Nửa ngày nếu ghé qua.",
        "best_time_vi": "Cuối xuân đến đầu thu; ven sông đẹp vào mùa hè.",
        "tips_vi": "Đây là vùng biên giới – tuân thủ quy định chụp ảnh, giấy tờ khu vực biên giới nếu có.",
    },
    [
        {"title": "Рувики — Амурзет", "url": "https://ru.ruwiki.ru/wiki/%D0%90%D0%BC%D1%83%D1%80%D0%B7%D0%B5%D1%82"},
    ],
    ["village", "amur-river", "border", "jewish-settlement", "amurzet"],
    maps_text("Село Амурзет", "Амурзет", "Amurzet", "Amurzet", 47.696700, 131.098100),
))

# 20) Село Ленинское -----------------------------------------------------------
RECORDS.append(rec(
    "leninskoye-village",
    "Làng Leninskoye bên sông Amur (Selo Leninskoye)",
    "Село Ленинское",
    "Leninskoye Village",
    ["other"],
    47.934000, 132.623000,
    "Trung tâm huyện Leninsky, bên bờ trái sông Amur, Tỉnh tự trị Do Thái, Nga (cách Birobidzhan ~132 km).",
    "Làng biên giới bên sông Amur, một trong những điểm định cư Cossack lâu đời của vùng, có bến vượt sông sang Trung Quốc.",
    "Село Ленинское là trung tâm hành chính của huyện Leninsky, nằm bên bờ trái sông Amur ở phía nam Tỉnh tự trị Do Thái. Ngôi làng được lập từ năm 1858 bởi những người Cossack vùng Transbaikal với tên gọi ban đầu là Mikhailo-Semyonovskoye – tức có lịch sử lâu đời hơn nhiều so với thời kỳ hình thành vùng tự trị Do Thái. Nằm ngay đối diện thành phố Tongjiang của Trung Quốc bên kia sông, Leninskoye là một điểm ở vùng biên giới với bến vượt sông và giao thương qua Amur. Với du khách, đây là nơi cảm nhận không khí làng quê biên viễn và ngắm dòng Amur hùng vĩ – ranh giới tự nhiên giữa hai quốc gia.",
    [
        "Làng trung tâm huyện Leninsky bên sông Amur.",
        "Do người Cossack lập năm 1858 (tên gốc Mikhailo-Semyonovskoye).",
        "Đối diện thành phố Tongjiang (Trung Quốc), có bến vượt sông.",
    ],
    {
        "hours_vi": "Làng – tham quan tự do; dịch vụ theo giờ địa phương.",
        "ticket_vi": "Miễn phí (đi lại, lưu trú tự túc).",
        "duration_vi": "Nửa ngày nếu ghé qua.",
        "best_time_vi": "Cuối xuân đến đầu thu; mùa hè thuận cho ngắm sông.",
        "tips_vi": "Vùng biên giới – tuân thủ quy định giấy tờ và chụp ảnh khu vực biên giới.",
    },
    [
        {"title": "Рувики — Ленинское (Еврейская автономная область)", "url": "https://ru.ruwiki.ru/wiki/%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D1%81%D0%BA%D0%BE%D0%B5_(%D0%95%D0%B2%D1%80%D0%B5%D0%B9%D1%81%D0%BA%D0%B0%D1%8F_%D0%B0%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C)"},
    ],
    ["village", "amur-river", "border", "cossack", "leninskoye"],
    maps_text("Село Ленинское", "Ленинское", "Leninskoye", "Leninskoye", 47.934000, 132.623000),
))

# 21) Озеро Забеловское / кластер «Забеловский» (заповедник Бастак) -------------
RECORDS.append(rec(
    "zabelovskoye-lake",
    "Hồ Zabelovskoye – cụm Zabelovsky (Ozero Zabelovskoye)",
    "Озеро Забеловское / кластер «Забеловский» (заповедник Бастак)",
    "Zabelovskoye Lake / Zabelovsky Cluster (Bastak Reserve)",
    ["park_garden"],
    48.300000, 133.867000,
    "Đồng bằng ngập lũ sông Amur, huyện Smidovichsky, Tỉnh tự trị Do Thái, Nga (~35 km tây-bắc thị trấn Smidovich; toạ độ là tâm khu đất ngập nước).",
    "Hồ nước ngọt lớn nhất tỉnh trong vùng đầm lầy ven sông Amur, thuộc cụm Zabelovsky của khu bảo tồn Bastak – thiên đường của chim nước và hệ sinh thái ngập nước.",
    "Озеро Забеловское là hồ nước ngọt lớn nhất Tỉnh tự trị Do Thái (khoảng 4,3 km²), một hồ cửa sông cổ (старица) nối với sông Amur qua lạch Krestovaya, nằm trong vùng đồng bằng ngập lũ rộng lớn ở phía nam tỉnh. Khu vực này thuộc cụm Zabelovsky – được sáp nhập vào khu bảo tồn thiên nhiên Bastak năm 2011 – và là một vùng đất ngập nước có giá trị sinh thái cao. Đây là nơi cư trú và dừng chân của nhiều loài chim nước di cư, trong đó có những loài quý hiếm như sếu và cò, cùng hệ động – thực vật đặc trưng của đầm lầy Amur. Việc tham quan cần theo tuyến và có sự cho phép của ban quản lý khu bảo tồn. (Toạ độ ghi ở đây là tâm của khu đất ngập nước.)",
    [
        "Hồ nước ngọt lớn nhất tỉnh (~4,3 km²), hồ cửa sông cổ nối Amur.",
        "Thuộc cụm Zabelovsky của khu bảo tồn Bastak (từ 2011).",
        "Vùng đất ngập nước quan trọng cho chim di cư (sếu, cò...).",
    ],
    {
        "hours_vi": "Vùng bảo tồn – vào theo tuyến và cần xin phép ban quản lý Bastak.",
        "ticket_vi": "Theo quy định của khu bảo tồn (có thể cần giấy phép và hướng dẫn viên).",
        "duration_vi": "Nửa ngày đến cả ngày tuỳ tuyến.",
        "best_time_vi": "Cuối xuân đến đầu thu (mùa chim làm tổ, di cư).",
        "tips_vi": "Liên hệ khu bảo tồn Bastak trước; mang ống nhòm, đồ chống muỗi, không gây tiếng ồn.",
    },
    [
        {"title": "ФЕСК — Забеловское озеро (водно-болотное угодье)", "url": "http://www.fesk.ru/wetlands/289.html"},
    ],
    ["lake", "wetland", "nature-reserve", "bastak", "birdwatching"],
    maps_text("Озеро Забеловское заповедник Бастак", "Смидович", "Zabelovskoye Lake Bastak Reserve", "Smidovich", 48.300000, 133.867000),
))

# 22) Лондоковская пещера ------------------------------------------------------
RECORDS.append(rec(
    "londoko-cave",
    "Hang Londoko (Londokovskaya peshchera)",
    "Лондоковская пещера",
    "Londoko Cave",
    ["park_garden"],
    49.049980, 131.880000,
    "Huyện Obluchensky, ~5 km bắc thị trấn Izvestkovy zavod (gần Teploozyorsk), Tỉnh tự trị Do Thái, Nga.",
    "Di tích thiên nhiên hang động cấp tỉnh ở vùng núi đá vôi phía tây, điểm khám phá cho những người ưa hang động.",
    "Лондоковская пещера là một di tích thiên nhiên (памятник природы) cấp tỉnh dạng hang động, nằm ở huyện Obluchensky phía tây Tỉnh tự trị Do Thái, cách thị trấn Izvestkovy zavod khoảng 5 km về phía bắc. Hang hình thành trong vùng đá vôi (karst) đặc trưng của khu vực – nơi vốn có hoạt động khai thác đá vôi lâu đời. Khu vực được bảo vệ có diện tích khoảng 12,5 ha, ranh giới là vòng tròn bán kính 200 m quanh cửa hang. Đây là điểm đến cho những du khách ưa khám phá địa chất – hang động và cảnh quan núi đá vôi của miền tây tỉnh, tuy quy mô nhỏ và cần chuẩn bị kỹ khi tham quan.",
    [
        "Di tích thiên nhiên hang động cấp tỉnh trong vùng đá vôi karst.",
        "Khu bảo vệ ~12,5 ha (vòng tròn bán kính 200 m quanh cửa hang).",
        "Điểm khám phá địa chất – hang động ở miền tây tỉnh.",
    ],
    {
        "hours_vi": "Ngoài trời/hang tự nhiên – không có giờ cố định; nên đi ban ngày.",
        "ticket_vi": "Miễn phí (tự túc di chuyển và trang bị).",
        "duration_vi": "Khoảng 1–2 giờ tuỳ mức khám phá.",
        "best_time_vi": "Mùa khô, cuối xuân đến đầu thu.",
        "tips_vi": "Mang đèn pin, giày bám tốt và đi cùng người quen địa hình; thận trọng khi vào hang.",
    },
    [
        {"title": "Иди лесом — Лондоковская пещера (ЕАО)", "url": "https://idilesom.com/eao/places/1581"},
    ],
    ["cave", "karst", "nature-monument", "obluchensky"],
    maps_text("Лондоковская пещера", "Известковый", "Londoko Cave", "Izvestkovy", 49.049980, 131.880000),
))

# 23) Посёлок Смидович ---------------------------------------------------------
RECORDS.append(rec(
    "smidovich-settlement",
    "Đô thị Smidovich (Posyolok Smidovich)",
    "Посёлок Смидович",
    "Smidovich Settlement",
    ["other"],
    48.593000, 133.810000,
    "Trung tâm huyện Smidovichsky, trên quốc lộ Chita–Khabarovsk, Tỉnh tự trị Do Thái, Nga (cách Birobidzhan ~76 km về phía đông).",
    "Đô thị trung tâm huyện Smidovichsky ở miền đông tỉnh, cửa ngõ hướng về Khabarovsk và là điểm tiếp cận cụm bảo tồn Zabelovsky.",
    "Посёлок Смидович là trung tâm hành chính của huyện Smidovichsky – huyện cực đông của Tỉnh tự trị Do Thái, nằm trên quốc lộ liên bang Chita–Khabarovsk và tuyến đường sắt Xuyên Siberia. Ban đầu khu dân cư mang tên «In» (theo tên con sông), đến năm 1934 được đổi thành Smidovich để tưởng nhớ nhà hoạt động Xô-viết P. G. Smidovich. Là điểm dừng thuận tiện trên trục giao thông chính về phía Khabarovsk, đô thị cũng là cửa ngõ để tiếp cận vùng đầm lầy ven Amur và cụm bảo tồn Zabelovsky của khu bảo tồn Bastak ở phía nam huyện.",
    [
        "Trung tâm huyện cực đông của tỉnh, trên trục Chita–Khabarovsk.",
        "Đổi tên từ «In» thành Smidovich năm 1934.",
        "Cửa ngõ tới cụm bảo tồn Zabelovsky (đầm lầy Amur).",
    ],
    {
        "hours_vi": "Đô thị – tham quan tự do; dịch vụ theo giờ địa phương.",
        "ticket_vi": "Miễn phí (đi lại, lưu trú tự túc).",
        "duration_vi": "Vài giờ nếu ghé qua/nghỉ chân.",
        "best_time_vi": "Cuối xuân đến đầu thu.",
        "tips_vi": "Điểm dừng thuận tiện khi di chuyển giữa Birobidzhan và Khabarovsk; hỏi thông tin nếu muốn vào cụm Zabelovsky.",
    },
    [
        {"title": "Рувики — Смидович (Еврейская автономная область)", "url": "https://ru.ruwiki.ru/wiki/%D0%A1%D0%BC%D0%B8%D0%B4%D0%BE%D0%B2%D0%B8%D1%87_(%D0%95%D0%B2%D1%80%D0%B5%D0%B9%D1%81%D0%BA%D0%B0%D1%8F_%D0%B0%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C)"},
    ],
    ["town", "district-center", "trans-siberian", "smidovich"],
    maps_text("Посёлок Смидович", "Смидович", "Smidovich", "Smidovich", 48.593000, 133.810000),
))

# 24) Река Биджан --------------------------------------------------------------
RECORDS.append(rec(
    "bidzhan-river",
    "Sông Bidzhan (Reka Bidzhan)",
    "Река Биджан",
    "Bidzhan River",
    ["other"],
    48.347000, 131.940000,
    "Chảy theo hướng bắc – nam qua huyện Leninsky, Tỉnh tự trị Do Thái, Nga (toạ độ là điểm tham chiếu gần làng Bidzhan).",
    "Con sông đặt nửa sau cái tên «Biro-Bidzhan», nhánh trái sông Amur bắt nguồn từ rặng Tiểu Hưng An.",
    "Река Биджан là con sông đã góp nửa sau vào cái tên của thành phố và cả vùng «Biro-Bidzhan». Đây là nhánh trái của sông Amur, dài khoảng 274 km, hình thành từ hợp lưu của hai dòng Pravyy Bidzhan và Levyy Bidzhan, bắt nguồn từ vùng núi Tiểu Hưng An rồi chảy theo hướng bắc – nam qua huyện Leninsky trước khi đổ về đồng bằng ven Amur. Thung lũng sông với rừng, đầm và ruộng đồng là cảnh quan tiêu biểu của vùng, đồng thời gắn với các khu định cư nông nghiệp của người Do Thái xưa. Với ý nghĩa lịch sử – địa danh cùng cảnh sắc thiên nhiên, Bidzhan là một phần bản sắc của Tỉnh tự trị Do Thái. (Toạ độ ghi ở đây là điểm tham chiếu gần làng Bidzhan.)",
    [
        "Sông góp nửa sau tên gọi «Biro-Bidzhan».",
        "Nhánh trái sông Amur, dài khoảng 274 km.",
        "Bắt nguồn từ rặng Tiểu Hưng An, chảy qua huyện Leninsky.",
    ],
    {
        "hours_vi": "Cảnh quan thiên nhiên – tự do; nên đi ban ngày.",
        "ticket_vi": "Miễn phí (tự túc di chuyển).",
        "duration_vi": "Tuỳ hành trình; thường ghép với các điểm ở huyện Leninsky.",
        "best_time_vi": "Cuối xuân đến đầu thu.",
        "tips_vi": "Đường tới các đoạn sông chủ yếu là đường quê; nên đi ô tô và hỏi người địa phương.",
    },
    [
        {"title": "Водные ресурсы России — река Биджан", "url": "https://waterresources.ru/reki/bidzhan/"},
    ],
    ["river", "nature", "amur-basin", "leninsky", "bidzhan"],
    maps_text("Река Биджан", "Ленинский район", "Bidzhan River", "Leninsky District", 48.347000, 131.940000),
))

# 25) Село/пос. Николаевка -----------------------------------------------------
RECORDS.append(rec(
    "nikolayevka-settlement",
    "Đô thị Nikolayevka (Posyolok Nikolayevka)",
    "Посёлок Николаевка",
    "Nikolayevka Settlement",
    ["other"],
    48.560000, 134.780000,
    "Huyện Smidovichsky, phía đông tỉnh, gần thành phố Khabarovsk (qua sông), Tỉnh tự trị Do Thái, Nga.",
    "Một trong những đô thị lớn của huyện Smidovichsky ở cực đông tỉnh, nằm sát vùng Khabarovsk.",
    "Посёлок Николаевка là một trong những khu dân cư đô thị lớn của huyện Smidovichsky, nằm ở cực đông Tỉnh tự trị Do Thái, gần ranh giới với vùng Khabarovsk (chỉ cách thành phố Khabarovsk bởi dòng Amur và ranh giới hành chính). Nhờ vị trí kề cận đô thị lớn Khabarovsk và nằm trên trục giao thông chính, Nikolayevka là điểm dân cư sầm uất theo tiêu chuẩn địa phương và thường là cửa ngõ phía đông khi vào tỉnh từ hướng Khabarovsk. Đây là điểm dừng chân tiện lợi hơn là một điểm tham quan nổi bật, phù hợp với du khách di chuyển giữa hai vùng.",
    [
        "Đô thị lớn của huyện Smidovichsky, cực đông tỉnh.",
        "Nằm sát vùng Khabarovsk – cửa ngõ phía đông của tỉnh.",
        "Điểm dừng chân tiện lợi trên trục giao thông chính.",
    ],
    {
        "hours_vi": "Đô thị – tham quan tự do; dịch vụ theo giờ địa phương.",
        "ticket_vi": "Miễn phí (đi lại, lưu trú tự túc).",
        "duration_vi": "Ghé qua ngắn; điểm trung chuyển.",
        "best_time_vi": "Quanh năm; thuận tiện khi đi/đến Khabarovsk.",
        "tips_vi": "Thích hợp làm điểm dừng khi di chuyển giữa Khabarovsk và các huyện của tỉnh.",
    },
    [
        {"title": "Рувики — Николаевка (Еврейская автономная область)", "url": "https://ru.ruwiki.ru/wiki/%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2%D0%BA%D0%B0_(%D0%95%D0%B2%D1%80%D0%B5%D0%B9%D1%81%D0%BA%D0%B0%D1%8F_%D0%B0%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C)"},
    ],
    ["town", "district", "khabarovsk-border", "nikolayevka"],
    maps_text("Посёлок Николаевка Смидовичский район", "Николаевка", "Nikolayevka", "Nikolayevka", 48.560000, 134.780000),
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
        # kiểm tra phạm vi EAO: lat 47.3–49.4, lon 130–135
        lat = r["coordinates"]["lat"]
        lon = r["coordinates"]["lon"]
        assert 47.3 <= lat <= 49.4, f"lat ngoài phạm vi EAO: {r['slug']} {lat}"
        assert 130.0 <= lon <= 135.0, f"lon ngoài phạm vi EAO: {r['slug']} {lon}"
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
