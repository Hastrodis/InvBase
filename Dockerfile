FROM python:3.6-stretch

ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y python3-dev

WORKDIR /InvBase

# Сначала копируем requirements.txt, для того, чтобы образ собирался быстрее (см. слои докера)
COPY requirements.txt /InvBase/
RUN pip install -r requirements.txt

# Далее копируем сам код приложения
COPY . /InvBase/
WORKDIR /InvBase/

EXPOSE 8000