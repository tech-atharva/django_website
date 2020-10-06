from django.contrib import admin
from django.urls import path
from services import views

urlpatterns = [path("", views.index), path('wordpress/', views.wordpress), path('HtmlCssandJavascript/', views.Html), path("pythonDjango/", views.Python_Django)]
