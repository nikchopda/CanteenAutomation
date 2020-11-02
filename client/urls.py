from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^loginvalidation', views.validation, name='validation'),
    url(r'^registration', views.registration, name='registration'),
    url(r'^register', views.register, name='register'),
    url(r'^getsession',views.getsession,name='getsession'),
    url(r'^cancel',views.cancel,name='cancel'),
    url(r'^logout',views.logout,name='logout')
]