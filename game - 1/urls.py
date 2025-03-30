from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login.html", views.login, name="login"),
    path("game.html", views.game, name="game"),
    path("home.html", views.logout, name="logout")
]