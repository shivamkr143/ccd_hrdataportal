from django import forms
from django.forms import ModelForm,Textarea,Select
from hrdata.models import  Company,Job_Profiles,HrDetails

from django.contrib.auth.models import User


class CompanyForm(forms.ModelForm):
    class Meta():
        model=Company
        fields = ['company_name','alt_name1','alt_name2','alt_name3','alt_name4','offered_job_profile']
        # widgets = {
        #     'description': Textarea,
        #     'representativeComments':Textarea(attrs={'rows': 3 }),
        # }

class HrForm(forms.ModelForm):
    class Meta():
        model=HrDetails
        fields = '__all__'

class JobProfileForm(forms.ModelForm):
    class Meta():
        model=Job_Profiles
        fields = '__all__'



