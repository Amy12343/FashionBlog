# Generated by Django 3.1.1 on 2020-09-28 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20200927_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_class',
            name='Product_image',
            field=models.ImageField(null='true', upload_to=''),
            preserve_default='true',
        ),
        migrations.AlterField(
            model_name='product_class',
            name='Catagories',
            field=models.CharField(choices=[('Cloth', 'Cloth'), ('Shoes', 'Shoes'), ('Cosmetics', 'Cosmetics')], default='Cloth', max_length=50),
        ),
    ]
