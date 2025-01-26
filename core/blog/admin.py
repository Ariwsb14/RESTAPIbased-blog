from django.contrib import admin
from .models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_date', 'published_date', 'author')
    list_filter = ('status', 'created_date', 'published_date', 'author')
    search_fields = ('title', 'content', 'author__email')
    ordering = ('-created_date',)   

# show models in admin panel/
admin.site.register(Post)
admin.site.register(Category)
