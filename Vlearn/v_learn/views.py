from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    my_dir = {"insertme": "hello,hi"}
    return render(request, "index.html", context=my_dir)
