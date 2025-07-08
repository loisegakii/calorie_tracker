from django.urls import path
from . import views

urlpatterns = [
    path('', views.calorie_tracker, name='tracker'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('reset/', views.reset_items, name='reset_items'),
]
