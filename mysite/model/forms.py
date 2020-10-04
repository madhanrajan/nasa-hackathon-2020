from django import forms
from .models import ImageModel

class ImageForm(forms.Form):
    image = forms.ImageField()