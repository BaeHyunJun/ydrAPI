from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import testRestAPI, Data, Calc
from .serializers import TestSerializer, DataSerializer, CalcSerializer

class TestListAPI(APIView):
    def get(self, request):
        queryset = testRestAPI.objects.all()
        print(queryset)
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data)


class DataListAPI(APIView):
    def get(self, request):
        queryset = Data.objects.all()
        print(queryset)
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def HelloAPI(request):
    return Response("Hello API!")

@api_view(['GET'])
def randomAPI(request, id):
    totalCalcs = Calc.objects.all()
    randomCalcs = random.sample(list(totalCalcs), id)
    serializer = CalcSerializer(randomCalcs, many=True)
    return Response(serializer.data)