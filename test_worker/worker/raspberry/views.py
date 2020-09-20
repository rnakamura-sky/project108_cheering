from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def run(request):
    # return HttpResponse('Hello world!')
    data = {
        'State': 'Success'
    }
    return JsonResponse(data)
