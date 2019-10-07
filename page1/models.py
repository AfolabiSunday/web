from django.db import models

# Create your models here.

class new_user(models.Model):

    username = models.CharField(max_length= 100, default=False)
    firstname = models.CharField(max_length=50, default=False)
    lastname = models.CharField(max_length=50, default=False)
    email = models.EmailField(max_length=244, default=False)
    img = models.ImageField(max_length=1000, default=False)
    password = models.CharField(max_length=50, default=False)
    
    def __str__(self):
        return self.username


#there is a bug of environment veriable here that needs to be fixed