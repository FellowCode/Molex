# Generated by Django 2.1 on 2018-08-17 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompPeripherals', '0002_remove_keyboard_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyboard',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True),
        ),
    ]
