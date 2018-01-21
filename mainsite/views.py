from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from mainsite import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import System


# Create your views here.
@login_required(login_url='login')
def summary(request):
    return render(request, 'base.html', locals())


def login(request):
    if request.user.is_authenticated:
        return redirect(to='summary')
    if request.method != 'POST':
        form = forms.LoginForm()
    else:
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username'].strip()
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, 'ログインしました')
                    return redirect(to=summary)
                else:
                    messages.add_message(request, messages.ERROR,
                                         'ユーザーは無効です。 システム管理者に連絡してください。')
            else:
                messages.add_message(request, messages.ERROR, 'ログインに失敗しました')

    return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, 'ログアウトしました')
    return redirect(to=login)


def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                auth.login(request, user)
                messages.add_message(request, messages.SUCCESS, user.last_name + 'さま、QA Managerへようこそ')
                return redirect(to=summary)
        else:
            messages.add_message(request, messages.ERROR, 'バリデーションエラー')
    else:
        form = forms.SignUpForm()
    return render(request, 'signup.html', locals())


@login_required(login_url='login')
def profile(request):
    user = request.user
    form = forms.ProfileForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'ユーザ情報を更新しました。')
    return render(request, 'profile.html', {'form': form})


@login_required(login_url='login')
def list_systems(request):
    own_systems = System.objects.filter(manager=request.user).filter(end_date=None)
    attend_systems = request.user.system_set.filter(end_date=None)
    return render(request, 'system_list.html', locals())
