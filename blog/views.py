from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Blog Index Page", request)
