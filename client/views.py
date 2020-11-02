import smtplib
from django.core.mail import send_mail
from urllib.parse import urlparse
import urllib.request
from email.mime.text import MIMEText
#import sms
from django.db.models import Q
from public import public
from decorator import decorator
import httplib2
import self as self
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from sendsms.message import SmsMessage
#from sinchsms import SinchSMS
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
#from sendsms import api
from django.views.decorators.csrf import csrf_exempt

from chef.models import Chef

#SENDSMS_BACKEND = 'myapp.mysmsbackend.SmsBackend'
#from sendsms.backends.base import BaseSmsBackend
from prog.models import Orderdetails
from .models import Customer, Item, Orders
import json
import urllib
import http.cookiejar
from getpass import getpass
import sys
import os
from stat import *
l=[];
def login(request):
    return render(request, 'login.html')
def registration(request):
    return render(request, 'registration.html')
dict={'status':''}

@csrf_exempt
def register(request):
    username1 = request.POST['usernm']
    mobileno1 = request.POST['mno']
    firstname1 = request.POST['firstname']
    password1 = request.POST['passwd']
    lastname1 = request.POST['lastname']
    eid1=request.POST['email']
    v=Customer(username=username1,firstname=firstname1,lastname=lastname1,password=password1,mobileno=mobileno1,emailid=eid1)
    v.save()
    return HttpResponse('1')
@csrf_exempt
def validation(request):

    username1=request.POST['unm']
    password1=request.POST['pwd']
    data=Customer.objects.filter(Q(username=username1)|Q(emailid=username1))
    if not data:
        return HttpResponse('0')
    elif data[0].password==password1:
        request.session['unm'] = data[0].username
        random_number = User.objects.make_random_password(length=10, allowed_chars='123456789')
        request.session['oid'] = random_number
        request.session['itemlist']=l;
        #del request.session['itemlist']
        return HttpResponse('1')
    else:
        return HttpResponse('2')

@csrf_exempt
def getsession(request):
    try:
        sdata = request.session['itemlist']
        itemcount = len(sdata)
    except AttributeError:
        print("error")
    return HttpResponse(json.dumps({'data':sdata,'itemcount':itemcount}), content_type="application/json")

@csrf_exempt
def cancel(request):
    v = request.POST['ino1']
    oid = request.POST['oid1']
    data = Orders.objects.filter(orderid=oid,itemno=v)
    qt=data[0].quantity
    data.delete()
    item = Item.objects.filter(itemno=v)
    price=item[0].price
    a=Orderdetails.objects.filter(orderid=oid)
    tp=a[0].totalprice
    np=int(tp)-(int(price)*int(qt))
    Orderdetails.objects.filter(orderid=oid).update(totalprice=np)
    data = Orders.objects.filter(orderid=oid)
    item = Item.objects.all()
    return HttpResponse()

def logout(request):
    if not 'unm' in request.session:
        return HttpResponseRedirect('/client')
    del request.session['unm']
    del request.session['oid']
    if 'itemlist' in request.session:
        del request.session['itemlist']
    if 'total' in request.session:
        del request.session['total']

    return HttpResponseRedirect('/client')

@csrf_exempt
def uniqueusr(request):
    dt=Customer.objects.values_list('username',flat=True)
    return HttpResponse(json.dumps({'data': list(dt)}), content_type="application/json")

