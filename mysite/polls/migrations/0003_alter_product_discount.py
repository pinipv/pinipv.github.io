# Generated by Django 4.1.5 on 2023-02-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_product_delete_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.BooleanField(),
        ),
    ]
