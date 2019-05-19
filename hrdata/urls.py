from django.contrib import admin
from django.conf.urls import url
from . import views
from hrdata import views
from django.urls import path
from  django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

app_name = 'hrdata'

urlpatterns = [
    url(r'^home/$', views.view_data, name='home'),
    url(r'^addcompany/$', views.addCompany, name='addcompany'),
    url(r'^addjobprofile/$', views.addJobProfile, name='add_jobprofile'),
    url(r'^addhr/$', views.addHr, name='add_hr')
]