from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    testlist=testInfo.objects.all()
    return render(request,'say/index.html',{'testlist':testlist})
def testpost(request):
    return render(request,'say/testpost1.html')

def json1(request):
    return render(request,'say/json1.html')

def json2(request):
    return JsonResponse({'h1':'hello','h2':'world'})

