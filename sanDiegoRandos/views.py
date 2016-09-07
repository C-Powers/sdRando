from django.shortcuts import render
from .models import Permanents
from .permScrape import getPerms, scrapeSite
# Create your views here.

def home(request):
    return render(request, 'sanDiegoRandos/home.html', {})

def returnPermanents(request):
    posts = Permanents.objects.all()
    return render(request, 'sanDiegoRandos/permanents.html',{'posts':posts})

def gatherPermanents(request):
    '''
    location = models.CharField(max_length=200)
    freeRoute = models.BooleanField()
    distance = models.CharField(max_length=200)
    climb = models.CharField(max_length=200)
    permName = models.CharField(max_length=200)
    organizer = models.CharField(max_length=200)
    permLink = models.URLField(null=True)
    '''

    sdPermList = getPerms()

    for routes in sdPermList:
        print(routes)
        Permanents.objects.create(
        location = routes[0],
        freeRoute = routes[1],
        distance = routes[2],
        climb = routes[3],
        permName = routes[5],
        organizer = routes[6],
        permLink = routes[8])

    #need to remove duplicate rows in sqlite db
    '''
    for row in Permanents.objects.all():
        if Permanents.objects.filter(permName=row.permName).count() > 1:
            row.delete
            '''
    return render(request, 'sanDiegoRandos/gather.html', {})
