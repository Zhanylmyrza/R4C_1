from django.urls import path
from .views import robot_create

urlpatterns = [
    path('create/', robot_create, name='robot-create'),
]