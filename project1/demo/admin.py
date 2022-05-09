from django.contrib import admin
from .models import Employee, Project
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    lis_display=['id','name', 'sal']
admin.site.register(Employee, EmployeeAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'employee']
admin.site.register(Project, ProjectAdmin)