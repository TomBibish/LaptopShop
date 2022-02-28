# Generated by Django 4.0.2 on 2022-02-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_app', '0003_alter_laptop_flash_storage_alter_laptop_hdd_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='weight',
            field=models.FloatField(max_length=128),
        ),
    ]