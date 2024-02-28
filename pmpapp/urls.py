from django.urls import path

# for authentication for user login we will import views from django auth
from django.contrib.auth import views as auth_views
from . import views
from .import forms

app_name = 'pmpapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    # in this code we will use django authentication but will tell them to use on which form which 
    #in this case is our login form
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html',authentication_form = forms.LoginForm),name="login")
]
