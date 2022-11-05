from django.db import models

from core.models import User

# Create your models here.


class Character(models.Model):
    (user := models.ForeignKey(User, on_delete=models.CASCADE))
    (name := models.CharField(unique=True, null=False, max_length=20))

    def __str__(self) -> str:
        return self.name
