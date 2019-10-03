# __author__ == "Priya"

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_input, name='get_input'),
    path('<str:room_name>/', views.room, name='room'),
]