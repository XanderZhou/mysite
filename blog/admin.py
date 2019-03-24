from django.contrib import admin
from .models import BlogType,Blog
# Register your models here.


@admin.register(BlogType)
class blogtypeadmin(admin.ModelAdmin):
    list_display = ('id',"type_name")

@admin.register(Blog)
class blogadmin(admin.ModelAdmin):
    list_display = ('pk','blog_type','context','title','author','created_time')