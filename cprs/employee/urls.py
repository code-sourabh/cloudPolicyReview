
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.employee_index , name="employee_index"),
    path('employee_index.html/' , views.employee_index , name="employee_index")
]