"""
models forms
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .constant import CATEGORIES, COUNTRY, RESP, SEXE, STATUS
from exchange.models import Client, Detail, Product, Card, Professional

User = get_user_model()


class UserForm(UserCreationForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'First Name',
            'class': 'form-control'
        }
    ))

    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Last Name',
            'class': 'form-control'
        }
    ))

    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Username',
            'class': 'form-control'
        }
    ))

    email = forms.CharField(label='', widget=forms.EmailInput(
        attrs={
            'placeholder': 'Email',
            'class': 'form-control'
        }
    ), required=False)

    address = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Address',
            'class': 'form-control',
            
        }
    ), required=False)

    picture = forms.ImageField(label='', widget=forms.ClearableFileInput(
        attrs={
            'placeholder': 'entry your image',
            'class': 'form-control'
        }
    ), required=False)

    country = forms.ChoiceField(label='', choices=COUNTRY, widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    state = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'State',
            'class': 'form-control',
        }
    ), required=False)

    sexe = forms.ChoiceField(label='', choices=SEXE, widget=forms.Select(
        attrs={
            'class': 'form-control'
        },
    ), required=False)

    status = forms.ChoiceField(label='type of account', choices=STATUS, widget=forms.Select(
        attrs={
            'class': 'form-control'
        },
    ), required=False)

    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }
    ))

    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control'
        }
    ))
    
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'username',
            'email',
            'address',
            'picture',
            'country',
            'state',
            'sexe',
            'status',
            'password1',
            'password2'
        }


class ProForm(UserForm):
    class Meta:
        model = Professional
        fields = {
            'first_name',
            'last_name',
            'username',
            'email',
            'address',
            'picture',
            'country',
            'state',
            'sexe',
            'status',
            'password1',
            'password2'
        }

class CLiForm(UserForm):
    class Meta:
        model = Client
        fields = {
            'first_name',
            'last_name',
            'username',
            'email',
            'address',
            'picture',
            'country',
            'state',
            'sexe',
            'status',
            'password1',
            'password2'
        }


class ProductCreateForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Product Name',
            'class': 'form-control col-md-6'
        }
    ))

    price = forms.DecimalField(label='', widget=forms.NumberInput(
        attrs={
            'placeholder': 'Product Price',
            'class': 'form-control col-md-6'
        }
    ))

    picture = forms.ImageField(label='', widget=forms.ClearableFileInput(
        attrs={
            'placeholder': 'Product Image',
            'class': 'form-control col-md-6'
        }
    ), required=False)

    category = forms.ChoiceField(label='category', choices=CATEGORIES, widget=forms.Select(
        attrs={
            'class': 'form-control col-md-6'
        },
    ))
    
    class Meta:
        model = Product
        fields = ('name', 'price', 'picture', 'category')


class CardForm(forms.ModelForm):
    zip_code = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Zip Code',
            'class': 'form-control'
        }
    ), required=False)

    card_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Card Name',
            'class': 'form-control'
        }
    ), required=False)

    card_number = forms.CharField(label='', widget=forms.NumberInput(
        attrs={
            'placeholder': 'Card Number',
            'class': 'form-control'
        }
    ), required=False)

    expiration = forms.CharField(label='', widget=forms.DateInput(
        attrs={
            'placeholder': 'Expiration',
            'class': 'form-control'
        }
    ), required=False)

    cvv = forms.CharField(label='', widget=forms.NumberInput(
        attrs={
            'placeholder': 'CVV',
            'class': 'form-control'
        }
    ), required=False)

    class Meta:
        model = Card
        fields = ['zip_code', 'card_name', 'card_number', 'expiration', 'cvv']


class DetailForm(forms.ModelForm):
    product_number = forms.CharField(label='', widget=forms.NumberInput(
        attrs={
            'placeholder': 'Count',
            'class':'col-md-6'
        }
    ))

    class Meta:
        model = Detail
        fields = ['product_number']
