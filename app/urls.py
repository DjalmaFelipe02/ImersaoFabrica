from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('new', views.register_student, name='register_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('',views.student_page, name='student_filters'),
]
