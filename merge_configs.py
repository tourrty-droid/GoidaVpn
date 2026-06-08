import os
import random
from datetime import datetime, timedelta
import requests

# =====================================================================
# ИСТОЧНИКИ КОНФИГУРАЦИЙ
# =====================================================================
VLESS_URL_1 = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/new/all_new.txt"
VLESS_URL_2 = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/new/by_protocol/vless/vless_001.txt"
VLESS_URL_3 = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/clean/vless.txt"

HYSTERIA_URL = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/clean/hysteria2.txt"
# =====================================================================

# НАСТРОЙКА ПУТЕЙ
OUTPUT_DIR = "data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "GoiVpnAUTO")
LOGS_DIR = "logs"

HEADER_TEXT = """# profile-title: GoidaVpn
# profile-update-interval: 1
#support-url: https://github.com/tourrty-droid/GoidaVpn
#announce: 🟢 GoidaVpn Status: Fine 🟢 После 8:00 РКН блокируют некоторые сервера
# мяу
# гав\n\n"""

COUNTRY_MAP = {
    'NL': ('🇳🇱', 'Нидерланды'), 'US': ('🇺🇸', 'США'), 'DE': ('🇩🇪', 'Германия'),
    'GB': ('🇬🇧', 'Великобритания'), 'UK': ('🇬🇧', 'Великобритания'), 'FR': ('🇫🇷', 'Франция'),
    'FI': ('🇫🇮', 'Финляндия'), 'RU': ('🇷🇺', 'Россия'), 'SG': ('🇸🇬', 'Сингапур'),
    'JP': ('🇯🇵', 'Япония'), 'HK': ('🇭🇰', 'Гонконг'), 'TR': ('🇹🇷', 'Турция'),
    'PL': ('🇵🇱', 'Польша'), 'SE': ('🇸🇪', 'Швеция'), 'CH': ('🇨🇭', 'Швейцария'),
    'KZ': ('🇰🇿', 'Казахстан'), 'UA': ('🇺🇦', 'Украина'), 'BY': ('🇧🇾', 'Беларусь'),
}

def clean_and_rename_config(line, index):
    if '#' not in line:
        return line
    base_part, config_name = line.rsplit('#', 1)
    config_name_upper = config_name.upper()
    flag, country_name = "🌐", "Неизвестно"
    for code, (f, name) in COUNTRY_MAP.items():
        if code in config_name_upper or f in config_name:
            flag, country_name = f, name
            break
    return f"{base_part}#{flag} {country_name} | Server #{index}"

def download_data(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"⚠️ Ошибка при скачивании {url}: {e}")
        return ""

def manage_logs_and_backup():
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)

    # 1. Создаем бэкап с фиксацией точного времени (Часы-Минуты-Секунды)
    if os.path.exists(OUTPUT_FILE) and os.path.getsize(OUTPUT_FILE) > 0:
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_name = os.path.join(LOGS_DIR, f"backup_{current_time}.txt")
        try:
            with open(OUTPUT_FILE, "r", encoding="utf-8") as src, open(backup_name, "w", encoding="utf-8") as dst:
                dst.write(src.read())
            print(f"Резервная копия сохранена с точным временем: {backup_name}")
        except Exception as e:
            print(f"⚠️ Не удалось создать бекап: {e}")

    # 2. ОЧИСТКА КАЖДЫЙ ДЕНЬ: Удаляем любые бэкапы, которые старше 24 часов
    try:
        print("Проверка папки логов на наличие файлов старше 24 часов...")
        now = datetime.now()
        one_day_ago = now - timedelta(days=1)
        
        for filename in os.listdir(LOGS_DIR):
            file_path = os.path.join(LOGS_DIR, filename)
            
            if os.path.isfile(file_path) and filename.startswith("backup_") and filename.endswith(".txt"):
                try:
                    # Извлекаем дату и время из имени файла (backup_YYYY-MM-DD_HH-MM-SS.txt)
                    date_str = filename.replace("backup_", "").replace(".txt", "")
                    file_date = datetime.strptime(date_str, "%Y-%m-%d_%H-%M-%S")
                    
                    # Если файл был создан больше суток назад — удаляем его
                    if file_date < one_day_ago:
                        os.remove(file_path)
                        print(f"🗑️ Срок хранения истек (24ч). Удален лог: {filename}")
                except ValueError:
                    # На случай сбоя формата имени проверяем реальное время изменения файла операционной системой
                    file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                    if file_mtime < one_day_ago:
                        os.remove(file_path)
                        print(f"🗑️ Удален старый файл по системному времени: {filename}")
                        
    except Exception as e:
        print(f"⚠️ Ошибка при очистке папки логов: {e}")

def fetch_and_merge():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Создана папка {OUTPUT_DIR}")

    manage_logs_and_backup()

    print("Запуск парсинга всех баз данных...")
    
    urls = [VLESS_URL_1, VLESS_URL_2, VLESS_URL_3, HYSTERIA_URL]
    combined_raw_lines = []
    
    for url in urls:
        data = download_data(url)
        if data:
            combined_raw_lines.extend(data.splitlines())
    
    matched_lines, all_lines = [], []
    
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

    if not matched_lines:
        print("Строк с тегом YouTube не найдено. Смешиваем общую базу.")
        matched_lines = all_lines

    if not matched_lines:
        print("Все источники пусты. Прерывание.")
        return False

    random.shuffle(matched_lines)
    top_7_configs = matched_lines[:7]
    
    beautiful_configs = [clean_and_rename_config(config, i) for i, config in enumerate(top_7_configs, 1)]
    
    print(f"Запись свежих объединенных данных в {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(HEADER_TEXT)
        for config in beautiful_configs:
            f.write(config + "\n")
            
    print(f"Файл {OUTPUT_FILE} успешно обновлен!")
    return True

if __name__ == "__main__":
    fetch_and_merge()
