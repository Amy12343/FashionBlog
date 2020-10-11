from django import forms
from .models import Product_Class


class Product(forms.ModelForm):
    class Meta:
        model = Product_Class
        fields = '__all__'