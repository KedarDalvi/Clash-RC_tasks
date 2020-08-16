from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Profile
def home1(request):
    if request.method == 'POST':
        fname = request.POST['name1']
        lname = request.POST['name2']
        phone = request.POST['mob']
        email = request.POST['email']
        gender = request.POST['gender']
        profile = Profile(first_name=fname,last_name=lname,phone_no=phone,email_id=email,gender=gender)
        profile.save()

    return render(request,'task2_part1/home1.html')

def login1(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            data = Profile.objects.get(email_id=email)
            return render(request, "task2_part1/profile.html", {'data': data})
        except Profile.DoesNotExist:
            messages.error(request, f'User does not exist')
            return redirect('task1-login1')

    return render(request, 'task2_part1/login1.html', )
