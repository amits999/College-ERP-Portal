from django.db import models

# Create your models here.
sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class Student(models.Model):
    USN = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')
    DOB = models.DateField(default='1998-01-01')
