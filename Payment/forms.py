from django import forms
from .models import payment_class


class Payment(forms.ModelForm):
    class Meta:
        model = payment_class
        fields = '__all__'