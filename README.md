
#How to run tutorial
####cpython 3.6.9
~~~~
- git clone {rep}
- install venv (User does it)
- python3 -m venv env
- cd django_test
- python3 -m pip install -r requirements.txt
- cd projectshop

1) python manage.py migrate
2) python manage.py makefixtures    #or checkfile to manages/fixtures/readme.md
3) python3 manage.py runfixtures
4) celery -A projectshop worker -B     #new window to terminal (OPTIONAL FIELD)
5) python manage.py runserver 
~~~~

**Run fixtures (check tutorial projectshop/manages/fixtures)**
<hr>

~~~~
         USERS
_________________________
login       |   password    
_________________________
Assistant    |     123
_________________________
Accountant   |     123
_________________________
Cashier      |     123
_________________________
admin        |     123
_________________________
~~~~

# TESTING
~~~~
python3 manage.py test manages

coverage run manage.py test 

coverage report 
~~~~

# PYLINT

~~~~
pylint --load-plugins pylint_django "PATH TO RUN"
~~~~


# CELERY RUN
~~~~
celery -A projectshop worker -B

celery -A projectshop  worker --loglevel=INFO
~~~~


