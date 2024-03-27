from django.urls import path, include
from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path(
        "register",
        views.register,
        name="register",
    ),
    path("home/", include('dana_integration_api_app.routes.home_route')),
    path("api/", include('dana_integration_api_app.routes.api_route')),
    # path("users", views.users, name="users"),
]
