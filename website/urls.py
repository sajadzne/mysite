
from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_View, name='index'),
    path('about', about_View, name='about'),
    path('contact', contact_View, name='contact'),
    path('blog', blog_View, name='blog'),
]