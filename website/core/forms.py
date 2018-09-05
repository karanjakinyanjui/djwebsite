from django import forms
from .models import MyPics


class PhotoForm(forms.ModelForm):
    class Meta:
        model = MyPics
        fields = ('file', )