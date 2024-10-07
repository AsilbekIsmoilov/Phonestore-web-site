from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from store.models import Customer, ShippingAddress


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"password",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"re-password",
    }))


    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"username",
            }),
            "email":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"email",
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"username",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"password",
    }))


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','email']
        widgets = {
            "name":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Your name"
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control",
                "placeholder":"Your email"
            })
        }




class ShippingAddresForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['city','street','address']
        widgets = {
            "city":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Your city"
            }),
            "street":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Your street"
            }),
            "address":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Your address"
            })
        }