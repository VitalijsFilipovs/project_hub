📘 project_hub — Django REST API с пагинацией и логированием
📌 Описание
Учебный проект на Django для демонстрации:

Безопасной пагинации (CursorPagination)

Глобальной настройки DRF

Логирования HTTP-запросов, SQL-запросов и системных сообщений

Проект содержит простой API /api/categories/, где можно получить список категорий с постраничной загрузкой.

🚀 Стек технологий
Python 3.13

Django 5.2

Django REST Framework

SQLite (по умолчанию)

Логирование через стандартный logging из Python

✅ Реализовано
🔹 Глобальная пагинация:
python
Копировать код
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE': 6,
}
🔹 Логирование:
Сервер → консоль

HTTP-запросы → logs/http_logs.log

SQL-запросы → logs/db_logs.log

🔹 Категории:
Модель Category(name, created_at)

Эндпоинт /api/categories/

Пагинация через курсоры

JSON-ответы

📁 Структура проекта
bash
Копировать код
project_hub/
├── tasks/
│   ├── models.py        # модель Category
│   ├── views.py         # APIView
│   ├── serializers.py   # DRF-сериализатор
│   ├── urls.py          # маршруты
├── project_hub/
│   ├── settings.py      # конфигурация, включая логгинг и REST
├── logs/
│   ├── http_logs.log    # HTTP-запросы
│   └── db_logs.log      # SQL-запросы
├── db.sqlite3
├── manage.py
📦 Установка и запуск
bash
Копировать код
git clone https://github.com/VitalijsFilipovs/project_hub.git
cd project_hub
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
🔗 Примеры запросов
Список категорий:
GET /api/categories/

👨‍💻 Автор
Виталий Филипов
GitHub профайл
