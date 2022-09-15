from django.urls import path
from app import views

urlpatterns = [
    path('', views.test),
    path('template/', views.home)
]
