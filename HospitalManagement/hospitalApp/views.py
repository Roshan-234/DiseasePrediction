from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{})


def signin(request):
    return render(request,'signin.html',{})


def signup(request):
    return render(request,'signup.html',{})

def contact(request):
    return render(request,'contact.html',{})


def services(request):
    return render(request,'services.html',{})