FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    default-jre \
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

RUN LATEST=$(curl -s https://api.github.com/repos/allure-framework/allure2/releases/latest \
    | grep "tag_name" | cut -d '"' -f 4) \
    && wget https://github.com/allure-framework/allure2/releases/download/$LATEST/allure-$LATEST.zip -O allure.zip \
    && unzip allure.zip -d /opt/ \
    && ln -s /opt/allure-$LATEST/bin/allure /usr/bin/allure \
    && rm allure.zip

RUN allure --version

CMD ["pytest", "--allure=allure-results"]
