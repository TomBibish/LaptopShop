# Generated by Django 4.0.2 on 2022-02-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_app', '0005_stats_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='laptop_grade',
            field=models.IntegerField(max_length=1),
        ),
    ]
