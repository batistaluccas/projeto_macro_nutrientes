from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'counter/pages/home.html')

# Create your views here.
