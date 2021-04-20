from django import forms
from .models import QuotePost, QuoteComment


class QuoteForm(forms.ModelForm):

    class Meta:
        model = QuotePost
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class QuoteCommentForm(forms.ModelForm):

    class Meta:
        model = QuoteComment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={'class:': 'form-control'})
        }
