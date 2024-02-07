from django import forms
from .models import Comment, Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['coffee_experience']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_text']