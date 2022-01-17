# excel-api
This is the solution of a [test](https://gist.github.com/abj/a073ca103839b20e9876bf09c9791656) task for the position of Python backend developer

## Requirements:

- git
- docker and docker-compose
- postman

## How to run

1. Clone this repo

```bash
# If use https
git clone https://github.com/dmitry-bakeev/excel-api.git

# if use ssh
git clone git@github.com:dmitry-bakeev/excel-api.git
```

2. Run project

```bash
docker-compose up -d
```

4. Create first user

```bash
./manage.sh createsuperuser
```

## API

- `/api/token/` - authorization.
Get `POST` request (json or form-data) with keys `username` and `password`.
Example request:
```json
{
    "username": "admin",
    "password": "password"
}
```
Return json result with `access` and `refresh` tokens.
Example response:
```json
{
    "refresh": "refresh-token",
    "access": "access-token"
}
```

- `/api/token/refresh/` - refresh access token.
Get `POST` request (json or form-data) with key `refresh`.
Example request:
```json
{
    "refresh": "refresh-token"
}
```
Return json result with new `access` token.
Example response:
```json
{
    "access": "access-token"
}
```

- `/excel/upload/` - excel file upload.
Get `POST` request (form-data) with key `path` - file with `.xlsx` or `.xls` extension. Required Bearer token for JWT auth.
Return json result with uploading status.
Example response:
```json
{
    "id": 7,
    "path": "/media/excel/2022/1/17/1.xlsx"
}
```

- `/excel/detail/{id}/` - detail about excel file.
Get `GET` request with `id` in url path.
Return json result with detail information about excel file.
Example response
```json
{
    "id": 7,
    "path": "/media/excel/2022/1/17/1.xlsx",
    "processing_stop": "2022-01-17T12:13:55.685778+03:00",
    "processing_status": "Обработано",
    "processing_result": "removed: 3",
    "created_at": "2022-01-17T12:13:03.178398+03:00"
}
```
