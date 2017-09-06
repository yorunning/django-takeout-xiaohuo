from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    number = models.CharField('电话号码',max_length=11,blank=True)

    class Mete(AbstractUser.Meta):
        pass