import os
import random
import re
import requests

# Ссылки на донорские репозитории
VLESS_URL = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/clean/vless.txt"
HYSTERIA_URL = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/ru-sni/hysteria2.txt"

OUTPUT_FILE = "AutoConfigs.txt"

# Ваша кастомная шапка подписок
HEADER_TEXT = """# profile-title: GoidaVpn
# profile-update-interval: 1
#support-url: https://github.com/tourrty-droid/GoidaVpn
#announce: 🟢 GoidaVpn Status: Fine 🟢 После 8:00 РКН блокируют некоторые сервера
# мяу
# гав\n\n"""

# Словарь для перевода кодов и флагов стран на русский язык
COUNTRY_MAP = {
    'NL': ('🇳🇱', 'Нидерланды'),
    'US': ('🇺🇸', 'США'),
    'DE': ('🇩🇪', 'Германия'),
    'GB': ('🇬🇧', 'Великобритания'),
    'UK': ('🇬🇧', 'Великобритания'),
    'FR': ('🇫🇷', 'Франция'),
    'FI': ('🇫🇮', 'Финляндия'),
    'RU': ('🇷🇺', 'Россия'),
    'SG': ('🇸🇬', 'Сингапур'),
    'JP': ('🇯🇵', 'Япония'),
    'HK': ('🇭🇰', 'Гонконг'),
    'TR': ('🇹🇷', 'Турция'),
    'PL': ('🇵🇱', 'Польша'),
    'SE': ('🇸🇪', 'Швеция'),
    'CH': ('🇨🇭', 'Швейцария'),
    'KZ': ('🇰🇿', 'Казахстан'),
    'UA': ('🇺🇦', 'Украина'),
    'BY': ('🇧🇾', 'Беларусь'),
}

def clean_and_rename_config(line, index):
    """
    Анализирует хвост конфига после #, определяет страну
    и возвращает строку с красивым русским названием.
    """
    if '#' not in line:
        return line
        
    base_part, config_name = line.rsplit('#', 1)
    config_name_upper = config_name.upper()
    
    # Значения по умолчанию (если страну не определили)
    flag = "🌐"
    country_name = "Неизвестно"
    
    # Ищем код страны в названии конфига
    for code, (f, name) in COUNTRY_MAP.items():
        # Проверяем наличие буквенного кода страны (например, "NL" или "NL_") 
        # или прямое присутствие эмодзи-флага в строке
        if code in config_name_upper or f in config_name:
            flag = f
            country_name = name
            break
            
    # Собираем красивое и лаконичное имя: "Флаг Страна | Сервер №"
    new_name = f"{flag} {country_name} | Server #{index}"
    return f"{base_part}#{new_name}"

def download_data(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"⚠️ Ошибка при скачивании {url}: {e}")
        return ""

def fetch_and_merge():
    print("Запуск парсинга баз данных...")
    
    vless_data = download_data(VLESS_URL)
    hysteria_data = download_data(HYSTERIA_URL)
    
    combined_raw_lines = vless_data.splitlines() + hysteria_data.splitlines()
    
    matched_lines = []
    all_lines = []
    
    print("Фильтрация строк по тегам YouTube/YT...")
    for line in combined_raw_lines:
        line = line.strip()
        if not line:
            continue
            
        all_lines.append(line)
        
        if '#' in line:
            config_name = line.split('#')[-1].lower()
            if 'youtube' in config_name or 'yt' in config_name:
                matched_lines.append(line)

    print(f"Найдено строго по фильтру YouTube: {len(matched_lines)}")
    
    if not matched_lines:
        print("Строк с тегом YouTube не найдено. Смешиваем общую базу.")
        matched_lines = all_lines

    if not matched_lines:
        print("Оба источника пусты. Прерывание.")
        return False

    # Перемешиваем конфиги
    random.shuffle(matched_lines)
    
    # Отбираем ровно ТОП-7 штук
    top_7_configs = matched_lines[:7]
    print(f"Успешно сформировано конфигураций для записи: {len(top_7_configs)}")
    
    # Переименовываем отобранные конфиги, чтобы они выглядели красиво
    beautiful_configs = []
    for i, config in enumerate(top_7_configs, 1):
        beautiful_config = clean_and_rename_config(config, i)
        beautiful_configs.append(beautiful_config)
    
    print(f"Запись очищенных данных в {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(HEADER_TEXT)
        for config in beautiful_configs:
            f.write(config + "\n")
            
    print(f"Файл {OUTPUT_FILE} успешно обновлен!")
    return True

if __name__ == "__main__":
    fetch_and_merge()
