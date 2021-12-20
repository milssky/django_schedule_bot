from django.shortcuts import render, HttpResponse


# Create your views here.
def index_bot(request):
    return HttpResponse("Hello")