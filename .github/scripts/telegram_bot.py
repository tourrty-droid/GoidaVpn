#!/usr/bin/env python3
"""
Telegram-бот для автоматических уведомлений о событиях в репозитории GoidaVPN
Поддерживает: релизы, issues, push, workflow_run (ошибки CI/CD)
"""

import os
import json
import sys
import requests
from datetime import datetime
from typing import Optional, Dict, Any

# Загрузка конфига из переменных окружения GitHub Actions
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
EVENT_NAME = os.getenv("GITHUB_EVENT_NAME")
EVENT_PATH = os.getenv("GITHUB_EVENT_PATH")
REPO_NAME = os.getenv("GITHUB_REPOSITORY", "tourrty-droid/GoidaVpn")
WORKFLOW = os.getenv("GITHUB_WORKFLOW", "")
RUN_ID = os.getenv("GITHUB_RUN_ID", "")
SHA = os.getenv("GITHUB_SHA", "")[:7]

# Конфиг зеркал для уведомлений
MIRRORS = {
    "GitLab": "https://gitlab.com/tourrty-droid/GoidaVpn",
    "GitHub": "https://github.com/tourrty-droid/GoidaVpn",
    "Codeberg": "https://codeberg.org/tourrty-droid/GoidaVpn"
}

# Теги issues, на которые бот отправляет уведомления
SEND_LABELS = ["critical", "broken", "blocked", "mirror", "dns"]


def send_telegram_message(text: str, parse_mode: str = "HTML") -> bool:
    """Отправляет сообщение в Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": False
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"❌ Ошибка отправки в Telegram: {e}")
        return False


def load_event_data() -> Dict[str, Any]:
    """Загружает данные события GitHub"""
    if not EVENT_PATH or not os.path.exists(EVENT_PATH):
        return {}
    with open(EVENT_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def format_release_message(data: Dict) -> str:
    """Форматирует сообщение о новом релизе"""
    release = data.get("release", {})
    tag = release.get("tag_name", "unknown")
    name = release.get("name", tag)
    body = release.get("body", "Без описания")[:300]
    url = release.get("html_url", "")
    is_prerelease = release.get("prerelease", False)

    emoji = "🧪" if is_prerelease else "🚀"
    type_text = "Пре-релиз" if is_prerelease else "Релиз"

    return f"""
{emoji} <b>Новый {type_text}!</b>

<b>Версия:</b> <code>{tag}</code>
<b>Название:</b> {name}

<b>Изменения:</b>
{body}

🔗 <a href="{url}">Скачать на GitHub</a>
    """.strip()


def format_issue_message(data: Dict) -> Optional[str]:
    """Форматирует сообщение о новом issue (только с указанными тегами)"""
    issue = data.get("issue", {})
    labels = [l.get("name", "") for l in issue.get("labels", [])]

    # Отправляем только если есть совпадение с SEND_LABELS
    if not any(label in SEND_LABELS for label in labels):
        return None

    title = issue.get("title", "Без названия")
    url = issue.get("html_url", "")
    user = issue.get("user", {}).get("login", "unknown")
    matched_labels = [l for l in labels if l in SEND_LABELS]
    labels_text = ", ".join([f"#{l}" for l in matched_labels])

    return f"""
🚨 <b>Новое обращение!</b>

<b>Теги:</b> {labels_text}
<b>Заголовок:</b> {title}
<b>От:</b> @{user}

🔗 <a href="{url}">Посмотреть</a>
    """.strip()


def format_push_message(data: Dict) -> Optional[str]:
    """Форматирует сообщение о пуше (синхронизация зеркал)"""
    commits = data.get("commits", [])
    ref = data.get("ref", "")

    if "mirror-sync" in ref or len(commits) == 0:
        return None

    branch = ref.replace("refs/heads/", "")
    commit_list = "\n".join([
        f"• <code>{c.get('id', '')[:7]}</code> {c.get('message', '').split(chr(10))[0][:50]}"
        for c in commits[:5]
    ])

    if len(commits) > 5:
        commit_list += f"\n<i>...и ещё {len(commits) - 5} коммитов</i>"

    return f"""
💻 <b>Обновление кода</b>

<b>Ветка:</b> <code>{branch}</code>
<b>Коммитов:</b> {len(commits)}

{commit_list}

🌐 <b>Зеркала обновлены:</b>
{chr(10).join([f'• <a href="{url}">{name}</a>' for name, url in MIRRORS.items()])}
    """.strip()


def format_workflow_failure(data: Dict) -> str:
    """Форматирует сообщение об ошибке CI/CD"""
    status = data.get("workflow_run", {}).get("conclusion", "failure")
    workflow_name = WORKFLOW or data.get("workflow", {}).get("name", "unknown")
    run_url = f"https://github.com/{REPO_NAME}/actions/runs/{RUN_ID}"

    if status == "success":
        return ""

    return f"""
⚠️ <b>Сбой в CI/CD!</b>

<b>Workflow:</b> {workflow_name}
<b>Статус:</b> ❌ Ошибка
<b>Коммит:</b> <code>{SHA}</code>

🔗 <a href="{run_url}">Посмотреть логи</a>
    """.strip()


def main():
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Не заданы TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID")
        sys.exit(1)

    data = load_event_data()
    message = None

    # Определяем тип события и форматируем сообщение
    handlers = {
        "release": lambda d: format_release_message(d),
        "issues": lambda d: format_issue_message(d),
        "push": lambda d: format_push_message(d),
        "workflow_run": lambda d: format_workflow_failure(d)
    }

    if EVENT_NAME in handlers:
        message = handlers[EVENT_NAME](data)

    if message:
        # Добавляем подпись
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")
        full_message = f"{message}\n\n<i>🕐 {timestamp} | 🤖 GoidaVPN Bot</i>"

        if send_telegram_message(full_message):
            print(f"✅ Уведомление отправлено: {EVENT_NAME}")
        else:
            print(f"❌ Не удалось отправить уведомление")
    else:
        print(f"ℹ️ Событие {EVENT_NAME} не требует уведомления")


if __name__ == "__main__":
    main()
