from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# Create your views here.
def homepage(request):
    return render(request, 'index.html')

@login_required()
def customer(request):
    return render(request, 'index.html')

@login_required()
def courier(request):
    return render(request, 'index.html')
