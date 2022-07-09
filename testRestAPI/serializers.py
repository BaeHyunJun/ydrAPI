from rest_framework import serializers
from .models import testRestAPI, Data, Calc

class TestSerializer(serializers.ModelSerializer):
    class Meta :
        model = testRestAPI
        fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
    class Meta :
        model = Data
        fields = '__all__'

class CalcSerializer(serializers.ModelSerializer):
    class Meta :
        model = Calc
        fields = ('title', 'body', 'rate', 'count')