# Generated by Django 2.1 on 2018-08-17 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CompPeripherals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyboard',
            name='weight',
        ),
    ]
