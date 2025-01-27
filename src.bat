@echo off

timeout /T 2
echo Activating the Venv. . . 
call venv\Scripts\activate

timeout /T 3
echo Running Django Project. . .

start http://127.0.0.1:8000/

timeout /T 1
start python manage.py runserver

@REM :loop



@REM   < "server_output.log" (  

@REM     set /a line_count=0

@REM     for /f "tokens=*" %%a in ('find /c /v "Is the server running on that host and accepting TCP/IP connections?"') do set line_count=%%a

@REM     echo Current line count: %line_count%

@REM   )



@REM   timeout /t 15 > nul  



@REM goto loop
