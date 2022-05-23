from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CospBlog, Category, Event
from django.urls import reverse_lazy, reverse
import random
from .forms import *
from django.http import HttpResponseRedirect
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

def FavouriteView(request, pk):
    cospblog = get_object_or_404(CospBlog, id = request.POST.get('fav_id'))
    is_fav = False
    if cospblog.favourite.filter(id=request.user.id).exists():
        cospblog.favourite.remove(request.user)
        is_fav = False
    else:
        cospblog.favourite.add(request.user)
        is_fav=True
    return HttpResponseRedirect(reverse('postarticle', args = [str(pk)]))


def LikeView(request, pk):
    cospblog = get_object_or_404(CospBlog, id = request.POST.get('post_id'))
    liked=False
    if cospblog.like.filter(id=request.user.id).exists():
        cospblog.like.remove(request.user)
        liked = False
    else:
        cospblog.like.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('postarticle', args = [str(pk)]))



class MainPage(ListView):
    model = CospBlog
    template_name = 'mainpage.html'
    queryset = CospBlog.objects.order_by('-like')[:4]

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(MainPage, self).get_context_data(*args, **kwargs)
        context ["cat_menu"] =  cat_menu
        return context

###########################################################################################

class EventsPage(ListView):
    model = Event
    template_name = 'event.html'
    queryset = Event.objects.order_by('-i_am_going')[:3]

class EventDetails(DetailView):
    model = Event
    template_name = 'event_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super( EventDetails, self).get_context_data( **kwargs)
        stuff = get_object_or_404(Event, id=self.kwargs['pk'])
        total_goings= stuff.total_goings()

        goings = False
        if stuff.i_am_going.filter(id=self.request.user.id).exists():
            goings = True

        context["total_goings"] = total_goings
        context["goings"] = goings
        return context

def GoingView(request, pk):
    event = get_object_or_404(Event, id = request.POST.get('going_id'))
    goings=False
    if event.i_am_going.filter(id=request.user.id).exists():
        event.i_am_going.remove(request.user)
        goings = False
    else:
        event.i_am_going.add(request.user)
        goings=True
    return HttpResponseRedirect(reverse('eventdetails', args = [str(pk)]))




class AddEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event_add.html'


class UpdateEventView(UpdateView):
    model = Event
    template_name = 'edit_event.html'
    fields = ['name', 'event_date', 'place', 'description', 'event_image']

class DeleteEventView(DeleteView):
    model = Event
    template_name = 'delete_event.html'
    success_url = reverse_lazy('mainpage')

############################################################################################
class PostArticle(DetailView):
    model = CospBlog
    template_name = 'post_article.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super( PostArticle, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    def get_context_data(self,*args, **kwargs):
        context = super(PostArticle, self).get_context_data( **kwargs)

        get_ids = get_object_or_404(CospBlog, id = self.kwargs['pk'])
        total_likes = get_ids.total_likes()
        get_favourites = get_object_or_404(CospBlog, id = self.kwargs['pk'])


        is_fav = False
        if get_favourites.favourite.filter(id=self.request.user.id).exists():
            is_fav = True
        context["is_fav"] = is_fav


#########################

#########################
        liked  =  False
        if get_ids.like.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context



class AddPostView(CreateView):
    model = CospBlog
    form_class = CospBlogForm
    template_name = 'add_blog.html'


class UpdatePostView(UpdateView):
    model = CospBlog
    template_name = 'edit_blog.html'
    fields = ['post_title', 'your_post', 'post_image']

class DeletePostView(DeleteView):
    model = CospBlog
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('mainpage')



def CategoryView(request, cats):
    category_posts = CospBlog.objects.filter(category = cats)
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts': category_posts})



def CategoryMenuView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_menu.html', {'cat_menu_list': cat_menu_list})



def post_favourite_list(request):
    user = request.user
    favourite_lists = user.favourite.all()
    context = {
        'favourite_lists' : favourite_lists
    }
    return render(request, 'favourite_lists.html', context)












titlesforgame= [
    "naruto","hinata","eren","mikasa","armin","jojo","yagami","itachi","saitama","kaneki","gojo","natsu","yato","gintama","killua","bakugo",
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

    if msg == 5:
        failure = "You beat 5! \n Game Restarted"
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
