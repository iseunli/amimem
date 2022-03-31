#home
from django.urls import path
from .views import MainPage, PostArticle

urlpatterns = [
    path('', MainPage.as_view(), name = "mainpage"),
    path('post/<int:pk>', PostArticle.as_view(), name = "postarticle")
]
