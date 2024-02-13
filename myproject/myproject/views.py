# from django.http import HttpResponse
from django.shortcuts import render


# The views are the information that is displayed to the user.
def homepage(request):
    # return HttpResponse("Hello, World!")
    return render(request, "home.html")


def about(request):
    # return HttpResponse("About page")
    return render(request, "about.html")
