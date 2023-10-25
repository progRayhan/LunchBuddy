from django.urls import path

from restaurant.views.create_restaurant import AdminCreateRestaurantView

urlpatterns = [
    # http://0.0.0.0:8023/api/v1/restaurant/admin/create/
    path(
        route="admin/create/",
        view=AdminCreateRestaurantView.as_view(),
        name="admin_restaurant_create",
    )
]
