from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100) 
    password = forms.CharField(label='Your password', max_length=100, widget=forms.PasswordInput) 
    password_confirm = forms.CharField(label='Confirm your password', max_length=100, widget=forms.PasswordInput) 


class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100) 
    password = forms.CharField(label='Your password', max_length=100, widget=forms.PasswordInput) 
