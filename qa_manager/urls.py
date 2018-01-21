"""qa_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summary', views.summary, name='summary'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('system/list', views.list_systems, name='list_systems'),
    path('system/new', views.new_system, name='new_system'),
    path('system/<int:system_id>/quit', views.quit_system, name='quit_system'),
    path('system/<int:system_id>/end', views.end_system, name='end_system'),
    path('system/<int:system_id>/reopen', views.reopen_system, name='reopen_system'),
    path('system/<int:system_id>invite', views.system_invite, name='system_invite'),
    path('qa/new', views.new_qa, name='new_qa')

]
