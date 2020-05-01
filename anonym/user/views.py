from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Profile
import time
j= None
x=None
# Create your views here.


def signup_view(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)

            c = Profile()
            c.name = user
            c.save()


            return redirect("/user/home")
    else:
        form = UserCreationForm()
    return render(request,"user/signup.html",{"form": form})



def login_view(request):
    print(request.POST)
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)


        if form.is_valid():

            user = form.get_user()
            print(type(user))
            login(request,user)


            if "next" in request.POST:

                return redirect(request.POST.get('next'))
            else:
                print("am here")
                return redirect("/user/home/")

    else:
        form = AuthenticationForm()
    return render(request,"user/login.html",{"form":form})


def home(request):
    user= request.user
    return render(request,"user/home.html",{"user":user})



def mess(request):
    i=[]
    j = Profile.objects.get(name=request.user)
    d = j.attrs
    e=[]

    global x

    for key, value in d.items():
        temp=[key,value]
        e.append(temp)
    if request.method=="POST":
        print(x)
        r = e[::-1]
        y=r[:x+4]
        x += 4
        print(len(e))


    else:
        x=0
        r = e[::-1]
        y=r[x:x+7]
        x += 7
        print("here")
        print(y)



    return render(request, "user/view.html", {"y": y, "i": i})



def message(request):
    global j
    if request.method=="GET":

        c = request.GET.get("user")
        try:
            j= Profile.objects.get(name=c)

        except:
            return redirect("/")
    elif request.method=="POST":
        c = request.POST.get("message")
        o= Profile.objects.get(name=j)
        localtime = time.asctime(time.localtime(time.time()))
        o.attrs[localtime]=c
        o.save()

    else:
        print("nothing")
    return render(request,"user/message.html")
