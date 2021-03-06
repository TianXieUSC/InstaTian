"""InstaTian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# We can create "urls.py" for each App and use this method to manage all the urls.
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Insta.views import MyView, PostsView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, addLike, \
    UserDetailView, toggleFollow, EditProfile, addComment, ExploreView

urlpatterns = [
    path('myview', MyView.as_view(), name='my_view'),
    path('', PostsView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='make_post'),
    path('posts/update/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
    path('posts/delete/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
    path('like', addLike, name='addLike'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('togglefollow', toggleFollow, name='togglefollow'),
    path('user/<int:pk>/edit_profile', EditProfile.as_view(), name='edit_profile'),
    path('comment', addComment, name='addComment'),
    path('explore', ExploreView.as_view(), name='explore'),
]
