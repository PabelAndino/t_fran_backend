# Generated by Django 3.2.9 on 2022-03-23 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curacion', '0008_auto_20220323_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlbultos',
            name='pilon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curacion.pilon'),
        ),
    ]
