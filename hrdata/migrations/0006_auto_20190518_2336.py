# Generated by Django 2.1.1 on 2019-05-18 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrdata', '0005_hrdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='sector',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='hrdetails',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hrdetails',
            name='last_contacted',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hrdetails',
            name='remarks',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
