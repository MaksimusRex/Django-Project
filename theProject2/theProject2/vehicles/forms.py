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