from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserChangeForm

class RegisterView(generic.FormView):
    template_name = "users/register.html"
    form_class = UserChangeForm
    success_url = reverse_lazy("login")

