import os
import requests
import hashlib
import sys
from pathlib import Path

# --- Настройки ---
# Ссылка на исходный файл в репозитории kort0881
SOURCE_URL = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/main/data/githubmirror/clean/vless.txt"
# Путь к целевому файлу в вашем репозитории (измените при необходимости)
TARGET_FILE_PATH = "data/Githubmirror/vless"

# --- Код скрипта ---
def main():
    print(f"Загрузка файла из {SOURCE_URL}...")
    try:
        response = requests.get(SOURCE_URL, timeout=30)
        response.raise_for_status()
        new_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке файла: {e}")
        sys.exit(1)

    # Проверяем, существует ли целевой файл локально
    target_path = Path(TARGET_FILE_PATH)
    if not target_path.exists():
        print("Целевой файл не существует. Будет создан новый.")
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(new_content, encoding='utf-8')
        print("Файл успешно создан.")
        return

    # Если файл существует, сравниваем его содержимое
    print("Проверка изменений...")
    old_content = target_path.read_text(encoding='utf-8')
    if old_content == new_content:
        print("Изменений не обнаружено. Обновление не требуется.")
        return

    print("Обнаружены изменения. Обновляю файл...")
    target_path.write_text(new_content, encoding='utf-8')
    print("Файл успешно обновлён.")

if __name__ == "__main__":
    main()
