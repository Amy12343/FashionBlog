# Generated by Django 3.1.1 on 2020-09-26 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0004_customer_class_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_class',
            name='Address',
        ),
        migrations.AlterField(
            model_name='customer_class',
            name='Name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
