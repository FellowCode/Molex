# Generated by Django 2.1 on 2018-08-12 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_auto_20180812_2117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'categories'},
        ),
    ]