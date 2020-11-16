import json
import os
from tkinter.tix import MAX

from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from CanAutomationSystem.settings import BASE_DIR
from chef.models import Chef
from client.models import Item, Orders, Customer
from prog.models import Admin, Orderdetails

def login(request):
    return render(request, 'adminlogin.html')

def forget(request):
    if not 'adminnm' in request.session:
        return HttpResponseRedirect('/prog')
    return render(request, 'forgot.html')

def fp(request):
    unm=request.POST['unm']
    data = Admin.objects.filter(name=unm)
    if not data:
        messages.info(request,'inavalid username')
        return HttpResponseRedirect('/prog/forget')
    messages.info(request, ' login with adminid : '+unm+' and password  : '+data[0].value)
    return HttpResponseRedirect('/prog/forget')
@csrf_exempt
def validation(request):
    username1 = request.POST['unm']
    password1 = request.POST['pwd']
    data = Admin.objects.filter(name=username1)
    if not data:
        return HttpResponse('0')
    elif data[0].value == password1:
        request.session['adminnm'] = username1
        return HttpResponse('1')
    else:
        return HttpResponse('2')

def additem(request):
    if not 'adminnm' in request.session:
        return HttpResponseRedirect('/prog')
    data=Chef.objects.all()
    m=0
    a=Item.objects.all()
    for i in a:
        if int(i.itemno)>m:
            m=int(i.itemno)
    return render(request, 'additem.html',{'querydata':data,'inos':str(m+1)})
		
def addchef(request):
    if not 'adminnm' in request.session:
        return HttpResponseRedirect('/prog')
    return render(request, 'addchef.html')

@csrf_exempt
def additemwork(request):
    if not 'adminnm' in request.session:
        return HttpResponseRedirect('/prog')
    itemno1 = request.POST['itemno']
    itemname1 = request.POST['itemname']
    category1 = request.POST['category']
    image1 = request.FILES['image']
    price1 = request.POST['price']
    fs=FileSystemStorage(location=os.path.join(BASE_DIR,'static/../client/static/'))
    filename=fs.save(image1.name,image1)
    v = Item(itemno=itemno1,itemname=itemname1,category=category1,image='/static/'+image1.name,price=price1)
    v.save()
    return HttpResponseRedirect('/prog/additem')

@csrf_exempt
def addchefwork(request):
    if not 'adminnm' in request.session:
        return HttpResponseRedirect('/prog')
    chefid1 = request.POST['chefid']
    chefname1 = request.POST['chefname']
    category1 = request.POST['category']
    if chefid1=='':
        return HttpResponse('0')
    if chefname1 == '':
        return HttpResponse('1')
    if category1=='':
        return HttpResponse('3')
    v = Chef(chefid=chefid1, chefname=chefname1, category=category1)
    v.save()
    messages.info(request, 'Chef added successfully')
    # dict.staus="";
    return HttpResponse('2')

def updateitem(request):
    if not 'adminnm' in request.session:
        return HttpResponseRedirect('/prog')
    iid = request.GET.get('itemno')
    a = Item.objects.filter(itemno=iid)
    data = Chef.objects.all()
    return render(request, 'updateitem.html', {'qdata': a,'querydata':data})
@csrf_exempt
def updateitemwork(request):
    if not 'adminnm' in request.session:
        return HttpResponseRedirect('/prog')
    itemno1 = request.POST['itemno']
    itemname1 = request.POST['itemname']
    category1 = request.POST['category']
    img1 = request.POST['img']
    price1 = request.POST['price']
    d=Item.objects.filter(itemno=itemno1)
    if not d[0].image==img1:
        image1 = request.FILES['image']
        fs = FileSystemStorage(location=os.path.join(BASE_DIR, 'static/../client/static/'))
        filename = fs.save(image1.name, image1)
        Item.objects.filter(itemno=itemno1).update(itemno=itemno1, itemname=itemname1, category=category1,
                                                   image='/static/' + image1.name, price=price1)
    else:
        Item.objects.filter(itemno=itemno1).update(itemno=itemno1, itemname=itemname1, category=category1, image=img1, price=price1)

    return HttpResponseRedirect('/prog/viewitem')
	
def updatechef(request):
    if not 'adminnm' in request.session:
        return HttpResponseRedirect('/prog')
    cid = request.GET.get('chefid')
    a = Chef.objects.filter(chefid=cid)
    return render(request,'updatechef.html',{'qdata':a})
@csrf_exempt
def updatechefwork(request):
    if not 'adminnm' in request.session:
        return HttpResponseRedirect('/prog')
    chefid1=request.POST['chefid']
    chefname1=request.POST['chefname']
    category1=request.POST['category']
    if chefid1=='':
        return HttpResponse('0')
    if chefname1 == '':
        return HttpResponse('1')
    if category1=='':
        return HttpResponse('3')
    Chef.objects.filter(chefid=chefid1).update(chefname=chefname1,category=category1)
    return HttpResponse('2')
	
def adminwork(request):
    if not 'adminnm' in request.session:
        return HttpResponseRedirect('/prog')
    return render(request,'adminwork.html')
	
def logout(request):
    if 'adminnm' in request.session:
        del request.session['adminnm']
    return HttpResponseRedirect('/prog')



