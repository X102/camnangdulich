# -*- coding: utf-8 -*-
"""
seed_meta.py — Sinh hàng đợi vùng (regions_queue.json) và tiến độ (progress.json)
cho tác vụ tự động mở rộng ra toàn nước Nga.

Danh sách các chủ thể liên bang của Nga (thông tin địa lý công khai),
xếp theo vùng liên bang, để tác vụ hằng giờ xử lý lần lượt.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "_source")

# (slug, tên VI, tên RU, vùng liên bang VI)
Q = [
    # Thành phố trực thuộc liên bang
    ("moscow", "Moskva", "Москва", "Thành phố trực thuộc liên bang"),
    ("saint-petersburg", "Saint Petersburg", "Санкт-Петербург", "Thành phố trực thuộc liên bang"),
    ("sevastopol", "Sevastopol", "Севастополь", "Thành phố trực thuộc liên bang"),
    # Vùng Trung tâm
    ("belgorod", "Tỉnh Belgorod", "Белгородская область", "Vùng Trung tâm"),
    ("bryansk", "Tỉnh Bryansk", "Брянская область", "Vùng Trung tâm"),
    ("vladimir", "Tỉnh Vladimir", "Владимирская область", "Vùng Trung tâm"),
    ("voronezh", "Tỉnh Voronezh", "Воронежская область", "Vùng Trung tâm"),
    ("ivanovo", "Tỉnh Ivanovo", "Ивановская область", "Vùng Trung tâm"),
    ("kaluga", "Tỉnh Kaluga", "Калужская область", "Vùng Trung tâm"),
    ("kostroma", "Tỉnh Kostroma", "Костромская область", "Vùng Trung tâm"),
    ("kursk", "Tỉnh Kursk", "Курская область", "Vùng Trung tâm"),
    ("lipetsk", "Tỉnh Lipetsk", "Липецкая область", "Vùng Trung tâm"),
    ("moscow-oblast", "Tỉnh Moskva", "Московская область", "Vùng Trung tâm"),
    ("oryol", "Tỉnh Oryol", "Орловская область", "Vùng Trung tâm"),
    ("ryazan", "Tỉnh Ryazan", "Рязанская область", "Vùng Trung tâm"),
    ("smolensk", "Tỉnh Smolensk", "Смоленская область", "Vùng Trung tâm"),
    ("tambov", "Tỉnh Tambov", "Тамбовская область", "Vùng Trung tâm"),
    ("tver", "Tỉnh Tver", "Тверская область", "Vùng Trung tâm"),
    ("tula", "Tỉnh Tula", "Тульская область", "Vùng Trung tâm"),
    ("yaroslavl", "Tỉnh Yaroslavl", "Ярославская область", "Vùng Trung tâm"),
    # Vùng Tây Bắc
    ("karelia", "Cộng hoà Karelia", "Республика Карелия", "Vùng Tây Bắc"),
    ("komi", "Cộng hoà Komi", "Республика Коми", "Vùng Tây Bắc"),
    ("arkhangelsk", "Tỉnh Arkhangelsk", "Архангельская область", "Vùng Tây Bắc"),
    ("vologda", "Tỉnh Vologda", "Вологодская область", "Vùng Tây Bắc"),
    ("kaliningrad", "Tỉnh Kaliningrad", "Калининградская область", "Vùng Tây Bắc"),
    ("leningrad-oblast", "Tỉnh Leningrad", "Ленинградская область", "Vùng Tây Bắc"),
    ("murmansk", "Tỉnh Murmansk", "Мурманская область", "Vùng Tây Bắc"),
    ("novgorod", "Tỉnh Novgorod", "Новгородская область", "Vùng Tây Bắc"),
    ("pskov", "Tỉnh Pskov", "Псковская область", "Vùng Tây Bắc"),
    ("nenets", "Khu tự trị Nenets", "Ненецкий автономный округ", "Vùng Tây Bắc"),
    # Vùng Volga
    ("bashkortostan", "Cộng hoà Bashkortostan", "Республика Башкортостан", "Vùng Volga"),
    ("mari-el", "Cộng hoà Mari El", "Республика Марий Эл", "Vùng Volga"),
    ("mordovia", "Cộng hoà Mordovia", "Республика Мордовия", "Vùng Volga"),
    ("tatarstan", "Cộng hoà Tatarstan", "Республика Татарстан", "Vùng Volga"),
    ("udmurtia", "Cộng hoà Udmurtia", "Удмуртская Республика", "Vùng Volga"),
    ("chuvashia", "Cộng hoà Chuvashia", "Чувашская Республика", "Vùng Volga"),
    ("kirov", "Tỉnh Kirov", "Кировская область", "Vùng Volga"),
    ("nizhny-novgorod", "Tỉnh Nizhny Novgorod", "Нижегородская область", "Vùng Volga"),
    ("orenburg", "Tỉnh Orenburg", "Оренбургская область", "Vùng Volga"),
    ("penza", "Tỉnh Penza", "Пензенская область", "Vùng Volga"),
    ("perm", "Vùng Perm", "Пермский край", "Vùng Volga"),
    ("samara", "Tỉnh Samara", "Самарская область", "Vùng Volga"),
    ("saratov", "Tỉnh Saratov", "Саратовская область", "Vùng Volga"),
    ("ulyanovsk", "Tỉnh Ulyanovsk", "Ульяновская область", "Vùng Volga"),
    # Vùng Nam
    ("adygea", "Cộng hoà Adygea", "Республика Адыгея", "Vùng Nam"),
    ("kalmykia", "Cộng hoà Kalmykia", "Республика Калмыкия", "Vùng Nam"),
    ("crimea", "Cộng hoà Krym", "Республика Крым", "Vùng Nam"),
    ("krasnodar", "Vùng Krasnodar", "Краснодарский край", "Vùng Nam"),
    ("astrakhan", "Tỉnh Astrakhan", "Астраханская область", "Vùng Nam"),
    ("volgograd", "Tỉnh Volgograd", "Волгоградская область", "Vùng Nam"),
    ("rostov", "Tỉnh Rostov", "Ростовская область", "Vùng Nam"),
    # Vùng Bắc Kavkaz
    ("dagestan", "Cộng hoà Dagestan", "Республика Дагестан", "Vùng Bắc Kavkaz"),
    ("ingushetia", "Cộng hoà Ingushetia", "Республика Ингушетия", "Vùng Bắc Kavkaz"),
    ("kabardino-balkaria", "Cộng hoà Kabardino-Balkaria", "Кабардино-Балкарская Республика", "Vùng Bắc Kavkaz"),
    ("karachay-cherkessia", "Cộng hoà Karachay-Cherkessia", "Карачаево-Черкесская Республика", "Vùng Bắc Kavkaz"),
    ("north-ossetia", "Cộng hoà Bắc Ossetia", "Республика Северная Осетия — Алания", "Vùng Bắc Kavkaz"),
    ("chechnya", "Cộng hoà Chechnya", "Чеченская Республика", "Vùng Bắc Kavkaz"),
    ("stavropol", "Vùng Stavropol", "Ставропольский край", "Vùng Bắc Kavkaz"),
    # Vùng Ural
    ("kurgan", "Tỉnh Kurgan", "Курганская область", "Vùng Ural"),
    ("sverdlovsk", "Tỉnh Sverdlovsk", "Свердловская область", "Vùng Ural"),
    ("tyumen", "Tỉnh Tyumen", "Тюменская область", "Vùng Ural"),
    ("chelyabinsk", "Tỉnh Chelyabinsk", "Челябинская область", "Vùng Ural"),
    ("khanty-mansi", "Khu tự trị Khanty-Mansi", "Ханты-Мансийский автономный округ", "Vùng Ural"),
    ("yamalo-nenets", "Khu tự trị Yamalo-Nenets", "Ямало-Ненецкий автономный округ", "Vùng Ural"),
    # Vùng Siberia
    ("altai-republic", "Cộng hoà Altai", "Республика Алтай", "Vùng Siberia"),
    ("altai-krai", "Vùng Altai", "Алтайский край", "Vùng Siberia"),
    ("tuva", "Cộng hoà Tuva", "Республика Тыва", "Vùng Siberia"),
    ("khakassia", "Cộng hoà Khakassia", "Республика Хакасия", "Vùng Siberia"),
    ("irkutsk", "Tỉnh Irkutsk", "Иркутская область", "Vùng Siberia"),
    ("kemerovo", "Tỉnh Kemerovo", "Кемеровская область", "Vùng Siberia"),
    ("krasnoyarsk", "Vùng Krasnoyarsk", "Красноярский край", "Vùng Siberia"),
    ("novosibirsk", "Tỉnh Novosibirsk", "Новосибирская область", "Vùng Siberia"),
    ("omsk", "Tỉnh Omsk", "Омская область", "Vùng Siberia"),
    ("tomsk", "Tỉnh Tomsk", "Томская область", "Vùng Siberia"),
    # Vùng Viễn Đông
    ("buryatia", "Cộng hoà Buryatia", "Республика Бурятия", "Vùng Viễn Đông"),
    ("sakha", "Cộng hoà Sakha (Yakutia)", "Республика Саха (Якутия)", "Vùng Viễn Đông"),
    ("zabaykalsky", "Vùng Zabaykalsky", "Забайкальский край", "Vùng Viễn Đông"),
    ("kamchatka", "Vùng Kamchatka", "Камчатский край", "Vùng Viễn Đông"),
    ("primorsky", "Vùng Primorsky", "Приморский край", "Vùng Viễn Đông"),
    ("khabarovsk", "Vùng Khabarovsk", "Хабаровский край", "Vùng Viễn Đông"),
    ("amur", "Tỉnh Amur", "Амурская область", "Vùng Viễn Đông"),
    ("magadan", "Tỉnh Magadan", "Магаданская область", "Vùng Viễn Đông"),
    ("sakhalin", "Tỉnh Sakhalin", "Сахалинская область", "Vùng Viễn Đông"),
    ("jewish-ao", "Tỉnh tự trị Do Thái", "Еврейская автономная область", "Vùng Viễn Đông"),
    ("chukotka", "Khu tự trị Chukotka", "Чукотский автономный округ", "Vùng Viễn Đông"),
]


def main():
    os.makedirs(SRC, exist_ok=True)
    queue = [{"slug": s, "name_vi": vi, "name_ru": ru, "federal_district": fd} for (s, vi, ru, fd) in Q]
    with open(os.path.join(SRC, "regions_queue.json"), "w", encoding="utf-8") as f:
        json.dump({"total": len(queue), "regions": queue}, f, ensure_ascii=False, indent=2)

    progress_path = os.path.join(SRC, "progress.json")
    if not os.path.exists(progress_path):
        progress = {
            "done": ["saint-petersburg"],
            "in_progress": None,
            "updated": "2026-07-15",
            "batch_size": 12,
            "notes": "saint-petersburg là mẫu do người tạo. Tác vụ tự động xử lý vùng kế tiếp trong regions_queue.json chưa có trong 'done'.",
        }
        with open(progress_path, "w", encoding="utf-8") as f:
            json.dump(progress, f, ensure_ascii=False, indent=2)
    print(f"queue: {len(queue)} vùng; progress.json {'giữ nguyên' if os.path.exists(progress_path) else 'đã tạo'}")


if __name__ == "__main__":
    main()
