import os
import requests
import sys
from pathlib import Path

# --- Настройки ---
SOURCE_URL = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/main/data/githubmirror/clean/vless.txt"
TARGET_FILE_PATH = "data/Githubmirror/vless/vless.txt"

# --- Код скрипта ---
def main():
    print(f"Загрузка файла из {SOURCE_URL}...")
    try:
        response = requests.get(SOURCE_URL, timeout=30)
        response.raise_for_status()
        new_content = response.text
        print(f"Файл загружен. Размер: {len(new_content)} байт")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке файла: {e}")
        sys.exit(1)

    # Создаем целевую директорию, если её нет
    target_path = Path(TARGET_FILE_PATH)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Директория {target_path.parent} создана (или уже существует)")

    # Сохраняем файл (всегда перезаписываем)
    print(f"Сохраняем файл в {TARGET_FILE_PATH}...")
    target_path.write_text(new_content, encoding='utf-8')
    
    # Проверяем, что файл создан
    if target_path.exists():
        print(f"✅ Файл успешно сохранен. Размер: {target_path.stat().st_size} байт")
    else:
        print("❌ Ошибка: файл не был создан")
        sys.exit(1)

if __name__ == "__main__":
    main()
