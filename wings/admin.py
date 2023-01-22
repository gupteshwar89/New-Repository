import email
from django.contrib import admin

from .models import Patient
from .models import UploadImage

class PatientAdmin(admin.ModelAdmin):
    list_display=['case_paper_no', 'file_no','email','phone']
    search_fields=['case_paper_no','file_no','phone','email']
    list_per_page:10

    admin.site.register(Patient)
    admin.site.register(UploadImage)
    from .models import Multiple

# Register your models here.
    admin.site.register(Multiple)
