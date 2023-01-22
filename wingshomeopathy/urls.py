"""wingshomeopathy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 
from wings import views
#from wings.views import image_request
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.frontend, name='frontend'),
    path('login/',include('django.contrib.auth.urls')),
    
    #Path to access the backend page
    
    path('backend/',views.backend, name='backend'),
    #path to add_patient the frontend page
    path('add_patient/',views.add_patient, name='add_patient'),
    #path to access the patients individuals
    path('patient/<int:case_paper_no>',views.patient,name="patient"),
    #path to edit the edit patients
    path('edit_patient/',views.edit_patient, name='edit_patient'),
    #path to Delete_Patient the edit patients
    path('delete_patient/<int:case_paper_no>',views.delete_patient, name='delete_patient'),
    
    
    #fetching Images
    #path('show/<int:case_paper_no>', views.display_images,name='display_images'),
    #path('display_image/<int:case_paper_no>',views.display_images, name='display_image'),

     #path('', image_request, name = "image-request")  
     #path('image/', include(('wings.urls'), namespace='wings')) 
     path('image/<int:case_paper_no>',views.display_images,name='display_images'),
    #upload Images
     path('uploadimg/',views.upload,name="upload_images"),
     

]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)