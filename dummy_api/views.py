from django.shortcuts import render,redirect
from .models import Employee
from django.http import HttpResponse,FileResponse,Http404,HttpResponseRedirect,JsonResponse

# Create your views here.

def ping(request):
    data={'status':200}
    return JsonResponse(data)

