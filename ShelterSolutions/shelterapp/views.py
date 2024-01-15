from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    a = property.objects.all()
    b = Unit.objects.all()
    c = tenant_unit.objects.all()
    unit_id = []
    p_name = []
    addr = []
    location = []
    features = []
    img = []
    Property = []
    type = []
    rent = []

    t_id = []
    t_name = []
    photo = []
    t_addr = []
    docu = []

    for i in b:
        unit_id.append(i.id)
        p_name.append(i.Property.p_name)
        addr.append(i.Property.addr)
        img.append(str(i.img).split('/')[-1])
        type.append(i.type)
        rent.append(i.rent)

    for i in c:
        t_id.append(i.id)
        t_name.append(i.Tenant.t_name)
        photo.append(str(i.Tenant.photo).split('/')[-1])
        t_addr.append(i.Tenant.addr)
        docu.append(i.Tenant.docu)
    print(img)
    mylist1 = zip(p_name, addr, img, type, rent, unit_id)
    mylist2 = zip(t_name, photo, t_addr, docu, t_id)



    return render(request,'index.html',{'data1':mylist1,'data2':mylist2})

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
                return redirect(admin_log)
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
    a = property.objects.all()
    b = Unit.objects.all()
    c = tenant_unit.objects.all()
    unit_id = []
    p_name = []
    addr = []
    location = []
    features = []
    img = []
    Property = []
    type = []
    rent = []

    t_id = []
    t_name = []
    photo = []
    t_addr = []
    docu = []

    for i in b:
        unit_id.append(i.id)
        p_name.append(i.Property.p_name)
        addr.append(i.Property.addr)
        img.append(str(i.img).split('/')[-1])
        type.append(i.type)
        rent.append(i.rent)

    for i in c:
        t_id.append(i.id)
        t_name.append(i.Tenant.t_name)
        photo.append(str(i.Tenant.photo).split('/')[-1])
        t_addr.append(i.Tenant.addr)
        docu.append(i.Tenant.docu)
    print(img)
    mylist1 = zip(p_name, addr, img, type, rent, unit_id)
    mylist2 = zip(t_name, photo, t_addr, docu, t_id)

    return render(request,'admin_index.html',{'username':user,'data1':mylist1,'data2':mylist2})

def add_property(request):
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        addr = request.POST.get('addr')
        location = request.POST.get('location')
        features = request.POST.get('features')

        b = property(p_name=p_name,addr=addr,location=location,features=features)
        b.save()
        return redirect(add_unit)


    return render(request,'add_property.html')

def add_unit(request):

    properties = property.objects.all()
    if request.method == 'POST':

        p_id = request.POST.get('p_name')
        p_instance =  property.objects.get(pk=p_id)
        rent = request.POST.get('rent')
        type = request.POST.get('type')
        img = request.FILES.get('img')
        print(img)
        a = Unit(Property=p_instance,rent=rent,type=type,img=img)
        a.save()
        return redirect(admin_index)

    return render(request,'add_unit.html',{'properties':properties})

def add_tenant(request):

    if request.method == 'POST':
        t_name = request.POST.get('t_name')
        addr = request.POST.get('addr')
        doc = request.FILES.get('doc')
        photo = request.FILES.get('photo')

        a = tenant(t_name=t_name,addr=addr,docu=doc,photo=photo)
        a.save()
        return redirect(add_tenant_unit)
    return render(request,'add_tenant.html')

def add_tenant_unit(request):
    tenants = tenant.objects.all()
    units = Unit.objects.all()
    if request.method == 'POST':
        t_id = request.POST.get('tenant')
        t_instance = tenant.objects.get(pk=t_id)
        end_date = request.POST.get('end_date')
        rent_date = request.POST.get('rent_date')
        unit_id = request.POST.get('unit')
        unit_instance = Unit.objects.get(pk=unit_id)
        a = tenant_unit(Tenant=t_instance,end_date=end_date,rent_date=rent_date,unit=unit_instance)
        a.save()
        return redirect(admin_index)
    return render(request,'add_tenant_unit.html',{'tenants':tenants,'units':units})

def property_view(request):
    a = property.objects.all()
    b = Unit.objects.all()
    c = tenant_unit.objects.all()
    unit_id = []
    p_name = []
    addr = []
    location = []
    features = []
    img = []
    Property = []
    type = []
    rent = []

    t_id = []
    t_name = []
    photo = []
    t_addr = []
    docu = []

    for i in b:
        unit_id.append(i.id)
        p_name.append(i.Property.p_name)
        addr.append(i.Property.addr)
        img.append(str(i.img).split('/')[-1])
        type.append(i.type)
        rent.append(i.rent)

    for i in c:
        t_id.append(i.id)
        t_name.append(i.Tenant.t_name)
        photo.append(str(i.Tenant.photo).split('/')[-1])
        t_addr.append(i.Tenant.addr)
        docu.append(i.Tenant.docu)
    print(img)
    mylist1 = zip(p_name,addr,img,type,rent,unit_id)
    mylist2 = zip(t_name,photo,t_addr,docu,t_id)
    return render(request,'properties.html',{'data1':mylist1})

def property_single(request,id):
    a = Unit.objects.get(id=id)
    img = str(a.img).split('/')[-1]
    return render(request,'property_single.html',{'data':a,'img':img})

def tenant_single(request,id):
    a = tenant_unit.objects.get(id=id)
    img = str(a.Tenant.photo).split('/')[-1]
    return render(request,'tenant_single.html',{'data':a,'img':img})