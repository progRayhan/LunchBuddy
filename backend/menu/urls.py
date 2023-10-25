from django.urls import path

from menu.views.current_day_menu import CurrentDayMenuView
from menu.views.upload_menu import UploadMenuView

urlpatterns = [
    # http://0.0.0.0:8023/api/v1/menu/admin/upload-menu/
    path(
        route="admin/upload-menu/",
        view=UploadMenuView.as_view(),
        name="upload_menu_for_restaurants",
    ),
    # http://0.0.0.0:8023/api/v1/menu/current-day-menu/
    path(
        route="current-day-menu/",
        view=CurrentDayMenuView.as_view(),
        name="current_day_menu",
    ),
]
