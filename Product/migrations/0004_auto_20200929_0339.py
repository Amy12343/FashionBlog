# Generated by Django 3.1.1 on 2020-09-28 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20200929_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_class',
            name='Product_image',
            field=models.ImageField(default=1, upload_to='images/Product_image/'),
        ),
    ]
