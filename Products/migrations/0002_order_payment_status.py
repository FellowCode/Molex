# Generated by Django 2.1 on 2018-08-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]