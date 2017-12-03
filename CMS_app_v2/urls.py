"""
Contract_Management_System_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""
from django.conf.urls import url, include
from CMS_app_v2 import views

app_name = 'CMS_app_v2'

# To define the specific function in views.py file to be executed
urlpatterns = [
    url(r'^upload/$', views.document_upload, name='upload'),
]
