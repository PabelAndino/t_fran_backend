# Generated by Django 3.2.9 on 2022-03-23 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curacion', '0009_alter_controlbultos_pilon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finca',
            name='descripcion',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]