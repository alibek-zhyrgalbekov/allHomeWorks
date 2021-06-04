import re
from itertools import product

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput, PasswordInput, NumberInput, Select
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


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=TextInput(attrs={
                                   "placeholder": "Nickname",
                                   'class': 'form-control'
                               }))
    email = forms.CharField(max_length=100,
                            widget=TextInput(attrs={
                                'placeholder': 'eMail',
                                'class': 'form-control'
                            }))
    password = forms.CharField(max_length=100,
                               widget=PasswordInput(attrs={
                                   'placeholder': 'Repeat Password',
                                   'class': 'form-control'
                               }))
    password1 = forms.CharField(max_length=100,
                                widget=PasswordInput(attrs={
                                    'placeholder': 'Repeat Password',
                                    'class': 'form-control'
                                }))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).count() > 0:
            raise ValidationError('Такой пользователь существует')
        return username

    def clean_email(self):
        result = re.split(r'@', self.cleaned_data['email'])

        if len(result) > 1:
            result2 = re.split(r'\.', result[1])
            if len(result2) > 1:
                return self.cleaned_data['email']
            else:
                raise ValidationError('Введите корректный eMail!')
        else:
            raise ValidationError('Введите корректный eMail!')

    def clean_password1(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise ValidationError('Пароли не совпадают')
        return self.cleaned_data['password1']

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        email='a@b.ru',
                                        password=self.cleaned_data['password1'])
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=4, label="Введите логин",
                               widget=TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Логин'
                               }))

    password = forms.CharField(max_length=100, min_length=4, label="Пароль",
                               widget=PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Пароль'
                               }))

    def clean_username(self):
        users = User.objects.filter(username=self.cleaned_data['username'])

        if len(users) == 0:
            raise ValidationError('Введите корректные данные!')

        return self.cleaned_data['username']


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=200,
                            widget=TextInput(attrs={
                                'placeholder': 'Название продукта',
                                'class': 'form-control'
                            }))
    price = forms.IntegerField(
        widget=NumberInput(attrs={
            'placeholder': 'Цена',
            'class': 'form-control'
        }))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=Select(attrs={
            'placeholder': 'Название категории',
            'class': 'form-control'
        }))

    class Meta:
        model = Product
        fields = '__all__'
