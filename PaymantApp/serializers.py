from rest_framework.serializers import ModelSerializer
from .models import CardUser


class CardSRL(ModelSerializer):
    class Meta:
        model = CardUser
        fields = '__all__'


class AddmoneySRL(ModelSerializer):
    class Meta:
        model = CardUser
        fields = ('card_number','money')


