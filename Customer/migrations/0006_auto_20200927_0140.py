# Generated by Django 3.1.1 on 2020-09-26 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0005_auto_20200927_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_class',
            name='Address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Customer.address'),
        ),
        migrations.AlterField(
            model_name='customer_class',
            name='phone_No',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
