from pyexpat import model
from rest_framework import serializers
from .models import UserFiles , Tank , Fish


class TankSerializer(serializers.ModelSerializer):
    class Meta():
        model = Tank
        fields='__all__'


