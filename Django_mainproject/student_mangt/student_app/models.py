from django.db import models

# Create your models here.
class students(models.Model):
    stud_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_no=models.CharField()
    department=models.CharField()
