#!/bin/bash

# Сборка Docker-образа
docker build -t effective-mobile-tests .

# Очистка старых результатов
rm -rf allure-results allure-report
mkdir -p allure-results allure-report

# Запуск тестов внутри контейнера
docker run --rm \
    -v $(pwd)/allure-results:/app/allure-results \
    effective-mobile-tests

# Генерация Allure отчета внутри контейнера
docker run --rm \
    -v $(pwd)/allure-results:/app/allure-results \
    -v $(pwd)/allure-report:/app/allure-report \
    effective-mobile-tests \
    allure generate /app/allure-results -o /app/allure-report --clean

# Открыть отчет в браузере
allure open allure-report
