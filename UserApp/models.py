from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    pasport_seriya = models.CharField(max_length=2)
    pasport_number = models.CharField(max_length=7)

    def __str__(self):
        return self.name + " " + self.surname
