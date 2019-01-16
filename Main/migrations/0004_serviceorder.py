# Generated by Django 2.1.4 on 2019-01-16 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20180820_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=11)),
                ('note', models.TextField()),
            ],
        ),
    ]
