from django.urls import path

from . import views

urlpatterns = [
    path('destination', views.destination, name='Destination'),
    path('<dest_name>', views.destinationview, name='Travello')
]

