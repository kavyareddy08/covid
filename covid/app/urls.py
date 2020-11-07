from django.contrib import admin
from django.urls import path,include 
from app import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('handleBlog',views.handleBlog,name='handleBlog'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
    path('signup',views.signup,name='signup'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('add',views.add,name='add'),
    path('search',views.search,name='search'),
    path('msme',views.msme,name='msme'),
    path('real',views.real,name='real'),
    path('avi',views.avi,name='avi'),
    path('txt',views.txt,name='txt'),
    path('txtd',views.txtd,name='txtd'),
    path('d',views.d,name='d'),
    path('s',views.s,name='s'),
    path('f',views.f,name='f'),
    path('a',views.a,name='a'),
    path('b',views.b,name='b'),
    path('c',views.c,name='c'),
    path('p',views.p,name='p'),
    path('q',views.q,name='q'),
    path('r',views.r,name='r'),
    
]