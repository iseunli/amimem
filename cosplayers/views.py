from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CospBlog
from django.urls import reverse_lazy
import random




titlesforgame= [
    "naruto",
    "hinata",
    "eren",
    "mikasa",
    "armin",
    "jojo",
    "yagami",
    "itachi",
    "saitama",
    "kaneki",
    "gojo",
    "natsu",
    "yato",
    "gintama",
    "killua",
    "bakugo",
]

def randomtitle():
    global jword
    global rantitle
    rantitle = random.choice(titlesforgame)
    jum = random.sample(rantitle, len(rantitle))
    jword = "".join(jum)

msg = 0
failure =""
def jumbbledgame(request):
    randomtitle()
    global jword, msg
    return render(request, 'game.html',
                  {'jum_word': jword,
                   'msg': msg})

def checkans(request):
    global rantitle, msg, jword, failure
    user_answer = request.GET['answer']

    if user_answer.lower().strip() == rantitle:
        msg += 1
        jumbbledgame(request)
    else:
        msg = 0
        jumbbledgame(request)

    if msg == 10:
        failure = "You beat 10! \n Game Restarted"
        msg=0
    else:
        failure =""

    return render(request, 'game.html', {'jum_word': jword,
                   'msg': msg,
                    'failure': failure})

def quizz (request):
    return render(request, 'quiz.html')




def tests(request):
    return render(request, 'tests.html')
def test1(request):
    return render(request, 'test1.html')
def test2(request):
    return render(request, 'test2.html')
def test3(request):
    return render(request, 'test3.html')

class MainPage(ListView):
    model = CospBlog
    template_name = 'mainpage.html'
    ordering = [ '-id']

class PostArticle(DetailView):
    model = CospBlog
    template_name = 'post_article.html'

class AddPostView(CreateView):
    model = CospBlog
    template_name = 'add_blog.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = CospBlog
    template_name = 'edit_blog.html'
    fields = ['post_title', 'your_post']

class DeletePostView(DeleteView):
    model = CospBlog
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('mainpage')
