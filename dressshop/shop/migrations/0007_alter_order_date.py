# Generated by Django 5.0.2 on 2024-02-11 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_star_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 2, 11, 15, 4, 5, 561591)),
        ),
    ]
