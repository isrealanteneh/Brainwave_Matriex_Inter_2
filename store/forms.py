from django import forms 
from .models import Product ,StoreUser, Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'amount', 'unit_price', 'unit_of_measure','catagoires')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name','amount', 'shipping_address')
        
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','password')
        widgets = {
            'password':forms.PasswordInput(),
        }
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter password'

class MangegerForm(forms.ModelForm):
    class Meta:
        model = StoreUser
        fields = ['role','user_status']
        labels = {
            "role":"",
            "user_status":"",
        }
   
        
        
class MangegerOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        labels = {
            "status":""
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget =forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter password'
