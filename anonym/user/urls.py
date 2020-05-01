from django.conf.urls import url
from . import views

app_name = "user"



urlpatterns =[
    url(r"^signup/$",views.signup_view ,name ="signup"),
    url(r"^login/$",views.login_view ,name ="login"),
    url(r"^home/$",views.home,name ="home"),
    url(r"^message/$",views.mess),
    url(r"^",views.message,name ="message"),

]
