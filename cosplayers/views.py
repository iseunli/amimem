from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CospBlog

class MainPage(ListView):
    model = CospBlog
    template_name = 'mainpage.html'

class PostArticle(DetailView):
    model = CospBlog
    template_name = 'post_article.html'