# Generated by Django 4.1.3 on 2022-11-04 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_character_character_class_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_server',
            field=models.BooleanField(default=False),
        ),
    ]
