# Generated by Django 2.1 on 2018-08-16 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Intel', 'Intel'), ('AMD', 'AMD')], default='Intel', max_length=8)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('coreCount', models.IntegerField()),
                ('threadsCount', models.IntegerField()),
                ('frequency', models.DecimalField(decimal_places=2, max_digits=3)),
                ('RAM_type', models.CharField(choices=[('DDR2', 'DDR2'), ('DDR3', 'DDR3'), ('DDR4', 'DDR4')], default='DDR3', max_length=10)),
            ],
            options={
                'verbose_name': 'CPU',
                'verbose_name_plural': 'CPU',
            },
        ),
        migrations.CreateModel(
            name='CPUProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Products.Product')),
                ('cpu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Parts.CPU')),
            ],
            options={
                'verbose_name': '> CPU',
                'verbose_name_plural': '> CPU',
            },
            bases=('Products.product',),
        ),
        migrations.CreateModel(
            name='CPUSocket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
            options={
                'verbose_name': 'CPU Socket',
            },
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'GPU',
                'verbose_name_plural': 'GPU',
            },
        ),
        migrations.CreateModel(
            name='GraphicCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GPU_ruler', models.CharField(choices=[('GeForce', 'GeForce'), ('Radeon', 'Radeon')], default='GeForce', max_length=8)),
                ('RAM', models.IntegerField()),
                ('RAM_type', models.CharField(choices=[('GDDR3', 'GDDR3'), ('GDDR4', 'GDDR4'), ('GDDR5', 'GDDR5')], default='GDDR5', max_length=8)),
                ('watts', models.IntegerField()),
                ('GPU', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Parts.GPU')),
            ],
        ),
        migrations.CreateModel(
            name='GraphicCardBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GraphicCardProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Products.Product')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Parts.GraphicCardBrand')),
                ('graphic_card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Parts.GraphicCard')),
            ],
            options={
                'verbose_name': '> Graphiccard',
            },
            bases=('Products.product',),
        ),
        migrations.CreateModel(
            name='InterfaceName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Products.Product')),
                ('name', models.CharField(max_length=50)),
                ('formFactor', models.CharField(choices=[('MATX', 'MATX'), ('ATX', 'ATX')], default='MATX', max_length=5)),
                ('RAM_slot_count', models.CharField(choices=[('2', '2'), ('4', '4')], default='2', max_length=2)),
                ('RAM_type', models.CharField(choices=[('DDR2', 'DDR2'), ('DDR3', 'DDR3'), ('DDR4', 'DDR4')], default='DDR3', max_length=8)),
            ],
            options={
                'verbose_name': '> Motherboard',
            },
            bases=('Products.product',),
        ),
        migrations.CreateModel(
            name='MotherboardBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MotherboardChipset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MotherboardInterface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('Motherboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interfaces', to='Parts.Motherboard')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='Parts.InterfaceName')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Products.Product')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(choices=[('DIMM', 'DIMM'), ('SO-DIMM', 'SO-DIMM')], default='DIMM', max_length=8)),
                ('RAM_type', models.CharField(choices=[('DDR2', 'DDR2'), ('DDR3', 'DDR3'), ('DDR4', 'DDR4')], default='DDR3', max_length=8)),
                ('RAM_amount', models.IntegerField()),
                ('frequency', models.IntegerField()),
            ],
            options={
                'verbose_name': '> RAM',
                'verbose_name_plural': '> RAM',
            },
            bases=('Products.product',),
        ),
        migrations.CreateModel(
            name='RAMBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SSD',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Products.Product')),
                ('name', models.CharField(max_length=50)),
                ('memory_type', models.CharField(choices=[('SLC', 'SLC'), ('MLC', 'MLC'), ('TLC', 'TLC')], default='TLC', max_length=5)),
                ('memory_amount', models.IntegerField()),
                ('read_speed', models.IntegerField()),
                ('write_speed', models.IntegerField()),
            ],
            options={
                'verbose_name': '> SSD',
                'verbose_name_plural': '> SSD',
            },
            bases=('Products.product',),
        ),
        migrations.CreateModel(
            name='SSDBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'SSD Brand',
            },
        ),
        migrations.AddField(
            model_name='ssd',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Parts.SSDBrand'),
        ),
        migrations.AddField(
            model_name='ram',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Parts.RAMBrand'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Parts.MotherboardBrand'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='chipset',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='Parts.MotherboardChipset'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='socket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Parts.CPUSocket'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='socket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Parts.CPUSocket'),
        ),
    ]
