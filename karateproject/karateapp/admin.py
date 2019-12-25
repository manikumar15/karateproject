from django.contrib import admin
from .models import Enquiry


admin.site.site_header = 'Karate Webiste'


class Enquiryadmin(admin.ModelAdmin):
    list_display = ('name','email','message',)
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Enquiry,Enquiryadmin)