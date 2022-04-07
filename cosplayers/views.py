from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CospBlog
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


class MainPage(ListView):
    model = CospBlog
    template_name = 'mainpage.html'

class PostArticle(DetailView):
    model = CospBlog
    template_name = 'post_article.html'


