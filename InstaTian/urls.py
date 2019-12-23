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

from Insta.views import SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    # third way to add the url path, continue to app 'insta' url path
    path('insta/', include('Insta.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    # manually define the sign up view
    path('auth/signup/', SignUp.as_view(), name='signup'),
]

