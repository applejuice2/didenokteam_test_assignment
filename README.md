### Тестовое задание для Didenok Team.

Задача -  разработать менеджер паролей с методами GET и POST. Пароль хранится в БД, привязанный к имени сервиса, который указывается при создании пароля.

### Реализовано
 -  Хранение пароля в БД в зашифрованном виде
 - Эндпоинт для получения информации о всех сервисах, а также добавления нового сервиса с паролем и обновлением старого, фильтрация по service_name
 - Получение имени сервиса идёт посредством URL
 - Подготовлен `Dockerfile` для веб-приложения
 - Подготовлен конфиг `docker-compose.yml` для развертывания контейнеров (БД + веб-приложение) одной командой
 - Проведено тестирование основных модулей проекта

### Технические детали
Технологии: Python, Django, Django REST Framework, PostgreSQL (Django ORM), Docker / docker-compose, Unittest

### Развертывание

Локальное развертывание в macOS (алгоритм может меняться в зависимости от ОС):

1. Склонировать репозиторий 
```
git clone https://github.com/applejuice2/didenok_team_test_assignment.git
```
2. Создать файл .env с кредами в директории infra (пример находиться в директории infra - .env.example)

3. Собрать контейнеры и запустить их (вызвав из директории infra следующую команду)
```
docker-compose up -d --build 
```
4. Дождаться установки всех зависимостей и поднятия контейнеров
5. Выполнить по очереди следующие команды: запустить миграции в БД, создать суперюзера, собрать статику
```
docker-compose exec web python manage.py makemigrations 
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```

6. Для запуска тестов выполнить команду:
```
docker-compose exec web python manage.py test
``` 
7. Перейти в http://127.0.0.1:8000/password/

### Доступные эндпоинты

- `GET /password/` - отображение сервисов с паролями.
- `POST /password/{service_name}/` - создание пароля/замена существующего пароля.
- `GET /password/{service_name}/` - получение пароля по имени сервиса.
- `GET /password/?service_name={part_of_service_name}` -  поиск по **part_of_service_name** и выдача паролей с подходящими service_name
