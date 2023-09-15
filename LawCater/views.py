from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def clientlogin(request):
    return render(request, 'clientlogin.html')

def contactus(request):
    return render(request, 'contactus.html')

def lawyerlogin(request):
    return render(request, 'lawyerloginpage.html')

def signuplawyer(request):
    return render(request, 'signup-lawyer.html')

def signupclient(request):
    return render(request, 'signup-client.html')