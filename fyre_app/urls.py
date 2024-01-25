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
    # 2019
    path(
        "analytics/2019/residences/",
        views.analytics_2019_residences,
        name="analytics_2019_residences",
    ),
    path(
        "analytics/2019/buisness/",
        views.analytics_2019_buisness,
        name="analytics_2019_buisness",
    ),
    path(
        "analytics/2019/general/",
        views.analytics_2019_general,
        name="analytics_2019_general",
    ),
    # 2020
    path(
        "analytics/2020/residences/",
        views.analytics_2020_residences,
        name="analytics_2020_residences",
    ),
    path(
        "analytics/2020/buisness/",
        views.analytics_2020_buisness,
        name="analytics_2020_buisness",
    ),
    path(
        "analytics/2020/general/",
        views.analytics_2020_general,
        name="analytics_2020_general",
    ),
    # 2021
    path(
        "analytics/2021/residences/",
        views.analytics_2021_residences,
        name="analytics_2021_residences",
    ),
    path(
        "analytics/2021/buisness/",
        views.analytics_2021_buisness,
        name="analytics_2021_buisness",
    ),
    path(
        "analytics/2021/general/",
        views.analytics_2021_general,
        name="analytics_2021_general",
    ),
    # 2022
    path(
        "analytics/2022/residences/",
        views.analytics_2022_residences,
        name="analytics_2022_residences",
    ),
    path(
        "analytics/2022/buisness/",
        views.analytics_2022_buisness,
        name="analytics_2022_buisness",
    ),
    path(
        "analytics/2022/general/",
        views.analytics_2022_general,
        name="analytics_2022_general",
    ),
    path("analytics/custom/", views.analytics_custom, name="analytics_custom"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
