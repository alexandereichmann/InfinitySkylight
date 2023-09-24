from rest_framework import serializers
from .models import *


class lastOperatingvaluesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastOperatingvalues
        fields = '__all__'


class gt11Serializer(serializers.ModelSerializer):
    class Meta:
        model = GT11
        fields = '__all__'


class gt12Serializer(serializers.ModelSerializer):
    class Meta:
        model = GT12
        fields = '__all__'


class st10Serializer(serializers.ModelSerializer):
    class Meta:
        model = ST10
        fields = '__all__'


class rw1Serializer(serializers.ModelSerializer):
    class Meta:
        model = RW1
        fields = '__all__'


class dw1Serializer(serializers.ModelSerializer):
    class Meta:
        model = DW1
        fields = '__all__'


class vacuum1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuum1
        fields = '__all__'


class trancT1Serializer(serializers.ModelSerializer):
    class Meta:
        model = TrancT1
        fields = '__all__'


class gasP1Serializer(serializers.ModelSerializer):
    class Meta:
        model = GasP1
        fields = '__all__'


class gt21Serializer(serializers.ModelSerializer):
    class Meta:
        model = GT21
        fields = '__all__'


class gt22Serializer(serializers.ModelSerializer):
    class Meta:
        model = GT22
        fields = '__all__'


class st20Serializer(serializers.ModelSerializer):
    class Meta:
        model = ST20
        fields = '__all__'


class rw2Serializer(serializers.ModelSerializer):
    class Meta:
        model = RW2
        fields = '__all__'


class dw2Serializer(serializers.ModelSerializer):
    class Meta:
        model = DW2
        fields = '__all__'


class vacuum2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuum2
        fields = '__all__'


class trancT2Serializer(serializers.ModelSerializer):
    class Meta:
        model = TrancT2
        fields = '__all__'


class gasP2Serializer(serializers.ModelSerializer):
    class Meta:
        model = GasP2
        fields = '__all__'
