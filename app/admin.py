from django.contrib import admin

# Register your models here.

from app.models import Topic,Webpage,Access_Records


admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Access_Records)