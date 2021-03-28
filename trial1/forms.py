from django import forms

class sendEmail(forms.Form):
    person_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
