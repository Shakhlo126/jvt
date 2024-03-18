from django.contrib import admin
from .models import Category, Tag, Book


# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ( 'id','title', 'author')
    list_display_links = ('id', 'title')
    filter_horizontal = ('tags',)
    search_fields = ('title',)


admin.site.register(Book, Admin)
admin.site.register(Category)
admin.site.register(Tag)

