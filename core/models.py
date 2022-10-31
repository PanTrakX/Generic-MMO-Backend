from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Character(models.Model):

    (user := models.ForeignKey(User, on_delete=models.CASCADE))
    (name := models.CharField(unique=True, null=False, max_length=20))

    def __str__(self) -> str:
        return self.name
