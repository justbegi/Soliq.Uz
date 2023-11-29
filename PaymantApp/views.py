from django.shortcuts import render
from .serializers import CardSRL,AddmoneySRL
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import CardUser
# Create your views here.

class Add_Card(APIView):
    quareser = CardUser.objects
    #