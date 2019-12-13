from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post


class MyView(TemplateView):
    template_name = 'home.html'


class PostsView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
