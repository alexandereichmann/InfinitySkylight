from django.db import models


# Create your models here.


class LastOperatingvalues(models.Model):
    Gt11 = models.CharField(max_length=5)
    Gt12 = models.CharField(max_length=5)
    ST10 = models.CharField(max_length=5)
    RW1 = models.CharField(max_length=5)
    DW1 = models.CharField(max_length=5)
    Vacuum1 = models.CharField(max_length=5)
    TrancT1 = models.CharField(max_length=5)
    GasP1 = models.CharField(max_length=5)
    Gt21 = models.CharField(max_length=5)
    Gt22 = models.CharField(max_length=5)
    ST20 = models.CharField(max_length=5)
    RW2 = models.CharField(max_length=5)
    DW2 = models.CharField(max_length=5)
    Vacuum2 = models.CharField(max_length=5)
    TrancT2 = models.CharField(max_length=5)
    GasP2 = models.CharField(max_length=5)


class GT11(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class GT12(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class ST10(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class RW1(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class DW1(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class Vacuum1(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class TrancT1(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class GasP1(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class GT21(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class GT22(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class ST20(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class RW2(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class DW2(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class Vacuum2(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class TrancT2(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class GasP2(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)
