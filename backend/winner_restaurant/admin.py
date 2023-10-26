from django.contrib import admin

from .models import WinnerRestaurantModel


class WinnerRestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "restaurant",
    )
    list_display_links = ("restaurant",)
    list_per_page = 25


admin.site.register(WinnerRestaurantModel, WinnerRestaurantAdmin)
