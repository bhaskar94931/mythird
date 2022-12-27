from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('bhaskar is learning django')
def second(request):
    return HttpResponse('bhaskar is good boy')
def third(request):
    return HttpResponse('django is a framework of python')
