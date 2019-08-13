from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect

# Create your views here.

def login (request) :
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None :
            auth.login(request,user)
            # if destination.desti == 1 :
            #     return redirect('destination/destination')
            # else :
            return redirect('/')
        elif username == '':
            messages.error(request, 'Please Enter Your Username')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif password == '' :
            messages.error(request, 'Please Enter Your Password')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else :
            messages.error(request, 'Invalid Credentials')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else :
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request) :

    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                # return redirect('register')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            elif User.objects.filter(email=email).exists() :
                messages.info(request,'Email Taken')
                # return redirect('register')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else : 
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
                user.save()
                messages.info(request,'User Created')
                return render(request, 'login.html')
                
        else :
            messages.info(request,'Password Not Matching')
            # return redirect('register')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return redirect('/')
    else :
        return render(request, 'register.html')
