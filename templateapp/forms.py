from django import forms
from .models import CommentModel

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment']