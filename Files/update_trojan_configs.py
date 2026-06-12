import requests
import sys
from pathlib import Path

# --- Настройки ---
# Ссылка на исходный файл с Trojan конфигами (замените на актуальную)
SOURCE_URL = "https://raw.githubusercontent.com/kort0881/vpn-vless-configs-russia/main/data/githubmirror/clean/trojan.txt"
TARGET_FILE_PATH = "data/Githubmirror/trojan/trojan.txt"

# --- Код скрипта ---
def main():
    print(f"🚀 Загрузка Trojan конфигов из {SOURCE_URL}...")
    try:
        response = requests.get(SOURCE_URL, timeout=30)
        response.raise_for_status()
        new_content = response.text
        print(f"✅ Файл загружен. Размер: {len(new_content)} байт")
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при загрузке файла: {e}")
        sys.exit(1)

    # Получаем путь к целевому файлу
    target_path = Path(TARGET_FILE_PATH)
    
    # Проверяем, не существует ли parent как файл
    parent_dir = target_path.parent
    
    if parent_dir.exists() and not parent_dir.is_dir():
        print(f"⚠️ {parent_dir} существует как файл, а не директория. Удаляем...")
        parent_dir.unlink()
    
    # Создаем директорию
    parent_dir.mkdir(parents=True, exist_ok=True)
    print(f"✅ Директория {parent_dir} готова")

    # Сохраняем файл
    print(f"💾 Сохраняем файл в {TARGET_FILE_PATH}...")
    target_path.write_text(new_content, encoding='utf-8')
    
    # Проверяем результат
    if target_path.exists():
        print(f"✅ Trojan конфиги успешно сохранены. Размер: {target_path.stat().st_size} байт")
        print(f"✅ Первые 100 символов: {new_content[:100]}...")
    else:
        print("❌ Ошибка: файл не был создан")
        sys.exit(1)

if __name__ == "__main__":
    main()
