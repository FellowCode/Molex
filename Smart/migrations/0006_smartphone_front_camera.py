# Generated by Django 2.1 on 2018-08-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smart', '0005_remove_smartphone_front_camera'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='front_camera',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=4),
        ),
    ]
