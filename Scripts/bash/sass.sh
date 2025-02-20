#!/usr/bin/bash

source venv/bin/activate
echo "Your current directory -> $PWD"
read -sp "Sass file path :  " sass_path
read -sp "Css output path :  " out_path

sleep 1
python3 manage.py sass --watch --no-source-map $sass_path $out_path