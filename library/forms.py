from django import forms
# from .models import BookComment


class FavForm(forms.Form):
    favorited = forms.BooleanField(required=False)

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = BookComment
