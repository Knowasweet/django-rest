# Famous persons (Django Rest Framework)

The project contains information about people from the series.
Use swagger to check all api documentation.

## Technical stack, technologies

- Python 3.10
- Django
- Django Rest Framework
- Djoser
- Swagger
- Docker, Docker-compose
- PostgreSQL

## Project Setup

Install required packages:
```
pip3 install -r requirements.txt
```
Initialize database:
```
python manage.py migrate
```
Start application:
```
python manage.py runserver 127.0.0.1:<your_port>
```
Check api
```
http://127.0.0.1:<your_port>/swagger/
```
## Docker Build Setup
```
docker-compose up
```