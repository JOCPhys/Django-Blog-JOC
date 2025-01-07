from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
"""
Admin configuration for the Post model.
customise admin interface for managing Post objects.
Ingerits from SummernoteModelAdmin to provide rich text editing capabilities 
for the content field.

Attributes:
    list_display (tuple): fields to display in the admin list view.
    search_fields (list): fields to search for in the admin list view.
    list_filter (tuple): fields to filter by in the admin list view.
    prepopulated_fields (dict): fields to prepopulate based on other fields.
    summernote_fields (tuple): fields to enable rich text editing.
"""
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)