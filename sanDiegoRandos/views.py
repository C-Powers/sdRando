from django.shortcuts import render
from .models import Permanents
from .permScrape import getPerms, scrapeSite
# Create your views here.

def home(request):
    return render(request, 'sanDiegoRandos/home.html', {})

def returnPermanents(request):
    '''
    location = models.CharField(max_length=200)
    freeRoute = models.BooleanField()
    distance = models.CharField(max_length=200)
    climb = models.CharField(max_length=200)
    permName = models.CharField(max_length=200)
    organizer = models.CharField(max_length=200)
    permLink = models.URLField(null=True)
    '''
    posts = Permanents.objects.all()
    posts.location="poop meistro"
    posts.freeRoute= True
    posts.distance = "200km"
    posts.climb = "too much"
    posts.permName = "poopy"
    posts.organizer = "jerk"
    posts.permLink = ""
    return render(request, 'sanDiegoRandos/permanents.html',{'posts':posts})
