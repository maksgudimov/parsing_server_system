FROM python:3.11

WORKDIR /app

#COPY requirements.txt .
RUN pip install django==5.0.4
RUN pip install djangorestframework==3.15.1
RUN pip install selenium==4.20.0

RUN pip install webdriver-manager==4.0.1

RUN pip install beautifulsoup4==4.12.3

RUN pip install sentry-sdk==1.41.0

RUN pip install redis==3.5.3

RUN pip install django-redis==4.12.1



# Копируем весь проект
COPY . .