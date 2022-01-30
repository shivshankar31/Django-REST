from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def employeeView(request):
    emp = {
        'ID' : 1,
        'Name' : 'Joann',
        'location' : 'London',
        'Salary' : 1000000
    }

    return JsonResponse(emp)
