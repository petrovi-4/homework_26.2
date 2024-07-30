#Платформа онлайн обучения


##Технологии использованные в проекте
- Python 3.12
- Django 5.0.6
- DRF 3.15.2
- PostgreSQL
- Celery 5.4.0
- Redis 5.0.7
- Docker


## Инструкция по развертыванию проекта
**<span style="color:green">Клонировать репозиторий:</span>**

```
git@github.com:petrovi-4/homework_26.2.git
```

### <span style="color:red">Из Docker контейнера</span>

**<span style="color:green">Запустить контейнер</span>**

```
docker-compose up -d —build 
```

### <span style="color:red">Без Docker</span>

**<span style="color:green">Создать и активировать виртуальное окружение:</span>**

```
python3 -m venv env         (для Unix-систем)
source env/bin/activate     (для Unix-систем)
```
```
python -m venv env          (для Windows-систем)
env/Scripts/activate.bat    (для Windows-систем)
```

**<span style="color:green">Установка зависимостей из файла requirements.txt:</span>**

```
python3 -m pip install --upgrade pip    (для Unix-систем)
python -m pip install --upgrade pip     (для Windows-систем)
```
```
pip install -r requirements.txt
```

**<span style="color:green">Выполнить миграции:</span>**

```
python3 manage.py migrate   (для Unix-систем) 
python manage.py migrate    (для Windows-систем)
```

**<span style="color:green">Запуск проекта:</span>**

```
python3 manage.py runserver (для Unix-систем)
python manage.py runserver  (для Windows-систем)
```

**<span style="color:green">Запуск переодической задачи по отправке уведомлений через Telegram:</span>**

```
celery -A config worker -l INFO -P eventlet
celery -A config  beat -l info
```

**<span style="color:green">Документация API:</span>**

```
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
```




**<span style="color:maroon">Автор</span>**  
[Мартынов Сергей](https://github.com/petrovi-4)

![GitHub User's stars](https://img.shields.io/github/stars/petrovi-4?label=Stars&style=social)
![licence](https://img.shields.io/badge/licence-GPL--3.0-green)
