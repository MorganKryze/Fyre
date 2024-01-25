echo "----- Creating translation ids -----"
python manage.py makemessages -l en -i "assets*"
python manage.py makemessages -l fr -i "assets*"
echo "----- Done -----"
