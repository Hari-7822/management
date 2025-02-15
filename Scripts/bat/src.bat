@echo off

cd ../../
timeout /T 2
echo Activating the Venv. . . 
call venv\Scripts\activate

timeout /T 3
echo Running Django Project. . .

start http://127.0.0.1:8000/

timeout /T 1
start python manage.py runserver