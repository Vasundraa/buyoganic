# Generated by Django 5.0.1 on 2024-05-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0004_alter_productshop_options_productshop_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productshop',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
    ]
