from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Please input your review here (Max characters = 512)',
            'rows': 5,
            'cols': 50
        }))
    score = forms.ChoiceField(label="Rating", choices=[(x, x) for x in range(1, 6)])

    class Meta:
        model = Review
        fields = ['comment', 'score',]
