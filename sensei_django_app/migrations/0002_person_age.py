# Generated by Django 2.2.24 on 2021-09-27 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensei_django_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
