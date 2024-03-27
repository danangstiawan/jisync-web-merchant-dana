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
    path(
        "user/<int:user_id>",
        user_api.user_id,
        name="user_id",
    ),
]
