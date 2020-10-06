from django.shortcuts import render
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        "title": "tech atharva - The boy he knows web devolepment",
        "nav_title": "Tech atharva",
        "main": "Tech Atharva",
    }
    return render(request, "index.html", context)


def about(request):
    context = {
        "title": "About | tech atharva",
        "nav_title": "Tech atharva",
        "main": "About Tech atharva",
    }
    return render(request, "about.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        massage = request.POST.get("massage")
        contact = Contact(name=name, email=email, phone=phone, massage=massage)
        contact.save()

    context = {
        "title": "contact Us",
        "nav_title": "Tech atharva",
        "main": "Contact to Tech atharva",
    }
    return render(request, "contact.html", context)
