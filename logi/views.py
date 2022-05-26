from http.client import HTTPResponse
from multiprocessing import managers
from urllib import request
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .serializers import FishSerializer, TankSerializer , UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Tank , UserFiles , Fish

# Create your views here.
def login(request):
    return HttpResponse("homepage")

class TankInfo(APIView):

    def get(self,request,tokenID):
        tankI = Tank.objects.filter(tankLoc = tokenID)
        serialize = TankSerializer(tankI , many = True)
        return Response(serialize.data)
    
    def post(self):
        pass

class FishInfo(APIView):

    def get(self,request):
        selected_fish = Fish.objects.filter(name = "sardine")
        serialize = FishSerializer(selected_fish , many = True)
        return Response(serialize.data)
    
    def post(self):
        pass