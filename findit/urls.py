"""
URL configuration for findit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.conf.urls import static
from django.contrib import admin
from django.urls import path

from findit import settings
from reports.views import add_report, edit_report, home, login_page, register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('home/login/', login_page, name='login_page'),    # Login page
    path('home/register/', register_page, name='register'),
    path('home/add_report/', add_report, name='add_report'),
    path('home/edit_report/<int:report_id>/', edit_report, name='edit_report'),
]

TEMPLATE_DIRS = [
    'templates',    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files
urlpatterns += staticfiles_urlpatterns()
