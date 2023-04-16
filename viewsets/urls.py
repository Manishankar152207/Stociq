from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from viewsets import views

router = DefaultRouter()
router.register('viewsets', views.ViewSetApi, basename='viewsets')


urlpatterns = router.urls
