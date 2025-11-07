# Тестовое задание FastAPI(Books),

## Стек технологий:

- Python 3.13.5
- FastAPI 0.121.0
- Pydantic 2.12.4

## Функциональнсть

- Хранение данных в памяти
- Query параметры для GET-запроса получения списка книг
- Документация (Swagger UI)
- Описание сущностей схем Pydantic

## Установка и запуск:

1. **Клонируйте репозиторий:**

```bash
git clone https://github.com/ReDLiX123/TestFastAPI-books-
cd TestFastAPI-books-
```

2. **Создайте и активируйте виртуальное окружение:**

```bash
# Windows
python -m venv .venv

.venv\Scripts\activate
```

3. **Установите зависимости:**

```bash
pip install -r requirements.txt
```

4. **Запустите сервер:**

```bash
uvicorn main:app --reload
```

## Запуск через Docker(Опционально):

У Вас должен быть установлен Docker, только в этом случае Вы можете запустить приложение в контейнере.

1. **Соберите Docker-образ:**(Docker Desktop должен быть запущен и готов к работе)

```bash
docker build -t fastapi-test .
```

2. **Запустите контейнер:**

```bash
docker run -p 8000:8000 fastapi-test
```

## **Использование:**

После запуска сервера документация API находится по адресу:
http://127.0.0.1:8000/docs
