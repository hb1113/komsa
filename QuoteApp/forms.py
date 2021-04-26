from django import forms
from .models import QuotePost, QuoteComment


class QuoteForm(forms.ModelForm):

    class Meta:
        model = QuotePost
        fields = ['text', 'tag']

        widgets = {
            "text": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'text',
            }),
            "tag": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'tags',
            })
        }


class QuoteCommentForm(forms.ModelForm):

    class Meta:
        model = QuoteComment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={'class:': 'form-control'})
        }
