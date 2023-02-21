from profile import Profile
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import signUpForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib import messages
from django.utils import timezone
from hospitalApp.models import contactEnquiry
from .models import Appointment
from .models import HeartDisease

# from .models import Patient
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html',{})


def diabetes(request):
    return render(request,'diabetes.html',{})


def braintumor(request):
    return render(request,'braintumor.html',{})


def heartdisease(request):
    if request.method == "POST":
        print(request.POST)
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        chestPain = request.POST.get('cp')
        trestbps = request.POST.get('trestbps')
        chol = request.POST.get('chol')
        fbs = request.POST.get('fbs')
        restecg = request.POST.get('restecg')
        maximumHeartRate = request.POST.get('maximumHeartRate')
        ExerciseInducedAngina = request.POST.get('ExerciseInducedAngina')
        STdepression = request.POST.get('STdepression')
        # here left side is the model field name .........
        en=HeartDisease(age = age, sex = sex, chestPain = chestPain, restingBloodPressure = trestbps, cholesterol = chol , fastingBloodSugar = fbs , restingElectrocardiographic = restecg , maximumHeartRate = maximumHeartRate, ExerciseInducedAngina = ExerciseInducedAngina  , STdepression = STdepression)

        en.save()
    return render(request,'heartdisease.html')


def breastcancer(request):
    return render(request,'breastcancer.html',{})

def appointment(request):
    return render(request,'appointment.html',{})

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

def save_appointment(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        emaill = request.POST.get('email')
        date = timezone.datetime.strptime(request.POST['date'], '%m/%d/%Y').strftime('%Y-%m-%d')
        # time = timezone.datetime.strptime(request.POST['time'], '%H:%M')
        time = timezone.datetime.strptime(request.POST['time'], '%I:%M%p').time()
 

        messagess = request.POST.get('message')
        if name and name.strip() != "":
            en = Appointment(name = name, email = emaill, date = date, time = time, messages = messagess)
            en.save()
            return HttpResponse("Appointment saved successfully.")
        else:
            return HttpResponse("Error: Name is required.")
        # here left side is the model field name and right side is var name in the function.........
        # en = Appointment(name = name, email = emaill, date = date, time = time, messages = messagess)
        # en.save()
        
        
    return render(request, 'appointment.html')
    
    





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
    

     return render(request,'signin.html',{})





def signup(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = signUpForm()
    return render (request=request, template_name="signup.html", context={"signUpForm":form})

def contact(request):
    return render(request,'contact.html',{})


def services(request):
    return render(request,'services.html',{})

# def createAppointment(request):
#      if request.method == 'POST':
#           if request.POST.get('name') and request.POST.get('email') and request.POST.get('date')and request.POST.get('time'):
#                appointment = Appointment()
#                appointment.name = request.POST.get('name')
#                appointment.email = request.POST.get('email')
#                appointment.date = request.POST.get('date')
#                appointment.time = request.POST.get('time')
#                appointment.save()

#                return render (request, 'home')
#      else:
#         return render (request, 'home')


     