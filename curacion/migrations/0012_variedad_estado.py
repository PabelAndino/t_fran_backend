# Generated by Django 3.2.9 on 2022-05-26 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curacion', '0011_auto_20220525_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='variedad',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]