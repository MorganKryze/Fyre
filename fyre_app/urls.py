from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("analytics/", views.analytics, name="analytics"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("analytics/2019/residences/", views.analytics_2019_residences, name="analytics_2019_residences"),
    path("analytics/2019/buisness/", views.analytics_2019_buisness, name="analytics_2019_buisness"),
    path("analytics/2019/general/", views.analytics_2019_general, name="analytics_2019_general"),
    path("analytics/2020/", views.analytics2020, name="analytics_2020"),
    path("analytics/2021/", views.analytics2021, name="analytics_2021"),
    path("analytics/2022/", views.analytics2022, name="analytics_2022"),
    path("analytics/custom/", views.analytics_custom, name="analytics_custom"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)