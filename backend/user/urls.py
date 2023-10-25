from django.urls import path

from .views.user_login import LoginView

urlpatterns = [
    # http://0.0.0.0:8023/api/v1/user/login/
    path(
        route="login/",
        view=LoginView.as_view(),
        name="admin_login",
    )
]
