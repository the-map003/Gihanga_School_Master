# Generated by Django 5.0.4 on 2024-06-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0004_alter_author_options_remove_author_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='author',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
    ]
