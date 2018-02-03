# modern-django-1000px

## how to install this project

* create your virtualenv (optional)

  ```bash
  $ pip3 install virtualenv
  $ virtualenv -python3 venv
  $ source ./venv/bin/activate
  ```

* install project dependencies

  ```bash
    (venv) $ pip install -Ur ./requirements/base.txt
  ```

## how to run the server

* migrate database (first time only)

  ```bash
    (venv) $ python manage.py makemigrations
    (venv) $ python manage.py migrate
  ```

* run server

  ```bash
    (venv) $ export DJANGO_SETTINGS_MODULE="config.settings.<specify your desired settings file e.g: local.py>"
    (venv) $ python manage.py runserver
  ```
