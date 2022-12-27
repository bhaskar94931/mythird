from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def third(request):
    return HttpResponse('django is a framework of python')
def fourth(request):
    return HttpResponse('Navya is good girl')
