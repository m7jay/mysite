from django.contrib import admin

from blog.models import Author, Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_filter = ("title", "tags", "author", "date_created")
    list_display = ("title", "author", "date_created")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
