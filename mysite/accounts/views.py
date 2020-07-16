from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserRegistrationForm



# Create your views here.
def login_user(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print(request.GET)
            login(request, user)
            redirect_url= request.GET.get('next','home')
        # Redirect to a success page.
            return redirect(redirect_url)

        else:
        # Return an 'invalid login' error message.
            messages.error(request, 'Bad username or password')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    # Redirect to a success page.
    return redirect('home')

def user_registration(request):
    if request.method== 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email=email, password=password)
            messages.success(request, 'THANKS FOR REGISTERING', )
            return redirect('accounts:login')
            #
            # print(form.cleaned_data)
            # print('form as valid')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html',{'form': form})
