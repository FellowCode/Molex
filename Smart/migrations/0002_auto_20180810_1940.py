# Generated by Django 2.1 on 2018-08-10 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Smart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smartphone',
            old_name='Net',
            new_name='net',
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='CPU',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Smart.CPUSmartphone'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Smart.BrandSmartphone'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='product_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Products.Product'),
        ),
    ]
