from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(label="Comment", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Please make a comment here. (Max characters = 512)',
            'rows': 4,
            'cols': 50
        }))
    score = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])

    class Meta:
        model = Review
        fields = ['comment', 'score',]
