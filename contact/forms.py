from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(max_length=100, label='Email')
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea)
