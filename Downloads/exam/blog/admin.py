from django.contrib import admin
from .models import (Category,
                     Comments,
                     Post,
                     Advertise,
                     Author,
                     Subscribe,
                     Tag,
                     Insta_images)


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_name', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'author_name')
    search_fields = ['title', 'author_name']
    # filter_horizontal = ['Tag']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Subscribe)
admin.site.register(Insta_images)
admin.site.register(Comments)
admin.site.register(Advertise)
