from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.


def home(req):
    # return HttpResponse('Hello World!')
    return render(
        req,
        "home.html",
    )


def todos(req):
    items = TodoItem.objects.all()
    return render(req, "todos.html", {"todos": items})


def login(req):
    return render(req, "login.html")
