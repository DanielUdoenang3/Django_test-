from django.urls import path
from hello import views

urlpatterns = [
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),


    path("", views.home, name="home"),
]
