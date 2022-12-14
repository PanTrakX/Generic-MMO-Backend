# Generated by Django 4.1.2 on 2022-11-01 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameserverinstance',
            name='current_players',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gameserverinstance',
            name='last_time_pinged',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='gameserverinstance',
            name='max_players',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
