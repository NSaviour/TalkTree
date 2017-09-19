from django.contrib import admin
from .models import *
# Register your models here.

class testInfoAdmin(admin.ModelAdmin):
    list_display=['pk','title','ttpub_date']





admin.site.register(testInfo,testInfoAdmin)


