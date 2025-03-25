"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "ASC"
admin.site.site_title = "ASC"
admin.site.index_title = "ASC"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/website/', include('website.urls')),
    path('api/services/', include('Services.urls')),
    path('api/portfolio/', include('Portfolio.urls')),
    path('api/contact/', include('Contact.urls')),
    path('api/career/', include('Career.urls')),
    path('api/blogs/', include('Blogs.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/master/', include('website_Master.urls')),
    path('api/quiz/', include('quiz.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
