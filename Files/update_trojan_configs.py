import requests
import sys
from pathlib import Path
from datetime import datetime

# --- Настройки ---
SOURCE_URL = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/main/data/githubmirror/clean/trojan.txt"
TARGET_FILE_PATH = "data/Githubmirror/trojan/trojan.txt"

# --- Код скрипта ---
def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Загрузка Trojan конфигов...")
    
    try:
        response = requests.get(SOURCE_URL, timeout=30)
        response.raise_for_status()
        new_content = response.text
        print(f"✅ Файл загружен. Размер: {len(new_content)} байт")
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при загрузке: {e}")
        sys.exit(1)

    # Получаем путь к целевому файлу
    target_path = Path(TARGET_FILE_PATH)
    
    # Проверяем parent директорию
    parent_dir = target_path.parent
    if parent_dir.exists() and not parent_dir.is_dir():
        print(f"⚠️ {parent_dir} существует как файл. Удаляем...")
        parent_dir.unlink()
    
    # Создаем директорию
    parent_dir.mkdir(parents=True, exist_ok=True)

    # Сохраняем файл
    target_path.write_text(new_content, encoding='utf-8')
    
    if target_path.exists():
        print(f"✅ Trojan сохранен. Размер: {target_path.stat().st_size} байт")
    else:
        print("❌ Ошибка сохранения Trojan")
        sys.exit(1)

if __name__ == "__main__":
    main()
