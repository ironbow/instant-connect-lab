from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('meeting/', views.meeting, name='meeting'),
    path('add_device/', views.add_device, name='add_device'),
    path('add_controlhub/', views.add_controlhub, name='add_controlhub'),
    
]