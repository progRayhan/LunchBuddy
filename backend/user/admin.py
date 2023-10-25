from django.contrib import admin

from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone_number",
        "email",
        "user_type",
        "first_name",
        "last_name",
        "employee_id",
        "company",
        "company_phone_number",
        "position",
        "gender",
    )
    list_display_links = (
        "phone_number",
        "email",
        "employee_id",
    )
    search_fields = (
        "phone_number",
        "email",
        "employee_id",
    )
    list_per_page = 25


admin.site.register(UserAccount, UserAccountAdmin)
