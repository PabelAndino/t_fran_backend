# Generated by Django 3.2.9 on 2022-02-10 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curacion', '0002_controlbultos_controlbultosdetalle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pilon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
            ],
        ),
    ]
