# GoidaVpn

> **Your path to a free life / Ваш путь к свободной жизни.**

<div align="center">
  <img src="https://shields.io" alt="GitHub Stars">
  <img src="https://shields.io" alt="License">
</div>

---

## 📋 Table of Contents / Содержание
- [English](#english)
- [Русский](#русский)

---

# English

### 🎯 About
GoidaVpn provides regularly updated text configurations for bypassing internet restrictions. The repository contains valid URI-addresses for popular VPN clients supporting Xray/V2Ray protocols.

### ⚡ Auto-Update & Core Script
The repository features an automated backend driven by `merge_configs.py`. This script automatically fetches, validates, and merges configuration files into production lists (`AutoConfigs.txt`, `GoidaVpnList1`), ensuring that your subscription nodes are always fresh and functional without manual intervention.

### ✨ Features
- 🔄 **Regularly Updated** - Configurations updated automatically via Python actions to maintain reliability.
- 🔌 **Auto-Update Support** - Native subscription URL support for automatic server updates inside your client.
- 🌍 **Multi-Platform** - Support for Android, iOS, Windows, macOS, and Linux.
- 📱 **Multiple Clients** - Compatible with v2rayNG, Hiddify, NekoBox, and other Xray/V2Ray clients.
- ⚡ **Easy Setup** - Simple import process with just a few clicks.

### 📊 Live Status


| Platform | Status | Link |
| :--- | :---: | :--- |
| **Android / iOS** | 🟢 Active | [View Configs](./AutoConfigs.txt) |
| **Windows / macOS / Linux** | 🛠 In Development | *Temporary maintenance* |
| **Android TV** | 🛠 In Development | *~4 servers blocked by RKN* |

### 🗂 Repository Structure
- `AutoConfigs.txt` / `GoidaVpnList1` — Text files containing ready-to-use configuration strings (`vless://`, `hysteria2://`, etc.).
- `merge_configs.py` — The automation script responsible for keeping the server base updated.

### 🚀 Quick Start Guide

#### Method 1: Direct Import (Copy-Paste)
1. Open `AutoConfigs.txt` or `GoidaVpnList1` in this repository.
2. Copy one or multiple configuration lines.
3. Open your VPN client (**v2rayNG**, **Hiddify**, or **NekoBox**).
4. Select **"Import profiles from clipboard"**.

#### Method 2: Subscription URL (Auto-Update)
1. Click on the desired `.txt` file above.
2. Click the **Raw** button in the upper right corner.
3. Copy the URL from your browser's address bar.
4. Paste this URL into your client's **"Subscription URLs"** section and click update.

---

# Русский

### 🎯 О проекте
GoidaVpn содержит регулярно обновляемые текстовые конфигурации для обхода интернет-ограничений. Репозиторий содержит валидные URI-адреса для популярных VPN-клиентов с поддержкой протоколов Xray/V2Ray.

### ⚡ Автообновление и скрипт слияния
Главная особенность репозитория — полная автоматизация. Скрипт `merge_configs.py` автоматически собирает, фильтрует и объединяет конфигурации рабочих серверов в файлы списков (`AutoConfigs.txt`, `GoidaVpnList1`). Это гарантирует актуальность подписок без необходимости ручного обновления со стороны разработчика.

### ✨ Возможности
- 🔄 **Регулярное обновление** - Конфигурации генерируются автоматически для обеспечения стабильной связи.
- 🔌 **Автообновление подписок** - Поддержка URL-ссылок для автоматического обновления серверов прямо внутри вашего приложения.
- 🌍 **Мультиплатформенность** - Поддержка Android, iOS, Windows, macOS и Linux.
- 📱 **Множество клиентов** - Совместимость с v2rayNG, Hiddify, NekoBox и другими популярными форками Xray.

### 📊 Live-Статус


| Платформа | Статус | Ссылка |
| :--- | :---: | :--- |
| **Android / iOS** | 🟢 Активно | [Просмотр конфигов](./AutoConfigs.txt) |
| **Windows / macOS / Linux** | 🛠 В разработке | *Временное обслуживание* |
| **Android TV** | 🛠 В разработке | *~4 сервера заблокировано РКН* |

### 🗂 Структура репозитория
- `AutoConfigs.txt` / `GoidaVpnList1` — готовые конфигурационные строки (`vless://`, `hysteria2://`), доступные для импорта.
- `merge_configs.py` — Python-скрипт, отвечающий за парсинг и автообновление серверов.

### 🚀 Инструкция по использованию

#### Вариант 1: Прямой импорт строк (из буфера обмена)
1. Откройте файл `AutoConfigs.txt` в корне этого репозитория.
2. Скопируйте одну или несколько строк конфигурации.
3. В VPN-клиенте (**v2rayNG**, **Hiddify**, **NekoBox**) выберите **«Импорт профилей из буфера обмена»**.

#### Вариант 2: Использование в качестве URL-подписки (Автообновление)
1. Откройте нужный `.txt` файл на GitHub.
2. Нажмите кнопку **Raw** в верхнем правом углу.
3. Скопируйте URL-адрес из адресной строки браузера.
4. Вставьте этот URL в своем приложении в раздел **«Группы подписок» (Subscription-ссылки)** и обновите её.

---

### 🛠 Решение проблем / Troubleshooting
- **Handshake timeout / Отсутствие сети**: Проведите тест задержки (ping) в приложении или обновите подписку, чтобы получить свежие IP.
- **Строки не импортируются**: Убедитесь, что при копировании не захватили лишние пробелы.

### 👥 Источники и благодарности
База конфигураций опирается на наработки сообщества, включая:
- [AvenCores/goida-vpn-configs](https://github.com)

### 📝 Лицензия & Дисклеймер
Проект распространяется по лицензии **MIT**. Проект создан исключительно в образовательных целях.
