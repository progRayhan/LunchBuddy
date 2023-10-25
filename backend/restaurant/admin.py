from django.contrib import admin

from .models import RestaurantModel


class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "restaurant_id",
        "restaurant_name",
        "phone_number",
        "website",
        "opening_hour",
        "closing_hour",
    )
    list_display_links = (
        "restaurant_id",
        "restaurant_name",
        "phone_number",
        "website",
    )
    search_fields = (
        "restaurant_id",
        "restaurant_name",
        "phone_number",
    )
    list_per_page = 25


admin.site.register(RestaurantModel, RestaurantAdmin)
