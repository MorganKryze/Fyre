echo "----- Build start -----"
python3.9 -m pip install -r envs/django/requirements.txt
python3.9 manage.py collectstatic --noinput --clear  --ignore admin
echo "----- Done -----"
