from rest_framework import viewsets
from .models import *
from .serializer import *

# Create your views here.
class LastChemicalvaluesviewset(viewsets.ModelViewSet):
    queryset = LastChemicalvalue.objects.all()
    serializer_class = lastChemicalvaluesSerializer


class HPD11viewset(viewsets.ModelViewSet):
    queryset = HPD11.objects.all()
    serializer_class = hPD11Serializer


class IPD11viewset(viewsets.ModelViewSet):
    queryset = IPD11.objects.all()
    serializer_class = iPD11Serializer


class LPD11viewset(viewsets.ModelViewSet):
    queryset = LPD11.objects.all()
    serializer_class = lPD11Serializer


class HPMS11viewset(viewsets.ModelViewSet):
    queryset = HPMS11.objects.all()
    serializer_class = hPMS11Serializer


class IPMS11viewset(viewsets.ModelViewSet):
    queryset = IPMS11.objects.all()
    serializer_class = iPMS11Serializer


class LPMS11viewset(viewsets.ModelViewSet):
    queryset = LPMS11.objects.all()
    serializer_class = lPMS11Serializer


class HPD12viewset(viewsets.ModelViewSet):
    queryset = HPD12.objects.all()
    serializer_class = hPD12Serializer


class IPD12viewset(viewsets.ModelViewSet):
    queryset = IPD12.objects.all()
    serializer_class = iPD12Serializer


class LPD12viewset(viewsets.ModelViewSet):
    queryset = LPD12.objects.all()
    serializer_class = lPD12Serializer


class HPMS12viewset(viewsets.ModelViewSet):
    queryset = HPMS12.objects.all()
    serializer_class = hPMS12Serializer


class IPMS12viewset(viewsets.ModelViewSet):
    queryset = IPMS12.objects.all()
    serializer_class = iPMS12Serializer


class LPMS12viewset(viewsets.ModelViewSet):
    queryset = LPMS12.objects.all()
    serializer_class = lPMS12Serializer

class HPD21viewset(viewsets.ModelViewSet):
    queryset = HPD21.objects.all()
    serializer_class = hPD21Serializer


class IPD21viewset(viewsets.ModelViewSet):
    queryset = IPD21.objects.all()
    serializer_class = iPD21Serializer


class LPD21viewset(viewsets.ModelViewSet):
    queryset = LPD21.objects.all()
    serializer_class = lPD21Serializer


class HPMS21viewset(viewsets.ModelViewSet):
    queryset = HPMS21.objects.all()
    serializer_class = hPMS21Serializer


class IPMS21viewset(viewsets.ModelViewSet):
    queryset = IPMS21.objects.all()
    serializer_class = iPMS21Serializer


class LPMS21viewset(viewsets.ModelViewSet):
    queryset = LPMS21.objects.all()
    serializer_class = lPMS21Serializer


class HPD22viewset(viewsets.ModelViewSet):
    queryset = HPD22.objects.all()
    serializer_class = hPD22Serializer


class IPD22viewset(viewsets.ModelViewSet):
    queryset = IPD22.objects.all()
    serializer_class = iPD22Serializer


class LPD22viewset(viewsets.ModelViewSet):
    queryset = LPD22.objects.all()
    serializer_class = lPD22Serializer


class HPMS22viewset(viewsets.ModelViewSet):
    queryset = HPMS22.objects.all()
    serializer_class = hPMS22Serializer


class IPMS22viewset(viewsets.ModelViewSet):
    queryset = IPMS22.objects.all()
    serializer_class = iPMS22Serializer


class LPMS22viewset(viewsets.ModelViewSet):
    queryset = LPMS22.objects.all()
    serializer_class = lPMS22Serializer

