@echo off
call "venv/Scripts/activate" & cd python manage.py runserver & start http://127.0.0.1:8000/