from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class balance(models.Model):
    WUser = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
    def __str__(self):
        return self.WUser.username
