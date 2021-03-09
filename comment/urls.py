from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index , name="comments"),
=======
    path('', views.render, name="comments")
>>>>>>> product
]
