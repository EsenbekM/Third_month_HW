from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('profile/', views.profile_view)
]