from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('alltrades/', views.alltrades, name="alltrades"),
    path('todaytrades/', views.todaytrades, name="todaytrades"),
    path('clientlogs/', views.clientlogs, name="clientlogs"),
    path('adminusers/', views.adminusers, name="adminusers"),
]
