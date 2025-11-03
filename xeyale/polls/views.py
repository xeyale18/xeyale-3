from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Salam Xəyalə! Bu, sənin ilk Django səhifəndir 💫")
