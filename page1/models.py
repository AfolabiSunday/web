from django.db import models

# Create your models here.

class new_user(models.Model):

    username = models.CharField(max_length= 100, blank=True)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=244, blank=True)
    img = models.ImageField(max_length=1000, blank=True)
    password = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.username


#there is a bug of environment veriable here that needs to be fixed