from django.shortcuts import render
from django.http import HttpResponse

def authentication_index(request):
    return render(request , 'authLogin/authentication_index.html')

