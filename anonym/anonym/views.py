from django.shortcuts import render

def name(request):
    #return HttpResponse("About")
    return render(request,"index.html")