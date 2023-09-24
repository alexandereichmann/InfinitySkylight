from rest_framework import serializers
from .models import *


class lastChemicalvaluesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastChemicalvalue
        fields = '__all__'


class hPD11Serializer(serializers.ModelSerializer):
    class Meta:
        model = HPD11
        fields = '__all__'


class iPD11Serializer(serializers.ModelSerializer):
    class Meta:
        model = IPD11
        fields = '__all__'


class lPD11Serializer(serializers.ModelSerializer):
    class Meta:
        model = LPD11
        fields = '__all__'


class hPMS11Serializer(serializers.ModelSerializer):
    class Meta:
        model = HPMS11
        fields = '__all__'


class iPMS11Serializer(serializers.ModelSerializer):
    class Meta:
        model = IPMS11
        fields = '__all__'


class lPMS11Serializer(serializers.ModelSerializer):
    class Meta:
        model = LPMS11
        fields = '__all__'


class hPD12Serializer(serializers.ModelSerializer):
    class Meta:
        model = HPD12
        fields = '__all__'


class iPD12Serializer(serializers.ModelSerializer):
    class Meta:
        model = IPD12
        fields = '__all__'


class lPD12Serializer(serializers.ModelSerializer):
    class Meta:
        model = LPD12
        fields = '__all__'


class hPMS12Serializer(serializers.ModelSerializer):
    class Meta:
        model = HPMS12
        fields = '__all__'


class iPMS12Serializer(serializers.ModelSerializer):
    class Meta:
        model = IPMS12
        fields = '__all__'


class lPMS12Serializer(serializers.ModelSerializer):
    class Meta:
        model = LPMS12
        fields = '__all__'


class hPD21Serializer(serializers.ModelSerializer):
    class Meta:
        model = HPD21
        fields = '__all__'


class iPD21Serializer(serializers.ModelSerializer):
    class Meta:
        model = IPD21
        fields = '__all__'


class lPD21Serializer(serializers.ModelSerializer):
    class Meta:
        model = LPD21
        fields = '__all__'


class hPMS21Serializer(serializers.ModelSerializer):
    class Meta:
        model = HPMS21
        fields = '__all__'


class iPMS21Serializer(serializers.ModelSerializer):
    class Meta:
        model = IPMS21
        fields = '__all__'


class lPMS21Serializer(serializers.ModelSerializer):
    class Meta:
        model = LPMS21
        fields = '__all__'


class hPD22Serializer(serializers.ModelSerializer):
    class Meta:
        model = HPD22
        fields = '__all__'


class iPD22Serializer(serializers.ModelSerializer):
    class Meta:
        model = IPD22
        fields = '__all__'


class lPD22Serializer(serializers.ModelSerializer):
    class Meta:
        model = LPD22
        fields = '__all__'


class hPMS22Serializer(serializers.ModelSerializer):
    class Meta:
        model = HPMS22
        fields = '__all__'


class iPMS22Serializer(serializers.ModelSerializer):
    class Meta:
        model = IPMS22
        fields = '__all__'


class lPMS22Serializer(serializers.ModelSerializer):
    class Meta:
        model = LPMS22
        fields = '__all__'
