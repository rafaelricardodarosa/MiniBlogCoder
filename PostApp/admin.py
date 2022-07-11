from django.contrib import admin

# Register your models here.

from .models import Category, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at'] #aqui nos mostra los campos que queremos en painel de admin
    prepopulated_fields = {'slug': ('title',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'updated_at', 'image_table'] #aqui nos mostra los campos que queremos en painel de admin
    readonly_fields = ('image_table',)
    list_filter = ['category'] #aqui nos filtra por categoria en painel admin
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['status']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
