# -*- coding: utf-8 -*-
"""_add_three_places_an_crafts.py — Bo sung dia diem con thieu (lan chay tu dong 2026-07-27).

UU TIEN VUNG (a): cac THI TRAN/THANH PHO PHU CAN quanh Moskva (moscow-oblast.json) va
Tinh Leningrad (leningrad-oblast.json). Noi do Moskva & SPb da bao hoa.

Lan nay bo sung 14 danh thang THAT SU noi tieng con THIEU:

  MOSCOW OBLAST (12):
   1) Xuong ve khay Zhostovo (Bao tang)          [museum]  — nghe ve khay son mai noi tieng the gioi
   2) Xuong ve tieu hoa Fedoskino                 [museum]  — cai noi tranh son mai Nga
   3) Nha may su Gzhel (Gzhelsky farforovy zavod) [museum]  — su xanh-trang coban truyen thong
   4) Bao tang Khan & Sal Nga (Pavlovsky Posad)   [museum]  — bao tang khan choang duy nhat o Nga
   5) Xuong khac go Bogorodskoye                  [museum]  — do choi go khac dan gian
   6) Tu vien Staro-Golutvin (Kolomna)            [church]  — do Thanh Sergius lap 1385
   7) Tu vien Bobrenev (Kolomna)                  [church]  — gan tran Kulikovo 1380
   8) Tu vien nu Vvedensky Vladychny (Serpukhov)  [church]  — lap 1360, icon "Chen Thanh Vo Tan"
   9) Tu vien Borisoglebsky (Dmitrov)             [church]  — the ky 15-16, gan dien Kremlin Dmitrov
  10) Kremlin Volokolamsk (Doi Nha Tho)           [fortress,church] — Nha tho Phuc Sinh tk 15
  11) Nha tho Rozhdestva Khrista (Verea/Gorodok)  [church,monument] — mo tuong Dorokhov 1812
  12) Nha tho tron Podmoklovo (rotunda)           [church]  — kien truc Baroque Petrine doc dao

  LENINGRAD OBLAST (2):
  13) Mem "Nevsky Pyatachok" (Kirovsk)            [monument] — bai dat dau cau Neva, Thchien II
  14) Tu vien Antoniyevo-Dymsky (Tikhvin)         [church]   — tk 13, ho Dymskoye

TOA DO THAT (WGS84, doi chieu 2026-07 — sobory.ru / 2GIS / Yandex Maps, thu tu lat~54-60, lon~30-39,
KHONG dao lat/lon):
   Zhostovo(museum) 56.00661, 37.64495 (2GIS center)
   Fedoskino        56.05499, 37.583472 (Yandex/2GIS)
   Gzhel(zavod)     55.600198, 38.452205 (Yandex ll, lang Rechitsy)
   Pavl.Posad(muzey)55.779906, 38.649679 (2GIS center)
   Bogorodskoye     56.495869, 38.18797 (2GIS trung tam pgt; link Yandex tro thang toi xuong)
   Staro-Golutvin   55.079731, 38.832162 (sobory.ru)
   Bobrenev         55.118951, 38.76024 (sobory.ru)
   Vvedensky Vlad.  54.898611, 37.398889 (sobory.ru 54 deg 53'55"N 37 deg 23'56"E)
   Borisoglebsky    56.342879, 37.531077 (sobory.ru)
   Volokolamsk krem 56.037917, 35.957748 (sobory.ru, Nha tho Phuc Sinh tren Doi Nha Tho)
   Verea sobor      55.344131, 36.188321 (sobory.ru)
   Podmoklovo       54.86698, 37.34676 (sobory.ru)
   Nevsky Pyatachok 59.841954, 30.956176 (Wikipedia/2GIS Rubezhny Kamen)
   Antoniyevo-Dymsk 59.57228, 33.675936 (sobory.ru, lang Bronevik, ho Dymskoye)

Noi dung tieng Viet NGUYEN GOC (paraphrase tu nguon mo, KHONG sao chep nguyen van; ghi nguon).
Chen AN TOAN: bo qua slug/id da ton tai; sao luu .bak truoc khi ghi.
"""
import json, os, datetime, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGIONS = os.path.join(ROOT, "data", "regions")
TODAY = "2026-07-27"
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

MO = "moscow-oblast"
MO_VI = "Tỉnh Moskva"
MO_FED = "Vùng Trung tâm"
LO = "leningrad-oblast"
LO_VI = "Tỉnh Leningrad"
LO_FED = "Vùng Tây Bắc"


def build_maps(lat, lon, name_ru, name_en, city_ru, city_en, org_url=None):
    """Link ban do TRO THANG toi dia diem. Uu tien URL trang to chuc tren Yandex (chinh xac nhat);
    neu khong co thi dung text=<ten Nga>, <thanh pho> + ll=lon,lat de mo dung the dia diem."""
    if org_url:
        yandex = org_url
    else:
        yq = urllib.parse.quote(f"{name_ru}, {city_ru}")
        yandex = f"https://yandex.com/maps/?text={yq}&ll={lon},{lat}&z=16"
    gq = urllib.parse.quote(f"{name_en}, {city_en}, Russia")
    google = f"https://www.google.com/maps/search/?api=1&query={gq}"
    return {"yandex": yandex, "google": google}


