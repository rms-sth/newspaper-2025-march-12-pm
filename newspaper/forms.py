from django import forms
from newspaper.models import Comment, Newsletter


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"
