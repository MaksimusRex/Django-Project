from django import forms
from .models import Prison

class PrisonCreationForm(forms.ModelForm):
    class Meta:
        model = Prison
        fields = ['name', 'capacity', 'cells', 'security_level', 'picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter prison name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter capacity'}),
            'security_level': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Prison Name',
            'location': 'Location',
            'capacity': 'Capacity',
            'security_level': 'Security Level',
        }

class PrisonSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by name',
            'class': 'search-input',
        })
    )