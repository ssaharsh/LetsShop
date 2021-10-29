from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login',auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path('logout',auth_views.LogoutView.as_view(template_name="home.html"),name="logout"),
    path('register',views.register,name="register"),
]
