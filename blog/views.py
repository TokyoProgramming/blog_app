from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'pages/home-page.html')



def post(request):
    return render(request, 'pages/post-page.html')


def category(request):
    return render(request, 'pages/category-page.html')

