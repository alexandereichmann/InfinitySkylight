from rest_framework import viewsets
from .models import *
from .serializer import *

# Create your views here.

class ICviewset(viewsets.ModelViewSet):
    queryset = IC.objects.all()
    serializer_class = iCSerializer

class Elecviewset(viewsets.ModelViewSet):
    queryset = Elec.objects.all()
    serializer_class = elecSerializer

class Mechviewset(viewsets.ModelViewSet):
    queryset = Mech.objects.all()
    serializer_class = mechSerializer

