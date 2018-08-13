# Generated by Django 2.1 on 2018-08-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompPeripherals', '0002_auto_20180812_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mouse',
            name='connection_type',
        ),
        migrations.AddField(
            model_name='headphone',
            name='microphone',
            field=models.CharField(choices=[('есть', 'есть'), ('нет', 'нет')], default='есть', max_length=10),
        ),
        migrations.AddField(
            model_name='keyboard',
            name='illumination',
            field=models.CharField(choices=[('Нет', 'Нет'), ('RGB', 'RGB'), ('Монотонная', 'Монотонная')], default='RGB', max_length=20),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='connection_type',
            field=models.CharField(choices=[('USB', 'USB'), ('Jack 3.5', 'Jack 3.5'), ('Bluetooth', 'Bluetooth'), ('2.4 Ghz', '2.4 Ghz')], default='Jack 3.5', max_length=30),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='earbubs_type',
            field=models.CharField(choices=[('Вставные(вакуумные)', 'Вставные(вакуумные)'), ('Охватывающие', 'Охватывающие')], default='Охватывающие', max_length=50),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='interface',
            field=models.CharField(choices=[('USB', 'USB'), ('PS/2', 'PS/2'), ('Bluetooth', 'Bluetooth'), ('2.4Ghz', '2.4Ghz')], default='USB', max_length=5),
        ),
    ]
