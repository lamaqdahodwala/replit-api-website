from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'index.html')

def search(req):
    return render(req, 'search.html')