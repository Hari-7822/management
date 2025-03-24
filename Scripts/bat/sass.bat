@echo off
cd ../../
echo Activating the virtual environment...
call venv/Scripts/activate
set base_uri= ./students/static/
    start py manage.py sass %base_uri%sass/ %base_uri%css/ --watch