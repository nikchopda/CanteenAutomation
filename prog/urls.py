from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^adminloginvalidation', views.validation, name='validation'),
	url(r'^adminwork',views.adminwork,name='adminwork'),
    url(r'^additemwork', views.additemwork, name='additemwork'),
	url(r'^additem', views.additem, name='additem'),
	url(r'^addchefwork', views.addchefwork, name='addchefwork'),
	url(r'^addchef', views.addchef, name='addchef'),
    url(r'^updatechefwork',views.updatechefwork,name='updatechefwork'),
	url(r'^updateitemwork',views.updateitemwork,name='updateitemwork'),
    url(r'^forget',views.forget,name='forget'),
	url(r'^updatechef',views.updatechef,name='updatechef'),
	url(r'^updateitem',views.updateitem,name='updateitem'),
    url(r'^fp',views.fp,name='fp'),
    url(r'^logout',views.logout,name='logout'),
]