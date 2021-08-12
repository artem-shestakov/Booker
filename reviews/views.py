from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "base.html")


def search(request):
    search_text = request.GET.get("search", "") 
    return render(request, "search.html", {
        "search_item": search_text
    })