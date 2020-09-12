from pathlib import Path
import os

os.environ.setdefault('DJANGO_SETTINGO_MODULE','pro10.settings')

import django
django.setup()

from app.models import *
from faker import Faker


def Add_topics():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def Add_webpage(webpagename,url):
    topic_name=Add_topics()
    w=Webpage.objects.get_or_create(topic_name=topic_name, name=webpagename,url=url)[0]
    w.save()
    return w


def Access_Records(models.Model):
    name=Add_webpage(webpagename,url)
    a=Access_Records.objects.get_or_create(name=name,date=date)[0]
    a.save()



for i in range(10):
    fakename=f.first_name()
    fakeurl=f.url()
    fakedate=f.date()
    Add_records(fakename,fakeurl,fakedate)
