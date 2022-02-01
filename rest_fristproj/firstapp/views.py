from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from firstapp.models import empModel

# Create your views here.

def employeeView(request):
    # emp = {
    #     'ID' : 1,
    #     'Name' : 'Joann',
    #     'location' : 'London',
    #     'Salary' : 1000000
    # }

    data = empModel.objects.all();
    response = {
        'employees' : list(data.values('id', 'name', 'location', 'salary'))
    }

    return JsonResponse(response)
