from django.shortcuts import render
from .serializers import CardSRL, AddmoneySRL
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import CardUser


# Create your views here.

class Add_Card(APIView):
    queryset = CardUser.objects.all()
    serializer_class = CardSRL
    @swagger_auto_schema(request_body=CardSRL)
    def post(self, request):
        serializer = CardSRL(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"MSG": "Card Created"})
        else:
            return Response(serializer.errors)


class AddMoneyView(APIView):

    def post(self, request):
        card_number = request.data.get("card_number")
        money = request.data.get("money")
        filtr_card = CardUser.objects.all().filter(card_number=card_number)
        print(filtr_card)
        for i in filtr_card:
            user_puli = i.money
        hamma_pul = user_puli + money
        updater = CardUser.objects.all().filter(card_number=card_number).update(money=hamma_pul)
        return Response({"message": "ok"})

davlat_korxonalari = [
    "Tatu",
    "Qushbegi hotel",
    "Mars IT ",
    "Akfa",
    "Korzika",
    "Rivera",
    "Chanel",
    "Makro",
    "Mobiuz",
    "Uzbektelecom",
    "Uzmobile",
    "Ucell",
    "Beeline",
    "Perfectum Mobile",
    "Uzonline",
    "Uzinfocom",
    "Uzpakhtasanoat",
    "Uzdonmahsulot",
    "Uzdoninvest",
    "Mars IT",
    "Uzavtosanoat",
    "Akfa Medline",
    "Tatu",
    "Uztransgaz",
    "Uztrans",
    "Havo Yollari",
    "Oftob medline",
    "Kapitalbank",
    "GM",
    "BYD",
    "KIA",
    "Sanata",
    "Chery",
 ]


from CheckApp.models import CheckModel
from CheckApp.serializers import CheckSerializer,CreateCheckSRL
import random

class CheckView(APIView):
    @swagger_auto_schema(request_body=CreateCheckSRL)
    def post(self,request):
        user = request.data.get('user')
        money = request.data.get('money')
        user_money = CardUser.objects.all().filter(card_holder=int(user))
        for i in user_money:
            if i.money >= money:
                qolgan_pul = i.money - money
                update = CardUser.objects.all().filter(card_holder = user).update(money=qolgan_pul)
                seriya_raqam = random.randint(10000,99999)
                fiksal_raqam = ''
                for i in range(14):
                    fiksal_raqam += str(random.randint(1,9))
                fiksal_belgi= ""
                for i in range(6):
                    fiksal_belgi += str(random.randint(1,9))
                check_raqam = ""
                for i in range(10):
                    check_raqam += str(random.randint(1,9))

                return Response({"MSG":"ok"})

            else:
                return Response({"MSG":"else"})
            
                
        
    


        


        