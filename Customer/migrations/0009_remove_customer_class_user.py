# Generated by Django 3.1.1 on 2020-10-03 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0008_auto_20201002_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_class',
            name='user',
        ),
    ]
