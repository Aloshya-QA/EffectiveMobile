FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    fonts-liberation \
    libnss3 \
    libatk-bridge2.0-0 \
    libxkbcommon0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m playwright install

RUN wget https://github.com/allure-framework/allure2/releases/download/2.16.0/allure-2.16.0.zip \
    && unzip allure-2.16.0.zip -d /opt/ \
    && ln -s /opt/allure-2.16.0/bin/allure /usr/bin/allure \
    && rm allure-2.16.0.zip

CMD ["pytest", "--alluredir=allure-results"]
