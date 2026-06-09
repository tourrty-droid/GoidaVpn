import os
import random
import requests
from datetime import datetime

# НАСТРОЙКИ
VLESS_URLS = [
    "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/new/all_new.txt",
    "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/new/by_protocol/vless/vless_001.txt",
    "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/clean/vless.txt",
    "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/clean/hysteria2.txt"
]

OUTPUT_FILE = "data/GoiVpnAUTO"
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

HEADER = "# profile-title: GoidaVpn\n# profile-update-interval: 1\n# announce: 🟢 GoidaVpn Status: Fine\n\n"

def send_tg(text):
    if TOKEN and CHAT_ID:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"})

def main():
    # 1. Скачивание
    all_configs = []
    for url in VLESS_URLS:
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                all_configs.extend([l.strip() for l in r.text.splitlines() if l.strip() and '#' in l])
        except: continue

    # 2. Фильтрация
    youtube_configs = [c for c in all_configs if 'youtube' in c.lower() or 'yt' in c.lower()]
    target = youtube_configs if youtube_configs else all_configs
    
    if not target:
        send_tg("❌ Ошибка: Конфиги не найдены.")
        return

    # 3. Выборка
    random.shuffle(target)
    final_configs = target[:7]
    
    # Добавляем нумерацию
    result = [f"{c.rsplit('#', 1)[0]}#{c.rsplit('#', 1)[1]} | Server #{i+1}" for i, c in enumerate(final_configs)]
    
    # 4. Запись
    os.makedirs("data", exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(HEADER + "\n".join(result))
    
    # 5. Отчет
    now = datetime.now()
    report = f"✅ <b>GoidaVpn обновлен!</b>\n🕒 {now.strftime('%H:%M:%S')}\n⏱ Задержка: {now.minute * 60 + now.second} сек.\n\n"
    report += "\n".join([f"{i+1}. {c.split('#')[-1]}" for i, c in enumerate(final_configs)])
    send_tg(report)
    print("Успешно обновлено.")

if __name__ == "__main__":
    main()
    
