from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from Insta.forms import CustomUserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class MyView(TemplateView):
    template_name = 'home.html'


# return a self.object_list to html file, a list of views
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
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    # require users to provide -- field
    fields = '__all__'
    login_url = 'login'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']


class PostDeleteView(DeleteView):
    model = Post
    # 'model' has been pasted to html template as object
    template_name = 'post_delete.html'
    # the return page after deletion
    success_url = reverse_lazy("posts")


# users sign up view
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")
