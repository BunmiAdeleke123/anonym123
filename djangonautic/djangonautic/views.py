from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    #return HttpResponse("About")
    return render(request,"about.html")


def homepage(request):
    #return HttpResponse("HomePage")
    return render(request,"front.html")