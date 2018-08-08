from django import forms
from django.forms import ModelForm
from .models import *
from app.models import Register,Cart
from  django.db.models import fields
from django.contrib.auth import authenticate, get_user_model, login, logout

user = get_user_model()

class userLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username = username,password=password)
        if username and password:
            if not user:
                raise forms.ValidationError("the user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("the user is no longer active")
        return super(userLogin,self).clean(*args, **kwargs)

class userRegister(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),required = True,max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),required = True,max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),required = True,max_length=50)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone'}),required = True,max_length=20)

    class Meta():
        model = Register
        fields = ['fullname','email','password','phone']
