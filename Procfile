web: gunicorn django_project.wsgi:application --log-file - --log-level debug
python main.py collectstatic --noinput
main.py migrate
