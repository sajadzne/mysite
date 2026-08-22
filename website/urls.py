
from django.urls import path
from website.views import *

urlpatterns = [
    path('', index_View),
    path('about', about_View),
    path('contact', contact_View)
]