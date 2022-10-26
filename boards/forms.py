from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'placeholder': "What's in your mind?"}
    ), max_length=4000, help_text='The max length for your message should be 4000')
    # metaData

    class Meta:
        model = Topic
        fields = ['subject', 'message']
