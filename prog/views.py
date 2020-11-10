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

		
def logout(request):
    if 'adminnm' in request.session:
        del request.session['adminnm']
    return HttpResponseRedirect('/prog')



