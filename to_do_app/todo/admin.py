from django.contrib import admin
from .models import UserProfile, Todo
# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title','description','completed']
    search_fields = ['title']
    
    
admin.site.register(UserProfile)
    
