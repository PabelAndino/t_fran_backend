# Generated by Django 3.2.9 on 2022-03-14 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curacion', '0004_alter_controlbultos_observacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pilon',
            old_name='numero',
            new_name='nombre',
        ),
        migrations.AddField(
            model_name='pilon',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
