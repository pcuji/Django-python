from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime

def index(request):
    # return HttpResponse('index.html')
    now = datetime.datetime.now()
    context = { 'date_time': now}
    print("hola soy yo pedro")
    return render(request, 'index.html', context)


def about(request):
    return HttpResponse('about')
    # return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def websites(request):
    return render(request, 'websites.html')

def packages(request):
    return render(request, 'packages.html')

def freelancer(request):
    return render(request, 'freelancer.html')

def cloud(request):
    return render(request, 'cloud.html')
def applications(request):
    return render(request, 'applications.html' )

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')
def team(request):
    #return HttpResponse('about')
    return render(request, 'team.html')
def careers(request):
    #return HttpResponse('about')
    return render(request, 'careers.html')
