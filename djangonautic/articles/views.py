from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_list(request):
    article = Article.objects.all().order_by("date")
    return render(request,"articles/article_list.html",{"article":article})

def article_details(request, slug):
    articles = Article.objects.get(slug=slug)
    return render(request,"articles/article_detail.html",{"articles":articles})

@login_required(login_url="/accounts/login")
def article_create(request):
    return render(request, "articles/article_create.html")
