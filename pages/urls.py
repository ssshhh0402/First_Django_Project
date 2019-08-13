from django.contrib import admin
from django.urls import path  
from . import views
urlpatterns = [
    path('',views.index),
    path('hello/<str:name>/', views.hello),
    path('lotto/', views.lotto),
    path('dinner/', views.dinner),
    path('cube/<int:num>/', views.cube),
    path('about/<str:name>/<int:age>/', views.about),
    path('isitgwangbok/', views.gwangbok),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('log/', views.log),
    path('sign_up/',views.sign),
    path('okay/', views.okay),
    path('inner/', views.inner),
    path('games/', views.game),
path('rufrhk/', views.rsp),

]