echo "----- Building static files -----"
python manage.py collectstatic --noinput --clear --ignore admin
echo "----- Running server -----"
python manage.py runserver
echo "----- Done -----"