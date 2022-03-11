from django.shortcuts import render,redirect
from django.urls import path 
from . import views

# Create your tests here..
urlpatterns = [
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("contacts",views.contacts,name="contacts"),
    path("test",views.test,name="test"),
    path("products",views.products,name="products"),
    path("story",views.story,name="story"),
    path("services",views.services,name="services"),
    path("setcookie",views.setcookie,name="setcookie"),
    path("getcookie",views.getcookie,name="getcookie"),
    path("forms",views.forms,name="forms"),
]
