echo "----- Building static files -----"
python manage.py collectstatic --noinput --clear -i admin -i data
echo "----- Running server -----"
python manage.py runserver
echo "----- Done -----"