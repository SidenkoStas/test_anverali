# Table of Contents
1. [Функционал приложения](#функционал-приложения)
2. [Используемый стек технологий](#используемый-стек-технологий)
3. [Инструкция для запуска](#инструкция-для-запуска)
   1. [Python зависимости](#python-зависимости)
   2. [Первое задание](#первое-задание)
   3. [Второе задание](#второе-задание)






# Функционал приложения.

Приложение включает Django с моделью пользователя и 2-мя различными кабинетами для заказчика и исполнителя.
В папке ckecker программа для проверки и обновления поля пол битрикс лидов на основе их имён.


# Используемый стек технологий.
- Python
- Django
- PostgreSQL
- psycopg
- fast-bitrix24


# Инструкция для запуска.

## Python зависимости
Для установки всех необходимых библиотек запустить в терминале:
```
pip install -r requirements.txt
```

# Первое задание

## Переменные окружения.
**В папке checker создать файл расширения _.settings_**
Для базы данных Postgresql где хранятся таблицы с женскими и мужскими именами указать следуюшие переменные:
```
POSTGRES_DB=XXXXXXXX
POSTGRES_USER=XXXXXXXX
POSTGRES_PASSWORD=XXXXXXXX
HOST=XXXXXXXX
PORT=XXXX
```
**Для подключения к bitrix впишите webhook**
```
WEBHOOK=XXXXXXX
```

## Запустите программу из папки checker
```
python main.py
```


# Второе задание

## Переменные окружения.
**В папке bitrix24 создать файл расширения _.env_**
```
SECRET_KEY=XXXXXX
DEBUG=XXXX
ALLOWED_HOSTS=XXXXXX XXXXXXX # Перечислить все необходимые хосты через пробел.
```
Для базы данных Postgresql указать следуюшие переменные:
```
POSTGRES_DB=XXXXXXXX
POSTGRES_USER=XXXXXXXX
POSTGRES_PASSWORD=XXXXXXXX
HOST=XXXXXXXX
PORT=XXXX
```

## Выполните инструкции для создания и наполнения базы данных и создания суперпользователя:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Запустите сервер Django:

```
python manage.py runserver
```

**По умолчанию проект работает на порту 8000.**