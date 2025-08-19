@echo off
REM Build Docker image
docker build -t effective-mobile-tests .

REM Clearing old results
rmdir /s /q allure-results
rmdir /s /q allure-report
mkdir allure-results
mkdir allure-report

REM Running tests
docker run --rm -v %cd%\allure-results:/app/allure-results effective-mobile-tests

REM Generating a report
docker run --rm -v %cd%\allure-results:/app/allure-results -v %cd%\allure-report:/app/allure-report effective-mobile-tests allure generate /app/allure-results -o /app/allure-report --clean

REM Open report
allure open allure-report
