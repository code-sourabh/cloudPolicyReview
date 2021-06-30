from django.shortcuts import render
from django.http import HttpResponse

def manager_index(request):
    return HttpResponse("<h2>This is my manager page... </h2>")
# Create your views here.
