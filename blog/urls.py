from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('delete/<int:blog_id>', views.delete, name='delete'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
]
