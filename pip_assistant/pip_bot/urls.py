# __author__ == "Priya"

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('get-response/', views.get_output)
    #path('<str:room_name>/', views.room, name='room'),
]