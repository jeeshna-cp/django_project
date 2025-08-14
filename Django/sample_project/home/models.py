from django.db import models # type: ignore

# Create your models here.
class departments(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()


class contacts(models.Model):
    phone_no=models.CharField()
    email=models.EmailField()