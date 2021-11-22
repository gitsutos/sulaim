from django.urls import path
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
  path('add_item/',index),
  path('add_todo/',add_cost),
  path('delete_todo/<int:todo_id>', delete_todo),
  path('Cost_of_month/', cost_of_year),
  path('login', login),
  path('list_view_of_costs', list_view_of_costs),
  path('', RedirectView.as_view(url='/add_item')),
]