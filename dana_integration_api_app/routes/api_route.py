from django.urls import path
from ..api import user_api

urlpatterns = [
    path(
        "users",
        user_api.users,
        name="users",
    ),
    path(
        "user",
        user_api.user,
        name="user",
    ),
]
