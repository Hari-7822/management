read -sp "Enter commit message :  " msg

git add .

git commit -m $msg

git pull origin 

git push
