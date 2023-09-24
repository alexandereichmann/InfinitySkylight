from django.db import models


# Create your models here.


class LastChemicalvalue(models.Model):
    HPD11 = models.CharField(max_length=5)
    IPD11 = models.CharField(max_length=5)
    LPD11 = models.CharField(max_length=5)
    HPMS11 = models.CharField(max_length=5)
    IPMS11 = models.CharField(max_length=5)
    LPMS11 = models.CharField(max_length=5)
    HPD12 = models.CharField(max_length=5)
    IPD12 = models.CharField(max_length=5)
    LPD12 = models.CharField(max_length=5)
    HPMS12 = models.CharField(max_length=5)
    IPMS12 = models.CharField(max_length=5)
    LPMS12 = models.CharField(max_length=5)
    HPD21 = models.CharField(max_length=5)
    IPD21 = models.CharField(max_length=5)
    LPD21 = models.CharField(max_length=5)
    HPMS21 = models.CharField(max_length=5)
    IPMS21 = models.CharField(max_length=5)
    LPMS21 = models.CharField(max_length=5)
    HPD22 = models.CharField(max_length=5)
    IPD22 = models.CharField(max_length=5)
    LPD22 = models.CharField(max_length=5)
    HPMS22 = models.CharField(max_length=5)
    IPMS22 = models.CharField(max_length=5)
    LPMS22 = models.CharField(max_length=5)


class HPD11(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class IPD11(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class LPD11(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class HPMS11(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class IPMS11(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class LPMS11(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)

class HPD12(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class IPD12(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class LPD12(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class HPMS12(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class IPMS12(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class LPMS12(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class HPD21(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class IPD21(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class LPD21(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class HPMS21(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class IPMS21(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class LPMS21(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)
class HPD22(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class IPD22(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class LPD22(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class HPMS22(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class IPMS22(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)


class LPMS22(models.Model):
    date = models.CharField(max_length=255, default="")
    value = models.IntegerField(default=0)
    employee = models.CharField(max_length=255)
