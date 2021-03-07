from django.urls import path, include
from user import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('create_profile', views.create_profile, name="create_profile"),
    path('read_profile', views.read_profile, name="read_profile"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('delete_profile', views.delete_profile, name="delete_profile"),
    path('admin', views.admin, name="delete_profile"),

]
