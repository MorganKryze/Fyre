from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("analytics/", views.analytics, name="analytics"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("analytics/2019/", views.analytics2019, name="analytics_2019"),
    path("analytics/2020/", views.analytics2020, name="analytics_2020"),
    path("analytics/2021/", views.analytics2021, name="analytics_2021"),
    path("analytics/2022/", views.analytics2022, name="analytics_2022"),
    path("analytics/custom/", views.analytics_custom, name="analytics_custom"),
]