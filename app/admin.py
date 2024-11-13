from django.contrib import admin

from .models import BlogDESC, Aftor, Kategoriya





@admin.register(BlogDESC)
class BlogMaqolaAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'date', 'author', 'category'
        ]



@admin.register(Aftor)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ['full_name']






@admin.register(Kategoriya)
class KategoriyaAdmin(admin.ModelAdmin):
    list_display = ['name']
