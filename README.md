# EffectiveMobile UI Tests

Фреймворк для автоматизации UI-тестов с использованием **Playwright**, **Pytest**, **Allure**, 
**Github Actions** и паттернов 
проектирования: **Page Object Model**, **Chain of Invocations**, **Loadable Page**.
Поддерживается запуск локально через Docker с автоматической генерацией Allure-отчётов.

---

## 📌 Предварительные требования

### Перед запуском необходимо установить:

1. **Java JDK**  
   👉 [Скачать JDK](https://adoptium.net/temurin/releases/)


2. **Docker Desktop**  
👉 [Скачать Docker](https://www.docker.com/products/docker-desktop/)


3. **Allure CLI**  
   👉 [Скачать Allure CLI](https://github.com/allure-framework/allure2/releases) 

   > На Linux/macOS можно также установить через пакетный менеджер:  
   - Ubuntu/Debian: `sudo apt install allure`  
   - macOS (Homebrew): `brew install allure`

---

## 🚀 Запуск тестов

## Linux/macOS
В корне проекта найти скрипт и выполнить в терминале:

```bash
./run_tests_with_report.sh
```
### Скрипт:

 - Проверит наличие Docker и Allure CLI (при отсутствии — установит через официальные репозитории).

 - Соберёт Docker-образ с тестами.

 - Запустит тесты внутри контейнера.

 - Сгенерирует Allure-отчёт.

 - Автоматически откроет отчёт в браузере.

---

## Windows
В корне проекта найти скрипт и запустить:

```bash
run_tests_with_report.bat
```
### Скрипт:

 - Проверит наличие Docker и Allure CLI (при отсутствии предложит инструкции по установке).
 - Соберёт Docker-образ с тестами.
 - Запустит тесты внутри контейнера.
 - Сгенерирует Allure-отчёт.
 - Автоматически откроет отчёт в браузере.

---