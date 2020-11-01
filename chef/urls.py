from django.conf.urls import url
from requests import request

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^loginvalidation', views.validation, name='validation'),
    url(r'^process',views.process,name='process'),
    url(r'^complete',views.complete,name='complete'),
    url(r'^logout', views.logout, name='logout'),

]