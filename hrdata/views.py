from django.shortcuts import render,redirect
import pickle
import os
from django.contrib import messages
from graphos.sources.simple import SimpleDataSource
from graphos.renderers import gchart
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from  django.views import generic
from django.http import HttpResponse,HttpResponseRedirect
from hrdata.forms import CompanyForm,HrForm,JobProfileForm
from hrdata.models import Company,Job_Profiles,HrDetails
from  django.contrib.auth import authenticate,login,logout
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
# Create your views here.

def home(request):
    return HttpResponse("hello working")


def addCompany(request):
    company_form = CompanyForm()
    if request.method == "POST":
        company_form = CompanyForm(request.POST)
        if company_form.is_valid:
            company_form.save(commit=True)
            return HttpResponse("Company added")
    else:
        form_name ="Company Details"
        return render(request, 'addCompany.html', {'form': company_form,'form_name':form_name})


def addHr(request):
    hr_form = HrForm()
    if request.method == "POST":
        hr_form = HrForm(request.POST)
        if hr_form.is_valid:
            hr_form.save(commit=True)
            return HttpResponse("HR Details added")
    else:
        form_name = "HR Details"
        return render(request, 'addCompany.html', {'form': hr_form,'form_name':form_name})

def addJobProfile(request):
    jobprofile_form = JobProfileForm()
    if request.method == "POST":
        jobprofile_form = JobProfileForm(request.POST)
        if jobprofile_form.is_valid:
            jobprofile_form.save(commit=True)
            return HttpResponse("Job Profile added")
    else:
        form_name = "Job Profile Details"
        return render(request, 'addCompany.html', {'form': jobprofile_form,'form_name':form_name})

def view_data(request):
    hrdata = HrDetails.objects.all()
    company_details = Company.objects.all()
    print(company_details)
    for d in company_details:
        print(d.offered_job_profile.all())

    return render(request, 'home.html', {'company_details':company_details})
