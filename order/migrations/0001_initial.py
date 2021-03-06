# Generated by Django 3.1.1 on 2020-09-26 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.IntegerField(blank=True, null=True)),
                ('order_Date', models.DateField(blank=True, null=True)),
                ('order_Status', models.TextField(blank=True, null=True)),
                ('Customer', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Customer.customer_class')),
            ],
        ),
    ]
