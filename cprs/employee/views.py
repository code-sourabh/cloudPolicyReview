from django.shortcuts import render
from django.http import HttpResponse

def employee_index(request):
# return HttpResponse("<h2>this is page for an employee</h2>")

    return render(request , 'employee/employee_index.html')
