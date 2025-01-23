"""
URL configuration for vivekanand project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from school import views

urlpatterns = [
    path('',views.home,name="home"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('contact',views.contact,name="contact"),
    path('events',views.events,name="events"),
    path('stuLogin',views.stuLogin,name="stuLogin"),
    path('studentadmin',views.studentadmin,name="studentadmin"),
    path('student',views.student,name="student"),
    path('director',views.director,name="director"),
    path('teachers',views.teachers,name="teachers"),
    path('signup',views.signup,name="signup")
]