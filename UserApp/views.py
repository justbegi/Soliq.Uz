from django.shortcuts import render
from .serializers import  UserSerializer,Login_SRL
from .models import User
from rest_framework.response import  Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

class RegistrationView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return  Response(serializer.errors)


class Login(APIView):
# Create your views here.
    queryset = User.objects.all()
    serializer_class = Login_SRL
    @swagger_auto_schema(request_body=Login_SRL)
    def post(self,request):
        name=request.data.get('name')
        password=request.data.get('password')
        user = User.objects.all().filter(name=name,password=password)
        return Response({"MSG":"SUCCSESS"})




