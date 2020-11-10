from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^adminloginvalidation', views.validation, name='validation'),
	url(r'^addchef', views.addchef, name='addchef'),
    url(r'^forget',views.forget,name='forget'),
    url(r'^fp',views.fp,name='fp'),
    url(r'^logout',views.logout,name='logout'),
]