# Generated by Django 4.2.5 on 2023-10-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.CharField(max_length=255),
        ),
    ]
