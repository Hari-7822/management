read -sp "Enter commit message :  " msg
echo
git add .
git commit -m $msg
git pull origin 
git push
