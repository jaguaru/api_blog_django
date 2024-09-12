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


# Interacting with the REST API

This REST API consists of two sections, the first is for user authentication and the second is for create, read, update and delete Posts and Comments.

The first step is to get an application, such as Postman or another similar application, to make local and remote http requests and get a response.

### User Register: To interact with the application, the first thing we must do is create a user with the following data: username, email and password.

    Request:

    URL: http://127.0.0.1:8000/api/register/
    Method: POST
    Body:

        {
            "username": "user_01",
            "email": "user_01@example.com",
            "password": "Mypassword_01"
        }
    
    Response:

        {
            "message": "Successfully created user!"
        }

### Generate User Token: In this section we need to put the user data entered in the previous step.

    Request:

    URL: http://127.0.0.1:8000/api/token/
    Method: POST
    Body:

        {
            "username": "user_01",
            "password": "Mypassword_01"
        }
    
    Response:

        {

            "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjI1MzI4MSwiaWF0IjoxNzI2MTY2ODgxLCJqdGkiOiJhOTMxOGY0ODI3MGU0ZDM1YmRiNzg3YTAxYTZjMGY2YSIsInVzZXJfaWQiOjR9.jS1LHtX_okJvUr7QA9HjOAI_HPL2kJOqQ027bdpV7fs",
            "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2MTY4NjgxLCJpYXQiOjE3MjYxNjY4ODEsImp0aSI6IjBhZDQ4ZTYxODY5NzRkMTE5OGI4YjU2NGMxYzllMjI5IiwidXNlcl9pZCI6NH0.wsomb5wHXKZM4liTmYpZgxlrZmud03BEcKFg5IlbY0c"

        }

