@echo off

timeout /T 2
echo Activating the Venv. . . 
call venv\Scripts\activate

timeout /T 3
echo  Running Django Project. . .

start brave.exe http://127.0.0.1:8000/

timeout /T 1
start /b python manage.py runserver   