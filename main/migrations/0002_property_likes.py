# Generated by Django 4.1.6 on 2024-05-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
