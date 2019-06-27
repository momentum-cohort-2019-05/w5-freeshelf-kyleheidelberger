from django import forms
from .models import Book, Author, Category

class FavForm(forms.Form):
    favorite = forms.BooleanField(required=False)
