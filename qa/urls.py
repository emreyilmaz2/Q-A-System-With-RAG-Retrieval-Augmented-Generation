from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ana sayfa için görünüm
    path('ask-question/', views.ask_question, name='ask_question'),  # Soru sorma sayfası
]
