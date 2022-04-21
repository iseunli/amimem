#home
from django.urls import path
from .views import MainPage, PostArticle, AddPostView, UpdatePostView, DeletePostView
from . import views

urlpatterns = [
    path('', MainPage.as_view(), name = "mainpage"),
    path('post/<int:pk>', PostArticle.as_view(), name = "postarticle"),
    path('/jumbblegame', views.jumbbledgame, name = "jumgame"),
    path('/check', views.checkans, name="check"),
    path('/quiz', views.quizz, name="quiz"),
    path('/tests', views.tests, name="test"),
    path('/test1', views.test1, name="test1"),
    path('/test2', views.test2, name="test2"),
    path('/test3', views.test3, name="test3"),
    path('create_post/', AddPostView.as_view(), name = "create_post"),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="edit_post"),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name="delete_post"),

]
