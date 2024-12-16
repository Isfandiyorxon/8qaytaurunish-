from django.contrib import admin
from django.urls import path
from .views import home,lesson_detail,lesson_to_curse

urlpatterns = [
    path('', home,name='home'),
    path('darslar/<int:pk>/', lesson_detail, name='lesson_detail'),
    path('course/<int:pk>/',lesson_to_curse,name='lesson_to_curse')
]