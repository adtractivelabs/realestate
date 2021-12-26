from django.contrib import admin
from .models import  *

# AuthorProfile Admin View
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ['name','gender','date_created','date_modified']
    list_filter  = ['name','gender','date_created','date_modified']

# BlogCategory Admin View
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','name','image','author','created_date']
    list_filter  = ['title','name','image','author','created_date']

# Tag Admin view
class TagAdmin(admin.ModelAdmin):
    list_display = ['name','author','is_draft','created_date']
    list_filter  = ['name','author','is_draft','created_date']


#  Blog Admin View
class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_title','blog_slug','blog_category','blog_author','is_draft','pub_date','created_date']
    list_filter  = ['blog_title','blog_slug','blog_category','blog_author','is_draft','pub_date','created_date']
    prepopulated_fields = {'blog_slug': ('blog_title',), } 

admin.site.register(AuthorProfile,AuthorProfileAdmin)
admin.site.register(BlogCategory,BlogCategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Blog,BlogAdmin)

