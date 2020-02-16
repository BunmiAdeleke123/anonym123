
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.article_list,name="lists"),
    url(r"^create/$", views.article_create, name= "create"),
    url(r"^(?P<slug>[\w-]+)/$", views.article_details, name ="details"),

]

