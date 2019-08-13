from django.contrib import admin
from .models import Destination, News, Destination_individual
# Register your models here.


admin.site.register(Destination)
admin.site.register(News)
admin.site.register(Destination_individual)