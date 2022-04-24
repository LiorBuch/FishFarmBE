from http.client import HTTPResponse
from multiprocessing import managers
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .serializers import TankSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Tank , UserFiles

# Create your views here.
def login(request):
    return HttpResponse("homepage")

class TankInfo(APIView):

    def get(self,request):
        tankI = Tank.objects.filter(tank_name = "uTest1")
        serlize = TankSerializer(tankI , many = True)
        return Response(serlize.data)
    
    def post(self):
        pass