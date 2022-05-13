from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import EditAccountForm
class UserRegistration(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEdit(generic.UpdateView):
    form_class = EditAccountForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('mainpage')

    def get_object(self):
        return self.request.user

