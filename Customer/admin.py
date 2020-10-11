from django.contrib import admin
from .models import Customer_class,Address
# Register your models here.
admin.site.register( [Customer_class,Address] )
