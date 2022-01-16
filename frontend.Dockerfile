FROM nginx:stable-alpine

RUN mkdir /app
WORKDIR /app

VOLUME ["/app/staticfiles", "/app/media"]

COPY ./docker/nginx.conf /etc/nginx/nginx.conf
