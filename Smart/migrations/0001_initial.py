# Generated by Django 2.1 on 2018-08-05 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandSmartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='CPUSmartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('MediaTek', 'MediaTek'), ('Snapdragon', 'Snapdragon'), ('Other', 'Other')], max_length=15)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='children', serialize=False, to='Products.Product')),
                ('name', models.CharField(max_length=60)),
                ('android', models.CharField(choices=[('6.0', '6.0'), ('7.0', '7.0'), ('7.1', '7.1'), ('8.0', '8.0'), ('8.1', '8.1')], max_length=4)),
                ('camera', models.IntegerField()),
                ('matrix', models.CharField(choices=[('IPS', 'IPS'), ('OLED', 'OLED'), ('TFT', 'TFT')], max_length=6)),
                ('diagonal', models.DecimalField(decimal_places=2, max_digits=4)),
                ('resolution', models.CharField(choices=[('1920x1080', '1920x1080'), ('2160х1080', '2160х1080'), ('1280x720', '1280x720'), ('1440x720', '1440x720')], max_length=12)),
                ('battery', models.IntegerField()),
                ('RAM', models.IntegerField()),
                ('ROM', models.IntegerField()),
                ('SIM_count', models.CharField(choices=[('1 SIM', '1 SIM'), ('2 SIM', '2 SIM')], default='2', max_length=8)),
                ('Net', models.CharField(choices=[('3G', '3G'), ('4G', '4G')], max_length=3)),
                ('CPU', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='children', to='Smart.CPUSmartphone')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='children', to='Smart.BrandSmartphone')),
            ],
            options={
                'default_related_name': 'children',
            },
            bases=('Products.product',),
        ),
    ]
