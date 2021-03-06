# Generated by Django 4.0.2 on 2022-02-23 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('inches', models.FloatField(max_length=6)),
                ('resolution', models.CharField(max_length=128)),
                ('cpu', models.CharField(max_length=128)),
                ('ram', models.IntegerField(max_length=3)),
                ('ssd', models.IntegerField(blank=True, max_length=4, null=True)),
                ('hdd', models.IntegerField(blank=True, max_length=4, null=True)),
                ('flash_storage', models.IntegerField(blank=True, max_length=4, null=True)),
                ('gpu', models.CharField(max_length=128)),
                ('op_sys', models.CharField(max_length=128)),
                ('weight', models.FloatField(max_length=128)),
                ('price_euros', models.FloatField()),
                ('stock_amount', models.IntegerField(max_length=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='laptop_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('is_cancelled', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='laptop_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_price', models.FloatField()),
                ('amount', models.IntegerField(max_length=10)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='laptop_app.laptop')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='laptop_app.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_laptops',
            field=models.ManyToManyField(through='laptop_app.OrderItem', to='laptop_app.Laptop'),
        ),
    ]
