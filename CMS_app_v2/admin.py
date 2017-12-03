from django.contrib import admin
from CMS_app_v2.models import Document

class CMSAdmin(admin.ModelAdmin):

    # Defining the fields that can be searched
    search_fields = ['title', 'status']

    # Defining the fields that can be filtered
    list_filter = ['status']

    # Defining the fields to be displayed in the list view
    list_display = ['title', 'description', 'document', 'uploaded_datetime', 'status']

    # Defining the fields to be editable in the list view
    list_editable = ['status', 'document']

# Register your models here.
admin.site.register(Document, CMSAdmin)
