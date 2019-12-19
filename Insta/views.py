from annoying.decorators import ajax_request
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from Insta.forms import CustomUserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Like, InstaUser, UserConnection


class MyView(TemplateView):
    template_name = 'home.html'


# return a self.object_list to html file, a list of views
class PostsView(ListView):
    # set the model to be post
    model = Post
    # set the template (showing html) to be ...
    template_name = 'index.html'

    # # filter, use this function as query, default to return all the post object -- return post.objects
    # def get_queryset(self):
    #     current_user = self.request.user
    #     following = set()
    #     for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
    #         following.add(conn.following)
    #     return Post.objects.filter(author__in=following)


# return a self.object to html file
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class UserDetailView(DeleteView):
    model = InstaUser
    template_name = 'user_detail.html'


# return a "form" to html file
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    # require users to provide -- field
    fields = '__all__'
    # require to login in order to make a post
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


# function based view
# response to ajax request
@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    # get post where user clicked
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        # save the object to database
        like.save()
        result = 1
    # if the user has already liked, like.save() give error
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }

# TODO follow / unfollow: add ajax
# TODO make comments: updateview
# TODO update profile
