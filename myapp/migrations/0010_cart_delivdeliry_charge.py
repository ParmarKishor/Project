# Generated by Django 4.1.4 on 2023-01-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='delivdeliry_charge',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
