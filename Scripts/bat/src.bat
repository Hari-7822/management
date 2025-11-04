@echo off
setlocal
set "addr=192.168.29.240:8000"
cd ../../
ping localhost -n 3 >nul

echo Activating the virtual environment...
call venv\Scripts\activate

ping localhost -n 4 >nul

echo Running Django Project...
start http://%addr%

ping localhost -n 2 >nul

start cmd /k python manage.py runserver %addr%

endlocal
