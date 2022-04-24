from urllib import request
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('log/',views.login, name='login'),
    path('reqtank/',views.TankInfo.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)