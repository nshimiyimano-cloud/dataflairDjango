from django.db import models

class Student(models.Model):
    roll_no=models.TextField()
    name=models.TextField(max_length=40)
    stud_class=models.TextField()
    department=models.TextField(
        #python manage.py makemigrations
        #python manage.py migrate after we will need to run this and makesure u have connected database
    )
