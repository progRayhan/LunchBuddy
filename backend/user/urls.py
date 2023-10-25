from django.urls import path

from .views.create_employee import AdminCreateEmployeeView
from .views.user_login import LoginView

urlpatterns = [
    # http://0.0.0.0:8023/api/v1/user/login/
    path(
        route="login/",
        view=LoginView.as_view(),
        name="admin_login",
    ),
    # http://0.0.0.0:8023/api/v1/user/admin/employee-create/
    path(
        route="admin/employee-create/",
        view=AdminCreateEmployeeView.as_view(),
        name="admin_employee_create",
    ),
]
