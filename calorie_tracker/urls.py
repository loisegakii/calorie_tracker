from django.urls import path
from . import views

urlpatterns = [
    path('', views.calorie_tracker, name='tracker'),
]
