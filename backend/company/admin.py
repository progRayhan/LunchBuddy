from django.contrib import admin

from .models import CompanyModel


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company_id",
        "company_name",
        "is_active",
    )
    list_display_links = (
        "company_id",
        "company_name",
    )
    search_fields = (
        "company_id",
        "company_name",
    )
    list_per_page = 25


admin.site.register(CompanyModel, CompanyAdmin)
