from django.urls import path
from .views import *

urlpatterns = [
  path('add_item/',index),
  path('add_todo/',add_cost),
  path('', empty),
  path('delete_todo/<int:todo_id>', delete_todo),
  path('Cost_of_month/',cost_of_year),
  path('login',login),
]