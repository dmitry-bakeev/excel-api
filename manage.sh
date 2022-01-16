#!/bin/bash

docker-compose run --rm --entrypoint /usr/bin/env backend python manage.py "$@"
