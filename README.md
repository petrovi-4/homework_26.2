# Платформа онлайн обучения


## Технологии использованные в проекте
- Python 3.12
- Django 5.0.6
- DRF 3.15.2
- PostgreSQL
- Celery 5.4.0
- Redis 5.0.7
- Docker


## Инструкция по развертыванию проекта
**Клонировать репозиторий:**

```
git@github.com:petrovi-4/homework_26.2.git
```

### Из Docker контейнера

**Запустить контейнер**

```
docker-compose up -d —build 
```

### Без Docker

**Создать и активировать виртуальное окружение:**

```
python3 -m venv env         (для Unix-систем)
source env/bin/activate     (для Unix-систем)
```
```
python -m venv env          (для Windows-систем)
env/Scripts/activate.bat    (для Windows-систем)
```

**Установка зависимостей из файла requirements.txt:**

```
python3 -m pip install --upgrade pip    (для Unix-систем)
python -m pip install --upgrade pip     (для Windows-систем)
```
```
pip install -r requirements.txt
```

**Выполнить миграции:**

```
python3 manage.py migrate   (для Unix-систем) 
python manage.py migrate    (для Windows-систем)
```

**Запуск проекта:**

```
python3 manage.py runserver (для Unix-систем)
python manage.py runserver  (для Windows-систем)
```

**Запуск переодической задачи по отправке уведомлений через Telegram:**

```
celery -A config worker -l INFO -P eventlet
celery -A config  beat -l info
```

**Документация API:**

```
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
```




**Автор**  
[Мартынов Сергей](https://github.com/petrovi-4)

![GitHub User's stars](https://img.shields.io/github/stars/petrovi-4?label=Stars&style=social)
![licence](https://img.shields.io/badge/licence-GPL--3.0-green)