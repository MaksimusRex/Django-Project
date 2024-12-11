from datetime import datetime

from django import forms
from unicodedata import numeric

from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_type', 'make', 'model', 'year', 'license_plate', 'color']
        widgets = {
            'vehicle_type': forms.Select(),
            'color': forms.TextInput(attrs={'placeholder': 'Optional'}),
        }

class VehicleSearchForm(forms.Form):
    vehicle_type = forms.ChoiceField(
        choices=[('', 'All')] + [(t, t) for t in Vehicle.objects.values_list('vehicle_type', flat=True).distinct()],
        required=False,
        label="Vehicle Type",
    )
    model = forms.CharField(
        required=False,
        max_length=100,
        label="Model",
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by model',
            'class': 'search-input',
        })
    )
    year = forms.CharField(
        required=False,
        label="Year",
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by year',
            'class': 'search-input',
        })
    )
    color = forms.CharField(
        required=False,
        max_length=50,
        label="Color",
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by color',
            'class': 'search-input',
        })
    )

    def clean_year(self):
        year = self.cleaned_data.get('year')

        # Check if year is None, meaning the field was left empty (valid case)
        if year is None:
            return year

        # Explicitly check if the input is a number
        if not isinstance(year, int):
            raise forms.ValidationError("Year must be a number.")

        if year < 1900 or year > datetime.now().year:
            raise forms.ValidationError("Enter a valid year between 1800 and 2100.")

        return year