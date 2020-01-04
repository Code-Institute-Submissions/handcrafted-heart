from django.shortcuts import render


# The views.

def index(request):
    """A view that display the index page"""
    return render(request, "index.html")