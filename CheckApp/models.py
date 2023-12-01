from django.db import models
from UserApp.models import User

class CheckModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    seriya_raqam = models.IntegerField(unique=True)
    fiskal_raqam = models.CharField(unique=True,max_length=14)
    fiskal_belgi = models.IntegerField(unique=True)
    check_raqam = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.fiskal_raqam)


# Create your models here.
