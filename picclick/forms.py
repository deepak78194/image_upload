from django import forms
from .models import Picclick

class PostForm(forms.ModelForm):

    class Meta:
        model = Picclick
        fields = ['title', 'image']