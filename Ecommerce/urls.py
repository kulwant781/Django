"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
import shop  # Import the shop module
import blog  # Import the blog module
from django.conf import settings
from django.conf.urls.static import static
from blog.admin import blog_admin_site
from shop.admin import shop_admin_site

urlpatterns = [
    path('blog-admin/', blog_admin_site.urls),
    path('shop-admin/', shop_admin_site.urls),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Add a URL pattern for the home page
    path('shop/', include('shop.urls')),  # Use include() to include the shop app's URLs
    path('blog/', include('blog.urls')),  # Use include() to include the blog app's URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Add this line to serve media files in development

