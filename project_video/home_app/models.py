from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import FileField
from django.db.models import IntegerField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.utils import timezone

# Create your models here.

class VideoClass(models.Model):
    judul = models.CharField(max_length=100)
    videofile = models.FileField(upload_to='videos', null=True, verbose_name="")
    update_at = models.DateTimeField(auto_now=True)
    deskripsi_video = models.TextField()
    def __str__(self):
        return self.judul