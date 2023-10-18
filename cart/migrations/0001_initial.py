# Generated by Django 4.2.5 on 2023-10-18 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('subprice', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('quantity', models.IntegerField(default=1, max_length=2)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]