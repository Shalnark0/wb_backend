# WB Backend (FastAPI + PostgreSQL)

Бэкенд для аналитики товаров с Wildberries. Реализован с использованием FastAPI, SQLAlchemy (async), Alembic и PostgreSQL.

## 🚀 Стек технологий

- Python 3.11+
- FastAPI
- SQLAlchemy + AsyncPG
- Alembic (миграции)
- Pydantic
- PostgreSQL
- Uvicorn

## 📦 Установка

1. Клонируйте репозиторий и перейдите в папку проекта:

```bash
git clone <репозиторий>
cd wb_backend
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate    # или venv\Scripts\activate на Windows
```
3. Установите зависимости:

```bash
pip install -r requirements.txt
```
4. Настройте переменные окружения в .env (лежит рядом с app/ и alembic/):

```ini
DATABASE_URL=postgresql://<user>:<password>@localhost:5432/wb_db
```

## 📄 Миграции
1. Создание новой миграции:

```bash
alembic revision --autogenerate -m "описание миграции"
```
2. Применение миграций:

```bash
alembic upgrade head
```

## 🛠 Запуск приложения
```bash
uvicorn app.main:app --reload
```

## 📌 API
```
POST /api/parse: запустить парсинг

GET /api/products: получить список товаров с фильтрами:

min_price

min_rating

min_feedbacks
```

## 📁 Структура
```bash
wb_backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   └── services/
│
├── alembic/
│   ├── versions/
│   └── env.py
├── .env
├── requirements.txt
└── README.md
```