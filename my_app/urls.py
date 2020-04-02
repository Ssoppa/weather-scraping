from django.urls import path
from .views import home, contact, about, new_search

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('new_search', new_search, name='new_search')
]
