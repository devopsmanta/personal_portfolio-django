from django.contrib import admin
from .models import Category, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    pass


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'last_modified']
    list_filter = ['created_on']
    search_fields = ['title']
    inlines = [CommentInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_on', 'post']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

