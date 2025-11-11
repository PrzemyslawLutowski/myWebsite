from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'content',
        'publish',
        'status',
        'author',
    ]
    list_filter = [
        'status',
        'publish',
        'author',
    ]
    search_fields = [
        'title',
        'content'
    ]
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    show_facets = admin.ShowFacets.ALWAYS