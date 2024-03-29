# Generated by Django 5.0.2 on 2024-02-21 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=40, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='img_product/', verbose_name='Картинка')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('in_stock', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category', verbose_name='Категория')),
            ],
        ),
    ]
