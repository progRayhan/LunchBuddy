from django.contrib import admin

from .models import VoteModel


class VoteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "menu",
        "vote",
        "employee_phone_number",
    )
    list_display_links = ("employee_phone_number",)
    search_fields = ("employee_phone_number",)
    list_per_page = 25


admin.site.register(VoteModel, VoteAdmin)
