# Generated by Django 5.0.1 on 2024-05-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0006_alter_productshop_is_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productshop',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
    ]
