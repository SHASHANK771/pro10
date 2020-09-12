from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.

from app.models import *

def display(request):
    #topics=Topic.objects.all()
    topics=Topic.objects.get(Topic_name='cricket')
    return render(request,'display.html', context={'topics':topics})


def display_webpage(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(name='shashank sen')
    #webpages=Webpage.objects.filter(name='Amy')
    #webpages=Webpage.objects.all().order_by('topic_name')
    #webpages=Webpage.objects.all().filter(topic_name='song') .order_by('url')
    #webpages=Webpage.objects.all()[0:5]
    #webpages=Webpage.objects.exclude(topic_name='cricket')
    #webpages=Webpage.objects.filter(name__startswith='j')
    #webpages=Webpage.objects.filter(name__endswith='n')
    #webpages=Webpage.objects.filter(name__contains='S')
    #webpages=Webpage.objects.all().order_by('name')#In Ascending order
    #webpages=Webpage.objects.all().order_by('-name')# In Descending order
    #webpages=Webpage.objects.all().order_by (Length('name'))# Ascending order based on length
    webpages=Webpage.objects.all().order_by (Length('name').desc())



    return render(request,'display_webpage.html', context={'webpages':webpages})





def display_Access(request):
    access=Access_Records.objects.all()
    #access=Access_Records.objects.filter(date='2000-10-12')
    #access=Access_Records.objects.filter(date__year='2009')
    #access=Access_Records.objects.filter(date__month='10')
    #access=Access_Records.objects.filter(date__day='12')
    #access=Access_Records.objects.filter(date__gt='1990-09-11')
    #access=Access_Records.objects.filter(date__year__gt='2009')
    #access=Access_Records.objects.filter(date__gte='2000-10-12')
    #access=Access_Records.objects.filter(date__lt='2000-10-12')
    access=Access_Records.objects.filter(date__lte='2000-10-12')
    


    return render(request,'display_Access.html', context={'access':access})    