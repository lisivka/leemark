from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','description',  'photo',  'status', 'media','genre','weight','height','buy_url',)


class PostForm2(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ('name', 'photo')
        fields = ('name', 'description','status', 'media','genre','weight','height','buy_url',)





