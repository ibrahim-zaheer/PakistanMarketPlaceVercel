from django import forms

from .models import conversationMessage
class conversationMessageForm(forms.ModelForm):
    class Meta:
        model = conversationMessage
        fields = {'content',}