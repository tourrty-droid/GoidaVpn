import os
import random
import requests

# Ссылки на донорские репозитории
VLESS_URL = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/clean/vless.txt"
HYSTERIA_URL = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/new/by_protocol/hysteria2/hysteria2_001.txt"

OUTPUT_FILE = "AutoConfigs.txt"

# Ваша кастомная шапка подписок
HEADER_TEXT = """# profile-title: GoidaVpn
# profile-update-interval: 1
#support-url: https://github.com/tourrty-droid/GoidaVpn
#announce: 🟢 GoidaVpn Status: Fine 🟢 После 8:00 РКН блокируют некоторые сервера
# мяу
# гав\n\n"""

def download_data(url):
    """Скачивает текст по ссылке с таймаутом"""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"⚠️ Ошибка при скачивании {url}: {e}")
        return ""

def fetch_and_merge():
    print("Запуск парсинга баз данных...")
    
    # Скачиваем оба файла
    vless_data = download_data(VLESS_URL)
    hysteria_data = download_data(HYSTERIA_URL)
    
    # Объединяем все строки в один массив
    combined_raw_lines = vless_data.splitlines() + hysteria_data.splitlines()
    
    matched_lines = []
    all_lines = []
    
    print("Фильтрация строк по тегам YouTube/YT...")
    for line in combined_raw_lines:
        line = line.strip()
        if not line:
            continue
            
        # Сохраняем вообще каждую рабочую ссылку для подстраховки
        all_lines.append(line)
        
        if '#' in line:
            config_parts = line.split('#')
            config_name = config_parts[-1].lower()
            
            # Наш фильтр по тегам YouTube
            if 'youtube' in config_name or 'yt' in config_name:
                matched_lines.append(line)

    print(f"Найдено строго по фильтру YouTube: {len(matched_lines)}")
    
    # ЗАЩИТА: Если по фильтру ничего нет, берем общую базу из VLESS + Hysteria2
    if not matched_lines:
        print("Строк с тегом YouTube не найдено. Смешиваем общую базу.")
        matched_lines = all_lines

    if not matched_lines:
        print("Оба источника пусты. Прерывание операции.")
        return False

    # Перемешиваем общий список (теперь там лежат и VLESS, и Hysteria2)
    random.shuffle(matched_lines)
    
    # Срезаем ТОП-7 лучших
    top_7_configs = matched_lines[:7]
    print(f"Успешно сформировано конфигураций для записи: {len(top_7_configs)}")
    
    print(f"Запись объединенных данных в {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(HEADER_TEXT)
        for config in top_7_configs:
            f.write(config + "\n")
            
    print(f"Файл {OUTPUT_FILE} успешно обновлен!")
    return True

if __name__ == "__main__":
    fetch_and_merge()
