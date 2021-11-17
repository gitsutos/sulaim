from django.urls import path
from . import views

urlpatterns = [
  path('add_item/',views.index),
  path('add_todo/', views.AddDo),
  path('', views.empty),
  path('delete_todo/<int:todo_id>', views.delete_todo),
  path('Cost_of_month/',views.cost_of_year)
]