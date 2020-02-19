
# RUN PROJECT
~~~~
python3 manage.py migrate

python3 manage.py runserver
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
Accountant   |    123
_________________________
Cashier      |    123
_________________________
admin        |     123
_________________________
~~~~

# TESTING
~~~~
python3 manage.py test manages

coverage run --source='.' manage.py test

coverage run --source='.' --omit='*migrations*' manage.py test 

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


#How to run tutorial
~~~~
- git clone {rep}
- cd django_test
- python3 pip3 install -r requirements.txt
- cd projectshop

1) Python manage.py migrate
2) python manage.py makefixtures    #or checkfile to manages/fixtures/readme.md
3) python manage.py loaddata "name fixtures'
4) celery -A projectshop worker -B     #new window to terminal (OPTIONAL FIELD)
5) python manage.py runserver 
~~~~