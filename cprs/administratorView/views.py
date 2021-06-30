from django.shortcuts import render 
from django.http import HttpResponse

def index(request):
    
# return HttpResponse("<h2>This is administrator page</h2>")
    return render(request , 'administratorView/administrator_index.html')
