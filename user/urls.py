from django.contrib import admin
from django.urls import path, include
from . import views

from django.urls import path, include
from user import views

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
    
=======

>>>>>>> product
=======
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('dashboard', views.dashboard, name="register"),

    path('create_profile', views.create_profile, name="create_profile"),
    path('read_profile', views.read_profile, name="read_profile"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('delete_profile', views.delete_profile, name="delete_profile"),
    path('admin', views.admin, name="delete_profile"),

>>>>>>> 61962f376e9d0c8880e99283078671bb43876d10
]
