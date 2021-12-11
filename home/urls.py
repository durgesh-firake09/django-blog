"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about-us/", views.about, name='about'),
    path("contact-us/", views.contact, name='contact'),
    path("posts/", views.browsePosts, name='posts'),
    path("user/sign-up/", views.signUp, name='signUp'),
    path("user/login/", views.login, name='login'),
    path("user/reset-password/", views.resetPassword, name='resetPassword'),
    path("posts/<int:sno>/", views.viewPost, name='resetPassword'),
]
