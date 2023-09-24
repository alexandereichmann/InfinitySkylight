from rest_framework import serializers
from .models import *


class iCSerializer(serializers.ModelSerializer):
    class Meta:
        model = IC
        fields = '__all__'


class elecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elec
        fields = '__all__'


class mechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mech
        fields = '__all__'

