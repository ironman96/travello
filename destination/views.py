from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from my_app.models import Destination, Destination_individual
from accounts.views import login
from django.shortcuts import get_object_or_404


# Create your views here.

# def destination(request, dest_name):
#     if request.user.is_authenticated:
#         dests = Destination.objects.all()
#         desti = get_object_or_404(Destination, name = dest_name)
#         return render(request, 'destinations.html', {'dests' : dests})
#     else : 
#         return redirect('/accounts/login')


def destination(request):
    if request.user.is_authenticated:
        dests = Destination.objects.all()
        return render(request, 'destinations.html', {'dests' : dests})
    else : 
        return redirect('/accounts/login')


def destinationview(request, dest_name) :
        
    if request.user.is_authenticated:

        dest_name = dest_name
        destination = get_object_or_404(Destination, name = dest_name)
        desti_indi = get_object_or_404(Destination_individual, name = dest_name)
        return render(request, 'destination_individual.html', {'destination' : destination , 'desti_indi' : desti_indi, 'dest_name' : dest_name})
    else : 
        return redirect('/accounts/login')
