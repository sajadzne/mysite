from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def index_View(request):
    return render(request,'website/index.html')


def about_View(request):
    return render(request, 'website/about.html')


def contact_View(request):
    return render(request, 'website/contact.html')
