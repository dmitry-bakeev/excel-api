FROM python:3.8-alpine

WORKDIR /app

# Install native dependencies
RUN apk update && \
    apk add build-base jpeg-dev libpng-dev linux-headers gettext postgresql-dev libxml2-dev libxslt-dev libffi-dev bash

# Install gunicorn
RUN pip install gunicorn

# Install python dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy app files
COPY . .

VOLUME ["/app/staticfiles", "/app/media"]

# Set up
EXPOSE 8000

ENV WORKERS=4
ENTRYPOINT ["/app/docker/django-entrypoint.sh"]
CMD gunicorn -b 0.0.0.0:8000 -w $WORKERS --forwarded-allow-ips="*" main.wsgi:application
