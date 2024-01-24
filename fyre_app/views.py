from django.shortcuts import render
import os
from django.conf import settings


def index(request):
    return render(request, "index.html")


def analytics(request):
    return render(request, "pages/analytics.html")


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")


def terms(request):
    return render(request, "pages/terms.html")


def privacy(request):
    return render(request, "pages/privacy.html")


def analytics2019(request):
    with open(os.path.join(settings.BASE_DIR, 'assets/plots/2019/first.html'), 'r') as f:
        first_plot = f.read()
    with open(os.path.join(settings.BASE_DIR, 'assets/plots/2019/second.html'), 'r') as f:
        second_plot = f.read()
    return render(request, "pages/analytics/2019.html", {'first_plot': first_plot, 'second_plot': second_plot})


def analytics2020(request):

    return render(request, "pages/analytics/2020.html")


def analytics2021(request):

    return render(request, "pages/analytics/2021.html")


def analytics2022(request):
    return render(request, "pages/analytics/2022.html")


def analytics_custom(request):

    return render(request, "pages/analytics/custom.html")
