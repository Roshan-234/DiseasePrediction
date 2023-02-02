from profile import Profile
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from hospitalApp.models import contactEnquiry
from .models import Appointment
# from .models import Patient
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html',{})

# this is for contact us form
def saveEnquiry(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        emaill = request.POST.get('email')
        subjectt = request.POST.get('subject')
        messagess = request.POST.get('message')
        # here left side is the model field name .........
        en=contactEnquiry(your_name = name, your_email = emaill, subject = subjectt, messages = messagess)
        en.save()
    return render(request,"contact.html")



def signin(request):

    # if request.method =='POST':
    #      Email= request.POST['Email']
    #      Password= request.POST['password']

    #      user =auth.authenticate(Email='Email' , Password='password')

    #      if user is not None:
    #         auth.login(request,user)
    #         return render('home')
    #      else:
    #         messages.info(request, 'Credentials Invalid')
    #         return render('signin')
    # else:
    

     return render(request,'home.html',{})


def signup(request):

    # if request.method =='POST':
    #     Firstname= request.POST['firstname']
    #     Lastname= request.POST['lastname']
    #     Email= request.POST['Email']
    #     Password= request.POST['password']


    #     if User.objects.filter(Email='email').exists():
    #         messages.info(request,'Email Taken')
    #         return render('signup')
    #     elif User.objects.filter(Firstname='firstname').exists():
    #             messages.info(request,'Username Taken')
    #             return render('signup')
    #     else:
    #             user = User.objects.create_user(Firstname='firstname', Email='email', Password='password')
    #             user.save()

    #     #log user in and redirect to settings page 
    #     user_login= auth.authenticate(Firstname='firstname', Password='password')
    #     auth.login(request,user_login)

    #     #create profile obj for new user
    #     user_model=User.objects.get(Firstname='first_name')
    #     new_Patient = Patient.objects.create(last_name=user_model.first_name)
    #     new_Patient.save()
    #     return render('signin')
        

        
    # else:
        return render(request,'signup.html',{})

def contact(request):
    return render(request,'contact.html',{})


def services(request):
    return render(request,'services.html',{})

def createAppointment(request):
     if request.method == 'POST':
          if request.POST.get('name') and request.POST.get('email') and request.POST.get('date')and request.POST.get('time'):
               appointment = Appointment()
               appointment.name = request.POST.get('name')
               appointment.email = request.POST.get('email')
               appointment.date = request.POST.get('date')
               appointment.time = request.POST.get('time')
               appointment.save()

               return render (request, 'home')
     else:
        return render (request, 'home')


     