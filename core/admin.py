from dataclasses import field
from django.contrib import admin
from core.models import Counterparts, News, Resume,contrgrupp,licenss,Priv,mg

from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget

class CounterpartsResource(resources.ModelResource):
    
    class Meta:

        model=Counterparts

class CounterpartsAdmin(ImportExportModelAdmin):
    resource_classe=CounterpartsResource
    list_display = [
        "name",
        "full_name",
        "adres",
        "okpo_cod",
        "group",
     
    ]
    prepopulated_fields={
        'slug':('name',)}
    # list_display=[field.name for field in Counterparts._meta.fields if field.name !='id']
    search_fields = ["name", "okpo_cod"]


admin.site.register(Counterparts,CounterpartsAdmin)


@admin.register(contrgrupp)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]

@admin.register(Priv)
class PrivAdmin(admin.ModelAdmin):
   
    list_display = ["grup","us"]


class licenssResource(resources.ModelResource):
    
    class Meta:

        model=licenss

class licenssAdmin(ImportExportModelAdmin):
    resource_classe=licenssResource
    list_display = [
        "okpo","data_po","create_at","guid","contragent",
     
    ]
    
    search_fields = ["okpo", "data_po","contragent"]


admin.site.register(licenss,licenssAdmin)
admin.site.register(Resume)
class mgResource(resources.ModelResource):
    class Meta:
         model=mg

class mgAdmin(ImportExportModelAdmin):
    resource_classe=mgResource
    list_display = ["okpo", "mg", "create_at", "contragent", "ip_address"]

    search_fields = ["contragent"]


admin.site.register(mg,mgAdmin)


class NewsResource(resources.ModelResource):
    class Meta:
        model = News


class NewsAdmin(admin.ModelAdmin):
    resource_classe = NewsResource
    list_display = ["title", "image", "file", "slug", "created_at"]
    search_fields = ["content"]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(News, NewsAdmin)
