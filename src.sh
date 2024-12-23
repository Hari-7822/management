#!/bin/bash

sleep 2
echo "Activating the Venv. . ."
source venv/bin/activate

sleep 3
echo "Running Django Project. . ."

xdg-open http://127.0.0.1:8000/

sleep 1
python manage.py runserver &
