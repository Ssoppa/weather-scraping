from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'my_app/index.html')


def contact(request):
    return render(request, 'my_app/contact.html')


def about(request):
    return render(request, 'my_app/about.html')


def new_search(request):
    return render(request, 'my_app/about.html')
