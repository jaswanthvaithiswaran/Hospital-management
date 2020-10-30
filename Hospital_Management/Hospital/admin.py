from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  staff
# Register your models here.
class StaffAdmin(UserAdmin):
    list_display =('email','username')
    search_fields =('email','username')
    

    filter_horizontal =()
    list_filter = ()
    fieldsets = ()
admin.site.register(staff,StaffAdmin)
