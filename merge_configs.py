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

# НАСТРОЙКА ПУТЕЙ И TELEGRAM
OUTPUT_DIR = "data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "GoiVpnAUTO")
LOGS_DIR = "logs"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

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

def send_telegram_message(text):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"⚠️ Ошибка Telegram: {e}")

def clean_and_rename_config(line, index):
    if '#' not in line: return line
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
        print(f"⚠️ Ошибка скачивания {url}: {e}")
        return ""

def manage_logs_and_backup():
    if not os.path.exists(LOGS_DIR): os.makedirs(LOGS_DIR)
    if os.path.exists(OUTPUT_FILE) and os.path.getsize(OUTPUT_FILE) > 0:
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_name = os.path.join(LOGS_DIR, f"backup_{current_time}.txt")
        try:
            with open(OUTPUT_FILE, "r", encoding="utf-8") as src, open(backup_name, "w", encoding="utf-8") as dst:
                dst.write(src.read())
        except Exception as e:
            print(f"⚠️ Ошибка бэкапа: {e}")
    
    # Очистка логов старше 24ч
    try:
        now = datetime.now()
        one_day_ago = now - timedelta(days=1)
        for filename in os.listdir(LOGS_DIR):
            file_path = os.path.join(LOGS_DIR, filename)
            if os.path.isfile(file_path) and filename.startswith("backup_"):
                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_mtime < one_day_ago:
                    os.remove(file_path)
    except Exception as e:
        print(f"⚠️ Ошибка очистки логов: {e}")

def fetch_and_merge():
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)
    manage_logs_and_backup()
    
    urls = [VLESS_URL_1, VLESS_URL_2, VLESS_URL_3, HYSTERIA_URL]
    combined_raw_lines = []
    for url in urls:
        data = download_data(url)
        if data: combined_raw_lines.extend(data.splitlines())
    
    matched_lines = [line.strip() for line in combined_raw_lines if line.strip() and '#' in line and ('youtube' in line.split('#')[-1].lower() or 'yt' in line.split('#')[-1].lower())]
    
    if not matched_lines:
        matched_lines = [line.strip() for line in combined_raw_lines if line.strip()]

    if not matched_lines:
        send_telegram_message("❌ <b>GoidaVpn: Ошибка!</b>\nВсе источники пусты.")
        return False

    random.shuffle(matched_lines)
    top_7_configs = matched_lines[:7]
    beautiful_configs = [clean_and_rename_config(config, i) for i, config in enumerate(top_7_configs, 1)]
    
    # Расчет задержки и формирование отчета
    now = datetime.now()
    seconds_passed = now.minute * 60 + now.second
    report_lines = [
        f"✅ <b>GoidaVpn обновлен!</b>", 
        f"🕒 <b>Время запуска:</b> {now.strftime('%H:%M:%S')}",
        f"⏱ <b>Задержка:</b> {seconds_passed} сек.",
        ""
    ]
    for i, cfg in enumerate(beautiful_configs, 1):
        parts = cfg.split('#', 1)
        name = parts[1] if len(parts) > 1 else "Без названия"
        link = (parts[0][:35] + "...") if len(parts[0]) > 35 else parts[0]
        report_lines.append(f"{i}. <b>{name}</b>\n<code>{link}</code>")
    
    send_telegram_message("\n".join(report_lines))
    
    # ВОТ ЗДЕСЬ БЫЛА ОШИБКА ОТСТУПА, ТЕПЕРЬ ВСЁ ВЕРНО:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(HEADER_TEXT + "\n".join(beautiful_configs))
    return True
    
