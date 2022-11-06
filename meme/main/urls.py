from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"), # / route
    path("register/",views.register,name="register"), # Register route
    path("login/", views.login, name="login"), #Login Route
    path("logout/", views.logout, name="logout"),
    path("memes/", views.getmemes, name="memes")
]