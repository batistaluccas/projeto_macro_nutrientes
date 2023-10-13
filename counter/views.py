from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'counter/home.html')

# Create your views here.
