from django.db import models

# Create your models here.


class GameServerInstance(models.Model):

    (ip := models.GenericIPAddressField())
    (port := models.PositiveIntegerField())
