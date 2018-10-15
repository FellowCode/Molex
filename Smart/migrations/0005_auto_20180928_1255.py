# Generated by Django 2.1 on 2018-09-28 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smart', '0004_auto_20180901_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='operating_system',
            field=models.CharField(choices=[('Android', 'Android'), ('Windows 10', 'Windows 10'), ('iOS', 'iOS'), ('Windows 10 и Android', 'Windows 10 и Android')], default='Android', max_length=40),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='resolution',
            field=models.CharField(choices=[('1920x1080', '1920x1080'), ('2160х1080', '2160х1080'), ('1280x720', '1280x720'), ('1440x720', '1440x720'), ('1024x600', '1024x600'), ('1920x1200', '1920x1200'), ('1920x1280', '1920x1280'), ('1280x800', '1280x800')], default='2160х1080', max_length=12),
        ),
    ]
