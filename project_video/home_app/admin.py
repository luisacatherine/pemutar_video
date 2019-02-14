from django.contrib import admin
from .models import VideoClass

# Register your models here.
my_model = [VideoClass]
admin.site.register(my_model)