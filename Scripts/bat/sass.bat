@echo off
cd ../../
echo Activating the virtual environment...
call venv/Scripts/activate

@REM set /p inp=What you wanna do(watch(w)/migrate(m)): 
@REM if %inp%="w" (
    start py manage.py sass ./students/static/sass/ ./students/static/css/ --watch
@REM )
@REM if %inp% = "m" (
    @REM start py manage.py  ./students/static/sass/ ./students/static/css/ -g
@REM )
@REM else()


@REM @echo off

@REM :text-gen
@REM setlocal enabledelayedexpansion

@REM set "text=Hello, World!"
@REM for /l %%i in (0, 1, 12) do (
@REM     set "char=!text:~%%i,1!"
@REM     <nul set /p=!char!
@REM     timeout /t 0 /nobreak >nul
@REM     ping -n 1 -w 500 127.0.0.1 >nul
@REM )
@REM echo.
@REM endlocal
@REM EXIT /B 0
@REM call :text-gen 