from django import forms
from django.contrib.auth.models import User
from .models import System, Qa


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


class LoginForm(forms.Form):
    username = forms.CharField(label='ユーザ名', max_length=150)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)
    keep_logged_in = forms.BooleanField(widget=forms.CheckboxInput, label="ログイン情報を保持する", required=False, initial=False)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']
        labels = {
            'email': 'メールアドレス',
            'last_name': '姓',
            'first_name': '名'
        }
        widgets = {
            'email': forms.EmailInput,
        }


class SystemNewForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['name']


class InvitationForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['users']


class QaNewForm(forms.ModelForm):
    class Meta:
        model = Qa
        fields = ['system', 'function', 'title', 'detail', 'expect_answer_user', 'expect_answer_date', 'priority']
