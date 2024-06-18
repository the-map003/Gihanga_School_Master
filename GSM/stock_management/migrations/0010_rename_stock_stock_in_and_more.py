# Generated by Django 5.0.4 on 2024-04-30 09:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_management', '0009_alter_purchaseorder_options_purchaseorder_total'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stock',
            new_name='Stock_In',
        ),
        migrations.RenameField(
            model_name='stock_in',
            old_name='suppliyer',
            new_name='supplier',
        ),
        migrations.RenameField(
            model_name='stock_out',
            old_name='suppliyer',
            new_name='supplier',
        ),
    ]