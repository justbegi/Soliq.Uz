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
