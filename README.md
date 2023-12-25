# openpost

This project is a simple web application which supports team communications including retrospectives, team sharing, and more.

## Prerequisite

You need to install the following packages

    $ python -m pip install Django django-model-utils

## How to run tests

    $ python manage.py test openpost

## How to create DB tables

    $ python manage.py makemigrations openpost
    $ python manage.py migrate

## How to run dev-server

You may access the development server via a web-browser after the following command:

    $ python manage.py runserver 0.0.0.0:8000

## How to login as a super user

    $ python manage.py createsuperuser

Then, access http://localhost:8000/admin via a web-browser

## License

This project source code is available under MIT license. Please see [LICENSE](LICENSE).
