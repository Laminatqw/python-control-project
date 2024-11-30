# Generated by Django 5.1.3 on 2024-11-29 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=25)),
                ('brand', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('region', models.CharField(max_length=25)),
                ('currency', models.CharField(choices=[('UAH', 'Українська гривня'), ('EUR', 'Євро'), ('USD', 'Долар США')], max_length=5)),
                ('status', models.CharField(choices=[('active', 'Активний'), ('inactive', 'Неактивний'), ('pending', 'На розгляді')], max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]