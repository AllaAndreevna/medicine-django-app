
  # Medicine django app
This is a simple app for controlling a treatment.\
Stack: Python/Django/PostgreSQL

## How to run it?
1) Clone this repo on your local machine and open it in any code redactor (f.e. Visual Studio Code)
2) Download PostgreSQL and create your local database with parametres:
   
name: postgres\
user: postgres\
password: 12345678\
host: localhost\
port: 5432

3) create virtual venv ```python -m venv myenv```
4) open your venv ```myenv/Scripts/activate```
5) ```pip install django``` ```pip install psycopg2``` 
6) ```mkdir medicine-app```
7) ```python manage.py migrate``` after installing all required libraries\
8) ```py manage.py runserver``` - to run a server

## How to interact with the database:
```python manage.py shell``` open python shell\
```from django.db import connection```\
Then run your SQL request in a following structure:
~~~
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM medicine_patient")  
    rows = cursor.fetchall()
    for row in rows:
        print(row)
~~~

For example, 
~~~
with connection.cursor() as cursor:
    cursor.execute("""SELECT
  m.Name AS MedicineName
FROM medicine_medicine AS m
JOIN medicine_prescription AS p
  ON m.ID = p.medicine_id
JOIN medicine_order AS o
  ON p.ID = o.prescription_id
JOIN medicine_patient AS pt
  ON p.patient_id = pt.ID
WHERE
  pt.ID = (
    SELECT
      patient_id
    FROM medicine_order
    WHERE
      patient_id = 1
    ORDER BY
      ID DESC
    LIMIT 1
  )
ORDER BY
  o.ID DESC
LIMIT 5;""")  # Замените на вашу таблицу
    rows = cursor.fetchall()
    for row in rows:
        print(row)
~~~



NOTE! that in this database there are tables 
~~~
('medicine_medicine',)
('medicine_analogs',)
('medicine_doctor',)
('medicine_prescription',)
('medicine_patient',)
('medicine_order',)
('medicine_pharmacy',)
~~~
not just "Medicine" or "Patient". 
