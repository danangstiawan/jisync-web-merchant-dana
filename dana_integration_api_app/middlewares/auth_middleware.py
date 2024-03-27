from django.shortcuts import redirect
from ..utils import construct_response
from http import HTTPStatus


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/home/") and not request.session.get("user_id"):
            return redirect(
                "/login"
            )  # Redirect to login page if user_id is not in session
        elif request.path.startswith("/api/") and not request.session.get("user_id"):
            return construct_response(
                None,
                HTTPStatus.UNAUTHORIZED,
                msg="You are not logged in",
            )
        response = self.get_response(request)
        return response
