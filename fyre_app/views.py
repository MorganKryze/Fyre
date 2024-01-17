from django.shortcuts import render
import matplotlib.pyplot as plt
import io


def index(request):
    return render(request, "index.html")


def analytics(request):
    plt.switch_backend('Agg')  # Switch to Agg backend
    plt.plot(range(10))
    plt.title("Simple Plot for demo purpose")
    fig = plt.gcf()

    fig.patch.set_facecolor('none')
    fig.patch.set_alpha(0)
    
    # Save the figure to a BytesIO object
    buf = io.BytesIO()
    fig.savefig(buf, format='svg', transparent=True)
    buf.seek(0)
    
    # Get the SVG data as a string
    svg = buf.getvalue().decode('utf-8')
    
    return render(request, 'analytics.html', {'data': svg})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")

def error_500_view(request):
    raise Exception("This is a test exception for the 500 error page.")