# ============================================================ 1) ZHOSTOVO FACTORY (MUSEUM)
ZHOSTOVO = {
    "id": f"{MO}-zhostovo-decorative-painting-factory",
    "slug": "zhostovo-decorative-painting-factory",
    "region": MO, "region_name_vi": MO_VI, "federal_district": MO_FED,
    "name_vi": "Xưởng vẽ trang trí Zhostovo & Bảo tàng (Zhostovskaya fabrika)",
    "name_ru": "Жостовская фабрика декоративной росписи",
    "name_en": "Zhostovo Factory of Decorative Painting",
    "categories": ["museum"],
    "coordinates": {"lat": 56.00661, "lon": 37.64495},
    "address_vi": "Phố Divnaya 15, làng Zhostovo, huyện Mytishchi, Tỉnh Moskva; cách trung tâm Moskva khoảng 30 km về phía bắc, gần hồ chứa Kliazma.",
    "rating": None,
    "presentation_short_vi": "Zhostovo là quê hương của nghề vẽ khay sơn mài trên kim loại nổi tiếng khắp thế giới, khởi nguồn từ năm 1825. Những chiếc khay nền đen bóng điểm các bó hoa rực rỡ vẽ tay đã trở thành một biểu tượng của mỹ nghệ dân gian Nga; tại đây du khách có thể thăm bảo tàng và tự tay thử vẽ trong lớp học nghề.",
    "presentation_long_vi": "Nằm bên hồ chứa Kliazma, cách Moskva chừng 30 km về phía bắc, làng Zhostovo gắn liền với một trong những nghề thủ công mỹ nghệ được yêu thích nhất của nước Nga: nghề vẽ khay sơn mài. Truyền thống này bắt đầu năm 1825, khi anh em nhà Vishnyakov mở xưởng làm khay, hộp và đồ dùng từ giấy bồi rồi phủ sơn; về sau người thợ chuyển sang làm khay bằng kim loại. Phong cách Zhostovo đặc trưng định hình vào thập niên 1870-1880 với những bó hoa lớn tươi tắn được đặt tự do trên nền sẫm, vẽ theo lối nhiều lớp tạo chiều sâu và ánh sáng. Năm 1960, các hợp tác xã địa phương hợp nhất thành Xưởng vẽ trang trí Zhostovo, và tên gọi 'Zhostovo' ngày nay là một chỉ dẫn địa lý được bảo hộ. Bên trong xưởng có bảo tàng lưu giữ bộ sưu tập khay phong phú vào bậc nhất, từ những mẫu cổ thế kỷ 19 tới tác phẩm của các nghệ nhân bậc thầy đương đại. Khách tham quan thường kết hợp xem dây chuyền sản xuất với một buổi học vẽ, nơi hướng dẫn viên chỉ cách cầm cọ và đưa những nét hoa đặc trưng - một trải nghiệm thú vị, dễ kết hợp trong chuyến đi trong ngày ở hướng bắc Moskva.",
    "highlights_vi": [
        "Nghề vẽ khay sơn mài trên kim loại có từ năm 1825, với bó hoa rực rỡ trên nền đen bóng - biểu tượng mỹ nghệ dân gian Nga.",
        "Bảo tàng của xưởng lưu giữ bộ sưu tập khay Zhostovo vào loại phong phú nhất, trải dài từ thế kỷ 19 đến nay.",
        "Có tour xem sản xuất và lớp học vẽ khay để du khách tự tay trải nghiệm; 'Zhostovo' là chỉ dẫn địa lý được bảo hộ.",
    ],
    "practical": {
        "hours_vi": "Tham quan bảo tàng và xưởng chủ yếu theo tour đặt trước, thường trong khung 10:00-17:00; nên gọi/đặt lịch trước.",
        "ticket_vi": "Có phí vào bảo tàng và phí riêng cho lớp học vẽ; mức giá thay đổi theo chương trình, nên hỏi trước khi đến.",
        "duration_vi": "Khoảng 1,5-2 giờ nếu kèm lớp học vẽ.",
        "best_time_vi": "Quanh năm (không gian trong nhà).",
        "tips_vi": "Nên đặt trước tour + lớp học vẽ. Từ Moskva đi hướng Mytishchi rồi vào làng Zhostovo; thuận tiện đi ô tô. Sản phẩm vẽ tay có bán tại cửa hàng của xưởng.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(56.00661, 37.64495, "Жостовская фабрика декоративной росписи",
                       "Zhostovo Factory of Decorative Painting", "Жостово", "Zhostovo"),
    "official_site": "https://zhostovo.ru/",
    "sources": [
        {"title": "Wikipedia (RU) — Жостовская фабрика декоративной росписи", "url": "https://ru.wikipedia.org/wiki/Жостовская_фабрика_декоративной_росписи"},
        {"title": "2GIS — Музей Жостовской фабрики декоративной росписи", "url": "https://2gis.ru/moscow/firm/70000001062911769"},
    ],
    "tags": ["museum", "folk-craft", "handicraft", "zhostovo", "lacquer", "mytishchi", "day-trip", "moscow-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 2) FEDOSKINO FACTORY (MUSEUM)
FEDOSKINO = {
    "id": f"{MO}-fedoskino-miniature-factory",
    "slug": "fedoskino-miniature-factory",
    "region": MO, "region_name_vi": MO_VI, "federal_district": MO_FED,
    "name_vi": "Xưởng tiểu hoạ sơn mài Fedoskino (Fedoskinskaya fabrika)",
    "name_ru": "Федоскинская фабрика миниатюрной живописи",
    "name_en": "Fedoskino Factory of Miniature Painting",
    "categories": ["museum"],
    "coordinates": {"lat": 56.05499, "lon": 37.583472},
    "address_vi": "Phố Lukutinskaya 66A, làng Fedoskino, huyện Mytishchi, Tỉnh Moskva; cách trung tâm Moskva khoảng 30 km về phía bắc.",
    "rating": None,
    "presentation_short_vi": "Fedoskino là cái nôi lâu đời nhất của nghệ thuật tiểu hoạ sơn mài Nga - lối vẽ bằng sơn dầu trên vật liệu giấy bồi (papier-mâché), hình thành từ cuối thế kỷ 18. Kỹ thuật lót xà cừ và ánh kim dưới lớp sơn tạo chiều sâu lấp lánh đặc trưng; tại xưởng có bảo tàng và lớp học vẽ cho khách.",
    "presentation_long_vi": "Cách Moskva khoảng 30 km về phía bắc, làng Fedoskino được xem là cái nôi của nghệ thuật tiểu hoạ sơn mài Nga. Nghề bắt nguồn từ năm 1795, khi thương nhân P. I. Korobov mở xưởng làm hộp đựng thuốc lá bằng giấy bồi ở làng Danilkovo (nay thuộc Fedoskino); về sau dòng họ Lukutin phát triển nghề thành một trường phái riêng. Nét độc đáo của tiểu hoạ Fedoskino là vẽ bằng sơn dầu nhiều lớp trên nền giấy bồi phủ sơn, thường lót lá kim loại hoặc mảnh xà cừ bên dưới để ánh sáng xuyên qua các lớp màu, khiến bức tranh nhỏ như phát sáng từ bên trong. Chủ đề quen thuộc là cảnh sinh hoạt dân gian, bộ ba ngựa kéo xe troika, phong cảnh và chân dung. Chính từ Fedoskino, kỹ thuật này lan toả và truyền cảm hứng cho các trung tâm sơn mài nổi tiếng khác của Nga. Ngày nay xưởng vẫn hoạt động, có bảo tàng trưng bày những hộp sơn mài tinh xảo qua các thời kỳ và tổ chức lớp học vẽ để du khách hiểu về quy trình công phu này - một điểm đến hấp dẫn cho người yêu mỹ nghệ, dễ kết hợp cùng làng khay Zhostovo gần đó.",
    "highlights_vi": [
        "Trung tâm tiểu hoạ sơn mài lâu đời nhất nước Nga, khởi nguồn từ xưởng của Korobov năm 1795 và dòng họ Lukutin.",
        "Kỹ thuật vẽ sơn dầu trên giấy bồi có lót xà cừ/ánh kim, tạo hiệu ứng chiều sâu lấp lánh đặc trưng.",
        "Xưởng còn hoạt động, có bảo tàng và lớp học vẽ; dễ kết hợp tham quan cùng làng khay Zhostovo lân cận.",
    ],
    "practical": {
        "hours_vi": "Tham quan bảo tàng và xưởng theo tour, thường 10:00-18:00; nên đặt lịch trước, nhất là với lớp học vẽ.",
        "ticket_vi": "Có phí vào bảo tàng và phí lớp học vẽ riêng; nên hỏi trước.",
        "duration_vi": "Khoảng 1,5-2 giờ.",
        "best_time_vi": "Quanh năm (trong nhà).",
        "tips_vi": "Đặt trước tour + lớp học. Từ Moskva đi hướng Mytishchi - Marfino; thuận tiện đi ô tô. Có thể ghép cùng Zhostovo trong một ngày.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(56.05499, 37.583472, "Федоскинская фабрика миниатюрной живописи",
                       "Fedoskino Factory of Miniature Painting", "Федоскино", "Fedoskino",
                       org_url="https://yandex.com/maps/org/fedoskinskaya_fabrika_miniatyurnoy_zhivopisi/123799425374/"),
    "official_site": "https://fabrica-fedoskino.ru/",
    "sources": [
        {"title": "Wikipedia (RU) — Федоскинская миниатюра", "url": "https://ru.wikipedia.org/wiki/Федоскинская_миниатюра"},
        {"title": "Путеводитель Подмосковья (welcome.mosreg.ru) — Федоскинская фабрика миниатюрной живописи", "url": "https://welcome.mosreg.ru/ideas/fedoskinskaa-fabrika-miniaturnoj-zivopisi"},
    ],
    "tags": ["museum", "folk-craft", "lacquer-miniature", "fedoskino", "mytishchi", "day-trip", "moscow-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 3) GZHEL PORCELAIN FACTORY
GZHEL = {
    "id": f"{MO}-gzhel-porcelain-factory",
    "slug": "gzhel-porcelain-factory",
    "region": MO, "region_name_vi": MO_VI, "federal_district": MO_FED,
    "name_vi": "Nhà máy sứ Gzhel (Gzhelsky farforovy zavod)",
    "name_ru": "Гжельский фарфоровый завод",
    "name_en": "Gzhel Porcelain Factory",
    "categories": ["museum"],
    "coordinates": {"lat": 55.600198, "lon": 38.452205},
    "address_vi": "Phố Novaya 45A, làng Rechitsy (vùng Gzhel), huyện Ramensky, Tỉnh Moskva; cách trung tâm Moskva khoảng 55 km về phía đông nam.",
    "rating": None,
    "presentation_short_vi": "Gzhel là vùng làng nghề gốm sứ trứ danh ở đông nam Moskva, nổi tiếng khắp thế giới với đồ sứ vẽ tay hoạ tiết coban xanh trên nền trắng. Nhà máy sứ Gzhel mở tour tham quan dây chuyền, có bảo tàng mỹ nghệ và lớp học vẽ để khách tự trang trí sản phẩm.",
    "presentation_long_vi": "Cách Moskva chừng 55 km về phía đông nam, Gzhel là tên gọi chung của một cụm làng có truyền thống làm gốm lâu đời, được nhắc tới từ thế kỷ 14. Từ thế kỷ 19, phong cách đặc trưng của vùng định hình: hoạ tiết vẽ tay bằng men coban cho ra sắc xanh lam trên nền sứ trắng, với những bông hồng, đường cong và hoa văn mềm mại đã trở thành 'thương hiệu' của sứ Nga. Nhà máy sứ Gzhel (đặt tại làng Rechitsy) ngày nay là một trong những cơ sở lớn nhất chuyên sản xuất sứ truyền thống vẽ tay coban. Nơi đây đón khách tham quan trọn chuỗi sản xuất - từ tạo hình, tráng men đến vẽ và nung - kèm một bảo tàng trưng bày sản phẩm mỹ nghệ và các buổi học vẽ ('master-class') để du khách tự tay trang trí một chiếc cốc hay đĩa nhỏ, sau đó sản phẩm được nung men và có thể nhận sau. Đây là điểm đến hấp dẫn cả với gia đình có trẻ nhỏ, giúp hiểu vì sao sứ Gzhel lại được yêu mến đến vậy; có thể kết hợp mua đồ tại cửa hàng của nhà máy với giá xưởng.",
    "highlights_vi": [
        "Vùng làng nghề gốm sứ trứ danh với hoạ tiết coban xanh trên nền trắng - biểu tượng của sứ Nga.",
        "Tour xem trọn dây chuyền sản xuất sứ vẽ tay, kèm bảo tàng mỹ nghệ tại nhà máy.",
        "Lớp học vẽ ('master-class') để du khách tự trang trí sản phẩm; cửa hàng bán đồ sứ giá xưởng.",
    ],
    "practical": {
        "hours_vi": "Đón khách theo tour đặt trước; nhà máy thường mở cửa từ khoảng 9:00, nghỉ theo lịch riêng - nên đặt trước.",
        "ticket_vi": "Vé tour tham quan khoảng 600₽ (người lớn), 300₽ (trẻ 4-14 tuổi); lớp học vẽ khoảng 300-550₽ tuỳ chương trình (tham khảo, có thể thay đổi).",
        "duration_vi": "Khoảng 1,5-2 giờ.",
        "best_time_vi": "Quanh năm (trong nhà).",
        "tips_vi": "Bắt buộc đặt tour trước. Từ Moskva có tàu ngoại ô tới ga Gzhel rồi đi tiếp; tự lái theo cao tốc M7/Egoryevskoye tiện hơn. Ghé cửa hàng của nhà máy để mua sứ chính hãng.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(55.600198, 38.452205, "Гжельский фарфоровый завод", "Gzhel Porcelain Factory",
                       "Гжель", "Gzhel",
                       org_url="https://yandex.com/maps/org/gzhelskiy_farforovy_zavod/51312399657/"),
    "official_site": "https://farfor-gzhel.ru/",
    "sources": [
        {"title": "Yandex Maps — Гжельский фарфоровый завод", "url": "https://yandex.com/maps/org/gzhelskiy_farforovy_zavod/51312399657/"},
        {"title": "Путеводитель Подмосковья (welcome.mosreg.ru) — Гжельский фарфор", "url": "https://welcome.mosreg.ru/ideas/gzel-skij-farfor"},
    ],
    "tags": ["museum", "folk-craft", "porcelain", "gzhel", "ramensky", "day-trip", "moscow-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 4) MUSEUM OF RUSSIAN SHAWL (PAVLOVSKY POSAD)
PLATOK = {
    "id": f"{MO}-pavlovsky-posad-shawl-museum",
    "slug": "pavlovsky-posad-shawl-museum",
    "region": MO, "region_name_vi": MO_VI, "federal_district": MO_FED,
    "name_vi": "Bảo tàng Lịch sử Khăn choàng & Khăn Sal Nga (Pavlovsky Posad)",
    "name_ru": "Музей истории русского платка и шали",
    "name_en": "Museum of the History of the Russian Shawl and Scarf",
    "categories": ["museum"],
    "coordinates": {"lat": 55.779906, "lon": 38.649679},
    "address_vi": "Quảng trường Revolyutsii 9/1, thành phố Pavlovsky Posad, Tỉnh Moskva; cách trung tâm Moskva khoảng 65 km về phía đông.",
    "rating": None,
    "presentation_short_vi": "Đây là bảo tàng duy nhất ở Nga dành riêng cho chiếc khăn choàng. Thành phố Pavlovsky Posad nổi danh với những chiếc khăn len in hoa văn bó hoa hồng rực rỡ - một phần không thể thiếu của trang phục truyền thống Nga; bảo tàng giới thiệu lịch sử và hàng trăm mẫu khăn quý.",
    "presentation_long_vi": "Pavlovsky Posad, thành phố cách Moskva khoảng 65 km về phía đông, từ thế kỷ 19 đã nổi tiếng với nghề dệt và in khăn choàng len (platok). Những chiếc khăn Pavlovoposad với bó hoa hồng và hoa văn đối xứng rực rỡ trên nền đỏ thắm, đen hay kem đã trở thành biểu tượng của phục sức dân gian Nga, được phụ nữ nhiều thế hệ trân trọng. Bảo tàng Lịch sử Khăn choàng và Sal Nga, mở cửa năm 2002, là bảo tàng duy nhất trong cả nước chuyên về đề tài này. Bộ sưu tập giới thiệu quá trình phát triển của nghề, từ những mẫu khăn dệt kim tuyến thế kỷ 18-19 tới khăn len in hoa đặc trưng của Pavlovsky Posad, cùng khăn lụa, khăn thêu và các phụ kiện đi kèm. Qua từng gian trưng bày, khách hình dung được sự tinh tế trong thiết kế hoa văn và vai trò của chiếc khăn trong đời sống, lễ hội và thời trang Nga. Đây là điểm dừng chân giàu màu sắc, dễ kết hợp với việc mua khăn chính hãng tại thành phố - món quà lưu niệm mang đậm hồn Nga.",
    "highlights_vi": [
        "Bảo tàng duy nhất ở Nga dành riêng cho chiếc khăn choàng, mở cửa từ năm 2002.",
        "Bộ sưu tập phong phú khăn len in hoa Pavlovoposad cùng khăn lụa, khăn kim tuyến qua nhiều thế kỷ.",
        "Cơ hội hiểu về hoa văn bó hoa hồng đặc trưng và mua khăn chính hãng làm quà.",
    ],
    "practical": {
        "hours_vi": "Thường mở 09:00-17:00; nghỉ 'ngày vệ sinh' vào thứ Ba cuối tháng - nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào cửa mức phổ thông, giá phải chăng (tham khảo trực tiếp bảo tàng).",
        "duration_vi": "Khoảng 1-1,5 giờ.",
        "best_time_vi": "Quanh năm (trong nhà).",
        "tips_vi": "Từ Moskva đi tàu ngoại ô tuyến Gorkovskoye đến ga Pavlovsky Posad (khoảng 1,5 giờ). Kết hợp ghé cửa hàng khăn Pavlovoposad để mua quà.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(55.779906, 38.649679, "Музей истории русского платка и шали",
                       "Museum of the History of the Russian Shawl and Scarf", "Павловский Посад", "Pavlovsky Posad"),
    "official_site": "http://muzeyplatka.ppmvk.ru/",
    "sources": [
        {"title": "Культура.РФ — Музей истории русского платка и шали", "url": "https://www.culture.ru/institutes/24584/muzei-istorii-russkogo-platka-i-shali"},
        {"title": "Музеи России (museum.ru) — Музей истории русского платка и шали", "url": "http://www.museum.ru/M2926"},
    ],
    "tags": ["museum", "folk-craft", "shawl", "textile", "pavlovsky-posad", "day-trip", "moscow-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 5) BOGORODSKOYE WOOD CARVING FACTORY
BOGORODSKOYE = {
    "id": f"{MO}-bogorodskoye-toy-factory",
    "slug": "bogorodskoye-toy-factory",
    "region": MO, "region_name_vi": MO_VI, "federal_district": MO_FED,
    "name_vi": "Xưởng khắc gỗ nghệ thuật Bogorodskoye & Bảo tàng đồ chơi",
    "name_ru": "Богородская фабрика художественной резьбы по дереву",
    "name_en": "Bogorodskoye Wood Carving Factory",
    "categories": ["museum"],
    "coordinates": {"lat": 56.495869, "lon": 38.18797},
    "address_vi": "Nhà 79Б, thị trấn Bogorodskoye, bên sông Kunya, huyện Sergiev Posad, Tỉnh Moskva; cách Sergiev Posad khoảng 25-27 km về phía bắc.",
    "rating": None,
    "presentation_short_vi": "Bogorodskoye là quê hương của nghề khắc đồ chơi gỗ mộc dân gian Nga có lịch sử hơn 500 năm. Nổi tiếng nhất là những món đồ chơi chuyển động như 'đàn gà mổ thóc' hay 'người và gấu gõ búa'. Xưởng còn hoạt động và có bảo tàng đồ chơi kèm lớp học nghề.",
    "presentation_long_vi": "Bên dòng sông Kunya, cách Sergiev Posad chừng 25-27 km về phía bắc, thị trấn Bogorodskoye gắn liền với nghề khắc đồ chơi gỗ - một trong những nghề thủ công dân gian đặc sắc nhất của nước Nga, được cho là có lịch sử hơn 500 năm. Đồ chơi Bogorodskoye thường làm từ gỗ mềm như bồ đề, dẻ gai, dương, để mộc không sơn hoặc chỉ tô điểm nhẹ, phô ra vẻ đẹp của thớ gỗ và nét dao khắc. Đặc trưng nhất là những món đồ chơi cơ học chuyển động nhờ thanh trượt hoặc quả nặng: hình 'đàn gà mổ thóc' xoay tròn, hay 'người nông dân và chú gấu thay nhau gõ búa' - hình ảnh đã đi vào ký ức tuổi thơ của nhiều thế hệ. Năm 1913, các thợ khắc lập hợp tác xã 'Người thợ khắc Bogorodskoye', mở trường dạy nghề; đến năm 1960 hợp tác xã chuyển thành xưởng khắc gỗ nghệ thuật. Tại xưởng có bảo tàng đồ chơi trưng bày hàng trăm mẫu tượng và đồ chơi qua các thời kỳ, đồng thời tổ chức tham quan và lớp học khắc để du khách tự làm một món đồ chơi đơn giản - trải nghiệm lý thú, đặc biệt với trẻ em, và dễ kết hợp trong hành trình khám phá Sergiev Posad cùng Vành đai Vàng.",
    "highlights_vi": [
        "Nghề khắc đồ chơi gỗ mộc dân gian hơn 500 năm tuổi - một biểu tượng của mỹ nghệ Nga.",
        "Những món đồ chơi chuyển động kinh điển: 'đàn gà mổ thóc', 'người và gấu gõ búa'.",
        "Xưởng còn hoạt động, có bảo tàng đồ chơi và lớp học khắc gỗ cho du khách.",
    ],
    "practical": {
        "hours_vi": "Bảo tàng thường mở 10:00-16:00; tham quan xưởng và lớp học cần đăng ký trước qua điện thoại.",
        "ticket_vi": "Vé bảo tàng mức phổ thông (khoảng 100-150₽, tham khảo); lớp học khắc tính phí riêng.",
        "duration_vi": "Khoảng 1-1,5 giờ.",
        "best_time_vi": "Quanh năm (trong nhà).",
        "tips_vi": "Nên đặt trước, nhất là khi đi lớp học khắc. Đường tới Bogorodskoye khá xa Sergiev Posad, tự lái sẽ chủ động hơn; kết hợp tham quan Trinity Lavra trong ngày.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(56.495869, 38.18797, "Богородская фабрика художественной резьбы по дереву",
                       "Bogorodskoye Wood Carving Factory", "Богородское", "Bogorodskoye"),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Богородская резьба", "url": "https://ru.wikipedia.org/wiki/Богородская_резьба"},
        {"title": "Путеводитель Подмосковья (welcome.mosreg.ru) — Богородская фабрика художественной резьбы по дереву", "url": "https://welcome.mosreg.ru/ideas/kurocki-medvedi-i-muzicki-s-toporikami-v-tradicionnom-podmoskovnom-promysle"},
    ],
    "tags": ["museum", "folk-craft", "wood-carving", "toys", "bogorodskoye", "sergiev-posad", "day-trip", "moscow-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 6) STARO-GOLUTVIN MONASTERY (KOLOMNA)
GOLUTVIN = {
    "id": f"{MO}-staro-golutvin-monastery",
    "slug": "staro-golutvin-monastery",
    "region": MO, "region_name_vi": MO_VI, "federal_district": MO_FED,
    "name_vi": "Tu viện Bogoyavlensky Staro-Golutvin (Kolomna)",
    "name_ru": "Богоявленский Старо-Голутвин монастырь",
    "name_en": "Bogoyavlensky Staro-Golutvin Monastery",
    "categories": ["church"],
    "coordinates": {"lat": 55.079731, "lon": 38.832162},
    "address_vi": "Phố Golutvinskaya 11, thành phố Kolomna, Tỉnh Moskva; ở rìa đông nam Kolomna, gần nơi sông Moskva hợp lưu với sông Oka.",
    "rating": None,
    "presentation_short_vi": "Tu viện Staro-Golutvin do chính Thánh Sergius thành Radonezh sáng lập năm 1385 theo lời mời của đại công Dmitry Donskoy. Quần thể nổi bật với những tháp canh mảnh mai theo phong cách tân Gothic, được cho là do kiến trúc sư Matvei Kazakov thiết kế.",
    "presentation_long_vi": "Nằm ở rìa đông nam Kolomna, gần nơi sông Moskva đổ vào sông Oka, Tu viện Bogoyavlensky Staro-Golutvin là một trong những tu viện gắn với tên tuổi Thánh Sergius thành Radonezh. Theo truyền thống, ngài lập tu viện năm 1385 theo lời mời của đại công Dmitry Donskoy, khi tới Kolomna để hoà giải các vương công; đích thân Thánh Sergius chọn đất và ban phước cho ngôi thánh đường đầu tiên. Trải qua nhiều thế kỷ, tu viện là trung tâm tâm linh quan trọng của vùng Kolomna. Diện mạo hiện nay mang dấu ấn cuối thế kỷ 18 - đầu thế kỷ 19, đặc biệt là hàng tường bao và những tháp góc cao vút, trang trí răng cưa theo phong cách tân Gothic (giả Gothic) đặc trưng, thường được gán cho kiến trúc sư trứ danh Matvei Kazakov. Trung tâm quần thể là Nhà thờ Chúa Hiển Linh (Bogoyavlensky). Sau thời kỳ đóng cửa dưới thời Xô Viết, tu viện được khôi phục và nay còn là nơi đặt chủng viện Kolomna. Với bề dày lịch sử và kiến trúc độc đáo, đây là điểm đến ý nghĩa để bổ sung cho hành trình khám phá thành phố cổ Kolomna, bên cạnh Kremlin và các bảo tàng nổi tiếng.",
    "highlights_vi": [
        "Do Thánh Sergius thành Radonezh sáng lập năm 1385 theo lời mời của Dmitry Donskoy.",
        "Những tháp góc tân Gothic (giả Gothic) mảnh mai, thường được gán cho kiến trúc sư M. Kazakov.",
        "Trung tâm là Nhà thờ Chúa Hiển Linh; nay còn là nơi đặt chủng viện Kolomna.",
    ],
    "practical": {
        "hours_vi": "Là tu viện đang hoạt động, mở cửa hằng ngày theo giờ lễ (khoảng sáng sớm đến chiều tối).",
        "ticket_vi": "Vào tự do (khuyến khích công đức tuỳ tâm).",
        "duration_vi": "Khoảng 45 phút - 1 giờ.",
        "best_time_vi": "Quanh năm; ngày trời quang đẹp nhất để ngắm các tháp tân Gothic.",
        "tips_vi": "Trang phục kín đáo khi vào nhà thờ. Gần ga Golutvin (Kolomna); dễ kết hợp tham quan Kremlin Kolomna và Bảo tàng Pastila trong cùng ngày.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(55.079731, 38.832162, "Богоявленский Старо-Голутвин монастырь",
                       "Bogoyavlensky Staro-Golutvin Monastery", "Коломна", "Kolomna"),
    "official_site": None,
    "sources": [
        {"title": "Соборы.ру — Коломна, Богоявленский Старо-Голутвин монастырь", "url": "https://sobory.ru/article/?object=01135"},
        {"title": "Туристер.Ру — Старо-Голутвин монастырь, Коломна", "url": "https://www.tourister.ru/world/europe/russia/city/kolomna/temples/21702"},
    ],
    "tags": ["church", "monastery", "orthodox", "sergius-of-radonezh", "kolomna", "neo-gothic", "day-trip", "moscow-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 7) BOBRENEV MONASTERY (KOLOMNA)
BOBRENEV = {
    "id": f"{MO}-bobrenev-monastery",
    "slug": "bobrenev-monastery",
    "region": MO, "region_name_vi": MO_VI, "federal_district": MO_FED,
    "name_vi": "Tu viện Bobrenev - Sinh Nhật Đức Mẹ (Kolomna)",
    "name_ru": "Богородице-Рождественский Бобренёв монастырь",
    "name_en": "Bobrenev Monastery",
    "categories": ["church"],
    "coordinates": {"lat": 55.118951, "lon": 38.76024},
    "address_vi": "Làng Staroye Bobrenevo, cách Kremlin Kolomna khoảng 3 km về phía bắc qua sông Moskva, Tỉnh Moskva.",
    "rating": None,
    "presentation_short_vi": "Tu viện Bobrenev tương truyền được lập cuối thế kỷ 14 sau chiến thắng Kulikovo năm 1380, theo lời khấn của đại công Dmitry Donskoy và viên tướng Dmitri Bobrok. Quần thể trắng muốt nằm giữa cánh đồng bên kia sông, đối diện Kremlin Kolomna, tạo khung cảnh thanh bình đặc trưng.",
    "presentation_long_vi": "Nằm giữa cánh đồng thoáng đãng bên kia sông Moskva, cách Kremlin Kolomna khoảng 3 km, Tu viện Bobrenev mang trong mình một truyền thuyết gắn với trang sử oai hùng của nước Nga. Theo lưu truyền, tu viện được dựng vào cuối thế kỷ 14 sau chiến thắng vang dội trước quân Mông Cổ - Tatar trong trận Kulikovo năm 1380, như một lời tạ ơn theo lời khấn của đại công Dmitry Donskoy và viên tướng thân cận Dmitri Mikhailovich Volynets - người mang biệt danh 'Bobrok', từ đó thành tên tu viện. Sử liệu ghi nhận nơi đây từ năm 1578. Trung tâm quần thể là Nhà thờ Sinh Nhật Đức Mẹ và Nhà thờ Icon Đức Mẹ Feodorovskaya, cùng vòng tường bao và tháp trang trí. Sau thời gian dài hoang phế thời Xô Viết, tu viện được trùng tu và hồi sinh, giữ được vẻ tĩnh mịch hiếm có. Chính vị trí biệt lập giữa đồng nội, với những mái vòm trắng nổi bật trên nền trời và hình bóng Kremlin Kolomna phía xa, khiến Bobrenev trở thành một trong những khung cảnh được yêu thích khi khám phá vùng Kolomna - lý tưởng cho những ai muốn tìm sự yên tĩnh và góc ảnh đẹp.",
    "highlights_vi": [
        "Truyền thống gắn với chiến thắng Kulikovo 1380 và lời khấn của Dmitry Donskoy cùng tướng Bobrok.",
        "Nhà thờ Sinh Nhật Đức Mẹ và Nhà thờ Icon Feodorovskaya giữa khung cảnh đồng nội thanh bình.",
        "Tầm nhìn đặc trưng hướng về Kremlin Kolomna bên kia sông - góc ngắm cảnh và chụp ảnh đẹp.",
    ],
    "practical": {
        "hours_vi": "Tu viện đang hoạt động, mở cửa hằng ngày theo giờ lễ.",
        "ticket_vi": "Vào tự do (khuyến khích công đức tuỳ tâm).",
        "duration_vi": "Khoảng 45 phút - 1 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu, ngày trời quang để ngắm quần thể trắng trên nền đồng xanh.",
        "tips_vi": "Trang phục kín đáo. Đường vào băng qua cánh đồng, nên đi giày thoải mái; dễ kết hợp với tham quan Kremlin Kolomna gần đó.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(55.118951, 38.76024, "Богородице-Рождественский Бобренёв монастырь",
                       "Bobrenev Monastery", "Старое Бобренево", "Staroye Bobrenevo"),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Бобренев монастырь", "url": "https://ru.wikipedia.org/wiki/Бобренев_монастырь"},
        {"title": "Соборы.ру — Старое Бобренево, Бобренёв монастырь", "url": "https://sobory.ru/article/?object=01130"},
    ],
    "tags": ["church", "monastery", "orthodox", "kulikovo", "kolomna", "day-trip", "moscow-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 8) VVEDENSKY VLADYCHNY CONVENT (SERPUKHOV)
VLADYCHNY = {
    "id": f"{MO}-vvedensky-vladychny-convent",
    "slug": "vvedensky-vladychny-convent",
    "region": MO, "region_name_vi": MO_VI, "federal_district": MO_FED,
    "name_vi": "Tu viện nữ Vvedensky Vladychny (Serpukhov)",
    "name_ru": "Введенский Владычный монастырь",
    "name_en": "Vvedensky Vladychny Convent",
    "categories": ["church"],
    "coordinates": {"lat": 54.898611, "lon": 37.398889},
    "address_vi": "Phố Oktyabrskaya 40, thành phố Serpukhov, Tỉnh Moskva; ở phía nam thành phố, gần sông Nara và sông Oka.",
    "rating": None,
    "presentation_short_vi": "Được lập năm 1360 bởi Thánh Alexy - Giám mục Moskva, theo một thị kiến của Đức Mẹ, đây là một trong những tu viện cổ nhất vùng Serpukhov. Nơi đây gắn với icon 'Chén Thánh Vô Tận' (Neupivaemaya Chasha), được người hành hương tìm đến cầu nguyện.",
    "presentation_long_vi": "Ở phía nam Serpukhov, gần chỗ sông Nara đổ vào sông Oka, Tu viện Vvedensky Vladychny là một trong những tu viện lâu đời nhất của vùng, được lập năm 1360. Theo truyền thống, Thánh Alexy - Giám mục Moskva - đã dựng tu viện theo một thị kiến của Đức Mẹ và giao cho môn đệ là Thánh Varlaam trông coi. Trung tâm quần thể là Nhà thờ Dâng Đức Mẹ vào Đền thờ (Vvedensky) cùng nhà thờ Thánh George trong khối nhà ăn và tháp chuông. Trải qua thăng trầm, tu viện từng là nam viện rồi chuyển thành nữ viện; sau thời kỳ Xô Viết bị đóng cửa, nơi đây được khôi phục thành một nữ tu viện đang hoạt động. Vladychny đặc biệt gắn với sự xuất hiện của icon 'Chén Thánh Vô Tận' (Neupivaemaya Chasha) vào năm 1878 - bức ảnh thánh được tôn kính như nguồn trợ giúp cho những ai muốn dứt bỏ nghiện ngập; ngày nay cả Tu viện Vladychny và Tu viện Vysotsky gần đó đều gìn giữ những bản icon được sùng kính này, khiến Serpukhov trở thành điểm hành hương quan trọng. Không gian cổ kính, trầm mặc sau tường bao là nơi lý tưởng để tĩnh tâm và tìm hiểu chiều sâu văn hoá Chính Thống giáo Nga.",
    "highlights_vi": [
        "Một trong những tu viện cổ nhất vùng Serpukhov, lập năm 1360 bởi Thánh Alexy - Giám mục Moskva.",
        "Gắn với sự xuất hiện của icon 'Chén Thánh Vô Tận' (Neupivaemaya Chasha) năm 1878 - điểm hành hương nổi tiếng.",
        "Nhà thờ Vvedensky và nhà thờ Thánh George cổ kính; nay là nữ tu viện đang hoạt động.",
    ],
    "practical": {
        "hours_vi": "Là nữ tu viện đang hoạt động, mở cửa hằng ngày theo giờ lễ.",
        "ticket_vi": "Vào tự do (khuyến khích công đức tuỳ tâm).",
        "duration_vi": "Khoảng 45 phút - 1 giờ.",
        "best_time_vi": "Quanh năm; các ngày lễ Chính Thống giáo đông người hành hương.",
        "tips_vi": "Trang phục kín đáo (nữ nên mang khăn trùm đầu, mặc váy dài). Có thể kết hợp viếng Tu viện Vysotsky và Bảo tàng Lịch sử - Nghệ thuật Serpukhov trong cùng ngày.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(54.898611, 37.398889, "Введенский Владычный монастырь", "Vvedensky Vladychny Convent",
                       "Серпухов", "Serpukhov",
                       org_url="https://yandex.com/maps/org/vvedenskiy_vladychniy_zhenskiy_monastyr/1048532540/"),
    "official_site": None,
    "sources": [
        {"title": "Соборы.ру — Серпухов, Введенский Владычный монастырь", "url": "https://sobory.ru/article/?object=00622"},
        {"title": "Yandex Maps — Введенский Владычний женский монастырь", "url": "https://yandex.com/maps/org/vvedenskiy_vladychniy_zhenskiy_monastyr/1048532540/"},
    ],
    "tags": ["church", "monastery", "convent", "orthodox", "pilgrimage", "serpukhov", "day-trip", "moscow-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 9) BORISOGLEBSKY MONASTERY (DMITROV)
BORISOGLEBSKY = {
    "id": f"{MO}-borisoglebsky-monastery-dmitrov",
    "slug": "borisoglebsky-monastery-dmitrov",
    "region": MO, "region_name_vi": MO_VI, "federal_district": MO_FED,
    "name_vi": "Tu viện Borisoglebsky (Dmitrov)",
    "name_ru": "Борисоглебский монастырь (Дмитров)",
    "name_en": "Borisoglebsky Monastery (Dmitrov)",
    "categories": ["church"],
    "coordinates": {"lat": 56.342879, "lon": 37.531077},
    "address_vi": "Phố Minina 4, thành phố Dmitrov, Tỉnh Moskva; ngay gần quần thể Kremlin Dmitrov, cách trung tâm Moskva khoảng 65 km về phía bắc.",
    "rating": None,
    "presentation_short_vi": "Tu viện Borisoglebsky ở Dmitrov có từ không muộn hơn năm 1472, với trung tâm là Nhà thờ đá trắng thờ hai Thánh Boris và Gleb (khoảng thập niên 1520). Quần thể tường thành và tháp canh nhỏ nhắn nằm ngay sát Kremlin Dmitrov nổi tiếng.",
    "presentation_long_vi": "Tọa lạc ngay gần quần thể Kremlin Dmitrov, Tu viện Borisoglebsky là một trong những điểm nhấn của thành phố cổ phía bắc Moskva. Sử liệu ghi nhận tu viện từ không muộn hơn năm 1472, dù truyền thống cho rằng nơi đây có thể còn xưa hơn. Trái tim của quần thể là Nhà thờ đá trắng thờ hai vị thánh tử đạo đầu tiên của nước Nga - Boris và Gleb, dựng vào khoảng thập niên 1520, mang dáng vẻ mộc mạc, cân đối tiêu biểu cho kiến trúc Nga thế kỷ 16. Bao quanh là vòng tường gạch với các tháp góc và cổng thánh, tạo nên hình ảnh một tu viện - pháo đài thu nhỏ. Bên trong còn có nhà thờ nhỏ, khu nhà ở của tu sĩ và nhà nguyện. Sau khi bị đóng cửa và dùng vào nhiều mục đích thời Xô Viết, tu viện đã được trả lại cho Giáo hội và trùng tu, nay là nam tu viện đang hoạt động. Nhờ vị trí liền kề Kremlin Dmitrov với các đài lũy đất, nhà thờ chính toà Đức Mẹ Lên Trời và những công trình lịch sử khác, Borisoglebsky rất dễ đưa vào một chuyến đi trong ngày để cảm nhận trọn vẹn không khí của một đô thị cổ vùng ven Moskva.",
    "highlights_vi": [
        "Tu viện có từ không muộn hơn năm 1472, một trong những công trình cổ của Dmitrov.",
        "Nhà thờ đá trắng thờ hai Thánh Boris và Gleb (khoảng thập niên 1520) theo kiến trúc Nga thế kỷ 16.",
        "Vòng tường và tháp góc như một tu viện - pháo đài thu nhỏ, ngay cạnh Kremlin Dmitrov.",
    ],
    "practical": {
        "hours_vi": "Tu viện đang hoạt động, mở cửa hằng ngày theo giờ lễ.",
        "ticket_vi": "Vào tự do (khuyến khích công đức tuỳ tâm).",
        "duration_vi": "Khoảng 30-45 phút.",
        "best_time_vi": "Quanh năm.",
        "tips_vi": "Trang phục kín đáo. Từ Moskva đi tàu ngoại ô tuyến Savyolovsky đến Dmitrov; kết hợp tham quan Kremlin Dmitrov và phố đi bộ trong cùng ngày.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(56.342879, 37.531077, "Борисоглебский монастырь", "Borisoglebsky Monastery",
                       "Дмитров", "Dmitrov"),
    "official_site": None,
    "sources": [
        {"title": "Соборы.ру — Дмитров, Борисоглебский мужской монастырь", "url": "https://sobory.ru/article/?object=00399"},
        {"title": "Соборы.ру — Дмитров, Собор Бориса и Глеба", "url": "https://sobory.ru/article/?object=09508"},
    ],
    "tags": ["church", "monastery", "orthodox", "dmitrov", "history", "day-trip", "moscow-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 10) VOLOKOLAMSK KREMLIN
VOLOKOLAMSK = {
    "id": f"{MO}-volokolamsk-kremlin",
    "slug": "volokolamsk-kremlin",
    "region": MO, "region_name_vi": MO_VI, "federal_district": MO_FED,
    "name_vi": "Kremlin Volokolamsk (Đồi Nhà Thờ)",
    "name_ru": "Волоколамский кремль",
    "name_en": "Volokolamsk Kremlin",
    "categories": ["fortress", "church"],
    "coordinates": {"lat": 56.037917, "lon": 35.957748},
    "address_vi": "Phố Gorval 1 (Đồi Nhà Thờ), thành phố Volokolamsk, Tỉnh Moskva; cách trung tâm Moskva khoảng 100 km về phía tây bắc.",
    "rating": None,
    "presentation_short_vi": "Trên đỉnh Đồi Nhà Thờ giữa thành phố Volokolamsk là quần thể Kremlin cổ, với điểm nhấn là Nhà thờ Phục Sinh bằng đá trắng cuối thế kỷ 15 - một trong những nhà thờ cổ nhất vùng Moskva. Cạnh đó là Nhà thờ Thánh Nikolai thế kỷ 19 và tháp chuông, nay là bảo tàng.",
    "presentation_long_vi": "Volokolamsk là một trong những thị trấn lâu đời nhất của vùng đất Moskva, được nhắc tới lần đầu năm 1135 - còn sớm hơn cả Moskva. Điểm đến trung tâm của thành phố là Kremlin nằm trên Đồi Nhà Thờ (Sobornaya gora), một mô đất cao được bao quanh bởi tường rào và tháp trang trí thế kỷ 19 - đầu 20. Nổi bật nhất là Nhà thờ Phục Sinh (Voskresensky) bằng đá trắng, dựng vào cuối thế kỷ 15, thuộc hàng những nhà thờ cổ nhất còn lại của vùng Moskva, với khối kiến trúc vuông vức, trang trí chạm khắc mộc mạc tiêu biểu cho nghệ thuật Nga trung đại. Bên cạnh là Nhà thờ Thánh Nikolai xây thế kỷ 19 theo phong cách Nga - Byzantine, tưởng niệm những người lính ngã xuống trong Chiến tranh Krym, và một tháp chuông vươn cao nối liền hai công trình. Ngày nay cả quần thể là bảo tàng lịch sử - kiến trúc: khách có thể vào xem trưng bày, leo tháp chuông để ngắm toàn cảnh thành phố và vùng đồng quê xung quanh. Vị trí trên cao cùng sự hoà quyện của kiến trúc nhiều thời kỳ khiến Kremlin Volokolamsk là điểm dừng chân hấp dẫn khi khám phá miền tây bắc Tỉnh Moskva, có thể kết hợp với Tu viện Iosifo-Volotsky gần đó.",
    "highlights_vi": [
        "Nhà thờ Phục Sinh đá trắng cuối thế kỷ 15 - một trong những nhà thờ cổ nhất vùng Moskva.",
        "Quần thể trên Đồi Nhà Thờ với Nhà thờ Thánh Nikolai thế kỷ 19 và tháp chuông cho tầm nhìn toàn cảnh.",
        "Nay là bảo tàng lịch sử - kiến trúc; Volokolamsk được nhắc tới từ năm 1135, sớm hơn cả Moskva.",
    ],
    "practical": {
        "hours_vi": "Bảo tàng thường mở 09:00-17:00, nghỉ thứ Hai và ngày vệ sinh cuối tháng - nên kiểm tra lịch trước.",
        "ticket_vi": "Vé vào bảo tàng và leo tháp chuông mức phổ thông (tham khảo tại chỗ).",
        "duration_vi": "Khoảng 1-1,5 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu, ngày trời quang để lên tháp chuông ngắm cảnh.",
        "tips_vi": "Từ Moskva đi tàu ngoại ô tuyến Rizhsky hoặc xe buýt tới Volokolamsk. Kết hợp thăm Tu viện Iosifo-Volotsky và các đài tưởng niệm trận Moskva 1941 trong vùng.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(56.037917, 35.957748, "Волоколамский кремль", "Volokolamsk Kremlin",
                       "Волоколамск", "Volokolamsk"),
    "official_site": None,
    "sources": [
        {"title": "Соборы.ру — Воскресенский собор на Соборной горке, Волоколамск", "url": "https://sobory.ru/article/?object=00395"},
        {"title": "Wikipedia (RU) — Воскресенский собор (Волоколамск)", "url": "https://ru.wikipedia.org/wiki/Воскресенский_собор_(Волоколамск)"},
    ],
    "tags": ["fortress", "kremlin", "church", "museum", "volokolamsk", "history", "day-trip", "moscow-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 11) VEREYA NATIVITY CATHEDRAL (GORODOK)
VEREYA = {
    "id": f"{MO}-vereya-nativity-cathedral",
    "slug": "vereya-nativity-cathedral",
    "region": MO, "region_name_vi": MO_VI, "federal_district": MO_FED,
    "name_vi": "Nhà thờ Sinh Nhật Chúa Kitô & Gò thành Verea (Gorodok)",
    "name_ru": "Собор Рождества Христова (Верея)",
    "name_en": "Nativity of Christ Cathedral (Vereya)",
    "categories": ["church", "monument"],
    "coordinates": {"lat": 55.344131, "lon": 36.188321},
    "address_vi": "Khu Gò thành (Gorodok) trên bờ cao sông Protva, thành phố Verea, huyện Naro-Fominsk, Tỉnh Moskva; cách trung tâm Moskva khoảng 110 km về phía tây nam.",
    "rating": None,
    "presentation_short_vi": "Verea là một trong những thành phố nhỏ và cổ kính nhất Tỉnh Moskva. Trên gò thành đắp đất (Gorodok) bên bờ cao sông Protva sừng sững Nhà thờ Sinh Nhật Chúa Kitô, dưới chân là mộ của tướng Ivan Dorokhov - vị anh hùng giải phóng Verea trong cuộc Chiến tranh Vệ quốc 1812.",
    "presentation_long_vi": "Verea, thành phố nhỏ bên sông Protva cách Moskva khoảng 110 km về phía tây nam, mang dáng vẻ trầm mặc của một đô thị tỉnh lẻ cổ kính, từng là trung tâm buôn bán sầm uất trên tuyến đường thương mại xưa. Trái tim lịch sử của thành phố là Gorodok - gò thành đắp đất từ thời trung cổ trên bờ cao sông Protva, nơi vẫn còn nhận ra dấu tích lũy đất của toà thành gỗ năm nào. Ngự trên gò là Nhà thờ Sinh Nhật Chúa Kitô, khởi dựng từ thế kỷ 16 và được xây lại, tu bổ qua nhiều thời kỳ, với khối tháp chuông cao trở thành điểm nhấn của toàn cảnh thị trấn. Nhà thờ và gò thành gắn liền với ký ức về cuộc Chiến tranh Vệ quốc năm 1812: tướng Ivan Dorokhov đã chỉ huy quân Nga đánh chiếm lại Verea từ tay quân Napoléon, và theo di nguyện, ông được an táng ngay bên nhà thờ; một đài tưởng niệm vị tướng được dựng tại đây. Đứng trên gò thành phóng tầm mắt xuống dòng Protva uốn lượn và những mái nhà cổ, du khách cảm nhận rõ vẻ đẹp yên bình, đậm chất Nga của Verea - một điểm đến lý tưởng cho chuyến khám phá miền tây nam Tỉnh Moskva.",
    "highlights_vi": [
        "Gò thành đắp đất (Gorodok) thời trung cổ trên bờ cao sông Protva - lõi lịch sử của Verea.",
        "Nhà thờ Sinh Nhật Chúa Kitô (khởi dựng thế kỷ 16) với tháp chuông là điểm nhấn toàn cảnh thị trấn.",
        "Mộ và đài tưởng niệm tướng Ivan Dorokhov - anh hùng giải phóng Verea năm 1812.",
    ],
    "practical": {
        "hours_vi": "Nhà thờ đang hoạt động, mở cửa theo giờ lễ; khu gò thành tham quan tự do bên ngoài.",
        "ticket_vi": "Vào tự do (khuyến khích công đức tuỳ tâm).",
        "duration_vi": "Khoảng 45 phút - 1 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu, ngày trời quang để ngắm cảnh sông Protva từ gò thành.",
        "tips_vi": "Trang phục kín đáo khi vào nhà thờ. Từ Moskva thuận tiện nhất là đi ô tô/xe buýt; có thể kết hợp tham quan các điền trang và di tích lịch sử vùng Naro-Fominsk - Mozhaysk.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(55.344131, 36.188321, "Собор Рождества Христова", "Nativity of Christ Cathedral",
                       "Верея", "Vereya"),
    "official_site": None,
    "sources": [
        {"title": "Соборы.ру — Верея, Собор Рождества Христова", "url": "https://sobory.ru/article/?object=01124"},
        {"title": "Wikipedia (RU) — Собор Рождества Христова (Верея)", "url": "https://ru.wikipedia.org/wiki/Собор_Рождества_Христова_(Верея)"},
    ],
    "tags": ["church", "monument", "gorodok", "1812", "dorokhov", "vereya", "history", "day-trip", "moscow-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 12) PODMOKLOVO ROTUNDA CHURCH
PODMOKLOVO = {
    "id": f"{MO}-podmoklovo-rotunda-church",
    "slug": "podmoklovo-rotunda-church",
    "region": MO, "region_name_vi": MO_VI, "federal_district": MO_FED,
    "name_vi": "Nhà thờ tròn Sinh Nhật Đức Mẹ ở Podmoklovo (rotunda)",
    "name_ru": "Церковь Рождества Пресвятой Богородицы (Подмоклово)",
    "name_en": "Church of the Nativity of the Virgin (Podmoklovo)",
    "categories": ["church"],
    "coordinates": {"lat": 54.86698, "lon": 37.34676},
    "address_vi": "Làng Podmoklovo, huyện Serpukhov, Tỉnh Moskva; trên bờ cao sông Oka, cách Serpukhov khoảng 10 km về phía tây nam.",
    "rating": None,
    "presentation_short_vi": "Đây là một trong những công trình kiến trúc độc đáo nhất của nước Nga thời Pyotr Đại đế: một ngôi nhà thờ hình tròn (rotunda) xây năm 1714-1722, lấy cảm hứng từ kiến trúc Phục Hưng Ý, vành ngoài trang trí bằng những pho tượng thánh tông đồ bằng đá.",
    "presentation_long_vi": "Nằm trên bờ cao sông Oka ở làng Podmoklovo, cách Serpukhov chừng 10 km, ngôi nhà thờ Sinh Nhật Đức Mẹ là một hiện tượng hiếm có trong kiến trúc tôn giáo Nga. Được xây dựng trong các năm 1714-1722 theo ý tưởng của công tước Grigory Dolgorukov, công trình có hình khối là một khối tròn (rotunda) hai tầng ánh sáng, mái vòm cao và tháp đèn phía trên - một hình mẫu hoàn toàn khác lạ so với lối nhà thờ Nga truyền thống. Nguồn cảm hứng của nó được cho là đến từ kiến trúc Phục Hưng Ý, cụ thể là ngôi đền tròn Tempietto của Bramante ở Roma. Điều làm nên nét đặc sắc bậc nhất là vành hành lang cột bao quanh, bên trên đặt một dãy tượng các thánh tông đồ và nhà truyền giáo bằng đá - điều gần như không có ở bất kỳ nhà thờ Chính Thống giáo nào khác. Nằm giữa khung cảnh đồng quê yên ả bên sông Oka, ngôi nhà thờ trắng thanh thoát với những pho tượng lặng lẽ tạo nên một hình ảnh vừa cổ điển vừa nên thơ, thu hút giới yêu kiến trúc và nhiếp ảnh. Đây là điểm đến thú vị để bổ sung cho hành trình khám phá vùng Serpukhov phía nam Moskva.",
    "highlights_vi": [
        "Nhà thờ hình tròn (rotunda) độc đáo thời Pyotr Đại đế, xây 1714-1722, lấy cảm hứng từ Phục Hưng Ý.",
        "Vành cột bao quanh với dãy tượng các thánh tông đồ bằng đá - nét hiếm gặp ở nhà thờ Chính Thống giáo.",
        "Vị trí nên thơ trên bờ cao sông Oka, được giới yêu kiến trúc và nhiếp ảnh ưa thích.",
    ],
    "practical": {
        "hours_vi": "Nhà thờ đang hoạt động, mở cửa theo giờ lễ; khuôn viên có thể tham quan bên ngoài.",
        "ticket_vi": "Vào tự do (khuyến khích công đức tuỳ tâm).",
        "duration_vi": "Khoảng 30-45 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu, ngày trời quang để chiêm ngưỡng các pho tượng và cảnh sông Oka.",
        "tips_vi": "Trang phục kín đáo khi vào nhà thờ. Đường vào làng nhỏ, tự lái sẽ thuận tiện; dễ kết hợp với Serpukhov (Tu viện Vysotsky, Vladychny) trong cùng ngày.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(54.86698, 37.34676, "Церковь Рождества Пресвятой Богородицы",
                       "Church of the Nativity of the Virgin", "Подмоклово", "Podmoklovo",
                       org_url="https://yandex.com/maps/org/tserkov_rozhdestva_presvyatoy_bogoroditsy_v_podmoklovo/1370945739/"),
    "official_site": None,
    "sources": [
        {"title": "Соборы.ру — Церковь Рождества Богородицы в Подмоклово", "url": "https://sobory.ru/article/?object=01602"},
        {"title": "Wikipedia (RU) — Церковь Рождества Богородицы (Подмоклово)", "url": "https://ru.wikipedia.org/wiki/Церковь_Рождества_Богородицы_(Подмоклово)"},
    ],
    "tags": ["church", "rotunda", "baroque", "architecture", "podmoklovo", "serpukhov", "oka", "day-trip", "moscow-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 13) NEVSKY PYATACHOK MEMORIAL (KIROVSK, LO)
NEVSKY = {
    "id": f"{LO}-nevsky-pyatachok-memorial",
    "slug": "nevsky-pyatachok-memorial",
    "region": LO, "region_name_vi": LO_VI, "federal_district": LO_FED,
    "name_vi": "Đài tưởng niệm «Nevsky Pyatachok» (Bãi đất Neva)",
    "name_ru": "Мемориал «Невский пятачок»",
    "name_en": "Nevsky Pyatachok Memorial",
    "categories": ["monument"],
    "coordinates": {"lat": 59.841954, "lon": 30.956176},
    "address_vi": "Bờ đông (tả ngạn) sông Neva, rìa nam thành phố Kirovsk, huyện Kirovsky, Tỉnh Leningrad; cách Sankt-Peterburg khoảng 45 km về phía đông nam.",
    "rating": None,
    "presentation_short_vi": "«Nevsky Pyatachok» là tên gọi bãi đất đầu cầu nhỏ bé bên bờ đông sông Neva, nơi Hồng quân cố thủ trong những trận đánh khốc liệt bậc nhất của cuộc phong toả Leningrad. Trung tâm đài tưởng niệm là tượng đài «Tảng đá Biên cương» (Rubezhny Kamen) dựng năm 1972.",
    "presentation_long_vi": "Trên dải đất hẹp bên tả ngạn sông Neva, ở rìa nam thành phố Kirovsk, «Nevsky Pyatachok» ghi dấu một trong những trang bi tráng nhất của Chiến tranh Vệ quốc vĩ đại. Từ tháng 9 năm 1941, Hồng quân đổ bộ và giữ được một bàn đạp nhỏ - chỉ rộng chừng vài km2, nên được gọi là 'bãi đất' (pyatachok, nghĩa đen là 'đồng xu') - với hy vọng từ đây phá vây, nối lại liên lạc với Leningrad đang bị phong toả. Suốt nhiều tháng ròng, binh sĩ Xô Viết bám trụ dưới mưa bom bão đạn trong điều kiện vô cùng khắc nghiệt; tổn thất tại đây được xem là cực kỳ nặng nề, khiến địa danh này trở thành biểu tượng của lòng quả cảm và sự hy sinh. Quần thể tưởng niệm dần hình thành từ năm 1952 với cột tháp cao, về sau bổ sung xe tăng T-34, pháo và đặc biệt là tượng đài «Tảng đá Biên cương» (Rubezhny Kamen) khánh thành ngày 12 tháng 9 năm 1972 - khối gang và đá hoa cương lồng vào nhau, khắc hình người lính và những vần thơ của Robert Rozhdestvensky. Là một mắt xích của 'Vành đai Vinh quang Xanh' bảo vệ Leningrad, nơi đây nay là không gian tưởng niệm trang nghiêm, nhắc nhớ cái giá của hoà bình. Du khách đến đây trong tâm thế tưởng niệm, có thể kết hợp thăm bảo tàng - khu bảo tồn 'Chọc thủng vòng vây Leningrad' gần đó.",
    "highlights_vi": [
        "Bãi đất đầu cầu bên bờ đông sông Neva - một trong những chiến địa khốc liệt nhất thời phong toả Leningrad.",
        "Tượng đài «Tảng đá Biên cương» (Rubezhny Kamen, 1972) khắc thơ Robert Rozhdestvensky.",
        "Một mắt xích của 'Vành đai Vinh quang Xanh'; có xe tăng T-34 và cột tháp tưởng niệm.",
    ],
    "practical": {
        "hours_vi": "Khu tưởng niệm ngoài trời, tham quan tự do quanh năm.",
        "ticket_vi": "Miễn phí.",
        "duration_vi": "Khoảng 30-45 phút.",
        "best_time_vi": "Cuối xuân đến đầu thu; các ngày lễ tưởng niệm (9/5, các mốc phá vây) rất trang trọng.",
        "tips_vi": "Đến đây với thái độ tưởng niệm trang nghiêm. Thuận tiện đi ô tô từ Sankt-Peterburg theo hướng Kirovsk; có thể kết hợp bảo tàng - khu bảo tồn 'Proryv' (Chọc thủng vòng vây Leningrad).",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(59.841954, 30.956176, "Мемориал «Невский пятачок»", "Nevsky Pyatachok Memorial",
                       "Кировск", "Kirovsk"),
    "official_site": None,
    "sources": [
        {"title": "Wikipedia (RU) — Невский пятачок", "url": "https://ru.wikipedia.org/wiki/Невский_пятачок"},
        {"title": "Artefact (ar.culture.ru) — Невский пятачок", "url": "https://ar.culture.ru/ru/subject/nevskiy-pyatachok"},
    ],
    "tags": ["monument", "memorial", "wwii", "leningrad-blockade", "kirovsk", "neva", "leningrad-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}

# ============================================================ 14) ANTONIYEVO-DYMSKY MONASTERY (TIKHVIN, LO)
DYMSKY = {
    "id": f"{LO}-antonievo-dymsky-monastery",
    "slug": "antonievo-dymsky-monastery",
    "region": LO, "region_name_vi": LO_VI, "federal_district": LO_FED,
    "name_vi": "Tu viện Antoniyevo-Dymsky (gần Tikhvin)",
    "name_ru": "Антониево-Дымский монастырь",
    "name_en": "Anthony-Dymsky Monastery",
    "categories": ["church"],
    "coordinates": {"lat": 59.57228, "lon": 33.675936},
    "address_vi": "Làng Bronevik, bên hồ Dymskoye, huyện Boksitogorsk, Tỉnh Leningrad; cách thành phố Tikhvin khoảng 15-17 km về phía đông nam.",
    "rating": None,
    "presentation_short_vi": "Tu viện Antoniyevo-Dymsky bên hồ Dymskoye được xem là một trong những tu viện lâu đời nhất miền tây bắc nước Nga, gắn với Thánh Antoniy Dymsky ở thế kỷ 13. Người hành hương có truyền thống dầm mình dưới hồ, nơi có cây thánh giá đánh dấu chỗ vị thánh từng cầu nguyện.",
    "presentation_long_vi": "Nằm bên hồ Dymskoye tĩnh lặng, cách Tikhvin chừng 15-17 km về phía đông nam, Tu viện Antoniyevo-Dymsky được coi là một trong những tu viện cổ xưa nhất của vùng tây bắc nước Nga. Theo truyền thống, tu viện gắn với Thánh Antoniy Dymsky, người đã tới ẩn tu bên hồ vào thế kỷ 13 và được tôn kính là vị sáng lập; thánh tích của ngài được lưu giữ tại đây. Một nét độc đáo của nơi này là tục hành hương ra hồ Dymskoye: giữa hồ có một tảng đá và cây thánh giá đánh dấu chỗ tương truyền Thánh Antoniy từng đứng cầu nguyện, và khách mộ đạo có lệ dầm mình xuống làn nước được xem là thiêng. Quần thể tu viện với nhà thờ chính thờ Icon Đức Mẹ Kazan cùng các nhà nguyện đã trải qua nhiều lần hưng phế - bị tàn phá, đóng cửa rồi hồi sinh - và nay là một nam tu viện đang hoạt động, thu hút khách hành hương và những ai muốn tìm chốn tĩnh lặng giữa thiên nhiên. Với bề dày lịch sử và khung cảnh hồ nước thanh bình, Antoniyevo-Dymsky là điểm đến ý nghĩa để kết hợp cùng Tu viện Đức Mẹ Lên Trời Tikhvin nổi tiếng trong cùng hành trình.",
    "highlights_vi": [
        "Một trong những tu viện cổ nhất tây bắc nước Nga, gắn với Thánh Antoniy Dymsky thế kỷ 13.",
        "Tục hành hương dầm mình dưới hồ Dymskoye, nơi có thánh giá đánh dấu chỗ vị thánh cầu nguyện.",
        "Nhà thờ thờ Icon Đức Mẹ Kazan và thánh tích Thánh Antoniy; nay là nam tu viện đang hoạt động.",
    ],
    "practical": {
        "hours_vi": "Tu viện đang hoạt động, mở cửa hằng ngày theo giờ lễ.",
        "ticket_vi": "Vào tự do (khuyến khích công đức tuỳ tâm).",
        "duration_vi": "Khoảng 45 phút - 1 giờ.",
        "best_time_vi": "Cuối xuân đến đầu thu; mùa hè thuận tiện cho tục dầm mình dưới hồ.",
        "tips_vi": "Trang phục kín đáo. Đường tới tu viện khá xa, tự lái hoặc theo tour hành hương từ Tikhvin sẽ thuận tiện; dễ kết hợp với Tu viện Đức Mẹ Lên Trời Tikhvin.",
    },
    "photo": None, "photo_credit": None,
    "maps": build_maps(59.57228, 33.675936, "Антониево-Дымский монастырь", "Anthony-Dymsky Monastery",
                       "Тихвин", "Tikhvin"),
    "official_site": None,
    "sources": [
        {"title": "Соборы.ру — Броневик, Антониево-Дымский Троицкий мужской монастырь", "url": "https://sobory.ru/article/?object=06588"},
        {"title": "Глобус Санкт-Петербургской митрополии — Антониево-Дымский мужской монастырь", "url": "https://globus.aquaviva.ru/antonievo-dymskiy-muzhskoy-monastyr"},
    ],
    "tags": ["church", "monastery", "orthodox", "pilgrimage", "tikhvin", "lake", "leningrad-oblast"],
    "status": "enriched", "last_updated": TODAY, "country": "russia",
}


PLAN = {
    "moscow-oblast.json": [ZHOSTOVO, FEDOSKINO, GZHEL, PLATOK, BOGORODSKOYE, GOLUTVIN,
                            BOBRENEV, VLADYCHNY, BORISOGLEBSKY, VOLOKOLAMSK, VEREYA, PODMOKLOVO],
    "leningrad-oblast.json": [NEVSKY, DYMSKY],
}


def main():
    total_added = 0
    for fname, recs in PLAN.items():
        path = os.path.join(REGIONS, fname)
        arr = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
        if not isinstance(arr, list):
            print(f"  ! {fname}: noi dung khong phai mang — bo qua.")
            continue
        existing_slugs = {p.get("slug") for p in arr}
        existing_ids = {p.get("id") for p in arr}
        to_add = []
        for r in recs:
            if r["slug"] in existing_slugs or r["id"] in existing_ids:
                print(f"  = BO QUA (da co): {fname} :: {r['slug']}")
                continue
            to_add.append(r)
        if not to_add:
            continue
        if os.path.exists(path):
            bak = path + f".bak_add_{TS}"
            with open(bak, "w", encoding="utf-8") as f:
                json.dump(arr, f, ensure_ascii=False, indent=2)
            print(f"  ~ backup: {os.path.basename(bak)}")
        arr.extend(to_add)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(arr, f, ensure_ascii=False, indent=2)
        total_added += len(to_add)
        print(f"  + {fname}: them {len(to_add)} dia diem -> tong {len(arr)}")
        for r in to_add:
            print(f"        - {r['name_vi']}  [{','.join(r['categories'])}]  ({r['coordinates']['lat']},{r['coordinates']['lon']})")

    print(f"\nTong da them lan nay: {total_added} dia diem.")


if __name__ == "__main__":
    main()
