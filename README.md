# openpost

This project is a simple web application which supports team communications including retrospectives, team sharing, and more.

## Prerequisite

It is recommended to use virtualenv to install required packages.

    $ sudo apt-get install python3 python3-venv python-is-python3
    $ python -m venv venv
    $ source venv/bin/activate
    $ python -m pip install Django django-model-utils coverage

## How to create DB tables

    $ python manage.py makemigrations openpost
    $ python manage.py migrate

## How to run dev-server

You may access the development server via a web-browser after the following command:

    $ python manage.py runserver 0.0.0.0:8000

You can also run the server in the background with the following command:

    $ nohup python manage.py runserver 0.0.0.0:8000 > openpost.log 2>&1 &

## How to run tests

    $ python manage.py test openpost

## How to measure code coverage

    $ coverage run --source='.' manage.py test openpost
    $ coverage report

## How to deactivate the virtualenv

You may deactive the virtualenv using the following command:

    $ deactivate

## License

This project source code is available under MIT license. Please see [LICENSE](LICENSE).
