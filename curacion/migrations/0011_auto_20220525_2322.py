# Generated by Django 3.2.9 on 2022-05-25 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curacion', '0010_alter_finca_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variedad',
            name='estado',
        ),
        migrations.AlterField(
            model_name='variedad',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]