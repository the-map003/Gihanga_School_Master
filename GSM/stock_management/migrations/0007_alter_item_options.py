# Generated by Django 5.0.4 on 2024-04-26 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_management', '0006_remove_item_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['created_at']},
        ),
    ]