from django.urls import path
from .views import error_500_view
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("analytics/", views.analytics, name="analytics"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('test-500/', error_500_view),
]