
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('saveenquiry', views.saveEnquiry, name="saveenquiry"),
    path('contact',views.contact,name="contact"),
    path('services',views.services,name="services"),
    # path('about',views.about,name="about"),
         
]
