# Generated by Django 3.1.1 on 2020-09-26 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_remove_customer_class_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_class',
            name='Address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Customer.address'),
        ),
    ]
