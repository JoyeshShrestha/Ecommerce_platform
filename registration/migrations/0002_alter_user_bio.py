# Generated by Django 4.2.5 on 2023-10-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(default='', max_length=255),
        ),
    ]
