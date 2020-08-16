from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Details
from django.contrib.auth.models import User,auth

def home(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            fname = request.POST['name1']
            lname = request.POST['name2']
            phone = request.POST['mob']
            email = request.POST['email']
            password = request.POST['password1']
            try:
                user = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email )
                details = Details(user=user, phone_no= phone)
                details.save()
                print("user created")
                user = auth.authenticate(username=username,password=password)
                login(request,user)
                return redirect('success')
            except:
                messages.info(request,'User already exist')
                return render(request,'task2_2/signup.html',)
        else:
            messages.info(request, 'Passwords do not match :)')
            return render(request,'task2_2/signup.html',)
    return render(request,'task2_2/signup.html')

def log_in(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('success')
            else:
                messages.info(request,'Invalid Credentials')
                return render(request,'task2_2/signin.html',)
    return render(request,'task2_2/signin.html',)


def log_out(request):
    auth.logout(request)
    messages.success(request,f'Successfully Logged out!')
    return render(request,'task2_2/signup.html',)

def success(request):
    details = Details.objects.get(user=request.user)
    return render(request,'task2_2/success.html',{'data':details})