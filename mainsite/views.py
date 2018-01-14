from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from mainsite import forms


# Create your views here.
def index(request):
    user = User.objects.get(username='lvwei1001')
    auth.login(request, user)
    return render(request, 'base.html', locals())


def login(request):
    # TODO: if user is logged in, redirect to index
    form = forms.LoginForm()
    return render(request, 'login.html', locals())
