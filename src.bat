@echo off

timeout /T 2
echo Activating the Venv. . . 
call venv\Scripts\activate

:migrate
set /p app=Application name:

py manage.py makemigrations %app%
py manage.py migrate
goto :eof

:run
echo Activating the Venv. . . 
call venv\Scripts\activate

timeout /T 3
echo  Running Django Project. . .

start /b python manage.py runserver   
timeout /T 1

start http://127.0.0.1:8000/
goto :eof


timeout /T 2
set /p inp=What you wanna do:
if %inp%="migrate" 


