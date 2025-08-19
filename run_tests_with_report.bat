@echo off
REM Сборка Docker-образа
docker build -t effective-mobile-tests .

REM Очистка старых результатов
rmdir /s /q allure-results
rmdir /s /q allure-report
mkdir allure-results
mkdir allure-report

REM Запуск тестов внутри контейнера
docker run --rm -v %cd%\allure-results:/app/allure-results effective-mobile-tests

REM Генерация Allure отчета внутри контейнера
docker run --rm -v %cd%\allure-results:/app/allure-results -v %cd%\allure-report:/app/allure-report effective-mobile-tests allure generate /app/allure-results -o /app/allure-report --clean

REM Открыть отчет
allure open allure-report
