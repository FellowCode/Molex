# Generated by Django 2.1 on 2018-08-14 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Computers', '0003_auto_20180814_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopGPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('ram_amount', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='graphic_ram_amount',
        ),
        migrations.AlterField(
            model_name='laptop',
            name='discreteGraphic',
            field=models.CharField(choices=[('есть', 'есть'), ('нет', 'нет')], default='нет', max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='gpu',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='Computers.LaptopGPU'),
        ),
    ]
