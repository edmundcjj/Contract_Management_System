"""Contract_Management_System_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from CMS_app_v2 import views

urlpatterns = [

    # Define which function to be executed in view.py for the index url
    url(r'^$', views.index, name='index'),

    # Linking the urls.py file to a separate urls.py
    url(r'^CMS_app_v2/', include('CMS_app_v2.urls')),
    url(r'^admin/', admin.site.urls),

    # Define the location of where media files are stored so that the urls can
    # locate the file and allow it to be downloadable
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
