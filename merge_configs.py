import os
import random
import requests

# Прямая ссылка (raw) на конфигурации
RAW_CONFIG_URL = "https://githubusercontent.com"
OUTPUT_FILE = "AutoConfigs.txt"

# Ваша кастомная шапка
HEADER_TEXT = """# ==========================================
# ТОП-7 КОНФИГУРАЦИЙ ДЛЯ YOUTUBE
# Обновляется автономно через GitHub Actions
# ==========================================\n\n"""

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
            
        # Запоминаем вообще все конфигурации на случай, если фильтр не сработает
        all_lines.append(line)
            
        if '#' in line:
            config_parts = line.split('#')
            config_name = config_parts[-1].lower()
            
            # Проверяем расширенный фильтр: и youtube, и сокращение yt
            if 'youtube' in config_name or 'yt' in config_name:
                matched_lines.append(line)

    print(f"Найдено строго по фильтру YouTube: {len(matched_lines)}")
    
    # ЗАЩИТА: Если по фильтру ничего не нашлось, берем любые конфигурации из файла
    if not matched_lines:
        print("Строк с тегом YouTube не найдено. Используем общие рабочие конфигурации.")
        matched_lines = all_lines

    if not matched_lines:
        print("Репозиторий источника пуст. Прерывание.")
        return False

    # Перемешиваем список, чтобы конфигурации всегда менялись при обновлении
    random.shuffle(matched_lines)
    
    # Отбираем ровно 7 штук
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
