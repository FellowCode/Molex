# Generated by Django 2.1 on 2018-08-13 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_auto_20180813_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='link',
        ),
    ]
