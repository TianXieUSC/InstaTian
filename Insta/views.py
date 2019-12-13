from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Post


class MyView(TemplateView):
    template_name = 'home.html'

# return a self.object_list to html file
class PostsView(ListView):
    # set the model to be post
    model = Post
    # set the template (showing html) to be ...
    template_name = 'index.html'

# return a self.object to html file
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# return a "form" to html file
class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    # require users to provide -- field
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy("posts")


