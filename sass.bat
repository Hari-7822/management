@echo off

call venv/Scritps/activate

start py manage.py ./students/static/sass/ ./students/static/css/ --watch
py manage.py ./students/static/sass/ ./students/static/css/ -g
