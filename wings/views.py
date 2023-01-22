from email import message
from functools import cache
from unicodedata import name
from django.db.models import Q
import re
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .forms import UserImage
from .models import Patient
from django.http import HttpResponseRedirect 
from django.contrib import messages
from .models import Patient
from django.core.paginator import Paginator
from .models import UploadImage
# Create your views here.
def frontend(request):
    return render(request,"frontend.html")

#------------backend-Section-----------

@login_required(login_url="login")
def backend(request):
     query = request.GET.get('query', None)
     #print(query)
     if query:
          #print(q)
          #query= request.GET['query']
          #print(" find the value",query)
          all_patient_list = Patient.objects.filter(Q(case_paper_no=query) | Q(file_no=query) | Q(phone=query) | Q(name=query))
          return render(request,"backend.html",{"patients": all_patient_list})  

     else:
        all_patient_list = Patient.objects.all().order_by('phone')
        paginator = Paginator(all_patient_list,10)
        page = request.GET.get('page')
        all_patient = paginator.get_page(page)
        return render(request,"backend.html",{"patients": all_patient})
         
     return render(request,"backend.html")
    # return HttpResponse(" This is backend page")
@login_required(login_url="login")
def add_patient(request):
    if request.method=="POST":
        #print('first')

        patient=Patient()
        #print('second')
        patient.case_paper_no= request.POST.get('case_paper_no')
        patient.file_no= request.POST.get('file_no')
        #print(patient.file_no)
       # print("file number is here")
        patient.date= request.POST.get('date')
        patient.name= request.POST.get('name')
        patient.age= request.POST.get('age')
        patient.gender= request.POST.get('gender')
        patient.height= request.POST.get('height')
        patient.weight= request.POST.get('weight')
        patient.address= request.POST.get('address')
        patient.pin_code= request.POST.get('pin_code')
        patient.telephone= request.POST.get('telephone')
        patient.office= request.POST.get('office')
        patient.marital_status= request.POST.get('marital_status')
        patient.phone= request.POST.get('phone')
        patient.email= request.POST.get('email')
        patient.food_type= request.POST.get('food_type')
        patient.qualification= request.POST.get('qualification')
        patient.occupation= request.POST.get('occupation')
        patient.reffered_by= request.POST.get('reffered_by')
        patient.diagnosis_provisional= request.POST.get('diagnosis_provisional')
        patient.diangosis_final= request.POST.get('diagnosis_final')
        patient.chief_complaints= request.POST.get('chief_complaints')
        patient.duration= request.POST.get('duration')
        patient.rx_taken= request.POST.get('rx_taken')
        patient.note= request.POST.get('note')
        #patient.created_at=request.POST.get('created_at')
        patient.save()
        #print("hi this page")
        #patient.save()
        messages.success(request,"Patients Added Successfully ")
            #return HttpResponse('patients addded succesfully')
            #return render(request,'add.html')
        #return HttpResponseRedirect(request,'/backend/')
        return render(request,'add.html')
    else:
        return render(request,'add.html')


#function to access the patient individual

@login_required(login_url="login")
def patient(request,case_paper_no):
    patient = Patient.objects.get(case_paper_no=case_paper_no)
    p={'case_paper_no': patient.case_paper_no,
        'file_no': patient.file_no,
        'date':patient.date,
        'name':patient.name,
        'age':patient.age,
        #'gender':patient.gender,
        'height':patient.height,
        'weight':patient.weight,
        'address':patient.address,
        'pin_code':patient.pin_code,
        'telephon':patient.telephone,
        'office':patient.office,
        'phone':patient.email,
        'qualification':patient.qualification,
        'occupation':patient.occupation,
        'reffered_by':patient.reffered_by,
        'diagnosis_provisional':patient.diagnosis_provisional,
        'diangosis_final':patient.diangosis_final,
        'duration':patient.duration,
        'rx_taken':patient.rx_taken,
        'note':patient.note,
        'gender':patient.gender,
        'marital_status':patient.marital_status,
        
        }
    #print("case_paper_no=",p.case_paper_no)
   # print(p)
    return render(request,"edit.html",{'p':p})
        #print("This is Patient_id=" , patient.case_paper_no)
        #return render(request,"edit.html",{'Patient':patient.id1})




"""
def add_new(request):
    if request.method=='POST':
        form = AddForm(request.POST)
        if form.is_valid():
            Patient = form.save()
            for image in request.FILES.getlist('images'):
                Images.objects.create(
                    ad_id=ad.pk,
                    image=image
                )
            return redirect('/')
    else:
        form = AddForm()
    return render(request,'add_post.html', {'form':form})
"""
#edit patient

