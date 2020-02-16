from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Profile, Department, Material,Result, ResultPost
from . import forms
from django.contrib.auth.decorators import login_required
from paystack.resource import TransactionResource
# Create your views here.
user=None
listofall=None
inf=None
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)

            c = Profile()
            c.name = user
            c.save()


            return redirect("/accounts/create")
    else:
        form = UserCreationForm()
    return render(request,"accounts/signup.html",{"form": form})


def login_view(request):
    global user
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)


        if form.is_valid():

            user = form.get_user()
            print(type(user))
            login(request,user)


            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                if str(user) == "Benjamin":
                    print("Oga sir!!")
                    return redirect("/accounts/result")

                else:
                    return redirect("/accounts/info")

    else:
        form = AuthenticationForm()
    return render(request,"accounts/login.html",{"form":form})


def logout_view(request):
    if request.method == "POST":
        print(request.user)
        logout(request)

    return render(request, "front.html")

@login_required(login_url="/accounts/login")
def create(request):
    if request.method =="POST":
        form = forms.CreateProfile(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            print(instance)
            instance.name = request.user
            c= Profile.objects.get(name=instance.name)
            c.department=instance.department
            c.part = instance.part
            c.dp = instance.dp
            c.Gender=instance.Gender


            c.save()
            return redirect("/accounts/info")

    else:
        form= forms.CreateProfile()
    return render(request,"accounts/create.html",{"form":form})

@login_required(login_url="/accounts/login")
def info(request):
    infos = Profile.objects.get(name=request.user)

    return render(request, "accounts/info.html", {"infos": infos})

@login_required(login_url="/accounts/login")
def reg(request):
    get = Profile.objects.get(name=request.user)

    items = Department.objects.get(department=get.department)
    b = items.courses.split(',')
    if request.method=="POST":
        c= request.POST.getlist('course')
        finalist= ",".join(c)
        get= Profile.objects.get(name=request.user)
        get.course_registered=finalist
        get.save()
        i = get.course_registered.split(",")

        for b in i[:]:
            d = Material.objects.get(course=b)
            d.People.append("{}".format(request.user))
            print(d.People)
            try:
                d.save()
            except ValueError:
                d.save()
        return redirect("/accounts/success/")

    return render(request,"accounts/coursereg.html",{"b":b})


def member(request):

    return render(request,"accounts/success.html",)


def result(request):
    all = Result.objects.all()
    j= Material.objects.all()

    global listofall
    listofall =[]

    if request.method == "POST":
        c = request.POST.get("course")
        global inf
        inf =c
        d = Result.objects.get(course_title=c)
        j = Material.objects.get(course=c)
        for k in j.People:
            d.attrs[k]=""

            d.save()
        listofall.append(d.attrs)

        return redirect("/accounts/fill/")



    return render(request, "accounts/result.html", {"all":all})


def fill(request):


    if request.method =="POST":
        j=request.POST.getlist("result")
        o = request.POST.getlist("people")
        dic={}
        for d,e in zip(o,j):
            dic[d]=e

        res = ResultPost.objects.get(course_title=inf)
        res.attrs= dic
        print(res.attrs)
        res.save()
        return redirect("/accounts/upload/")
    return render(request,'accounts/fill.html',{"l":listofall[0]})


def upload(request):
    j = ResultPost.objects.get(course_title=inf)
    f=  j.attrs

    return render(request,"accounts/upload.html",{"f":f,"inf":inf})


def getresult(request):
    h=  Profile.objects.get(name=request.user)
    d= [h.course_registered]
    t={}
    for ds in d:
        r=ResultPost.objects.get(course_title=ds)

        t[ds]=r.attrs[str(request.user)]
    print(t)

    return render(request, "accounts/results.html",{"t":t})

'''

import string
import random

from paystack.resource import TransactionResource



def main():
    rand = ''.join(
        [random.choice(
            string.ascii_letters + string.digits) for n in range(16)])
    secret_key = 'YOUR_SECRET_KEY'
    random_ref = rand
    test_email = 'TEST_EMAIL'
    test_amount = 'TEST_AMOUNT'
    plan = 'Basic'
    client = TransactionResource(secret_key, random_ref)
    response = client.initialize(test_amount,
                                 test_email,
                                 plan)
    print(response)
    client.authorize() # Will open a browser window for client to enter card details
    verify = client.verify() # Verify client credentials
    print(verify)
    print(client.charge()) # Charge an already exsiting client

'''