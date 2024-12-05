# medicine-django-app
This is a simple app for controlling a treatment.
Stack: Python/Django/PostgreSQL

How to run it?
1) Clone this repo on your local machine and open it in any code redactor (f.e. Visual Studio Code)
2) Download PostgreSQL and create your local database with parametres:
name: postgres
user: postgres
password: 12345678
host: localhost
port: 5432
3) create virtual venv ''' python -m venv myenv'''
4) open your venv '''myenv/Scripts/activate'''
5) '''pip install django''' '''pip install psycopg2''' 
6) '''mkdir medicine-app'''
7) '''django-admin startproject mysite medicine-app '''
8) '''py manage.py startapp medicine'''



py manage.py runserver - to run a server
python manage.py shell - to open python command line