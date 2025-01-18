from django.contrib import admin

from .models import Order
from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget


class orderResource(resources.ModelResource):
    
    class Meta:

        model=Order

class orderAdmin(ImportExportModelAdmin):
    resource_classe=orderResource
    list_display = [
        "document_type","okpo","status","job_description","contragent","conclusion","file_str","price","created_timestamp","guid","suma"
     
    ]
    
    search_fields = ["okpo","status","job_description","contragent","conclusion"]

admin.site.register(Order,orderAdmin)    


