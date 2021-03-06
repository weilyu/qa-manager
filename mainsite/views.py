from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.models import User
from django.contrib import auth
from mainsite import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import System, Qa
from datetime import datetime


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
    own_systems = System.objects.filter(manager=request.user).order_by('end_date')
    attend_systems = request.user.attendances.all().filter(end_date=None)
    return render(request, 'system_list.html', locals())


@login_required(login_url='login')
def new_system(request):
    form = forms.SystemNewForm(request.POST or None)
    if form.is_valid():
        system = form.save(commit=False)
        system.manager = request.user
        system.save()
        system.users.add(request.user)
        messages.add_message(request, messages.SUCCESS, 'システムを登録しました。')
        return redirect(to=list_systems)
    return render(request, 'system_new.html', {'form': form})


@login_required(login_url='login')
def quit_system(request, system_id):
    system = get_object_or_404(System, id=system_id)
    if system.manager == request.user:
        messages.add_message(request, messages.ERROR, '管理しているプロジェクトを退出することはできません。')
    else:
        system.users.remove(request.user)
        messages.add_message(request, messages.INFO, system.name + 'から退出しました。')
    return redirect(to=list_systems)


@login_required(login_url='login')
def end_system(request, system_id):
    system = get_object_or_404(System, id=system_id)
    if system.manager != request.user:
        raise Http404
    system.end_date = datetime.today()
    system.save()
    messages.add_message(request, messages.INFO, system.name +
                         'のQA管理を停止しました。')
    return redirect(to=list_systems)


@login_required(login_url='login')
def reopen_system(request, system_id):
    system = get_object_or_404(System, id=system_id)
    if system.manager != request.user:
        raise Http404
    system.end_date = None
    system.save()
    messages.add_message(request, messages.INFO, system.name +
                         'のQA管理を再開しました。')
    return redirect(to=list_systems)


@login_required(login_url='login')
def system_invite(request, system_id):
    form = forms.InvitationForm(request.POST or None, instance=System.objects.get(id=system_id))
    if form.is_valid():
        system = System.objects.get(id=system_id)
        if system.manager != request.user:
            raise Http404
        form.save()
        messages.add_message(request, messages.SUCCESS, 'システムのユーザリストを更新しました。')
        return redirect(to=list_systems)
    return render(request, 'system_invite.html', {'form': form})


@login_required(login_url='login')
def new_qa(request):
    form = forms.QaNewForm(request.POST or None)
    if form.is_valid():
        qa = form.save(commit=False)
        qa.sender = request.user
        qa.save()
        messages.add_message(request, messages.SUCCESS, 'QAを発行しました。')
        redirect(to=summary)
    return render(request, 'qa_new.html', locals())


@login_required(login_url='login')
def list_qa(request):
    attend_systems = request.user.attendances.all().filter(end_date=None)
    qas = Qa.objects.filter(system__in=attend_systems)
    return render(request, 'qa_list.html', {'qas': qas})
