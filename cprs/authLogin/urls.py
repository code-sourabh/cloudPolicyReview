from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.authentication_index , name='authentication_index'),
    path('manager/' , include('managerOrg.urls') ),
    path('employee/' , include('employee.urls')),
    path('administrator/' , include('administratorView.urls'))

]