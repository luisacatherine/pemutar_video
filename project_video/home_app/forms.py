from django import forms
from .models import VideoClass

class PostForm(forms.ModelForm):
    class Meta:
        model = VideoClass
        fields = ('judul', 'videofile', 'deskripsi_video')