#!/usr/bin/bash

commit_message = $(wc -l < $1)
# read -sp "Enter commit message :  " msg
echo
git add .
git commit -m $1
git pull origin 
git push
