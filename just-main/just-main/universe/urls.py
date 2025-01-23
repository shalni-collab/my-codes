from django.contrib import admin
from django.urls import path,include
from universe import views
urlpatterns = [
    path('',views.index,name="homes"),
    path('home',views.inde,name="home"),
    path('img',views.img,name="img"),
    path('vid',views.vid,name="vid"),
    path('car',views.car,name="car"),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('invalid',views.invalid,name="invalid"),
    path('signout',views.signout,name="signout"),
   

]
