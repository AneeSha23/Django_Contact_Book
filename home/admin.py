from django.contrib import admin

from .models import Contacts

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=("FirstName","LastName","Email","PhoneNumber")
admin.site.register(Contacts,ContactAdmin) #contacts is from models classname