# Generated by Django 3.2.4 on 2021-06-22 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='middleName',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='slug',
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]