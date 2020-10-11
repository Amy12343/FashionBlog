from django import forms
from .models import Customer_class


class Customer(forms.ModelForm):
    class Meta:
        model = Customer_class
        fields = '__all__'