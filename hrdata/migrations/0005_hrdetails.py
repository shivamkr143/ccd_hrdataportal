# Generated by Django 2.1.1 on 2019-05-18 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrdata', '0004_delete_hrdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='HrDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1500)),
                ('email', models.CharField(max_length=1500)),
                ('alt_email', models.CharField(blank=True, max_length=1500)),
                ('phone_number', models.CharField(max_length=1500)),
                ('alt_phone_number', models.CharField(blank=True, max_length=1500)),
                ('designation', models.CharField(blank=True, max_length=1500)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrdata.Company')),
            ],
        ),
    ]
