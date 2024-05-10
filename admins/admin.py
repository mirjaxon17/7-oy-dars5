from django.contrib import admin
from .models import Adress,Admins
from import_export.admin import ImportExportModelAdmin

@admin.register(Admins)
class AdminsAdmin(ImportExportModelAdmin):
    list_display = ['id','first_name','last_name','email','phone_number','adress']
    list_display_link= ['id','first_name','last_name','email','phone_number','adress']
    search_fields =  ['id','first_name','last_name','adress']
