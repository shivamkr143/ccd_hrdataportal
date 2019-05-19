from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Job_Profiles(models.Model):
    profile_name = models.CharField(max_length=1000,blank=False)
    description = models.CharField(max_length=4000,blank=True)
    def __str__(self):
        return self.profile_name

class Company(models.Model):
    company_name = models.CharField(max_length=1500,blank=False)
    alt_name1 = models.CharField(max_length=1500,blank=True)
    alt_name2 = models.CharField(max_length=1500,blank=True)
    alt_name3 = models.CharField(max_length=1500,blank=True)
    alt_name4 = models.CharField(max_length=1500,blank=True)
    offered_job_profile = models.ManyToManyField(Job_Profiles)
    sector = models.CharField(max_length=1500, blank=True)
    def __str__(self):
        return self.company_name

class HrDetails(models.Model):
    name = models.CharField(max_length=1500,blank=False)
    company_name = models.ForeignKey(Company,on_delete=models.CASCADE)
    email =  models.CharField(max_length=1500,blank=False)
    alt_email =  models.CharField(max_length=1500,blank=True)
    phone_number =  models.CharField(max_length=1500,blank=False)
    alt_phone_number = models.CharField(max_length=1500,blank=True)
    designation  = models.CharField(max_length=1500,blank=True)
    remarks = models.CharField(max_length=5000,blank=True)
    last_contacted = models.DateField(blank=True,null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
