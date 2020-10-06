from django.shortcuts import render, HttpResponse
from services.models import Wordpress_comment, Html_Css_Javascript, PythonandDjango

# Ceate your views here.
def index(request):
    context = {
        "title": "Serives of tech atharva",
        "nav_title": "Tech atharva",
        "main": "Serives of tech atharva",
    }
    return render(request, "services.html", context)


def wordpress(request):
    email = request.POST.get("email")
    message = request.POST.get("message")
    comment = Wordpress_comment(email=email, massage=message)

    data = Wordpress_comment.objects.all()

    if request.method == "POST":
        comment.save()

    context = {
        "title": "Wordpress | serives of tech atharva",
        "nav_title": "Tech atharva",
        "main": "Wordpress | serives of tech atharva",
        "data": data,
    }
    return render(request, "wordpress.html", context)


def Html(request):
    email = request.POST.get("email")
    message = request.POST.get("message")
    comment = Html_Css_Javascript(email=email, massage=message)

    data = Html_Css_Javascript.objects.all()

    if request.method == "POST":
        comment.save()

    context = {
        "title": "Html Css and javascript static website | serives of tech atharva",
        "nav_title": "Tech atharva",
        "main": "Html Css and javascript static website | serives of tech atharva",
        "data": data,
    }
    return render(request, "HtmlCss.html", context)


def Python_Django(request):
    email = request.POST.get("email")
    message = request.POST.get("message")
    comment = PythonandDjango(email=email, massage=message)

    data = PythonandDjango.objects.all()

    if request.method == "POST":
        comment.save()

    context = {
        "title": "Python Django Dynamic website | serives of tech atharva",
        "nav_title": "Tech atharva",
        "main": "Python Django Dynamic website | serives of tech atharva",
        "data": data,
    }
    return render(request, "Django_python.html", context)
