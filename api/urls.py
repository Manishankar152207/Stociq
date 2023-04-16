from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('check-client/', views.check_client, name='check-client'),
    path('executed-order/', views.executed_order, name='executed-order'),
    path('get-order/', views.get_order, name='get-order'),
    path('live-ip/', views.live_ip, name='live-ip'),
    path('logout/', views.logout, name='logout'),
]
