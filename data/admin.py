from django.contrib import admin
from .models import School, Profile,MyUser
# Register your models here.


class SchoolAdmin(admin.ModelAdmin):
    list_display=['school_id','name_school']
    search_fields=['name_school']
    list_filter=['school_id']


class ProfileAdmin(admin.ModelAdmin):
    list_display=['student_id','full_name','email','course']
    search_fields=['full_name']
    list_filter=['student_id']
    

class MyUserAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email']
    search_fields=['last_name']
    list_filter=['last_name']


admin.site.register(MyUser,MyUserAdmin)
admin.site.register(School,SchoolAdmin)
admin.site.register(Profile,ProfileAdmin)
