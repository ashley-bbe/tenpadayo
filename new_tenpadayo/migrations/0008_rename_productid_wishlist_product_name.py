# Generated by Django 3.2 on 2021-07-13 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_tenpadayo', '0007_auto_20210713_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='productid',
            new_name='product_name',
        ),
    ]