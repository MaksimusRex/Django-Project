from django import forms

from theProject2.crimes.models import Crime


class CrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = ['name', 'description', 'crime_type', 'points']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }