from django.shortcuts import render
import requests


def index(request):
        
        return render(request, 'index.html', {})


def about(request):
        return render(request, 'about.html', {})