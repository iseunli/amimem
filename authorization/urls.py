from django.urls import path
from .views import UserRegistration, UserEdit

urlpatterns = [
    path('registration/', UserRegistration.as_view(), name = "registration"),
path('edit_profile/', UserEdit.as_view(), name = "edit_profile"),

]
