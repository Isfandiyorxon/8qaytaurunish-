from django.contrib import admin
from django.urls import path
from .views import home,lesson_detail,lesson_to_curse,add_lesson

urlpatterns = [
    path('', home,name='home'),
    path('darslar/<int:pk>/', lesson_detail, name='lesson_detail'),
    path('course/<int:pk>/',lesson_to_curse,name='lesson_to_curse'),
    path('add_leson/',add_lesson,name='add_leson'),
]