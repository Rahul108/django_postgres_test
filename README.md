# Overview
This project is for testing purpose only...

# Used
* Django 2.2
* PostgreSQL 12.1

# Instructions
* To install django
```sh
# installing python3
$ sudo apt-get update
$ sudo apt-get install python3.6

# installing pip
$ sudo apt-get install python3-pip

# For Django
$ pip install django
```

* To install postgres
```sh
$ sudo apt-get install postgresql postgresql-contrib
$ sudo apt-get install libpq-dev python-dev
$ pip3 install psycopg2
```

* Opening, Creating a user, Create a database and Set permissions
```sh
# Change user to postgres
$ sudo u postgres

# Accessing on DBMS
$ psql

# Creating a Database with "CREATE DATABASE mydb"
$ CREATE DATABASE test_django_postgres;

# Creating an user with " CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypass'"
$ CREATE USER rahulsarker WITH ENCRYPTED PASSWORD '465757';

# Permissions
$ ALTER ROLE rahulsarker SET client_encoding TO 'utf8';
$ ALTER ROLE rahulsarker SET default_transaction_isolation TO 'read committed';
$ ALTER ROLE rahulsarker SET timezone TO 'UTC';
$ GRANT ALL PRIVILEGES ON DATABASE test_django_postgres TO rahulsarker;
```

* Connecting database to django : Open django_postgres > settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_django_postgres',
        'USER': 'rahulsarker',
        'PASSWORD': '465757',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

* Run Django project & migrate database
```sh
# Go to project directory and then
$ python3 manage.py makemigrations
$ python3 manage.py migrate

# For Django-Administration:
$ python3 manage.py createsuperuser

# To run django server
python3 manage.py runserver
```

# Resources
* [Django Official Documentaion](https://docs.djangoproject.com/en/2.2/)
