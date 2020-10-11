from django.contrib import admin
from.models import Product_Class,order_product
# Register your models here.
admin.site.register( [Product_Class,order_product] )
