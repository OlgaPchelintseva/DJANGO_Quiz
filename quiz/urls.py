from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start_quiz'),
    path('quiz/', views.questions, name='quiz'),
    path('quiz/result/', views.result, name='result_quiz'),
]