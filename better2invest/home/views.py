from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainpage(request):
    return render(request, "home.html")

def loginpage(request):
    return render(request, "login.html");

def signupPage(request):
    return render(request, "signup.html")