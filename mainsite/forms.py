from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'last_name', 'first_name', 'password', 'confirm_password', ]
        widgets = {
            'email': forms.EmailInput,
            'password': forms.PasswordInput,
        }
        labels = {
            'email': 'メールアドレス',
            'username': 'ユーザ名',
            'password': 'パスワード',
            'last_name': '姓',
            'first_name': '名'
        }
        help_texts = {
            'username': None
        }

    confirm_password = forms.CharField(widget=forms.PasswordInput, label='パスワード確認')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }
