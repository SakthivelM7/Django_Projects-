# Generated by Django 4.2.6 on 2023-11-22 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0002_customer_theater_showtime_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]
