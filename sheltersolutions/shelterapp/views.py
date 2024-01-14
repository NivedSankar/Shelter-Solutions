from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    return render(request,'index.html')

def admin_reg(request):
    if request.method == 'POST':
        a = userform(request.POST)
        if a.is_valid():
            username = a.cleaned_data['username']
            first_name = a.cleaned_data['first_name']
            last_name = a.cleaned_data['last_name']
            email = a.cleaned_data['email']
            password = a.cleaned_data['password']
            conf = a.cleaned_data['conf']
            if password == conf:
                b = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email)
                b.set_password(password)
                b.save()
                return HttpResponse("authenticated user added")
            else:
                return HttpResponse("Password didn't match")
        else:
            return HttpResponse("user not added")
    else:
        form = userform()
        return render(request,'admin_reg.html',{'form':form})


def admin_log(request):

    if request.method == 'POST':
        form = userlogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                request.session['username'] = username

                return redirect(admin_index)
            else:
                return HttpResponse('Invalid username or password')

        else:
            return HttpResponse('login failed')

    return render(request,'admin_log.html')

def admin_index(request):
    user = request.session['username']
    return render(request,'admin_index.html',{'username':user})

def add_property(request):
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        addr = request.POST.get('addr')
        location = request.POST.get('location')
        features = request.POST.get('features')

        b = property(p_name=p_name,addr=addr,location=location,features=features)
        b.save()
        request.session['p_name'] = p_name

    return render(request,'add_property.html')

def add_unit(request):
    properties = property.objects.all()
    return render(request,'add_unit.html',{'properties':properties})