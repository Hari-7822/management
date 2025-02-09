@REM @echo off

@REM timeout /T 2
@REM echo Activating the Venv. . . 
@REM call venv\Scripts\activate



@REM :migrate
@REM set /p app=Application name:

@REM py manage.py makemigrations %app%
@REM py manage.py migrate
@REM goto :eof

@REM :run
@REM echo Activating the Venv. . . 
@REM call venv\Scripts\activate

@REM timeout /T 3

@REM start http://127.0.0.1:8000/
@REM echo  Running Django Project. . .

@REM start /b python manage.py runserver   
@REM timeout /T 1

@REM goto :eof


@REM timeout /T 2
@REM set /p inp=What you wanna do:
@REM if %inp%="run" (
@REM     call :run
@REM )
@REM if %inp%="migrate"( call :migrate)



@echo off



FOR /F "tokens=*" %%a IN ('ipconfig') DO (

    echo %%a

)