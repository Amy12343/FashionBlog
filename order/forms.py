from django import forms
from .models import order_class


class order(forms.ModelForm):
    class Meta:
        model = order_class
        fields = ('order_no', 'order_Date', 'order_details', 'order_image', 'Customer', 'Payment')