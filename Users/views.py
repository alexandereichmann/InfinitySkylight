from rest_framework import viewsets
from .models import User
from .serializer import userSerializer


# Create your views here.

class Userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer
