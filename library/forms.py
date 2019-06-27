from django import forms
from .models import Book, Author, Category#, Favorite

class FavForm(forms.Form):
    favorite = forms.BooleanField(required=False)
