from rest_framework.serializers import ModelSerializer
from .models import CheckModel
class CheckSerializer(ModelSerializer):
    class Meta:
        model = CheckModel
        fields = '__all__'