# Generated by Django 4.1.4 on 2023-01-02 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firstlogin',
            field=models.BooleanField(default=False),
        ),
    ]