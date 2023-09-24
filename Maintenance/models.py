from django.db import models


# Create your models here.


class IC(models.Model):

    StartDate = models.DateTimeField()
    Place = models.CharField(max_length=255)
    Data = models.TextField()
    Note = models.TextField()
    Status = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    EndDate = models.DateTimeField(null=True)


class Elec(models.Model):

    StartDate = models.DateTimeField()
    Place = models.CharField(max_length=255)
    Data = models.TextField()
    Note = models.TextField()
    Status = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    EndDate = models.DateTimeField(null=True)


class Mech(models.Model):

    StartDate = models.DateTimeField()
    Place = models.CharField(max_length=255)
    Data = models.TextField()
    Note = models.TextField()
    Status = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    EndDate = models.DateTimeField(null=True)


