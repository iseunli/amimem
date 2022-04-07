from django.urls import path
from .views import UserRegistration

urlpatterns = [
    path('registration/', UserRegistration.as_view(), name = "registration"),

]
