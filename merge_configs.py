import os
import random
import requests

# Прямая ссылка (raw) на конфигурации, которую вы указали
RAW_CONFIG_URL = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/refs/heads/main/data/githubmirror/clean/vless.txt"
OUTPUT_FILE = "AutoConfigs.txt"

# Ваша кастомная шапка подписок
HEADER_TEXT = """# profile-title: GoidaVpn
# profile-update-interval: 1
#support-url: https://github.com
#announce: 🟢 GoidaVpn Status: Fine 🟢 После 8:00 РКН блокируют некоторые сервера
# мяу
# гав\n\n"""

def fetch_and_merge():
    print("Получение свежих данных из репозитория...")
    try:
        response = requests.get(RAW_CONFIG_URL, timeout=15)
        response.raise_for_status()
        config_data = response.text
    except Exception as e:
        print(f"Не удалось загрузить данные: {e}")
        return False

    print("Фильтрация строк по тегам YouTube/YT в названии...")
    matched_lines = []
    all_lines = []
    
    for line in config_data.splitlines():
        line = line.strip()
        if not line:
            continue
            
        # Сохраняем все конфигурации на случай, если фильтр пуст
        all_lines.append(line)
            
        if '#' in line:
            config_parts = line.split('#')
            config_name = config_parts[-1].lower()
            
            # Ищем упоминания youtube или сокращения yt
            if 'youtube' in config_name or 'yt' in config_name:
                matched_lines.append(line)

    print(f"Найдено строго по фильтру YouTube: {len(matched_lines)}")
    
    # Защита от пустого файла
    if not matched_lines:
        print("Строк с тегом YouTube не найдено. Используем общую базу.")
        matched_lines = all_lines

    if not matched_lines:
        print("Репозиторий источника оказался пуст.")
        return False

    # Перемешиваем список, чтобы конфигурации всегда менялись
    random.shuffle(matched_lines)
    
    # Отбираем ровно ТОП-7 штук
    top_7_configs = matched_lines[:7]
    print(f"Успешно отобрано конфигураций для записи: {len(top_7_configs)}")
    
    print(f"Запись данных в {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(HEADER_TEXT)
        for config in top_7_configs:
            f.write(config + "\n")
    
    print(f"Файл {OUTPUT_FILE} успешно обновлен!")
    return True

if __name__ == "__main__":
    fetch_and_merge()
