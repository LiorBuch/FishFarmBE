from tkinter import CASCADE
from unicodedata import name
from uuid import uuid4
from django.db import models

# Create your models here.

class Fish(models.Model):
    name = models.CharField(max_length=15)
    fishLoc = models.CharField(max_length=15 , default="no location")
    imageCountX = models.IntegerField()
    imageCountY = models.IntegerField()
    sclaeWidth = models.FloatField(default=1)
    sclaeHeight = models.FloatField(default=1)
    idnum = models.IntegerField(default=0)
    speed = models.FloatField(default=100)
    xPos = models.FloatField(default=400)
    yPos = models.FloatField(default=400)
    birth_date = models.DateTimeField(auto_now_add= True)
    age = models.IntegerField(default=0)
    species = models.CharField(max_length=30)
    texturePartWidth = models.FloatField(default=0)
    texturePartHeight = models.FloatField(default=0)
    fishPNG = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

class Tank(models.Model):
    tankLoc = models.CharField(max_length=60 , default="no location")
    numberOfDecorations = models.IntegerField(default=0)
    order = models.IntegerField(default=1)
    size = models.IntegerField(default=10)
    numberOfFish = models.IntegerField(default=0)
    wallpaper = models.CharField(max_length=15)
    gravel = models.CharField(max_length=15)

    def __str__(self) -> str:
        return str(self.tankLoc)

class UserFiles(models.Model):
    name = models.CharField(max_length=15)
    tokenID = models.UUIDField(primary_key=True , default=uuid4 , editable=True)
    xp_points = models.IntegerField(default=0)
    number_of_tanks = models.IntegerField(default=1)
    tank_one = models.ForeignKey(Tank , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
