web: gunicorn carigara.wsgi:application
release: python manage.py migrate --noinput && python setup_demo_data.py
