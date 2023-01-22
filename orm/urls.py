# from django.contrib import admin  
# from django.urls import path  
# from django.urls.conf import include  
# from django.conf import settings  
# from django.conf.urls.static import static  
  
# urlpatterns = [  
#     path('admin/', admin.site.urls),  
#     path('', include(('orm.urls'), namespace='orm'))  
      
# ]  
# if settings.DEBUG:  
#         urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 



from django.urls import path  
from .views import image_request  
  
app_name = 'orm'  
urlpatterns = [  
    path('',image_request, name = "image-request")  
]