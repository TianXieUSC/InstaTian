from django.shortcuts import render
from django.views.generic import TemplateView


class MyView(TemplateView):
    template_name = 'home.html'
