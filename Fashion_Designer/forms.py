from django import forms
from .models import Fashion_Designer_class


class Fashion_Designer(forms.ModelForm):
    class Meta:
        model = Fashion_Designer_class
        fields = '__all__'