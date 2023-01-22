from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render  
from orm.forms import UserImage  
from .models import UploadImage  
  
def image_request(request):  
    if request.method == 'POST':  
        form = UserImage(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'image.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImage()  
  
    return render(request, 'image.html', {'form': form})  