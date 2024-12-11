from django import forms
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
    )
    year = forms.IntegerField(
        required=False,
        label="Year",
    )
    color = forms.CharField(
        required=False,
        max_length=50,
        label="Color",
    )