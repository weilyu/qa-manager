from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def index(request):
    user = User.objects.get(username='lvwei1001')
    auth.login(request, user)
    return render(request, 'base.html', locals())
