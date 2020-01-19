from django import forms
from .models import Inspiration


class InspirationSharingForm(forms.ModelForm):

    class Meta:
        model = Inspiration
        fields = ('title', 'content', 'published_date')