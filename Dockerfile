FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY . /app/

RUN pip install -r requirements.txt
