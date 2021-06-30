from django.shortcuts import render
from django.http import HttpResponse

def manager_index(request):
# return HttpResponse("<h2>This is my manager page... </h2>")
# Create your views here.
    return render(request , 'managerOrg/manager_index.html')

def employee_policy_review(request):
    return render(request , 'managerOrg/employee_policy_review.html')
