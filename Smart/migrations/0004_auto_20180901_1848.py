# Generated by Django 2.1 on 2018-09-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smart', '0003_auto_20180826_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='android',
            field=models.CharField(blank=True, choices=[('5.1', '5.1'), ('6.0', '6.0'), ('7.0', '7.0'), ('7.1', '7.1'), ('8.0', '8.0'), ('8.1', '8.1')], default='8.1', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='operating_system',
            field=models.CharField(choices=[('Android', 'Android'), ('Windows 10', 'Windows 10'), ('iOS', 'iOS')], default='Android', max_length=20),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='resolution',
            field=models.CharField(choices=[('1920x1080', '1920x1080'), ('2160х1080', '2160х1080'), ('1280x720', '1280x720'), ('1440x720', '1440x720'), ('1024x600', '1024x600'), ('1920x1200', '1920x1200'), ('1920x1280', '1920x1280')], default='2160х1080', max_length=12),
        ),
    ]
