from django.contrib import admin

from .models import MenuModel


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "item_id",
        "food_name",
        "price",
        "vote_count",
        "restaurant",
    )
    list_display_links = (
        "item_id",
        "food_name",
    )
    search_fields = (
        "item_id",
        "food_name",
    )
    list_per_page = 25


admin.site.register(MenuModel, MenuAdmin)