@login_required(login_url="login")
def edit_patient(request):
    if request.method=='POST':
        patient=Patient.objects.get(case_paper_no=request.POST.get('case_paper_no'))
        if patient != None:
            patient.case_paper_no=request.POST.get('case_paper_no')
            patient.file_no=request.POST.get('file_no')
            patient.date=request.POST.get('date')
            patient.name=request.POST.get('name')
            patient.age=request.POST.get('age')
            patient.height=request.POST.get('height')
            patient.weight=request.POST.get('weight')
            patient.address=request.POST.get('address')
            patient.pin_code=request.POST.get('pin_code')
            patient.telephone=request.POST.get('telephone')
            patient.office=request.POST.get('office')
            patient.phone=request.POST.get('phone')
            patient.email=request.POST.get('email')
            patient.qualification=request.POST.get('qualification')
            patient.occupation=request.POST.get('occupation')
            patient.reffered_by=request.POST.get('reffered_by')
            patient.diagnosis_provisional=request.POST.get('diagnosis_provisional')
            patient.diagnosis_final=request.POST.get('diagnosis_final')
            patient.duration=request.POST.get('duration')
            patient.rx_taken=request.POST.get('rx_taken')
            patient.note=request.POST.get('note')
            patient.gender=request.POST.get('gender')
            patient.marital_status=request.POST.get('marital_status')
            patient.food_type=request.POST.get('food_type')
            patient.save()
            messages.success('request',"patient updated successfully")
            return HttpResponseRedirect('/backend')

# function to Delete the Patient
#@cache_control(no_cache=True, must_reval:date)
@login_required(login_url="login")
def delete_patient(request,case_paper_no):
    patient=Patient.objects.get(case_paper_no=case_paper_no)
    patient.delete()

    messages.success(request,"Patient Deleted Successfully")
    return HttpResponseRedirect('/backend')


# Fetching Image from database

@login_required(login_url="login")
def display_images(request,case_paper_no):  
    query = request.GET.get('query', None)
    patient=Patient.objects.all()
    upimg=UploadImage.objects.filter(patient=case_paper_no)
    #print(upimg.caption )
    #print(upimg)
   # print(patient.file_no)
    #print(patient.date)

    #all_patient_list = Patient.objects.filter(Q(case_paper_no=query) | Q(name=query))
    return render(request,"image.html",{"patients":upimg,"patient":patient}) 
    #return render(request,"backend.html",{"patients": all_patient_list})  
   
    
    #return render(request, 'image.html')



#-----------------------------image uploads---------------
# from wings.forms import UserImage  
# from .models import UploadImage  
  
# def image_request(request):  
#     if request.method == 'POST':  
#         form = UserImage(request.POST, request.FILES)  
#         if form.is_valid():  
#             form.save()  
  
#             # Getting the current instance object to display in the template  
#             img_object = form.instance  
              
#             return render(request, 'image.html', {'form': form, 'img_obj': img_object})  
#     else:  
#         form = UserImage()  
  
#     return render(request, 'image.html', {'form': form})  



# from django.views.generic import ListView
# from .models import UploadImage


# class HomePageView(ListView):
#     model = UploadImage
#     template_name = "image.html"


# from .models import UploadImage
# #from .models import MultipleImage
# @login_required(login_url="login")
# def upload(request):
#     if request.method == "POST":
#         images = request.FILES.getlist('images')
#         for image in images:
#             UploadImage.objects.create(images=image)
#     images = UploadImage.objects.all()
#     print("*******************"+"Hi world"+"******************************")
#     return render(request, 'upimg.html', {'images': images})



# @login_required(login_url="login")
# def upload(request):
#     image1=UploadImage.objects.last()
#     #image1file=image1.imagefile
#     #form=UserImage(request.POST)
#     #if form.is_valid():
#      #   form.save()

#     # if request.method == "POST":
#     #     images = request.FILES.getlist('images')
#     #     for image in images:
#     #         UploadImage.objects.create(images=image)
#     # images = UploadImage.objects.all()
#     print("*******************"+"Hi world"+"******************************")
#     return render(request, 'upimg.html', {'images': image1})



from .models import Multiple

def  upload(request):
    if request.method=='POST':

        images=request.FILES.getlist('images')
        for img in images:
            Multiple.objects.create(images=img)
    images=Multiple.objects.all()
    print(images)
    return render(request,"index.html",{"images":images})


