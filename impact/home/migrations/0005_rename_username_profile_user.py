# Generated by Django 3.2.4 on 2021-06-24 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]
