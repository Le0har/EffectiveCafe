# EffectiveCafe

Полнофункциональное веб-приложение на Django для управления заказами в кафе.

## Возможности EffectiveCafe

- Добавление заказа
- Удаление заказа
- Поиск заказа
- Отображение всех заказов
- Изменение статуса заказа
- Расчет выручки за смену

## Технологии

- python 3.10+ - высокоуровневый язык программирования общего назначения
- django 5.1.3 - фреймворк для веб-приложений на языке Python
- psycopg2-binary 2.9.10 - библиотека взаимодействия с СУБД PostgreSQL

## Установка на локальной машине

1. Клонировать репозиторий c GitHub
```
$ git clone https://github.com/Le0har/EffectiveCafe
```
2. Создать виртуальное окружение
```
$ python3 -m venv django_venv
```
3. Запустить виртуальное окружение
```
$ source django_venv/bin/activate
```
4. Обновить менеджер пакетов pip
```
$ python -m pip install --upgrade pip
```
5. Установить зависимости из ```requirements.txt```
```
$ pip install -r requirements.txt
```
6. Настроить подключение к БД (PostgreSQL) в файле ```settings.py```

- `ENGINE` - механизм, который используется для поключения к БД. В данном проекте - `django.db.backends.postgresql_psycopg2`
- `NAME` - имя БД
- `USER` - имя пользователя для подключения к БД
- `PASSWORD` - пароль для подключения к БД
- `HOST` - хост, на котором располагается БД. В данном проекте - `localhost`
- `PORT` - порт подключения к БД. В данном проекте - `5432`

7. Выполнить миграции
```
$ python manage.py migrate
```

8. Записать данные в БД (опционально)
```
$ python manage.py createdata
```

9. Запустить проект
```
$ python manage.py runserver
```

## Автор

Тихонов Алексей [https://github.com/Le0har](https://github.com/Le0har)