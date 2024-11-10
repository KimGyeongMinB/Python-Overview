from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True ,validators=[]) # validators=[] 공백 허용
    nickname = models.CharField(max_length=10, unique=True) # nickname
    roles = models.CharField(max_length=50, default='USER') # roles

    def __str__(self):
        return self.username