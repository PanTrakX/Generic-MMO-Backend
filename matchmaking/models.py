from django.db import models

from datetime import datetime
# Create your models here.


class GameServerInstance(models.Model):

    (ip := models.GenericIPAddressField())
    (port := models.PositiveIntegerField())
    (current_players := models.PositiveIntegerField(default=0))
    (max_players := models.PositiveIntegerField(default=0))
    (last_time_pinged := models.DateTimeField(default=datetime.now))
