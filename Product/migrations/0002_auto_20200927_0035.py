# Generated by Django 3.1.1 on 2020-09-26 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('Customer', '0002_auto_20200927_0035'),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choose',
            new_name='order_product',
        ),
    ]
