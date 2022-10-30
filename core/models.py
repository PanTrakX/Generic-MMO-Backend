from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class CharacterClass(models.Model):

    (name := models.CharField(max_length=20))

    def __str__(self) -> str:
        return self.name


class Character(models.Model):

    (user := models.ForeignKey(User, on_delete=models.CASCADE))
    (name := models.CharField(unique=True, null=False, max_length=20))
    (character_class := models.ForeignKey(CharacterClass, on_delete=models.CASCADE))

    def __str__(self) -> str:
        return self.name
