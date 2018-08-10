# Generated by Django 2.1 on 2018-08-10 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=50)),
                ('person_phone', models.CharField(max_length=12)),
                ('person_pay', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('isPaid', models.BooleanField()),
                ('isCompleted', models.BooleanField()),
                ('order', models.TextField()),
                ('person', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
