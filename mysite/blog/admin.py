from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nome', 'publicado', 'criado')
    list_filter = ('nome', 'publicado', 'criado')
    date_hierarchy = 'publicado'
    search_fields = ('nome',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado', 'status')
    list_filter = ('status', 'criado', 'publicado', 'autor')
    readonly_fields = ('view_image',)
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado'
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug': ('titulo',)}
