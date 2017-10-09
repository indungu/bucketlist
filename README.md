# Bucketlist-REST-API 
[![Build Status](https://travis-ci.org/indungu/bucketlist.svg?branch=master)](https://travis-ci.org/indungu/bucketlist)

A Django RestFramework based API for creating and managing bucketlists.

This project is - as at this moment - entirely based on the tutorial by Jee Gikera (@gitgik)
posted as a two-part step-by-step test-driven approach on REST API development with Django REST Framework.

The links to the said tutorials are:

  https://scotch.io/tutorial/build-a-rest-api-with-django-a-test-driven-approach-part-1
  
  https://scotch.io/tutorial/build-a-rest-api-with-django-a-test-driven-approach-part-2
  
# Install

To set up and test this project just clone the repository locally, install package dependencies and run the dev server as follows

_Clone Repo_

  `git clone https://github.com/indungu/bucketlist`

_Change directory and install dependencies_

  `cd bucketlist`
  `pip install .`
  `pip install -r requirements.txt`
  
_make initial migrations_
Migrations create a local instance of the database that you will be working with.

  `python manage.py runserver`

_run the dev-server_

  `python manage.py runserver`

# How To Use

The following output is generated when you run the dev server.

  `System check identified no issues (0 silenced).`
  `October 09, 2017 - 17:53:38`
  `Django version 1.11.5, using settings 'bucketlist.settings'`
  `Starting development server at http://127.0.0.1:8000/`
  `Quit the server with CTRL-BREAK.`

In your browser of choice navigate to the url given: 

  `http://127.0.0.1/8000/bucketlists`

or alternatively

  `http://localhost:8000/bucketlists`

This launches a pop-up login window requesting a username and password.
In your console use the following command to create a new superuser account.

  `python manage.py createsuperuser`

Then enter your desired username, email, password then confirm password and you should get the following affirmation

  `Superuser created successfully.`

Use the created user credentials to login.

# 
