from rest_framework import viewsets
from .models import *
from .serializer import *


# Create your views here.

class LastOperatingvaluesviewset(viewsets.ModelViewSet):
    queryset = LastOperatingvalues.objects.all()
    serializer_class = lastOperatingvaluesSerializer


class Gt11viewset(viewsets.ModelViewSet):
    queryset = GT11.objects.all()
    serializer_class = gt11Serializer


class Gt12viewset(viewsets.ModelViewSet):
    queryset = GT12.objects.all()
    serializer_class = gt12Serializer


class St10viewset(viewsets.ModelViewSet):
    queryset = ST10.objects.all()
    serializer_class = st10Serializer


class Rw1viewset(viewsets.ModelViewSet):
    queryset = RW1.objects.all()
    serializer_class = rw1Serializer


class Dw1viewset(viewsets.ModelViewSet):
    queryset = DW1.objects.all()
    serializer_class = dw1Serializer


class Vacuum1viewset(viewsets.ModelViewSet):
    queryset = Vacuum1.objects.all()
    serializer_class = vacuum1Serializer


class TrancT1viewset(viewsets.ModelViewSet):
    queryset = TrancT1.objects.all()
    serializer_class = trancT1Serializer


class GasP1viewset(viewsets.ModelViewSet):
    queryset = GasP1.objects.all()
    serializer_class = gasP1Serializer


class Gt21viewset(viewsets.ModelViewSet):
    queryset = GT21.objects.all()
    serializer_class = gt21Serializer


class Gt22viewset(viewsets.ModelViewSet):
    queryset = GT22.objects.all()
    serializer_class = gt22Serializer


class St20viewset(viewsets.ModelViewSet):
    queryset = ST20.objects.all()
    serializer_class = st20Serializer


class Rw2viewset(viewsets.ModelViewSet):
    queryset = RW2.objects.all()
    serializer_class = rw2Serializer


class Dw2viewset(viewsets.ModelViewSet):
    queryset = DW2.objects.all()
    serializer_class = dw2Serializer


class Vacuum2viewset(viewsets.ModelViewSet):
    queryset = Vacuum2.objects.all()
    serializer_class = vacuum2Serializer


class TrancT2viewset(viewsets.ModelViewSet):
    queryset = TrancT2.objects.all()
    serializer_class = trancT2Serializer


class GasP2viewset(viewsets.ModelViewSet):
    queryset = GasP2.objects.all()
    serializer_class = gasP2Serializer
