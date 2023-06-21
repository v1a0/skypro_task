## О проекте

Тестовое задание от SkyPro.

> Шаг 1. Создайте API эндпоинты 
> 
> - GET /resume
> - PATCH /resume (Права только у пользователя-владельца)
> 
> Схема данных:
> - status: ...
> - grade:  ...
> - specialty: ...
> - salary: ...
> - education: ...
> - experience: ...
> - portfolio: ...
> - title: ...
> - phone: ...
> - email: ….
>
> Шаг 2. Напишите тесты на эти два эндпоинта с помощью APIClient. 

## О решении

Авторизация пользователя происходит по средствам `BasicAuth`. 

Swagger доступен по адресу http://127.0.0.1:8000/swagger после запуска проекта.


## Сборка и запуск

### Установка зависимостей

```shell
cd skypro_task
python -m pip install -r reqirments.txt
```

### Миграции и инициализация тестовых данных 

```shell
cd src
python manage.py migrate
python manage.py loaddata fixtures/users.json
```

После исполнения скрипта будут созданы следующие учетный записи (логин:пароль):

- user_1:user_1
- user_2:user_2

Для первого пользователя произойдет инициализация резюме, для второго резюме будет
первородно пустым (по умолчанию).


### Запуск сервера


```shell
python manage.py runserver 127.0.0.1:8000
```


### Запуск тестов
```shell
python manage.py test
```


## Примеры запросов

```shell
curl --location --request GET 'http://127.0.0.1:8000/resume/' \
--header 'Authorization: Basic dXNlcl8xOnVzZXJfMQ==' \
--header 'Cookie: csrftoken=IIvYAdpmDJKcIl5AC6vMo12za6rU7jLc' \
--data-raw ''
```

```shell
curl --location --request PATCH 'http://127.0.0.1:8000/resume/' \
--header 'Authorization: Basic dXNlcl8xOnVzZXJfMQ==' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=IIvYAdpmDJKcIl5AC6vMo12za6rU7jLc' \
--data-raw '{
    "status": "active",
    "grade": "middle",
    "specialty": "backend",
    "salary": 200002,
    "education": "Harvard",
    "experience": "Apple, Google, Amazon",
    "portfolio": "https://example.com/resume",
    "title": "Backend Developer 2023",
    "phone": "+71337137713",
    "email": "contact@mail.com"
}'
```