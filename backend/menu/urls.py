from django.urls import path

from menu.views.upload_menu import UploadMenuView

urlpatterns = [
    # http://0.0.0.0:8023/api/v1/menu/admin/upload-menu/
    path(
        route="admin/upload-menu/",
        view=UploadMenuView.as_view(),
        name="upload_menu_for_restaurants",
    )
]
