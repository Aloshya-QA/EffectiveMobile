#!/bin/bash

# Build Docker image
docker build -t effective-mobile-tests .

# Clearing old results
rm -rf allure-results allure-report
mkdir -p allure-results allure-report

# Running tests
docker run --rm \
    -v $(pwd)/allure-results:/app/allure-results \
    effective-mobile-tests

# Generating a report
docker run --rm \
    -v $(pwd)/allure-results:/app/allure-results \
    -v $(pwd)/allure-report:/app/allure-report \
    effective-mobile-tests \
    allure generate /app/allure-results -o /app/allure-report --clean

# Open report
allure open allure-report
