from django.db import models

# Create your models here.

class new_user(models.Model):

    username = models.CharField(max_length= 100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length= 200)
    number = models.IntegerField()
    img = models.ImageField(max_length=1000)


    there is a bug of environment veriable here that needs to be fixed