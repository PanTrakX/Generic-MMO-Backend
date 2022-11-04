# Generated by Django 4.1.3 on 2022-11-04 16:41

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matchmaking', '0003_gameserverinstance_server_auth_token'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gameserverinstance',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='gameserverinstance',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='gameserverinstance',
            name='id',
        ),
        migrations.AddField(
            model_name='gameserverinstance',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
