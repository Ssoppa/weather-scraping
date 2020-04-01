from django.urls import path
from .views import home, contact, about, new_search

urlpatterns = [
    path('', home),
    path('contact', contact),
    path('about', about),
]
