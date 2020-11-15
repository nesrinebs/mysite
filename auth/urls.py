from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('edit', views.edit_view, name='edit'),
    path('profiles', views.profiles_view, name='profiles'),
    url(r'^profiles/(?P<id>\d+)/edit/$', views.edit_view, name='edit'),

]
