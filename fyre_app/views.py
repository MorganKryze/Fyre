from django.shortcuts import render
import matplotlib.pyplot as plt
import io
# from django.utils.translation import gettext as _


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
    plt.switch_backend("Agg")  # Switch to Agg backend
    plt.plot(range(10))
    plt.title("Simple Plot for demo purpose")
    fig = plt.gcf()

    fig.patch.set_facecolor("none")
    fig.patch.set_alpha(0)

    # Save the figure to a BytesIO object
    buf = io.BytesIO()
    fig.savefig(buf, format="svg", transparent=True)
    buf.seek(0)

    # Get the SVG data as a string
    svg = buf.getvalue().decode("utf-8")

    return render(request, "pages/analytics/2019.html", {"data": svg})


def analytics2020(request):
    plt.switch_backend("Agg")  # Switch to Agg backend
    plt.plot(range(10))
    plt.title("Simple Plot for demo purpose")
    fig = plt.gcf()

    fig.patch.set_facecolor("none")
    fig.patch.set_alpha(0)

    # Save the figure to a BytesIO object
    buf = io.BytesIO()
    fig.savefig(buf, format="svg", transparent=True)
    buf.seek(0)

    # Get the SVG data as a string
    svg = buf.getvalue().decode("utf-8")

    return render(request, "pages/analytics/2020.html", {"data": svg})


def analytics2021(request):
    plt.switch_backend("Agg")  # Switch to Agg backend
    plt.plot(range(10))
    plt.title("Simple Plot for demo purpose")
    fig = plt.gcf()

    fig.patch.set_facecolor("none")
    fig.patch.set_alpha(0)

    # Save the figure to a BytesIO object
    buf = io.BytesIO()
    fig.savefig(buf, format="svg", transparent=True)
    buf.seek(0)

    # Get the SVG data as a string
    svg = buf.getvalue().decode("utf-8")

    return render(request, "pages/analytics/2021.html", {"data": svg})


def analytics2022(request):
    plt.switch_backend("Agg")  # Switch to Agg backend
    plt.plot(range(10))
    plt.title("Simple Plot for demo purpose")
    fig = plt.gcf()

    fig.patch.set_facecolor("none")
    fig.patch.set_alpha(0)

    # Save the figure to a BytesIO object
    buf = io.BytesIO()
    fig.savefig(buf, format="svg", transparent=True)
    buf.seek(0)

    # Get the SVG data as a string
    svg = buf.getvalue().decode("utf-8")

    return render(request, "pages/analytics/2022.html", {"data": svg})


def analytics_custom(request):
    plt.switch_backend("Agg")  # Switch to Agg backend
    plt.plot(range(10))
    plt.title("Simple Plot for demo purpose")
    fig = plt.gcf()

    fig.patch.set_facecolor("none")
    fig.patch.set_alpha(0)

    # Save the figure to a BytesIO object
    buf = io.BytesIO()
    fig.savefig(buf, format="svg", transparent=True)
    buf.seek(0)

    # Get the SVG data as a string
    svg = buf.getvalue().decode("utf-8")

    return render(request, "pages/analytics/custom.html", {"data": svg})
