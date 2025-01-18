from django.contrib import admin
from .models import employees, posting
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget


class employeesResource(resources.ModelResource):

    class Meta:

        model = employees


class employeesAdmin(ImportExportModelAdmin):
    resource_class = employeesResource
    list_display = [
        "guid",
        "inn",
        "surname",
        "nameK",
        "fatherly",
        "info",
        "name",
        "bankcard",
        "info2",
        "info3",
        "info4",
        "firma",
        "email",
        "phone_number",
    ]
    search_fields = [
        "guid",
        "inn",
        "surname",
        "nameK",
        "fatherly",
        "info",
        "name",
        "bankcard",
        "email",
        "phone_number",
    ]


admin.site.register(employees, employeesAdmin)


class postingResource(resources.ModelResource):

    class Meta:

        model = posting


class postingAdmin(ImportExportModelAdmin):
    resource_class = postingResource
    list_display = [
        "guid",
        "suma",
        "quantity",
        "sub1dt",
        "sub1kt",
        "info",
        "accdt",
        "acckt",
        "dat",
    ]
    search_fields = [
        "guid",
        "suma",
        "quantity",
        "sub1dt",
        "sub1kt",
        "info",
        "accdt",
        "acckt",
        "dat",
    ]


admin.site.register(posting, postingAdmin)
