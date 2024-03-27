from django.shortcuts import render
from .controller.user_controller import User_Controller



def home(req):

    return render(
        req,
        "home.html",
    )


def login(req):
    if req.method == "POST":
        login_data = dict(req.POST.items())
        resp = User_Controller.login(
            req,
            email=login_data["email"],
            password=login_data["password"],
        )

        return resp
    return render(req, "login.html")


def users(req):
    # users = User_Controller.get_all_user()
    # print(users)
    return render(req, "users.html")


def report(req):
    return render(req, "report.html")


def register(req):
    if req.method == "POST":
        user_data = dict(req.POST.items())
        return User_Controller.register(user_data)

    return render(req, "register.html")
