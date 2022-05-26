from pyexpat import model
from rest_framework import serializers
from .models import UserFiles , Tank , Fish


class TankSerializer(serializers.ModelSerializer):
    class Meta():
        model = Tank
        fields='__all__'

class FishSerializer(serializers.ModelSerializer):
    class Meta():
        model = Fish
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserFiles
        fields = '__all__'
