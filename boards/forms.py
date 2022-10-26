from email import message
from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea, max_length=4000)
    # metaData

    class meta:
        model = Topic
        fields = ['subject', 'message']
