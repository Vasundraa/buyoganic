# Generated by Django 4.2.2 on 2024-03-09 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0003_alter_productshop_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productshop',
            options={'ordering': ['-price']},
        ),
        migrations.AddField(
            model_name='productshop',
            name='category',
            field=models.CharField(default='NULL', max_length=255),
        ),
    ]