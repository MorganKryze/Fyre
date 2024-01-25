from django.shortcuts import render


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


# 2019
def analytics_2019_residences(request):
    return render(request, "pages/analytics/2019/residences.html")


def analytics_2019_buisness(request):
    return render(request, "pages/analytics/2019/buisness.html")


def analytics_2019_general(request):
    return render(request, "pages/analytics/2019/general.html")


# 2020
def analytics_2020_residences(request):
    return render(request, "pages/analytics/2020/residences.html")


def analytics_2020_buisness(request):
    return render(request, "pages/analytics/2020/buisness.html")


def analytics_2020_general(request):
    return render(request, "pages/analytics/2020/general.html")


# 2021
def analytics_2021_residences(request):
    return render(request, "pages/analytics/2021/residences.html")


def analytics_2021_buisness(request):
    return render(request, "pages/analytics/2021/buisness.html")


def analytics_2021_general(request):
    return render(request, "pages/analytics/2021/general.html")


# 2022
def analytics_2022_residences(request):
    return render(request, "pages/analytics/2022/residences.html")


def analytics_2022_buisness(request):
    return render(request, "pages/analytics/2022/buisness.html")


def analytics_2022_general(request):
    return render(request, "pages/analytics/2022/general.html")


def analytics_custom(request):
    return render(request, "pages/analytics/custom.html")
