# GoidaVpn

> **Your path to a free life / Ваш путь к свободной жизни.**

[![GitHub Stars](https://img.shields.io/github/stars/tourrty-droid/GoidaVpn?style=flat-square)](https://github.com/tourrty-droid/GoidaVpn)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Platform Support](https://img.shields.io/badge/platform-Android%20|%20iOS%20|%20Windows%20|%20macOS%20|%20Linux-brightgreen?style=flat-square)](https://github.com/tourrty-droid/GoidaVpn)

---

## 📋 Table of Contents / Содержание

- [English](#english)
- [Русский](#русский)

---

## English

### 🎯 About

GoidaVpn provides regularly updated text configurations for bypassing internet restrictions. The repository contains valid URI-addresses for popular VPN clients supporting Xray/V2Ray protocols.

### ✨ Features

- 🔄 **Regularly Updated** - Configurations updated automatically to maintain reliability
- 🌍 **Multi-Platform** - Support for Android, iOS, Windows, macOS, and Linux
- 📱 **Multiple Clients** - Compatible with v2rayNG, Hiddify, NekoBox, and other Xray/V2Ray clients
- ⚡ **Easy Setup** - Simple import process with just a few clicks
- 🔌 **Auto-Update** - Subscription URL support for automatic server updates
- 📝 **Well-Documented** - Clear instructions for setup and troubleshooting

### 🗳️ Community Feedback

We value your opinion! Please share your ideas and suggestions here:
👉 [Join the Discussion](https://github.com/tourrty-droid/GoidaVpn/discussions/2#discussion-10215496)

### 📊 Live Status

| Platform | Status | Link |
| :--- | :--- | :--- |
| **Android / iOS** | 🟢 Active | [View Configs](https://github.com/tourrty-droid/GoidaVpn/blob/main/GoidaVpn_mobile) |
| **Windows / macOS / Linux** | 🛠️ In Development | Temporary maintenance |
| **Android TV** | 🛠️ In Development | ~4 servers blocked by RKN |

### 🗂 Repository Structure

The root directory contains text files (`.txt`) with ready-to-use configuration strings:

- **Valid URI-Addresses**: Each line in the files (e.g., `vless://...`, `hysteria2://...`) is ready for instant import into your VPN client
- **Easy Access**: Browse files directly on GitHub and copy configurations
- **Raw URLs**: Each file has a raw URL for subscription-based auto-updates

### 🚀 Quick Start Guide

VPN configurations from this repository can be used in any client supporting **Xray/V2Ray** on Android, Windows, macOS, and Linux.

#### Method 1: Direct Import (Copy-Paste)

1. Open the required text file in the root directory of this repository
2. Copy one or multiple configuration lines
3. Open your VPN client (e.g., **v2rayNG**, **Hiddify**, or **NekoBox**)
4. Select the **"Import profiles from clipboard"** option
5. Run a latency test (ping) and connect to your chosen server

#### Method 2: Subscription URL (Auto-Update)

For automatic server updates within your client:

1. Click on the desired text file in GitHub
2. Click the **Raw** button in the upper right corner
3. Copy the URL from your browser's address bar
4. Paste this URL in your app's **"Subscription URLs"** section
5. Perform an update to fetch the latest configurations

### 🛠 Troubleshooting

- **Connection Error (Handshake timeout / Network unavailable)**
  - Run a latency test in the app to refresh the server list
  - If the issue persists, update your configurations to get fresh servers
  - Try different servers from the list

- **Configurations Won't Import**
  - Ensure the copied line doesn't contain extra spaces or line breaks
  - Use clipboard tools to clean the text before importing
  - Verify your client supports the protocol (VLESS, Hysteria2, etc.)

- **Server Blocked or Not Working**
  - Test different servers from the list
  - Check if your ISP/region has specific blocks
  - Try updating your configuration list

### 👥 Credits & Sources

The configuration database and server distribution logic are based on community contributions:

- [AvenCores/goida-vpn-configs](https://github.com/AvenCores/goida-vpn-configs) - Original free VPN configurations repository
- Community members and contributors who help maintain these configs

### 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### ⚠️ Disclaimer

This project is provided for educational and legitimate purposes only. Users are responsible for ensuring their use complies with local laws and regulations.

---

## Русский

### 🎯 О проекте

GoidaVpn содержит регулярно обновляемые текстовые конфигурации для обхода интернет-ограничений. Репозиторий содержит валидные URI-адреса для популярных VPN-клиентов с поддержкой протоколов Xray/V2Ray.

### ✨ Возможности

- 🔄 **Регулярное обновление** - Конфигурации обновляются автоматически для надежности
- 🌍 **Мультиплатформенность** - Поддержка Android, iOS, Windows, macOS и Linux
- 📱 **Множество клиентов** - Совместимость с v2rayNG, Hiddify, NekoBox и другими клиентами Xray/V2Ray
- ⚡ **Легкая настройка** - Простой процесс импорта в несколько кликов
- 🔌 **Автообновление** - Поддержка URL-подписок для автоматического обновления серверов
- 📝 **Подробная документация** - Четкие инструкции по настройке и решению проблем

### 🗳️ Примите участие в развитии проекта!

Нам важно ваше мнение. Пожалуйста, напишите свою идею по этой ссылке:
👉 [Перейти в обсуждения](https://github.com/tourrty-droid/GoidaVpn/discussions/2#discussion-10215496)

### 📊 Live-Статус

| Платформа | Статус | Ссылка |
| :--- | :--- | :--- |
| **Android / iOS** | 🟢 Активно | [Просмотр конфигов](https://github.com/tourrty-droid/GoidaVpn/blob/main/GoidaVpn_mobile) |
| **Windows / macOS / Linux** | 🛠️ В разработке | Временное обслуживание |
| **Android TV** | 🛠️ В разработке | ~4 сервера заблокировано РКН |

### 🗂 Структура репозитория

В корневой директории проекта расположены текстовые файлы (`.txt`), содержащие готовые строки конфигураций:

- **Валидные URI-адреса**: Каждая строка в файле (например, `vless://...`, `hysteria2://...`) готова к моментальному импорту в ваш VPN-клиент
- **Легкий доступ**: Просмотрите файлы прямо на GitHub и скопируйте нужные конфигурации
- **Raw URL-ы**: Каждый файл имеет raw URL для подписок с автообновлением

### 🚀 Инструкция по использованию

Конфигурации из данного репозитория можно использовать в любых клиентах с поддержкой **Xray/V2Ray** на Android, Windows, macOS и Linux.

#### Вариант 1: Прямой импорт строк (из буфера обмена)

1. Откройте необходимый текстовый файл в корне этого репозитория
2. Скопируйте одну или несколько строк конфигурации
3. Откройте ваш VPN-клиент (например, **v2rayNG**, **Hiddify** или **NekoBox**)
4. Выберите функцию **«Импорт профилей из буфера обмена»**
5. Проведите тест задержки (пинга) и запустите подключение к выбранному серверу

#### Вариант 2: Использование в качестве URL-подписки (автоматическое обновление)

Для автоматического обновления серверов внутри клиента используйте прямые ссылки на сырые (raw) файлы:

1. Нажмите на нужный текстовый файл в интерфейсе GitHub
2. Нажмите кнопку **Raw** в верхнем правом углу содержимого файла
3. Скопируйте полученный URL-адрес из адресной строки браузера
4. Вставьте этот URL в своем приложении в раздел **«Группы подписок» (Subscription-ссылки)** и выполните обновление

### 🛠 Решение возможных проблем

- **Ошибка соединения (Handshake timeout / Отсутствие сети)**
  - Выполните повторный тест задержки в приложении для актуализации списка
  - Если проблема сохраняется, обновите конфигурации для получения свежих серверов
  - Попробуйте подключиться к другому серверу из списка

- **Конфигурации не импортируются**
  - Убедитесь, что копируемая строка не содержит лишних пробелов и символов переноса строки
  - Используйте инструменты буфера обмена для очистки текста перед импортом
  - Проверьте, что ваш клиент поддерживает нужный протокол (VLESS, Hysteria2, и т.д.)

- **Сервер заблокирован или не работает**
  - Попробуйте подключиться к другому серверу из списка
  - Проверьте, блокирует ли ваш провайдер/регион определенные адреса
  - Попробуйте обновить список конфигураций

### 👥 Источники и благодарности

База конфигураций и логика распределения серверов опираются на наработки сообщества:

- [AvenCores/goida-vpn-configs](https://github.com/AvenCores/goida-vpn-configs) — оригинальный репозиторий бесплатных VPN-конфигураций
- Члены сообщества и контрибьюторы, помогающие поддерживать эти конфигурации

### 📝 Лицензия

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для подробностей.

### ⚠️ Дисклеймер

Этот проект предоставляется в образовательных и законных целях. Пользователи несут ответственность за соответствие своего использования местным законам и нормативным актам.

---

## 🤝 Contributing / Контрибьютинг

Contributions are welcome! Feel free to:
- Report issues and bugs
- Suggest improvements
- Submit pull requests
- Share configuration sources

Контрибьюции приветствуются! Вы можете:
- Сообщать об ошибках
- Предлагать улучшения
- Отправлять pull requests
- Делиться источниками конфигураций

---

**Last Updated / Последнее обновление**: June 2026
