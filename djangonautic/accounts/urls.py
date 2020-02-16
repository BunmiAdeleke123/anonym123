from django.conf.urls import url
from . import views

app_name = "accounts"

urlpatterns =[
    url(r"^signup/$",views.signup_view, name ="signup"),
    url(r"^login/$",views.login_view,name = "login"),
    url(r"^logout/$", views.logout_view, name = "logout"),
    url(r"^create/$", views.create, name = "create"),
    url(r"^info/", views.info),
    url(r"^course_reg/", views.reg),
    url(r"^success/", views.member),
    url(r"^result/", views.result),
    url(r"^fill/", views.fill),
    url(r"^upload/", views.upload),
    url(r"^results/", views.getresult),


]