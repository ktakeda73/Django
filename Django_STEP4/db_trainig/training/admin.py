from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Office)
class OfficeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass