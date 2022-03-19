from django import forms

class BookingForm(forms.Form):
    date = forms.DateField(label='date')
    time = forms.ChoiceField()
