import os
from fabric.api import local

def runserver():
    os.environ.setdefault('DEBUG', 'True')
    local('python manage.py runserver 0.0.0.0:8000')

def test():
    os.environ.setdefault('DEBUG', 'True')
    local('python manage.py test')

def shell_plus():
    os.environ.setdefault('DEBUG', 'True')
    local('python manage.py shell_plus')

def makemigrations():
    os.environ.setdefault('DEBUG', 'True')
    local('python manage.py makemigrations')

def migrate():
    os.environ.setdefault('DEBUG', 'True')
    local('python manage.py migrate')
