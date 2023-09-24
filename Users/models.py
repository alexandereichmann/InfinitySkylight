from django.db import models


# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=255)
    jop = models.CharField(max_length=255)
    Pass=models.CharField(max_length=25)
    def __str__(self):
        return self.Name
