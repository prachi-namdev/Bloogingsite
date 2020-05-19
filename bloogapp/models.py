from django.db import models
from datetime import datetime

# Create your models here.
class blog(models.Model):
    username=models.CharField(max_length=60)
    password=models.CharField(max_length=10)
    emailaddress=models.CharField(max_length=20)
    firstname=models.CharField(max_length=60)
    lastname=models.CharField(max_length=60)


class POSTBLOG(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.FileField(upload_to='images/')
    author=models.CharField(max_length=50,default="")
    upload_date=models.DateTimeField(auto_now_add=True)
