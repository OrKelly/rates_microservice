**Rates** - микросервисы для работы с пользовательскими отзывами. Поддерживает все CRUD операции, а так-же может выводить
средний рейтинг отдельных товаров и список наиболее высоко оцененных

## Локальный запуск
Cоздайте файл .env и перенесите данные из .env.example в него, выставив свои значения.

Далее нужно установить все зависимости посредством команды: 
```
pip install -r requirements.txt
```

После этого необходимо запустить миграции через команды:
```
alembic revision --autogenerate -m 'initial'
alembic upgrade head
```


Приложение запускается при помощи команды:
```
python -m uvicorn app.main:app --reload 
```

Для запуска с помощью Docker используйте команды:
```
docker-compose build
docker-compose up
```


