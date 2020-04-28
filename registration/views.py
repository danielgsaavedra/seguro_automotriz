from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator


class LoginPageView(TemplateView):
    template_name = "registration/login.html"


class RegisterPageView(TemplateView):
    template_name = "registration/registro.html"
