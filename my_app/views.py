from django.shortcuts import render
from .models import Destination
from .models import News

# Create your views here.

def index (request) :

    dests = Destination.objects.all()
    news_1 = News.objects.all()
    
    return render(request, 'index.html', {'dests' : dests, 'news_1' : news_1})        
