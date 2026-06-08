import os
import re
import socket
import time
import urllib.parse
import requests

# Прямая ссылка (raw) на конфигурации
RAW_CONFIG_URL = "https://githubusercontent.com"
OUTPUT_FILE = "AutoConfigs.txt"

# Ваша кастомная шапка
HEADER_TEXT = """# ==========================================
# ТОП-7 САМЫХ БЫСТРЫХ КОНФИГУРАЦИЙ (Фильтр: YouTube)
# Отсортировано по скорости отклика (TCP Ping)
# Обновляется автономно через GitHub Actions
# ==========================================\n\n"""

def measure_ping(vless_link):
    """
    Разбирает строку VLESS, замеряет скорость отклика по TCP в секундах.
    Возвращает время ответа (float) или None, если сервер недоступен.
    """
    try:
        clean_link = vless_link.replace("vless://", "http://")
        parsed = urllib.parse.urlparse(clean_link)
        
        host = parsed.hostname
        port = parsed.port
        
        if not host or not port:
            return None
            
        start_time = time.perf_counter()
        with socket.create_connection((host, int(port)), timeout=2.5):
            end_time = time.perf_counter()
            
        # Возвращаем затраченное время
        return end_time - start_time
    except (socket.timeout, socket.error, ValueError):
        return None

def fetch_and_merge():
    print("Получение свежих данных из репозитория...")
    try:
        response = requests.get(RAW_CONFIG_URL, timeout=15)
        response.raise_for_status()
        config_data = response.text
    except Exception as e:
        print(f"Не удалось загрузить данные: {e}")
        return False

    print("Фильтрация строк по тегу YouTube в названии...")
    matched_lines = []
    
    for line in config_data.splitlines():
        line = line.strip()
        if not line:
            continue
            
        if '#' in line:
            config_parts = line.split('#')
            config_name = config_parts[-1]
            
            if 'youtube' in config_name.lower():
                matched_lines.append(line)

    print(f"Найдено подходящих по имени конфигов: {len(matched_lines)}")
    
    if not matched_lines:
        print("Подходящих конфигов не найдено. Выход.")
        return False

    print("Запуск замера скорости серверов (TCP Ping)...")
    scored_configs = []
    
    for index, config in enumerate(matched_lines, 1):
        print(f"[{index}/{len(matched_lines)}] Тестирование... ", end="", flush=True)
        ping_time = measure_ping(config)
        
        if ping_time is not None:
            ping_ms = int(ping_time * 1000)
            print(f"✅ ОТВЕТ: {ping_ms}ms")
            scored_configs.append((ping_time, config))
        else:
            print("❌ ОТКЛОНЕН")

    if not scored_configs:
        print("Ни один сервер не ответил на запросы. Файл не изменен.")
        return False

    # Сортируем список по возрастанию времени ответа (от самых быстрых к медленным)
    scored_configs.sort(key=lambda x: x[0])
    
    # Отбираем только ТОП-7 лучших серверов
    top_7_configs = [config for _, config in scored_configs[:7]]
    print(f"\nВыбрано лучших серверов для записи: {len(top_7_configs)}")

    print(f"Запись ТОП-7 конфигураций в {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(HEADER_TEXT)
        for config in top_7_configs:
            f.write(config + "\n")
    
    print(f"Файл {OUTPUT_FILE} успешно обновлен!")
    return True

if __name__ == "__main__":
    fetch_and_merge()
