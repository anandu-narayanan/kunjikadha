"""
Django forms for story creation.
"""
from django import forms


class StoryInitiationForm(forms.Form):
    """
    Form for initializing a new story with character, place, and theme.
    """
    THEME_CHOICES = [
        ('friendship', '👫 Friendship'),
        ('kindness', '❤️ Kindness'),
        ('adventure', '🗺️ Adventure'),
        ('learning', '📚 Learning'),
        ('courage', '💪 Courage'),
        ('family', '👨‍👩‍👧 Family'),
        ('nature', '🌿 Nature'),
        ('fun', '🎉 Fun & Games'),
    ]
    
    character = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'ഉദാ: കാക്ക',
            'class': 'form-control form-input'
        })
    )
    
    place = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'ഉദാ: വനം',
            'class': 'form-control form-input'
        })
    )
    
    theme = forms.ChoiceField(
        choices=THEME_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control form-input'
        })
    )


class StoryChoiceForm(forms.Form):
    """
    Form for selecting the next story choice.
    """
    choice = forms.ChoiceField(
        choices=[],  # Will be populated dynamically
        widget=forms.RadioSelect(attrs={
            'class': 'choice-radio'
        }),
        required=True
    )
    
    def __init__(self, *args, choices=None, **kwargs):
        super().__init__(*args, **kwargs)
        if choices:
            self.fields['choice'].choices = choices
