# BlogAPP CRUD for creating Posts and Comments

BlogAPP is a REST API CRUD application built with Django. This allows users to Post and Comment. Posts and comments can be created, deleted, updated and deleted only by the author.

In order to use this application you must have all the necessary packages installed. In the next section you will find instructions to install everything you need.


# Firt steps:

### Dowload the repository:

Open a window console and type

    $ git clone https://github.com/jaguaru/api_blog_django.git

## Setting up the virtual environment:

Open the tickets directory:

    $ cd api_blog_django/

Create the directory and the virtual environment:

    $ python3 -m venv .env/

Activate the virtual environment:

    $ source .venv/bin/activate

Virtual environment activated:

    (.venv) $

Install the required packages:

    (.venv) $ pip install -r requirements.txt

Create the necessary migrations

    $ python manage.py makemigrations
    $ python manage.py migrate

Run the Django server:

    (.venv) $ python3 manage.py runserver

