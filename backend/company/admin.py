from django.contrib import admin

from .models import CompanyModel


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company_id",
        "company_name",
        "phone_number",
        "is_active",
    )
    list_display_links = (
        "company_id",
        "company_name",
        "phone_number",
    )
    search_fields = (
        "company_id",
        "company_name",
        "phone_number",
    )
    list_per_page = 25


admin.site.register(CompanyModel, CompanyAdmin)
