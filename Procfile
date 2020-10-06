release: python manage.py collectstatic
release: python manage.py migrate
web: gunicorn project.wsgi --log-file -