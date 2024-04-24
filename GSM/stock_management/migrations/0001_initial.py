# Generated by Django 5.0.4 on 2024-04-23 08:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact1', models.CharField(max_length=255)),
                ('contact2', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='stock_management.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Stock_Out',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit', models.FloatField()),
                ('stocked_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.TextField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockout', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockout', to='stock_management.item')),
                ('suppliyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockout', to='stock_management.supplier')),
            ],
            options={
                'ordering': ['-stocked_at'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit', models.FloatField()),
                ('stocked_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.TextField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='stock_management.item')),
                ('suppliyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='stock_management.supplier')),
            ],
            options={
                'ordering': ['-stocked_at'],
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit', models.FloatField()),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='stock_management.item')),
                ('suppliyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='stock_management.supplier')),
            ],
            options={
                'ordering': ['-ordered_at'],
            },
        ),
    ]