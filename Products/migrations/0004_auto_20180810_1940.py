# Generated by Django 2.1 on 2018-08-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_auto_20180810_1326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['isCompleted']},
        ),
        migrations.AddField(
            model_name='order',
            name='isProcessed',
            field=models.BooleanField(default=True),
        ),
    ]
