# __author__ == "Priya"

from django import forms

class ChatForm(forms.Form):
    user_input = forms.CharField(max_length=1000)
    myTextarea = forms.CharField(widget=forms.Textarea)