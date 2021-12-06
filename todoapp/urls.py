from django.urls import path
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path('add_item/', index),
    path('home/', home_view),
    path('add_todo/', add_cost),
    path('delete_todo/<int:todo_id>', delete_todo),
    path('Cost_of_month/', cost_of_year),
    path('list_view_of_costs/', list_view_of_costs),
    path('', RedirectView.as_view(url='home/')),
    path('is_auth_or_no/', is_auth_or_no)
]
