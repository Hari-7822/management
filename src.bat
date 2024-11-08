@echo off

timeout /T 2

echo Activating the Venv. . . 
call venv\Scripts\activate

timeout /T 3
echo  Running Django Project. . .

start /b python manage.py runserver  
timeout /T 1

start http://127.0.0.1:8000/