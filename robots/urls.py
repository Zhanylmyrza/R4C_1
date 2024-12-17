from django.urls import path
from .views import robot_create, generate_production_report

urlpatterns = [
    path('create/', robot_create, name='robot-create'),
    path('production-report/', generate_production_report, name='production_report'),
]