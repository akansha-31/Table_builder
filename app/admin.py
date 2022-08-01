from django.contrib import admin
from .models import TableColumns, TableRecords, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
 
admin.site.register(User, UserAdmin)
admin.site.register(TableRecords)
admin.site.register(TableColumns)