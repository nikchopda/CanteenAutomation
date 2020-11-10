import re
from random import randint

from django.contrib.admin.templatetags.admin_list import register
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from chef.models import Chef
import MySQLdb

from client.models import Orders, Item


def login(request):
    return render(request, 'cheflogin.html')


@csrf_exempt
def validation(request):
    chefid1 = request.POST['chefid']
    chefname1 = request.POST['chefname']
    data = Chef.objects.filter(chefid=chefid1)
    if not data:
        return HttpResponse('0')
    elif data[0].chefname == chefname1:
        request.session['chefname'] = chefname1;
        return HttpResponse('1')
    else:
        return HttpResponse('2')
		
def prepareorder(request):
    if not 'chefname' in request.session:
        return HttpResponseRedirect('/chef')
    cname = request.session['chefname']
    c = Chef.objects.filter(chefname=cname)
    data = Orders.objects.filter(category=c[0].category)
    item = Item.objects.all()
    return render(request, 'prepareorder.html', {'qdata': item, 'querydata': data})

def logout(request):
    if 'chefname' in request.session:
        del request.session['chefname']
    return HttpResponseRedirect('/chef')