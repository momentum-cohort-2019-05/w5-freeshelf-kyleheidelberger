from django import forms
# from .models import Book, Favorite


class FavForm(forms.Form):
    favorited = forms.BooleanField(required=False)
