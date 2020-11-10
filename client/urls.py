from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^loginvalidation', views.validation, name='validation'),
    url(r'^registration', views.registration, name='registration'),
    url(r'^register', views.register, name='register'),
    url(r'^choose', views.chooseorder, name='chooseorder'),
    url(r'^forgetpassword',views.forgetpassword,name='forgetpassword'),
    url(r'^fpwd',views.fpwd,name='fpwd'),
    url(r'^changepassword',views.changepassword,name='changepassword'),
    url(r'^cpwd',views.cpwd,name='cpwd'),
    url(r'^getsession',views.getsession,name='getsession'),
    url(r'^cancel',views.cancel,name='cancel'),
    url(r'^logout',views.logout,name='logout')
]