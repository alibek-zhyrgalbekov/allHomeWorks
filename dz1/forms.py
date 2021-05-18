from itertools import product

from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput
from dz1.models import Category, Product


class CategoryForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=10,
                           required=True, label='Продукт',
                           widget=TextInput(
                               attrs={
                                   'placeholder': 'Название продукта'
                               }
                           ))

    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            Product.objects.get(title=name)
            raise ValidationError('Такой продукт уже существует')
        except Exception:
            return name

    def save(self, commit=True):
        prod = Product.objects.create(title=self.cleaned_data['name'])
        prod.save()
        return prod


