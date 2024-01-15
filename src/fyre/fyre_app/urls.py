from django.urls import path
# from django_distill import distill_path, distill_re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("analytics/", views.analytics, name="analytics"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    # distill_path("", views.index, name="index", distill_func=lambda: None),
    # distill_path("analytics/", views.analytics, name="analytics",  distill_func=lambda: None),
    # distill_path("about/", views.about, name="about", distill_func=lambda: None),
    # distill_path("contact/", views.contact, name="contact", distill_func=lambda: None),
]