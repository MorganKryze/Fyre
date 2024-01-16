from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def analytics(request):
    return render(request, "analytics.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
