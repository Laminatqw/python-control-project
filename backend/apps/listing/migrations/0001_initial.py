# Generated by Django 5.1.3 on 2024-12-01 14:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0003_remove_carmodel_currency_remove_carmodel_region_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='cars.carmodel')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')], max_length=3)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to=settings.AUTH_USER_MODEL)),
                ('region', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ListingViewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_at', models.DateTimeField(auto_now_add=True)),
                ('region', models.CharField(max_length=100)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='listing.listingmodel')),
            ],
        ),
    ]
