from unicodedata import name
from django.db import models

# Create your models here.

class Fish(models.Model):
    name = models.CharField(max_length=15)
    birth_date = models.DateField()
    age = models.IntegerField(default=1)
    species = models.CharField(max_length=30)

class Tank(models.Model):
    tank_name = models.CharField(max_length=15)
    order = models.IntegerField(default=1)
    size = models.IntegerField(default=10)
    wallpaper = models.CharField(max_length=15)
    gravel = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.tank_name

class UserFiles(models.Model):
    name = models.CharField(max_length=15)
    xp_points = models.IntegerField(default=0)
    number_of_tanks = models.IntegerField(default=1)
    tank_one = models.ForeignKey(Tank , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
