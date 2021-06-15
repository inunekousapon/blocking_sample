# syntax=docker/dockerfile:experimental
FROM python:3.9.5-buster

ENV LANG ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8
ENV APP_ROOT /app

# waitライブラリの追加
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.6.0/wait /wait 
# ライブラリの権限変更
RUN chmod +x /wait

WORKDIR $APP_ROOT
