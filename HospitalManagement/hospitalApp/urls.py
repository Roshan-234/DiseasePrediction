
from django.urls import path
from . import views
from .views import save_appointment

urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('saveenquiry', views.saveEnquiry, name="saveenquiry"),
    path('appointment', views.save_appointment, name="save_appointment"),
    path('contact',views.contact,name="contact"),
    path('services',views.services,name="services"),
    # path('appointment',views.appointment,name="appointment"),w
    # path('about',views.about,name="about"),
         
]
