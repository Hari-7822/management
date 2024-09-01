@echo off

timeout /T 4

echo Activating the Venv. . . 
call venv\Scripts\activate

timeout /T 4

echo  Running Django Project. . .
timeout /T 4

start http://127.0.0.1:8000/
python manage.py runserver