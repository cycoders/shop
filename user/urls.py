from django.urls import path
from user import views

urlpatterns = [
    path('profile', views.create_profile, name="create_profile"),
    path('profile', views.read_profile, name="read_profile"),
    path('profile', views.update_profile, name="update_profile"),
    path('profile', views.delete_profile, name="delete_profile"),

]
