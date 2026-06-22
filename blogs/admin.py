from django.contrib import admin

from .models import Category,Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'status', 'created_at','is_featured')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('title', 'author', 'short_description', 'body_description','status')
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate the slug field based on the title
    list_editable =('is_featured',)  # Allow editing the is_featured field directly from the list view

    
# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)  # Register the Blog model with the custom BlogAdmin class