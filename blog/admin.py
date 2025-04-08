from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Post

class BlogAdminSite(AdminSite):
    site_header = "Blog Admin"
    site_title = "Blog Admin Portal"
    index_title = "Welcome to the Blog Admin"

blog_admin_site = BlogAdminSite(name='blog_admin')

@admin.register(Post, site=blog_admin_site)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    