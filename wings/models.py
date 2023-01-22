#from concurrent.futures.process import _python_exit
from datetime import date
import email
from random import choices
from secrets import choice
from unicodedata import name
from django.db import models
from django.utils import dateformat

class Patient(models.Model):
    GENDER = (
        ('M' ,'M'),
        ('F' ,'F'),
    )

    MARITAL_STATUS = (
        ('SINGLE' ,'SIMGLE'),
        ('MARRIED' ,'MARRIED'),
        ('DIVORCE' ,'DIVORCE'),
        ('WIDOW' ,'WIDOW'),
    )

    FOOD_TYPE = (
        ('VEGETARIAN' ,'VEGETARIAN'),
        ('NON-VEGETARIAN' ,'NON-VEGETARIAN'),
        ('EGGITARIAN' ,'EGGITARIAN'),
        ('OTHER' ,'OTHER'),
    )
    case_paper_no =models.IntegerField(primary_key=True )
    file_no=models.CharField(max_length=20)
    date=models.DateField()
    name=models.CharField(max_length=40)
    age=models.CharField(max_length=3)
    gender=models.CharField(max_length=1,null=True,choices=GENDER)
    height=models.CharField(max_length=50)
    weight=models.CharField(max_length=100)
    address=models.CharField(max_length=200,null=False)
    pin_code=models.IntegerField()
    telephone=models.CharField(max_length=200)
    office=models.CharField(max_length=300)
    marital_status=models.CharField(max_length=20,null=True,choices=MARITAL_STATUS)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    
    food_type=models.CharField(max_length=30,null=True,choices=FOOD_TYPE)
    qualification=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100)
    reffered_by=models.CharField(max_length=400)
    diagnosis_provisional=models.CharField(max_length=200)
    diangosis_final=models.CharField(max_length=300)
    chief_complaints=models.TextField()
    duration=models.CharField(max_length=200,null=True)
    rx_taken=models.CharField(max_length=300)
    note=models.TextField()
   
    
    def __str__(self):
        return self.name


"""
class Images(models.Model):
    image=models.ImageField(upload_to='upload_images/%Y/%m/%d/')
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)

    def __str__(self):
        return self.image
   """

  
class UploadImage(models.Model):  
    caption = models.CharField(max_length=200,null=True)  
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')  
  
    def __str__(self):  
        return self.caption

# ---------------------------------------------Upload Images -----------------------------------------
#class MultipleImage(models.Model):
 #   images=models.FileField()

class Multiple(models.Model):
    images=models.FileField()
