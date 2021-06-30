from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.manager_index , name='manager_index'),
    path('employee_policy_review.html/' , views.employee_policy_review , name='employee_policy_review')
]
