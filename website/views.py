from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def index_View(request):
    return HttpResponse('<h1>Home page</h1>')

def about_View(request):
    return HttpResponse('<h1>About page</h1>')

def contact_View(request):
    return HttpResponse('<h1>Contact page</h1>')
