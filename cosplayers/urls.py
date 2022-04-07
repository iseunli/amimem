#home
from django.urls import path
from .views import MainPage, PostArticle
from . import views

urlpatterns = [
    path('', MainPage.as_view(), name = "mainpage"),
    path('post/<int:pk>', PostArticle.as_view(), name = "postarticle"),
    path('/jumbblegame', views.jumbbledgame, name = "jumgame"),
    path('/check', views.checkans, name="check"),

   ]
