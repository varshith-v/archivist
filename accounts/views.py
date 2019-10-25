from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def signUp(request):
    if request.method == 'POST':
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        userName = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.filter(email=email).exists():
            messages.info(request,'An account exists with this Email id.\n Try to Login!',extra_tags='email_exists')
            return redirect('signup')
        
        elif User.objects.filter(username=userName).exists():
            messages.info(request,'Username taken.\n Try a different one.',extra_tags='username_exists')
            return redirect('signup')
        
        elif password1 != password2:
            messages.error(request,'Password mismatch!\n Try again',extra_tags='password_mismatch')
            return redirect('signup')
        
        else:
            user = User.objects.create_user(username=userName,password=password1,email=email, first_name=firstName, last_name=lastName)
            user.save()
            print('User created')
            return redirect('/')
    else:
        return render(request,'signup.html') 
    
def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request,'login.html')