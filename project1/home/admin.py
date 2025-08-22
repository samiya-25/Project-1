from django.contrib import admin
from .models import Home

# Register your models here.
class homeAdmin(admin.ModelAdmin):
    list_display=['name','age','email']


admin.site.register(Home,homeAdmin)